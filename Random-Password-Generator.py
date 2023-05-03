import random
import string

# Lista znaków, z których ma składać się hasło
chars = string.ascii_letters + string.digits + string.punctuation

# Funkcja generująca hasło o zadanej długości
def generate_password(length):
    # Losujemy z listy `chars` `length` razy
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Wywołujemy funkcję `generate_password` z argumentem `length` równym 12 (długość hasła)
password = generate_password(12)

# Wyświetlamy wygenerowane hasło
print("Wygenerowane hasło to:", password)
