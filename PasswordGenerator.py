print()

print("=====Password Generator=====")

import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password=None

print()
print("Note: The length of the password must be greater than or equal to 4.")
print()

l=int(input("Enter length of password: "))

if l>=4:
    password = ''.join(random.sample(characters, l))

else:
    print("Length of password must be greater than or equal to 4!!!")
    print()
    l = int(input("Enter length of password: "))
    if l >= 4:
        password = ''.join(random.sample(characters, l))

print()
print("---------------")
print(f"Generated password: {password}")
print("---------------")
print()














