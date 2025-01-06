import argparse
import csv
import requests

parser = argparse.ArgumentParser(description="Batch insertion of trainings to the CSS internet sites form from the CSV file")
parser.add_argument("uid", help="Define user identifier (see cookies uid parameter)")
parser.add_argument("key", help="Define user key (see cookies key parameter)")
parser.add_argument("session", help="Define the session ID of the logged browser (see cookies PHPSESSID variableparameter)")
parser.add_argument("csv_file_name", help="Define file name of the cvs file")
args = parser.parse_args()

# open the source CSV file with the training data
with open(args.csv_file_name, 'r') as trainings_file:
    trainings = csv.DictReader(trainings_file, delimiter=';')

    # go through the training file with each workout
    for training in trainings:

        # print the training parameters for the user
        print("Adding training: ", training['date'] , ", ", training['type'], ", ", training['time'])

        # define the mandatory parameters of the workout
        data = {
            'name': 'rec',
            '_submit_check': 1,
            'datum': training['date'],
            'cas': training['time'],
            'typ': training['type'],
            'km': training['length'],
        }

        # add the optional parameter avg if defined in CSV file
        if 'avg' in training.keys():
            data['prum'] = training['avg']

        # add the optional parameter eardate_avg if defined in CSV file
        if 'heardate_avg' in training.keys():
            data['t1'] = training['heardate_avg']

        # add the optional parameter eardrate_max if defined in CSV file
        if 'heardrate_max' in training.keys():
            data['t2'] = training['heardrate_max']

        # add the optional parameter feeling if defined in CSV file
        if 'feeling' in training.keys():
            data['pocit'] = training['feeling']

        # add the optional parameter info if defined in CSV file
        if 'info' in training.keys():
            data['info'] = training['info']

        # define the cookies stolen from the web browser
        cookies = {
            'uid': args.uid,
            'key': args.key,
            'PHPSESSID': args.session,
        }

        # Send the HTTP post request to add the workout TODO: check whether it was added properly
        requests.post('https://www.csstodulky.cz/profil/?p=trn', cookies=cookies, data=data)
