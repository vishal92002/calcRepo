""" content of test_sample.py#"""


def inc(x_value):
    """Adding one to x value"""

    return x_value + 1


def test_answer():
    """Testing the inc function to increment x value by one"""

    assert inc(4) == 5
