"""
Economic utility functions
===============================================================================

Overview
-------------------------------------------------------------------------------


Functions in this module
-------------------------------------------------------------------------------



"""
from math import log, exp

def exp_utility_fun(r_param):
    """Exponential utility function.

    U(x) = 1 - exp(-x / r_param)
    """
    def utility_fun(x, inverse=False):
        return (1 - exp( -x / r_param)) if inverse is False else - r_param * log(1 - x)

    return utility_fun



def log_utility_fun(r_param):
    """Exponential utility function.

    U(x) = log(x + r_param)
    """
    def utility_fun(x, inverse=False):
        return log(x + r_param) if inverse is False else exp(x) - r_param

    return utility_fun


def sqrt_utility_fun(r_param):
    """Exponential utility function.

    U(x) = + sqrt(x + r_param)
    """
    def utility_fun(x, inverse=False):
        return (x + r_param) ** 0.5 if inverse is False else x * x - r_param

    return utility_fun
