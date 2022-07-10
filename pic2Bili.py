import sys
import requests


def uploadPic(SESSDATA, picFile):
    headers = {
        "contentType": 'multipart/form-data',
        "Cookie": f"SESSDATA={SESSDATA}"
    }
    data = {
        "category": "daily",
        "biz": "draw"
    }
    with open(picFile, "rb") as f:
        files = {
            "file_up": f,
        }
        res = requests.post(headers=headers, url="https://api.vc.bilibili.com/api/v1/drawImage/upload",
                            data=data, files=files)
    return res


if __name__ == '__main__':
    argsList = sys.argv
    for i in range(2, len(argsList)):
        uploadRes = uploadPic(argsList[1], argsList[i])
        if uploadRes.json()['code'] != 0:
            msg = uploadRes.json()['message'] + ",请检查SESSDATA是否正确或有效"
            print()
            break
        else:
            imgUrl = uploadRes.json()['data']['image_url']
            print(imgUrl.replace("http", "https"))
