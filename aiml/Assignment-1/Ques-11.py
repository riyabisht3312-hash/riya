name = input("Enter your name: ")
upper_name = ""
lower_name = ""
for ch in name:
if 'a' <= ch <= 'z': # lowercase to uppercase
upper_name += chr(ord(ch) - 32)
else:
upper_name += ch
if 'A' <= ch <= 'Z': # uppercase to lowercase
lower_name += chr(ord(ch) + 32)
else:
lower_name += ch
print("Uppercase:", upper_name)
print("Lowercase:", lower_name)