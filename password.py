# Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import random
x = int(input('How many characters do you want to be your password ?'))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

random_pass = x
p = "".join(random.sample(s, random_pass))
print(p)

