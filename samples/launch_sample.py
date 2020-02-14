"""This module serves as the launch point to run the samples

This module first setups up the Toka SDK API client by connecting
and logging into the Toka controller and then runs the available and
configured samples one after the other...
"""

import sys
import argparse
import getpass
import time
# import traceback

import tokasdk.models.physical_port_connections_obj
import tokasdk.models.add_topology_request_devices
import tokasdk.models.add_topology_request_intermediaries
import tokasdk.models.add_topology_request_indirect_connections

import libsamples.setup.setup_steps
import libsamples.inventory.inventory_device_mgmt
import libsamples.inventory.inventory_conn_mgmt
import libsamples.topology.topology_mgmt
import libsamples.testbuilder.testbuilder_mgmt

def setup_and_parse_args():
    """Setup and parse the command line arguments.

Parse the command line arguments and set the Toka controller IP,
username and password. If the above parameters are not provided as
arguments then prompt the user for the same    

    Returns:
        Namespace: Namespace object containing user supplied arguments
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-i', 
                            '--ip', 
                            help='IP address for your Toka controller',
                            action='store',
                            required=True)

    arg_parser.add_argument('-u', 
                            '--user', 
                            help='Username for your Toka controller',
                            action='store',
                            required=True)

    arg_parser.add_argument('-p', 
                            '--password', 
                            help='Password for your Toka controller',
                            action='store')


    user_supplied_args = arg_parser.parse_args()

    if (None == user_supplied_args.password):
        user_supplied_args.password = getpass.getpass('Enter the password for the Toka controller - ').strip('\r\n')
    
    return user_supplied_args


def run_samples(toka_controller_ip, toka_controller_user, toka_controller_passwd):
    """Invoke the samples from the samples library.
    
    Args:
        toka_controller_ip (str): IP address of the Toka controller
        toka_controller_user (str): Username to login to the Toka controller
        toka_controller_passwd (str): Password to login to the Toka controller
    
    Returns:
        bool: True if successful, False otherwise
    """
    toka_sdk_config_obj = libsamples.setup.setup_steps.configure_api_client(toka_controller_ip, True)

    if None == toka_sdk_config_obj:
        print('[launch_sample][run_samples] Failed to configure the Toka SDK object. Returning failure')
        return False


    toka_api_token = libsamples.setup.setup_steps.login(toka_sdk_config_obj, toka_controller_user, toka_controller_passwd)
    if None == toka_api_token:
        print('[launch_sample][run_samples] Failed to login to the Toka controller. Returning failure')
        return False

    print('[launch_sample][run_samples] Login success. API token - {0}'.format(toka_api_token))

    # Add a network device with the specified hostname 
    deviceAddedSuccessfully = libsamples.inventory.inventory_device_mgmt.add_network_device(
                                toka_api_configuration=toka_sdk_config_obj,
                                hostname='ap4122.lab.us.company.local'
    )
    if True != deviceAddedSuccessfully:
        print('[launch_sample][run_samples] Failed to add the network device to the Toka controller. Returning failure')
        return False

    # Add a network device with the specified hostname, type, ports
    # and asset id
    port_conn_obj = tokasdk.models.physical_port_connections_obj.PhysicalPortConnectionsObj(
                                type='External',
                                interfaces='eth0,eth1,eth2,eth3'
    )

    deviceAddedSuccessfully = libsamples.inventory.inventory_device_mgmt.add_network_device(
                                toka_api_configuration=toka_sdk_config_obj,
                                hostname='server8922.lab.us.company.local',
                                device_type='server',
                                device_asset_id='us-inv-8922',
                                device_ports=port_conn_obj
    )

    if True != deviceAddedSuccessfully:
        print('[launch_sample][run_samples] Failed to add the network device to the Toka controller. Returning failure')
        return False


    # Search devices whose names contain the string 'ap'
    listOfMatchingDevices = libsamples.inventory.inventory_device_mgmt.search_devices(
                    toka_api_configuration=toka_sdk_config_obj,
                    hostname='ap'
    )
    if None == listOfMatchingDevices:
        print('[launch_sample][run_samples] Failed to search devices on the Toka controller. Returning failure')
        return False

    for matchingDevice in listOfMatchingDevices:
        print('[launch_sample][run_samples] Device name - {0}'.format(matchingDevice['hostname']))


    # Search devices whose names contain the string 'ap' and are
    # reserved
    listOfMatchingDevices = libsamples.inventory.inventory_device_mgmt.search_devices(
                    toka_api_configuration=toka_sdk_config_obj,
                    hostname='ap',
                    device_reservation_status='reserved'
    )

    if None == listOfMatchingDevices:
        print('[launch_sample][run_samples] Failed to search devices on the Toka controller. Returning failure')
        return False

    for matchingDevice in listOfMatchingDevices:
        print('[launch_sample][run_samples] Device name - {0}, Device reservation status - {1}'.format(matchingDevice['hostname'], matchingDevice['reservationDetails']['reservationStatus']))

    # Delete a device with the specified hostname
    deviceDeletedSuccessfully = libsamples.inventory.inventory_device_mgmt.delete_device(
                                toka_api_configuration=toka_sdk_config_obj,
                                hostname='ap4122.lab.us.company.local'
    )
    if True != deviceDeletedSuccessfully:
        print('[launch_sample][run_samples] Failed to delete the device from the Toka controller. Returning failure')
        return False


    # Add a connection between the specified devices and ports    
    connectionIdForNewConnection = libsamples.inventory.inventory_conn_mgmt.add_connection(
                                    toka_api_configuration=toka_sdk_config_obj,
                                    src_hostname='server8922.lab.us.company.local',
                                    src_port_id='eth0',
                                    target_hostname='switch9461.lab.us.company.local',
                                    target_port_id='eth1')

    if None == connectionIdForNewConnection:
        print('[launch_sample][run_samples] Failed to add the connection to the Toka controller. Returning failure')
        return False

    # Add a connection between the specified devices and ports    
    connectionId2ForNewConnection = libsamples.inventory.inventory_conn_mgmt.add_connection(
                                    toka_api_configuration=toka_sdk_config_obj,
                                    src_hostname='server8922.lab.us.company.local',
                                    src_port_id='eth2',
                                    target_hostname='ati-L1-4912',
                                    target_port_id='port1.0.7')

    if None == connectionId2ForNewConnection:
        print('[launch_sample][run_samples] Failed to add the connection to the Toka controller. Returning failure')
        return False

    # Search direct connections involving 'server8922.lab.us.company.local' 
    listOfMatchingConnections = libsamples.inventory.inventory_conn_mgmt.search_direct_connections(
                    toka_api_configuration=toka_sdk_config_obj,
                    hostname='server8922.lab.us.company.local'
    )
    if None == listOfMatchingConnections:
        print('[launch_sample][run_samples] Failed to search connections on the Toka controller. Returning failure')
        return False

    for matchingConnection in listOfMatchingConnections:
        print('[launch_sample][run_samples] Connection id - {0}, Source device - {1}, '
            'Target Device -{2}'.format(
                            matchingConnection['connectionId'], 
                            matchingConnection['sourceHost'],
                            matchingConnection['targetHost']))


    # Fetch all direct connections in the inventory
    listOfMatchingConnections = libsamples.inventory.inventory_conn_mgmt.search_direct_connections(
                    toka_api_configuration=toka_sdk_config_obj
    )
    if None == listOfMatchingConnections:
        print('[launch_sample][run_samples] Failed to search connections on the Toka controller. Returning failure')
        return False

    for matchingConnection in listOfMatchingConnections:
        print('[launch_sample][run_samples] Connection id - {0}, Source device - {1}, '
            'Target Device -{2}'.format(
                            matchingConnection['connectionId'], 
                            matchingConnection['sourceHost'],
                            matchingConnection['targetHost']))


    # Delete the connection with the specified connection id
    connectionDeletedSuccessfully = libsamples.inventory.inventory_conn_mgmt.delete_connection(
                    toka_api_configuration=toka_sdk_config_obj,
                    connection_id=connectionIdForNewConnection)

    if True != connectionDeletedSuccessfully:
        print('[launch_sample][run_samples] Failed to delete the connection from the Toka controller. Returning failure')
        return False


    # Create a topology with the specified devices
    device_server = tokasdk.models.add_topology_request_devices.AddTopologyRequestDevices(
                name='server8922.lab.us.company.local',
                abstract_id='DUT1')

    device_switch = tokasdk.models.add_topology_request_devices.AddTopologyRequestDevices(
                name='switch9461.lab.us.company.local',
                abstract_id='DUT2')

    topoCreatedSuccessfully = libsamples.topology.topology_mgmt.create_topology(
            toka_api_configuration=toka_sdk_config_obj,
            topo_name='topo-sample-1',
            list_of_devices_to_add_to_topo=[device_server, device_switch]
    )

    if True != topoCreatedSuccessfully:
        print('[launch_sample][run_samples] Failed to create the topology. Returning failure')
        return False

    # Create a topology with the specified devices that are connected via a
    # Link Manager
    device_server = tokasdk.models.add_topology_request_devices.AddTopologyRequestDevices(
                name='server8922.lab.us.company.local',
                abstract_id='DUT1')

    device_trgen = tokasdk.models.add_topology_request_devices.AddTopologyRequestDevices(
                name='trgen2012.lab.us.company.local',
                abstract_id='TG1')

    server_linkmgr_connection_intermediaries = ( 
        tokasdk.models.add_topology_request_intermediaries.AddTopologyRequestIntermediaries(
                source_host='server8922.lab.us.company.local',
                source_port_id='eth2',
                target_host='ati-L1-4912',
                target_port_id='port1.0.7'
    ))

    trgrn_linkmgr_connection_intermediaries = (
        tokasdk.models.add_topology_request_intermediaries.AddTopologyRequestIntermediaries(
                source_host='ati-L1-4912',
                source_port_id='port1.0.8',
                target_host='trgen2012.lab.us.company.local',
                target_port_id='port1'
    ))

    server_trgen_connection_obj = (
        tokasdk.models.add_topology_request_indirect_connections.AddTopologyRequestIndirectConnections(
        intermediaries=[server_linkmgr_connection_intermediaries, 
                        trgrn_linkmgr_connection_intermediaries]
    ))

    topoCreatedSuccessfully = libsamples.topology.topology_mgmt.create_topology(
            toka_api_configuration=toka_sdk_config_obj,
            topo_name='topo-sample-2',
            list_of_devices_to_add_to_topo=[device_server, device_trgen],
            list_of_indirect_connections_to_be_added_to_topo=[server_trgen_connection_obj]
    )

    if True != topoCreatedSuccessfully:
        print('[launch_sample][run_samples] Failed to create the topology. Returning failure')
        return False


    # Search topologies whose name starts with the string 'topo'
    list_of_matching_topologies = libsamples.topology.topology_mgmt.search_topologies(
                    toka_api_configuration=toka_sdk_config_obj,
                    topo_name='topo'
    )
    if None == list_of_matching_topologies:
        print('[launch_sample][run_samples] Failed to search topologies on the Toka controller. Returning failure')
        return False

    for matching_topology in list_of_matching_topologies:
        print('[launch_sample][run_samples] Topology name - {0}'.format(matching_topology['name']))


    # Search topologies whose name starts with the string 'topo' 
    # and are reserved
    list_of_matching_topologies = libsamples.topology.topology_mgmt.search_topologies(
                    toka_api_configuration=toka_sdk_config_obj,
                    topo_name='topo',
                    topo_reservation_status='reserved'
    )
    if None == list_of_matching_topologies:
        print('[launch_sample][run_samples] Failed to search topologies on the Toka controller. Returning failure')
        return False

    for matching_topology in list_of_matching_topologies:
        print('[launch_sample][run_samples] Topology name - {0}, Topology reservation status - {1}'.format(
                    matching_topology['name'], 
                    matching_topology['reservationDetails']['reservationStatus']))


    # Delete a topology with the specified name
    topologyDeletedSuccessfully = libsamples.topology.topology_mgmt.delete_topology(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-sample-1'
    )
    if True != topologyDeletedSuccessfully:
        print('[launch_sample][run_samples] Failed to delete the topology from the Toka controller. Returning failure')
        return False


    # Reserve a topology with the specified name
    topologyReservedSuccessfully = libsamples.topology.topology_mgmt.reserve_topology(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup'
    )
    if True != topologyReservedSuccessfully:
        print('[launch_sample][run_samples] Failed to reserve the topology on the Toka controller. Returning failure')
        return False

    # Run a test with the specified name
    testStartedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.run_test(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting',
                                test_id='TestNetworkPacketLoss'
    )

    if True != testStartedSuccessfully:
        print('[launch_sample][run_samples] Failed to start the test on the Toka controller. Returning failure')
        return False
    
    # Sleep a couple of seconds to ensure that the test has started
    time.sleep(2)

    # Pause a test with the specified name
    testPausedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.pause_test(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting',
                                test_id='TestNetworkPacketLoss'
    )

    if True != testPausedSuccessfully:
        print('[launch_sample][run_samples] Failed to pause the test on the Toka controller. Returning failure')
        return False

    # Resume a test with the specified name
    testResumedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.resume_test(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting',
                                test_id='TestNetworkPacketLoss'
    )

    if True != testResumedSuccessfully:
        print('[launch_sample][run_samples] Failed to resume the test on the Toka controller. Returning failure')
        return False


    # Abort a test with the specified name
    testAbortedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.abort_test(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting',
                                test_id='TestNetworkPacketLoss'
    )

    if True != testAbortedSuccessfully:
        print('[launch_sample][run_samples] Failed to abort the test on the Toka controller. Returning failure')
        return False

    # Fetch run status for the test with the specified name
    testRunStatus = libsamples.testbuilder.testbuilder_mgmt.fetch_test_status(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting',
                                test_id='TestNetworkPacketLoss'
    )

    if None == testRunStatus:
        print('[launch_sample][run_samples] Failed to fetch the test run status on the Toka controller. Returning failure')
        return False


    # Run a test suite with the specified name
    testSuiteStartedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.run_test_suite(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting'
    )

    if True != testSuiteStartedSuccessfully:
        print('[launch_sample][run_samples] Failed to start the test suite on the Toka controller. Returning failure')
        return False


    # Sleep a couple of seconds to ensure that the test suite has started
    time.sleep(2)

    # Abort a test suite with the specified name
    testSuiteAbortedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.abort_test_suite(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting',
    )

    if True != testSuiteAbortedSuccessfully:
        print('[launch_sample][run_samples] Failed to abort the test suite on the Toka controller. Returning failure')
        return False


    # Fetch run status for the test suite with the specified name
    testSuiteRunStatus = libsamples.testbuilder.testbuilder_mgmt.fetch_test_suite_status(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_name='TrafficTesting'
    )

    if None == testSuiteRunStatus:
        print('[launch_sample][run_samples] Failed to fetch the test suite run status on the Toka controller. Returning failure')
        return False


    # Clone a test suite with the specified name
    testSuiteClonedSuccessfully = libsamples.testbuilder.testbuilder_mgmt.clone_test_suite(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup',
                                test_suite_to_clone_from='TrafficTesting',
                                test_suite_to_clone_to='TrafficTesting4'
    )

    if True != testSuiteClonedSuccessfully:
        print('[launch_sample][run_samples] Failed to clone the test suite on the Toka controller. Returning failure')
        return False

    # Release a topology with the specified name
    topologyReleasedSuccessfully = libsamples.topology.topology_mgmt.release_topology(
                                toka_api_configuration=toka_sdk_config_obj,
                                topo_name='topo-us-lab-setup'
    )
    if True != topologyReleasedSuccessfully:
        print('[launch_sample][run_samples] Failed to reserve the topology on the Toka controller. Returning failure')
        return False

    return True


def main():
    """Main enty point to connect to the Toka controller and run the samples
    """
    user_supplied_args = setup_and_parse_args()
    if None == user_supplied_args:
        print('[launch_sample][main] Failed to parse arguments. Returning failure')
        sys.exit(1)

    if (None == user_supplied_args.ip or 
        0 == len(user_supplied_args.ip) or 
        None == user_supplied_args.user 
        or 0 == len(user_supplied_args.user) or
        None == user_supplied_args.password or
        0 == len(user_supplied_args.password)):
        print('[launch_sample][main] Either the Toka controller IP address, '
              'username and/or password was not provided. Returning failure')
        sys.exit(1)

    
    successfully_run_samples = run_samples(user_supplied_args.ip, user_supplied_args.user, user_supplied_args.password)
    if (True == successfully_run_samples):
        print('[launch_sample][main] Samples executed successfully...')
        sys.exit(0)
    else:
        sys.exit(1)


main()
