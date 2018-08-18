import sys
import math
import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])

congthuc = ((math.sqrt((2*(math.pow(a,(b + min(3,a))))) + (6*(math.pow(b, (a - max(0,b))))))) / (abs((math.pow(a,2)) - (math.pow(b,(2**3))))))

stdio.writeln("BXK3CS100 = " + str(congthuc))
