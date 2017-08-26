#!/usr/bin/env python2
import sys
f = open(sys.argv[1],"r")
print f.read()[::-1]
