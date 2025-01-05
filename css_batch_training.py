import argparse
import csv
import requests

parser = argparse.ArgumentParser(description="Batch insertion of trainings to the CSS internet sites form from the CSV file")
parser.add_argument("uid", help="Define user identifier (see cookies uid parameter)")
parser.add_argument("key", help="Define user key (see cookies key parameter)")
parser.add_argument("session", help="Define the session ID of the logged browser (see cookies PHPSESSID variableparameter)")
parser.add_argument("csv_file_name", help="Define file name of the cvs file")
args = parser.parse_args()


with open(args.csv_file_name, 'r') as trainings_file:
    trainings = csv.DictReader(trainings_file, delimiter=';')

    for training in trainings:

        print("Adding training: ", training['date'] , ", ", training['type'], ", ", training['time'])

        data = {
            'name': 'rec',
            '_submit_check': 1,
            'datum': training['date'],
            'cas': training['time'],
            'typ': training['type'],
            'km': training['length'],
#            'prum': training['avg'],
#            't1': training['heardrate_avg'],
#            't2': training['heardrate_max'],
#            'pocit': training['feeling'],
#            'info': training['info'],
        }

        cookies = {
            'uid': args.uid,
            'key': args.key,
            'PHPSESSID': args.session,
        }

        requests.post('https://www.csstodulky.cz/profil/?p=trn', cookies=cookies, data=data)
