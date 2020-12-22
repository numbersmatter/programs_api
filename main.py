import flask
from flask import request, jsonify
import markupsafe
from markupsafe import escape



def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('not running on Werkzeug Server')
    func()


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# create some test data
programs = [
    {'id': 0,
    'program_name': 'Housing Nonprofit',
    'org_name': 'Organization for Housing',
    'service_type': 'Housing'},
    {'id':1,
    'program_name': 'Food Nonprofit',
    'org_name': 'Organization for Food',
    'service_type': 'Food'},
    {'id':2,
    'program_name': 'Transportation Nonprofit',
    'org_name': 'Organization for Transportation',
    'service_type': 'Transportation'},
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Find Nonprofit Programs</h1><p> This site is a prototype API for finding nonprofit programs</p>"

@app.route('/programs', methods=['GET'])
def all_programs():
    return jsonify(programs)

@app.route('/programs/id', methods=['GET'])
def prog_id():
    #check if an id is provided as part of url
    # if id is provided assign it a variable.
    # if no id is provided display error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: no id provided. Please specify an id"

# create an empty container for results
    results = []

    #loop though the data for matches
    for program in programs:
        if program['id'] == id:
            results.append(program)

    return jsonify(results)

@app.route('/programs/id/<int:prog_id>', methods=['GET'])
def return_program(prog_id):
    #return programs with matching id
    results = []

    for program in programs:
        if program['id'] == prog_id:
            results.append(program)

    return jsonify(results)


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down'

app.run()
