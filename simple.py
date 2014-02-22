#!/usr/bin/env python
"""My awesome script."""
import opster


@opster.command()
def hello():
    """A hello word implementation."""
    print 'Hello world!'


@opster.command()
def greet(
    name=('n', 'Dima', 'Your name.'),
):
    """Greet a concrete person."""
    print 'Hello, {name}. How are you?'.format(name=name)


if __name__ == '__main__':
    hello.command()
