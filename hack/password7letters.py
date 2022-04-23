

f = open('password.txt', 'w')
alpha = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
n = len(alpha) 

def dfs(a):
	if len(a) == 2:
		s = "".join(a)
		f.write(s + '\n')
		return	
	for i in range(0, n):
		dfs(a + [alpha[i]])
dfs([])
f.close()
