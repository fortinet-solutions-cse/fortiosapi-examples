#!/usr/bin/env python
#firewall Address set up using FORTIOSAPI from Github

import logging
import sys

from fortiosapi import FortiOSAPI

formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger('fortiosapi')
hdlr = logging.FileHandler('testfortiosapi.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

def main():

    # Parse for command line argument for fgt ip
    if len(sys.argv) < 2:
        # Requires fgt ip and password
        print "Please specify fgt ip address"
        exit()

    # Initilize fgt connection
    ip = sys.argv[1]
    try:
        passwd = sys.argv[2]
    except:
        passwd = ''
    #fgt = FGT(ip)

    # Hard coded vdom value for all requests
    vdom = "root"

    # Login to the FGT ip

    fgt = FortiOSAPI()

    fgt.login(ip, 'fgtadmin', passwd, verify=False)

    data = {
        'name': "APItest",
        'subnet' : "10.20.0.0 255.255.255.0",
        'type': "ipmask"
        #        associated_interface: "port2"
    }
    fgt.set('firewall', 'address', vdom="root", data=data)
    fgt.logout()
if __name__ == '__main__':
  main()