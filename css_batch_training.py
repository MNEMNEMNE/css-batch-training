""" Module providing parsing of parameters """

import argparse
import csv
import requests
import os

parser = argparse.ArgumentParser(description="Batch insertion of trainings to the CSS internet sites form from the CSV file")
parser.add_argument("username", help="Define the username of the user")
parser.add_argument("password", help="Define the password of the user")
parser.add_argument("csv_file_name", help="Define file name of the CSV file")
args = parser.parse_args()

# variable with login data to post requests to the CSS website
data = {
    'action': 'login',
    'jmeno': args.username,
    'heslo': args.password,
    'send': 'Přihlásit',
}

# Send the HTTP post request with url parsed data to login to the CSS website and get the cookies
try:
    response = requests.post('https://csstodulky.cz/login/index.php', data=data, timeout=5)
except requests.exceptions.Timeout:
    print("Error: The request timed out")
    exit(1)

if response.status_code != 200:
    print("Error: Login failed")
    exit(1)

cookies = response.cookies
print("Cookies: ", cookies)

# open the source CSV file with the training data
# Ensure the file exists and is a proper CSV file
if not os.path.isfile(args.csv_file_name):
    print(f"Error: The file {args.csv_file_name} does not exist.")
    exit(1)

try:
    with open(args.csv_file_name, 'r', encoding="utf-8") as trainings_file:
        trainings = csv.DictReader(trainings_file, delimiter=';')

        # Check if the CSV file has the required headers
        required_headers = {'date', 'type', 'time', 'length'}
        if not required_headers.issubset(trainings.fieldnames):
            print(f"Error: The CSV file {args.csv_file_name} does not contain the required headers: {required_headers}")
            exit(1)

        # Go through the training file with each workout
        for training in trainings:
            # Print the training parameters for the user
            print("Adding training: ", training['date'], ", ", training['type'], ", ", training['time'])

            # Define the mandatory parameters of the workout
            data = {
                'name': 'rec',  # TODO: maybe not necessary
                '_submit_check': 1,
                'datum': training['date'],
                'cas': training['time'],
                'typ': training['type'],
                'km': training['length'],
            }

            # Add the optional parameter avg if defined in CSV file
            if 'avg' in training.keys():
                data['prum'] = training['avg']

            # Add the optional parameter heardate_avg if defined in CSV file
            if 'heardate_avg' in training.keys():
                data['t1'] = training['heardate_avg']

            # Add the optional parameter heardrate_max if defined in CSV file
            if 'heardrate_max' in training.keys():
                data['t2'] = training['heardrate_max']

            # Add the optional parameter feeling if defined in CSV file
            if 'feeling' in training.keys():
                data['pocit'] = training['feeling']

            # Add the optional parameter info if defined in CSV file
            if 'info' in training.keys():
                data['info'] = training['info']

            # Send the HTTP post request to add the workout TODO: check whether it was added properly
            requests.post('https://www.csstodulky.cz/profil/?p=trn', cookies=cookies, data=data, timeout=5)
            
except csv.Error as e:
    print(f"Error: The file {args.csv_file_name} is not a proper CSV file. {e}")
    exit(1)
        
