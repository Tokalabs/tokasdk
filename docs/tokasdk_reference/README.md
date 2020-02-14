# Documentation for API Endpoints

All URIs are relative to *https://LS200VE-Controller/tokalabs/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConnectionsApi* | [**add_connections**](docs/ConnectionsApi.md#add_connections) | **POST** /connections | Add a new connection to the inventory
*ConnectionsApi* | [**delete_connection**](docs/ConnectionsApi.md#delete_connection) | **DELETE** /connections/{connectionid} | Delete an existing connection from the inventory
*ConnectionsApi* | [**get_connections_and_filter**](docs/ConnectionsApi.md#get_connections_and_filter) | **GET** /connections | Retrieve all connections that have been added to the inventory as well  as search and filter the connections based on certain criteria 
*InventoryManagementApi* | [**add_aws_region**](docs/InventoryManagementApi.md#add_aws_region) | **POST** /devices/aws/region/ | Add an AWS region to the inventory
*InventoryManagementApi* | [**add_aws_vpc**](docs/InventoryManagementApi.md#add_aws_vpc) | **POST** /devices/aws/vpc/ | Add an existing AWS VPC or create a new AWS VPC and add it to the  inventory
*InventoryManagementApi* | [**add_ec2**](docs/InventoryManagementApi.md#add_ec2) | **POST** /devices/aws/ec2instance/ | Add an existing AWS EC2 instance or create a new AWS EC2 instance and  add it to the inventory
*InventoryManagementApi* | [**add_link_manager**](docs/InventoryManagementApi.md#add_link_manager) | **POST** /devices/linkmanager/ | Add a new link manager device to the inventory
*InventoryManagementApi* | [**add_network_device**](docs/InventoryManagementApi.md#add_network_device) | **POST** /devices/network/ | Add a new network device to the inventory
*InventoryManagementApi* | [**add_traffic_generator**](docs/InventoryManagementApi.md#add_traffic_generator) | **POST** /devices/trafficgenerator/ | Add a new traffic generator device to the inventory
*InventoryManagementApi* | [**add_v_center**](docs/InventoryManagementApi.md#add_v_center) | **POST** /devices/vmware/vcenter/ | Add a new VMware vCenter device to the inventory
*InventoryManagementApi* | [**add_vm**](docs/InventoryManagementApi.md#add_vm) | **POST** /devices/vmware/vm/ | Add an already existing VM (hosted on the specified VMware vCenter) or  launch a new VM (on the specified VMware vCenter and then add) to the inventory
*InventoryManagementApi* | [**add_vm_profile**](docs/InventoryManagementApi.md#add_vm_profile) | **POST** /devices/vmware/vmprofile/ | Add a new VMware VM Profile to the inventory
*InventoryManagementApi* | [**delete_inventory_device**](docs/InventoryManagementApi.md#delete_inventory_device) | **DELETE** /devices/{hostname} | Delete an existing device from the inventory 
*InventoryManagementApi* | [**edit_aws_region**](docs/InventoryManagementApi.md#edit_aws_region) | **PUT** /devices/aws/region/{hostname} | Edit/update an existing AWS region in the inventory
*InventoryManagementApi* | [**edit_ec2**](docs/InventoryManagementApi.md#edit_ec2) | **PUT** /devices/aws/ec2instance/{hostname} | Edit/update an existing AWS EC2 instance device in the inventory
*InventoryManagementApi* | [**edit_link_manager**](docs/InventoryManagementApi.md#edit_link_manager) | **PUT** /devices/linkmanager/{hostname} | Edit/update an existing link manager device in the inventory
*InventoryManagementApi* | [**edit_network_device**](docs/InventoryManagementApi.md#edit_network_device) | **PUT** /devices/network/{hostname} | Edit/update an existing network device in the inventory
*InventoryManagementApi* | [**edit_traffic_generator**](docs/InventoryManagementApi.md#edit_traffic_generator) | **PUT** /devices/trafficgenerator/{hostname} | Edit/update an existing traffic generator device in the inventory
*InventoryManagementApi* | [**edit_v_center**](docs/InventoryManagementApi.md#edit_v_center) | **PUT** /devices/vmware/vcenter/{hostname} | Edit/update an existing VMWare vCenter device in the inventory
*InventoryManagementApi* | [**edit_vm**](docs/InventoryManagementApi.md#edit_vm) | **PUT** /devices/vmware/vm/{hostname} | Edit/update an existing VMware VM device in the inventory
*InventoryManagementApi* | [**edit_vm_profile**](docs/InventoryManagementApi.md#edit_vm_profile) | **PUT** /devices/vmware/vmprofile/{hostname} | Edit/update an existing VMware VM Profile in the inventory
*InventoryManagementApi* | [**get_inventory_devices**](docs/InventoryManagementApi.md#get_inventory_devices) | **GET** /devices | Retrieve all devices that have been added to the inventory as well as search and filter the devices based on certain criteria
*LoginApi* | [**login**](docs/LoginApi.md#login) | **POST** /login | Login to the Toka controller and obtain a valid Toka API token
*SSLCertificateManagementApi* | [**configure_custom_certificate**](docs/SSLCertificateManagementApi.md#configure_custom_certificate) | **POST** /ssl/customCertificate | Configures the Tokalabs controller to use a new certificate (and private key associated with the certificate)
*SSLCertificateManagementApi* | [**configure_self_signed_certificate**](docs/SSLCertificateManagementApi.md#configure_self_signed_certificate) | **POST** /ssl/selfSignedCertificate | Generate a new self-signed SSL certificate and configure the Tokalabs server to use this newly generated self-signed SSL certificate
*SSLCertificateManagementApi* | [**generate_csr**](docs/SSLCertificateManagementApi.md#generate_csr) | **POST** /ssl/csr | Generate a new certificate signing request (CSR) and a private key associated with the CSR 
*TestBuilderApi* | [**abort_test_suite_v1**](docs/TestBuilderApi.md#abort_test_suite_v1) | **GET** /topology/{topology_name}/abort/suite/suite&#x3D;{suite_name}/user&#x3D;{username}/token&#x3D;{api_token} | Abort an already executing test suite
*TestBuilderApi* | [**abort_test_v1**](docs/TestBuilderApi.md#abort_test_v1) | **GET** /topology/{topology_name}/abort/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Abort an already executing test
*TestBuilderApi* | [**clone_test_suite_v1**](docs/TestBuilderApi.md#clone_test_suite_v1) | **GET** /topology/oldSuiteName&#x3D;{old_suite_name}/newSuiteName&#x3D;{new_suite_name}/topologyName&#x3D;{topology_name}/user&#x3D;{username}/token&#x3D;{api_token} | Clone a test suite.
*TestBuilderApi* | [**get_test_status_v1**](docs/TestBuilderApi.md#get_test_status_v1) | **GET** /topology/{topology_name}/status/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Retrieve status of a test
*TestBuilderApi* | [**get_test_suite_status_v1**](docs/TestBuilderApi.md#get_test_suite_status_v1) | **GET** /topology/{topology_name}/status/suite/suite&#x3D;{suite_name}/user&#x3D;{username}/token&#x3D;{api_token} | Retrieve status of a test suite.
*TestBuilderApi* | [**pause_test_v1**](docs/TestBuilderApi.md#pause_test_v1) | **GET** /topology/{topology_name}/pause/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Pause an already executing test
*TestBuilderApi* | [**resume_test_v1**](docs/TestBuilderApi.md#resume_test_v1) | **GET** /topology/{topology_name}/resume/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Resume an already paused test
*TestBuilderApi* | [**run_test_suite_v1**](docs/TestBuilderApi.md#run_test_suite_v1) | **GET** /topology/{topology_name}/run/suite/suite&#x3D;{suite_name}/user&#x3D;{username}/token&#x3D;{api_token} | Run a test suite
*TestBuilderApi* | [**run_test_v1**](docs/TestBuilderApi.md#run_test_v1) | **GET** /topology/{topology_name}/run/test/suite&#x3D;{suite_name}/test&#x3D;{testcase_id}/user&#x3D;{username}/token&#x3D;{api_token} | Run a test
*TopologyApi* | [**add_topology**](docs/TopologyApi.md#add_topology) | **POST** /topologies | Create a new topology
*TopologyApi* | [**delete_topology**](docs/TopologyApi.md#delete_topology) | **DELETE** /topologies/{topologyname} | Delete an existing topology
*TopologyApi* | [**edit_topology**](docs/TopologyApi.md#edit_topology) | **PUT** /topologies/{topologyname} | Edit/update an existing topology
*TopologyApi* | [**get_topology**](docs/TopologyApi.md#get_topology) | **GET** /topologies | Retrieve all topologies as well as search and filter topologies based on certain criteria
*TopologyApi* | [**release_topology_v1**](docs/TopologyApi.md#release_topology_v1) | **GET** /topology/{topology_name}/release/user&#x3D;{username}/token&#x3D;{api_token} | Release an already reserved topology
*TopologyApi* | [**reserve_topology_v1**](docs/TopologyApi.md#reserve_topology_v1) | **GET** /topology/{topology_name}/reserve/user&#x3D;{username}/token&#x3D;{api_token} | Reserve a topology


# Documentation For Models

 - [AddAWSRegionRequest](docs/AddAWSRegionRequest.md)
 - [AddAWSRegionRequestDeviceManagement](docs/AddAWSRegionRequestDeviceManagement.md)
 - [AddAWSRegionRequestDeviceManagementManagementInterfaces](docs/AddAWSRegionRequestDeviceManagementManagementInterfaces.md)
 - [AddAWSVpcRequest](docs/AddAWSVpcRequest.md)
 - [AddAWSVpcRequestOptions](docs/AddAWSVpcRequestOptions.md)
 - [AddConnectionsRequest](docs/AddConnectionsRequest.md)
 - [AddEC2Request](docs/AddEC2Request.md)
 - [AddLinkManagerRequest](docs/AddLinkManagerRequest.md)
 - [AddNetworkDeviceRequest](docs/AddNetworkDeviceRequest.md)
 - [AddTopologyRequest](docs/AddTopologyRequest.md)
 - [AddTopologyRequestAccessControl](docs/AddTopologyRequestAccessControl.md)
 - [AddTopologyRequestDevices](docs/AddTopologyRequestDevices.md)
 - [AddTopologyRequestIndirectConnections](docs/AddTopologyRequestIndirectConnections.md)
 - [AddTopologyRequestIntermediaries](docs/AddTopologyRequestIntermediaries.md)
 - [AddTopologyRequestOptions](docs/AddTopologyRequestOptions.md)
 - [AddTopologyRequestOptionsDeviceConnectionOptions](docs/AddTopologyRequestOptionsDeviceConnectionOptions.md)
 - [AddTopologyRequestReservationManagement](docs/AddTopologyRequestReservationManagement.md)
 - [AddTrafficGeneratorRequest](docs/AddTrafficGeneratorRequest.md)
 - [AddVCenterRequest](docs/AddVCenterRequest.md)
 - [AddVCenterRequestAutoDiscoveryOptions](docs/AddVCenterRequestAutoDiscoveryOptions.md)
 - [AddVCenterRequestDeviceManagement](docs/AddVCenterRequestDeviceManagement.md)
 - [AddVCenterRequestDeviceManagementManagementInterfaces](docs/AddVCenterRequestDeviceManagementManagementInterfaces.md)
 - [AddVMRequest](docs/AddVMRequest.md)
 - [AddVmProfileRequest](docs/AddVmProfileRequest.md)
 - [ConfigureCustomCertificateRequest](docs/ConfigureCustomCertificateRequest.md)
 - [DeviceManagementObj](docs/DeviceManagementObj.md)
 - [DeviceManagementObjAWS](docs/DeviceManagementObjAWS.md)
 - [DeviceManagementObjAWSManagementInterfaces](docs/DeviceManagementObjAWSManagementInterfaces.md)
 - [DeviceManagementObjFull](docs/DeviceManagementObjFull.md)
 - [DeviceManagementObjFullManagementInterfaces](docs/DeviceManagementObjFullManagementInterfaces.md)
 - [DeviceManagementObjManagementInterfaces](docs/DeviceManagementObjManagementInterfaces.md)
 - [DeviceManagementVMwareObj](docs/DeviceManagementVMwareObj.md)
 - [DeviceManagementVMwareObjManagementInterfaces](docs/DeviceManagementVMwareObjManagementInterfaces.md)
 - [EditAWSRegionRequest](docs/EditAWSRegionRequest.md)
 - [EditEC2Request](docs/EditEC2Request.md)
 - [EditLinkManagerRequest](docs/EditLinkManagerRequest.md)
 - [EditNetworkDeviceRequest](docs/EditNetworkDeviceRequest.md)
 - [EditTopologyRequest](docs/EditTopologyRequest.md)
 - [EditTrafficGeneratorRequest](docs/EditTrafficGeneratorRequest.md)
 - [EditVCenterRequest](docs/EditVCenterRequest.md)
 - [EditVMRequest](docs/EditVMRequest.md)
 - [EditVmProfileRequest](docs/EditVmProfileRequest.md)
 - [GenerateCSRRequest](docs/GenerateCSRRequest.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [PhysicalPortConnectionsObj](docs/PhysicalPortConnectionsObj.md)
 - [SnmpConfigurationObj](docs/SnmpConfigurationObj.md)
 - [TokaAPIResponse](docs/TokaAPIResponse.md)
 - [TokaAPIv1Response](docs/TokaAPIv1Response.md)
 - [VirtualInterfaceObj](docs/VirtualInterfaceObj.md)
 - [VmwareOptions](docs/VmwareOptions.md)


# Documentation For Authorization


# ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


# Author

support@tokalabs.com


