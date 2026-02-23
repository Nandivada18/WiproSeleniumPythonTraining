#skip - if defects are there
#skip - if the testcases are absolute
#windows, mobile - OS dependency
#browsers - FF, IE, chrome

import pytest
#testcases1
def test_case1():
    print("testcase1 is executed")

#testcases2
@pytest.mark.skip
def test_case2():
    print("testcase2 is executed")

#testcases3
def test_case3():
    print("testcase3 is executed")

#testcases4
@pytest.mark.skip
def openbrowser():
    print("opening the browser")