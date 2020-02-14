# tokasdk.TestBuilderApi

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_test_suite_v1**](TestBuilderApi.md#abort_test_suite_v1) | **GET** /topology/{topology_name}/abort/suite/suite&#x3D;{suite_name}/user&#x3D;{username}/token&#x3D;{api_token} | Abort an already executing test suite
[**abort_test_v1**](TestBuilderApi.md#abort_test_v1) | **GET** /topology/{topology_name}/abort/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Abort an already executing test
[**clone_test_suite_v1**](TestBuilderApi.md#clone_test_suite_v1) | **GET** /topology/oldSuiteName&#x3D;{old_suite_name}/newSuiteName&#x3D;{new_suite_name}/topologyName&#x3D;{topology_name}/user&#x3D;{username}/token&#x3D;{api_token} | Clone a test suite.
[**get_test_status_v1**](TestBuilderApi.md#get_test_status_v1) | **GET** /topology/{topology_name}/status/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Retrieve status of a test
[**get_test_suite_status_v1**](TestBuilderApi.md#get_test_suite_status_v1) | **GET** /topology/{topology_name}/status/suite/suite&#x3D;{suite_name}/user&#x3D;{username}/token&#x3D;{api_token} | Retrieve status of a test suite.
[**pause_test_v1**](TestBuilderApi.md#pause_test_v1) | **GET** /topology/{topology_name}/pause/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Pause an already executing test
[**resume_test_v1**](TestBuilderApi.md#resume_test_v1) | **GET** /topology/{topology_name}/resume/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Resume an already paused test
[**run_test_suite_v1**](TestBuilderApi.md#run_test_suite_v1) | **GET** /topology/{topology_name}/run/suite/suite&#x3D;{suite_name}/user&#x3D;{username}/token&#x3D;{api_token} | Run a test suite
[**run_test_v1**](TestBuilderApi.md#run_test_v1) | **GET** /topology/{topology_name}/run/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Run a test


# **abort_test_suite_v1**
> TokaAPIv1Response abort_test_suite_v1(topology_name, suite_name, username, api_token)

Abort an already executing test suite

Abort an already executing test suite

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test suite to abort.
suite_name = 'suite_name_example' # str | Name of the test suite to abort.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Abort an already executing test suite
    api_response = api_instance.abort_test_suite_v1(topology_name, suite_name, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->abort_test_suite_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test suite to abort. | 
 **suite_name** | **str**| Name of the test suite to abort. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abort_test_v1**
> TokaAPIv1Response abort_test_v1(topology_name, suite_name, testcase_id, username, api_token)

Abort an already executing test

Abort an already executing test

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test to abort.
suite_name = 'suite_name_example' # str | Name of the test suite that contains the test to abort.
testcase_id = 'testcase_id_example' # str | Id of the test to abort.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Abort an already executing test
    api_response = api_instance.abort_test_v1(topology_name, suite_name, testcase_id, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->abort_test_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test to abort. | 
 **suite_name** | **str**| Name of the test suite that contains the test to abort. | 
 **testcase_id** | **str**| Id of the test to abort. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_test_suite_v1**
> TokaAPIv1Response clone_test_suite_v1(old_suite_name, new_suite_name, topology_name, username, api_token)

Clone a test suite.

Clone a test suite.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
old_suite_name = 'old_suite_name_example' # str | Name of the test suite to be cloned.
new_suite_name = 'new_suite_name_example' # str | Name of the new test suite to be created as a clone.
topology_name = 'topology_name_example' # str | Name of the topology that contains the test suite to clone.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Clone a test suite.
    api_response = api_instance.clone_test_suite_v1(old_suite_name, new_suite_name, topology_name, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->clone_test_suite_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_suite_name** | **str**| Name of the test suite to be cloned. | 
 **new_suite_name** | **str**| Name of the new test suite to be created as a clone. | 
 **topology_name** | **str**| Name of the topology that contains the test suite to clone. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_status_v1**
> TokaAPIv1Response get_test_status_v1(topology_name, suite_name, testcase_id, username, api_token)

Retrieve status of a test

Retrieve status of a test

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test whose status is to be retrieved.
suite_name = 'suite_name_example' # str | Name of the test suite that contains the test whose status is to be retrieved.
testcase_id = 'testcase_id_example' # str | Id of the test whose status is to be retrieved.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Retrieve status of a test
    api_response = api_instance.get_test_status_v1(topology_name, suite_name, testcase_id, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->get_test_status_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test whose status is to be retrieved. | 
 **suite_name** | **str**| Name of the test suite that contains the test whose status is to be retrieved. | 
 **testcase_id** | **str**| Id of the test whose status is to be retrieved. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suite_status_v1**
> TokaAPIv1Response get_test_suite_status_v1(topology_name, suite_name, username, api_token)

Retrieve status of a test suite.

Retrieve status of a test suite.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test suite whose status is to be retrieved.
suite_name = 'suite_name_example' # str | Name of the test suite whose status is to be retrieved.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Retrieve status of a test suite.
    api_response = api_instance.get_test_suite_status_v1(topology_name, suite_name, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->get_test_suite_status_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test suite whose status is to be retrieved. | 
 **suite_name** | **str**| Name of the test suite whose status is to be retrieved. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_test_v1**
> TokaAPIv1Response pause_test_v1(topology_name, suite_name, testcase_id, username, api_token)

Pause an already executing test

Pause an already executing test

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test to pause.
suite_name = 'suite_name_example' # str | Name of the test suite that contains the test to pause.
testcase_id = 'testcase_id_example' # str | Id of the test to pause.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Pause an already executing test
    api_response = api_instance.pause_test_v1(topology_name, suite_name, testcase_id, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->pause_test_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test to pause. | 
 **suite_name** | **str**| Name of the test suite that contains the test to pause. | 
 **testcase_id** | **str**| Id of the test to pause. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_test_v1**
> TokaAPIv1Response resume_test_v1(topology_name, suite_name, testcase_id, username, api_token)

Resume an already paused test

Resume an already paused test

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the paused test to resume.
suite_name = 'suite_name_example' # str | Name of the test suite that contains the paused test to resume.
testcase_id = 'testcase_id_example' # str | Id of the paused test that is to be resumed.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Resume an already paused test
    api_response = api_instance.resume_test_v1(topology_name, suite_name, testcase_id, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->resume_test_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the paused test to resume. | 
 **suite_name** | **str**| Name of the test suite that contains the paused test to resume. | 
 **testcase_id** | **str**| Id of the paused test that is to be resumed. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_test_suite_v1**
> TokaAPIv1Response run_test_suite_v1(topology_name, suite_name, username, api_token)

Run a test suite

Run a test suite

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test suite to run.
suite_name = 'suite_name_example' # str | Name of the test suite to run.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Run a test suite
    api_response = api_instance.run_test_suite_v1(topology_name, suite_name, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->run_test_suite_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test suite to run. | 
 **suite_name** | **str**| Name of the test suite to run. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_test_v1**
> TokaAPIv1Response run_test_v1(topology_name, suite_name, testcase_id, username, api_token)

Run a test

Run a test

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import tokasdk
from tokasdk.rest import ApiException
from pprint import pprint
configuration = tokasdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://LS200VE-Controller/tokalabs/api
configuration.host = "https://LS200VE-Controller/tokalabs/api"
# Create an instance of the API class
api_instance = tokasdk.TestBuilderApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology that contains the test to run.
suite_name = 'suite_name_example' # str | Name of the test suite that contains the test to run.
testcase_id = 'testcase_id_example' # str | Id of the test to run.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Run a test
    api_response = api_instance.run_test_v1(topology_name, suite_name, testcase_id, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestBuilderApi->run_test_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology that contains the test to run. | 
 **suite_name** | **str**| Name of the test suite that contains the test to run. | 
 **testcase_id** | **str**| Id of the test to run. | 
 **username** | **str**| Name of the user initiating the request. | 
 **api_token** | **str**| API token for the the user initiating the request. | 

### Return type

[**TokaAPIv1Response**](TokaAPIv1Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

