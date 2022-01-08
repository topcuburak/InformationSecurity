There are mainly 5 functions in the code.

	1) plaintext_to_ciphertext(plain_text_file, cipher_text_file, key)
	- This function takes the plain text as txt file, generates the cipher text file as txt format by using key.
	- The generated ciphertexts are shuffled before saving them into the cipher text file. 
	
	2) ReadFromFile_and_ConvertToBin(plain_text_file, cipher_text_file)
	- This funtion reads both plaintexts and ciphetexts from the given file names
	- and generates the binary values for them since both plaintexts and ciphertexts
	- are hold as hexadecimal in those files.
	
	- After hexadecimal values are converted to the string binaries, those string values need to be converted 
	- to the numeric ones. The string to numeric conversion is done also here.
	
	3) key_finder(bin_pl, bin_cip)
	- This function is used to find the key. To find key, plaintexts and ciphertexts are XORed.
	- For 10 plaintexts and 10 ciphertexts, there will be 100 XORed. Each 10 of those 100 results from 1 plain text.
	- By comparing those resutls, we will try to find out the common results in each of those 10 results. 
	- The common one will be the KEY that we look for.
	- This part of the algorithm takes O(K^2) time.
	
	4) key_generator() 
	- This function generates key in each time randomly.
	
	5) results_to_output(binary_pltext, key, output_file)
	- This function takes plain text, founded key and output file name
	- to write; matching plaintexts-ciphertexts and key to the output file.
		
NOTES:
	- key length is specified as 128 bits. 
	- In each run, different key will be generated. Also, since key is changing each time, generated ciphertext file will also be changed in each run.
	- In the assignment, it is said that 2 files will be taken as input. My code also takes 2 files as input after it generates the ciphertext file. 
	
I have imported below functions in my code. If one of them is missing in your python3 library, you can install it with 'pip3 install' command. 

	import getopt, sys 
	import random
	import numpy as np
	
Please delete output and cipher text files and run the code in the following way:

python3 main.py "Sample Plaintext File.txt" "Sample Ciphertext File.txt" "Output File.txt" 


