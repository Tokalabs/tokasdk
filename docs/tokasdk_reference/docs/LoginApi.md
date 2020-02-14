# tokasdk.LoginApi

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](LoginApi.md#login) | **POST** /login | Login to the Toka controller and obtain a valid Toka API token


# **login**
> TokaAPIResponse login(login_request=login_request)

Login to the Toka controller and obtain a valid Toka API token

Login to the Toka controller and obtain a valid Toka API token

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
api_instance = tokasdk.LoginApi(tokasdk.ApiClient(configuration))
login_request = tokasdk.LoginRequest() # LoginRequest |  (optional)

try:
    # Login to the Toka controller and obtain a valid Toka API token
    api_response = api_instance.login(login_request=login_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | [optional] 

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
**400** | Request was malformed |  -  |
**401** | Request did not include a valid authentication token |  -  |
**500** | Unexpected error occurred while processing the request |  -  |
**200** | Request was successfully serviced |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

