import urllib3, json


# url = "https://enka.shinshin.moe/u/700768234/__data.json"

# json_url = urlopen(url)

# data = json.loads(json_url.read())

# print(data)

# http = urllib3.PoolManager()

# r = http.request('GET', 'https://enka.shinshin.moe/u/700768234/__data.json')
# print(r.status)
# #print(r.data)


def get_data(uid):
    http = urllib3.PoolManager()
    #url = 'https://enka.shinshin.moe/u/700768234/__data.json'
    url = 'https://enka.shinshin.moe/u/' + str(uid) + '/__data.json'
    r = http.request('GET', url)
    if r.status == 200:
        print('Succes to get data. Code: ' + str(r.status))
        data = json.loads(r.data)
        return data
    else:
        print('Error loading data. Code: ' + str(r.status))