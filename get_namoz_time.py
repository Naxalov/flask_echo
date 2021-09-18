import requests
import datetime
import json




def get_namoz_times(longitude, latitude):
    timing = datetime.date.today()
    timing = timing.strftime("%d-%m-%Y")
    print(timing)
    
    r = requests.get(f"http://api.aladhan.com/v1/timings/{timing}?latitude={latitude}&longitude={longitude}&method=3")

    data = r.text

    data = json.loads(data)

    bomdod = data["data"]["timings"]["Fajr"]
    quyosh = data["data"]["timings"]["Sunrise"]
    peshin = data["data"]["timings"]["Dhuhr"]
    asr = data["data"]["timings"]["Asr"]
    shom = data["data"]["timings"]["Maghrib"]
    hufton = data["data"]["timings"]["Isha"]
    hafta_kun = data["data"]["date"]["hijri"]["weekday"]["en"]
    hijriy_oy = data["data"]["date"]["hijri"]["month"]["en"]
    hijriy_sana = data["data"]["date"]["hijri"]["day"]
    shahar = data["data"]["meta"]["timezone"]



    return (f"\n🗓️Bugungi sana: {timing} \n\n☪️Hijriy sana: {hijriy_oy} oyi {hijriy_sana} kuni\nHafta kuni: {hafta_kun} \n\nShahar: 📍{shahar}\n\n🕋 Namoz vaqtlari:\n\nBomdod:  {bomdod} \nQuyosh chiqishi: {quyosh} \nPeshin: {peshin} \nAsr: {asr} \nShom: {shom}, \nHufton: {hufton}")



def get_by_city(city_name):
    timing = datetime.date.today()
    timing = timing.strftime("%d-%m-%Y")
    URL = "http://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city_name,
        "country": "country",
        "month": "08",
        "year": "2021"
    }
    r = requests.get(URL, params=params)
    data = r.json()

    bomdod = data["data"]["timings"]["Fajr"]
    quyosh = data["data"]["timings"]["Sunrise"]
    peshin = data["data"]["timings"]["Dhuhr"]
    asr = data["data"]["timings"]["Asr"]
    shom = data["data"]["timings"]["Maghrib"]
    hufton = data["data"]["timings"]["Isha"]
    hafta_kun = data["data"]["date"]["hijri"]["weekday"]["en"]
    hijriy_oy = data["data"]["date"]["hijri"]["month"]["en"]
    hijriy_sana = data["data"]["date"]["hijri"]["day"]
    shahar = data["data"]["meta"]["timezone"]

    return (f"\n🗓️Bugungi sana: {timing} \n\n☪️Hijriy sana: {hijriy_oy} oyi {hijriy_sana} kuni\nHafta kuni: {hafta_kun} \n\nShahar: 📍{shahar}\n\n🕋 Namoz vaqtlari:\n\nBomdod:  {bomdod} \nQuyosh chiqishi: {quyosh} \nPeshin: {peshin} \nAsr: {asr} \nShom: {shom}, \nHufton: {hufton}")
