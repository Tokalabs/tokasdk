"""This module has methods to manage the connections in Toka controller inventory.

This module has methods for the following -
 - Adding a direct connections between devices in the inventory
 - Searching direct connections within the inventory
 - Delete a direct connection from the inventory

    Compatible with the following Toka controller version(s) -
    >= 1.4.8.0

    Compatible with the following Python version(s) -
    2.7, 3.4+

    Require(s) the following third party/external Python modules -
    None
    
    Uses the following Toka SDK API client sample(s) -
    A successfully configured and authenticated Toka SDK configuration object 

    Typical usage example:
    Refer to launch_sample.py

"""

# Standard Python Module Imports
import sys
import traceback

# Third Party Module Imports
# None

# Toka SDK Module Imports
import tokasdk
from tokasdk.rest import ApiException

def add_connection(toka_api_configuration, src_hostname, src_port_id, target_hostname, target_port_id):
    """Connect the specified devices on the specified ports.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object
        src_hostname (str): Hostname of the source device to be connected
        src_port_id (str): Port id of the source device to be connected
        target_hostname (str): Hostname of the target device to be connected
        target_port_id (str): Port id of the target device to be connected
    
    Returns:
        str: connection id of the newly created connection if successful, None otherwise
    """
    if (None == toka_api_configuration or 
        None == src_hostname or 0 == len(src_hostname.strip()) or 
        None == src_port_id or 0 == len(src_port_id.strip()) or
        None == target_hostname or 0 == len(target_hostname.strip()) or 
        None == target_port_id or 0 == len(target_port_id.strip())):
        print('[inventory_conn_mgmt][add_connection] Invalid input specified. '
              'Either the Toka API configuration object or the source '
              'hostname or the source port id or the target hostname '
              'or the target port id is null or empty. Returning failure')
        return None
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_CONN_ID = 'connectionId'

    try:
        add_connection_request = tokasdk.AddConnectionsRequest(
                                    source_host=src_hostname.strip(), 
                                    target_host=target_hostname.strip(), 
                                    source_port_id=src_port_id.strip(), 
                                    target_port_id=target_port_id.strip())

        toka_connections_api_instance = tokasdk.ConnectionsApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_connections_api_instance.add_connections(
                        add_connections_request=add_connection_request)
        
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower() and
            TOKA_API_RESPONSE_KEY_CONN_ID in api_response.additional_details and
            None != api_response.additional_details[TOKA_API_RESPONSE_KEY_CONN_ID]):
            # Connection added successfully...
            return api_response.additional_details[TOKA_API_RESPONSE_KEY_CONN_ID]
        else:
            print('[inventory_conn_mgmt][add_connection] Failed to '
                    'add the connection. Returniing failure. '
                    'Error message ' + api_response.message)
            return None
    except ApiException as exc:
        print('[inventory_conn_mgmt][add_connection] APIException '
                ' occurred while attempting to add the connection. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message - {2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return None
    except Exception as exc:
        print('[inventory_conn_mgmt][add_connection] Exception '
              ' occurred while attempting to add the connection. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return None    


def search_direct_connections(toka_api_configuration, hostname=None):
    """Search for connections in the Toka controller inventory based on the specified filter(s).
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object
        hostname (str, optional): Hostname to be used for searching and filtering 
                                    direct connections. Defaults to None.
    
    Returns:
        list: List of connections matching the specified filters if successful,
              None otherwise
    """
    if None == toka_api_configuration:
        print('[inventory_conn_mgmt][search_direct_connections] Invalid input specified. The '
        'Toka API configuration object is null or empty. Returning failure')
        return None
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_DIRECT_CONN_LIST = 'directConnectionsList'

    try:
        toka_connections_api_instance = tokasdk.ConnectionsApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_connections_api_instance.get_connections_and_filter(
                                hostname=hostname)
                
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower() and 
            None != api_response.additional_details):
            if (TOKA_API_RESPONSE_KEY_DIRECT_CONN_LIST in api_response.additional_details and
            None != api_response.additional_details[TOKA_API_RESPONSE_KEY_DIRECT_CONN_LIST]):
                # Atleast 1 connection matched the search filter...
                return api_response.additional_details[TOKA_API_RESPONSE_KEY_DIRECT_CONN_LIST]
            else:
                # No connections matched the search filter. Return an empty list
                return []
        else:
            print('[inventory_conn_mgmt][search_direct_connections] Failed to '
                    'retrieve devices. Returniing failure. '
                    'Error message ' + api_response.message)
            return None
    except ApiException as exc:
        print('[inventory_conn_mgmt][search_direct_connections] APIException '
                ' occurred while attempting to add a network device. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message - {2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return None
    except Exception as exc:
        print('[inventory_conn_mgmt][search_direct_connections] Exception '
              ' occurred while attempting to add a network device. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return None    

def delete_connection(toka_api_configuration, connection_id):
    """Delete a conenction from the Toka controller inventory.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object
        connection_id (str): Connection id for the connection to be deleted
    
    Returns:
        bool: True if the connection was deleted successfully, False otherwise
    """
    if (None == toka_api_configuration or 
        None == connection_id or 0 == len(connection_id.strip())):
        print('[inventory_device_mgmt][delete_connection] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the hostname is null or empty. Returning failure')
        return False
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'

    try:
        toka_connections_api_instance = tokasdk.ConnectionsApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_connections_api_instance.delete_connection(
                            connectionid=connection_id)
        
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower()):
            # Connection was deleted successfully...
            return True
        else:
            print('[inventory_device_mgmt][delete_connection] Failed to '
                    'delete the connection. Returniing failure. '
                    'Error message ' + api_response.message)
            return False
    except ApiException as exc:
        print('[inventory_device_mgmt][delete_connection] APIException '
                ' occurred while attempting to delete the connection. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message - {2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[inventory_device_mgmt][delete_connection] Exception '
              ' occurred while attempting to delete the connection. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    
