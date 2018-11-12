#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import splitext, basename, dirname
import csv
import argparse


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def run(csv_file, indented=" " * 4, delimiter=";", model=None):
    with open(csv_file, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=delimiter)
        seeder = ""
        for data in spamreader:
            attributes = list(data.keys())
            model = getFileName(csvfile.name).capitalize() if not model else model
            content = f"{model}::create([\n"
            for attribute in attributes:
                content += f'{indented}"{attribute}" => "{data[attribute]}",\n'
            content = f"{content[:-2]}\n]);"
            seeder += f"{content}\n"
        seeder_file = f"{dirname(csvfile.name)}/{getFileName(csvfile.name)}.txt"
        f  = open(seeder_file, "w")
        f.write(seeder)
        f.close()


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
