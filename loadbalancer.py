#!/usr/bin/env python
#firewall Address set up using FORTIOSAPI from Github

import logging
import sys

from fortiosapi import FortiOSAPI
from pprint import pprint
import json
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger('fortiosapi')
hdlr = logging.FileHandler('testfortiosapi.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

def usage():
    print("Please use user:password@ip as a parameter")
    exit()

def main():

    # Parse for command line argument for fgt ip
    if len(sys.argv) < 2:
        # Requires fgt ip and password
        usage()

    # Initialize fgt connection
    ip = sys.argv[1].split("@")[1]
    try:
        user_passwd = sys.argv[1].split("@")[0]
    except:
        usage()
    try:
        user = user_passwd.split(":")[0]
        password = user_passwd.split(":")[1]
    except:
        usage()

    # Hard coded vdom value for all requests
    vdom = "root"

    # Login to the FGT ip

    fgt = FortiOSAPI()
    fgt.login(ip, user, password=password, verify=False)

    data = {
          "name": "APItestVIP",
          "type": "server-load-balance",
          "ldb-method": "least-rtt",
          "extintf": "port1",
          "server-type":  "http",
          "monitor": [ {"name": "http"}],
          "extport": "88",
          "realservers": [
            { "id": 1, "ip": "198.51.100.42",
              "port": 80, "status": "active"},
              {"id": 2, "ip": "10.40.0.25",
               "port": 80, "status": "active"}
          ]
        }

    ret = fgt.set('firewall', 'vip', vdom="root", data=data)
    pprint(ret)
    ##to do a get https://104.47.161.74/api/v2/monitor/firewall/load-balance/select/?count=300 "count is mandatory

    if ret['http_status'] == 200:
        pprint(fgt.monitor('firewall', 'load-balance',
                                  mkey='select', vdom='root',parameters='count=20')['results'])
        fgt.logout()
        exit(0)
    else:
        print("error: %s " % ret['status'])
        fgt.logout()
        exit(2)
if __name__ == '__main__':
  main()