#Funcion para rendondear un numero (p)

p = 1204328

def red(p):
	if len(str(p)) <= 3:
		r = p

	elif len(str(p)) == 4:
		r = str(p)[:1] + '.' + str(p)[1:3] + ' kb'

	elif len(str(p)) == 5:
		r =  str(p)[:2] + '.' + str(p)[2:3] + ' kb'

	elif len(str(p)) == 6:
		r =  '0' + '.' + str(p)[:2] + ' Mb'

	elif len(str(p)) == 7:
		r = str(p)[:1] + '.' + str(p)[1:3] + ' Mb'

	elif len(str(p)) == 8:
		r = str(p)[:2] + ' Mb'

	elif len(str(p)) == 9:
		r = str(p)[:3] + ' Mb'

	return r; 

r = red(p)

print r