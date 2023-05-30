import pandas as pd
from flask import Flask, render_template, request, Response
app = Flask(__name__)
scuola = pd.read_csv('MUHAMMAD ABDUL - ds1880_studenti_scuola_secondaria_2grado_sudd_indirizzo_statale_as_2020_2021.csv', sep=';')


@app.route('/', methods=['GET'])
def home():   
    percorsi = list(set(scuola['PERCORSO']))
    return render_template('home.html', percorsi = percorsi)

@app.route('/esercizio7', methods=['GET'])
def esercizio7():
    scuolaInserita = request.args.get('DenominazioneScuola') 
    table = scuola[scuola['DenominazioneScuola'] == scuolaInserita]
    return render_template('risultato.html', table = table.to_html())

@app.route('/esercizio8', methods=['GET'])
def esercizio8():
    percorsoInserita = request.args.get('percorsi') 
    table = scuola[scuola['PERCORSO'].str.contains(percorsoInserita)][['DenominazioneScuola']].drop_duplicates(subset='DenominazioneScuola').sort_values(by = 'DenominazioneScuola')
    return render_template('risultato.html', table = table.to_html())


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=32245, debug=True)