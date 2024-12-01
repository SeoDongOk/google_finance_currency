import pandas as pd
import requests
import os
from dotenv import load_dotenv

# django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "be.settings")
import django
django.setup()
from sendData.models import Swap

if __name__ == "__main__":
    try:
        # env를 통한 Firebase 연동
        load_dotenv("../.env")
        FIREBASE_URL = os.getenv("FIREBASE_URL")
        print(FIREBASE_URL)
        API_KEY = os.getenv("API_KEY")
        url = f"{FIREBASE_URL}.json?auth={API_KEY}"
        response = requests.get(url)
        #데이터 요청
        if response.status_code == 200:
            data = response.json()
        else:
            print("오류 발생:", response.status_code, response.text)

        # 데이터 통합
        target_key=data.keys()
        df=pd.DataFrame()
        for i in target_key:
            row = pd.DataFrame([data[i]])  # 개별 키 데이터를 데이터프레임으로 변환 (리스트 형태로 감쌈)
            df = pd.concat([df, row], ignore_index=True)  # 리스트 형태로 concat에 전달

        # 데이터 추출
        colums=df.columns
        usd_fair = []
        target = "USD"
        for i in colums:
            if target in i[:3]:
                # json 타입으로 저장
                Swap(
                    current_ticker = i[:3],
                    trade_ticker = i[3:],
                ).save()
    except Exception as e:
        print("Error:", e)