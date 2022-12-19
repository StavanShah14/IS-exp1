# -*- coding: utf-8 -*-
"""RSA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1luP7w2OrWWumQ68S9UpoWXQkHOzw_jeh
"""

def prime(n): 
	isprime = True 
	if n<2: 
		isprime = False 
	else: 
		for i in range(2,n): 
			if n%i==0: 
				isprime = False 
				break 
	return isprime 
 
string_p=input("enter string p:")
p=len(string_p)
flag, i = True, 1 

if prime(p): 
	p=p
else: 
	while flag: 
		if prime(p+i) and prime(p-i): 
			p=p-i 
			flag = False 
		elif prime(p-i): 
			p=p-i
			flag = False 
		elif prime(p+i): 
			p=p+i
			flag = False 
		i += 1 


string_q=input("enter string q:")
q=len(string_q)
flag1, j = True, 1
if prime(q): 
	q=q
else: 
	while flag1: 
		if prime(q+j) and prime(q-j): 
			q=q+j 
			flag1 = False 
		elif prime(q-j): 
			q=q-j
			flag1 = False 
		elif prime(q+j): 
			q=q+j
			flag1 = False 
		j += 1

e = int(input("Enter the value of e:"))

n = p*q
phi_n = (p-1)*(q-1)

print(f"The public key is ({e},{n})")
for i in range(phi_n):
  if (e*i) % phi_n == 1:
    d = i

print(f"The private key is ({d},{n})")

# Encryption
pt = int(input("Enter the plain text:"))

ct = pt**e % n

print("The plain text is:",pt)
print("After Encryption\nThe cipher text is:",ct)

pt = ct**d % n

print("After Decryption\nThe plain text is:",pt)

