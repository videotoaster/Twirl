#!/usr/bin/python3
#
#  Twirl package manager
#
#  Copyright 2021 VideoToaster <glitchyneopet@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the LGPL.
#

import sys
import requests

if len(sys.argv) < 3:
    # is it help?
    if sys.argv[1] == "hlp":
        print("Twirl Arguments:")
        print("upg   upgrade a package to the newest version")
        print("ins   install a new package")
        print("lst   redownload listings from repo")
        print("rem   remove a package")
        print("hlp   display help")
        print("Questions? E-mail me at glitchyneopet@gmail.com.")
        sys.exit(0) # exit gracefully
    # if not, display an error and exit ungracefully (throw error)
    print("Twirl requires 3 arguments.")
    print("Usage: twirl [ARGS] [PACKAGE]")
    print("For help, use twirl hlp.")
    sys.exit(1)

    for i in range(len(sys.argv)-2):
        print(sys.argv[i+2])
