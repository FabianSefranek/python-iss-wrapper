import requests
from datetime import datetime
class Iss:
    def get_location():
        res = requests.get('http://api.open-notify.org/iss-now.json').json()
        if 'failure' in res['message']:
            return {'message': 'Unable to fetch current location'}
        return res['iss_position']

    def get_next_pass_time(lat=1.0, lon=1.0, alt=1.0):
        res = requests.get(f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}&alt={alt}&n=1').json()
        if 'failure' in res['message']:
            if res['reason'] == 'Latitude must be number between -90.0 and 90.0':
                return {'message': 'Latitude must be number between -90.0 and 90.0'}
            if res['reason'] == 'Longitue must be number between -180.0 and 180.0':
                return {'message': 'Longitue must be number between -180.0 and 180.0'}
            if res['reason'] == 'Altitude must be number between 0 and 10,000':
                return {'message': 'Altitude must be number between 0 and 10,000'}
        else:
            return datetime.fromtimestamp(res['response'][0]['risetime']).strftime('%Y-%m-%d %H:%M:%S')

    def get_pass_times(lat=1.0, lon=1.0, alt=1.0, num=2):
        li = []
        res = requests.get(f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}&alt={alt}&n={num}').json()
        if 'failure' in res['message']:
            if res['reason'] == 'Latitude must be number between -90.0 and 90.0':
                return {'message': 'Latitude must be number between -90.0 and 90.0'}
            if res['reason'] == 'Longitue must be number between -180.0 and 180.0':
                return {'message': 'Longitue must be number between -180.0 and 180.0'}
            if res['reason'] == 'Altitude must be number between 0 and 10,000':
                return {'message': 'Altitude must be number between 0 and 10,000'}
        else:
            for i in res['response']:
                li.append(datetime.fromtimestamp(i['risetime']).strftime('%Y-%m-%d %H:%M:%S'))
            return li

    def get_number_of_astronauts():
        res = requests.get('http://api.open-notify.org/astros.json').json()
        if 'failure' in res['message']:
            return {'message': 'Unable to fetch number of astronauts'}
        return res['number']

    def get_astronauts():
        li = []
        res = requests.get('http://api.open-notify.org/astros.json').json()
        if 'failure' in res['message']:
            return {'message': 'Unable to fetch names of astronauts'}
        for i in res['people']:
            li.append(i['name'])
        return li