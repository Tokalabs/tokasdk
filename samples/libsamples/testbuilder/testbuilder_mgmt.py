"""This module has methods to manage the topologies in Toka controller.

This module has methods for the following -
 - Run a test
 - Abort a test
 - Pause a test
 - Resume a test
 - Get run status of a test
 - Run a test suite
 - Abort a test suite
 - Get run status of a test suite
 - Clone a test suite

    Compatible with the following Toka controller version(s) -
    >= 1.4.7.1

    Compatible with the following Python version(s) -
    2.7, 3.4+

    Require(s) the following third party/external Python modules -
    None
    
    Uses the following Toka SDK API client sample(s) -
    A successfully configured and authenticated Toka SDK configuration object 
    A successfully reserved topology

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


def run_test(toka_api_configuration, topo_name=None, test_suite_name=None, test_id=None):
    """Run a test on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test to be run.
        test_suite_name (str): Name of the test suite that contains the test to be run.
        test_id (str): Id of the test to be run.

    Returns:
        bool: True if the test was started successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == topo_name or 0 == len(topo_name.strip()) or
        None == test_suite_name or 0 == len(test_suite_name.strip()) or
        None == test_id or 0 == len(test_id.strip())):
        print('[testbuilder_mgmt][run_test] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name or the test suite name or the test id '
              'is null or empty. Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Start'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        
        toka_testbuilder_api_instance = tokasdk.TestBuilderApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_testbuilder_api_instance.run_test_v1(
                        topology_name=topo_name,
                        suite_name=test_suite_name,
                        testcase_id=test_id,
                        username=tuple_user_token[0],
                        api_token=tuple_user_token[1])
                                
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Test was started successfully...
            return True
        else:
            print('[testbuilder_mgmt][run_test] Failed to '
                    'run the test. Returniing failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][run_test] APIException '
                ' occurred while attempting to run the test. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][run_test] Exception '
              ' occurred while attempting to run the test. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    


def abort_test(toka_api_configuration, topo_name=None, test_suite_name=None, test_id=None):
    """Abort an already running test on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test to be aborted.
        test_suite_name (str): Name of the test suite that contains the test to be aborted.
        test_id (str): Id of the test to be aborted.

    Returns:
        bool: True if the test was aborted successfully, False otherwise.
    """
    if ( None == toka_api_configuration or 
         None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_name or 0 == len(test_suite_name.strip()) or 
         None == test_id or 0 == len(test_id.strip())):
        print('[testbuilder_mgmt][abort_test] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty or the test_suite_name is null or empty or '
              'the test_id is null or empty. Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Aborted'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False

        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.abort_test_v1(
                                                    topology_name=topo_name, 
                                                    suite_name=test_suite_name,
                                                    testcase_id=test_id,
                                                    username=tuple_user_token[0], 
                                                    api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Test was aborted uccessfully...
            return True
        else:
            print('[testbuilder_mgmt][abort_test] Failed to '
                    'abort the test. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][abort_test] APIException '
                ' occurred while attempting to abort the test. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][abort_test] Exception '
              ' occurred while attempting to abort the test. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    

def pause_test(toka_api_configuration, topo_name=None, test_suite_name=None, test_id=None):
    """Pause an already running test on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test to be paused.
        test_suite_name (str): Name of the test suite that contains the test to be paused.
        test_id (str): Id of the test to be paused.

    Returns:
        bool: True if the test was paused successfully, False otherwise.
    """
    if ( None == toka_api_configuration or None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_name or 0 == len(test_suite_name.strip()) or 
         None == test_id or 0 == len(test_id.strip()) ):
        print('[testbuilder_mgmt][pause_test] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty or '
              'the test_suite_name is null or empty. or'
              'the test_id is null or empty. or'
              ' Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Paused'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.pause_test_v1(
                                                    topology_name=topo_name, 
                                                    suite_name=test_suite_name, 
                                                    testcase_id=test_id, 
                                                    username=tuple_user_token[0], 
                                                    api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Test was paused successfully...
            return True
        else:
            print('[testbuilder_mgmt][pause_test] Failed to '
                    'pause the test. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][pause_test] APIException '
                ' occurred while attempting to pause the test. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][pause_test] Exception '
              ' occurred while attempting to pause the test. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False


def resume_test(toka_api_configuration, topo_name=None, test_suite_name=None, test_id=None):
    """Resume an already paused test on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test to be resumed.
        test_suite_name (str): Name of the test suite that contains the test to be resumed.
        test_id (str): Id of the test to be resumed.

    Returns:
        bool: True if the test was resumed successfully, False otherwise.
    """
    if ( None == toka_api_configuration or None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_name or 0 == len(test_suite_name.strip()) or 
         None == test_id or 0 == len(test_id.strip()) ):
        print('[testbuilder_mgmt][resume_test] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty or '
              'the test_suite_name is null or empty. or'
              'the test_id is null or empty. or'
              ' Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Resumed'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.resume_test_v1(
                                                    topology_name=topo_name, 
                                                    suite_name=test_suite_name, 
                                                    testcase_id=test_id, 
                                                    username=tuple_user_token[0], 
                                                    api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Test was resumed successfully...
            return True
        else:
            print('[testbuilder_mgmt][resume_test] Failed to '
                    'resume the test. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][resume_test] APIException '
                ' occurred while attempting to resume the test. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][resume_test] Exception '
              ' occurred while attempting to resume the test. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False


def fetch_test_status(toka_api_configuration, topo_name=None, test_suite_name=None, test_id=None):
    """Retrieve the run status of the test on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test whose run status is to be retrieved.
        test_suite_name (str): Name of the test suite that contains the test whose run status is to be retrieved.
        test_id (str): Id of the test whose run status is to be retrieved.

    Returns:
        str: Test run status if successful, None otherwise.
    """
    if ( None == toka_api_configuration or None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_name or 0 == len(test_suite_name.strip()) or 
         None == test_id or 0 == len(test_id.strip()) ):
        print('[testbuilder_mgmt][fetch_test_status] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty or '
              'the test_suite_name is null or empty. or'
              'the test_id is null or empty. or'
              ' Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Success'    
    TOKA_API_RESPONSE_KEY_STATUS = 'status'
    TOKA_API_RESPONSE_KEY_TEST_STATUS = 'test_case_status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.get_test_status_v1(
                                                        topology_name=topo_name, 
                                                        suite_name=test_suite_name, 
                                                        testcase_id=test_id, 
                                                        username=tuple_user_token[0], 
                                                        api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower()) and
            True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_TEST_STATUS) and 
            None != api_v1_response.test_case_status ):
            # Test run status was retrieved successfully
            return api_v1_response.test_case_status
        else:
            print('[testbuilder_mgmt][fetch_test_status] Failed to '
                    'retrieve the test run status. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][fetch_test_status] APIException '
                ' occurred while attempting to retrieve the test run status. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][fetch_test_status] Exception '
              ' occurred while attempting to retrieve the test run status. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False   

def run_test_suite(toka_api_configuration, topo_name=None, test_suite_name=None):
    """Run a test suite on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test suite to be run.
        test_suite_name (str): Name of the test suite to be run.

    Returns:
        bool: True if the test suite was started successfully, False otherwise.
    """
    if (None == toka_api_configuration or 
        None == topo_name or 0 == len(topo_name.strip()) or
        None == test_suite_name or 0 == len(test_suite_name.strip())):
        print('[testbuilder_mgmt][run_test_suite] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name or the test suite name  '
              'is null or empty. Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Start'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        
        toka_testbuilder_api_instance = tokasdk.TestBuilderApi(
                                tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_testbuilder_api_instance.run_test_suite_v1(
                        topology_name=topo_name,
                        suite_name=test_suite_name,
                        username=tuple_user_token[0],
                        api_token=tuple_user_token[1])
                                
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Test suite was started successfully...
            return True
        else:
            print('[testbuilder_mgmt][run_test_suite] Failed to '
                    'run the test suite. Returniing failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][run_test_suite] APIException '
                ' occurred while attempting to run the test suite. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][run_test_suite] Exception '
              ' occurred while attempting to run the test suite. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    

def abort_test_suite(toka_api_configuration, topo_name=None, test_suite_name=None):
    """Abort an already running test suite on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test suite to be aborted.
        test_suite_name (str): Name of the test suite to be aborted.

    Returns:
        bool: True if the test suite was aborted successfully, False otherwise.
    """
    if ( None == toka_api_configuration or 
         None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_name or 0 == len(test_suite_name.strip())):
        print('[testbuilder_mgmt][abort_test_suite] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty or the test_suite_name is null or empty. '
              'Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Aborted'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False

        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.abort_test_suite_v1(
                                                    topology_name=topo_name, 
                                                    suite_name=test_suite_name,
                                                    username=tuple_user_token[0], 
                                                    api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
            # Test suite was aborted uccessfully...
            return True
        else:
            print('[testbuilder_mgmt][abort_test_suite] Failed to '
                    'abort the test suite. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][abort_test_suite] APIException '
                ' occurred while attempting to abort the test suite. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][abort_test_suite] Exception '
              ' occurred while attempting to abort the test suite. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    

def fetch_test_suite_status(toka_api_configuration, topo_name=None, test_suite_name=None):
    """Retrieve the run status of the test suite on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test suite whose run status is to be retrieved.
        test_suite_name (str): Name of the test suite whose run status is to be retrieved.

    Returns:
        str: Test suite run status if successful, None otherwise.
    """
    if ( None == toka_api_configuration or None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_name or 0 == len(test_suite_name.strip()) ):
        print('[testbuilder_mgmt][fetch_test_suite_status] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name is null or empty or '
              'the test_suite_name is null or empty. '
              ' Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Success'    
    TOKA_API_RESPONSE_KEY_STATUS = 'status'
    TOKA_API_RESPONSE_KEY_TEST_SUITE_STATUS = 'test_suite_status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.get_test_suite_status_v1(
                                                        topology_name=topo_name, 
                                                        suite_name=test_suite_name, 
                                                        username=tuple_user_token[0], 
                                                        api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower()) and
            True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_TEST_SUITE_STATUS) and 
            None != api_v1_response.test_suite_status ):
            # Test suite run status was retrieved successfully
            return api_v1_response.test_suite_status
        else:
            print('[testbuilder_mgmt][fetch_test_suite_status] Failed to '
                    'retrieve the test suite run status. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][fetch_test_suite_status] APIException '
                ' occurred while attempting to retrieve the test suite run status. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][fetch_test_suite_status] Exception '
              ' occurred while attempting to retrieve the test suite run status. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False   


def clone_test_suite(toka_api_configuration, topo_name=None, test_suite_to_clone_from=None, test_suite_to_clone_to=None):
    """Clone a test suite on the Toka controller.
    
    Args:
        toka_api_configuration (tokasdk.Configuration): Toka SDK configuration object.
        topo_name (str): Name of the topology that contains the test suite to be cloned.
        test_suite_to_clone_from (str): Name of the test suite that is to be cloned.
        test_suite_to_clone_to (str): Name of the newly created test suite.

    Returns:
        bool: True if the test suite was cloned successfully, False otherwise.
    """
    if ( None == toka_api_configuration or 
         None == topo_name or 0 == len(topo_name.strip()) or 
         None == test_suite_to_clone_from or 0 == len(test_suite_to_clone_from.strip()) or 
         None == test_suite_to_clone_to or 0 == len(test_suite_to_clone_to.strip()) ):
        print('[testbuilder_mgmt][clone_test_suite] Invalid input '
              'specified. Either the Toka API configuration object or '
              'the topology name or '
              'the test suite name to clone from or'
              'the test suite name to clone to is null or empty. '
              'Returning failure')
        return False

    TOKA_API_RESPONSE_SUCCESS = 'Success'
    TOKA_API_RESPONSE_KEY_STATUS = 'status'

    try:
        tuple_user_token = (libsamples.setup.setup_steps
                    .fetch_username_token_from_configuration_object(
                        toka_api_configuration=toka_api_configuration))
        if None == tuple_user_token:
            return False
        toka_topology_api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(toka_api_configuration))
        api_v1_response = toka_topology_api_instance.clone_test_suite_v1(
                                                    old_suite_name=test_suite_to_clone_from, 
                                                    new_suite_name=test_suite_to_clone_to, 
                                                    topology_name=topo_name, 
                                                    username=tuple_user_token[0], 
                                                    api_token=tuple_user_token[1])
        if (True == hasattr(api_v1_response, TOKA_API_RESPONSE_KEY_STATUS) and 
            None != api_v1_response.status and 
            -1 != api_v1_response.status.lower().find(TOKA_API_RESPONSE_SUCCESS.lower())):
             # Test suite cloned successfully...
            return True
        else:
            print('[testbuilder_mgmt][clone_test_suite] Failed to '
                    'clone the test suite. Returning failure. '
                    'Error message ' + str(api_v1_response))
            return False
    except ApiException as exc:
        print('[testbuilder_mgmt][clone_test_suite] APIException '
                ' occurred while attempting to clone the test suite. '
                'Returning failure. APIException status- {0}, '
                'reason - {1}, message -{2}, response body - {3}'
                .format(exc.status, exc.reason, exc.message, exc.body))
        return False
    except Exception as exc:
        print('[testbuilder_mgmt][clone_test_suite] Exception '
              ' occurred while attempting to clone the test suite. '
              'Returning failure. Exception message - {0}'
              .format(exc.message))
        # traceback.print_exc()            
        return False    
