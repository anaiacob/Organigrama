import math
import numpy as np
from collections import deque
from reportlab.pdfgen import canvas
from .strings_functions import compare_strings, calc_pers, afis_pers, spatiere, numarare
from functions.graph_functions import count_children_except, centralizare, sum
import openpyxl
from .utils.recurent import last_day_of_current_month

def read_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data



def aflare_pozitie(i,vect_coord):
    for j in vect_coord:
        if j[0]==i:
            return j[1],j[2]
#calcularea coordonatelor
def calcLevelh(height,width,x,y, node_levels,h,vect_coord,w,c,children,v,data1,graph):
    nr=0
    k1,k2,k3=0,0,0
    y1,y2,y3=y,y,y
    cy1,cy2,cy3=0,0,0
    if children == 1:
        for n in node_levels:
            if n[2]==w:
                #recurent
                v.add(n)
                k1=calc_pers(data1,n[0])
                c.setLineWidth(1)
                c.setStrokeColor("black")
                #c.line(x+1.3*width,y1+height/2,x+1.5*width+10, y1+height/2)
                afis_pers(data1,c,width,height,n[0],x+1.3*width+10,y1-height)
                cy1=y1-height/2
                y1=y1-(k1+3)*height
                y1=y1-2*spatiere(data1,n[0],node_levels)*height
                
    elif children == 2:
        nr=0
        for n in node_levels:
            if n[2]==w:
                v.add(n)
                if nr%2==0:
                    k1=calc_pers(data1,n[0])
                    vect_coord.append((n[0],x,y1)) #-k1*height
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")
                    #c.line(x+600,y1+height/2,x+615,y1+height/2)
                    nr=nr+1
                    afis_pers(data1,c,width,height,n[0],x,y1-height)
                    cy1=y1-height/2
                    y1=y1-(k1+3)*height
                    y1=y1-2*spatiere(data1,n[0],node_levels)*height
                    
                else:
                    k2=calc_pers(data1,n[0])
                    
                    vect_coord.append((n[0],x+1.25*width,y2))#-k2*height
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")
                    #c.line(x+1.25*width-10,y2+height/2,x+1.25*width,y2+height/2)
                    nr=nr+1
                    afis_pers(data1,c,width,height,n[0],x+1.25*width,y2-height)
                    cy2=y2-height/2
                    y2=y2-(k2+3)*height
                    #y2=y2-count_children_except(data1,n[0],n[2])*height
                    y2=y2-spatiere(data1,n[0],node_levels)*height
                    
            # elif n[3]==w:
            #     #caut in vect_coord tatal
            #     for g in vect_coord:
            #         if g[0]==n[2]:
            #             kchild=calc_pers(data1,n[0])
            #             vect_coord.append(n[0],g[1]+0.04*width)
            #             break
    else:
        for n in node_levels:
            if n[2]==w:
                v.add(n)
                if nr%3==0:
                    k1=calc_pers(data1,n[0])
                    
                    vect_coord.append((n[0],x,y1)) #-k1*height
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")
                    c.line(x-15,y1+height/2,x,y1+height/2)
                    nr=nr+1
                    afis_pers(data1,c,width,height,n[0],x,y1-height)
                    cy1=y1-height/2
                    y1=y1-(k1+3)*height
                    y1=y1-2*spatiere(data1,n[0],node_levels)*height
                    
                    #mai tarziu conditie in cazul in care ies din pagina si nodurile de pe level h/2+1
                elif nr%3==1:
                    k2=calc_pers(data1,n[0])
                    vect_coord.append((n[0],x+1.25*width,y2))#-k2*height
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")
                    c.line(x+1.25*width-10,y2+height/2,x+1.25*width,y2+height/2)
                    nr=nr+1
                    afis_pers(data1,c,width,height,n[0],x+1.25*width,y2-height)
                    cy2=y2-height/2
                    y2=y2-(k2+3)*height
                    #y2=y2-count_children_except(data1,n[0],n[2])*height
                    y2=y2-spatiere(data1,n[0],node_levels)*height
                    
                    
                else:
                    k3=calc_pers(data1,n[0])
                    vect_coord.append((n[0],x+2.5*width,y3))#-k3*height
                    #y3=y3-count_children_except(graph,n[0],n[2])*height-height*2 
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")
                    c.line(x+2.5*width-15,y3+height/2,x+2.5*width,y3+height/2)
                    nr=nr+1
                    afis_pers(data1,c,width,height,n[0],x+2.5*width,y3-height)
                    cy3=y3-height/2
                    y3=y3-(k3+3)*height
                    y3=y3-spatiere(data1,n[0],node_levels)*height
            elif n[3]==w:
                break
                    
        c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
        c.setStrokeColor("black")
        if cy1 != 0:
            c.line(x-15,y+1.6*height,x-15,cy1+height)
        if cy2!=0:
            c.line(x+1.25*width-10,y+1.6*height,x+1.25*width-10,cy2+height)
        if cy3!=0:
            c.line(x+2.5*width-15,y+1.6*height,x+2.5*width-15,cy3+height)
    #AICI E GRESEALA CA NU PUNE CUM TREBUIE NU E CORECTA FUNCTIA nu le ordoneaza corect
    #ok=0

#afiseaza persoanele pe foaie 
def afisarePersoaneLevelh(height,width,x,y, node_levels,h,vect_coord,w,c,children,data1,graph):
    v=set()
    calcLevelh(height,width,x,y, node_levels,h,vect_coord,w,c,children,v,data1,graph)
    
    for i in v:
        if count_children_except(graph,i[0],i[2])!=0:
            l,p=aflare_pozitie(i[0],vect_coord)
            u=calc_pers(data1,i[0])
            c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
            c.setStrokeColor("black")
            p=p-(u+2)*height
            cp=p+2*height
            ok=1
            pok=0
            for j in node_levels: #AICI E PROBLEMA PENTRU DISTANTE SI ULTIMUL LEVEL TREBUIE REGANDITA !!!!!!
                if (j[1]>math.floor(h/2)+1 and j[1]<=h) and (j[2]==i[0] or j[3]==i[0]):
                    k=calc_pers(data1,j[0])
                    pok+=k
                    if p>height:
                        vect_coord.append((j[0],l+(j[1]-math.floor(h/2)+1)*0.02*width,p-height))#height*count_children_except(graph,j[0],j[2])-k*height#-height*count_children_except(graph,j[0],j[2])-height*2-k*height
                        afis_pers(data1,c,width,height,j[0],l+(j[1]-math.floor(h/2)+1)*0.02*width,p-2*height)
                        #schimba formula de calcul ca e gresita
                        ccp=p-height
                        if ok>2:
                            ok=1
                        p=p-height*(count_children_except(graph,j[0],j[2])+2*k+ok)#-(pok+1)*height#-(u+1)*height#-height*(u+1)-k*height
                        ok+=1
                        c.line(l+(j[1]-math.floor(h/2)+1)*0.02*width-10,ccp+height/2,l+(j[1]-math.floor(h/2)+1)*0.02*width,ccp+height/2)
                        c.line(l+(j[1]-math.floor(h/2)+1)*0.02*width-10,cp,l+(j[1]-math.floor(h/2)+1)*0.02*width-10,ccp+height/2)
                        
                        #p=p-height*(count_children_except(graph,j[0],j[2])-ok+1)-(pok+1)*height
        
def nr_spatii(node_levels,cautat):
    nr=0
    for n in node_levels:
        if n[2]==cautat or n[3]==cautat:
            nr=nr+1
    return nr



def desenare_centralizator(c,node_levels,data1,data2,input_string,q,graph,h,first):
    
    width1, width2, width3, width4= 1000, 600, 400, 100
    height1, height2 = 100, 50
    c.setFillColor("red")
    c.setFont("Helvetica", 15) 
    string1=str("Uz confidential")
    string2=str("Conform Politicii de Clasificare si Tratare a Informatiei nr. 59/31.03.2016")
    c.drawString(25,4950,string1)
    c.drawString(25,4900,string2)
    c.setFillColor("black")
    last_day_str = last_day_of_current_month()
    x,y=150,4800
    string3=str("PERSONALUL " + input_string + " " + last_day_str)
    c.setFont("Helvetica", 25)
    c.setFillColor("black")
    c.drawString(x+100,y,string3)
    #c.setFont("Helvetica", 15)
    c.setFillColor("black")
    y=y-150
    #E2DAD6
    R_hex = int('E2', 16)  # 'FB' este componenta roșie în hexazecimal
    G_hex = int('DA', 16)  # 'E0' este componenta verde în hexazecimal
    B_hex = int('D6', 16)  # '87' este componenta albastră în hexazecimal
                    # Setează culoarea casetei folosind valorile convertite
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x, y, width1, height1, fill=True)
    c.setFillColor("black")
    c.drawString(x + 50, y + height1/2, str("Denumire entitate"))
    y=y+height2
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1,y,width2,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+ width1 + 15, y + height2/2, str("NUMAR DE PERSONAL"))
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+width2,y,width2,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+width2+15,y+height2/2,"PERSONAL PART-TIME")
    c.setFont("Helvetica", 20)
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1,y-height2,width4,height2,fill=True) #copy it
    c.setFillColor("black")
    c.drawString(x+width1+ 10,y-height2+height2/2,"Cond I")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+width4+ 10,y-height2+height2/2,"Cond II")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+2*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+2*width4+ 10,y-height2+height2/2,"TESA")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+3*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+3*width4+ 10,y-height2+height2/2,"Maistri")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+4*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+4*width4+ 10,y-height2+height2/2,"Muncit")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+5*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+5*width4+ 10,y-height2+height2/2,"TOTAL")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+6*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+6*width4+ 10,y-height2+height2/2,"Cond I")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+7*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+7*width4+ 10,y-height2+height2/2,"Cond II")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+8*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+8*width4+ 10,y-height2+height2/2,"TESA")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+9*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+9*width4+ 10,y-height2+height2/2,"Maistri")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+10*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+10*width4+ 10,y-height2+height2/2,"Muncit")
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    c.rect(x+width1+11*width4,y-height2,width4,height2,fill=True)
    c.setFillColor("black")
    c.drawString(x+width1+11*width4+ 10,y-height2+height2/2,"TOTAL")
    y=y-height1
    R_hex = int('F5', 16)  # 'FB' este componenta roșie în hexazecimal
    G_hex = int('ED', 16)  # 'E0' este componenta verde în hexazecimal
    B_hex = int('ED', 16)  # '87' este componenta albastră în hexazecimal
                    # Setează culoarea casetei folosind valorile convertite
    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    
    nr=0
    parent=None
    for node in node_levels:
        if node[1]>1:
            nr=nr+1
        else:
            parent=node[0]
    copii=0
    level=2
    count=0
    vect_parc=[]
    node_parent=int(parent)
    print(first)
    # conds1, condpt1, conds2, condpt2, tesas, tesapt, muncitors, muncitorpt, maistris, maistript, totals, totalpt=0,0,0,0,0,0,0,0,0,0,0,0
    centralizare(data1,graph,node_parent ,first, vect_parc, h,)
    print(vect_parc,end='\n')
    s_conds1, s_condpt1, s_conds2, s_condpt2, s_tesas, s_tesapt, s_muncitors, s_muncitorpt, s_maistris, s_maistript, s_totals, s_totalpt = 0,0,0,0,0,0,0,0,0,0,0,0
    for node in vect_parc:
        if node[1]>1:
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            # print(node)
            c.rect(x,y-count*height2,width1,height2,fill=True)
            c.setFillColor("black")
            t=0
            for index, val in enumerate(data2['ID obiect']):
                        if val == node[0]:
                            t = index
                            break
            text1 = str(data2.iloc[t]['Nume obiect'])
            # print(text1)
            c.drawString(x+node[1]*30,y-count*height2+height2/2,text1)
            #s_conds1,s_conds2,s_tesas,s_maistris,s_muncitors,s_totals,s_condpt1,s_condpt2,s_tesapt,s_maistript,s_muncitorpt,s_totalpt=sum(vect_parc,s_conds1,s_conds2,s_tesas,s_maistris,s_muncitors,s_totals,s_condpt1,s_condpt2,s_tesapt,s_maistript,s_muncitorpt,s_totalpt,graph,node[0],first)
            # conds1=numarare(data1,node[0],node_levels,'Conducere1','Standard')
            # conds2=numarare(data1,node[0],node_levels,'Conducere2','Standard')
            # maistris=numarare(data1,node[0],node_levels,'Maistri','Standard')
            # tesas=numarare(data1,node[0],node_levels,'Tesa','Standard')
            # muncitors=numarare(data1,node[0],node_levels,'Muncitori','Standard')
            # condpt1=numarare(data1,node[0],node_levels,'Conducere1','Timp partial')
            # condpt2=numarare(data1,node[0],node_levels,'Conducere2','Timp partial')
            # tesapt=numarare(data1,node[0],node_levels,'Tesa','Timp partial')
            # muncitorpt=numarare(data1,node[0],node_levels,'Muncitori','Timp partial')
            # maistript=numarare(data1,node[0],node_levels,'Maistri','Timp partial')
            # s_condpt1=s_condpt1+condpt1
            # s_condpt2=s_condpt2+condpt2
            # s_tesapt=s_tesapt+tesapt
            # s_muncitorpt=s_muncitorpt+muncitorpt
            # s_maistrips=s_maistrips+maistript
            # s_totalpt=s_totalpt+condpt1+condpt2+tesapt+maistript+muncitorpt
            # s_totals=s_totals+conds1+conds2+tesas+maistris+muncitors
            # s_conds1=s_conds1+conds1
            # s_conds2=s_conds2+conds2
            # s_tesas=s_tesas+tesas
            # s_maistris=s_maistris+maistris
            # s_muncitors=s_muncitors+muncitors
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+0*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_conds1!=0:
                c.drawString(x+width1+0*width4+ 10,y-count*height2+height2/2,str(s_conds1))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+1*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_conds2!=0:
                c.drawString(x+width1+1*width4+ 10,y-count*height2+height2/2,str(s_conds2))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+2*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_tesas!=0:
                c.drawString(x+width1+2*width4+ 10,y-count*height2+height2/2,str(s_tesas))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+3*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_maistris!=0:
                c.drawString(x+width1+3*width4+ 10,y-count*height2+height2/2,str(s_maistris))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+4*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_muncitors!=0:
                c.drawString(x+width1+4*width4+ 10,y-count*height2+height2/2,str(s_muncitors))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+5*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            c.drawString(x+width1+5*width4+ 10,y-count*height2+height2/2,str(s_totals))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+6*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_condpt1!=0:
                c.drawString(x+width1+6*width4+ 10,y-count*height2+height2/2,str(s_condpt1))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+7*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_condpt2!=0:
                c.drawString(x+width1+7*width4+ 10,y-count*height2+height2/2,str(s_condpt2))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+8*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_tesapt!=0:
                c.drawString(x+width1+8*width4+ 10,y-count*height2+height2/2,str(s_tesapt))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+9*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_maistript!=0:
                c.drawString(x+width1+9*width4+ 10,y-count*height2+height2/2,str(s_maistript))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+10*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            if s_muncitorpt!=0:
                c.drawString(x+width1+10*width4+ 10,y-count*height2+height2/2,str(s_muncitorpt))
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
            c.rect(x+width1+11*width4,y-count*height2,width4,height2,fill=True)
            c.setFillColor("black")
            c.drawString(x+width1+11*width4+ 10,y-count*height2+height2/2,str(s_totalpt))
            count=count+1
            # # print(count)
            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
    
#     s_conds1=numarare(data1,node_parent,node_levels,'Conducere1','Standard')
#     s_conds2=numarare(data1,node_parent,node_levels,'Conducere2','Standard')
#     s_maistris=numarare(data1,node_parent,node_levels,'Maistri','Standard')
#     s_tesas=numarare(data1,node_parent,node_levels,'Tesa','Standard')
#     s_muncitors=numarare(data1,node_parent,node_levels,'Muncitori','Standard')
#     s_condpt1=numarare(data1,node_parent,node_levels,'Conducere1','Timp partial')
#     s_condpt2=numarare(data1,node_parent,node_levels,'Conducere2','Timp partial')
#     s_tesapt=numarare(data1,node_parent,node_levels,'Tesa','Timp partial')
#     s_muncitorpt=numarare(data1,node_parent,node_levels,'Muncitori','Timp partial')
#     s_maistrips=numarare(data1,node_parent,node_levels,'Maistri','Timp partial')
#     R_hex = int('BD', 16)  # 'FB' este componenta roșie în hexazecimal
#     G_hex = int('E8', 16)  # 'E0' este componenta verde în hexazecimal
#     B_hex = int('CA', 16)
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x,y-count*height2,width1,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+ 10,y-count*height2+height2/2,str("TOTAL "+input_string))

#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+0*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+0*width4+ 10,y-count*height2+height2/2,str(s_conds1))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+width4+ 10,y-count*height2+height2/2,str(s_conds2))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+2*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+2*width4+ 10,y-count*height2+height2/2,str(s_tesas))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+3*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+3*width4+ 10,y-count*height2+height2/2,str(s_maistris))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+4*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+4*width4+ 10,y-count*height2+height2/2,str(s_muncitors))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+5*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+5*width4+ 10,y-count*height2+height2/2,str(s_totals))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+6*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+6*width4+ 10,y-count*height2+height2/2,str(s_condpt1))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+7*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+7*width4+ 10,y-count*height2+height2/2,str(s_condpt2))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+8*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+8*width4+ 10,y-count*height2+height2/2,str(s_tesapt))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+9*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+9*width4+ 10,y-count*height2+height2/2,str(s_maistrips))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+10*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+10*width4+ 10,y-count*height2+height2/2,str(s_muncitorpt))
#     c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
#     c.rect(x+width1+11*width4,y-count*height2,width4,height2,fill=True)
#     c.setFillColor("black")
#     c.drawString(x+width1+11*width4+ 10,y-count*height2+height2/2,str(s_totalpt))
# # BDE8CA


def generate_pdf(file_name, data1, data2, node_levels,h,graph,input_string,first):
    # Creează un obiect canvas pentru a desena pe pagină
    custom_w=2500
    custom_h=5000#4250
    c = canvas.Canvas(file_name, pagesize=(custom_w,custom_h))#landscape(A3))
    q= deque()
    list_node =set()
    # Iterăm prin nodurile din node_levels
    i=1
        # Verificăm nivelul nodului
    while i<=math.floor(h/2):
        for node in node_levels:
            if node[1]==i:
                if node[1]<math.floor(h/2) and node[1]==1 and count_children_except(graph, node[0], node[2])!=0:
                    #list_node.add(node[0])
                    q.append(node[0])
                    c.setFillColor("red")
                    c.setFont("Helvetica", 15) 
                    string1=str("Uz confidential")
                    string2=str("Conform Politicii de Clasificare si Tratare a Informatiei nr. 59/31.03.2016")
                    c.drawString(25,4950,string1)
                    c.drawString(25,4900,string2)
                    c.setFillColor("black")
                    x, y = 800, 4800  # Coordonatele de început ale casetei
                    width, height = 610, 50  # Dimensiunile casetei
                    # Desenăm caseta colorată
                    # Convertiți componentele de culoare hexazecimale în valori întregi
                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                    # Setează culoarea casetei folosind valorile convertite
                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                    c.rect(x, y, width, height, fill=True)
                    # Adăugăm textul în casetă
                    t=0
                    for index,val in enumerate(data2['OU Company/Power Plant father']):
                        if val==node[0]:
                            t=index
                            break
                    if i==1:
                        text_admin="ADMINISTRATOR " + str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    else:
                        text_admin=str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    text_comp=str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    if text_comp!="nan":
                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                        c.setFillColor("black")  # Setăm culoarea textului la negru
                        c.drawString(x + 10, y + height/2, text_admin)
                        y=y-25
                    ok=0
                    for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                    #print(data1.columns)
                                    if valoare == node[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                        s = str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                        R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                        G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                        B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                        # Setează culoarea casetei folosind valorile convertite
                                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                        # Actualizează coordonata y pentru următoarea casetă
                                        if ok:
                                            y=y-height
                                        else:
                                            y=y-25
                                        # Desenează caseta colorată
                                        c.rect(x, y, width, height, fill=True)
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x+5, y + height / 2, s)
                                        ok=ok+1
                    if ok==0:
                        y=y+25
                    nr=0
                    xd, xs, ys, yd = 200, 1200, y-50, y-50
                    auxd,auxs=0,0
                    for n in node_levels:
                        if n[2]==node[0]:
                            #list_node.add(n[0])
                            q.append(n[0])
                            ys=ys-50
                            yd=yd-50
                            if nr % 2 == 0:
                                R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                # Setează culoarea casetei folosind valorile convertite
                                c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                c.rect(xd, yd, width, height, fill=True)
                                # Adăugăm textul în casetă
                                t = 0
                                for index, val in enumerate(data2['ID obiect']):
                                    if val == n[0]:
                                        t = index
                                        break
                                text1 = str(data2.iloc[t]['Nume obiect'])
                                if text1!="Romania":
                                    
                                    c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                    c.setFillColor("black")  # Setăm culoarea textului la negru
                                    c.drawString(xd + 40, yd + height / 2, text1)
                                    yd=yd-25
                                
                                ok=0
                                for index3, valoare in enumerate(data1['COD DEPARTAMENT']):
                                    if valoare == n[0] and compare_strings(text_comp,data1.iloc[index3]['DEN COMPANIE']):
                                        s = str(data1.iloc[index3]['NUME']) + " " + str(data1.iloc[index3]['PRENUME']) + " " + str(data1.iloc[index3]['FUNCTIE']) + " " + str(data1.iloc[index3]['TIP ANGAJAT']) + " " + str(data1.iloc[index3]['DEN CATEGORIE PERSONAL'])
                                        R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                        G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                        B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                        # Setează culoarea casetei folosind valorile convertite
                                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                        # Actualizează coordonata y pentru următoarea casetă
                                        if ok:
                                            yd=yd-height
                                        else:
                                            yd = yd - 25
                                        # Desenează caseta colorată
                                        c.rect(xd, yd, width, height, fill=True)
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(xd+5, yd + height / 2, s)
                                        ok=ok+1
                                auxd=ok
                                c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                c.setStrokeColor("black")
                                c.line(xd+width,yd+(auxd*height)+25,x+width/2,yd+(auxd*height)+25) 
                            else:
                                R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                # Setează culoarea casetei folosind valorile convertite
                                c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                
                                c.rect(xs, ys, width, height, fill=True)
                                # Adăugăm textul în casetă
                                t = 0
                                for index, val in enumerate(data2['ID obiect']):
                                    if val == n[0]:
                                        t = index
                                        break
                                text1 = str(data2.iloc[t]['Nume obiect'])
                                if text1!="Romania":
                                    
                                    c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                    c.setFillColor("black")  # Setăm culoarea textului la negru
                                    c.drawString(xs + 40, ys + height / 2, text1)
                                    ys=ys-25
                                ok=0
                                for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                    if valoare == n[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                        s=str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                        R_hex = int('54', 16)  #54BAB9 'FB' este componenta roșie în hexazecimal
                                        G_hex = int('BA', 16)  # 'E0' este componenta verde în hexazecimal
                                        B_hex = int('B9', 16)  # '87' este componenta albastră în hexazecimal
                                        # Setează culoarea casetei folosind valorile convertite
                                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                        if ok:
                                            ys=ys-height
                                        else:
                                            ys=ys-25
                                        c.rect(xs, ys, width, height, fill=True)
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(xs+5, ys + height / 2, s)
                                        ok=ok+1
                                auxs=ok
                                c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                c.setStrokeColor("black")
                                c.line(x+width/2,ys+(auxs*height)+25,xs,ys+(auxs*height)+25)
                            nr = nr + 1
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")  # Setează culoarea liniei la negru (opțional)
                    aux=0
                    if yd<ys:
                        y_1=yd
                        aux=auxd
                    else:
                        y_1=ys
                        aux=auxs
                    y_1=y_1+(aux*height)+height/2
                    c.line(x+width/2, y, x+width/2, y_1)
                    c.showPage()
                
                elif node[1]<math.floor(h/2) and node[1]!=1 and count_children_except(graph, node[0], node[2])!=0:
                    c.setFillColor("red")
                    c.setFont("Helvetica", 15) 
                    string1=str("Uz confidential")
                    string2=str("Conform Politicii de Clasificare si Tratare a Informatiei nr. 59/31.03.2016")
                    c.drawString(25,4950,string1)#570
                    c.drawString(25,4900,string2)#555
                    c.setFillColor("black")
                    x, y = 800, 4800  # Coordonatele de început ale casetei 315, 510
                    width, height = 610, 50  # Dimensiunile casetei
                    # Desenăm caseta colorată
                    # Convertiți componentele de culoare hexazecimale în valori întregi
                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                    # Setează culoarea casetei folosind valorile convertite
                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                    c.rect(x, y, width, height, fill=True)
                    # Adăugăm textul în casetă
                    t=0
                    for index,val in enumerate(data2['OU Company/Power Plant father']):
                        if val==node[0]:
                            t=index
                            break
                    if i==1:
                        text_admin="ADMINISTRATOR " + str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    else:
                        text_admin=str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    text_comp=str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    if text_comp!="nan":
                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                        c.setFillColor("black")  # Setăm culoarea textului la negru
                        c.drawString(x + 10, y + height/2, text_admin)
                        y=y-25
                    ok=0
                    for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                    if valoare == node[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                        s = str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                        R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                        G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                        B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                        # Setează culoarea casetei folosind valorile convertite
                                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                        # Actualizează coordonata y pentru următoarea casetă
                                        if ok:
                                            y=y-height
                                        else:
                                            y=y-25
                                        # Desenează caseta colorată
                                        c.rect(x, y, width, height, fill=True)
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x+5, y + height / 2, s)
                                        ok=ok+1
                    if ok==0:
                        y=y+25
                    nr=0
                    #xd, xs, ys, yd = 50, 520, y-20, y-20
                    if count_children_except(graph,node[0],node[2])==1:
                        x1,y1=x,y-100
                        R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                        G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                        B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                        # Setează culoarea casetei folosind valorile convertite
                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                        c.rect(x1, y1, width1, height, fill=True)
                                # Adăugăm textul în casetă
                        t = 0
                        for index, val in enumerate(data2['ID obiect']):
                            if val == n[0]:
                                t = index
                                break
                        text1 = str(data2.iloc[t]['Nume obiect'])
                        for n in node_levels:
                            if n[2]==node[0]:
                                #list_node.add(n[0])
                                q.append(n[0])
                        if text1!="Romania":
                            
                            c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                            c.setFillColor("black")  # Setăm culoarea textului la negru
                            c.drawString(x1 + 4, y1 + height / 2, text1)
                        y1=y1-25
                        c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                        c.setStrokeColor("black")
                        c.line(x1,y1+25+height/2,x1-25,y1+25+height/2)
                        ok=0
                        for index3, valoare in enumerate(data1['COD DEPARTAMENT']):
                            if valoare == n[0] and compare_strings(text_comp,data1.iloc[index3]['DEN COMPANIE']):
                                        s = str(data1.iloc[index3]['NUME']) + " " + str(data1.iloc[index3]['PRENUME']) + " " + str(data1.iloc[index3]['FUNCTIE']) + " " + str(data1.iloc[index3]['TIP ANGAJAT']) + " " + str(data1.iloc[index3]['DEN CATEGORIE PERSONAL'])
                                        R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                        G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                        B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                        # Setează culoarea casetei folosind valorile convertite
                                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                        # Actualizează coordonata y pentru următoarea casetă
                                        if ok:
                                            y1=y1-height
                                        else:
                                            y1 = y1 - 25
                                        # Desenează caseta colorată
                                        c.rect(x1, y1, width, height, fill=True)
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x1+5, y1 + height / 2, s)
                                        ok=ok+1
                    elif count_children_except(graph,node[0],node[2])==2:
                        xd, xs, ys, yd = 200, 1200, y-50, y-50
                        auxd,auxs=0,0
                        for n in node_levels:
                            if n[2]==node[0]:
                                #list_node.add(n[0])
                                q.append(n[0])
                                ys=ys-50
                                yd=yd-50
                                if nr % 2 == 0:
                                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                    # Setează culoarea casetei folosind valorile convertite
                                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                    c.rect(xd, yd, width, height, fill=True)
                                    # Adăugăm textul în casetă
                                    t = 0
                                    for index, val in enumerate(data2['ID obiect']):
                                        if val == n[0]:
                                            t = index
                                            break
                                    text1 = str(data2.iloc[t]['Nume obiect'])
                                    if text1!="Romania":
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(xd + 40, yd + height / 2, text1)
                                        yd=yd-25
                                    
                                    ok=0
                                    for index3, valoare in enumerate(data1['COD DEPARTAMENT']):
                                        if valoare == n[0] and compare_strings(text_comp,data1.iloc[index3]['DEN COMPANIE']):
                                            s = str(data1.iloc[index3]['NUME']) + " " + str(data1.iloc[index3]['PRENUME']) + " " + str(data1.iloc[index3]['FUNCTIE']) + " " + str(data1.iloc[index3]['TIP ANGAJAT']) + " " + str(data1.iloc[index3]['DEN CATEGORIE PERSONAL'])
                                            R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                            G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                            B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                            # Setează culoarea casetei folosind valorile convertite
                                            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                            # Actualizează coordonata y pentru următoarea casetă
                                            if ok:
                                                yd=yd-height
                                            else:
                                                yd = yd - 25
                                            # Desenează caseta colorată
                                            c.rect(xd, yd, width, height, fill=True)
                                            c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                            c.setFillColor("black")  # Setăm culoarea textului la negru
                                            c.drawString(xd+5, yd + height / 2, s)
                                            ok=ok+1
                                    auxd=ok
                                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                    c.setStrokeColor("black")
                                    c.line(xd+width,yd+(auxd*height)+25,x+width/2,yd+(auxd*height)+25) 
                                else:
                                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                    # Setează culoarea casetei folosind valorile convertite
                                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                    
                                    c.rect(xs, ys, width, height, fill=True)
                                    # Adăugăm textul în casetă
                                    t = 0
                                    for index, val in enumerate(data2['ID obiect']):
                                        if val == n[0]:
                                            t = index
                                            break
                                    text1 = str(data2.iloc[t]['Nume obiect'])
                                    if text1!="Romania":
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(xs + 40, ys + height / 2, text1)
                                        ys=ys-25
                                    ok=0
                                    for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                        if valoare == n[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                            s=str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                            R_hex = int('54', 16)  #54BAB9 'FB' este componenta roșie în hexazecimal
                                            G_hex = int('BA', 16)  # 'E0' este componenta verde în hexazecimal
                                            B_hex = int('B9', 16)  # '87' este componenta albastră în hexazecimal
                                            # Setează culoarea casetei folosind valorile convertite
                                            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                            if ok:
                                                ys=ys-height
                                            else:
                                                ys=ys-25
                                            c.rect(xs, ys, width, height, fill=True)
                                            c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                            c.setFillColor("black")  # Setăm culoarea textului la negru
                                            c.drawString(xs+5, ys + height / 2, s)
                                            ok=ok+1
                                    auxs=ok
                                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                    c.setStrokeColor("black")
                                    c.line(x+width/2,ys+(auxs*height)+25,xs,ys+(auxs*height)+25)
                                nr = nr + 1
                        c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                        c.setStrokeColor("black")  # Setează culoarea liniei la negru (opțional)
                        aux=0
                        if yd<ys:
                            y_1=yd
                            aux=auxd
                        else:
                            y_1=ys
                            aux=auxs
                        y_1=y_1+(aux*height)+height/2
                        c.line(x+width/2, y, x+width/2, y_1)
                    else:
                        x1,x2,x3=100,100+1.25*width,100+2.5*width #50 290 550
                        l=y-100
                        y1,y2,y3=l,l,l
                        #auxd,auxs=0,0
                        aux1,aux2,aux3=0,0,0
                        width1=610 #220
                        for n in node_levels:
                            if n[2]==node[0]:
                                #list_node.add(n[0])
                                q.append(n[0])
                                if nr>=3:
                                    if nr%3 == 0:
                                        y1=y1-50
                                    elif nr%3 == 1:
                                        y2=y2-50
                                    else:
                                        y3=y3-50
                                if nr % 3 == 0:
                                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                    # Setează culoarea casetei folosind valorile convertite
                                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                    c.rect(x1, y1, width1, height, fill=True)
                                    # Adăugăm textul în casetă
                                    t = 0
                                    for index, val in enumerate(data2['ID obiect']):
                                        if val == n[0]:
                                            t = index
                                            break
                                    text1 = str(data2.iloc[t]['Nume obiect'])
                                    if text1!="Romania":
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x1 + 4, y1 + height / 2, text1)
                                        y1=y1-25
                                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                    c.setStrokeColor("black")
                                    c.line(x1,y1+25+height/2,x1-25,y1+25+height/2)
                                    ok=0
                                    for index3, valoare in enumerate(data1['COD DEPARTAMENT']):
                                        if valoare == n[0] and compare_strings(text_comp,data1.iloc[index3]['DEN COMPANIE']):
                                            s = str(data1.iloc[index3]['NUME']) + " " + str(data1.iloc[index3]['PRENUME']) + " " + str(data1.iloc[index3]['FUNCTIE']) + " " + str(data1.iloc[index3]['TIP ANGAJAT']) + " " + str(data1.iloc[index3]['DEN CATEGORIE PERSONAL'])
                                            R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                            G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                            B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                            # Setează culoarea casetei folosind valorile convertite
                                            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                            # Actualizează coordonata y pentru următoarea casetă
                                            if ok:
                                                y1=y1-height
                                            else:
                                                y1 = y1 - 25
                                            # Desenează caseta colorată
                                            c.rect(x1, y1, width, height, fill=True)
                                            c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                            c.setFillColor("black")  # Setăm culoarea textului la negru
                                            c.drawString(x1+5, y1 + height / 2, s)
                                            ok=ok+1
                                    aux1=ok
                                elif nr%3==1:
                                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                    # Setează culoarea casetei folosind valorile convertite
                                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                    
                                    c.rect(x2, y2, width1, height, fill=True)
                                    # Adăugăm textul în casetă
                                    t = 0
                                    for index, val in enumerate(data2['ID obiect']):
                                        if val == n[0]:
                                            t = index
                                            break
                                    text1 = str(data2.iloc[t]['Nume obiect'])
                                    if text1!="Romania":
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x2 + 4, y2 + height / 2, text1)
                                        y2=y2-25
                                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                    c.setStrokeColor("black")
                                    c.line(x3-50,y2+25+height/2,100+2.25*width,y2+25+height/2)
                                    ok=0
                                    for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                        if valoare == n[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                            s=str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                            R_hex = int('54', 16)  #54BAB9 'FB' este componenta roșie în hexazecimal
                                            G_hex = int('BA', 16)  # 'E0' este componenta verde în hexazecimal
                                            B_hex = int('B9', 16)  # '87' este componenta albastră în hexazecimal
                                            # Setează culoarea casetei folosind valorile convertite
                                            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                            if ok:
                                                y2=y2-height
                                            else:
                                                y2=y2-25
                                            c.rect(x2, y2, width1, height, fill=True)
                                            c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                            c.setFillColor("black")  # Setăm culoarea textului la negru
                                            c.drawString(x2+5, y2 + height / 2, s)
                                            ok=ok+1
                                    aux2=ok
                                    
                                else:
                                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                                    # Setează culoarea casetei folosind valorile convertite
                                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                    
                                    c.rect(x3, y3, width1, height, fill=True)
                                    # Adăugăm textul în casetă
                                    t = 0
                                    for index, val in enumerate(data2['ID obiect']):
                                        if val == n[0]:
                                            t = index
                                            break
                                    text1 = str(data2.iloc[t]['Nume obiect'])
                                    if text1!="Romania":
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x3 + 4, y3 + height / 2, text1)
                                        y3=y3-25
                                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                                    c.setStrokeColor("black")
                                    c.line(x3-50,y3+25+height/2,x3,y3+25+height/2)
                                    ok=0
                                    for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                        if valoare == n[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                            s=str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                            R_hex = int('54', 16)  #54BAB9 'FB' este componenta roșie în hexazecimal
                                            G_hex = int('BA', 16)  # 'E0' este componenta verde în hexazecimal
                                            B_hex = int('B9', 16)  # '87' este componenta albastră în hexazecimal
                                            # Setează culoarea casetei folosind valorile convertite
                                            c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                            if ok:
                                                y3=y3-height
                                            else:
                                                y3=y3-25
                                            c.rect(x3, y3, width1, height, fill=True)
                                            c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                            c.setFillColor("black")  # Setăm culoarea textului la negru
                                            c.drawString(x3+5, y3 + height / 2, s)
                                            ok=ok+1
                                    aux3=ok
                                    
                                nr = nr + 1
                        c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                        c.setStrokeColor("black")  # Setează culoarea liniei la negru (opțional)
                        '''aux=0
                        if yd<ys:
                            y_1=yd
                            aux=auxd
                        else:
                            y_1=ys
                            aux=auxs
                        y_1=y_1+(aux*height)+height/2
                        c.line(x+width/2, y, x+width/2, y_1)'''
                        #y2=y2+30
                        #y3=y3+30
                        c.line(x+width/2,y,x+width/2,y-15)
                        c.line(x1-25,y-15,x3-50,y-15)
                        c.line(x1-25,y-15,x1-25,y1+(aux1*height)+height)
                        auxline=0
                        if y2<y3:
                            yline=y3
                            auxline=aux3
                        else:
                            yline=y2
                            auxline=aux2
                        c.line(x3-50,y-15,x3-50,yline+(auxline*height)+height)
                    c.showPage()
                #mai trebuie lucrat la afisari si la liniile din pdf
                elif node[1]==math.floor(h/2) and node[1]!=1 and count_children_except(graph, node[0], node[2])!=0:
                    c.setFillColor("red")
                    c.setFont("Helvetica", 15) 
                    string1=str("Uz confidential")
                    string2=str("Conform Politicii de Clasificare si Tratare a Informatiei nr. 59/31.03.2016")
                    c.drawString(25,4950,string1)
                    c.drawString(25,4900,string2)
                    c.setFillColor("black")
                    x, y = 800, 4800  # Coordonatele de început ale casetei
                    width, height = 610, 50  # Dimensiunile casetei
                    # Desenăm caseta colorată
                    # Convertiți componentele de culoare hexazecimale în valori întregi
                    R_hex = int('FB', 16)  # 'FB' este componenta roșie în hexazecimal
                    G_hex = int('E0', 16)  # 'E0' este componenta verde în hexazecimal
                    B_hex = int('87', 16)  # '87' este componenta albastră în hexazecimal
                    # Setează culoarea casetei folosind valorile convertite
                    c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                    c.rect(x, y, width, height, fill=True)
                    # Adăugăm textul în casetă
                    t=0
                    for index,val in enumerate(data2['OU Company/Power Plant father']):
                        if val==node[0]:
                            t=index
                            break
                    if i==1:
                        text_admin="ADMINISTRATOR " + str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    else:
                        text_admin=str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    text_comp=str(data2.iloc[t]['Desc. OU Company/Power Plant father-unitatea superioara'])
                    if text_comp!="nan":
                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                        c.setFillColor("black")  # Setăm culoarea textului la negru
                        c.drawString(x + 10, y + height/2, text_admin)
                        y=y-25
                    ok=0
                    for index2, valoare in enumerate(data1['COD DEPARTAMENT']):
                                    if valoare == node[0] and compare_strings(text_comp,data1.iloc[index2]['DEN COMPANIE']):
                                        s = str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                        R_hex = int('54', 16)  # '54' este componenta roșie în hexazecimal
                                        G_hex = int('BA', 16)  # 'BA' este componenta verde în hexazecimal
                                        B_hex = int('B9', 16)  # 'B9' este componenta albastră în hexazecimal
                                        # Setează culoarea casetei folosind valorile convertite 
                                        c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                        # Actualizează coordonata y pentru următoarea casetă
                                        if ok:
                                            y=y-height
                                        else:
                                            y=y-25
                                        # Desenează caseta colorată
                                        c.rect(x, y, width, height, fill=True)
                                        c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                        c.setFillColor("black")  # Setăm culoarea textului la negru
                                        c.drawString(x+5, y + height / 2, s)
                                        ok=ok+1
                    children=count_children_except(graph, node[0], node[2])
                    vect_coord=[]
                    if ok==0:
                        y=y+25
                    xcoord=50
                    ycoord=y-100
                    afisarePersoaneLevelh(height,width,xcoord,ycoord, node_levels,h,vect_coord,node[0],c,children,data1,graph)
                    c.setLineWidth(1)  # Setează grosimea liniei la 1 (opțional)
                    c.setStrokeColor("black")
                    c.line(x+width/2,y,x+width/2,y-20)
                    if children ==1:
                        c.line(x+width/2,y-20,x+width/2,ycoord)
                    elif children == 2:
                        c.line(xcoord+width/2,y-20,x+width/2,y-20)
                        c.line(xcoord+width/2,y-20,xcoord+width/2,ycoord)
                        c.line(x+width/2,y-20,x+width/2,ycoord)
                    else:
                    #c.line(x+width/2,y,x+width/2,y-20)
                        c.line(xcoord-15,y-20,xcoord+2.5*width-15,y-20)
                    for o in vect_coord:
                        #print(o)
                        for ind, value in enumerate(data2['ID obiect']):
                            if value==o[0]:
                                #list_node.add(o[0])
                                q.append(o[0])
                                s=str(data2.iloc[ind]["Nume obiect"])
                                #s = str(data1.iloc[index2]['NUME']) + " " + str(data1.iloc[index2]['PRENUME']) + " " + str(data1.iloc[index2]['FUNCTIE']) + " " + str(data1.iloc[index2]['TIP ANGAJAT']) + " " + str(data1.iloc[index2]['DEN CATEGORIE PERSONAL'])
                                R_hex = int('5B', 16)  # '54' este componenta roșie în hexazecimal
                                G_hex = int('BC', 16)  # 'BA' este componenta verde în hexazecimal
                                B_hex = int('FF', 16)  # 'B9' este componenta albastră în hexazecimal
                                # Setează culoarea casetei folosind valorile convertite 5BBCFF
                                c.setFillColorRGB(R_hex / 255, G_hex / 255, B_hex / 255)
                                c.rect(o[1], o[2], width, height, fill=True)
                                c.setFont("Helvetica", 15)  # Setăm fontul și dimensiunea textului
                                c.setFillColor("black")  # Setăm culoarea textului la negru
                                c.drawString(o[1]+5, o[2] + height / 2, s)
                                
                    c.showPage()
                    
        i=i+1
    desenare_centralizator(c,node_levels,data1,data2,input_string,q,graph,h,first)
    # print("OK",end="\n")
    # print(q)
    
    # Salvează fișierul PDF
    c.save()
    
