import pytest

@pytest.mark.usefixtures("dataLoad")
class TestCl2:
    def test_editprofile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[2])

