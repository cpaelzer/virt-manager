#!/usr/bin/env python3

import logging
import argparse

from virtinst import cli
from virtinst import NodeDevice


def debugnodedev(hostdevs):
    ''' Debug nodedev probig'''
    conn = cli.getConnection("qemu:///system")
    print("\nProbing devices now:\n")
    for hostdev in hostdevs:
        try:
            nodedev = NodeDevice.lookupNodedevFromString(conn, hostdev)
            print("OK   - hostdev %s maps to %s" % (hostdev, nodedev.name))
        except ValueError as err:
            print("FAIL - failed to query hostdev %s - %s" % (hostdev, err))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    PARSER = argparse.ArgumentParser(description='Test nodedev lookup')
    PARSER.add_argument('hostdevs', metavar='<HostDev>', nargs='+',
                        help='Hostdevs to probe')
    ARGS = PARSER.parse_args()
    debugnodedev(ARGS.hostdevs)
