#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import splitext, basename, dirname
import csv

file_csv = argv[1]


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def run():
    with open(file_csv, newline='') as csvfile:
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


run()
