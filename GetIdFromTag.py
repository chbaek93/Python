
# -- Reference Url : https://gist.github.com/iMilnb/df47cd6aea9eeac153ff -- # 

def GetIdFromTag(object, tag):
  for o in object.filter(Filters=[{'Name':'tag:Name', 'Values':[tag]}]):
    return o.id 
  return None
  
if __name__ == "__main__":
  # ec2 = boto3.resource("ec2")
  client = GetClient() 
  tag = 'Bastion'
  # object = client.instances 
  object = client.security_groups 
  response = GetIdFromTag(base, tag)
  print(response)
  
 
