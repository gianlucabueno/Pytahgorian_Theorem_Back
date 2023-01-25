from flask import Flask,request
from calculate import hypotenuse
import json


# create the Flask app
app = Flask(__name__)
      
@app.route('/teorema_result',methods=['POST'])
def calculate():
    hyp = request.form.get('hyp')
    print(hyp)
    
    if hyp == None:
        valor = "!"
        print(valor)
    elif leg_adj == None:
        print("3")
    elif leg_opo == None:
        print("5")

    return "teste"


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
