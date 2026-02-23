#used inside the class
#it will run for every class definition it will run starting and at ending of the class

class Testclass1:
    #class level set up
    def setup_class(cls):
        print("API Authorization needed with username and password")

    def teardown_class(self):
        print("API Authorization closed ")

    def setup_method(method):
        print("Open the db connection")

    def teardown_method(method):
        print("Closing the db connection")
    #testcase1
    def testcase1(self):
        print("Testcase1 is executed")
    # testcase2
    def testcase2(self):
        print("Testcase2 is executed")
    # testcase3
    def testcase3(self):
        print("Testcase3 is executed")

class Testclass2:
    #testcase1
    def testcase1(self):
        print("Testcase1 is executed")
    # testcase2
    def testcase2(self):
        print("Testcase2 is executed")
    # testcase3
    def testcase3(self):
        print("Testcase3 is executed")