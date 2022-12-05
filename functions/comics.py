from fastapi import Response
from starlette.background import BackgroundTask
from fastapi.responses import FileResponse
import requests
import random
import os
import io
import img2pdf
from bs4 import BeautifulSoup
import time
import re
from os import listdir
import shutil
import natsort




def remove_file(path: str) -> None:
    os.remove(path)



def xhamster_download(comics_url):

    realurl=comics_url
    
    rannumber=random.randint(0,11)
    directory=f"mypdf{rannumber}"
    os.mkdir(directory)
    try:
        # getting response
        response = requests.get(realurl)
        soup=BeautifulSoup(response.text,"html.parser")
        gather=soup.findAll("div" ,class_="image-thumb")
        urls=[images["data-lazy"] for images in gather]

        for i, url in enumerate(urls):
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$',url)
            if not filename:
                Lab.config(text="Regex didn't match with the url: {}".format(url))
                continue
            if i==1:
                i="01"
            if i==2:
                i="02"
            if i==3:
                i="03"
            if i==4:
                i="04"
            if i==5:
                i="05"
            if i==6:
                i="06"
            if i==7:
                i="07"
            if i==8:
                i="08"
            if i==9:
                i="09"
            with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                
                response = requests.get(url)
                
                f.write(response.content)
        
    except Exception as e:
        print(e)


    # creating pdf file
    ran_pdf=random.randint(1,11111)
    pdfname=f"comix{ran_pdf}.pdf"


    try:
        with open(pdfname,"wb") as f:
            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".png"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpeg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

    with open(pdfname,'rb') as file:
        return_data = io.BytesIO(file.read())
        return_data.seek(0)
        # deleting directory
        shutil.rmtree(directory)


    ran=random.randint(0,111)
    headers = {'Content-Disposition': 'inline; filename="out.pdf"'}
    return Response(return_data.getvalue(), headers=headers,media_type="application/octet-stream", background=BackgroundTask(remove_file, pdfname))


def eightmuses_download(comicsurl):
    # https://8muses.xxx/

    realurl = comicsurl

    rannumber=random.randint(0,11)
    directory=f"mypdf{rannumber}"
    os.mkdir(directory)
    try:
        # getting response
        response = requests.get(realurl)
        soup=BeautifulSoup(response.text,"html.parser")
        images=soup.find_all('img')
        urls = [image['src'] for image in images]

        for i,url in enumerate(urls):
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$',url)
            if not filename:
                Lab.config(text="Regex didn't match with the url: {}".format(url))
                continue
            if i==1:
                i="01"
            if i==2:
                i="02"
            if i==3:
                i="03"
            if i==4:
                i="04"
            if i==5:
                i="05"
            if i==6:
                i="06"
            if i==7:
                i="07"
            if i==8:
                i="08"
            if i==9:
                i="09"
            with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                
                response = requests.get(url)
                
                f.write(response.content)
        
    except Exception as e:
        print(e)



    # it becomes difficult for pdf to add files in sequence 
    # so we came with a solution to change the name of files 
    # from 1.jpg to 01.jpg
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)



    # creating pdf file
    ran_pdf=random.randint(1,11111)
    pdfname=f"comix{ran_pdf}.pdf"


    try:
        with open(pdfname,"wb") as f:
            # img.convert('RGB')
            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".png"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpeg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


    with open(pdfname,'rb') as file:
        return_data = io.BytesIO(file.read())
    return_data.seek(0)
    # deleting directory
    shutil.rmtree(directory)
    
    ran=random.randint(0,111)
    headers = {'Content-Disposition': 'inline; filename="8muses.pdf"'}
    return Response(return_data.getvalue(), headers=headers,media_type="application/octet-stream", background=BackgroundTask(remove_file, pdfname))



def king_download(comics_url):
    # https://kingcomix.com/son-finds-mom-online-notenoughmilk/

    realurl = comics_url
        
    rannumber=random.randint(0,11)
    directory=f"mypdf{rannumber}"
    os.mkdir(directory)
    try:
        # getting response
        response = requests.get(realurl)
        soup=BeautifulSoup(response.text,"html.parser")
        images = soup.find_all('figure')
        img = [image.img for image in images]
        urls = [image['src'] for image in img]

        for i, url in enumerate(urls):
            filename = re.search(r'([\w]-[\w*]+[.](png|jpg|gif))$',url)
            if not filename:
                Lab.config(text="Regex didn't match with the url: {}".format(url))
                continue
            if i==0:
                i="00"
            if i==1:
                i="01"
            if i==2:
                i="02"
            if i==3:
                i="03"
            if i==4:
                i="04"
            if i==5:
                i="05"
            if i==6:
                i="06"
            if i==7:
                i="07"
            if i==8:
                i="08"
            if i==9:
                i="09"
            with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                
                response = requests.get(url)
                
                f.write(response.content)
        
    except Exception as e:
        print(e)


    # creating pdf file
    ran_pdf=random.randint(1,11111)
    pdfname=f"comix{ran_pdf}.pdf"

    
    # coping image to pdf
    try:
        with open(pdfname,"wb") as f:
            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".png"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpeg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

    # saving file in memory
    with open(pdfname,'rb') as file:
        return_data = io.BytesIO(file.read())
    return_data.seek(0)
    # deleting directory 
    shutil.rmtree(directory)
    # deletring pdfile
    headers = {'Content-Disposition': 'inline; filename="king.pdf"'}
    return Response(return_data.getvalue(), headers=headers,media_type="application/octet-stream", background=BackgroundTask(remove_file, pdfname))


def nhentai_download(comics_url):
    # https://nhentai.xxx/g/412151/
    realurl=comics_url
    rannumber=random.randint(0,11)
    directory=f"mypdf{rannumber}"
    os.mkdir(directory)
    try:
        # getting response
        response = requests.get(realurl)
        soup=BeautifulSoup(response.text,"html.parser")
        images=soup.find_all('img')
        urls = [image['src'] for image in images]

        for i, url in enumerate(urls):
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$',url)
            if not filename:
                # Lab.config(text="Regex didn't match with the url: {}".format(url))
                continue
            if i==1:
                i="01"
            if i==2:
                i="02"
            if i==3:
                i="03"
            if i==4:
                i="04"
            if i==5:
                i="05"
            if i==6:
                i="06"
            if i==7:
                i="07"
            if i==8:
                i="08"
            if i==9:
                i="09"
            
            with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    url = '{}{}'.format(site, url)
                
                response = requests.get(url)
                
                f.write(response.content)
        
    except Exception as e:
        print(e)


    # it becomes difficult for pdf to add files in sequence 
    # so we came with a solution to change the name of files 
    # from 1.jpg to 01.jpg
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)



    # creating pdf file
    ran_pdf=random.randint(1,11111)
    pdfname=f"comix{ran_pdf}.pdf"


    try:
        with open(pdfname,"wb") as f:
            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".png"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpeg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

    # saving file in memonry
    with open(pdfname,'rb') as file:
        return_data = io.BytesIO(file.read())
    return_data.seek(0)
    # deleting directory
    shutil.rmtree(directory)
   
    ran=random.randint(0,111)
    headers = {'Content-Disposition': 'inline; filename="nhentai.pdf"'}
    return Response(return_data.getvalue(), headers=headers,media_type="application/octet-stream", background=BackgroundTask(remove_file, pdfname))


def porncomics_download(comics_url):
    # https://porncomixinfo.net/chapter/fucking-mom/tzinnxt-fucking-mom/?style=list

    realurl=comics_url
        
    rannumber=random.randint(0,11)
    directory=f"mypdf{rannumber}"
    os.mkdir(directory)
    try:
        # getting response
        response = requests.get(realurl)
        soup=BeautifulSoup(response.text,"html.parser")
        print(soup)
        images = soup.findAll("img")
        print(images)
        urls = [img['src'] for img in images]

        for i,url in enumerate(urls):
            # filename = re.search(r'([\w]-[\w*]+[.](png|jpg|gif))$',url)
            # if not filename:
            #     print("Regex didn't match with the url: {}".format(url))
            #     continue
            if i==1:
                i="01"
            if i==2:
                i="02"
            if i==3:
                i="03"
            if i==4:
                i="04"
            if i==5:
                i="05"
            if i==6:
                i="06"
            if i==7:
                i="07"
            if i==8:
                i="08"
            if i==9:
                i="09"
            with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative 
                    # if it is provide the base url which also happens 
                    # to be the site variable atm. 
                    # url = '{}{}'.format(site, url)
                    pass
                
                response = requests.get(url)
                
                f.write(response.content)
        
    except Exception as e:
        print(e)




    # creating pdf file
    ran_pdf=random.randint(1,11111)
    pdfname=f"comix{ran_pdf}.pdf"


    try:
        with open(pdfname,"wb") as f:
            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".png"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)


            try:
                imgs = []
                for fname in os.listdir(directory):
                    if not fname.endswith(".jpeg"):
                        continue
                    path = os.path.join(directory, fname)
                    if os.path.isdir(path):
                        continue
                    imgs.append(path)
                f.write(img2pdf.convert(natsort.natsorted(imgs)))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


    with open(pdfname,'rb') as file:
        return_data = io.BytesIO(file.read())
    return_data.seek(0)
    # deleting directory
    shutil.rmtree(directory)
    # deletring pdf file

    ran=random.randint(0,111)
    headers = {'Content-Disposition': 'inline; filename="porcomics.pdf"'}
    return Response(return_data.getvalue(), headers=headers,media_type="application/octet-stream", background=BackgroundTask(remove_file, pdfname))
