import sys
import unittest

import book_rental as book_rentalClass


class book_rental_charge(unittest.TestCase):
    """Sample test case"""

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "book_rental_charge:setUp_:begin")

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
        no_of_days_rented = 6
        total_cost_per_day = 15
        total_cost = no_of_days_rented * \
            total_cost_per_day
        # self.assertEqual(no_of_days_rented,
        #                     total_cost_per_day,
        #                     "no_of_days_rented is not"
        #                     "equal to total_cost_per_day")
        print "book_rental_charge:total_cost"

    # test routine B
    def testB(self):
        """Test routine B"""
        print "book_rental_charge:testB"

    # test routine C
    def testC(self):
        """Test routine C"""
        print "book_rental_charge:testB"

    if __name__ == "__main__":
        unittest.main()

    fooRunner = unittest.TextTestRunner(verbosity=2)
    # includes the docstr
    # fooRunner.run(fooSuite)
