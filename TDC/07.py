import stdio
a=stdio.readFloat()
b=stdio.readFloat()
c=stdio.readFloat()
d=stdio.readFloat()
s=a*2+c*2+d+b
if 10>=a>=0 and 10>=b>=0 and 10>=c>=0 and 10>=d>=0 :
	if s>=9.0:
		if a>=6.5 and b>=6.5 and d>=6.5 and c>=6.5 :
			stdio.writeln('XS')
		elif a<=6.5 or b<=6.5 or d<=6.5 or c<=6.5 :
			stdio.writeln('G')	
	elif s>=8 :
		if a>=5 and b>=5 and d>=5 and c>=5:
			stdio.writeln('G')
		elif a<=5 or b<=5 or d<=5 or c<=5:
			stdio.writeln('K')
	elif s>=6.5:
		if a>=3 and b>=3 and d>=3 and c>=3:
			stdio.writeln('K')
		elif a<=3 or b<=3 or d<=3 or c<=3:
			stdio.writeln('TB')
	elif s>=5:
		if a>=2 and b>=2 and d>=2 and c>=2:
			stdio.writeln('TB')	
		elif a<=2 or b<=2 or d<=2 or c<=2:
			stdio.writeln('Y')
	else:	
		stdio.writeln('Y')	
