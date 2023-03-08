#imports
from flask import Flask, render_template, json, request, session, redirect, url_for
import json

#initialize the flask and SQL Objects
app = Flask(__name__)


#define methods for routes (what to do and display)
@app.route("/")
def main():
    return render_template('index.html', form_action_url=url_for('search'))

@app.route('/search', methods=['POST'])
def search():
    print("in search method")
    f = open('./data/TP_data.json')
    data = json.load(f)
    print(data['countries'][0])
    output_dict = [x for x in data['countries'] if x['ZipCode'] == 'T2N2A7']
    print(output_dict)
    print("length",len(output_dict))
    name = request.form.get("name")
    print(name)
    return 'Enter the data'

if __name__ == "__main__":
    app.run()
