# tokasdk.ConnectionsApi

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connections**](ConnectionsApi.md#add_connections) | **POST** /connections | Add a new connection to the inventory
[**delete_connection**](ConnectionsApi.md#delete_connection) | **DELETE** /connections/{connectionid} | Delete an existing connection from the inventory
[**get_connections_and_filter**](ConnectionsApi.md#get_connections_and_filter) | **GET** /connections | Retrieve all connections that have been added to the inventory as well  as search and filter the connections based on certain criteria 


# **add_connections**
> TokaAPIResponse add_connections(add_connections_request=add_connections_request)

Add a new connection to the inventory

Add a new connection to the inventory

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
api_instance = tokasdk.ConnectionsApi(tokasdk.ApiClient(configuration))
add_connections_request = tokasdk.AddConnectionsRequest() # AddConnectionsRequest |  (optional)

try:
    # Add a new connection to the inventory
    api_response = api_instance.add_connections(add_connections_request=add_connections_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->add_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_connections_request** | [**AddConnectionsRequest**](AddConnectionsRequest.md)|  | [optional] 

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

# **delete_connection**
> TokaAPIResponse delete_connection(connectionid)

Delete an existing connection from the inventory

Delete an existing connection from the inventory

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
api_instance = tokasdk.ConnectionsApi(tokasdk.ApiClient(configuration))
connectionid = 'connectionid_example' # str | Existing connection id.

try:
    # Delete an existing connection from the inventory
    api_response = api_instance.delete_connection(connectionid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectionid** | **str**| Existing connection id. | 

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

# **get_connections_and_filter**
> TokaAPIResponse get_connections_and_filter(connection_id=connection_id, hostname=hostname, reservation_status=reservation_status, include_indirect_connections=include_indirect_connections)

Retrieve all connections that have been added to the inventory as well  as search and filter the connections based on certain criteria 

Retrieve all connections that have been added to the inventory as well  as search and filter the connections based on certain criteria 

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
api_instance = tokasdk.ConnectionsApi(tokasdk.ApiClient(configuration))
connection_id = 'connection_id_example' # str | Filtering of retrieved connections based on connection id,   <br> Supports returning multiple connections by specifying a comma separated list of connection id’s.<br>At most 40 connection ids can be specified  (optional)
hostname = 'hostname_example' # str | Filter based on hostname. <br> Connections that have either the source host or target host matching the     specified hostname will be returned. <br> Supports specifying multiple hostnames by specifying a comma separated list of hostnames matching regular expression patterns (optional)
reservation_status = 'reservation_status_example' # str | Allows filtering of retrieved connections based on whether they are currently reserved or not <br> Note that only traffic generator connections can be “reserved” <br> Specifying this filter as “reserved/available” will \"exclude/include\" all connections not involving a traffic generator device (optional)
include_indirect_connections = 'include_indirect_connections_example' # str | Allows including indirect connections for the specified hosts <br> Allows for identifying neighbors of a device <br> If and set to true, then request must include only the hostname filter. <br> Response will include indirect connections in addition to direct connection.  (optional)

try:
    # Retrieve all connections that have been added to the inventory as well  as search and filter the connections based on certain criteria 
    api_response = api_instance.get_connections_and_filter(connection_id=connection_id, hostname=hostname, reservation_status=reservation_status, include_indirect_connections=include_indirect_connections)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->get_connections_and_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| Filtering of retrieved connections based on connection id,   &lt;br&gt; Supports returning multiple connections by specifying a comma separated list of connection id’s.&lt;br&gt;At most 40 connection ids can be specified  | [optional] 
 **hostname** | **str**| Filter based on hostname. &lt;br&gt; Connections that have either the source host or target host matching the     specified hostname will be returned. &lt;br&gt; Supports specifying multiple hostnames by specifying a comma separated list of hostnames matching regular expression patterns | [optional] 
 **reservation_status** | **str**| Allows filtering of retrieved connections based on whether they are currently reserved or not &lt;br&gt; Note that only traffic generator connections can be “reserved” &lt;br&gt; Specifying this filter as “reserved/available” will \&quot;exclude/include\&quot; all connections not involving a traffic generator device | [optional] 
 **include_indirect_connections** | **str**| Allows including indirect connections for the specified hosts &lt;br&gt; Allows for identifying neighbors of a device &lt;br&gt; If and set to true, then request must include only the hostname filter. &lt;br&gt; Response will include indirect connections in addition to direct connection.  | [optional] 

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

