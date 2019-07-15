print('Hello!')

myName= input('What is your name? ')

print('It is nice to meet you, ' + myName)



Ask= input('Would you like to encrypt or decrypt? E or D: ')
if Ask== 'E' or Ask== 'e':
	text= input('Enter the text you would like to encrypt: ')
	key= int(input('Pick a key 0-25 '))
	def Cesarencrypt(text, key):
		encrypttext= ''
		for letter in text:
			if letter.isalpha():
				usealpha = ord(letter)+key
				if usealpha > ord('z'):
					usealpha -=26
				finalletter = chr(usealpha)
				encrypttext += finalletter
		print('Your encrptyed text is: ', encrypttext)
		return encrypttext	
	Cesarencrypt(text, key)
elif Ask== 'D' or Ask== 'd':
	text= input('Enter the text you would like to decrypt: ')
	key=('What is the key? 0-25')
else:
	print('Sorry not a valid input, please try again. ')
