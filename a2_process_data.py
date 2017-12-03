
#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

##print(contents["chickenchicken"])

#print(contents[3][0])
#print("Cell at index 0,1:")
#print(contents[0][1])
#print("Cell at index 1,0:")
#print(contents[1][0])
#print(type(contents));
#print("type of contents")
#print(type(contents[0]))
#print("type of contents[0]")
#print(type(contents[0][0]))
#print("type of contents[0][0]")
concat = 0

concat = contents[0][2] + contents[0][6]

#print(concat)
#print(type(concat))

sum = 0.0
for i in range (2,209):
    sum = sum + float(contents[i][6])

average = sum / 208

#print(sum)
#print(type(sum))

#print(average)
#print(type(average))



#help(concat)

#print(3*contents[0][3])

upmessage = """<!DOCTYPE html>
            <html lang="en">
<head>
    <meta charset="utf-8">
    <title>Chocalate Companies and Their Qualifications</title>
</head>
<body>
<h1>Chocolate Factories all over the world</h1>
        """
altmessage="""
</body>
</html>"""
print(upmessage)

count = 0
sum = 0
for m in range(1,209):
    sum = sum + float(contents[m][6])
    if float(contents[m][6]) > 3:
        count = count+1;
print("<p>sum of ratings is : ")
print(sum)
print("</p>")

print("<p>number of factories which ratings are higher than 3 : ")
print(count)
print("</p>")

comment = """<p>This data shows the chocolote factories all over the world and their statistics like customer rating, bean types, and cacoa percentage.
The table shows that higher cocao percentage makes customers more happy</p>"""
print(comment)
print("<table>")
for j in range(1,209):
    print("<tr>")
    for i in range(1,9):
        print("<td>")
        print(contents[j][i])
        print("</td>")
    print("<tr>")

print("</table>")

print(altmessage)
