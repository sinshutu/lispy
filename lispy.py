#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from functools import reduce

# BNF
# atom              := symbol
#                    | number
#                    | string
# symbol            := 'atom
# number            := (+|-)+[0-9]\.[0-9]
# string            := ".*"
# s_expression      := atom
#                    | ()
#                    | (expression)
# s_expression_list := s_expression..
# expression        := function s_expression_list

# token regexs
number_pattern = re.compile(r'(^[1-9][0-9]*$)')
# string_pattern = re.compile(r'([A-Za-z][A-Za-z0-9]*)')
exp_pattern = re.compile(r'^\( *([^ ]*) *(.*)?\)$')
operator_pattern = re.compile(r'^([+-/\*])$')

DEBUG = False


def s_expression(source):
    if DEBUG:
        print('s_expression: ' + source)
    if source == '':
        return ''
    number_token = number_pattern.match(source)
    if number_token:
        return int(number_token.groups()[0])
    exp_token = exp_pattern.match(source)
    if exp_token:
        return expression(exp_token)
    return 'parse err'


def expression(exp_token):
    function = exp_token.groups()[0]
    s_exp_list = exp_token.groups()[1]
    if DEBUG:
        print('operator: ' + function)
        print('s_exp_list: ' + s_exp_list)
    if function == '':
        return 'nil'
    tokens = s_expression_list(s_exp_list)
    if DEBUG:
        print('tokens: ', end='')
        print(tokens)
    operator_token = operator_pattern.match(function)
    if operator_token:
        return calc(operator_token.groups()[0],
                    map(s_expression, tokens))
    return 'nil'


def s_expression_list(source):
    tmp_list = source.split()
    s_exp_list = []
    i = 0
    while i < len(tmp_list):
        tmp_exp = tmp_list[i]
        if tmp_exp[0] == '(':
            count = 1
            while count != 0:
                i += 1
                tmp_exp += ' ' + tmp_list[i]
                count -= 1 if tmp_list[i][-1] == ')' else 0
        i += 1
        s_exp_list.append(tmp_exp)
    return s_exp_list


def calc(operator, values):
    if DEBUG:
        print('calc')
    if operator == '+':
        return sum(values)
    if operator == '-':
        return reduce((lambda a, b: a - b), values)
    if operator == '*':
        return reduce((lambda a, b: a * b), values)
    if operator == '/':
        return reduce((lambda a, b: a / b), values)


def run():
    print('-----------')
    print('Hello LisPy')
    print('-----------')
    print('')
    while True:
        print('> ', end='')
        out = s_expression(input())
        print(out)


if __name__ == '__main__':
    run()
