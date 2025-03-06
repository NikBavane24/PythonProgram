#Any pytest file name should start with or end (test_,_test) ex- test_demo1 here
#pytest method name start with test ex- test_firstProgram()
#in pytest test always in method
#Method name should have sense
# -k stands for method name execution,-s for logs in out put,-v for more information for metadata
# Run specific file py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m smoke in cmd
# skip test with @pytest.mark.skip
# to run the test case but not to report pss/fail @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases-  conftest file to generalised fixture and make it available to all test cases
# Datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only,t will run once before class is initiated and at the end


import pytest

@pytest.mark.xfail
def test_firstProgram():
    print("Demo test completed")

@pytest.mark.smoke
def test_firstProgram1():
    print("good morning")

