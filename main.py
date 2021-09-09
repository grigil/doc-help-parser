import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
import requests
import re

url = "https://doc.help/msk/doctors"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=HEADERS, timeout=2) as resp:
                return await resp.text()
        except:
            print("task number #" + url.split("/?page=")[1] + " Failed: Long_request")

async def get_stock_data(i):
    response = await get_html(url + "/?page=" + str(i))

    try:
        soup = BeautifulSoup(response, 'html.parser')
        soup_data = soup.find_all("script")[1].text
        stock_data = re.findall('"count":10,"result":(.*?)\]\,\"direction\"', soup_data)[0]
        new_data = stock_data.split(',{"ex_last_name":null')
        for j in range(1, len(new_data)):
            new_data[j] = '{"ex_last_name":null'+new_data[j]
            with open("doctors.txt", "a") as file:
                file.write(new_data[j] + "\n" + "-" * 80 + "\n")
        print("task number #" + str(i) + " Success")
    except:
        print("task number #" + str(i) + " Failed: Too many requests")

if __name__ == "__main__":
    stock_list = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    pagination = soup.select('a[href*="?page="]')[-1].text
    loop = asyncio.get_event_loop()

    try:
        start = time.time()
        coroutines = [loop.create_task(get_stock_data(i)) for i in range(int(pagination))]
        # coroutines = [loop.create_task(get_stock_data(i)) for i in range(51)]
        loop.run_until_complete(asyncio.wait(coroutines))
    finally:
        loop.close()
        print(f"Время выполнения: {time.time() - start}")