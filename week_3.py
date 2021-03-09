import urllib.request as request
import json

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    #用 json 模組讀資料
    data=json.load(response)

#確認資料有沒有抓進來
#print(data)

#把 data -> result 中的 results 的值放到變數中
#data_taipei_list 是一個 list, 裡面的資料是 dict
data_taipei_list = data['result']['results']

#print(data_taipei_list, type(data_taipei_list))

with open("data.txt", "w", encoding="utf-8") as file:

    #把每一筆資料抓出來
    for each_data_taipei_list in data_taipei_list:

        #抓 file 的值
        first_pic_url = each_data_taipei_list['file']
        
        #原本是切割 ghttp 切出字串，抓第一個 LIST 再把字串尾 + "g" 就完美惹，但沒想到檢查 TXT 檔後發現，竟然還有 .JPG .png 等等...
        #改用 http 來切，切兩次，取中間，字首再把 http 加回去
        #切出圖片網址，還沒處理完畢
        first_pic_url = first_pic_url.split("http", 2)

        #確認分割後結果以及分割後資料類型，資料類型變為 list
        #print(first_pic_url, type(first_pic_url))

        #將圖片網址重新寫入變數
        first_pic_url ="http"+first_pic_url[1]

        #print(each_data_taipei_list['stitle'], each_data_taipei_list['longitude'], each_data_taipei_list['latitude'], first_pic_url,)

        #寫入資料 景點名稱,經度,緯度,第一張圖檔網址
        file.write(each_data_taipei_list['stitle']+","+each_data_taipei_list['longitude']+","+each_data_taipei_list['latitude']+","+first_pic_url+"\n")

file.close
