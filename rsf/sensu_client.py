# Using PySensu to connect to Sensu's API

from pysensu import pysensu

def make_client(app):
    hostname = app.config.get('SENSU_HOSTNAME')
    username = app.config.get('SENSU_USERNAME')
    password = app.config.get('SENSU_PASSWORD')
    port = app.config.get('SENSU_PORT')

    client = pysensu.Pysensu(hostname, user=username, password=password, port=port)
    return client