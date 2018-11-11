#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import splitext, basename, dirname
import csv
import argparse


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def run(csv_file):
    with open(csv_file, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=";")
        seeder = ""
        for data in spamreader:
            attributes = list(data.keys())
            intentation = " " * 4
            classModel = getFileName(csvfile.name).capitalize()
            content = f"{classModel}::create([\n"
            for attribute in attributes:
                content += f'{intentation}"{attribute}" => "{data[attribute]}",\n'
            content = f"{content[:-2]}\n]);"
            seeder += f"{content}\n"
        seeder_file = f"{dirname(csvfile.name)}/{getFileName(csvfile.name)}.txt"
        f  = open(seeder_file, "w")
        f.write(seeder)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', help='Path to CSV file')
    args = parser.parse_args()
    run(args.csvfile)

if __name__ == '__main__':
    main()
