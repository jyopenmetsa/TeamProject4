# imports
from flask import Flask, render_template, json, request, session, redirect, url_for
import json

# initialize the flask and SQL Objects
app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    print("in index def")

    if request.method == 'POST':
        usa = request.form.get('countryUSA')
        canada = request.form.get('countryCanada')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        state = request.form.get('state')
        code = request.form.get('code')

        filteredData = filterData(usa, canada, fname, lname, address1, address2, city, state, code)

        print("filtered data  : ", len(filteredData))
        form_data = request.form
    else:
        usa = fname = lname = address1 = address2 = state = city = code = ''
        filteredData = []
        form_data = {}
    return render_template('index.html', data=filteredData, form=form_data,
                           fname=fname, lname=lname,
                           address1=address1, address2=address2,
                           state=state, city=city, code=code)


def filterData(usa, canada, fname, lname, address1, address2, city, state, code):
    print("in filterData method")
    print(fname,lname,address1,address2,city,state,code)
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']

    print("canada : ", canada)
    print("usa : ", usa)
    print("state : ", state)
    print("address1 : ", address1)
    print("address2 : ", address2)

    selectedCountriesData = []

    if usa is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'United States of America']
    if canada is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'Canada']

    print(len(selectedCountriesData))

    filteredData = []
    filteredData[:] = []
    print("length of filter data before : ", len(filteredData))

    print(fname, lname, address1, address2, city, state, code)

    if fname:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if fname in x['First_Name']]
            print("length after fname if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if fname in x['First_Name']]
            print("length after fname else cond: ", len(filteredData))

    if lname:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if lname in x['Last_Name']]
            print("length after lname if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if lname in x['Last_Name']]
            print("length after lname else cond: ", len(filteredData))

    if address1:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if address1 in x['Address1']]
            print("length after addr1 if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if address1 in x['Address1']]
            print("length after addr1 else cond: ", len(filteredData))

    if address2:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if address2 in x['Address2']]
            print("length after addr2 if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if address2 in x['Address2']]
            print("length after addr2 else cond: ", len(filteredData))

    if city:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if city in x['City']]
            print("length after city if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if city in x['City']]
            print("length after city else cond: ", len(filteredData))

    if state:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if state in x['State']]
            print("length after state if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if state in x['State']]
            print("length after state else cond: ", len(filteredData))

    if code:
        if not filteredData:
            filteredData += [x for x in selectedCountriesData if code in x['ZipCode']]
            print("length after code if cond: ", len(filteredData))
        else:
            filteredData = [x for x in filteredData if code in x['ZipCode']]
            print("length after code else cond: ", len(filteredData))

    return filteredData

@app.route('/filter', methods=['GET'])
def filter():
    selectedCountriesData = []

    # usa = request.args.get('usa')
    # canada = request.args.get('canada')
    usa, canada, mexico, india, japan = None
    country = request.args.get('country')
    if country == "usa":
        usa = "on"

    if country == "canada":
        canada = "on"

    if country == "mexico":
        mexico = "on"

    if country == "india":
        india == "on"

    if country == "japan":
        japan = "on"

    fname = request.args.get('fname')
    lname = request.args.get('lname')
    address1 = request.args.get('address1')
    address2 = request.args.get('address2')
    city = request.args.get('city')
    state = request.args.get('state')
    code = request.args.get('code')

    print(fname, lname, address1, address2, city, state, code)

    filteredData = filterData(usa, canada, fname, lname, address1, address2, city, state, code)

    return filteredData


if __name__ == "__main__":
    app.run()
