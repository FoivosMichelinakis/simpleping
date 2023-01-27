#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Author: Foivos Michelinakis
# Date: January 2021
# License: GNU General Public License v3
# Developed for use by the EU H2020 MONROE project


import subprocess
import time
import json
import shutil

RESULTS_DIR = "/monroe/results/"
OUTPUTFILE = "/opt/simpleping/simplepingResults.txt"
TARGETINTERFACE = "op0"

try:
    with open("/monroe/config", "r") as fd:
        configurationParameters = json.load(fd)
except Exception as e:
    print("Cannot retrive /monroe/config {}".format(e))
    print("Using default parameters.......")
    configurationParameters = {"target": "www.google.com", "numberOfPings": 10}
    usingDefaults = True



cmd = ["ping", "-I", TARGETINTERFACE, "-c", str(configurationParameters['numberOfPings']), configurationParameters['target']]
output = subprocess.check_output(cmd).decode('ascii')

with open(OUTPUTFILE, 'a') as rt_tables:
    rt_tables.write(output)


shutil.copy2("/opt/simpleping/simplepingResults.txt", RESULTS_DIR + "simplepingResults.txt" + ".tmp")
shutil.move(RESULTS_DIR + "simplepingResults.txt" + ".tmp", RESULTS_DIR + "simplepingResults.txt")
# os.remove("/opt/simpleping/simplepingResults.txt")


time.sleep(3600)