textToEncrypt = input("Any String to Encrypt: ")
lst1 , b =[] , ""
for a in textToEncrypt:
    lst1.append (int((ord(a)-10*12/6)))
for a in lst1:  b += chr(a)
inflie=open('Encrypted.txt','w')
inflie.write(b)
infile.close()
