#!/usr/bin/env python
# coding=utf-8

import sys
from optparse import OptionParser

if __name__ == '__main__':
    print sys.argv
    command = sys.argv[1]
    if command == "delete":
        print command
        args = sys.argv[2:]
        print args
    elif command == "clear":
        print command
    elif command == "calculate":
        print command
    else:
        print "not command %s" % (command)
    sys.exit(0)
    op = OptionParser()
    print op
    op.add_option(
        "--db",
        "--database",
        action="store",
        type="string",
        help="delete database",
        dest="db_name")
    options, args = op.parse_args()
    print options.db_name
    print args

