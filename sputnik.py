f1 = open('transmission1.txt','r')
f2 = open('transmission2.txt','r')
f3 = open('transmission3.txt','r')
s = f1.read()
base = f2.read()
right = f3.read()
cnt = 0
left = ""
secret = ""
for i in base:
	if i =='+':
		if s[cnt] == '|': 
			secret += '1'
		elif s[cnt] =='-':
			secret += '0'
	else:
		if s[cnt] =='\\':	
			secret += '1'
		elif s[cnt] =='/':
			secret += '0'
	cnt+=1
x = int(secret,2)
s1 = hex(x)[2:-1].decode('hex')[4:]
print s1.decode('base64')