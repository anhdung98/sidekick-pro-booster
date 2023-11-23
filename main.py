import sys
import secrets
import requests
import urllib3
import argparse
from tqdm import trange
from time import sleep

# Disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Arguments parser
parser = argparse.ArgumentParser(description = "Sidekick Browser referrer code booster")
parser.add_argument("-c", "--code", help = "Referrer Code")
parser.add_argument("-n", "--number", help = "Sign-up times. Default: 20")
parser.add_argument("-r", "--retry", help = "Retry times if error. Default: 3")
args = parser.parse_args()

# Generate random string for X-Device-Id
def generate_random_string(length=32):
  characters = '0123456789abcdef'
  random_string = ''.join(secrets.choice(characters) for _ in range(length))
  return random_string

def get_token():
  response = requests.post(
    'https://api.meetsidekick.com/extension/session/temporary',
    json={'type': 'self'},
    verify=False)
  if response.status_code == 200:
    token = response.json()['token']
    return token
  else:
    return None

def set_referrer_code(token, code):
  headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'X-Device-Id': generate_random_string(64),
  }

  json_data = {
    'code': code,
  }

  response = requests.post(
    'https://api.meetsidekick.com/extension/me/change_inviter',
    headers=headers,
    json=json_data,
    verify=False
  )

  if (response.status_code == 200):
    return True
  else:
    return response.json()

# Main program
if __name__ == "__main__":
  referrer_code = args.code or input("Enter Referrer Code: ")
  sign_up_times = int(args.number) if args.number else 20
  retry_times = int(args.retry) if args.retry else 3

  for _ in trange(sign_up_times,
                  desc='Sign-up'):
    for i in range(retry_times):
      token = get_token()
      if token is None:
        print('Failed when connecting to server')
        sys.exit(0)

      response = set_referrer_code(token, referrer_code)
      if response is True:
        break

      print(f'Failed to set referrer code {referrer_code}: {response.get("message", "Server error")}')
      if (i == retry_times - 1):
        print('It seems the tool is not working, please check again')
        sys.exit(0)
      sleep(1)

  print('Set referrers successful')