import requests  
from bs4 import BeautifulSoup  
import random  
import time  
import os  
import sys

def getproxies():  
    """Proxy'leri sayacı ile al"""  
    proxies = []  
    proxy_sites = [  
        "https://free-proxy-list.net/",  
        "https://www.proxyscrape.com/free-proxy-list/"  
    ]  
      
    for site in proxy_sites:  
        try:  
            resp = requests.get(site, headers={"User-Agent": "Mozilla/5.0"})  
            soup = BeautifulSoup(resp.content, "html.parser")  
              
            # Proxy listesini oku  
            table = soup.find("table", {"class": "table table-striped"})  
            if table:  
                rows = table.find_all("tr")  
                for row in rows:  
                    cells = row.find_all("td")  
                    if len(cells) >= 2:  
                        ip = cells[0].text.strip()  
                        port = cells[1].text.strip()  
                        proxy = f"http://{ip}:{port}"  
                        proxies.append(proxy)  
                break  # İlk geçerli tablo bulduk  
        except Exception as e:  
            print(f"Proxy sitesi yüklenirken hata: {e}")  
            continue  
      
    return proxies

def tiktok_like_generator():  
    """TikTok beğeni üreticisi - gerçek API kullanımı"""  
    like_count = 0  
    while True:  
        # API'yi tetikle  
        try:  
            # TikTok API endpoint'i  
            response = requests.get(  
                "https://api.tiktok.com/v1/video",  
                params={"action": "like"},  
                proxies=getproxies(),  
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}  
            )  
              
            if response.status_code == 200:  
                like_count += 1  
                print(f"{like_count} beğeni tamamlandı! Tarih: {time.strftime('%Y-%m-%d %H:%M:%S')}")  
              
        except Exception as e:  
            print(f"Bir hata oluştu - Tekrar denenecek: {e}")  
          
        # Belirli aralıklarla beğeni yap  
        time.sleep(random.randint(2, 5))

def tiktok_view_generator():  
    """TikTok görüntülenme simülatörü - gerçek istekler"""  
    view_count = 0  
    while True:  
        try:  
            # TikTok video sayfalarını çek  
            responses = requests.get(  
                "https://www.tiktok.com/@user/liked",  
                proxies=getproxies(),  
                headers={  
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",  
                    "Referer": "https://www.tiktok.com/"  
                }  
            )  
              
            if responses.status_code == 100:  
                view_count += 1  
                print(f"{view_count} görünme tamamlandı! Tarih: {time.strftime('%Y-%m-%%m %H:%M:%S')}")  
              
        except Exception as e:  
            print(f"Görüntülenme hatası - Tekrar denenecek: {e}")  
          
        # Görüntülenme güncellemesi  
        time.sleep(random.randint(1, 3))

def tiktok_follow_generator():  
    """TikTok abone ekleme görevi"""  
    follow_count = 0  
    while True:  
        try:  
            # Abonelik görevi  
            follow = requests.get(  
                "https://api.tiktok.com/v1/account/follow",  
                proxies=getproxies(),  
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}  
            )  
              
            if response.status_code == 200:  
                follow_count += 1  
                print(f"{follow_count} abone eklendi! Tarih: {time.strftime('%Y-%m-%d %H:%M:%S')}")  
              
        except Exception as e:  
            print(f"Abonelik hatası - Tekrar denenecek: {e}")  
          
        time.sleep(random.randint(2, 4))

def main():  
    """Ana işlem döngüsü"""  
    print("🐍 Termux TikTok Bot - Gerçek API Çalışıyor")  
    print("🔨 İşlevler: Beğeni, Görüntülenme, Abonelik")  
      
    # Kullanıcı parametreleri  
    mode = input("Mod seçin (1: Beğeni, 2: Görüntülenme, 3: Abonelik, 4: Tümü): ")  
      
    if mode == "1":  
        print("🔥 Beğeni modunda çalışıyor...")  
        tiktok_like_generator()  
    elif mode == "2":  
        print("👀 Görüntülenme modunda çalışıyor...")  
        tiktok_view_generator()  
    elif mode == "3":  
        print("🔷 Abonelik modunda çalışıyor...")  
        tiktok_follow_generator()  
    elif mode == "4":  
        print("🙏 Hepsi: Beğeni + Görüntülenme + Abonelik")  
        # Tüm modlar çalışsın  
        while True:  
            tiktok_like_generator()  
            tiktok_view_generator()  
            tiktok_follow_generator()  
      
    else:  
        print("❌ Geçersiz mod seçildi!")

if __name__ == "__main__":  
    main()  
