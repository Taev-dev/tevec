"""This is basically a freebie, which makes sure the library imports and
has a version.
"""
import tevec


def test_has_version():
    assert tevec.__version__
    assert isinstance(tevec.__version__, str)
