# import os
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# def get_file_urls(html_file_path):
#     with open(html_file_path, 'r', encoding='utf-8') as file:
#         html_content = file.read()
    
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Obține toate link-urile către fișiere Excel
#     excel_files = [link.get('href') for link in soup.find_all('a') if link.get('href').endswith('.xlsx')]

#     return excel_files

# def download_file(url, save_path):
#     response = requests.get(url)
#     with open(save_path, 'wb') as file:
#         file.write(response.content)


# def delete(file_paths):
#         # Șterge fișierul după utilizare
#     for file_path in file_paths:
#         os.remove(file_path)
#         print(f"Fișier șters: {file_path}")


import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_excel_file(file_path):
    df = pd.read_excel(file_path)
    print(f"Conținutul fișierului {file_path}:")
    print(df)
    os.remove(file_path)
    print(f"Fișier șters: {file_path}")

@app.route('/', methods=['GET'])
def upload_form():
    return '''
    <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interfață generare automată organigrame</title>
        <style>
            .interfata h2{
                text-align: center;
                font-family: 'Times New Roman', Times, serif;
                text-shadow: darkgrey;
                text-shadow: 5px 5px 7px rgba(0, 0, 0, 0.5);
            }
            .interfata h4{
                text-align: right;
                font-family: 'Times New Roman', Times, serif;
                text-shadow: darkgrey;
                text-shadow: 5px 5px 7px rgba(0, 0, 0, 0.5);
            }
            .button-intf{
                float: right;
                padding: 30px 60px;
                margin: 10px;
                cursor: pointer;
                font-family: 'Times New Roman', Times, serif;
                text-align: center;
                background-color: #00A676;
                color: #000000;
                border: none;
                border-radius: 5px;
                margin-left: 700px;
                margin-top: 30x;
                text-shadow: 5px 5px 7px rgba(0, 0, 0, 0.5);
                width: 500px; /* Lățimea casetelor */
                height: 10px; /* Înălțimea casetelor */
                display: flex;
                flex-direction: column;
                box-shadow: 5px 5px 7px rgba(0,0,0,0.5);
		
            }
            .button:hover {
                background-color: #296c2c;
		color:white;
            }
            .label {
                padding: 10px 20px;
                font-size: 20px;
		text-shadow: 5px 5px 7px rgba(0, 0, 0, 0.5);
		font-family: 'Times New Roman', Times, serif;
                background-color: #00A676;
                color: white;
                border: none;
                cursor: pointer;
                margin: 10px;
                display: flex;
                flex-direction: column;
		margin-top: 30px;
            }
            .label:hover {
                background-color: #296c2c;
		color: white;
            }
	.tooltip {
            position: relative;
            display: inline-block;
            cursor: pointer;
            color: blue;
            text-decoration: underline;
	    margin-left: 500px;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: 400px;
            background-color: #f9f9f9;
            color: #000;
            text-align: center;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            bottom: -1000%; /* Poziționează caseta de text deasupra semnului întrebării */
            left: -7000%;
            opacity: 0;
            transition: opacity 0.3s;
        }
	.tooltip1 {
            position: relative;
            display: inline-block;
            cursor: pointer;
            color: blue;
            text-decoration: underline;
	    margin-left: 500px;
        }

	.tooltip1 .tooltiptext1 {
            visibility: hidden;
            width: 400px;
            background-color: #f9f9f9;
            color: #000;
            text-align: center;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            bottom: -300%; /* Poziționează caseta de text deasupra semnului întrebării */
            left: -5700%;
            opacity: 0;
            transition: opacity 0.3s;
        }
.checkbox-container {
	    margin-left: 700px;
            display: flex;
	    flex-direction: column;
            flex-wrap: wrap;
        }
        .checkbox-container label {
	    
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin: 5px;
            cursor: pointer;
        }
        .checkbox-container input[type="checkbox"] {
            display: none;
        }
        .checkbox-container input[type="checkbox"]:checked + label {
	    
            background-color: #add8e6;
            border-color: #00f;
        }
.container {
            display: flex;
            align-items: center; /* Aliniază elementele pe axa verticală */
        }
        .item {
            margin: 10px;
        }
        </style>
    </head>
    <body>
        <div class="interfata">
            <h2><strong><em>Interfață generare automată organigrame PPC România</em></strong></h2>
            <br><br><br><br>
            
        </div>
<form action="submit_form.php" method="post">
<div class="tooltip" onclick="toggleTooltip()">?
        <span class="tooltiptext">Pentru a putea genera organigramele trebuie ca documentele încărcate (două excel-uri) să conțină: <br>Denumiri companii ordonate crescător după coloana "OU Company/Power Plant father":{ID obiect <br>Nume obiect<br>OU Company/Power Plant father<br>Desc. OU Company/Power Plant father-unitatea superioara}<br>Lista angajati:{DEN COMPANIE<br>COD DEPARTAMENT<br>DEN DEPARTAMENT<br>NUME<br>PRENUME<br>FUNCTIE<br>TIP ANGAJAT<br>DEN CATEGORIE PERSONAL}
</span>
	
    </div>
	<label for="file-upload" class="button-intf"><strong><em>Încărcați fișierele necesare.</em></strong></label>
<br>
            <input id="file-upload" type="file" onchange="handleFileUpload(event)" style="float: right;">
<br><br>
	<input id="file-upload" type="file" onchange="handleFileUpload(event)" style="float: right;">


            <br><br><br><br><br>

<div class="tooltip1" onclick="toggleTooltip1()">?
        <span class="tooltiptext1">Se vor descărca în PC organigrama/organigramele companiilor selectate anterior în format pdf și xlsx.
</span>
</div>
<br><br>
        <label for="comp">
<div class="interfata">
            <h4><strong><em>Alege compania pentru care doriți să se genereze organigrama:</em></strong></h4>
            <br>        </div>
</label>
        <div class="checkbox-container">
            <input type="checkbox" id="PPC_BLUE_ROMANIA_SRL" name="comp[]" value="PPC_BLUE_ROMANIA_SRL">
            <label for="PPC_BLUE_ROMANIA_SRL">PPC BLUE ROMANIA SRL</label>

            <input type="checkbox" id="PPC_ADVANCED_ENERGY_SERVICES_ROMANIA_SRL" name="comp[]" value="PPC_ADVANCED_ENERGY_SERVICES_ROMANIA_SRL">
            <label for="PPC_ADVANCED_ENERGY_SERVICES_ROMANIA_SRL">PPC ADVANCED ENERGY SERVICES ROMANIA SRL</label>

            <input type="checkbox" id="PPC_RENEWABLES_ROMANIA_S.R.L." name="comp[]" value="PPC_RENEWABLES_ROMANIA_S.R.L.">
            <label for="PPC_RENEWABLES_ROMANIA_S.R.L.">PPC RENEWABLES ROMANIA S.R.L.</label>

	    <input type="checkbox" id="PPC_TRADING_SRL" name="comp[]" value="PPC_TRADING_SRL">
            <label for="PPC_TRADING_SRL">PPC TRADING SRL</label>

	    <input type="checkbox" id="PPC_SERVICII_COMUNE_SA" name="comp[]" value="PPC_SERVICII_COMUNE_SA">
            <label for="PPC_SERVICII_COMUNE_SA">PPC SERVICII COMUNE SA</label>
	    <input type="checkbox" id="PPC_ENERGY_SERVICES_CO_SA" name="comp[]" value="PPC_ENERGY_SERVICES_CO_SA">
            <label for="PPC_ENERGY_SERVICES_CO_SA">PPC ENERGY SERVICES CO SA</label>

	    <input type="checkbox" id="PPC_ENERGIE_SA" name="comp[]" value="PPC_ENERGIE_SA">
            <label for="PPC_ENERGIE_SA">PPC ENERGIE SA</label>

	    <input type="checkbox" id="PPC_ENERGIE_MUNTENIA_SA" name="comp[]" value="PPC_ENERGIE_MUNTENIA_SA">
            <label for="PPC_ENERGIE_MUNTENIA_SA">PPC ENERGIE MUNTENIA SA</label>

	    <input type="checkbox" id="RETELE_ELECTRICE_DOBROGEA_SA" name="comp[]" value="RETELE_ELECTRICE_DOBROGEA_SA">
            <label for="RETELE_ELECTRICE_DOBROGEA_SA">RETELE ELECTRICE DOBROGEA SA</label>

	    <input type="checkbox" id="RETELE_ELECTRICE_BANAT_SA" name="comp[]" value="RETELE_ELECTRICE_BANAT_SA">
            <label for="RETELE_ELECTRICE_BANAT_SA">RETELE ELECTRICE BANAT SA</label>

	    <input type="checkbox" id="RETELE_ELECTRICE_MUNTENIA_SA" name="comp[]" value="RETELE_ELECTRICE_MUNTENIA_SA">
            <label for="RETELE_ELECTRICE_MUNTENIA_SA">RETELE ELECTRICE MUNTENIA SA</label>

        </div>
<br><br>
        <input type="submit" value="Trimite" style="float: right;">
        <br>
        <label for="document">
        <div class="interfata">
                <h4><strong><em>Alegeți tipul de fișier care să se genereze.</em></strong></h4>
        </div></label>
        <div class="checkbox-container">
            <input type="checkbox" id="PDF" name="document[]" value="PDF">
            <label for="PDF">PDF</label>

            <input type="checkbox" id="EXCEL" name="document[]" value="EXCEL">
            <label for="EXCEL">EXCEL</label>

        </div>
        <br><br>
        <input type="submit" value="Trimite" style="float: right;">
            <a href="path/to/your/file.txt" download="file.txt" class="button-intf"><strong><em>Descărcați</em><strong></a>

</form>
        <script>
            function handleFileUpload(event) {
                const file = event.target.files[0];
                if (file) {
                    alert(`Fișierul selectat: ${file.name}`);
                    // Aici poți adăuga codul pentru a gestiona încărcarea fișierului
                }
            }
        </script>
	<script>
        function toggleTooltip() {
            var tooltipText = document.querySelector('.tooltip .tooltiptext');
            if (tooltipText.style.visibility === 'hidden' || tooltipText.style.visibility === '') {
                tooltipText.style.visibility = 'visible';
                tooltipText.style.opacity = '1';
            } else {
                tooltipText.style.visibility = 'hidden';
                tooltipText.style.opacity = '0';
            }
        }
    </script>
<script>
        function toggleTooltip1() {
            var tooltipText = document.querySelector('.tooltip1 .tooltiptext1');
            if (tooltipText.style.visibility === 'hidden' || tooltipText.style.visibility === '') {
                tooltipText.style.visibility = 'visible';
                tooltipText.style.opacity = '1';
            } else {
                tooltipText.style.visibility = 'hidden';
                tooltipText.style.opacity = '0';
            }
        }
    </script>

    </body>
</html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    files = request.files.getlist('file')
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            process_excel_file(file_path)
    return redirect(url_for('upload_form'))

# if __name__ == "__main__":
#     os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#     app.run(debug=True)
