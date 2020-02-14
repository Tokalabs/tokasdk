# tokasdk.TopologyApi

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_topology**](TopologyApi.md#add_topology) | **POST** /topologies | Create a new topology
[**delete_topology**](TopologyApi.md#delete_topology) | **DELETE** /topologies/{topologyname} | Delete an existing topology
[**edit_topology**](TopologyApi.md#edit_topology) | **PUT** /topologies/{topologyname} | Edit/update an existing topology
[**get_topology**](TopologyApi.md#get_topology) | **GET** /topologies | Retrieve all topologies as well as search and filter topologies based on certain criteria
[**release_topology_v1**](TopologyApi.md#release_topology_v1) | **GET** /topology/{topology_name}/release/user&#x3D;{username}/token&#x3D;{api_token} | Release an already reserved topology
[**reserve_topology_v1**](TopologyApi.md#reserve_topology_v1) | **GET** /topology/{topology_name}/reserve/user&#x3D;{username}/token&#x3D;{api_token} | Reserve a topology


# **add_topology**
> TokaAPIResponse add_topology(add_topology_request=add_topology_request)

Create a new topology

Create a new topology

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
api_instance = tokasdk.TopologyApi(tokasdk.ApiClient(configuration))
add_topology_request = tokasdk.AddTopologyRequest() # AddTopologyRequest |  (optional)

try:
    # Create a new topology
    api_response = api_instance.add_topology(add_topology_request=add_topology_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->add_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_topology_request** | [**AddTopologyRequest**](AddTopologyRequest.md)|  | [optional] 

### Return type

[**TokaAPIResponse**](TokaAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |
**201** | New resource was successfully created |  -  |
**202** | Request was successfully received and is being serviced. |  -  |
**400** | Request was malformed |  -  |
**401** | Request did not include a valid authentication token |  -  |
**403** | Request includes a valid authentication token but the token in unauthorized to perform the requested action |  -  |
**404** | Resource was not found on the server |  -  |
**409** | Resource could not be created as another resource with the same name already exists |  -  |
**500** | Unexpected error occurred while processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology**
> TokaAPIResponse delete_topology(topologyname)

Delete an existing topology

Delete an existing topology

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
api_instance = tokasdk.TopologyApi(tokasdk.ApiClient(configuration))
topologyname = 'topologyname_example' # str | Existing topology name

try:
    # Delete an existing topology
    api_response = api_instance.delete_topology(topologyname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topologyname** | **str**| Existing topology name | 

### Return type

[**TokaAPIResponse**](TokaAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |
**401** | Request did not include a valid authentication token |  -  |
**403** | Request includes a valid authentication token but the token in unauthorized to perform the requested action |  -  |
**404** | Resource was not found on the server |  -  |
**500** | Unexpected error occurred while processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_topology**
> TokaAPIResponse edit_topology(topologyname, edit_topology_request=edit_topology_request)

Edit/update an existing topology

Edit/update an existing topology

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
api_instance = tokasdk.TopologyApi(tokasdk.ApiClient(configuration))
topologyname = 'topologyname_example' # str | Existing topology name
edit_topology_request = tokasdk.EditTopologyRequest() # EditTopologyRequest |  (optional)

try:
    # Edit/update an existing topology
    api_response = api_instance.edit_topology(topologyname, edit_topology_request=edit_topology_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->edit_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topologyname** | **str**| Existing topology name | 
 **edit_topology_request** | [**EditTopologyRequest**](EditTopologyRequest.md)|  | [optional] 

### Return type

[**TokaAPIResponse**](TokaAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |
**201** | Resource was successfully updated |  -  |
**202** | Request was successfully received and is being serviced. |  -  |
**400** | Request was malformed |  -  |
**401** | Request did not include a valid authentication token |  -  |
**403** | Request includes a valid authentication token but the token in unauthorized to perform the requested action |  -  |
**404** | Resource was not found on the server |  -  |
**409** | Resource could not be updated as another resource with the same name already exists |  -  |
**500** | Unexpected error occurred while processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology**
> TokaAPIResponse get_topology(name=name, group=group, reservation_status=reservation_status, users_with_access=users_with_access, fields_to_fetch=fields_to_fetch)

Retrieve all topologies as well as search and filter topologies based on certain criteria

Retrieve all topologies as well as search and filter topologies based on certain criteria

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
api_instance = tokasdk.TopologyApi(tokasdk.ApiClient(configuration))
name = 'name_example' # str | Filtering topologies based on name<br> Supports specifying multiple topologies by specifying a comma separated list of topologies matching regular expression patterns (optional)
group = 'group_example' # str | Filtering topologies based on group name<br> Supports multiple groups by specifying a comma separated list  (optional)
reservation_status = 'reservation_status_example' # str | Allows filtering of retrieved topologies based on whether they are currently reserved or not (optional)
users_with_access = 'users_with_access_example' # str | Filter based on users who have access <br> Supports a special keyword all that implies retrieving topologies that all users have access to<br> Supports a special character ‘|’ as the OR operator<br> Supports using regular expressions (optional)
fields_to_fetch = 'fields_to_fetch_example' # str | Filtering of response data retrieved for each device <br> Comma separated list of fields to be returned for each topology<br> Supports filtering of only top-level fields e.g. name, group, accessControl etc<br> If not specified, all fields will be returned for the matching topologies (optional)

try:
    # Retrieve all topologies as well as search and filter topologies based on certain criteria
    api_response = api_instance.get_topology(name=name, group=group, reservation_status=reservation_status, users_with_access=users_with_access, fields_to_fetch=fields_to_fetch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filtering topologies based on name&lt;br&gt; Supports specifying multiple topologies by specifying a comma separated list of topologies matching regular expression patterns | [optional] 
 **group** | **str**| Filtering topologies based on group name&lt;br&gt; Supports multiple groups by specifying a comma separated list  | [optional] 
 **reservation_status** | **str**| Allows filtering of retrieved topologies based on whether they are currently reserved or not | [optional] 
 **users_with_access** | **str**| Filter based on users who have access &lt;br&gt; Supports a special keyword all that implies retrieving topologies that all users have access to&lt;br&gt; Supports a special character ‘|’ as the OR operator&lt;br&gt; Supports using regular expressions | [optional] 
 **fields_to_fetch** | **str**| Filtering of response data retrieved for each device &lt;br&gt; Comma separated list of fields to be returned for each topology&lt;br&gt; Supports filtering of only top-level fields e.g. name, group, accessControl etc&lt;br&gt; If not specified, all fields will be returned for the matching topologies | [optional] 

### Return type

[**TokaAPIResponse**](TokaAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was successfully serviced |  -  |
**400** | Request was malformed |  -  |
**401** | Request did not include a valid authentication token |  -  |
**403** | Request includes a valid authentication token but the token in unauthorized to perform the requested action |  -  |
**500** | Unexpected error occurred while processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_topology_v1**
> TokaAPIv1Response release_topology_v1(topology_name, username, api_token)

Release an already reserved topology

Release an already reserved topology

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
api_instance = tokasdk.TopologyApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology to release.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Release an already reserved topology
    api_response = api_instance.release_topology_v1(topology_name, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->release_topology_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology to release. | 
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

# **reserve_topology_v1**
> TokaAPIv1Response reserve_topology_v1(topology_name, username, api_token)

Reserve a topology

Reserve a topology

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
api_instance = tokasdk.TopologyApi(tokasdk.ApiClient(configuration))
topology_name = 'topology_name_example' # str | Name of the topology to reserve.
username = 'username_example' # str | Name of the user initiating the request.
api_token = 'api_token_example' # str | API token for the the user initiating the request.

try:
    # Reserve a topology
    api_response = api_instance.reserve_topology_v1(topology_name, username, api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->reserve_topology_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_name** | **str**| Name of the topology to reserve. | 
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

