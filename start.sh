#!/bin/bash
set -x #echo on

python main.py
cp output.txt test/STS.output.headlines.txt
perl test/correlation.pl test/STS.gs.headlines.txt test/STS.gs.headlines.txt