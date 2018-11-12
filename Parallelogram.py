def paralleogram(height, width, pitch):
        i = 0
	indent = " "*((pitch*(height))-pitch)
        while i < height:
                print indent + "*"*width
                i = i + 1
		indent = " "*((pitch*(height)-pitch)-(i*pitch))
paralleogram(10, 10, 3)                                       
