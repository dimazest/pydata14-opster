#!/usr/bin/env python
"""My slightly more awesome script."""
import opster


@opster.command()
def greet(
    name=('n', 'Dima', 'Your name.'),
):
    """Greet a concrete person."""
    print 'Hello, {name}. How are you?'.format(name=name)


if __name__ == '__main__':
    greet.command()
