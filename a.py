'''
To do:

1. Create a table of the input txt [X]
2. Determine classification y [X]
3. adjusting weights done [X]
4. STEP 2 DONE
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
        b = int(input_array[i])
    else:
        training_data.append(input_array[i])

#clear input array
input_array.clear()

# FILE READING - end


# DECLARATIONS
row_len = len(training_data)  #4
column_len = len(training_data[0]) - 1 #5
tdata_array = []
not_converge = 1

# make tdata_table dynamic
tdata_table = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
all_w = []
w = [0,0,0]

# fill tdata_table
for row in range(0,row_len):
    column_index = 0
    for column in range(0,column_len):
        if(column == 0 or column == 2 or column == 4):
            #tdata_array.append(training_data[row][column])
            tdata_table[row][column_index] = int(training_data[row][column])
            column_index += 1

tdata_table_row = len(tdata_table)
tdata_table_col = len(tdata_table[0])

while(not_converge != 0):
    for td_row in range(0, tdata_table_row):
        w_index = 0
        a = 0
        # Step 2 a - compute perceptron value
        for td_col in range(0, (tdata_table_col-1)):
            a = a + (tdata_table[td_row][td_col]*w[w_index])
            w_index += 1
            if(td_col == (tdata_table_col-2)):
                a = a + (b * w[w_index])
        # Step 2 b - determine classification, y
        y = determineY(a,t)



        # Step 2 c - adjust weights
        if td_row != 0:                             # we would be solving weights after the first row
            w = adjust_weight(td_row,w,a,b,y)
            temp_w = w.copy()
            all_w.append(temp_w)
    
    #print(all_w)
    not_converge = weight_converge(all_w,temp_w)
    all_w.clear()
    all_w.append(temp_w)
    print("Not Converge = ", not_converge)
        


   






