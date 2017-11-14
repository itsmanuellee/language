x = 2
y = 0
while ( x >0):
    y = y + (1.0 / (x**3)) **0.5
    print "x = %d, y = %f" % (x,y)
    x=x+1

    if y>=1:
        break
    
