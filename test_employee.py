import unittest
from employee import Employee 
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)

	def tearDown(self):
		pass

	def test_email(self):
		self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

	def test_fullname(self):
		self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 'Sue Smith')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.fullname, 'John Schafer')
		self.assertEqual(self.emp_2.fullname, 'Jane Smith')

	def test_apply_raise(self):
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()
 
		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)

	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			#make sure get method was called with correct url
			mocked_get.assert_called_with('http://company.com/Schafer/May')
			#make sure it returned the correct text
			self.assertEqual(schedule, 'Success')

			#test failed response
			mocked_get.return_value.ok = False
		
			schedule = self.emp_2.monthly_schedule('June')
			#make sure get method was called with correct url
			mocked_get.assert_called_with('http://company.com/Smith/June')
			#make sure it returned the correct text
			self.assertEqual(schedule, '_Bad Response!_')



if __name__ == '__main__':
	unittest.main()