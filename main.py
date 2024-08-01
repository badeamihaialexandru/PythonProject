from judete import romania
from flask import Flask
app = Flask(__name__)

def IndepartareCaractere(s):
    inlocuiri = {
        'ă': 'a',
        'â': 'a',
        'î': 'i',
        'ș': 's',
        'ț': 't'
    }
    for original, replacement in inlocuiri.items():
        s = s.replace(original, replacement)
    return s


@app.route('/county/<oras_param>', methods=['GET'])
def GenerareOras(oras_param):
    try:
        for county in romania:
            for oras in romania[county]:
                orasconvertit=IndepartareCaractere(oras)
                if orasconvertit==IndepartareCaractere(oras_param):
                    return county
        return f"city not found"
    except Exception as e:
        return f"ceva nu a mers cum trb"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)