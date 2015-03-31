#!/usr/bin/env python
# coding=utf-8

import sys
import argparse
import log
from handler.calculate import *

logger = log.getMyLogger(__name__)

def del_db(args):
    print 'del-db %s' % (args.database_name)


def del_tb(args):
    print 'del-tb %s %s' % (args.database, args.table)


def clear(args):
    print 'clear %s %s' % (args.database, args.table)

'''
def calculate(args):
    print 'calculate %s %s %s %s' % (args.name, args.frm, args.to, args.sort)
'''

parser = argparse.ArgumentParser(prog='funds')
subparser = parser.add_subparsers(help='sub-command help')

# create the parser for sub-command 'delete-db'
parser_deleteDb = subparser.add_parser('delete-db', help='删除数据库')
parser_deleteDb.add_argument(
    'database_name',
    metavar='database_name',
    help='database name deleted')
parser_deleteDb.set_defaults(func=del_db)
'''
args = parser_deleteDb.parse_args(['xx'])
print args
args.func(args.database_name)
'''
# create the parser for sub-command 'delete-tb'
parser_deleteTb = subparser.add_parser('delete-tb', help='删除数据库中的表')
parser_deleteTb.add_argument('-db', '--database', help="要删除表的数据库名")
parser_deleteTb.add_argument('-t', '--table', help="要删除的表名")
parser_deleteTb.set_defaults(func=del_tb)
'''
args = parser_deleteTb.parse_args(['-db', 'xx', '-t', 'tname'])
print args
args.func(args.database, args.table)
'''

# create the parser for sub-command 'calculate'
parser_calculate = subparser.add_parser('calculate', help='计算基金在某个时间段内的增量率')
parser_calculate.add_argument('-n', '--name', default=None, help='name of a fund')
parser_calculate.add_argument('-f', '--frm', default=datetime.date.today(), help='date from')
parser_calculate.add_argument('-t', '--to', type=int, default=7, help='to date')
parser_calculate.add_argument('-c', '--count', type=int, default=5, help='show count')
parser_calculate.add_argument('-s', '--sort', default='-', help='sort result')
parser_calculate.set_defaults(func=handler_calc)

'''
args = parser_calculate.parse_args(['-f', '11', '-t', '22'])
print args
args.func(args.name, args.frm, args.to, args.sort)
#args.func(args.n, args.f, args.t, args.s)
'''
# create the parser for sub-command 'clear'
parser_clear = subparser.add_parser('clear', help='清空数据库表中的内容')
parser_clear.add_argument('-db', '--database', help='要清空表的数据库名')
parser_clear.add_argument('-t', '--table', help='要清空的数据库表名')
parser_clear.set_defaults(func=clear)

'''
args = parser_clear.parse_args(['-db', 'xx', '-t', 'tname'])
print args
#args.func(database=args.database, table=args.table)
args.func(args)
'''
command = {'delete_db': parser_deleteDb,
           'delete_tb': parser_deleteTb,
           'clear': parser_clear,
           'calculate': parser_calculate, }

if __name__ == '__main__':
    #print sys.argv
    if len(sys.argv) < 2:
        parser.parse_args(['-h'])

    sub_cmd = sys.argv[1]

    if command.has_key(sub_cmd):
        logger.debug(sys.argv)
        print sys.argv
        pargs = command[sub_cmd].parse_args(sys.argv[2:])
        pargs.func(pargs)
    else:
        #print "not found"
        parser.parse_args(['-h'])
