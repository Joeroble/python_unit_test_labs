import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmployee = Employee(1, 'Bob')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee)
        self.assertIn(testEmployee, testAssignmentMgr.employees)



    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testEmployee1 = Employee(1, 'Bob')
        testEmployee2 = Employee(1, 'Bobert')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments
        testEmployee = Employee(1, 'Bob')
        testPhone = Phone(1, 'Samsung', 'Note')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.assign(1, testEmployee)



    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.        testEmployee = Employee(1, 'Bob')
        testPhone = Phone(1, 'Samsung', 'Note')
        testEmployee = Employee(1, 'Cheese')
        testEmployee2 = Employee(2, 'Double Cheese')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.assign(1, testEmployee)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, testEmployee2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
        testPhone = Phone(1, 'Samsung', 'Note')
        testPhone2 = Phone(2, 'Samsung', 'Galaxy')
        testEmployee= Employee(1, 'Douglas the Douglas')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.assign(1, testEmployee)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(2, testEmployee)




    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        testPhone = Phone(1, 'Samsung', 'Note')
        testEmployee= Employee(1, 'Douglas the Douglas')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.assign(1, testEmployee)
        testAssignmentMgr.assign(1, testEmployee)
        
        self.assertEqual(testPhone.employee_id, testEmployee.id)
        # TODO assertion does - employee still have the original phone? 



    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None

        testEmployee = Employee(1, 'Bob')
        testPhone = Phone(1, 'Samsung', 'Note')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.assign(1, testEmployee)
        testAssignmentMgr.un_assign(1)
        self.assertIsNone(testPhone.employee_id)


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        testPhone = Phone(1, 'Samsung', 'Note')
        testPhone2 = Phone(2, 'Samsung', 'Galaxy')
        testEmployee= Employee(1, 'Douglas the Douglas')
        testEmployee2 = Employee(2, 'Sammy Sammerson the Samstersons')
        testEmployee3 = Employee(3, "Does not exist")
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.assign(1, testEmployee)
        self.assertEqual(testPhone, testAssignmentMgr.phone_info(testEmployee))
        
        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(testEmployee3)

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

