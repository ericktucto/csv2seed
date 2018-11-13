#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from csv2seed.converter import run


@click.command()
@click.argument('csvfile')
@click.option('-s', '--spaces', help='Indentation to spaces', type=int,
              default=4)
@click.option('-t', '--tabulation', help='Indentation to tabulation',
              is_flag=True)
@click.option('-d', '--delimiter', help='Delimiter to columns, default = ;',
              default=";")
@click.option('-m', '--model', help='Set name model', default=None)
@click.option('-a', '--attributes',
              help='Set attributes to model')
@click.option('-H', '--hasnt-header', help='Indicate if it have a header',
              is_flag=True, default=True)
def main(csvfile, spaces, tabulation, delimiter, model, attributes,
         hasnt_header):
    attributes = tuple(attributes.split(",")) if attributes else None
    indented = "\t" if tabulation else " " * spaces

    run(csvfile, indented, delimiter, model, attributes, hasnt_header)


if __name__ == '__main__':
    main()
