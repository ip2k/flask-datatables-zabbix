import pyzabbix
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_get_hosts')
def get_hosts():
    pz = pyzabbix.ZabbixAPI(server='https://your-zabbix-server')
    pz.login('username', 'password')
    hosts = pz.host.get(output='extend', selectGroups='extend', selectInterfaces='extend')
    return jsonify(data=hosts)  # this puts everything inside a { 'data': [...], [...] } in the response so DataTables can deal with it

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
