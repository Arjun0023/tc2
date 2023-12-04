import csv

data = []
columns = []
rows = []

def mean(list1):
    sum = 0
    for i in list1:
        sum += float(i)
    mean = sum / len(list1)
    return mean

def median(l):
    l.sort()
    return l[len(l)//2]

def mode(l):
    s = list(set(l))
    counts = []
    for i in s:
        counts.append(l.count(i))

    ind = counts.index(max(counts))

    return s[ind]

def variance(l):
    mean1 = mean(l)
    sum = 0
    for i in l:
        sum += (float(i) - mean1)**2
    var = sum/len(l)
    return var

def standDev(l):
    var = variance(l)
    standard = (var**(1/2))

    return standard

def quart(l):
    l.sort()
    q25 = l[int(0.25 * len(l))]
    q75 = l[int(0.75 * len(l))]

    return [q25, q75]

with open("price_data (1).csv", 'r') as file:
     csvreader = csv.reader(file)
     for row in csvreader:
         data.append(row)

for row in data:
    rows.append(row)

for i in range(len(rows[0])):
    column = []
    for row in rows:
        column.append(row[i])
    columns.append(column)

numerical_columns = []
categorical_columns = []
for column in columns:
    try :
        float(column[1])
        numerical_columns.append(column)
    except ValueError:
        categorical_columns.append(column)

print("Name- Pavitra Pai, PRN: 20210802023")
print("TC2-Lab1 ")

print("Numerical Columns: ")
for column in numerical_columns:
    print(column[0])

print('\n')

print("Categorical Columns: ")
for column in categorical_columns:
    print(column[0])

print('\n')

print("Implementing Statistical Analysis on Numerical Data")
print('\n')
for i in range(0, len(numerical_columns)):
    print("Column: ", numerical_columns[i][0], '\n')
    print("Mean of Column is: " , mean(numerical_columns[i][1:len(numerical_columns[0])]))
    print("Median of Column is: " , median(numerical_columns[i][1:len(numerical_columns[0])]))
    print("Mode of Column is: " , mode(numerical_columns[i][1:len(numerical_columns[0])]))
    print("Standard Deviation is: ",
standDev(numerical_columns[i][1:len(numerical_columns[0])]))
    print("Variance of Column is: ",
variance(numerical_columns[i][1:len(numerical_columns[0])]))
    print("Quartile Range of Column is: ",
quart(numerical_columns[i][1:len(numerical_columns[0])]))
    print('\n')

print("Categorizing Categorical Variables into Binary and Nominal Values")
for i in range(len(categorical_columns)):
    if (len(list(set(categorical_columns[i][1:len(categorical_columns[i])])))) == 2:
        print("Column ", categorical_columns[i][0], " has Binary Values.")
    else:
        print("Column ", categorical_columns[i][0], " has Nominal Values.")