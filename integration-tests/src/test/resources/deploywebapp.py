# Copyright 2018, Oracle Corporation and/or its affiliates.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.

connect(sys.argv[1],sys.argv[2],sys.argv[3])
print 'cluster-1-NAP LA: ' + get('/Servers/managed-server1/NetworkAccessPoints/cluster-1-NAP/ListenAddress')
deploy(sys.argv[4],sys.argv[5],sys.argv[6],upload='false',remote='false')
