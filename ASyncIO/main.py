import asyncio
import requests
import time

async def func1():
    image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

    r = requests.get(image_url) 
    with open("python_logo.png",'wb') as f:
        f.write(r.content)
    await asyncio.sleep(2)
    print("func1")

async def func2():
    image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

    r = requests.get(image_url)
    with open("python_logo2.png",'wb') as f:
        f.write(r.content)
    await asyncio.sleep(2)
    print("func2")

async def func3():
    image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    r = requests.get(image_url)
    with open("python_logo3.png",'wb') as f:
        f.write(r.content)
    await asyncio.sleep(2)
    print("func3")

async def main():
    L= await asyncio.gather(
    
        func1(),
        func2(),
        func3()
    
    )