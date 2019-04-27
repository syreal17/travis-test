#!/usr/bin/env python
import click
from calculator import Calculator


@click.group()
def cli():
    pass


@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def add(a, b):
    """Add a to b and return the sum"""
    c = Calculator()
    result = c.add(a, b)
    click.echo('{} + {} = {}'.format(a, b, result))


@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def sub(a, b):
    """Subtract b from a and return the difference"""
    c = Calculator()
    result = c.sub(a, b)
    click.echo('{} - {} = {}'.format(a, b, result))


@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def mul(a, b):
    """Multiply a and b and return the product"""
    c = Calculator()
    result = c.mul(a, b)
    click.echo('{} * {} = {}'.format(a, b, result))


@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def div(a, b):
    """Divide a by b and return the quotient"""
    c = Calculator()
    result = c.div(a, b)
    click.echo('{} / {} = {}'.format(a, b, result))


if __name__ == '__main__':
    cli()
