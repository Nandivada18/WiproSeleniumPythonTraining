import pytest
from Test_SimpleFixture import api_url
#testcase1
def test_case1():
    print("Testcase1 is executed")
#testcase2
def test_case2():
    print("Testcase2 is executed")
#testcase3
def test_case3():
    print("Testcase3 is executed")
#testcase4
def test_case4():
    print("Testcase4 is executed")
#testcase5
def test_case5():
    print("Testcase5 is executed")

def test_login():
    print("Login test is executed")

def test_api(api_url):
    assert "https" in api_url