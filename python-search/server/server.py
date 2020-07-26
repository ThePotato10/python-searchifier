from flask import Flask, request
from flask_cors import CORS, cross_origin
from search2 import sort_by_rank

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/search')
@cross_origin(supports_credentials=True)
def sendSearchResults():
    x = request.args.get('q').lower()
    specifity = float(request.args.get('specifity'))
    return sort_by_rank(x, specifity)

if __name__ == '__main__':
    app.run()