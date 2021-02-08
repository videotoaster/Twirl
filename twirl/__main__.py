#!/usr/bin/python3
#
#  Twirl package manager
#
#  Copyright 2021 VideoToaster <glitchyneopet@gmail.com>
#  Copyright 2021 Thewarsawpakt <thewarsawpakt@gmail.com>
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the LGPL.

import argparse

parser = argparse.ArgumentParser(
    "Twirl Package Manager",
    description = "Invoke the twirl package manager."
)
parser.add_argument(
    "-i",
    help = "Installs a package with the specified name.",
    type = str,
)

parser.add_argument(
    "-u",
    help = "Performs a partial upgrade with specified package. WARNING: THIS MAY CAUSE SYSTEM DAMAGE.",
    type = str
)

parser.add_argument(
    "-U",
    help = "Performs a full system upgrade.",
    type = str
)

parser.add_argument(
    "-l",
    help = "Updates package listings.",
    type = str
)

parser.add_argument(
    "-r",
    help = "Removes a package but not it's dependencies.",
    type = str
)
parser.add_argument(
    "-R",
    help = "Removes a package and it's dependencies which aren't required by another program.",
    type = str
)

parser.add_argument(
    "-d",
    help = "Removes dependencies even if they are required by another program. WARNING: THIS MAY CAUSE SYSTEM DAMAGE.",
    type = str
)

args = parser.parse_args()

if (args.i and (args.u or args.r or args.R or args.d or args.l)) or (args.u and (args.R or args.d or args.r or args.i or args.l)) or (args.r and (args.l or args.i or args.u)):
    print("Please read the usage.")
    exit()