from app import app
import unittest
import requests


class empty_leave_request(unittest.TestCase):
    def test_empty_post(self):
        response = requests.post('http://localhost:5000/leave')
        self.assertEqual(response.status_code, 500)


class invalid_employee(unittest.TestCase):
    def test_empty_incorrect_post(self):
        response = requests.post('http://localhost:5000/leave', json={
            "emp_number": "2",
            "start_date": "2011-01-03",
            "end_date": "2012-01-03",
            "days_of_leave": 10
        })
        self.assertTrue(b'Employee Does not exist' in response)


if __name__ == "__main__":
    unittest.main()
