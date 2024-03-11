import requests
import time

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'{url} is up. Status code: {response.status_code}')
        else:
            print(f'{url} is down. Status code: {response.status_code}')
    except ConnectionError:
        print(f'Failed to connect to {url}. The server is not responding.')

if __name__ == '__main__':
    server_url = 'https://www.google.com'
    while True:
        check_server_status(server_url)
        time.sleep(2)