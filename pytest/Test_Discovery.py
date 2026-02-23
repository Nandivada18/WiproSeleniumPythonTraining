# unit testing is type of testing done by the developers
# what component they have developed they do the testing for it before integrating it to the other modules
# get defects earlier
# Pytest in python , junit and nunit - java
# pytest is used ny developers and testers

#test discovery - rules used create the pytest tests
#-v - verbose - rules used created the pytest tests
#-s - show print statements

#files should start with test
#functions should start with test

import pytest
#testcases1
def test_case1():
    print("testcase1 is executed")

#testcases2
def test_case2():
    print("testcase2 is executed")

#testcases3
def test_case3():
    print("testcase3 is executed")

#testcases1
def openbrowser():
    print("opening the browser")