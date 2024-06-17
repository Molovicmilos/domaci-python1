text = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

# 1. Get the length of the string
print(len(text))
# 2. Get the first 10 characters
print(text[:10])
# 3. Get the last 10 characters
print(text[-10:])
# 4. Get the characters from the 10th to the 20th
print(text[10:20])
# 5. Get the characters from the 10th to the end
print(text[10:])
# to uppercase
print(text.upper())
# to lowercase
print(text.lower())
# capitalize
print(text.capitalize())
#slice the string into words
print(text.split())