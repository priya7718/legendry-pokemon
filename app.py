#Importing the libraries
import pickle
from flask import Flask, render_template, request
#Global variables

app = Flask(__name__, static_folder="static")
loadedModel = pickle.load(open('KNN Model.pkl', 'rb'))
encoder1 = pickle.load(open('Type 1 Encoder.pkl', 'rb'))
encoder2 = pickle.load(open('Type 2 Encoder.pkl', 'rb'))

# app.config['upload_folder'] = upload_folder
# @app.route('/pokemon image/<path:path>')
# def download_file(path):
#     return send_from_directory('MEDIA_FOLDER', path)


#www.google.com.in/prediction

#Routes
@app.route('/')
def home():
    return render_template('pkm.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    Total = int(request.form['Total'])
    HP = int(request.form['HP'])
    Attack = int(request.form['Attack'])
    Defense = int(request.form['Defense'])   
    SpecialAttack = int(request.form['SpecialAttack'])
    SpecialDefense = int(request.form['SpecialDefense'])
    Speed = int(request.form['Speed'])
    Generation = int(request.form['Generation'])
    Type1  = request.form['Type 1']
    Type2 = request.form['Type 2']

    Type1 = encoder1.transform([Type1])
    Type2 = encoder2.transform([Type2])

    prediction = loadedModel.predict([[Total,HP,Attack,Defense,SpecialAttack,SpecialDefense,Speed,Generation,Type1,Type2]])[0]

    if prediction == 0:       
         prediction = "This pokemon is not legendary"
    else:
         prediction = "This pokemon is legendary"

    return render_template('pkm.html', Output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)