import os
import json
from cryptography.fernet import Fernet
from .utils import prompt_password, generate_random_password

class PasswordManager:
    def __init__(self, password_file='passwords.json', key_file='key.key'):
        self.password_file = password_file
        self.key_file = key_file
        self.key = self.load_key()
        self.cipher = Fernet(self.key)

    def load_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        else:
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        return key

    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()

    def save_password(self, service, username, password):
        encrypted_password = self.encrypt_password(password)
        data = self.load_data()
        data[service] = {'username': username, 'password': encrypted_password}
        self.save_data(data)

    def load_data(self):
        if os.path.exists(self.password_file):
            with open(self.password_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self, data):
        with open(self.password_file, 'w') as file:
            json.dump(data, file, indent=4)

    def get_password(self, service):
        data = self.load_data()
        if service in data:
            username = data[service]['username']
            encrypted_password = data[service]['password']
            password = self.decrypt_password(encrypted_password)
            return username, password
        return None

    def delete_password(self, service):
        data = self.load_data()
        if service in data:
            del data[service]
            self.save_data(data)

    def generate_password(self, length=12):
        return generate_random_password(length)