############################################
#
# Possible values for conf/outputs role
# 
# Follows Splunk outputs.conf.spec closely
#
############################################

splunk_outputs_conf:
  tcpout:
    defaultGroup: <target_group>, <target_group>, ...
    * The default group
    target_group:
      [target_group1:]
      * List of target groups

        useACK: [true|false]
        * Defaults to false
        server:
          - ["<server>:<port>"]
          - ["<server>:<port>"]
          - ...
          * List of servers to connect to

        sslPassword: <password>
        * Encrypted sslPassword
        * No default value

        sslCertPath: <path>
        * There is no default value.
        * Autogenerated file under $SPLUNK_HOME/etc/auth/server.pem

        sslRootCAPath: <path>
        * There is no default value.
        * Autogenerated file under $SPLUNK_HOME/etc/auth/ca.pem

        sslVerifyServerCert: [true|false]
        * Defaults to false.

        indexerDiscovery: <name>
        * Instructs the forwarder to fetch the list of indexers from the master node specified in the corresponding [indexer_discovery:<name>] stanza.

      [target_groupN:]
      ...

  indexer_discovery:
    * Indexer discovery settings

    [indexerDiscovery_target1:]
    * indexerDiscpvery_target list. Use name from tcpout stanza.

      pass4SymmKey: <password>
      * Encrypted Password

      master_uri: "<uri>"
      * Cluster Master URI
      * No default value
