from pprint import pprint

import requests

Heroes = ['Hulk', 'Captain America', 'Thanos']


def intelligence_level(names):
    list_2 = {}
    for name in names:
        url = "https://akabab.github.io/superhero-api/api/all.json"
        response = requests.get(url)
        content = response.json()

        for i in content:
            if i["name"] == name:
                list_2[name] = (i["powerstats"]["intelligence"])
    result = max(list_2)
    pprint(result)


if __name__ == '__main__':
    intelligence_level(Heroes)
