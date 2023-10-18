import webbrowser
import time
import pyautogui
import random

#Dosya Kapatıcı Değişkeni
fo = open("/Users/neaderlord/Documents/Belgeler/Belgeler/Kişisel-Projelerim/Motivasyon-Mesajı-Botu/motivasyon.py")

#Motivasyon Mesajları
mesaj1 = 'Bir yuzme antrenoru ogrencisine sinav olarak onu bir havuzun ortasina birakir ve bir kopekbaligi varmis gibi dusunmesini soyler. Ogrenci basarili bir sekilde hayatta kalmayi basarir ve antrenoru ona sunu soyler, Artik basarabilecegin her seyin onunde kopekbaligi varmıs gibi dusunme'
mesaj2 = 'Bir adam bir gun ofise kirmizi bir hirka giydiginde calisma arkadaslari onunla alay eder, Ertesi gun herkes kirmizi bir hirka giyerek ise gelir ve adamin yalniz olmadigini gosterir.'
mesaj3 = 'Bir ogrenci bir hata yapar ve ogretmeni onu kinar Ogrenci Ama benim bir seyler soyleyecek kadar onemli oldugumu dusunmustum diye cevap verir Ogretmeni ona, Sesini duyurmak istiyorsan ilk once susarak basla der.'
mesaj4 = 'Iki adamin birlikte yurudukleri bir yolculukta biri digerine Eger burada agac dikseydik simdi golge altinda yuruyebilirdik der Digeri O zaman ne duruyoruz hemen bir agac dikelim der Yoldan gecenler de onlara katilirlar ve bir orman yaratirlar.'
mesaj5 = 'Ucurtma ucurmak isteyen bir cocuk ruzgarin ters yonde esmesine ragmen ucurtmayi ucurabilmek icin ugrasir Hayatta da bazen zorluklarla karsilasiriz ama yilmamali ve mucadele etmeliyiz.'
mesaj6 = 'Kirik Tencere Bir kadin su tasimak icin iki tane tencere kullanir Bir tencere catlak oldugu icin suyun bir kismi dokulur Ama kadin yine de her gun ayni yolu yaparak catlak tencereyi kullanir Bir gun tencereye baktiginda catlak tencerenin sulardan damlayan yerinde ciceklerin buyudugunu gorur.'
mesaj7 = 'Yolculuk Bir yolculuga cikarken hedefe ulasmak kadar yolculugun kendisini de keyifle yasamak onemlidir.'
mesaj8 = 'Sinirlari Zorlamak Siniri asmak icin kendimize inanmamiz ve cesur olmamiz gerekiyor Sinirlarimizi zorlamak bizi daha iyi bir yerlere getirebilir.'
mesaj9 = 'Yarismacilar Iki yarismaci bir yarisa katilir ve biri digerinden daha hizli kosar Ama digeri yarisi bitirinceye kadar pes etmez ve sonunda kazanir Hayatta da onemli olan hizli kosmak degil pes etmemektir.'
mesaj10 = 'Degisim Degisim kacinilmazdir ve hayatimizda sik sik karsimiza cikar Degisime direnmek yerine onu kabul etmeyi ve firsatlara donusturmeyi ogrenmeliyiz.'
mesaj11 = "Yolculukta ilerlemek icin sadece kucuk bir adim atmaniz yeterlidir."
mesaj12 = "Basarili olmak icin ne yapabileceginizden cok ne yapmak istediginizi belirleyin."
mesaj13 = "Baskalarinin sizi kucuk dusurmesine izin vermeyin Kendinize guvenin ve kendinizi yukseltin."
mesaj14 = "Basarisizlik korkusu sizi geri tutmasin Basarisizliklarinizdan ders cikarin ve devam edin."
mesaj15 = "Cok calismanin bir karsiligi vardir Sabirli olun ve hedeflerinize odaklanin"
mesaj16 = "Kendinizi gelistirmek icin surekli ogrenin ve kendinizi yenileyin."
mesaj17 = "Hayatinizi yoneten kisi sizsiniz Hayatinizi istediginiz sekilde yonlendirin."
mesaj18 = "Basarili olmak icin onceliklerinizi belirleyin ve onlara odaklanin."
mesaj19 = "Ozguveniniz yuksek oldugunda basariniz da yuksek olacaktir."
mesaj20 = "Kendinize inanin ve hayallerinizi gerceklestirmek icin calisin."
mesaj21 = "Basarili olmak icin baskalarina yardim etmekten korkmayin."
mesaj22 = "Kendinizi gelistirmek icin her gun yeni bir seyler ogrenin."
mesaj23 = "Kendinizi motive etmek icin, hedeflerinizi belirleyin ve onlara ulasmak icin adimlar atin."
mesaj24 = "Siz bir seyi basarabileceginizi dusundugunuzde o seyi gerceklestirmek icin tum gucunuzu kullanin."
mesaj25 = "Basarili olmak icin risk almaniz gerekebilir Bu risklerden korkmayin."
mesaj26 = "Basarili olmak icin, her zaman daha iyisini yapmak icin kendinizi zorlayin."
mesaj27 = "Baskalarinin sozlerine kulak asmayin ve kendinize guvenin."
mesaj28 = "Kendinizi gelistirmek icin olumlu tutumlu olun ve kendinize inanin."
mesaj29 = "Baskalarina yardim ederek kendinizi de gelistirebilirsiniz."
mesaj30 = "Kendinizi gelistirmek icin surekli olarak yeni deneyimler yasayin."
mesaj31 = "Baskalarina yardim etmek, kendinize yardim etmek demektir."
mesaj32 = "Kendinize inanin ve korkularinizi yenerken buyuyun."
mesaj33 = "Kendinizi motive etmek icin, hedeflerinizi yazin ve onlara ulasmak icin caba sarf edin."
mesaj34 = "Basarili olmak icin, duzenli olarak kendinizi gelistirin."
mesaj35 = "Hayatinizin kontrolunu elinizde tutun ve hedeflerinize odaklanin."
mesaj36 = "Kendinizi gelistirmek icin, yeni seyler denemektenkorkmayin."
mesaj37 = "tipini skm"
mesaj38 = "sen beni sevmion"
mesaj39 = "yapay zeka yaziyo ben deil"

#Tarayıcıyı Açma 
webbrowser.open_new("https://web.whatsapp.com/send?phone=+905353582641&text&type=+905353582641&app_absent=1")

#Mesajları Random Ayarlama
ran = random.choice([mesaj1, mesaj2, mesaj3, mesaj4, mesaj5, mesaj6, mesaj7, mesaj8, mesaj9, mesaj10, mesaj11,mesaj12,
mesaj13,
mesaj14,
mesaj15,
mesaj16,
mesaj17,
mesaj18,
mesaj19,
mesaj20,
mesaj21,
mesaj22,
mesaj23,
mesaj24,
mesaj25,
mesaj26,
mesaj27,
mesaj28,
mesaj29,
mesaj30,
mesaj31,
mesaj32,
mesaj33,
mesaj34,
mesaj35,
mesaj36,
mesaj37,
mesaj38,
mesaj39])

#Sayfa Yüklenene Kadar Bekleme
time.sleep(25)

#Mesajı Yazma
pyautogui.write(ran)
pyautogui.press("Enter")

#Tarayıcıyı Açma 
webbrowser.open_new("https://web.whatsapp.com/send?phone=+905459547143&text&type=+905459547143&app_absent=1")

#Mesajları Random Ayarlama
ran = random.choice([mesaj1, mesaj2, mesaj3, mesaj4, mesaj5, mesaj6, mesaj7, mesaj8, mesaj9, mesaj10, mesaj11,mesaj12,
mesaj13,
mesaj14,
mesaj15,
mesaj16,
mesaj17,
mesaj18,
mesaj19,
mesaj20,
mesaj21,
mesaj22,
mesaj23,
mesaj24,
mesaj25,
mesaj26,
mesaj27,
mesaj28,
mesaj29,
mesaj30,
mesaj31,
mesaj32,
mesaj33,
mesaj34,
mesaj35,
mesaj36,
mesaj37,
mesaj38,
mesaj39])

#Sayfa Yüklenene Kadar Bekleme
time.sleep(25)

#Mesajı Yazma
pyautogui.write(ran)
pyautogui.press("Enter")

#Uygulamayı Kapatma
fo.close()
