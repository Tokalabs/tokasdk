"""This module has methods to setup and configure the Toka SDK API client.

Setup/Configuring the Toka SDK API client requires configuring the Toka SDK
controller fully qualified domain name (FQDN) or IP address as well as 
other options such as SSL verification settings.

    Compatible with the following Toka controller version(s) -
    >= 1.4.8.0

    Compatible with the following Python version(s) -
    2.7, 3.4+

    Require(s) the following third party/external Python modules -
    None
    
    Uses the following Toka SDK API client sample(s) -
    None

    Typical usage example:
    toka_sdk_config = setup.setup_steps.configure_api_client(toka_ip)
    if None === toka_sdk_config:
        # Could not successfully configure the Toka SDK API client
        return

    # Configured the Toka SDK API client successfully, next 
    # attempt to login to the Toka controller

    toka_api_token = setup.setup_steps.login(toka_sdk_config, toka_user, toka_pw)
    if None === toka_api_token:
        # Could not successfully login to the Toka controller
        return

    # Logged in to the Toka SDK API client successfully, continue
    # to interact with the Toka controller...

"""

# Standard Python Module Imports
import sys
import traceback

# Third Party Module Imports
# None

# Toka SDK Module Imports
import tokasdk
from tokasdk.rest import ApiException

def configure_api_client(toka_controller_name_ip, disable_ssl_cert_checks = False):
    """Setup the Toka SDK client.
    
    Args:
        toka_controller_name_ip (str): Hostname or IP address of the 
                                        Toka controller.
        disable_ssl_cert_checks (bool, optional): Disable SSL verification
                                        checks while communicating with the 
                                        Toka controller. Defaults to False.
    
    Returns:
        tokasdk.Configuration: Toka SDK configuration object is successful, 
                               None if failed.
    """
    if (None == toka_controller_name_ip or 
        0 == len(toka_controller_name_ip.strip())):
        print('[setup_steps][configure_api_client] Invalid Toka '
                        'controller name or IP specified. Returning '
                        'failure')
        return None
    
    TOKA_API_ENDPOINT_PROTOCOL = 'https'
    TOKA_API_ENDPOINT_PATH_PREFIX = '/tokalabs/api'
    CHR_FORWARD_SLASH = '/'
    CHR_COLON = ':'

    try:
        toka_controller_api_endpoint_url_prefix = (
            TOKA_API_ENDPOINT_PROTOCOL + 
            CHR_COLON + CHR_FORWARD_SLASH + CHR_FORWARD_SLASH +
            toka_controller_name_ip.strip() +
            TOKA_API_ENDPOINT_PATH_PREFIX
        )

        toka_api_configuration = tokasdk.Configuration()
        #toka_api_configuration.api_key['Authorization'] = 'YOUR_API_KEY'
        toka_api_configuration.host = toka_controller_api_endpoint_url_prefix

        if True == disable_ssl_cert_checks:
            toka_api_configuration.assert_hostname = False
            toka_api_configuration.verify_ssl = False
    
        return toka_api_configuration
    except ApiException as exc:
        print('[setup_steps][configure_api_client] APIException '
                        'while configuring Toka API client. '
                        'Returning failure. APIException status- {0}, '
                        'reason - {1}, message -{2}, response body - {3}'
                        .format(exc.status, exc.reason, exc.message, exc.body))
        return None
    except Exception as exc:
        print('[setup_steps][configure_api_client] Exception while '
                        'configuring Toka API client. Returning failure. '
                        'Exception message - {0}'.format(exc.message))
        # traceback.print_exc()            
        return None

    
def login(toka_api_configuration, username, password):
    """Log into the Toka controller.

    If the provided username and password combination is valid, then 
    thie function also set the server returned API token in the Toka 
    API configuration object so that all further operations attempted
    using the Toka SDK client will automatically use the API token.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        username (str): Username to be used for login.
        password (str): Password to be used for login.
    
    Returns:
        str: API token if successful, None if failed.
    """
    if (None == toka_api_configuration or 
        None == username or 0 == len(username.strip()) or 
        None == password or 0 == len(password.strip())):
        print('[setup_steps][login] Invalid input specified. Either the '
        'Toka API configuration object or the username or the '
        'password is null or empty. Returning failure')
        return None
    
    TOKA_API_REQUEST_HEADER_TOKEN = 'Authorization'
    TOKA_API_RESPONSE_KEY_TOKEN = 'token'
    TOKA_API_RESPONSE_SUCCESS = 'Success'

    try:
        login_request = tokasdk.LoginRequest(username=username.strip(), 
                                            password=password.strip())

        # Login to the Toka controller and obtain a valid Toka API token
        toka_login_api_instance = tokasdk.LoginApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_response = toka_login_api_instance.login(
                                    login_request=login_request)
        
        if (None != api_response.status and 
            TOKA_API_RESPONSE_SUCCESS.lower() == api_response.status.lower() and 
            None != api_response.additional_details and 
            TOKA_API_RESPONSE_KEY_TOKEN in api_response.additional_details and 
            TOKA_API_RESPONSE_KEY_TOKEN in api_response.additional_details[TOKA_API_RESPONSE_KEY_TOKEN]):
            # Login succeeded, Set the returned api token as the request header
            toka_api_configuration.api_key[TOKA_API_REQUEST_HEADER_TOKEN] = api_response.additional_details[TOKA_API_RESPONSE_KEY_TOKEN][TOKA_API_RESPONSE_KEY_TOKEN]
            return toka_api_configuration.api_key[TOKA_API_REQUEST_HEADER_TOKEN]
        else:
            print('[setup_steps][login] Login failed. Returniing failure. '
                    'Login failed message ' + api_response.message)
            return None
    except ApiException as exc:
        print('[setup_steps][login] APIException while attempting to login. '
                        'Returning failure. APIException status- {0}, '
                        'reason - {1}, message -{2}, response body - {3}'
                        .format(exc.status, exc.reason, exc.message, exc.body))
        return None
    except Exception as exc:
        print('[setup_steps][login] Exception while attempting to login. '
                        'Returning failure. Exception message - {0}'
                        .format(exc.message))
        # traceback.print_exc()            
        return None

def fetch_username_token_from_configuration_object(toka_api_configuration):
    """Fetch the username and token from the API token
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
    
    Returns:
        tuple: a tuple whose firse element is the username and the second is the token if successful,
                None otherwise
    """
    TOKA_API_REQUEST_HEADER_TOKEN = 'Authorization'
    CHR_FORWARD_SLASH = '/'

    if (None == toka_api_configuration or
        None == toka_api_configuration.api_key or 
        TOKA_API_REQUEST_HEADER_TOKEN not in toka_api_configuration.api_key or
        None == toka_api_configuration.api_key[TOKA_API_REQUEST_HEADER_TOKEN] or
        0 == len(toka_api_configuration.api_key[TOKA_API_REQUEST_HEADER_TOKEN].strip())):
        print('[setup_steps][fetch_username_token_from_configuration_object] '
            'Either the Toka API configuration object or the API token '
            'is null or empty. Returning failure')
        return None
    
    try:
        toka_api_token_components = (toka_api_configuration
                .api_key[TOKA_API_REQUEST_HEADER_TOKEN]
                .strip().split(CHR_FORWARD_SLASH))
        if 1 >= len(toka_api_token_components):
            # The username and token are seperated using the '/' character
            print('[setup_steps][fetch_username_token_from_configuration_object] '
                'Invalid API token. Does not seem to contain username and '
                'token. Returning failure')
            return None
        toka_api_username = toka_api_token_components[0]
        toka_api_token = CHR_FORWARD_SLASH.join(toka_api_token_components[1:])
        return (toka_api_username, toka_api_token)
    except Exception as exc:
        print('[setup_steps][fetch_username_token_from_configuration_object] '
            'Exception while attempting to fetch the username and token from '
            'the Toka SDK configuration object. Returning failure. '
            'Exception message - {0}'.format(exc.message))
        # traceback.print_exc()            
        return None

