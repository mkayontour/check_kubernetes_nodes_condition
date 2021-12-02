#!/usr/bin/env python

# Author: Thilo Wening <thilo.wening@netways.de>
# Company: NETWAYS GmbH
# Date: 02.12.2021

import argparse
import sys

from kubernetes import config, client

def main():
    args = argparse.ArgumentParser(description='Check health of Kubernetes Nodes')
    args.add_argument('-v', '--version', action='version', version='1.0')
    args.add_argument('--kube-config', help='Path to the kubernetes config file')
    args = args.parse_args()

    kube_config = args.kube_config
    nodes = []

    config.load_kube_config(kube_config)
    kube = client.CoreV1Api()
    res = ""

    for node in kube.list_node().items:
        nodes.append(node)

        res += 'Node: ' + node.metadata.name + '\n'
        for condition in node.status.conditions:
            if (condition.type == 'Ready' and condition.status != 'True') \
                or (condition.type != 'Ready' and condition.status != 'False'):
                res += '  [Critical] ' + condition.type + ': ' + condition.message + '\n'
            else:
                res += '  [OK] ' + condition.type + ': ' + condition.message + '\n'

    print(res)
    if "Critical" in res:
      sys.exit(2)
    else:
      sys.exit(0)

if __name__ == '__main__':
    main()
