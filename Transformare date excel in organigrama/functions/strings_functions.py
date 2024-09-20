import re


def compare_strings(str1, str2):
    clean_str1 = re.sub(r'[^a-zA-Z]', '', str1).lower()
    clean_str2 = re.sub(r'[^a-zA-Z]', '', str2).lower()
    return clean_str1 == clean_str2

def calc_pers(data1, n):
    nr = 0
    for val in data1["COD DEPARTAMENT"]:
        if val == n:
            nr += 1
    return nr

def afis_pers(data1,c,width,height,nt,x,y):
    for index3, j in enumerate(data1["COD DEPARTAMENT"]):
            if j==nt:
                s = str(data1.iloc[index3]['NUME']) + " " + str(data1.iloc[index3]['PRENUME']) + " " + str(data1.iloc[index3]['FUNCTIE']) + " " + str(data1.iloc[index3]['TIP ANGAJAT']) + " " + str(data1.iloc[index3]['DEN CATEGORIE PERSONAL'])
                R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                # Setează culoarea casetei folosind valorile convertite
                c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                c.rect(x, y, width, height, fill=True)
                c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                c.setFillColor("black")  # Setăm culoarea textului la negru
                c.drawString(x+5, y + height / 2, s)
                y=y-height

def spatiere(data1,n,node_levels):
    ok=1
    for j in node_levels:
        if j[2]==n or j[3]==n:
            ok=ok+1
            nr=calc_pers(data1,j[0])
            
            ok=ok+nr
    
    return ok

def numarare(data1, node, input_string_1, input_string_2):
    
    print("numararare",end="\n")
    nr = 0
    # Iterează direct prin valorile din cele trei coloane
    for index1, valoare in enumerate(data1['COD DEPARTAMENT']):
        if valoare==node and compare_strings(input_string_1,str(data1.iloc[index1]['DEN CATEGORIE PERSONAL'])) and compare_strings(input_string_2,str(data1.iloc[index1]['TIP ANGAJAT'])):
            nr += 1
    print("numararare final",end="\n")
    print(nr)
    return nr

