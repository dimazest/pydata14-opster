#!/usr/bin/env python
"""My awesome script."""
import opster


@opster.command()
def hello():
    """A hello world implementation."""
    print 'Hello world!'


if __name__ == '__main__':
    hello.command()
