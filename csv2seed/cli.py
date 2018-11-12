#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from csv2seed.converter import run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', help='Path to CSV file')
    parser.add_argument('-s', '--spaces', help='Indentation to spaces', type=int)
    parser.add_argument('-t', '--tabulation', help='Indentation to tabulation', action='store_true')
    parser.add_argument('-d', '--delimiter', help='Delimiter to columns, default = ;')
    parser.add_argument('-m', '--model', help='Set name model')
    args = parser.parse_args()

    indented = " " * args.spaces if args.spaces else " " * 4
    indented = "\t" if args.tabulation else indented
    delimiter = args.delimiter or ";"
    model = args.model

    run(args.csvfile, indented, delimiter, model)


if __name__ == '__main__':
    main()
