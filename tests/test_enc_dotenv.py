import dotenv
import io
import os
import pyAesCrypt

from unittest import TestCase
from enc_dotenv.main import encrypt_dotenv, load_encrypted_dotenv, __BUFFER__SIZE__


class TestEncDotenv(TestCase):
    def test_encrypt_dotenv(self):
        env_file_path = os.path.dirname(os.path.realpath(__file__))
        env_file_name = "test.env"
        env_file = env_file_path + "/" + env_file_name

        enc_env_file_path = env_file_path
        enc_env_file_name = "test.enc.env"
        enc_env_file = enc_env_file_path + "/" + enc_env_file_name
        password_file = env_file_path + "/test.password"

        decrypted_test_file = enc_env_file_path + "/decrypted.enc"

        # decrypted_ = pyAesCrypt.decryptStream(enc_env_file_path, )
        encrypt_dotenv(env_file, enc_env_file, password_file)

        # test decrypted file from here
        with open(password_file, 'r') as f_key:
            enc_password = f_key.read()
            pyAesCrypt.decryptFile(enc_env_file, decrypted_test_file, enc_password, __BUFFER__SIZE__)

        test_keys = ['SOME_SETTING_1', 'SOME_SETTING_2', 'INT_SETTING']

        for test_key in test_keys:
            self.assertEqual(
                dotenv.get_key(env_file, test_key),
                dotenv.get_key(decrypted_test_file, test_key),
            )

    def test_load_encrypted_dotenv(self):
        enc_env_file_path = os.path.dirname(os.path.realpath(__file__))
        enc_env_file_name = "test.enc.env"
        enc_env_file = enc_env_file_path + "/" + enc_env_file_name
        password_file = enc_env_file_path + "/test.password"
        load_encrypted_dotenv(enc_env_file, password_file, )
