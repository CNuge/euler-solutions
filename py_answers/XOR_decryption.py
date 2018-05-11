"""
Each character on a computer is assigned a unique code and the preferred standard 
is ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on the 
cipher text, restores the plain text; for example, 

65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", 
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, 
which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, 
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using cipher.txt (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the plain 
text must contain common English words, decrypt the message and find the sum of 
the ASCII values in the original text.


curl https://projecteuler.net/project/resources/p059_cipher.txt > p059_cipher.txt


https://projecteuler.net/problem=59
"""
import itertools

def iterate_ciphers(data):
	#the encodings for all the lower case letters
	cipher_components = [ ord(x) for x in 'abcdefghijklmnopqrstuvwxyz' ]

	potential_messages = []
	for c1 in cipher_components:
		for c2 in cipher_components:
			for c3 in cipher_components:
				cipher = [c1,c2,c3]

				pre_message = zip(data, itertools.cycle(cipher))

				message_num = [ x[0] ^ x[1] for x in pre_message ]

				message = ''.join([chr(x) for x in message_num])

				count_the = message.count('the')
				count_with = message.count('with')
				count_for = message.count('for')
				count_and = message.count('and')

				total = count_the + count_with + count_for + count_and

				if total > 10:
					potential_messages.append(message)
	return potential_messages

if __name__ == '__main__':
	x = 'A'
	ord(x)
	ord('*')
	ord('k')

	65 ^ 42 #to get the xor use the ^ symbol

	file = open('p059_cipher.txt','r')
	data = file.read()
	file.close()

	data = [int(x) for x in data.rstrip().split(',')]

	potential_messages = iterate_ciphers(data)

	len(potential_messages)

	for x in potential_messages:
		print(x)
		print('\n\n\n\n')

	message =  potential_messages[1]
	message

	#find the sum of the ASCII values in the original text.

	sum_ascii = 0
	for i in message:
		sum_ascii += ord(i)

	print(f'The message ascii values summed to: {sum_ascii}')