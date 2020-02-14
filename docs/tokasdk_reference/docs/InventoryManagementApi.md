# tokasdk.InventoryManagementApi

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_aws_region**](InventoryManagementApi.md#add_aws_region) | **POST** /devices/aws/region/ | Add an AWS region to the inventory
[**add_aws_vpc**](InventoryManagementApi.md#add_aws_vpc) | **POST** /devices/aws/vpc/ | Add an existing AWS VPC or create a new AWS VPC and add it to the  inventory
[**add_ec2**](InventoryManagementApi.md#add_ec2) | **POST** /devices/aws/ec2instance/ | Add an existing AWS EC2 instance or create a new AWS EC2 instance and  add it to the inventory
[**add_link_manager**](InventoryManagementApi.md#add_link_manager) | **POST** /devices/linkmanager/ | Add a new link manager device to the inventory
[**add_network_device**](InventoryManagementApi.md#add_network_device) | **POST** /devices/network/ | Add a new network device to the inventory
[**add_traffic_generator**](InventoryManagementApi.md#add_traffic_generator) | **POST** /devices/trafficgenerator/ | Add a new traffic generator device to the inventory
[**add_v_center**](InventoryManagementApi.md#add_v_center) | **POST** /devices/vmware/vcenter/ | Add a new VMware vCenter device to the inventory
[**add_vm**](InventoryManagementApi.md#add_vm) | **POST** /devices/vmware/vm/ | Add an already existing VM (hosted on the specified VMware vCenter) or  launch a new VM (on the specified VMware vCenter and then add) to the inventory
[**add_vm_profile**](InventoryManagementApi.md#add_vm_profile) | **POST** /devices/vmware/vmprofile/ | Add a new VMware VM Profile to the inventory
[**delete_inventory_device**](InventoryManagementApi.md#delete_inventory_device) | **DELETE** /devices/{hostname} | Delete an existing device from the inventory 
[**edit_aws_region**](InventoryManagementApi.md#edit_aws_region) | **PUT** /devices/aws/region/{hostname} | Edit/update an existing AWS region in the inventory
[**edit_ec2**](InventoryManagementApi.md#edit_ec2) | **PUT** /devices/aws/ec2instance/{hostname} | Edit/update an existing AWS EC2 instance device in the inventory
[**edit_link_manager**](InventoryManagementApi.md#edit_link_manager) | **PUT** /devices/linkmanager/{hostname} | Edit/update an existing link manager device in the inventory
[**edit_network_device**](InventoryManagementApi.md#edit_network_device) | **PUT** /devices/network/{hostname} | Edit/update an existing network device in the inventory
[**edit_traffic_generator**](InventoryManagementApi.md#edit_traffic_generator) | **PUT** /devices/trafficgenerator/{hostname} | Edit/update an existing traffic generator device in the inventory
[**edit_v_center**](InventoryManagementApi.md#edit_v_center) | **PUT** /devices/vmware/vcenter/{hostname} | Edit/update an existing VMWare vCenter device in the inventory
[**edit_vm**](InventoryManagementApi.md#edit_vm) | **PUT** /devices/vmware/vm/{hostname} | Edit/update an existing VMware VM device in the inventory
[**edit_vm_profile**](InventoryManagementApi.md#edit_vm_profile) | **PUT** /devices/vmware/vmprofile/{hostname} | Edit/update an existing VMware VM Profile in the inventory
[**get_inventory_devices**](InventoryManagementApi.md#get_inventory_devices) | **GET** /devices | Retrieve all devices that have been added to the inventory as well as search and filter the devices based on certain criteria


# **add_aws_region**
> TokaAPIResponse add_aws_region(add_aws_region_request=add_aws_region_request)

Add an AWS region to the inventory

Add an AWS region to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_aws_region_request = tokasdk.AddAWSRegionRequest() # AddAWSRegionRequest |  (optional)

try:
    # Add an AWS region to the inventory
    api_response = api_instance.add_aws_region(add_aws_region_request=add_aws_region_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_aws_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_aws_region_request** | [**AddAWSRegionRequest**](AddAWSRegionRequest.md)|  | [optional] 

### Return type

[**TokaAPIResponse**](TokaAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: applicatoin/json
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

# **add_aws_vpc**
> TokaAPIResponse add_aws_vpc(add_aws_vpc_request=add_aws_vpc_request)

Add an existing AWS VPC or create a new AWS VPC and add it to the  inventory

Add an existing AWS VPC or create a new AWS VPC and add it to the  inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_aws_vpc_request = tokasdk.AddAWSVpcRequest() # AddAWSVpcRequest |  (optional)

try:
    # Add an existing AWS VPC or create a new AWS VPC and add it to the  inventory
    api_response = api_instance.add_aws_vpc(add_aws_vpc_request=add_aws_vpc_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_aws_vpc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_aws_vpc_request** | [**AddAWSVpcRequest**](AddAWSVpcRequest.md)|  | [optional] 

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

# **add_ec2**
> TokaAPIResponse add_ec2(add_ec2_request=add_ec2_request)

Add an existing AWS EC2 instance or create a new AWS EC2 instance and  add it to the inventory

Add an existing AWS EC2 instance or create a new AWS EC2 instance and  add it to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_ec2_request = tokasdk.AddEC2Request() # AddEC2Request |  (optional)

try:
    # Add an existing AWS EC2 instance or create a new AWS EC2 instance and  add it to the inventory
    api_response = api_instance.add_ec2(add_ec2_request=add_ec2_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_ec2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_ec2_request** | [**AddEC2Request**](AddEC2Request.md)|  | [optional] 

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

# **add_link_manager**
> TokaAPIResponse add_link_manager(add_link_manager_request=add_link_manager_request)

Add a new link manager device to the inventory

Add a new link manager device to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_link_manager_request = tokasdk.AddLinkManagerRequest() # AddLinkManagerRequest |  (optional)

try:
    # Add a new link manager device to the inventory
    api_response = api_instance.add_link_manager(add_link_manager_request=add_link_manager_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_link_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_link_manager_request** | [**AddLinkManagerRequest**](AddLinkManagerRequest.md)|  | [optional] 

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

# **add_network_device**
> TokaAPIResponse add_network_device(add_network_device_request=add_network_device_request)

Add a new network device to the inventory

Add a new network device to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_network_device_request = tokasdk.AddNetworkDeviceRequest() # AddNetworkDeviceRequest |  (optional)

try:
    # Add a new network device to the inventory
    api_response = api_instance.add_network_device(add_network_device_request=add_network_device_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_network_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_network_device_request** | [**AddNetworkDeviceRequest**](AddNetworkDeviceRequest.md)|  | [optional] 

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

# **add_traffic_generator**
> TokaAPIResponse add_traffic_generator(add_traffic_generator_request=add_traffic_generator_request)

Add a new traffic generator device to the inventory

Add a new traffic generator device to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_traffic_generator_request = tokasdk.AddTrafficGeneratorRequest() # AddTrafficGeneratorRequest |  (optional)

try:
    # Add a new traffic generator device to the inventory
    api_response = api_instance.add_traffic_generator(add_traffic_generator_request=add_traffic_generator_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_traffic_generator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_traffic_generator_request** | [**AddTrafficGeneratorRequest**](AddTrafficGeneratorRequest.md)|  | [optional] 

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

# **add_v_center**
> TokaAPIResponse add_v_center(add_v_center_request=add_v_center_request)

Add a new VMware vCenter device to the inventory

Add a new VMware vCenter device to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_v_center_request = tokasdk.AddVCenterRequest() # AddVCenterRequest |  (optional)

try:
    # Add a new VMware vCenter device to the inventory
    api_response = api_instance.add_v_center(add_v_center_request=add_v_center_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_v_center: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_v_center_request** | [**AddVCenterRequest**](AddVCenterRequest.md)|  | [optional] 

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

# **add_vm**
> TokaAPIResponse add_vm(add_vm_request=add_vm_request)

Add an already existing VM (hosted on the specified VMware vCenter) or  launch a new VM (on the specified VMware vCenter and then add) to the inventory

Add an already existing VM (hosted on the specified VMware vCenter) or  launch a new VM (on the specified VMware vCenter and then add) to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_vm_request = tokasdk.AddVMRequest() # AddVMRequest |  (optional)

try:
    # Add an already existing VM (hosted on the specified VMware vCenter) or  launch a new VM (on the specified VMware vCenter and then add) to the inventory
    api_response = api_instance.add_vm(add_vm_request=add_vm_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_vm_request** | [**AddVMRequest**](AddVMRequest.md)|  | [optional] 

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

# **add_vm_profile**
> TokaAPIResponse add_vm_profile(add_vm_profile_request=add_vm_profile_request)

Add a new VMware VM Profile to the inventory

Add a new VMware VM Profile to the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
add_vm_profile_request = tokasdk.AddVmProfileRequest() # AddVmProfileRequest |  (optional)

try:
    # Add a new VMware VM Profile to the inventory
    api_response = api_instance.add_vm_profile(add_vm_profile_request=add_vm_profile_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->add_vm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_vm_profile_request** | [**AddVmProfileRequest**](AddVmProfileRequest.md)|  | [optional] 

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

# **delete_inventory_device**
> TokaAPIResponse delete_inventory_device(hostname, delete_from_server)

Delete an existing device from the inventory 

Delete an existing device from the inventory  

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | Name of the device to delete.
delete_from_server = 'delete_from_server_example' # str | delete device from inventory

try:
    # Delete an existing device from the inventory 
    api_response = api_instance.delete_inventory_device(hostname, delete_from_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->delete_inventory_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Name of the device to delete. | 
 **delete_from_server** | **str**| delete device from inventory | 

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

# **edit_aws_region**
> TokaAPIResponse edit_aws_region(hostname, edit_aws_region_request=edit_aws_region_request)

Edit/update an existing AWS region in the inventory

Edit/update an existing AWS region in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | AWS Region
edit_aws_region_request = tokasdk.EditAWSRegionRequest() # EditAWSRegionRequest |  (optional)

try:
    # Edit/update an existing AWS region in the inventory
    api_response = api_instance.edit_aws_region(hostname, edit_aws_region_request=edit_aws_region_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_aws_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| AWS Region | 
 **edit_aws_region_request** | [**EditAWSRegionRequest**](EditAWSRegionRequest.md)|  | [optional] 

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

# **edit_ec2**
> TokaAPIResponse edit_ec2(hostname, edit_ec2_request=edit_ec2_request)

Edit/update an existing AWS EC2 instance device in the inventory

Edit/update an existing AWS EC2 instance device in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | AWS Ec2 Instance Name
edit_ec2_request = tokasdk.EditEC2Request() # EditEC2Request |  (optional)

try:
    # Edit/update an existing AWS EC2 instance device in the inventory
    api_response = api_instance.edit_ec2(hostname, edit_ec2_request=edit_ec2_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_ec2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| AWS Ec2 Instance Name | 
 **edit_ec2_request** | [**EditEC2Request**](EditEC2Request.md)|  | [optional] 

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

# **edit_link_manager**
> TokaAPIResponse edit_link_manager(hostname, edit_link_manager_request=edit_link_manager_request)

Edit/update an existing link manager device in the inventory

Edit/update an existing link manager device in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | Link Manager name
edit_link_manager_request = tokasdk.EditLinkManagerRequest() # EditLinkManagerRequest |  (optional)

try:
    # Edit/update an existing link manager device in the inventory
    api_response = api_instance.edit_link_manager(hostname, edit_link_manager_request=edit_link_manager_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_link_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Link Manager name | 
 **edit_link_manager_request** | [**EditLinkManagerRequest**](EditLinkManagerRequest.md)|  | [optional] 

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

# **edit_network_device**
> TokaAPIResponse edit_network_device(hostname, edit_network_device_request=edit_network_device_request)

Edit/update an existing network device in the inventory

Edit/update an existing network device in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | name of the device
edit_network_device_request = tokasdk.EditNetworkDeviceRequest() # EditNetworkDeviceRequest |  (optional)

try:
    # Edit/update an existing network device in the inventory
    api_response = api_instance.edit_network_device(hostname, edit_network_device_request=edit_network_device_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_network_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| name of the device | 
 **edit_network_device_request** | [**EditNetworkDeviceRequest**](EditNetworkDeviceRequest.md)|  | [optional] 

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

# **edit_traffic_generator**
> TokaAPIResponse edit_traffic_generator(hostname, edit_traffic_generator_request=edit_traffic_generator_request)

Edit/update an existing traffic generator device in the inventory

Edit/update an existing traffic generator device in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | Traffic generator name
edit_traffic_generator_request = tokasdk.EditTrafficGeneratorRequest() # EditTrafficGeneratorRequest |  (optional)

try:
    # Edit/update an existing traffic generator device in the inventory
    api_response = api_instance.edit_traffic_generator(hostname, edit_traffic_generator_request=edit_traffic_generator_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_traffic_generator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Traffic generator name | 
 **edit_traffic_generator_request** | [**EditTrafficGeneratorRequest**](EditTrafficGeneratorRequest.md)|  | [optional] 

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

# **edit_v_center**
> TokaAPIResponse edit_v_center(hostname, edit_v_center_request=edit_v_center_request)

Edit/update an existing VMWare vCenter device in the inventory

Edit/update an existing VMWare vCenter device in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | vCenter device name
edit_v_center_request = tokasdk.EditVCenterRequest() # EditVCenterRequest |  (optional)

try:
    # Edit/update an existing VMWare vCenter device in the inventory
    api_response = api_instance.edit_v_center(hostname, edit_v_center_request=edit_v_center_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_v_center: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| vCenter device name | 
 **edit_v_center_request** | [**EditVCenterRequest**](EditVCenterRequest.md)|  | [optional] 

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

# **edit_vm**
> TokaAPIResponse edit_vm(hostname, edit_vm_request=edit_vm_request)

Edit/update an existing VMware VM device in the inventory

Edit/update an existing VMware VM device in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | VMware VM name
edit_vm_request = tokasdk.EditVMRequest() # EditVMRequest |  (optional)

try:
    # Edit/update an existing VMware VM device in the inventory
    api_response = api_instance.edit_vm(hostname, edit_vm_request=edit_vm_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| VMware VM name | 
 **edit_vm_request** | [**EditVMRequest**](EditVMRequest.md)|  | [optional] 

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

# **edit_vm_profile**
> TokaAPIResponse edit_vm_profile(hostname, edit_vm_profile_request=edit_vm_profile_request)

Edit/update an existing VMware VM Profile in the inventory

Edit/update an existing VMware VM Profile in the inventory

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | VM Profile Name
edit_vm_profile_request = tokasdk.EditVmProfileRequest() # EditVmProfileRequest |  (optional)

try:
    # Edit/update an existing VMware VM Profile in the inventory
    api_response = api_instance.edit_vm_profile(hostname, edit_vm_profile_request=edit_vm_profile_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->edit_vm_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| VM Profile Name | 
 **edit_vm_profile_request** | [**EditVmProfileRequest**](EditVmProfileRequest.md)|  | [optional] 

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

# **get_inventory_devices**
> TokaAPIResponse get_inventory_devices(hostname=hostname, device_category=device_category, device_type=device_type, device_vendor=device_vendor, reservation_status=reservation_status, primary_ip_address=primary_ip_address, id=id, fields_to_fetch=fields_to_fetch, sort_on=sort_on, sort_order=sort_order, page_num=page_num, page_size=page_size)

Retrieve all devices that have been added to the inventory as well as search and filter the devices based on certain criteria

Retrieve all devices that have been added to the inventory as well as search and filter the devices based on certain criteria

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
api_instance = tokasdk.InventoryManagementApi(tokasdk.ApiClient(configuration))
hostname = 'hostname_example' # str | Allows filtering of retrieved devices based on hostname, Supports using regular expression (optional)
device_category = 'device_category_example' # str | filter devices based on the device category <br> Supports a special character ‘|’ as the OR operator (optional)
device_type = 'device_type_example' # str | Allows filtering of retrieved devices based on the device type (e.g. Server)<br> Supports a special character ‘|’ as the OR operator (optional)
device_vendor = 'device_vendor_example' # str | Allows filtering of retrieved devices based on the device vendor (e.g. Allied Telesis)<br> Supports a special character ‘|’ as the OR operator (optional)
reservation_status = 'reservation_status_example' # str | Allows filtering of retrieved device based on whether they are currently reserved or not<br> Supports a special character ‘|’ as the OR operator (optional)
primary_ip_address = 'primary_ip_address_example' # str | Allows filtering of retrieved devices based on primary IPAddress<br> Supports using regular expression (optional)
id = 'id_example' # str | Allows filtering of retrieved devices based on the internal device id <br> Supported values – Any non-negative integer <br> Supports the following operators. <br>  Eg - Equals, Less than, Greater than, Less than or equals to, Greater than or equals to <br>   id[lte]=100 returns all devices with id <= 100 <br>   id[gt]=100 returns all devices with id > 100 <br>   id=45 return the devices with id=45 <br> (optional)
fields_to_fetch = 'fields_to_fetch_example' # str | Allows filtering of response data (hostname, vendor etc.) retrieved for each device<br> Comma separated list of fields to be returned for each device <br> If not specified, all fields will be returned for the matching devices (optional)
sort_on = 'sort_on_example' # str | Indicates the field to sort the retrieved devices on<br> If not specified, defaults to lastUpdatedAt (optional)
sort_order = 'sort_order_example' # str | Indicates the order to be used for sorting the retrieved devices<br> If not specified, defaults to – <br> desc if the field (e.g. lastUpdatedAt, createdAt) specified by the sortOn request parameter is of type date/time <br> asc if the field (e.g. hostname, deviceType) specified by the sortOn request parameter is of any type other than date/time (optional)
page_num = 'page_num_example' # str | Indicates the page number of the results to be retrieved<br> Supported values – Any integer value greater than 0, If not specified, defaults to 1 (optional)
page_size = 'page_size_example' # str | Indicates the maximum number of records included in a page i.e. indicates the maximum number of devices returned in the response<br> Supported values – Multiples of 5, If not specified, defaults to 200 (optional)

try:
    # Retrieve all devices that have been added to the inventory as well as search and filter the devices based on certain criteria
    api_response = api_instance.get_inventory_devices(hostname=hostname, device_category=device_category, device_type=device_type, device_vendor=device_vendor, reservation_status=reservation_status, primary_ip_address=primary_ip_address, id=id, fields_to_fetch=fields_to_fetch, sort_on=sort_on, sort_order=sort_order, page_num=page_num, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryManagementApi->get_inventory_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Allows filtering of retrieved devices based on hostname, Supports using regular expression | [optional] 
 **device_category** | **str**| filter devices based on the device category &lt;br&gt; Supports a special character ‘|’ as the OR operator | [optional] 
 **device_type** | **str**| Allows filtering of retrieved devices based on the device type (e.g. Server)&lt;br&gt; Supports a special character ‘|’ as the OR operator | [optional] 
 **device_vendor** | **str**| Allows filtering of retrieved devices based on the device vendor (e.g. Allied Telesis)&lt;br&gt; Supports a special character ‘|’ as the OR operator | [optional] 
 **reservation_status** | **str**| Allows filtering of retrieved device based on whether they are currently reserved or not&lt;br&gt; Supports a special character ‘|’ as the OR operator | [optional] 
 **primary_ip_address** | **str**| Allows filtering of retrieved devices based on primary IPAddress&lt;br&gt; Supports using regular expression | [optional] 
 **id** | **str**| Allows filtering of retrieved devices based on the internal device id &lt;br&gt; Supported values – Any non-negative integer &lt;br&gt; Supports the following operators. &lt;br&gt;  Eg - Equals, Less than, Greater than, Less than or equals to, Greater than or equals to &lt;br&gt;   id[lte]&#x3D;100 returns all devices with id &lt;&#x3D; 100 &lt;br&gt;   id[gt]&#x3D;100 returns all devices with id &gt; 100 &lt;br&gt;   id&#x3D;45 return the devices with id&#x3D;45 &lt;br&gt; | [optional] 
 **fields_to_fetch** | **str**| Allows filtering of response data (hostname, vendor etc.) retrieved for each device&lt;br&gt; Comma separated list of fields to be returned for each device &lt;br&gt; If not specified, all fields will be returned for the matching devices | [optional] 
 **sort_on** | **str**| Indicates the field to sort the retrieved devices on&lt;br&gt; If not specified, defaults to lastUpdatedAt | [optional] 
 **sort_order** | **str**| Indicates the order to be used for sorting the retrieved devices&lt;br&gt; If not specified, defaults to – &lt;br&gt; desc if the field (e.g. lastUpdatedAt, createdAt) specified by the sortOn request parameter is of type date/time &lt;br&gt; asc if the field (e.g. hostname, deviceType) specified by the sortOn request parameter is of any type other than date/time | [optional] 
 **page_num** | **str**| Indicates the page number of the results to be retrieved&lt;br&gt; Supported values – Any integer value greater than 0, If not specified, defaults to 1 | [optional] 
 **page_size** | **str**| Indicates the maximum number of records included in a page i.e. indicates the maximum number of devices returned in the response&lt;br&gt; Supported values – Multiples of 5, If not specified, defaults to 200 | [optional] 

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

