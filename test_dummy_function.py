import pytest
from dummy_function import *

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
