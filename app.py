from flask import Flask, render_template, request
app = Flask(__name__)
var1="CHAO"
@app.route('/',methods = ['GET'])
def show_index_html():
        var1='hola'
        return render_template('index.html', message=var1)

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        var1='chao'
        #print ("Pay is " + pay)
        #return "Data sent. Please check your program log"
         
        return render_template('index.html',message=var1)
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
#print(h)