import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import getpass

def DeriveKey(passwordParam):
    if type(passwordParam) == str:
        passwordParam = passwordParam.encode("utf-8")
    keyDerivationFunction = Scrypt(salt=b'ABCDEFGHIJKLMNOP', length=32, n=2**14, r=8, p=1, backend=default_backend())
    deriveKEY = keyDerivationFunction.derive(passwordParam)
    key = base64.urlsafe_b64encode(deriveKEY)
    return key
 
filename = 'secret-stuff.txt'

# read the contents of the file
with open(filename, 'r') as file:
    message = file.read()
 
password = getpass.getpass("enter password: ")
 
fernet = Fernet(DeriveKey(password))
encMessage = fernet.encrypt(message.encode())
 
with open(filename, 'wb') as f:
    f.write(encMessage)
