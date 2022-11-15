'''
Joshua V. Esguerra
CMSC 170 WX3L
Exercise 06 Perceptron
'''

#functions
from tabulate import tabulate

def determineY(a,t):
    y = 0
    if a >= t:
        y = 1
    return y

def adjust_weight(td_row,arr,a,b,y):
    w_counter = 0
    for j in range(0, (tdata_table_col-1)):
        w[w_counter] = w[w_counter] + (r*tdata_table[td_row][j]*(tdata_table[td_row][2] - y))
        if w_counter == 1:
            w_counter += 1
            w[w_counter] = w[w_counter] + (r*b*(tdata_table[td_row][2] - y))
        w_counter += 1
    return arr

# if not_converge == 1, all weights are not the same yet

def weight_converge(all_arr,current_arr):
    not_converge = 0
    for j in range(0,len(all_arr)):
        for i in range(0,len(current_arr)):
            if current_arr[i] != all_arr[0][i]:
                not_converge = 1
    return not_converge

#FILE READING
input_text = open("in1.txt","r")

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
        b = float(input_array[i])
    else:
        training_data.append(input_array[i])

#clear input array
input_array.clear()

# FILE READING - end

# DECLARATIONS
row_len = len(training_data)    #4
column_len = len(training_data[0])-1 # do not change
build_column_len = int(len(training_data[0])/2)             #3 Ex. 0 0 0
tdata_array = []
not_converge = 1
tdata_table = []
all_w = []
headers = []
final_tbl_col = build_column_len * 2 + 3     # total number of columns for each iteration
pos_y = final_tbl_col-2
pos_a = final_tbl_col-3
pos_b = build_column_len
iteration_num = 1
range_w_index = pos_b * 2


# create headers for the table
cond1 = build_column_len-1
cond2 = build_column_len*2
headers_index = 0
for header in range(0,final_tbl_col-2):
    format_x = "x" + str(header)
    format_w = "w" + str(headers_index)
    if header < cond1:
        headers.append(format_x)
    elif header == cond1:
        headers.append("b")
    elif header > cond1 and header < cond2-1:
        headers.append(format_w)
        headers_index += 1
    elif header == cond2-1:
        headers.append("wb")
    else:
        headers.append("a")
        headers.append("y")
        headers.append("z")

# create w array and tdata_table
tdata_table = [[0 for col in range(0,build_column_len)] for row in range(0,row_len)]
w = [0] * build_column_len
final_table = [[0 for col in range(0,final_tbl_col)] for row in range(0,row_len)]

# fill tdata_table with given input and also set final table
for row in range(0,row_len):
    column_index = 0
    for column in range(0,column_len):
        if(column % 2 == 0):
            tdata_table[row][column_index] = int(training_data[row][column])
            final_table[row][column_index] = int(training_data[row][column])
            column_index += 1
            if column == 4:    
                #tdata_table[row][final_tbl_col-1] = int(training_data[row][column])
                final_table[row][final_tbl_col-1] = int(training_data[row][column])

#tdata table is the x0, x1, z

# put b
for i in range(0,row_len):
    final_table[i][build_column_len-1] = b

# for the process
tdata_table_row = len(tdata_table)  # reusable for final iteration
tdata_table_col = len(tdata_table[0])   #3
output = open("output.txt", "w")  # write mode

while(not_converge != 0):
    for td_row in range(0, tdata_table_row):
        w_index = 0
        a = 0
        # Step 2 a - compute perceptron value
        for td_col in range(0, (tdata_table_col-1)):            # gets the value of x0, x1
            a = a + (tdata_table[td_row][td_col]*w[w_index])    # tdata_table[td_row][td_col] = x0, x1 and so on
            w_index += 1
            if(td_col == (tdata_table_col-2)):                  # gets value of b * w     
                a = a + (b * w[w_index])
        # Step 2 b - determine classification, y,a #y is index 7 and a is index 6
        y = determineY(a,t)

        #append to table
        final_table[td_row][pos_y] = y
        final_table[td_row][pos_a] = a

        # Step 2 c - adjust weights
        w = adjust_weight(td_row,w,a,b,y)
        temp_w = w.copy()
        all_w.append(temp_w)
        temp_w_index = 0

        print("Iteration : ", iteration_num)
        print(temp_w)
        if td_row < tdata_table_row-1:
            for temp in range(pos_b,range_w_index):
                final_table[td_row+1][temp] = temp_w[temp_w_index]
                temp_w_index+= 1

    # Print output
    format_string = "Iteration " + str(iteration_num) + " :\n"
    output.write(format_string)
    output.write(tabulate(final_table,headers))
    output.write("\n")
    iteration_num+=1

    # End of each iteration

    #check if converged
    not_converge = weight_converge(all_w,temp_w)
    all_w.clear()
    all_w.append(temp_w)

    # for the start of the next table
    if td_row < tdata_table_row:
        temp_w_index = 0
        for temp in range(pos_b,range_w_index):
            final_table[0][temp] = temp_w[temp_w_index]
            temp_w_index+= 1
output.close()

        


   






