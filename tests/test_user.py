import unittest
from api.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("maria", "nanfuka", "mimi", "maria.nanfuka@gmail.com",
                         "12345")

    def test_first_name(self):
        self.assertEqual(self.user.firstname, "maria", "firstname should be\
                         nanfuka")
        self.user.firstname = "sarah"
        self.assertEqual(self.user.firstname, "sarah", "firstname has changed\
                         to sarah")

    def test_last_name(self):
        self.assertEqual(self.user.lastname, "nanfuka", "lastname should be\
                         nanfuka")
        self.user.lastname = "Namutebi"
        self.assertEqual(self.user.lastname, "Namutebi", "lastname has changed\
                         to Namutebi")

    def test_user_name(self):
        self.assertEqual(self.user.user_name, "mimi", "username should be\
                         mimi")
        self.user.user_name = "rabbit"
        self.assertEqual(self.user.user_name, "rabbit", "username has changed\
                         to rabbit")

    def test_email(self):
        self.assertEqual(self.user.email, "maria.nanfuka@gmail.com", "Email should be\
                         maria@gmail.com")

    def test_password(self):
        self.assertEqual(self.user.password, "12345", "password should be\
                         12345")
        self.user.password = "1289"
        self.assertEqual(self.user.password, "1289", "password has changed  to\
                         1289")

    def test_object(self):
        self.assertIsInstance(self.user, User)
