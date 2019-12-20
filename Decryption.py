infile = open('Encrypted.txt','r')
textToDecrypt = infile.read()
# textToDecrypt = input("String to Decrypt")
lst2 , b =[] , ""
for a in textToDecrypt: lst2.append(int(((ord(a)*6/12)+10)*2))
for a in lst2:    b += chr(a)
inflie=open('Decrypted.txt','w')
inflie.write(b)
inflie.close()
