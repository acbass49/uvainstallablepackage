import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

def test_another_test():
    assert 1 == 1

@pytest.mark.xfail
def test_failed_test1():
    assert 1 == 2

@pytest.mark.skip(reason="bug we want to fix")
def test_failed_test2():
    assert 1 == 2

@pytest.mark.skipif(sys.platform == 'darwin', reason="requires windows system to test")
def test_failed_test3():
    print("My platform is", sys.platform)
    assert 1 == 1
