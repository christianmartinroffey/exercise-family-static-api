"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# get all of the family (DONE)
@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    if members is None:
        return "Something went wrong", 404

    return jsonify(response_body), 200

#GET to retrieve one family member (DONE)
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(id)
    if member is None:
        return "There are no people that id", 404

    return jsonify(member), 200

#post to add a new member to the family (DONE)
@app.route('/members', methods=['POST'])
def add_member():
    id = jackson_family._generateId()
    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)
    age = request.json.get("age", None)
    lucky_numbers = jackson_family._generateNumber()

    newMember= { 
        "first_name": first_name,
        "last_name" : last_name,
        "age" : age,
        "lucky_numbers" : lucky_numbers,
    }

    newMember = jackson_family(email=email,  first_name=first_name, last_name = last_name, id=id, lucky_numbers=lucky_numbers )        
    
    try: 
        db.session.add(newMember)        
        db.session.commit()

    
        return jsonify({}),200
    except Exception as err:
        print(str(err))
        return jsonify({'message': str(err)}), 500


#DELETE to remove one family member (DONE)

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(id):
    
    member = jackson_family.delete_member(id)
    if member is None:
        return "There are no people that id", 404

    return jsonify({"member has been deleted"}), 200

# -------
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
