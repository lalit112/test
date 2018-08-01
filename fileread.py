def test(file_name)
count = 0
file1 = open("output.txt","w")
with open(file_name,'r') as f:
	for lines in f:
		a = lines.split(' ')
		if a[0].startswith('*'):
			s = len(a[0])
			if s == 1:
				count = count +1
				file1.write(str(count) +lines.replace('*',''))
			elif s ==2:
				file1.write(str(count)+'.'+'1' +lines.replace('**',''))
			elif s ==3:
				file1.write(str(count)+'.'+'1'+'.'+'1' +lines.replace('***',''))
			elif s ==4:
				file1.write(str(count)+'.'+'1'+'.'+'1'+'.'+'1' +lines.replace('****',''))
		elif a[0].startswith('.'):
			s = len(a[0])
			if s == 1:
				file1.write(' '*s + '+'+ lines.replace('.',''))
			else:
				file1.write(' '*s + '-'+ lines.replace('.',''))
