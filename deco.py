
import requests

def register(api):
    def fixer(func):
        def wrapper(self,*args,**kwargs):
            params = func(self,*args,**kwargs)
            url = self.host + api
            response = requests.get(url,params=params)
            return response.json()
        return wrapper
    return fixer