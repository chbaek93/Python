# Python
---
AWS에서 사용할 수 있는 파이썬 소스입니다. 

흥미로운 함수는 ... 
```python 

def GetClient(Service = Service, Region = Region, Profile = Profile):
    session = boto3.Session(profile_name = Profile)
    client = session.client(Service, Region)
    
    return client
```
