from enum import Enum

deger = 0

deger2 = 0
class Aylar(Enum):
    Ocak = 1
    Subat=2
    Mart=3
    Nisan=4
    Mayis=5
    Haziran=6
    Temmuz=7
    Agustos=8
    Eylul=9
    Ekim=10
    Kasim=11
    Aralik=12




class Günler(Enum):
    Pazartesi = 1
    Sali=2
    Carsamba=3
    Persembe=4
    Cuma=5
    Cumartesi=6
    Pazar=7


def gunhesapla(gun1, ay1, yil1, gun2, ay2, yil2):

    gun=0
    if (gun2 >= gun1):

        gun = gun2 - gun1;

    if (gun2 < gun1):

         if (yil2 % 4 == 0 and yil2 % 100 != 0 or yil2 % 400 == 0 ): # Artık yılsa, ay Şubatsa ve gün sayısı yetmiyorsa gün2 ye 29 gün ekle.

                if (ay2 == Aylar.Subat.value):
                    gun2 += 29
                    deger = 1 # eğer değer =1 olursa ay da 1 eksilteceğiz.
                    gun = gun2 - gun1



         if (yil2 % 4 != 0 and yil2 % 100 == 0 or yil2 % 400 != 0): #Artık yılsa, ay Şubatsa ve gün sayısı yetmiyorsa gün2 ye 28 gün ekle.

                if (ay2 == Aylar.Subat.value):
                    gun2 += 28
                    deger = 1
                    gun = gun2 - gun1


         if (ay2 == Aylar.Ocak.value or ay2 ==Aylar.Mart.value or ay2 == Aylar.Mayis.value or ay2 == Aylar.Temmuz.value or ay2 ==Aylar.Agustos.value or ay2 == Aylar.Ekim.value or ay2 == Aylar.Aralik.value): # 31 gün içeren aylara eğer gün2 < gün1 se 31 ekle.

                gun2 += 31
                deger = 1
                gun = gun2 - gun1

    # 30 gün içeren aylara eğer gün2 < gün1 se 30 ekle.
         if (ay2 == Aylar.Nisan.value or ay2 == Aylar.Haziran.value or ay2 == Aylar.Eylül.value or ay2 == Aylar.Kasim.value):
                gun2 += 30
                deger = 1
                gun = gun2 - gun1



    return gun



def ayhesapla(ay1,yil1,ay2,yil2):

    ay = 0
    if (deger == 1): #Eğer gün2 < gün1 se değer i kontrol et eğer 1 ise ay ı 1 eksilt.

        ay2 -= 1



    if (ay2 >= ay1):


            ay = ay2 - ay1


    else:

            ay2 += 12
            deger2 = 1
            ay = ay2 - ay1




    return ay


def yilhesapla(yil1,yil2):

    yil = 0
    if (deger2 == 1): # Eğer ay2 < ay1 ise  deger2 yi kontrol et.Değer2 == 1 ise yıldan 1 eksiltme yap.

        yil2 -= 1

    if (yil2 >= yil1):
        yil = yil2 - yil1


    else:
        print("Yanlış yıl girdiniz.")

        exit()


    return yil




print("Sırasıyla gün, ay, yıl giriniz")
gun2=int(input( "Gün2 giriniz"))

if (gun2 < 1 or gun2 > 31):
    print("Yanlış gün değeri girdiniz.")
    exit()

ay2=int(input ("Ay2 giriniz"))
if (ay2 < 1 or ay2 > 12):
    print("Yanlış ay değeri girdiniz.")
    exit()

yil2=int(input("Yıl2 giriniz."))

if (yil2 < 1923):
    print(" 1923 yılından küçük bir değer girdiniz.")

if (yil2 % 4 != 0 and yil2 % 100 == 0 or yil2 % 400 != 0):

    if (ay2 == 2):

        if (gun2 < 1 or gun2 > 28):
            print("Şubat ayı için 28 günden fazla veya 1 günden az değer girdiniz.")
            exit()


if (yil2 % 4 == 0 and yil2 % 100 != 0 or yil2 % 400 == 0):
    if (ay2 == 2):

        if (gun2 < 1 or gun2 > 29):

            print("Şubat ayı için 29 günden fazla veya 1 günden az değer girdiniz.")
            exit()


    # Gün ay yıl 29 Ekim 1923 tarihini göstersin.

gun1 = 29
ay1 = Aylar.Ekim.value
yil1 = 1923

#istersenizherhangibirtarihtenitibarenhesaplamayapabilirsiniz.



a = gunhesapla(gun1, ay1, yil1, gun2, ay2, yil2)

b = ayhesapla(ay1, yil1, ay2, yil2)

c = yilhesapla(yil1, yil2)

print("Aradan ", a ," gun , " ,b , " ay , " , c ," yıl geçti" )


k = 0


yilhesap = 0


ayhesap = 0


if (gun2 - gun1 < 0):

    ay2 -= 1
    if (ay2 - ay1 < 0):

        yil2 -= 1



for i in range(yil1,yil2,1):

    if (i % 4 == 0 and i % 100 != 0 or i % 400 == 0):


        k = 366
        yilhesap = yilhesap + k

    else:


        k = 365
        yilhesap = yilhesap + k



print( c,  " yıl, gün olarak ",yilhesap,"gün eder." )


ayhesap = b * 30

print(b ,  " ay, gün olarak " ,ayhesap , "gün eder.")

int
toplam = yilhesap + ayhesap + a

print("Tüm yıl,ay,gün toplam = ", toplam , " gün eder.")


say = 0

haftaningunu=0;
if (gun1 == 29 and ay1 == Aylar.Ekim.value and yil1 == 1923):

    haftaningunu = 1



for haftaningunu in range(1,toplam,1):

    if (haftaningunu % 7 == 6 or haftaningunu % 7 == 0 ):

         say=say+1




print("1923 den bu yana ",say , " kadar haftasonu geçti.")
