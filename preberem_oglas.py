import re
import os
import csv


# ime mape v kateri imam projektno nalogo
car_directory = 'Projektna_naloga'
# ime datoteke, ki predstavlja vzorec podatkov, saj celotnih se ne morem pridobiti
frontpage_filename = 'vzorec2.html'
# ime CSV datoteke v katero bom shranil podatke
csv_filename = 'avtomobili_razni.csv'


def read_file_to_string(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz"""
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as file_in:
        return file_in.read()


def oglasi_v_blokih(page_content):
    """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
    vrne njih seznam"""
    rx = re.compile(r'<!-- MAKE MODEL CONTAINER -->(.*?)'
                    r'<!------------ END CENA  ------------>',
                    re.DOTALL)

    ads = re.findall(rx, page_content)
    return ads

def olepsamo_oglase(oglasi):
    sez = []
    for oglas in oglasi:
        avtomobil = []
        imeR = re.compile(r'<div class="GO-Results-Naziv bg-dark px-3 py-2.*?'
                    r'font-weight-bold text-truncate text-white text-decoration-none">.*?'
                    r'<span>(.*?)</span>.*?'
                    r'</div>',
                    re.DOTALL)
        ime = re.findall(imeR, oglas)
        avtomobil.append(ime)

        registracijaR = re.compile(r'<td class="w-25 d-none d-md-block pl-3">1.registracija</td>.*?'
                    r'<td class="w-75 pl-3">(.*?)</td>',
                    re.DOTALL)
        registracija = re.findall(registracijaR, oglas)
        if registracija == []:
            avtomobil.append(['NOVO'])
        else:
            avtomobil.append(registracija)

        kilometriR = re.compile(r'<td class="d-none d-md-block pl-3">Prevoženih</td>.*?'
                    r'<td class="pl-3">(.*?) km</td>',
                    re.DOTALL)
        kilometri = re.findall(kilometriR, oglas)
        if kilometri == []:
            avtomobil.append([0])
        else:
            avtomobil.append(kilometri)

        gorivoR = re.compile(r'<td class="d-none d-md-block pl-3">Gorivo</td>.*?'
                    r'<td class="pl-3">(.*?)</td>',
                    re.DOTALL)
        gorivo = re.findall(gorivoR, oglas)
        avtomobil.append(gorivo)

        menjalnikR = re.compile(r'<td class="d-none d-md-block pl-3">Menjalnik</td>.*?'
                    r'<td class="pl-3 text-truncate">(.*?)</td>',
                    re.DOTALL)
        menjalnik = re.findall(menjalnikR, oglas)
        if menjalnik == []:
            avtomobil.append(['elektricni'])
        else:
            avtomobil.append(menjalnik)

        if menjalnik == []:
            motorR = re.compile(r'<td class="d-none d-md-block pl-3">Motor</td>.*?'
                        r'<td class="pl-3 text-truncate">\n'
                        r'\s*(.*?) kW\n*\s*</td>',
                        re.DOTALL)
            motor = re.findall(motorR, oglas)
            avtomobil.append(['nima prostornine'])
            avtomobil.append(motor)

        else:
            prostorninaR = re.compile(r'<td class="d-none d-md-block pl-3">Motor</td>.*?'
                        r'<td class="pl-3 text-truncate">\n'
                        r'\s*(.*?) ccm, .*?\n\s*</td>',
                        re.DOTALL)
            prostornina = re.findall(prostorninaR, oglas)
            avtomobil.append(prostornina)

            mocR = re.compile(r'<td class="d-none d-md-block pl-3">Motor</td>.*?'
                        r'<td class="pl-3 text-truncate">\n'
                        r'\s*.*?, (.*?) kW /.*?</td>',
                        re.DOTALL)
            moc = re.findall(mocR, oglas)
            avtomobil.append(moc)

        baterijaR = re.compile(r'<td class="d-none d-md-block pl-3">Baterija</td>.*?'
                    r'<td class="pl-3 text-truncate">(.*?) kWh</td>',
                    re.DOTALL)
        baterija = re.findall(baterijaR, oglas)
        if baterija == []:
            avtomobil.append(['nima baterije'])
        else:
            avtomobil.append(baterija)

        cenaR = re.compile(r'<div class="GO-Results-Top-Price-TXT-Regular">(.*?) €</div>',
                        re.DOTALL)
        cena = re.findall(cenaR, oglas)
        if cena == []:
            staraR = re.compile(r'<div class="GO-Results-Top-Price-TXT-StaraCena">(.*?) €</div>',
                        re.DOTALL)
            stara = re.findall(staraR, oglas)
            avtomobil.append(stara)
            novaR = re.compile(r'<div class="GO-Results-Top-Price-TXT-AkcijaCena">(.*?) €</div>',
                        re.DOTALL)
            nova = re.findall(novaR, oglas)
            avtomobil.append(nova)
        else:
            avtomobil.append(cena)
            avtomobil.append(['ni akcije'])

        sez.append(avtomobil)
    return sez


def write_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


def write_car_ads_to_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
    slovarjev parametra ads enaki in je seznam ads neprazen."""

    header = ['ime', '1. registracija', 'kilometri', 'gorivo', 'menjalnik', 'prostornina motorja [ccm]', 'moc motorja [kW]', 'baterija [kWh]', 'redna cena', 'akcijska cena [€]']
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for oglas in ads:
            vrstica = [oglas[0][0], oglas[1][0], oglas[2][0], oglas[3][0], oglas[4][0], oglas[5][0], oglas[6][0], oglas[7][0], oglas[8][0], oglas[9][0]]
            writer.writerow(vrstica)


def main():
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """

    ads = oglasi_v_blokih(read_file_to_string(car_directory, frontpage_filename))
    avtucki = olepsamo_oglase(ads)
    write_car_ads_to_csv(avtucki, car_directory, csv_filename)



