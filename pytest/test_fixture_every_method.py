import pytest


class Test:

    #@pytest.fixture(scope='function',autouse=True)
    #def myfixture(self):
        #print("fixture is called")
    @pytest.mark.dependency()
    @pytest.mark.sanity
    def test_method1(self):
        print("Method1")

    @pytest.mark.dependency(depends=["test_method1"])
    def test_method2(self):
        print("Method2")