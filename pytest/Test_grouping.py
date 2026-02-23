#grouping - set of testcases run together - issue fix in the that module

import pytest
#testcases1
def test_case1():
    print("testcase1 is executed")

#testcases2
@pytest.mark.sanity
def test_case2():
    print("testcase2 is executed")

#testcases3
@pytest.mark.sanity
@pytest.mark.regression
def test_case3():
    print("testcase3 is executed")

