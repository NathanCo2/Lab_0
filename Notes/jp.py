from matplotlib import pyplot 

#Creates empty array
xaxis_times = []
yaxis_height = []

#opens the data file from folder and reads
with open('data.csv', 'r') as file: 
    #store column headers for first row by characters  
    header = file.readline(-1)
    time = header[:8]
    height = header[10:20]
    #iterates through each line of data file 
    for line in file:
        try:
            #splits each line where comma is present
            split = line.split(',')
            #Creates a list of the X-values (Time [s])
            x = split[0:1]#grabs first column
            join_x = ','.join(x)#combines 2 strings together
            xx = float(join_x)
            #Creates a list of the Y-values (Height [m])
            y = split[1:2]
            join_y = ','.join(y) 
            yy = float(join_y)
            #stores the created list of variables in the blank arrays
            xaxis_times.append(xx)
            yaxis_height.append(yy)
            #Creates points for plot
            #print(xaxis_times, yaxis_height)   
        except ValueError:
            #error occurs when float runs
            print('Error: Not a integer')
            pass
    #plots the values (x,y) values stored in array
    pyplot.plot(xaxis_times, yaxis_height)
    pyplot.xlabel('Time [s]')
    pyplot.ylabel('Height [m]')
    pyplot.grid(True)
    pyplot.show()
