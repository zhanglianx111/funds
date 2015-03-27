#!/usr/bin/env python
# coding=utf-8

import sys
import string 
import argparse

def del_db(args):
    print 'del-db %s' % args

def del_tb(db, tb):
    print 'del-tb %s %s' % (db, tb)

def clear(db, tb):
    print 'clear %s %s' % (db, tb)

def calculate(name, f, to, sort):
    print 'calculate %s %s %s %s' % (name, f, to, sort)

parser = argparse.ArgumentParser(prog='funds')
#parser.add_argument('--foo', action='store_true', help='foo help')
'''
subparser = parser.add_subparsers(title='funds',
                                  description='valid subcommands',
                                  help='addtional help',
                                  dest='subparser_name')
'''
subparser = parser.add_subparsers(help='sub-command help')

# create the parser for sub-command 'delete-db'
parser_deleteDb = subparser.add_parser('delete-db', help='删除数据库')
#parser_delete.add_argument('-db', help="要删除的数据库名")
parser_deleteDb.add_argument('database_name', metavar='database_name', help='database name deleted')
parser_deleteDb.set_defaults(func=del_db)

args = parser_deleteDb.parse_args(['xx'])
args.func(args.database_name)

# create the parser for sub-command 'delete-tb'
parser_deleteTb = subparser.add_parser('delete-tb', help='删除数据库中的表')
parser_deleteTb.add_argument('-db', help="要删除表的数据库名")
parser_deleteTb.add_argument('-t', help="要删除的表名")
parser_deleteTb.set_defaults(func=del_tb)

args = parser_deleteTb.parse_args(['-db','xx', '-t', 'tname'])
args.func(args.db, args.t)

# create the parser for sub-command 'clear'
parser_clear = subparser.add_parser('clear', help='清空数据库表中的内容')
parser_clear.add_argument('-db', help='要清空表的数据库名')
parser_clear.add_argument('-t', help='要清空的数据库表名')
parser_clear.set_defaults(func=clear)

args = parser_clear.parse_args(['-db','xx', '-t', 'tname'])
args.func(args.db, args.t)

# create the parser for sub-command 'calculate'
parser_calculate = subparser.add_parser('calculate', help='计算基金在某个时间段内的增量率')
parser_calculate.add_argument('-n', default=None, help='name of a fund' )
parser_calculate.add_argument('-f', help='date from')
parser_calculate.add_argument('-t', help='to date')
parser_calculate.add_argument('-s', default='-', help='sort result')
parser_calculate.set_defaults(func=calculate)


args = parser_calculate.parse_args(['-f', '11', '-t','22' ])
print args
args.func(args.n, args.f, args.t, args.s)

#arg = parser.parse_args(['-h'])
#arg = parser.parse_args(['clear','-h'])
#arg = parser.parse_args(['delete-db','-h'])
#arg = parser.parse_args(['delete-tb','-h'])
#arg = parser.parse_args(['calculate','-h'])



