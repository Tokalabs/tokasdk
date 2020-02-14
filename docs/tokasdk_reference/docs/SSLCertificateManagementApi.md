# tokasdk.SSLCertificateManagementApi

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_custom_certificate**](SSLCertificateManagementApi.md#configure_custom_certificate) | **POST** /ssl/customCertificate | Configures the Tokalabs controller to use a new certificate (and private key associated with the certificate)
[**configure_self_signed_certificate**](SSLCertificateManagementApi.md#configure_self_signed_certificate) | **POST** /ssl/selfSignedCertificate | Generate a new self-signed SSL certificate and configure the Tokalabs server to use this newly generated self-signed SSL certificate
[**generate_csr**](SSLCertificateManagementApi.md#generate_csr) | **POST** /ssl/csr | Generate a new certificate signing request (CSR) and a private key associated with the CSR 


# **configure_custom_certificate**
> TokaAPIResponse configure_custom_certificate(cert_file=cert_file, key_file=key_file)

Configures the Tokalabs controller to use a new certificate (and private key associated with the certificate)

Configures the Tokalabs controller to use a new certificate (and private key associated with the certificate)

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
api_instance = tokasdk.SSLCertificateManagementApi(tokasdk.ApiClient(configuration))
cert_file = 'cert_file_example' # str |  (optional)
key_file = 'key_file_example' # str |  (optional)

try:
    # Configures the Tokalabs controller to use a new certificate (and private key associated with the certificate)
    api_response = api_instance.configure_custom_certificate(cert_file=cert_file, key_file=key_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLCertificateManagementApi->configure_custom_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_file** | **str**|  | [optional] 
 **key_file** | **str**|  | [optional] 

### Return type

[**TokaAPIResponse**](TokaAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **configure_self_signed_certificate**
> TokaAPIResponse configure_self_signed_certificate()

Generate a new self-signed SSL certificate and configure the Tokalabs server to use this newly generated self-signed SSL certificate

Generate a new self-signed SSL certificate and configure the Tokalabs server to use this newly generated self-signed SSL certificate

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
api_instance = tokasdk.SSLCertificateManagementApi(tokasdk.ApiClient(configuration))

try:
    # Generate a new self-signed SSL certificate and configure the Tokalabs server to use this newly generated self-signed SSL certificate
    api_response = api_instance.configure_self_signed_certificate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLCertificateManagementApi->configure_self_signed_certificate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**201** | New resource was successfully created |  -  |
**202** | Request was successfully received and is being serviced. |  -  |
**400** | Request was malformed |  -  |
**401** | Request did not include a valid authentication token |  -  |
**403** | Request includes a valid authentication token but the token in unauthorized to perform the requested action |  -  |
**404** | Resource was not found on the server |  -  |
**409** | Resource could not be created as another resource with the same name already exists |  -  |
**500** | Unexpected error occurred while processing the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr**
> file generate_csr(generate_csr_request=generate_csr_request)

Generate a new certificate signing request (CSR) and a private key associated with the CSR 

Generate a new certificate signing request (CSR) and a private key associated with the CSR 

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
api_instance = tokasdk.SSLCertificateManagementApi(tokasdk.ApiClient(configuration))
generate_csr_request = tokasdk.GenerateCSRRequest() # GenerateCSRRequest |  (optional)

try:
    # Generate a new certificate signing request (CSR) and a private key associated with the CSR 
    api_response = api_instance.generate_csr(generate_csr_request=generate_csr_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSLCertificateManagementApi->generate_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_csr_request** | [**GenerateCSRRequest**](GenerateCSRRequest.md)|  | [optional] 

### Return type

**file**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json, text/html; charset=UTF-8, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate and key as zip file |  -  |
**201** | New resource was successfully created |  -  |
**202** | Request was successfully received and is being serviced. |  -  |
**400** | Request was malformed |  -  |
**401** | Request did not include a valid authentication token |  -  |
**403** | Request includes a valid authentication token but the token in unauthorized to perform the requested action |  -  |
**404** | Resource was not found on the server |  -  |
**409** | Resource could not be created as another resource with the same name already exists |  -  |
**500** | Unexpected error occurred while processing the request |  -  |
**0** | Downloadable certificate and key as zip file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

