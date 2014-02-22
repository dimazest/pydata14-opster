#!/usr/bin/env python
"""My slightly more awesome script."""
import opster


@opster.command()
def sum(
    number=('n', 5, 'An interger.'),
    other=('', 1, 'Another interger.'),
):
    """Greet a concrete person."""
    print number + other


@opster.command()
def repeat(
    word=('w', 'London', 'The word to repeat.'),
    times=('t', 1, 'Number of time to repeat the word.'),
):
    """Repeat a word several times."""
    print ' '.join([word] * times)


if __name__ == '__main__':
    opster.dispatch()
