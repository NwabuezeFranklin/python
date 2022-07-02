# to convert and revert a secret message
# Enter a simple message in a precise case
norm_message = input('Enter a message in upper_case letters: ')
secret = ""
for i in norm_message:
    secret += str(ord(i)- 23)
print ('The secret code ',secret)
normalized = ""
for i in range(0, len(secret)-1, 2):
    code = secret[i] + secret[i + 1]
    normalized += chr(int(code) + 23)
print(normalized)
# to use both upper and lower case characters you know what to do
