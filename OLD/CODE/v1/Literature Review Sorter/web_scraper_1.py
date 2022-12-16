from mendeley import Mendeley, MendeleyImplicitGrantAuthenticator

import yaml
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("doi", help="What to search")

args = parser.parse_args()

config_file = 'config.yml'

config = {}

if os.path.isfile(config_file):
    with open('config.yml') as f:
        config = yaml.load(f)
else:
    config['clientId'] = os.environ.get('MENDELEY_CLIENT_ID')
    config['clientSecret'] = os.environ.get('MENDELEY_CLIENT_SECRET')

mendeley = Mendeley(config['clientId'], config['clientSecret'])
session = mendeley.start_client_credentials_flow().authenticate()

doi = args.doi

doc = session.catalog.by_identifier(doi=doi, view='stats')
print('"%s" has %s readers.'.format(doc.title, doc.reader_count))


if __name__ == '__main__':
