from ..strings_functions import afis_pers
from ..strings_functions import calc_pers
from ..strings_functions import spatiere
from datetime import datetime, timedelta
def casete(data1,c,width,height,n,x,y,v,node_levels,nr,k):
    v.add(n)
    k=calc_pers(data1,n[0])
    c.setLineWidth(1)
    c.setStrokeColor("black")
                #c.line(x+1.3*width,y1+height/2,x+1.5*width+10, y1+height/2)
    afis_pers(data1,c,width,height,n[0],x+1.3*width+10,y-height)
    cy1=y-height/2
    y=y-(k+3)*height
    y=y-2*spatiere(data1,n[0],node_levels)*height
    print("y1= ")
    print(y,end="\n")
    nr=nr+1

def last_day_of_current_month():
    # Obține data curentă de pe computer
    today = datetime.today()
    year = today.year
    month = today.month

    # Determină prima zi a lunii următoare
    if month == 12:
        next_month = 1
        next_month_year = year + 1
    else:
        next_month = month + 1
        next_month_year = year
    
    first_day_of_next_month = datetime(next_month_year, next_month, 1)

    # Scade o zi pentru a obține ultima zi a lunii curente
    last_day = first_day_of_next_month - timedelta(days=1)

    # Returnează data în formatul "dd.mm.yyyy"
    return last_day.strftime("%d.%m.%Y")


