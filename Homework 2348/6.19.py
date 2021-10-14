word = input()
password = ''

for char in word:
   if char == 'a':
      password += '@'
   elif char == 'i':
      password += '!'
   elif char == 'B':
      password += '8'
   elif char == 'm':
      password +='M'
   elif char == 'o':
      password +='.'
   else:
      password +=char

password += "q*s"
print(password)