import unittest
from password_manager.manager import PasswordManager

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.manager = PasswordManager(password_file='test_passwords.json', key_file='test_key.key')

    def tearDown(self):
        import os
        if os.path.exists('test_passwords.json'):
            os.remove('test_passwords.json')
        if os.path.exists('test_key.key'):
            os.remove('test_key.key')

    def test_save_and_get_password(self):
        self.manager.save_password('test_service', 'test_user', 'test_password')
        result = self.manager.get_password('test_service')
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'test_user')
        self.assertEqual(result[1], 'test_password')

    def test_delete_password(self):
        self.manager.save_password('test_service', 'test_user', 'test_password')
        self.manager.delete_password('test_service')
        result = self.manager.get_password('test_service')
        self.assertIsNone(result)

if name == '__main__':
    unittest.main()