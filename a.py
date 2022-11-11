'''
To do:

1. Create a table of the input txt [X]
2. Determine classification y [X]
3. adjusting weights done [X]
4. STEP 2 DONE [X]
5. FILL THE FINAL TABLE WITH THE OUTPUTS [X]
6. PRINT THE TABLE NICELY
7. WRITE TO OUTPUT

Notes:
If you have 3 columns, for each iteration you would have a total of 9 columns
3 x, 3 w, a, b,  y
'''

#functions
def determineY(a,t):
    y = 0
    if a > t:
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
        b = float(input_array[i])
    else:
        training_data.append(input_array[i])

#clear input array
input_array.clear()

# FILE READING - end

# DECLARATIONS
row_len = len(training_data)    #4
column_len = len(training_data[0])-1 # do not change
build_column_len = int(len(training_data[0])/2)             #3
tdata_array = []
not_converge = 1
tdata_table = []
all_w = []
final_tbl_col = build_column_len * 2 + 3     # total number of columns for each iteration
pos_y = final_tbl_col-2
pos_a = final_tbl_col-3
iteration_num = 1


# create w array and tdata_table
tdata_table = [[0 for col in range(0,build_column_len)] for row in range(0,row_len)]
w = [0] * build_column_len
final_table = [[0 for col in range(0,final_tbl_col)] for row in range(0,row_len)]

# fill tdata_table with given input and also set final table
for row in range(0,row_len):
    column_index = 0
    for column in range(0,column_len):
        #if(column == 0 or column == 2 or column == 4): # if module num % 2 == 0
        if(column % 2 == 0):
            #tdata_array.append(training_data[row][column])
            tdata_table[row][column_index] = int(training_data[row][column])
            column_index += 1
            if column == 4:    
                final_table[row][final_tbl_col-1] = int(training_data[row][column])

# put b
for i in range(0,row_len):
    final_table[i][build_column_len-1] = b

# for the process
tdata_table_row = len(tdata_table)  # reusable for final iteration
tdata_table_col = len(tdata_table[0])

while(not_converge != 0):
    print("Iteration ",iteration_num, ":")
    for td_row in range(0, tdata_table_row):
        w_index = 0
        a = 0
        # Step 2 a - compute perceptron value
        for td_col in range(0, (tdata_table_col-1)):
            a = a + (tdata_table[td_row][td_col]*w[w_index])
            w_index += 1
            if(td_col == (tdata_table_col-2)):
                a = a + (b * w[w_index])
        # Step 2 b - determine classification, y,a #y is index 7 and a is index 6
        y = determineY(a,t)

        #append to table
        final_table[td_row][pos_y-1] = y
        final_table[td_row][pos_a-1] = a


        # Step 2 c - adjust weights
        if td_row != 0:                             # we would be solving weights after the first row
            w = adjust_weight(td_row,w,a,b,y)
            temp_w = w.copy()
            all_w.append(temp_w)
            
        print(final_table)
    iteration_num+=1

    # End of each iteration
    
    not_converge = weight_converge(all_w,temp_w)
    all_w.clear()
    all_w.append(temp_w)


    #print("Not Converge = ", not_converge)
        


   






