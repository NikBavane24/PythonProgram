import pytest

from Selenium_framework.conftest import setup


@pytest.mark.smoke
@pytest.mark.skip
def test_M1():
    msg="Hello"
    assert msg=="Hello1","Test failed because string does not match"

def test_M2():
    a=4
    b=6
    c=a+b
    print(c)

@pytest.mark.usefixtures("setup")
class TestCl1:
    def test_fixtureDemo(self):
        print("Execute fixtureDemo method")

    def test_fixtureDemo1(self):
        print("Execute fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("Execute fixtureDemo2 method")