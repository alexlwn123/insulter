from bs4 import BeautifulSoup
import requests as re
import json
import random

def get_remark(name: str):
  payload = {"from": "from" }
  route = random.choice(routes)
  route = route.replace(':name', name)
  route = route.replace(':from', "God")
  route = route.replace(':noun', "coitus")
  reply = re.get('https://www.foaas.com' + route).text
  soup = BeautifulSoup(reply, "html.parser")
  ans = soup.find_all('meta', limit=2)[-1]['content']
  ans = ans.replace('- God', '\n  - God')
  return ans

def main():
    cities = []
    text = re.get('https://www.foaas.com/operations').text
    soup = BeautifulSoup(text, "html.parser")
    obj = json.loads(str(soup))
    routes = [x['url'] for x in obj][2:]
    print(get_remark("Alex"))

if __name__ == '__main__':
    main()