'''
To do:

1. Create a table of the input txt [X]
2. Determine classification y [X]
'''

#functions
def determineY(a,t):
    y = 0
    if a >= t:
        y = 1
    return y

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

# make tdata_table dynamic
tdata_table = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
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

# check tdata_table
# for i in range(0,4):
#     for j in range(0,3):
#         print(tdata_table[i][j], end="")
#     print()


for td_row in range(0, tdata_table_row):
    w_index = 0
    a = 0
    for td_col in range(0, (tdata_table_col-1)):
        a = a + (tdata_table[td_row][td_col]*w[w_index])
        w_index += 1
        if(td_col == (tdata_table_col-2)):
            a = a + (b * w[w_index])
    print("a", a)
    # determine classification, y
    y = determineY(a,t)
    print("y",y)

    if td_row != 0:
        #print("adjust weight")
    #adjust weights
        for i in range(0,tdata_table_row):
            w_counter = 0
            for j in range(0, (tdata_table_col-1)):
                w[w_counter] = w[w_counter] + (r*tdata_table[i][j]*(tdata_table[i][2] - y))

                #temp
                if td_row == 1:
                    print("adjusted weight",w[w_counter])
                w_counter += 1

                #print("data",tdata_table[i][j])
            #print("w",w,end="")
        print()


    
print("test")






