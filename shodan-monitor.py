import shodan
import os

SHODAN_API_KEY = os.environ.get("SHODAN_API_KEY")

api = shodan.Shodan(SHODAN_API_KEY)

query = ""

try:
        # Search Shodan
        results = api.search(query)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print('Open port: {}'.format(result['port']))

except shodan.APIError as err :
    print('Error: {}'.format(err))