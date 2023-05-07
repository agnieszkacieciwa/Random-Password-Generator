import random
import string

# List of characters to compose the password
chars = string.ascii_letters + string.digits + string.punctuation

# Function that generates a password of a given length
def generate_password(length):
    # Choose from the `chars` list `length` times
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Call the `generate_password` function with the `length` argument set to 12
password = generate_password(12)

# Display the generated password
print("Generated password:", password)
