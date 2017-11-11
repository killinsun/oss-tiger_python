#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import sys
import subprocess


if __name__ == '__main__':
	cmd = "az vm list-ip-addresses"
	proc = subprocess.getoutput(cmd)

	datadict = json.loads(proc)

	i = 0
	for resource in datadict:
		print( resource[{virtualMachine: name

		k)
