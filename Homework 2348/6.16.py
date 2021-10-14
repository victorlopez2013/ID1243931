word = input()
password = ''

for char in word:
   if char == 'a':
      password += '@'
   elif char == 'i':
      password += '1'
   elif char == 's':
      password += '$'
   elif char == 'B':
      password += '8'
   elif char == 'm':
      password +='M'
   else:
      password +=char

password += "!"
print(password)