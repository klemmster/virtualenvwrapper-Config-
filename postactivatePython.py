#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
import sys
envName = os.path.basename(os.environ['VIRTUAL_ENV'])
for root, dirs, files in os.walk('/home/richy/Projects'):
    if envName in dirs:
        os.environ['PRE_VENV_ACTIVATE_DIR'] = os.getcwd()
        path = os.path.join(root, envName)
        print path #NECCCESARY for BASH
        sys.exit(0)
