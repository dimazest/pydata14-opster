from IPython.core.magic import Magics, magics_class, line_magic

from opster import dispatch


@magics_class
class IPythoner(Magics):
    """Integrate Opster and IPython::

    >>> %opster sum -h
    Sum two integers.

    options:

     -n --number  An interger. (default: 5)
        --other   Another interger. (default: 1)
     -h --help    display help

    """
    @line_magic
    def opster(self, parameter_s=''):
        dispatch(parameter_s.split())


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(IPythoner)
