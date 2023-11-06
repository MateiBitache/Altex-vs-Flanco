import requests
import re
from bs4 import BeautifulSoup
import threading
def faltex(*args):
    url=urlaltex
    url += f'?page={n}&size=48'
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'products' in data:
        for set in data['products']:
            if set['name'].find(obiectsplit[-1])!=-1 or set['name'].find(obiectsplit[-1].lower())!=-1 or set['name'].find(obiectsplit[-1].upper())!=-1:
                altex.append((set['price'], set['sku'], set['name']))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
def fflanco(titlu,obiectsplit):
    global c
    global ha
    try:
        linkul=titlu.find('a',class_="product-item-link")['href']
        titluu=titlu.find("h2").text
        pret="".join(titlu.find('span', class_="special-price").span.text.split())
        print(f"{c}. {titluu} la pretul de {pret}. Link-ul catre produs este {linkul}")
        c += 1
        ha=1
    except Exception:
        pass
obiect=input("Denumire Produs: ")
obiectsplit=obiect.lower().split()
urlaltex = 'https://fenrir.altex.ro/v2/catalog/search/' + '%20'.join(obiectsplit)
urlflanco="https://www.flanco.ro/catalogsearch/result/?q=" + '+'.join(obiectsplit)
altex=[]
n=1
print("Altex: ")
while n<10:
    faltex(headers,urlaltex,obiectsplit,n)
    n+=1
c=1
for tuple in altex:
    link2='https://altex.ro/'
    produs_nume=re.split('[\s,()]+',tuple[2].lower())
    link3="-".join(produs_nume)
    link2+=link3+'/cpd/'+tuple[1]+'/'
    print(f"{c+1}. Prețul pentru {tuple[2]} pe Altex este: {tuple[0]}. Link-ul către produs este: {link2}")
    c+=1


response=requests.get(urlflanco,headers=headers)
htmlf=BeautifulSoup(response.content,'html.parser')
titluri=htmlf.find_all('div', class_="product details product-item-details")
print("\n\nFlanco: ")
c=1
ha=0
for titlu in titluri:
    fflanco(titlu,obiectsplit)
if ha==0:
    print("Nu exista produsul")
