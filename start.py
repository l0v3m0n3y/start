import requests
class Client():
	def __init__(self):
		self.api="https://api.start.ru"
		self.api_key="a20b12b279f744f2b3c7b5c5400c4eb5"
		self.profile_id=None
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "application/json"}
	def get_languages(self):
		return requests.get(f"{self.api}/languages/content?apikey={self.api_key}",headers=self.headers).json()
	def no_trailer(self):
		return requests.get(f"{self.api}/notrailer?apikey={self.api_key}",headers=self.headers).json()
	def profile_list(self):
		return requests.get(f"{self.api}/notrailer?apikey={self.api_key}",headers=self.headers).json()
	def account_subscriptions(self):
		return requests.get(f"{self.api}/v2/account/subscriptions?apikey={self.api_key}",headers=self.headers).json()
	def billing_subscriptions(self):
		return requests.get(f"{self.api}/billing/subscriptions?apikey={self.api_key}",headers=self.headers).json()
	def refresh_account(self):
		return requests.get(f"{self.api}/auth/refresh?apikey={self.api_key}",headers=self.headers).json()
	def register(self,email,password):
		data={"email":email,"password":password,"device_id":"eb95581b-85bc-4d4f-983e-b58edbaf4125","device_type":"web","client_platform":"start","is_encoded":True}
		req=requests.post(f"{self.api}/v2/auth/email/register?apikey={self.api_key}",json=data,headers=self.headers)
		self.headers=req.headers
		self.profile_id=req.json()['profile_id']
		return req.json()
	def edit_profile(self,birthday:str=None,gender:str=None,name:str=None):
		if birthday:
			data={"birthday":birthday}
			req=requests.put(f"{self.api}/account/person/birthday?apikey={self.api_key}",json=data,headers=self.headers).json()
		if gender:
			data={"gender":gender}
			req=requests.put(f"{self.api}/account/person/gender?apikey={self.api_key}",json=data,headers=self.headers).json()
		if name:
			data={"name":name}
			req=requests.put(f"{self.api}/account/person/name?apikey={self.api_key}",json=data,headers=self.headers).json()
		return req
	def reset_password(self,email):
		data={"device_id":"359847a8-7395-40bf-820b-bbbc21294f24","device_type":"web","client_platform":"start","email":email}
		return requests.post(f"{self.api}/auth/password/reset?apikey={self.api_key}",json=data,headers=self.headers).json()
	def favirites(self,product_id):
		data={"product_id":product_id}
		return requests.post(f"{self.api}/profile/favorites/{self.profile_id}?apikey={self.api_key}",json=data,headers=self.headers).json()
	def rate_content(self,content_id,like:str=True):
		data={"profile_id":self.profile_id,"content_id":content_id,"like":like}
		return requests.post(f"{self.api}/v2/profile/rate-content?apikey={self.api_key}",json=data,headers=self.headers).json()
	def heroes(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/heroes?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}",headers=self.headers).json()
	def posmotret_segodnya(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/v2/showcase/chto-posmotret-segodnya?apikey={self.api_key}&locale={locale}&content_lang={content_lang}&profile_id={self.profile_id}&device_type=web&for_kids={for_kids}",headers=self.headers).json()
	def banner_featured(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/banner/featured?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}&device_type=web",headers=self.headers).json()
	def chyotkie_films(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/v2/showcase/chyotkie-filmy-i-serialy?apikey={self.api_key}&locale={locale}&content_lang={content_lang}&profile_id={self.profile_id}&device_type=web&for_kids={for_kids}",headers=self.headers).json()
	def start_predstavlyaet(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/v2/showcase/start-predstavlyaet-web?apikey={self.api_key}&locale={locale}&content_lang={content_lang}&profile_id={self.profile_id}&device_type=web&for_kids={for_kids}",headers=self.headers).json()
	def trending(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/trending?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}",headers=self.headers).json()
	def recommendation(self,for_kids:str=False,locale:str="ru",content_lang:str="ru"):
		return requests.get(f"{self.api}/recommendation/exp1/featured/{self.profile_id}?apikey={self.api_key}&for_kids={for_kids}&locale={locale}&content_lang={content_lang}",headers=self.headers).json()