
# -- Reference Url : https://gist.github.com/iMilnb/df47cd6aea9eeac153ff -- # 

def GetIdFromTag(object, tag):
  for o in object.filter(Filters=[{'Name':'tag:Name', 'Values':[tag]}]):
    return o.id 
  return None
  
if __name__ == "__main__":
  ec2 = boto3.resource("ec2")
  Tag = 'Bastion'
  # -- instance : object = client.instances 
  # -- security_groups : object = client.security_groups 
  # -- vpcs : object = client.vpcs 
  # -- subnets : object = client.subnets
  Base = client.security_groups 
  response = GetIdFromTag(Base, Tag)
  print(response)
  
 
