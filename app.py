#This is an a beginner level tutorial for those who want to get to know Flask

from flask import Flask, jsonify, request  #Flask modules import .. jsonfiy will be user in later versions

api = Flask(__name__)    #calling the flask constructor

@api.route('/')         #default entry point to the API
def testing_api():
    return "API is up and running"

@api.route('/greet')    #http://127.0.0.1:5000/greet 
def hello_world():
    return "Hello. I hope you will be doing fine"

@api.route('/wish', methods=["GET"])  #http://127.0.0.1:5000/wish 
def wish_me_luck():                   #http://127.0.0.1:5000/wish?user=anyname
    data = request.args.get('user')   #getting the optinal parameter through request
    data = data if data else ""       #ternary operator for displaying user name if entered
    return f"dear {data} I wish you luck wherever you go and whenever you are"

@api.route('/do_some_math', methods=["POST"]) #post request for adding two numbers
def do_some_math():
    reqData = request.get_json()    #getting the data in the body of post request
    
    reqX = reqData["x"]             #getting x and y
    reqY = reqData["y"]

    resData = reqX + reqY       #adddition
    resJson = { "z": resData}, 200    #response and response code
    
    return resJson     #returning response


#api starting point
if __name__ == "__main__":
    api.run(debug=True)
