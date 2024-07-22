from cryptography.fernet import Fernet
import pandas as pd

def encrypt_ip(ip, key):
    """Encrypt an IP address using Fernet."""
    # Create a Fernet instance with the encryption key
    fernet = Fernet(key)
    # Encrypt the IP address
    encrypted_ip = fernet.encrypt(ip.encode('utf-8'))
    return encrypted_ip

def decrypt_ip(encrypted_ip, key):
    """Decrypt an encrypted IP address using Fernet."""
    # Create a Fernet instance with the encryption key
    fernet = Fernet(key)
    # Decrypt the IP address
    decrypted_ip = fernet.decrypt(encrypted_ip).decode('utf-8')
    return decrypted_ip

# Generate a secret key
key = Fernet.generate_key()

ips = ["xxxx.xxxx.xxxx.xxxx", "xxx.xx.xxx.xx", "xx.xxx.xx.x"]
encrypted_ips = [encrypt_ip(ip, key) for ip in ips]

# Create a DataFrame with the encrypted IP addresses
df = pd.DataFrame(encrypted_ips, columns=['Encrypted IP'])
print(df)

# Decrypt the IP addresses
decrypted_ips = [decrypt_ip(encrypted_ip, key) for encrypted_ip in encrypted_ips]
print(decrypted_ips)
