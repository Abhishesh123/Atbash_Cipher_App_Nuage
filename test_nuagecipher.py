import nuagecipher
import pytest

with open("output_data.txt", "r") as f:
	data = nuagecipher.EncrypFunct(f.read()).lower()

def test_nuagecipher():
	assert ' '.join(nuagecipher.encrypted_data) == 'SVOOL DLIOW!'