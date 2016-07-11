import json

from flask import Flask
from sensu_client import make_client
from rundeck_formatter import format_host
import yaml

app = Flask(__name__)
app.config.update({
    'SENSU_HOSTNAME': 'localhost',
    'SENSU_PORT': '4567',
    'SENSU_USERNAME': '',
    'SENSU_PASSWORD': '',
})
client = make_client(app)

@app.route('/')
def status():
    return 'App server is running'

@app.route('/api/status')
def sensu_status():
    info = client._api_call("{}/info".format(client.api_url), "get")
    return json.dumps(info.json(), sort_keys=True, separators=(',',':'), indent=4)

@app.route('/api/nodes', methods=['GET'])
def node_list():
    # Grabbing all the clients (aka nodes) data and throwing it into a variable
    print('get all clients')
    hosts = client.get_all_clients()
    print('have all clients')

    hostsobj = {}

    # Iterating through the clients
    for host in hosts:
        name, object = format_host(host)
        hostsobj[name] = object

    # Serialize the data to a string for Rundeck to use
    yaml_string = yaml.safe_dump(hostsobj, default_flow_style=False)
    return yaml_string

if __name__ == '__main__':
    app.run()