DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'USER': config['USER'],
'PASSWORD': config['PASSWORD'],
# HOST is left blank intentionally here, so it can detect the env.
# and make a decision on whether to connect to our Cloud SQL
# instance via a UNIX socket (i.e deploying via app engine or vm instance) or locally via the CloudSQL proxy.
'PORT': config['PORT'],
} }


DATABASES['default']['HOST'] = config['CLOUDHOST']
if os.getenv('GAE_INSTANCE'):
pass
else:
DATABASES['default']['HOST'] = config['HOST']
