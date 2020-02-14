# Toka SDK Samples
Toka SDK samples serve as a library for common operations that can be accomplished using the Toka SDK API client as well as demonstrate using the the Toka SDK API client. Note that the Toka SDK API client supports a lot more operations (than that covered by the Toka SDK samples here) and allows for a lot more programmatic control of the Toka controller

### Licensing
All samples are licensed under Apache License 2.0

### Running Samples
A launch script `launch_sample.py` is included which invokes all of the samples and should be used as a starting point to run the available samples

### Samples Index
The samples library currently support the following  - 

1.  Setup
    *  Setting up the Toka SDK API client
    *  Logging into the Toka controller and retrieving the API token
2.  Inventory Management
    *  Add Device
        *  Add a network device with the specified hostname 
        *  Add a network device with the specified hostname, type, ports and asset id
    *  Search Devices
        *  Search devices using hostname
        *  Search devices using hostname and reservation status
    *  Delete Device
        *  Delete device using hostname
    *  Add Connection
        *  Add a connection between the specified devices and ports
    *  Search Connections
        *  Fetch all direct connections in the inventory
        *  Search direct connections involving a specific host
    *  Delete Connection
        *  Delete connection using connection id
3.  Topology Management 
    *  Create Toology
        *  Create a topology with the specified devices
        *  Create a topology with the specified devices that are connected via a Link Manager
    *  Search Topologies
        *  Search topologies using topology name
        *  Search topologies using topology name and reservation status
    *  Delete Topology
        *  Delete a topology using topology name
    *  Reserve Topology
        *  Reserve a topology using topology name
    *  Release Topology
        *  Release a topology using topology name
4.  Test Management 
    *  Run Test
        *  Run a test using test id 
    *  Abort Test
        *  Abort an already running test using test id 
    *  Pause Test
        *  Pause an already running test using test id 
    *  Resume Test
        *  Resume an already paused test using test id 
    *  Fetch Test Run Status
        *  Fetch the last run status of a test using test id 
    *  Run Test Suite
        *  Run a test suite using test suite name
    *  Abort Test Suite
        *  Abort an already running test suite using test suite name
    *  Fetch Test Suite Run Status
        *  Fetch the last run status of a test suite using test suite name
    *  Clone Test Suite
        *  Clone a test suite using test suite name

