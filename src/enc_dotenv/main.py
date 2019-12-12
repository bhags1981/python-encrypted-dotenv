import dotenv
import pyAesCrypt

# encryption / decryption buffer size - 64K
__BUFFER__SIZE__ = 64 * 1024


def _get_env_file_full_path(env_file_dir, file_name):
    env_file_full_path = "{}/{}".format(env_file_dir, file_name)
    return env_file_full_path


def load_encrypted_dotenv(enc_env_file_path, enc_password_file, buffer_size=__BUFFER__SIZE__, verbose=False,
                          override=False, **kwargs):
    # test decrypted file from here
    decrypted_env_file = enc_env_file_path + ".dec.env"
    with open(enc_password_file, 'r') as f_key:
        enc_password = f_key.read()
        pyAesCrypt.decryptFile(enc_env_file_path, decrypted_env_file, enc_password, buffer_size)
        dotenv.load_dotenv(decrypted_env_file, verbose=verbose, override=override, **kwargs)


def encrypt_dotenv(env_file_path, enc_env_file_path, enc_password_file, buffer_size=__BUFFER__SIZE__):
    # Read key from key file
    with open(enc_password_file, 'r') as f_key:
        enc_password = f_key.read()

    pyAesCrypt.encryptFile(env_file_path, enc_env_file_path, enc_password, buffer_size)

#
# def decrypt_dotenv(env_path, environment: Environment, key):
#     pass
