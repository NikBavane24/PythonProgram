import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute before test")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("user data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome","Nikhil","Shaurya"),("Firefox","SS")])
def crossBrowser(request):
    return request.param
