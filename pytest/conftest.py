import pytest

class Test2:
    @pytest.fixture(scope='function',autouse=True)
    def myfixture(self):
        print("Fixture is called")

