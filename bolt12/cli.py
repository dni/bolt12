""" bolt12 CLI """

import sys

import click

from .decode import decode as bolt12_decode

# disable tracebacks on exceptions
sys.tracebacklimit = 0


@click.group()
def command_group():
    """
    Python CLI for BOLT12 invoices
    decode bolt12 invoices
    """


@click.command()
@click.argument("bolt12", type=str)
def decode(bolt12):
    """
    decode a bolt12 invoice
    """
    decoded = bolt12_decode(bolt12)
    click.echo(decoded)


def main():
    """main function"""
    command_group.add_command(decode)
    command_group()


if __name__ == "__main__":
    main()
