import pokedex as pokedex
import requests
import pycurl
from io import BytesIO



b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.URL,'https://pokeapi.glitch.me/v1/pokemon/greninja')
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()
get_body = b_obj.getvalue()
print('Output of GET request:\n%s' % get_body.decode('utf8'))


pip3 install --compile --install-option="--with-openssl" pycurl

print("Hola Mateo hermoso")
print("Hola papá precioso")
edad = input("¿Cuántos años tienes? ")

print("Wooooooow, ya tienes "+edad+" años!")