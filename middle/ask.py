# coding=utf-8
import requests
import json

def question(asking_texts):

    #키 Headers
    apikey=""

    #내용
    uuid=""
    #text=["면접을 진행하기에 앞서 당부 드릴 것이 있습니다."]

    request_url = "https://wd9v47uopi.execute-api.ap-northeast-2.amazonaws.com/production/api/v1/audio"

    headers = {"Authorization":"LION-API-KEY 5e1f3cd2-9fc4-4156-8d94-3f5153579bba", "Content-Type": "application/json"}

    params = {"model_uuid": uuid, "texts":  [asking_texts], "makeIfNotExists": True}
    response = requests.post(request_url, headers=headers, data=json.dumps(params))

    result = response.json()

    res=result['data'][0]['downloadUrl']
    return (res)
