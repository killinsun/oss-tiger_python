#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import sys
import subprocess


if __name__ == '__main__':
	cmd = "az vm list"
	proc = subprocess.call(cmd, shell=True)

