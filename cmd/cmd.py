#!/usr/bin/env python
# coding=utf-8

import sys
import argparse

parser = argparse.ArgumentParser(prog='fund')
parser.add_argument('--foo', action='store_true', help='foo help')
subparser = parser.add_subparsers(help='sub-command help')

# create the parser for sub-command 'delete'
parser_delete = subparser.add_parser('delete', help='delete help')
parser_delete.add_argument('bar', type=int, help='bar help')

# create the parser for sub-command 'clear'
parser_clear = subparser.add_parser('clear', help='clear help')
parser_clear.add_argument('--baz', choices='xyz', help='baz help')

# create the parser for sub-command 'calculate'

parser_calculate = subparser.add_parser('calculate', help='calculate help')
parser_calculate.add_argument('--x', choices='nnn', help='x help')




