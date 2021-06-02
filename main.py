import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os

# Проверяет есть ли папка видео и если нет, то создает ее
current_dir = os.getcwd()
video_path = f"{current_dir}\\video"
if os.path.exists(video_path)!=True:
    os.mkdir("video")

# Исходная ссылка
url = "https://www.storyblocks.com/video/stock/money-is-falling-on-a-young-man-from-above-slow-motion-svfrderyrk1tphdxd"
#Делаем запрос
r = requests.get(url)
# BeautifulSoup принимает контент с ссылки
soup = BeautifulSoup(r.content,'html.parser')

#проходимя по всем ссылкам source на сайте
for id,link in enumerate(soup.find_all('source')):
    # ищем исходный файл
    src = link.get('src')
    # Устанавливаем заголовки
    ua = UserAgent()
    headers = {'User-Agent':str(ua.random)}
    # шлем запрос к найденной исходной ссылке на файл
    response = requests.get(src,stream=True,headers=headers)
    if response.status_code==200:
        # имя файла
        filename = f"{id}.mp4"
        # открываем файл и пишем в него контент
        with open(f"video\\{filename}","wb") as f:
            for chunck in response.iter_content(1024):
                if chunck:
                    f.write(chunck)
            # выводим сообщение пользователю что видео скачано
            print(f"Video {filename} was downloaded!")
# выводим сообщение, что все видео скачались со страницы
print("Downloading was finished!")
