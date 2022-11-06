import requests

url = 'https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=0&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=0&mocMax=999999&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=101000000&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&ONLvid=0&ONLnak=0&zaloga=10&arhiv=0&presort=3&tipsort=DESC&stran=1'

url1 = 'https://www.bolha.com/macke?gclid=Cj0KCQjwk5ibBhDqARIsACzmgLRLm3A9ZDOD4QjeNtuOd-kh4nxzFv9begbwiQoclqPFFh0SCKtevcsaAikVEALw_wcB'

# url2 = 'https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=katerikoli%20tip&znamka2=&model2=&tip2=katerikoli%20tip&znamka3=&model3=&tip3=katerikoli%20tip&cenaMin=100&cenaMax=100000&letnikMin=1970&letnikMax=2022&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=5000&kwMin=0&kwMax=999&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1000000120&EQ8=101000000&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=&paketgarancije=&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=&arhiv=&presort=&tipsort=&stran='

# url3 = 'https://www.avto.net/Ads/results321.asp'

# url4 = 'https://www.avto.net/'

# url5 = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 


odziv = requests.get(url, headers = headers)
def vrni():
    if odziv.status_code == 200:
        return print('dela')
    else:
        return odziv.status_code

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
# besedilo = ''
# for i in range(1, 2):
#     url = f'https://www.avto.net/Ads/results.asp?znamka=&model=&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=0&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=0&mocMax=999999&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=101000000&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&ONLvid=0&ONLnak=0&zaloga=10&arhiv=0&presort=3&tipsort=DESC&stran={i}'
#     a = requests.get(url, headers = headers)
#     besedilo = besedilo + a.content

##################################

# def download_url_to_string(url):
#     """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
#     strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
#     """
#     try:
#         # del kode, ki morda sproži napako
#         r = requests.get(url)
#     except requests.exceptions.ConnectionError:
#         # koda, ki se izvede pri napaki
#         # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
#         print("Napaka pri povezovanju do:", url)
#         return None
#     # nadaljujemo s kodo če ni prišlo do napake
#     if r.status_code == requests.codes.ok:
#         return r.text
#     else:
#         print("Napaka pri prenosu strani:", url)
#         return None


# def save_string_to_file(text, directory, filename):
#     """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
#     locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
#     niz "directory" prazen datoteko ustvari v trenutni mapi.
#     """
#     os.makedirs(directory, exist_ok=True)
#     path = os.path.join(directory, filename)
#     with open(path, 'w', encoding='utf-8') as file_out:
#         file_out.write(text)
#     return None