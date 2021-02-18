# Atbash_Cipher_App_Nuage

Atbase Cipher is a type of substitution cipher.It's replacing each letter in the plaintext with the corresponding letter if the alphabet were reversed. Its read content from input_data.txt file and then apply encryption after that encrypted data write into ouput_data.txt file. This is used to handle large file here  I m using Multithreding for this.

#Sample_Input_OutPut

##For **Hello world!**

If you want to apply encryption on **Hello world!** using Atbash Cipher technique. First of all write **Hello world!** in input_data.txt and then run nuagecipher.py Python file. if you are using ubantu terminal then open it and type **Python3 manage.py nuagecipher.py** after that you get output_data.txt file . when you open it you found encrypted data **Svool dliow!**.


## For "Christmas is the 25th December"

If you want to apply encryption on **Christmas is the 25th December
** using Atbash Cipher technique. First of all write **Christmas is the 25th December
** in input_data.txt and then run nuagecipher.py Python file. if you are using ubantu terminal then open it and type **Python3 manage.py nuagecipher.py** after that you get output_data.txt file . when you open it you found encrypted data **XSIRHGNZH RH GSV 25GS WVXVNYVI**.


#  Apply Unit testing using PyTest.

##Usecase for Svool dliow!

open test_nuagecipher.py file then you  will write SVOOL DLIOW! for compariosn in place of	assert ' '.join(nuagecipher.encrypted_data) == 'Abhishesh'

and run pytest test_nuagecipher.py command on terminal the it will show 

test session starts ==========================================================================
platform linux2 -- Python 2.7.18, pytest-4.6.9, py-1.8.1, pluggy-0.13.0
rootdir: /home/aar/Desktop/Atbash_Cipher_App_Nuage
collected 1 item                                                                                                                                                       

test_nuagecipher.py .                                                                                                                                            [100%]

============================================================ 1 passed in 0.10 seconds==========================================================

