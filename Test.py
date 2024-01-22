from getpass import getpass
u=input('username:')
p=getpass('password:')
while True:
  if p=='mysam':
    print(f'login as {u}')
  else:
    print('Incorrect password')
  break
