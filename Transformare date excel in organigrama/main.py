from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import os
from functions.graph_functions import Graph, build_graph, print_graph_dfs, level_order_traversal
from functions.pdfFile import generate_pdf
import math
import shutil
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'XLSX'}
DOWNLOAD_FOLDER = 'downloaded_files'
ALLOWED_EXTENSIONS_DOWNLOAD = {'xlsx', 'XLSX', 'pdf', 'PDF'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
data1 = None
data2 = None

def allowed_file_upload(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_file_download(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_DOWNLOAD

def process_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df

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
    <form action="/upload" method="post" enctype="multipart/form-data">
    <div class="tooltip" onclick="toggleTooltip()">?
            <span class="tooltiptext">Pentru a putea genera organigramele trebuie ca documentele încărcate (două excel-uri) să conțină: <br>Denumiri companii ordonate crescător după coloana "OU Company/Power Plant father":{ID obiect <br>Nume obiect<br>OU Company/Power Plant father<br>Desc. OU Company/Power Plant father-unitatea superioara}<br>Lista angajati:{DEN COMPANIE<br>COD DEPARTAMENT<br>DEN DEPARTAMENT<br>NUME<br>PRENUME<br>FUNCTIE<br>TIP ANGAJAT<br>DEN CATEGORIE PERSONAL}
    </span>
        
        </div>
        <label for="file-upload" class="button-intf"><strong><em>Încărcați fișierele necesare.</em></strong></label>
    <br>
                <input id="file-upload" type="file" name="file1" style="float: right;">
    <br><br>
        <input id="file-upload-2" type="file" name="file2" style="float: right;">


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

def replace_underscore_with_space(text):
    return text.replace('_', ' ')

@app.route('/upload', methods=['POST'])
def upload_file():

    # if 'file' not in request.files:
    #     return 'No file part'
    # files = request.files.getlist('file')
    # if len(files) != 2:
    #     return 'Please upload exactly two files.'

    # for i, file in enumerate(files):
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #         file.save(file_path)
    #         if i == 0:
    #             data1 = process_excel_file(file_path)
    #         else:
    #             data2 = process_excel_file(file_path)

    if 'file1' not in request.files or 'file2' not in request.files:
        return 'No file part', 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return 'No selected file', 400

    if allowed_file_upload(file1.filename) and allowed_file_upload(file2.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        
        filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
        
        file1.save(filepath1)
        file2.save(filepath2)
        
        # Procesează fișierele aici
        data2 = process_excel_file(filepath1)
        data1 = process_excel_file(filepath2)
    companies = request.form.getlist('comp[]')
    if not companies:
        return 'Please select at least one company.'
    # print(data1)
    # print(data2)
    # Aici poți adăuga logica pentru a genera organigramele bazate pe data1 și data2
    # și pentru companiile selectate.
    parents = data1['OU Company/Power Plant father'].tolist()
    children = data1['ID obiect'].tolist()
    graph = build_graph(parents, children)
    for company in companies:
        # parents = data2['OU Company/Power Plant father'].tolist()
        # children = data2['ID obiect'].tolist()
        # graph = build_graph(parents, children)
        # input_string = input("Introduceți denumirea companiei de start: ")
        company.replace('_',' ')
        int_string = company
        input_string=replace_underscore_with_space(int_string)
        print(input_string,end="\n")
        root=None
        for index, valoare in enumerate(data1['Desc. OU Company/Power Plant father-unitatea superioara']):
            if valoare == input_string:
                root=data1.iloc[index]['OU Company/Power Plant father']
        first=None
        for index, valoare in enumerate(data1['Desc. OU Company/Power Plant father-unitatea superioara']):
            if valoare == "Romania":
                first=data1.iloc[index]['OU Company/Power Plant father']
        
        # Verificați dacă s-a găsit un nod și afișați parcurgerile DFS și BFS
        if root is not None:
            
            hmax=print_graph_dfs(graph,root,first)
            node_levels = []
            level_order_traversal(graph,root,first,node_levels,math.floor(hmax/2))
            file_name="Organigrama "+str(input_string)+".pdf"
            generate_pdf(file_name,data2,data1,node_levels,hmax,graph,input_string,first)
            # if allowed_file_download(file1.filename) and allowed_file_download(file2.filename):
            #     file_name_path = os.path.join(app.config['DOWNLOAD_FOLDER'], file_name)
            #     file_name.save(file_name_path)
            # shutil.move(file_name,DOWNLOAD_FOLDER)
            # os.remove(file_name)

        else:
            print("Nodul introdus nu a fost găsit în graf.")

    # shutil.rmtree(UPLOAD_FOLDER)
        
        

    #STERGERE FOLDER UPLOADS 
    return 'Files uploaded and processed successfully. Companies selected: ' + ', '.join(companies)

if __name__ == "__main__":
    app.run(debug=True)
    


#managerii primii