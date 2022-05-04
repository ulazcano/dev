# Libraries
import matplotlib.pyplot as plt, mpld3
import pandas as pd
from math import pi

import base64
from io import BytesIO
from flask import Flask, render_template, request

from matplotlib.figure import Figure
 
# Set data
# df = pd.DataFrame({
# 'group': ['Ale','Uli'],
# 'var1': [5, 1.5],
# 'var2': [5, 10],
# 'var3': [5, 9],
# 'var4': [5, 3],
# 'var5': [5, 5],
# 'var6': [5, 3],
# 'var7': [5, 1]
# })
 
# # ------- PART 1: Create background
 
# # number of variable
# categories=list(df)[1:]
# N = len(categories)
 
# # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
# angles = [n / float(N) * 2 * pi for n in range(N)]
# angles += angles[:1]
 
# # Initialise the spider plot
# ax = plt.subplot(111, polar=True)
 
# # If you want the first axis to be on top:
# ax.set_theta_offset(pi / 2)
# ax.set_theta_direction(-1)
 
# # Draw one axe per variable + add labels
# plt.xticks(angles[:-1], categories)
 
# # Draw ylabels
# ax.set_rlabel_position(0)
# plt.yticks([2,4,6,8,10], ["2","4","6","8","10"], color="grey", size=7)
# plt.ylim(0,10)
 

# # ------- PART 2: Add plots
 
# # Plot each individual = each line of the data
# # I don't make a loop, because plotting more than 3 groups makes the chart unreadable
 
# # Ind1
# values=df.loc[0].drop('group').values.flatten().tolist()
# values += values[:1]
# ax.plot(angles, values, linewidth=1, linestyle='solid', label="Ale")
# ax.fill(angles, values, 'b', alpha=0.1)
 
# # Ind2
# values=df.loc[1].drop('group').values.flatten().tolist()
# values += values[:1]
# ax.plot(angles, values, linewidth=1, linestyle='solid', label="Uli")
# ax.fill(angles, values, 'r', alpha=0.1)
 
# # Add legend
# plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# # Show the graph



# # fig = plt.figure()
# plt.show()





# app = Flask(__name__)


# @app.route("/")
# def hello(figura):
#     # Generate the figure **without using pyplot**.
#     # fig = Figure()
#     # ax = fig.subplots()
#     # ax.plot([1, 2])
#     # Save it to a temporary buffer.
#     buf = BytesIO()
#     figura.savefig(buf, format="png")
#     # Embed the result in the html output.
#     data = base64.b64encode(buf.getbuffer()).decode("ascii")
#     return f"<img src='data:image/png;base64,{data}'/>"




inde = open("templates/index.html").read().format(first_header='goodbye')
print(inde)
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
        return render_template(inde)

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        print ("Pay is " + pay)
        #return "Data sent. Please check your program log"
        return render_template(inde)
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


show_index_html()
