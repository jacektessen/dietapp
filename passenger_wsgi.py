import os,sys,site
os.environ['LD_LIBRARY_PATH'] = '/usr/local/lib'

site.addsitedir('/home/login/site-packages') # glowny site-packages bazujac na module site
sys.path.insert(0,os.getcwd()) #kat z aplikacja
sys.path.insert(0,os.path.join(os.getcwd(), '/site-packages')) #kat site-packages w kat z aplikacja

#site.addsitedir(os.path.join(os.getcwd(), '/site-packages') #ew. to co wyzej ale przez site 
#(jesli instalowales tam przez easy_install)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dietapp.settings")
from django.core.wsgi import get_wsgi_application

#uruchomienie z wyswietlaniem bledow dla python 3.3 
import ErrorMiddlewareV
application = ErrorMiddlewareV.EMV(get_wsgi_application(), True)

#uruchomienie bez wyswietlania bledow 
#application = get_wsgi_application()
#git clone https://BoryczkoPl@bitbucket.org/jacektessen/dietapp.git