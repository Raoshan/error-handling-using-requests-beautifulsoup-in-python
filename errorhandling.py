import requests
import logging
logging.basicConfig(filename='amazon.log', format='%(asctime)s %(message)s',encoding='utf-8', level=logging.WARNING)
try:
    r = requests.get('https://jssssssssgghhnwr.com/nothinghere')
    r.raise_for_status()
    print(r.status_code)
# except requests.exceptions.HTTPError as err:
#     print("Bad Status Code", r.status_code)
#     raise err
except requests.exceptions.RequestException as err:
    print("Bad Status Code")
    logging.warning(err)

print('Program carries on down here..')