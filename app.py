# imports
from flask import Flask, render_template, json, request, session, redirect, url_for
import json

# initialize the flask and SQL Objects
app = Flask(__name__, template_folder='templates')

message_404 = {
    "status": 404,
    "message": "Country not in list usa,canada,mexico,india,japan"
}

# define methods for routes (what to do and display)
# @app.route("/")
# def main():
#     return render_template('index.html', form_action_url=url_for('search'))
#
# @app.route('/search', methods=['POST'])
# def search():
#     print("in search method")
#     f = open('./data/TP_data.json')
#     data = json.load(f)
#     print(data['countries'][0])
#     print(len(data['countries']))
#     output_dict = [x for x in data['countries'] if x['ZipCode'] == 'T2V2W2']
#     print(output_dict)
#     print("length",len(output_dict))
#     name = request.form.get("name")
#     print(name)
#     return render_template('index.html')

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

        if fname:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['First_Name'] == fname]
                print("length after fname if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['First_Name'] == fname]
                print("length after fname else cond: ", len(filteredData))

        if lname:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['Last_Name'] == lname]
                print("length after lname if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['Last_Name'] == lname]
                print("length after lname else cond: ", len(filteredData))

        if address1:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['Address1'] == address1]
                print("length after addr1 if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['Address1'] == address1]
                print("length after addr1 else cond: ", len(filteredData))

        if address2:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['Address2'] == address2]
                print("length after addr2 if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['Address2'] == address2]
                print("length after addr2 else cond: ", len(filteredData))

        if city:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['City'] == city]
                print("length after city if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['City'] == city]
                print("length after city else cond: ", len(filteredData))

        if state:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['State'] == state]
                print("length after state if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['State'] == state]
                print("length after state else cond: ", len(filteredData))

        if code:
            if not filteredData:
                filteredData += [x for x in selectedCountriesData if x['ZipCode'] == code]
                print("length after code if cond: ", len(filteredData))
            else:
                filteredData = [x for x in filteredData if x['ZipCode'] == code]
                print("length after code else cond: ", len(filteredData))

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


if __name__ == "__main__":
    app.run()
