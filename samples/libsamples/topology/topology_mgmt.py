"""This module has methods to manage the topologies in Toka controller.

This module has methods for the following -
 - Creating a new topology
 - Searching topologies
 - Delete a topology
 - Reserve a topology
 - Release a topology

    Compatible with the following Toka controller version(s) -
    >= 1.4.7.1

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

# Toka SDK Samples Imports
import libsamples.setup.setup_steps

def create_topology(toka_api_configuration, topo_name, list_of_devices_to_add_to_topo, list_of_indirect_connections_to_be_added_to_topo=[]):
    """Create a topology on the Toka controller inventory.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        list_of_devices_to_add_to_topo (list): List of devices to be added to the topology.
        list_of_indirect_connections_to_be_added_to_topo (list): List of indirect connections 
                                                to be added to the topology. Defaults to [].

    Returns:
        bool: True if the topology was created successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == topo_name or 0 == len(topo_name.strip()) or 
        None == list_of_devices_to_add_to_topo or 
        False == isinstance(list_of_devices_to_add_to_topo, list) or
        0 == len(list_of_devices_to_add_to_topo) or 
        False == isinstance(list_of_indirect_connections_to_be_added_to_topo, list)):
        print('[topology_mgmt][create_topology] Invalid input specified. Either the '
        'Toka API configuration object or the topology name or the '
        'list of devices to be added to the topology '
        'is null or empty. Returning failure')
        return False
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'

    try:
        create_topology_request = tokasdk.AddTopologyRequest(
                                        name=topo_name,
                                        devices=list_of_devices_to_add_to_topo,
                                        indirect_connections=list_of_indirect_connections_to_be_added_to_topo
        )
        toka_topology_api_instance = tokasdk.TopologyApi(
            tokasdk.ApiClient(toka_api_configuration))
        
        api_response = toka_topology_api_instance.add_topology(
                        add_topology_request=create_topology_request)

        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower()):
            # Topology was created successfully...
            return True
        else:
            print('[topology_mgmt][create_topology] Failed to '
                    'create the topology. Returniing failure. '
                    'Error message ' + str(api_response))
            return False
    except ApiException as exc:
        print('[topology_mgmt][create_topology] APIException '
                ' occurred while attempting to create topology. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[topology_mgmt][create_topology] Exception '
              ' occurred while attempting to create topology. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    


def search_topologies(toka_api_configuration, topo_name=None, topo_reservation_status=None):
    """Search for topologies in the Toka controller inventory based on the specified filters.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str, optional): Topology name to be used for searching and filtering topologies. 
                                     Defaults to None.
        topo_reservation_status (str, optional): Topology reservation status to be used for 
                                     searching and filtering topologies. Defaults to None.
    
    Returns:
        list: List of topologies matching the specified filters if successful,
              None otherwise.
    """
    if None == toka_api_configuration:
        print('[topology_mgmt][search_topologies] Invalid input specified. The '
        'Toka API configuration object is null or empty. Returning failure')
        return None
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_TOPOLOGYLIST = 'topologiesList'

    try:
        toka_topology_api_instance = tokasdk.TopologyApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_topology_api_instance.get_topology(
                            name=topo_name,
                            reservation_status=topo_reservation_status
        )
                
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower() and 
            None != api_response.additional_details):
            if (TOKA_API_RESPONSE_KEY_TOPOLOGYLIST in api_response.additional_details and
            None != api_response.additional_details[TOKA_API_RESPONSE_KEY_TOPOLOGYLIST]):
                # Atleast 1 topology matched the search filter...
                return api_response.additional_details[TOKA_API_RESPONSE_KEY_TOPOLOGYLIST]
            else:
                # No topologies matched the search filter. Return an empty list
                return []
        else:
            print('[[topology_mgmt][search_topologies] Failed to '
                    'retrieve topologies. Returniing failure. '
                    'Error message ' + str(api_response))
            return None
    except ApiException as exc:
        print('[topology_mgmt][search_topologies] APIException '
                ' occurred while attempting to retrieve topologies. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message - {2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return None
    except Exception as exc:
        print('[topology_mgmt][search_topologies] Exception '
              ' occurred while attempting to retrieve topologies. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return None    

def delete_topology(toka_api_configuration, topo_name=None):
    """Delete a topology from the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology to be deleted.
    
    Returns:
        bool: True if the topology was deleted successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == topo_name or 0 == len(topo_name.strip())):
        print('[topology_mgmt][delete_topology] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty. Returning failure')
        return False
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'

    try:
        toka_topology_api_instance = tokasdk.TopologyApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_topology_api_instance.delete_topology(
                                topologyname=topo_name
        )
        
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower()):
            # Topology was deleted successfully...
            return True
        else:
            print('[topology_mgmt][delete_topology] Failed to '
                    'delete the topology. Returniing failure. '
                    'Error message ' + str(api_response))
            return False
    except ApiException as exc:
        print('[topology_mgmt][delete_topology] APIException '
                ' occurred while attempting to delete the topology. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[topology_mgmt][delete_topology] Exception '
              ' occurred while attempting to delete the topology. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    

def reserve_topology(toka_api_configuration, topo_name=None):
    """Reserve a topology on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology to be released.
    
    Returns:
        bool: True if the topology was released successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == topo_name or 0 == len(topo_name.strip())):
        print('[topology_mgmt][reserve_topology] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty. Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        
        toka_topology_api_instance = tokasdk.TopologyApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.reserve_topology_v1(
                        topology_name=topo_name,
                        username=tuple_user_token[0],
                        api_token=tuple_user_token[1])
                                
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Topology was reserved successfully...
            return True
        else:
            print('[topology_mgmt][reserve_topology] Failed to '
                    'reserve the topology. Returniing failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[topology_mgmt][reserve_topology] APIException '
                ' occurred while attempting to reserve the topology. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[topology_mgmt][reserve_topology] Exception '
              ' occurred while attempting to reserve the topology. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    


def release_topology(toka_api_configuration, topo_name=None):
    """Release a topology on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology to be released.
    
    Returns:
        bool: True if the topology was released successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == topo_name or 0 == len(topo_name.strip())):
        print('[topology_mgmt][release_topology] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty. Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        
        toka_topology_api_instance = tokasdk.TopologyApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.release_topology_v1(
                        topology_name=topo_name,
                        username=tuple_user_token[0],
                        api_token=tuple_user_token[1])
                                
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Topology was released successfully...
            return True
        else:
            print('[topology_mgmt][release_topology] Failed to '
                    'release the topology. Returniing failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[topology_mgmt][release_topology] APIException '
                ' occurred while attempting to release the topology. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[topology_mgmt][release_topology] Exception '
              ' occurred while attempting to reserve the topology. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    
