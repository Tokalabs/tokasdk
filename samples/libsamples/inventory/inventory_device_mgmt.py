"""This module has methods to manage the devices in Toka controller inventory.

This module has methods for the following -
 - Adding a network device to the inventory
 - Searching devices within the inventory
 - Delete a device from the inventory

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

def add_network_device(toka_api_configuration, hostname, device_type='ap', device_asset_id='', device_vendor='', device_ports={}):
    """Add a network device to the Toka controller inventory.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        hostname (str): Hostname of the device to be added.
        device_type (str, optional): Type of device to be added. Defaults to 'ap'.
        device_asset_id (str, optional): Asset id of the device to be added. Defaults to ''.
        device_vendor (str, optional): Vendor of the device to be added. Defaults to ''.
        device_ports (dict, optional): Ports of the device to be added. Defaults to {}.
    
    Returns:
        bool: True if the network device was added successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == hostname or 0 == len(hostname.strip()) or 
        None == device_type or 0 == len(device_type.strip())):
        print('[inventory_device_mgmt][add_network_device] Invalid input specified. Either the '
        'Toka API configuration object or the hostname or the '
        'device type is null or empty. Returning failure')
        return False
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'

    try:
        add_network_device_request = tokasdk.AddNetworkDeviceRequest(
                                            hostname=hostname,
                                            device_type=device_type, 
                                            physical_port_connections=device_ports, 
                                            asset_id=device_asset_id, 
                                            vendor=device_vendor)

        toka_inv_mgmt_api_instance = tokasdk.InventoryManagementApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_inv_mgmt_api_instance.add_network_device(
                        add_network_device_request=add_network_device_request)
        
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower()):
            # Device was added successfully...
            return True
        else:
            print('[inventory_device_mgmt][add_network_device] Failed to '
                    'add the network device. Returniing failure. '
                    'Error message ' + str(api_response))
            return False
    except ApiException as exc:
        print('[inventory_device_mgmt][add_network_device] APIException '
                ' occurred while attempting to add a network device. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[inventory_device_mgmt][add_network_device] Exception '
              ' occurred while attempting to add a network device. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    


def search_devices(toka_api_configuration, hostname=None, device_type=None, device_reservation_status=None):
    """Search for devices in the Toka controller inventory based on the specified filters.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object
        hostname (str, optional): Hostname to be used for searching and filtering devices. 
                                     Defaults to None.
        device_type (str, optional): Device type to be used for searching and filtering devices. 
                                     Defaults to None.
        device_reservation_status (str, optional): Device reservation status to be used for 
                                     searching and filtering devices. Defaults to None.
    
    Returns:
        list: List of devices matching the specified filters if successful,
              None otherwise.
    """
    if None == toka_api_configuration:
        print('[inventory_device_mgmt][search_devices] Invalid input specified. The '
        'Toka API configuration object is null or empty. Returning failure')
        return None
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_DEVICELIST = 'devicesList'

    try:
        toka_inv_mgmt_api_instance = tokasdk.InventoryManagementApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_inv_mgmt_api_instance.get_inventory_devices(
                            hostname=hostname,
                            device_type=device_type,
                            reservation_status=device_reservation_status
        )
                
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower() and 
            None != api_response.additional_details):
            if (TOKA_API_RESPONSE_KEY_DEVICELIST in api_response.additional_details and
            None != api_response.additional_details[TOKA_API_RESPONSE_KEY_DEVICELIST]):
                # Atleast 1 device matched the search filter...
                return api_response.additional_details[TOKA_API_RESPONSE_KEY_DEVICELIST]
            else:
                # No devices matched the search filter. Return an empty list
                return []
        else:
            print('[inventory_device_mgmt][search_devices] Failed to '
                    'retrieve devices. Returniing failure. '
                    'Error message ' + str(api_response))
            return None
    except ApiException as exc:
        print('[inventory_device_mgmt][add_network_device] APIException '
                ' occurred while attempting to retrieve devices. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message - {2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return None
    except Exception as exc:
        print('[inventory_device_mgmt][add_network_device] Exception '
              ' occurred while attempting to retrieve devices. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return None    

def delete_device(toka_api_configuration, hostname=None):
    """Delete a device from the Toka controller inventory.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        hostname (str): Hostname of the device to be deleted.
    
    Returns:
        bool: True if the device was deleted successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == hostname or 0 == len(hostname.strip())):
        print('[inventory_device_mgmt][delete_device] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the hostname is null or empty. Returning failure')
        return False
    
    TOKA_API_RESPONSE_SUCCESS = 'Success'

    try:
        toka_inv_mgmt_api_instance = tokasdk.InventoryManagementApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_inv_mgmt_api_instance.delete_inventory_device(
                            hostname=hostname,
                            delete_from_server=False)
        
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower()):
            # Device was deleted successfully...
            return True
        else:
            print('[inventory_device_mgmt][delete_device] Failed to '
                    'delete the device. Returniing failure. '
                    'Error message ' + str(api_response))
            return False
    except ApiException as exc:
        print('[inventory_device_mgmt][delete_device] APIException '
                ' occurred while attempting to delete the device. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[inventory_device_mgmt][delete_device] Exception '
              ' occurred while attempting to delete the device. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    
