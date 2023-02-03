"""
Yazar(lar): BatuHanHub

Sürüm: 1.0
"""

import platform 
import psutil
import os

isletim_sistemi = os.name

bilgisayarAdi = platform.node() # Bilgisayar adı (Desktop xxxxx)

# İşletim Sistemleri
isletimSistemi = platform.system() # İşletim sistemi
isletimSistemiSurumu = platform.version() # İşletim sistemi sürümü
windowsSurumu = platform.win32_edition() # Windows sürümü (pro, home vs.)
isletimSistemiMimarisi = platform.architecture()[0] # İşletim sistemi mimarisi
kullaniciAdi = psutil.users()[0] # Kullanıcı adı
kullaniciAdi = kullaniciAdi[0]

# Bilgisayar hakkında
islemci = platform.processor() # İşlemci
islemciHizi = psutil.cpu_freq()[0] # İşlemci hızı
islemciHizi = str(islemciHizi)  
islemciMimarisi = platform.machine() # İşlemci Mimarisi

ramMiktari = psutil.virtual_memory()[0] # RAM
ramMiktari = int(ramMiktari) / 1024 / 1024 / 1024 #kb #mb #gb

takasAlani = psutil.swap_memory()[0] # Swap (takas alanı)
takasAlani = int(takasAlani) / 1024 / 1024 / 1024 #kb #mb #gb

sarj = psutil.sensors_battery()[0] # Şarjın kaç olduğunu gösterir
guc = psutil.sensors_battery()[2] # Güç kablosunun takılı olup olmadığını gösterir

if guc == False:
    guc = "Bağlı Değil"
    
elif guc == True:
    guc = "Bağlı"

diskler = psutil.disk_partitions() # Sistem üzerinde tüm diskler (Bellekler ve disklerin hepsi ve ne biçimde olduğu)

# Dil sürümleri
pythonSurum = platform.python_version() # Python sürümü

def windows():
    return f"""Bilgisayar adı : {bilgisayarAdi}
          
\t\tİŞLETİM SİSTEMİ

İşletim Sistemi              : {isletimSistemi}
İşletim Sistemi Sürümü       : {isletimSistemiSurumu} 
Windows Sürümü               : {windowsSurumu}
İşletim Sistemi Mimarisi     : {isletimSistemiMimarisi}
Kullanıcı Adı                : {kullaniciAdi}

\t\tBİLGİSAYAR HAKKINDA

İşlemci                      : {islemci}
İşlemci Hızı                 : {islemciHizi} GHz
İşlemci Mimarisi             : {islemciMimarisi}
RAM Miktarı                  : {ramMiktari} GB
Takas Alanı                  : {takasAlani} GB
Kalan Güç                    : {sarj}
Bir Güce Bağlı mı?           : {guc}

Diskler                      : \n\n{diskler}

\t\tDİL SÜRÜMLERİ
Python Sürümü                : {pythonSurum}
"""
    
def posix():
    return f"""Bilgisayar adı : {bilgisayarAdi}

\t\tİŞLETİM SİSTEMİ

İşletim Sistemi              : {isletimSistemi}
İşletim Sistemi Sürümü       : {isletimSistemiSurumu} 
İşletim Sistemi Mimarisi     : {isletimSistemiMimarisi}
Kullanıcı Adı                : {kullaniciAdi}

\t\tBİLGİSAYAR HAKKINDA

İşlemci                      : {islemci}
İşlemci Hızı                 : {islemciHizi} GHz
İşlemci Mimarisi             : {islemciMimarisi}
RAM Miktarı                  : {ramMiktari} GB
Takas Alanı                  : {takasAlani} GB
Kalan Güç                    : {sarj}
Bir Güce Bağlı mı?           : {guc}

Diskler                      : \n\n{diskler}

\n\t\tDİL SÜRÜMLERİ
Python Sürümü                : {pythonSurum}
"""

if isletim_sistemi == "nt":
    windows()
    dosya = open ("Sistem Bilgileri.txt", "w", encoding="utf8")
    dosya.write(windows())
    dosya.close()
    
elif isletim_sistemi == "posix":
    posix()
    dosya = open ("Sistem Bilgileri.txt", "w", encoding="utf8")
    dosya.write(posix())
    dosya.close()

input("Çıkmak için bir tuşa basınız...")  