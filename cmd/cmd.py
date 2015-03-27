#!/usr/bin/env python
# coding=utf-8

import sys
import argparse

def d(args):
    print 'd %s' % args

def c(args):
    print 'c %s' % args

def cc(args):
    print 'cc %s' % args

parser = argparse.ArgumentParser(prog='fund')
parser.add_argument('--foo', action='store_true', help='foo help')
subparser = parser.add_subparsers(help='sub-command help')

# create the parser for sub-command 'delete'
parser_delete = subparser.add_parser('delete', help='delete help')
parser_delete.add_argument('-db', type=string, help='bar help')
parser_delete.set_defaults(func=d)

# create the parser for sub-command 'clear'
parser_clear = subparser.add_parser('clear', help='clear help')
parser_clear.add_argument('-t', type=string, help='-t help')
parser_clear.set_defaults(func=c)

# create the parser for sub-command 'calculate'
parser_calculate = subparser.add_parser('calculate', help='calculate help')
parser_calculate.add_argument('--x', type=string, help='x help')
parser_calculate.set_defaults(func=cc)

args = parser.parse_args('delete -db db_name'.split())
args.func(args)



