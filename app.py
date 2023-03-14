# imports
from flask import Flask, render_template, json, request, session, redirect, url_for
import json

# initialize the flask and SQL Objects
app = Flask(__name__, template_folder='templates')

fullCountryList = ["usa","canada","mexico","india","japan"]

message_404 = {
        "status": 404,
        "message": "Invalid address"
    }
@app.route("/japan", methods=['GET', 'POST'])
def japan():
    print("in japan")
    options = ["Option 1", "Option 2", "Option 3","test"]
    japan_cities = []
    japan_cities.append("")
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']
    japanData = [x for x in countriesData if x['Country'] == 'Japan']
    for entry in japanData:
        city = entry["City"]
        if city not in japan_cities:
            japan_cities.append(city)
    japan_cities.sort()
    print(japan_cities)

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        # city = request.form.get('city')
        code = request.form.get('code')
        city = request.form.get('city')
        print("test",city)
        filteredData = filterData(usa=None, canada=None, mexico=None, india=None, japan="on",
                                  fname=fname, lname=lname, address1=address1, address2=address2,
                                  city=city, state=None, code=code)

        print("filtered data  : ", len(filteredData))
        form_data = request.form
    else:
        usa = fname = lname = address1 = address2 = city = code = ''
        filteredData = []
        form_data = {}
    return render_template('japan.html', data=filteredData, form=form_data,
                           fname=fname, lname=lname,
                           address1=address1, address2=address2, city=city, code=code, options=japan_cities)

@app.route("/usa", methods=['GET', 'POST'])
def usa():
    print("in usa")
    usa_cities = []
    usa_cities.append("")
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']
    usaData = [x for x in countriesData if x['Country'] == 'United States of America']
    for entry in usaData:
        city = entry["City"]
        if city not in usa_cities:
            usa_cities.append(city)
    usa_cities.sort()

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        code = request.form.get('code')
        city = request.form.get('city')
        print("test",city)
        filteredData = filterData(usa="on", canada=None, mexico=None, india=None, japan=None,
                                  fname=fname, lname=lname, address1=address1, address2=address2,
                                  city=city, state=None, code=code)

        print("filtered data  : ", len(filteredData))
        form_data = request.form
    else:
        usa = fname = lname = address1 = address2 = city = code = ''
        filteredData = []
        form_data = {}
    return render_template('usa.html', data=filteredData, form=form_data,
                           fname=fname, lname=lname,
                           address1=address1, address2=address2, city=city, code=code, options=usa_cities)

@app.route("/mexico", methods=['GET', 'POST'])
def mexico():
    print("in mexico")
    mexico_cities = []
    mexico_cities.append("")
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']
    mexicoData = [x for x in countriesData if x['Country'] == 'Mexico']
    for entry in mexicoData:
        city = entry["City"]
        if city not in mexico_cities:
            mexico_cities.append(city)
    mexico_cities.sort()

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        code = request.form.get('code')
        city = request.form.get('city')
        print("test",city)
        filteredData = filterData(usa=None, canada=None, mexico="on", india=None, japan=None,
                                  fname=fname, lname=lname, address1=address1, address2=address2,
                                  city=city, state=None, code=code)

        print("filtered data  : ", len(filteredData))
        form_data = request.form
    else:
        usa = fname = lname = address1 = address2 = city = code = ''
        filteredData = []
        form_data = {}
    return render_template('mexico.html', data=filteredData, form=form_data,
                           fname=fname, lname=lname,
                           address1=address1, address2=address2, city=city, code=code, options=mexico_cities)

@app.route("/canada", methods=['GET', 'POST'])
def canada():
    print("in canada")
    canada_cities = []
    canada_cities.append("")
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']
    canadaData = [x for x in countriesData if x['Country'] == 'Canada']
    for entry in canadaData:
        city = entry["City"]
        if city not in canada_cities:
            canada_cities.append(city)
    canada_cities.sort()

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        code = request.form.get('code')
        city = request.form.get('city')
        print("test",city)
        filteredData = filterData(usa=None, canada="on", mexico=None, india=None, japan=None,
                                  fname=fname, lname=lname, address1=address1, address2=address2,
                                  city=city, state=None, code=code)

        print("filtered data  : ", len(filteredData))
        form_data = request.form
    else:
        usa = fname = lname = address1 = address2 = city = code = ''
        filteredData = []
        form_data = {}
    return render_template('canada.html', data=filteredData, form=form_data,
                           fname=fname, lname=lname,
                           address1=address1, address2=address2, city=city, code=code, options=canada_cities)

@app.route("/india", methods=['GET', 'POST'])
def india():
    print("in india")
    india_cities = []
    india_cities.append("")
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']
    indiaData = [x for x in countriesData if x['Country'] == 'India']
    for entry in indiaData:
        city = entry["City"]
        if city not in india_cities:
            india_cities.append(city)
    india_cities.sort()

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        code = request.form.get('code')
        city = request.form.get('city')
        print("test",city)
        filteredData = filterData(usa=None, canada=None, mexico=None, india="on", japan=None,
                                  fname=fname, lname=lname, address1=address1, address2=address2,
                                  city=city, state=None, code=code)

        print("filtered data  : ", len(filteredData))
        form_data = request.form
    else:
        usa = fname = lname = address1 = address2 = city = code = ''
        filteredData = []
        form_data = {}
    return render_template('india.html', data=filteredData, form=form_data,
                           fname=fname, lname=lname,
                           address1=address1, address2=address2, city=city, code=code, options=india_cities)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("in index def")

    if request.method == 'POST':
        usa = request.form.get('USA')
        canada = request.form.get('Canada')
        mexico = request.form.get('Mexico')
        india = request.form.get('India')
        japan = request.form.get('Japan')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        state = request.form.get('state')
        code = request.form.get('code')

        filteredData = filterData(usa, canada, mexico, india, japan, fname, lname, address1, address2, city, state, code)

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


def filterData(usa, canada, mexico, india, japan, fname, lname, address1, address2, city, state, code):
    print("in filterData method")
    print(fname,lname,address1,address2,city,state,code)
    f = open('./data/TP_data1.json')
    data = json.load(f)
    countriesData = data['countries']

    print("canada : ", canada)
    print("usa : ", usa)
    print("india : ", india)
    print("mexico : ", mexico)
    print("japan : ", japan)
    print("state : ", state)
    print("address1 : ", address1)
    print("address2 : ", address2)
    print("fname : ", fname)
    print("lname : ", lname)

    selectedCountriesData = []

    if usa is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'United States of America']
    if canada is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'Canada']
    if mexico is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'Mexico']
    if india is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'India']
    if japan is not None:
        selectedCountriesData += [x for x in countriesData if x['Country'] == 'Japan']

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

    usa = canada = mexico = india = japan = None
    country = request.args.get('country')
    countryList = request.args.get('country').split(',')
    print(countryList)

    message_404_json = json.dumps(message_404)

    if not set(countryList).issubset(fullCountryList):
        print("not in list")
        return message_404_json

    if "usa" in countryList:
        usa = "on"

    if "canada" in countryList:
        canada = "on"

    if "mexico" in countryList:
        mexico = "on"

    if "india" in countryList:
        india = "on"

    if "japan" in countryList:
        japan = "on"

    fname = request.args.get('fname')
    lname = request.args.get('lname')
    address1 = request.args.get('address1')
    address2 = request.args.get('address2')
    city = request.args.get('city')
    state = request.args.get('state')
    code = request.args.get('code')

    print(fname, lname, address1, address2, city, state, code)

    filteredData = filterData(usa, canada, mexico, india, japan, fname, lname, address1, address2, city, state, code)

    return filteredData


if __name__ == "__main__":
    app.run()
