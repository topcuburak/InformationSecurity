import getopt, sys # for taking argument from the command line 
import random
import numpy as np


'''
This function generates ciphertexts by using ciphertexts and key.  
'''

def plaintext_to_ciphertext(plain_text_file, cipher_text_file, key):

	## open plaintext file
	pltext_file = open(plain_text_file, 'r')
	pltext = []

	## read plaintexts as strings (as hexadecimal)
	for line in pltext_file:
		plain = ""
		for ch in line:
			if ch != '\n':
				plain += ch
		pltext.append(plain)


	## convert string hexadecimals to the binary hexadecimals
	binary_pltext = []

	for i in range (0, len(pltext)):
		leng = len(pltext[i]) * 4
		hex_int = int(pltext[i], 16)
		hex_as_bin = bin(hex_int)
		padded_bin = hex_as_bin[2:].zfill(leng)
		binary_pltext.append(padded_bin)

	## empty binary ciphertexts
	bin_cipher = np.zeros((len(binary_pltext), len(binary_pltext[0])), dtype=int)

	#3 open ciphertext file
	ciphertext_file = open(cipher_text_file, 'w')

	## ciphertexts are generated using key and binary plaintexts that are converted into numeric form
	for i in range(0,len(binary_pltext)):
		for j in range(0, len(binary_pltext[0])):
			bin_cipher[i][j] = key[j] ^ int(binary_pltext[i][j])

		# generted ciphertexts are converted string hexadecimal values
		# and stored into ciphertext file
		k = 0
		while (k < len(binary_pltext[0])):
			temp_str = ""	
			temp_str += str(bin_cipher[i][k]) + str(bin_cipher[i][k+1]) + str(bin_cipher[i][k+2]) + str(bin_cipher[i][k+3])
			decimal = int(temp_str,2)
			hex_res = hex(decimal)
			ciphertext_file.write(hex_res[2:])
			k = k + 4

		ciphertext_file.write('\n')

	ciphertext_file.close()

	## shuffle the ciphertexts, to change the generation order
	lines = open(cipher_text_file, 'r').readlines()
	random.shuffle(lines)	
	open(cipher_text_file, 'w').writelines(lines)


	'''
	This function is used to read plaintexts and ciphertexts from the given file names as inputs
	'''
def ReadFromFile_and_ConvertToBin(plain_text_file, cipher_text_file):

	pltext_file = open(plain_text_file, 'r')
	pltext = []

	## read plainstexts
	for line in pltext_file:
		plain = ""
		for ch in line:
			if ch != '\n':
				plain += ch
		pltext.append(plain)

	pltext_file.close()

	# convert string hex plaintexts to the binary ones
	binary_pltext = []

	for i in range (0, len(pltext)):
		leng = len(pltext[i]) * 4
		hex_int = int(pltext[i], 16)
		hex_as_bin = bin(hex_int)
		padded_bin = hex_as_bin[2:].zfill(leng)
		binary_pltext.append(padded_bin)

	ciptext_file = open(cipher_text_file, 'r')
	ciptext = []

	## read ciphertexts
	for line in ciptext_file:
		cipher = ""
		for ch in line:
			if ch != '\n':
				cipher += ch
		ciptext.append(cipher)

	ciptext_file.close()
	
	# convert string hex ciphertexts to the binary ones
	binary_ciptext = []

	for i in range (0, len(ciptext)):
		leng = len(ciptext[i]) * 4
		hex_int = int(ciptext[i], 16)
		hex_as_bin = bin(hex_int)
		padded_bin = hex_as_bin[2:].zfill(leng)
		binary_ciptext.append(padded_bin)


	# convert both string binary plaintexts and ciphertexts to the numeric ones.  
	bin_pltext = np.zeros((len(binary_pltext), len(binary_pltext[0])), dtype=int)
	bin_ciptext = np.zeros((len(binary_ciptext), len(binary_ciptext[0])), dtype=int)

	for i in range(0, len(binary_pltext)):
		for j in range(0, len(binary_pltext[0])):
			bin_pltext[i][j] = str(binary_pltext[i][j])
			bin_ciptext[i][j] = str(binary_ciptext[i][j])

	return bin_pltext, bin_ciptext	


	'''
	This function is used to find key.
	'''
def key_finder(bin_pl, bin_cip):

	## we will XOR each plaintext and each ciphertext
	Xor_res = np.zeros((len(bin_pl)*len(bin_cip), len(bin_pl[0])), dtype=int)

	# there will be len(plaintexts^2) elements
	for i in range(0, len(bin_pl)):
		for j in range(0, len(bin_pl)):
			for k in range (0, len(bin_pl[0])):
				Xor_res[i*len(bin_pl)+j][k] = bin_pl[i][k] ^ bin_cip[j][k]

	# then we look for the Xor results to find the matching one
	# if one of the results repeats len(plaintexts) times, it is the key 
	for i in range(0, len(Xor_res)):
		count = 0
		for j in range(0, len(Xor_res)):
			if (Xor_res[i] == Xor_res[j]).all():
				count += 1
			if count == len(bin_pl):
				return Xor_res[i]

	# this function just generates random key
def key_generator():

	key = np.zeros((128), dtype = int)

	for i in range(0,len(key)):
		key[i] = random.randint(0,1)

	return key


	# this function writes the results to the outputfile
def results_to_output(binary_pltext, key, output_file):
	
	out = open(output_file, 'w')

	out.write("Key in binary format: \n")
	for i in range(0, len(key)):
		out.write(str(key[i]))

	out.write("\n\nKey in hexadecimal format: \n")
	k = 0
	while (k < len(key)):
		temp_str = ""
		temp_str += str(key[k]) + str(key[k+1]) + str(key[k+2]) + str(key[k+3])
		decimal = int(temp_str,2)
		hex_res = hex(decimal)
		out.write(hex_res[2:])
		k = k + 4

	out.write("\n\n -------- Plain texts -------- and ------- Cipher texts ------- : \n\n")

	for i in range(0, len(binary_pltext)):
		temp = []
		for j in range(0, len(key)):
			temp.append(key[j]^binary_pltext[i][j])

		k = 0
		while (k < len(key)):
			temp_str = ""
			temp_str += str(binary_pltext[i][k]) + str(binary_pltext[i][k+1]) + str(binary_pltext[i][k+2]) + str(binary_pltext[i][k+3])
			decimal = int(temp_str,2)
			hex_res = hex(decimal)
			out.write(hex_res[2:])
			k = k + 4

		out.write("  ")

		k = 0
		while (k < len(key)):
			temp_str = ""
			temp_str += str(temp[k]) + str(temp[k+1]) + str(temp[k+2]) + str(temp[k+3])
			decimal = int(temp_str,2)
			hex_res = hex(decimal)
			out.write(hex_res[2:])
			k = k + 4

		out.write("\n")
	out.close()
	print("The output file also created")


#takes command line arguments
plain_text_file = sys.argv[1]
cipher_text_file = sys.argv[2]
output_file = sys.argv[3]


#generate key
generated_key = key_generator()

#generate cipher texts
plaintext_to_ciphertext(plain_text_file, cipher_text_file, generated_key)

#read ciphertexts and plaintexts from the plain_text_file and cipher_text_file files
binary_pltext, binary_ciptext = ReadFromFile_and_ConvertToBin(plain_text_file, cipher_text_file)

#try to find out the key
founded_key = key_finder(binary_pltext, binary_ciptext)

#if randomly generated key and founded key is the same
if (founded_key == generated_key).all():
	# generate the output result
	print("The key is found generated by key_generator funtion as randomly")
	print("Let us create output file")
	results_to_output(binary_pltext, founded_key, output_file)

else:
	print("There must be something wrong!")

