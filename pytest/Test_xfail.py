#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import pytest
import sys
@pytest.mark.xfail(reason="Known bug in the third party library")
def test_function_with_bug():
    assert (1 + 1) == 3#this is assertion will fail as expected

#testcases1
@pytest.mark.sanity
def test_case1():
    print("testcase1 is executed")

#testcases2
@pytest.mark.regression
def test_case2():
    print("testcase2 is executed")

#testcases3
@pytest.mark.db
def test_case3():
    print("testcase3 is executed")

#xfail with a condition
@pytest.mark.xfail(sys.platform == "win32", reason = "Bug on windows")
def test():
    print("test on windows")

#this xfail will fail only on windows

#strict = True  XFIL FAILED FAILS the test suite
@pytest.mark.xfail(strict = True, reason = "Bug #1234 is not fixed yet")
def test_function():
    assert True

#the testcase should fail mandatorily
