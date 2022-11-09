
# sample create table
# for i in range(0,3):
#     print(str(1) + " ",end="")
#     for j in range(0,3):
#         print(str(0) + " ",end="")
    
#     print()
 
input_text = open("input.txt","r")

input_array = []
training_data = []

for input_line in input_text:
    input_array.append(input_line)

input_array_length = len(input_array)

# sort data from input file
for i in range(0,input_array_length):
    if(i == 0):
        r = float(input_array[i])
    elif(i == 1):
        t = float(input_array[i])
    elif(i == 2):
        b = int(input_array[i])
    else:
        training_data.append(input_array[i])

#clear input array
input_array.clear()

row_index = len(training_data)
column_index = len(training_data[0])-1

# if there is 3 data then length is 6
# 0, 2, 4

w = [0,0,0]
w_counter = 0
a = 0

def determineY(a,t):
    y = 0
    if a >= t:
        y = 1
    return y

test_range = 2

#for row in range(0,row_index):
for row in range(0,test_range):
    w_counter = 0
    print("Row " + str(row))
    #Iteration per Row
    for column in range(0, column_index):
        # compute perceptron value, a
        if(column == 0 or column == 2):
            a = a + (int(training_data[row][column]) * w[w_counter])            
            w_counter += 1
        elif(column == 3):
            a = a + (b * w[w_counter])
            w_counter += 1
    # determine classification, y
    y = determineY(a,t)

    #adjust weights
    #for row in range(0,row_index):
    for row in range(0,test_range):
        w_counter = 0
        #Iteration per Row
        for column in range(0, column_index):
            if(column == 0 or column == 2):
                w[w_counter] = w[w_counter] + (r*int(training_data[row][column])*(y-int(training_data[row][4])))
                w_counter += 1
            elif(column == 3):
                w[w_counter] = w[w_counter] + (r*b*(y-int(training_data[row][4])))
                w_counter += 1
    

    print("a",a)
    print("y",y)
    #check adjust weights
    for i in range(0,len(w)):
        print("w",i, " = ", w[i])



