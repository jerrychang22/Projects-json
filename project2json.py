#!/usr/bin/env python3
"""Script for simplyfing project descriptors for jc22.me website"""

import json

SRC = "./test/projects.txt"
DEST = "./test/projects.json"

def main():
    """Converts simple formatted project list into JSON"""
    output = {}
    output['items'] = []
    projects = []
    data = ''
    with open(SRC, 'r') as f:
        data = f.read()
        data = data.strip().split('\n@@@\n')
        length = len(data)
        for i in range(0, length):
            projects.append(data[i].split('\n'))
            projectd = {}
            projectd['id'] = length - i
            for item in projects[i]:
                keypair = item.split(':')
                projectd[keypair[0]] = keypair[1]
            output['items'].append(projectd)

    with open(DEST, 'w') as d:
        json.dump(output, d)
    return 0

if __name__ == '__main__':
    main()
