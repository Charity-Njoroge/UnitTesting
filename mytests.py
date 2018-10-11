import unittest
 
class book_rental_charge(unittest.TestCase):
    """Sample test case"""
     
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "book_rental_charge:setUp_:begin"
         
        testName = self.shortDescription()
        if (testName == "total_rental_cost1"):
            print "setting up for total_rental_cost1"
             
        elif (testName == "Test routine B"):
            print "setting up for test B"
             
        else:
            print "UNKNOWN TEST ROUTINE"
             
        print "book_rental_charge:setUp_:end"
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "book_rental_charge:tearDown_:begin"
         testName = self.shortDescription()
        if (testName == "total_rental_cost1"):
            print "cleaning up after total_rental_cost1"
             
        elif (testName == "Test routine B"):
            print "cleaning up after test B"
             
        else:
            print "UNKNOWN TEST ROUTINE"
        print "book_rental_charge:tearDown_:end"
     
    # test routine A
    def total_rental_cost1(self):
        """Test routine A"""
        print "book_rental_charge:testA"
     
    # test routine B
    def testB(self):
        """Test routine B"""
        print "book_rental_charge:testB"