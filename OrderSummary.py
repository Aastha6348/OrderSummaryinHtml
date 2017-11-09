import operator
import matplotlib.pyplot as plt

text = open("data.txt", "r")
data = [ ]

for line in text:
    data.append( line.strip().split(","))

# total no. of Orders
countvalue=str(len(data)-1)

# Extracting thr Amount List from data
lstAmount =[]
lstAmount=[x[3] for x in data]
lstAmount.pop(0)

# converting string values of list in integer
lstAmount = map(int, lstAmount)

# total Amount of Orders
totalordrAmount=str(sum(lstAmount))

# Extracting thr Name List from data
lstName=[]
lstName=[x[2] for x in data]
lstName.pop(0)

# dictionary with Customer Name and their order count
my_dict = {i:lstName.count(i) for i in lstName}

# finding the Customers who ordered only Once
one_occurence = dict((k, v) for k, v in my_dict.items() if v == 1)

# finding the No. Of Orders made by Customers
sorted1 = sorted(my_dict.items(), key=operator.itemgetter(1))
values=sorted(sorted1, key = lambda x: int(x[1]))

# creating html report about the transactional data
def repr_html_():
    html = ["<html lang='en'><head><title> Order Transaction History</title></head><body style='padding-top: 20px; padding-right: 25px; padding-left: 25px; border: 2px solid black; font-size: 20px;'>"]
    html.append("<p style='text-align: center; font-size: 30px; color: #CD6155; margin-bottom:1px'><b> Summary of Orders</b> </p>")
    html.append("<hr style='margin-left:30px; margin-right: 30px'>")
    html.append("<div style='margin-left:30px; margin-right: 30px; margin-top:10px; margin-bottom:10px;'><p style='color: #566573'>Total No. Of Orders are : ")
    html.append(countvalue)
    html.append("</p><p style='color: #566573'>Total Amount of Orders : ")
    html.append(totalordrAmount)
    html.append("</p><p style='color: #1B2631; margin-bottom:0px'>Customers ordered only once </p>")
    html.append("<table style='width:300px;border: 1px solid black;'>")
    html.append("<tr style='border: 1px solid black;text-align: left; color: #566573'>")
    html.append("<th >Customer Name</th>")
    html.append("</tr>")
    for key in one_occurence:
        html.append("<tr style='border: 1px solid black; color: #34495E'>")
        html.append("<td >{0}</td>".format(key))
        html.append("</tr>")
    html.append("</table>")
    html.append("<p style='color: #1B2631; margin-bottom:0px'> Customer Order Summary ")
    html.append("</p><table style='width:300px;border: 1px solid black;'>")
    html.append("<tr style='border: 1px solid black;text-align: left; color: #566573'>")
    html.append("<th >Customer Name</th>")
    html.append("<th >Count</th>")
    html.append("</tr>")
    for j, k in values:
        html.append("<tr style='border: 1px solid black; color: #34495E'>")
        html.append("<td >{0}</td>".format(j))
        html.append("<td >{0}</td>".format(k))
        html.append("</tr>")
    html.append("</table></div></body></html>")
    return ''.join(html)

value= repr_html_()


# writing the html file
with open('Summary.html', 'a') as the_file:
    the_file.write(value)

# creating graph about customer history
plt.bar(range(len(values)), [val[1] for val in values], align='center')
plt.xticks(range(len(values)), [val[0] for val in values])
plt.xticks(rotation=70)
plt.title('Customer Order Summary')
plt.xlabel('Customers')
plt.ylabel('Order Count')
plt.show()
plt.savefig('Bargraph.png')