import multiprocessing
import requests

# url1 ="https://imagej.net/images/cat.jpg"
# url2= "https://imagej.net/images/Cell_Colony2.jpg"
# url3= "https://imagej.net/images/AuPbSn40.jpg"

def download(url, name):
    print("Started download")
    r=requests.get(url)
    open(f"multiprocessing/file{name}.jpg", 'wb').write(r.content)
    print("Finished download")

if __name__== "__main__":
    url = "https://picsum.photos/2000/3000"
    pros=[]
    for i in range(5):
        p=multiprocessing.Process(target=download, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
