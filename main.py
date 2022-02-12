import requests
import csv
import json

def storing_csv():
    url = 'http://www.floatrates.com/daily/idr.json'
    res = requests.get(url).json()

    data = []

    for d in res.values():
        code = d['code']
        name = d['name']
        date = d['date']
        inverserate = d['inverseRate']
        content = [code, name, date, inverserate]
        data.append(content)

    with open('data.csv', mode='w', newline='', encoding="utf-8") as csv_file:
        # Create object
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write
        writer.writerow(["CODE", "NAME", "DATE", "INVERSE RATE"])
        for d in data:
            writer.writerow(d)
    print("Writing to CSV has been successful !")

def storing_json():
    url = 'http://www.floatrates.com/daily/idr.json'
    res = requests.get(url).json()

    data = []

    for d in res.values():
        code = d['code']
        name = d['name']
        date = d['date']
        inverserate = d['inverseRate']

        content = {
            "code": code,
            "name": name,
            "date": date,
            "inverse_rate ": inverserate
        }
        data.append(content)

    # Serializing json
    json_object = json.dumps(data, indent=4)
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
    print("Writing to JSON has been successful !")


storing_csv()
storing_json()