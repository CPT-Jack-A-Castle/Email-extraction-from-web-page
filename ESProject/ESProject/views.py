from  django.http import  HttpResponse
from django.shortcuts import render
import re, requests
from bs4 import BeautifulSoup


def index(reuqest):
    return render(reuqest, 'index.html')

def websiteUrl(request):
        url=request.GET.get('website-url')
        try:
            websiteHTML=requests.get(url)
        except:
            plainText = "this website is not reachable"
            content = {'error': plainText}
            return render(request, "index.html", content)
        else:
            htmlParse=BeautifulSoup(websiteHTML.content,'html.parser')
            data=htmlParse.get_text()
            plainText = re.findall("[a-zA-Z0-9-._]+@[a-zA-Z0-9-.]+[.][a-zA-Z0-9]+",data)
            error=""
            if len(plainText)==0:
                error="No email id found in this webpage"

            content={'plainText':plainText,'error':error}

            return render(request,"index.html",content)


