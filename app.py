from flask import Flask, request
import os
import service

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, I am a test!'

@app.route('/provider', methods=['GET'])
def corrosion_scale():

    args = request.args
    provider = args.get("provider")
    
    return service.search_provider_by_id(provider)

@app.route('/ip', methods=['GET'])
def corrosion():

    args = request.args
    ip = args.get("ip")

    return service.search_provider_by_ip(ip)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000

    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
    app.run()