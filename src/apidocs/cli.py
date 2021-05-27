# -*- coding: utf-8 -*-
import click

from utils import import_string

@click.group()
@click.version_option()
def main():
    """
    UPDATERS
 """

main.add_command(import_string("apidocs.run.generate"))