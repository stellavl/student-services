import PySimpleGUI as sg
import sqlite3


def main_window():
    layout = [[sg.Text("Choose user:", key="-user-")],
              [sg.Button("Φοιτητής",key="-foititis-"),
               sg.Button("Καθηγητής", key="-kathigitis-"),
               sg.Button("Γραμματεία", key="-grammateia-")],
              [sg.Button("Exit", key="-exit-")]]
    windowmain = sg.Window("Χρήστης",layout)
    while True:
        event, values = windowmain.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-foititis-":
            user=1
            kodikos_foititi(user)
        if event == "-kathigitis-":
            user=2
            kodikos_kathigiti(user)
        if event == "-grammateia-":
            user=3
            window_prosopikou(user)
    windowmain.close()

def window_foititi(am,user):
    flag=0
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''select "Αριθμός Μητρώου" from ΦΟΙΤΗΤΗΣ''')
    data=c.fetchall()
    conn.close()
    #check if AM is in database
    for i in range(len(data)):
        if am==data[i]:
            flag=1
            break
    if flag!=1:
        print("Couldn't log in student")
        kodikos_foititi(user)
    else:
        layout = [[sg.Button("Προσωπικά Στοιχεία", key="-stoixeia-")],
                  [sg.Button("Καθηγητές", key="-kathigites-")],
                  [sg.Button("Διδασκαλίες", key="-didaskalies-")],
                  [sg.Button("Μαθήματα", key="-mathimata-")],
                  [sg.Button("Κατευθύνσεις", key="-kateythinseis-")],
                  [sg.Button("Βαθμολογίες", key="-vathmologies-")],
                  [sg.Button("Exit", key="-exit-")]]           
        windowfoititi = sg.Window("Φοιτητής", layout, size=(250, 250))
        while True:
            event, values = windowfoititi.read()
            if event == "-exit-" or event == sg.WIN_CLOSED:
                break
            if event == "-stoixeia-":
                foititis(am, user)
            if event == "-kathigites-":
                kathigites(user,0)
            if event == "-didaskalies-":
                didaskalies(user)
            if event == "-mathimata-":
                mathimata(user)
            if event == "-kateythinseis-":
                kateythinseis(user)
            if event == "-vathmologies-":
                vathmologies(user)
        windowfoititi.close()       

def kodikos_foititi(user):
    layout = [[sg.Text("Insert Αριθμό Μητρώου", key="-insert-")],
               [sg.InputText(key='-AM-')],
               [sg.Submit(), sg.Cancel(key='-cancel-')]]
    windowfoititi =  sg.Window("Φοιτητής",layout)
    event, values = windowfoititi.read()
    try:
        am=tuple([int(values["-AM-"])])
    except: #if input is not integer
        if not event=='-cancel-':
            print("Couldn't log in student")
        windowfoititi.close()
    else:
        windowfoititi.close()
        if not event=='-cancel-':
            window_foititi(am,user)
        

def window_kathigiti(user,ID):
    flag=0
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''select "ID" from ΚΑΘΗΓΗΤΗΣ''')
    data=c.fetchall()
    conn.close()
    for i in range(len(data)):
        if ID==data[i]:
            flag=1
            break
    if flag!=1:
        print("Couldn't log in teacher")
        kodikos_kathigiti(user)
    else:
        layout = [[sg.Button("Προσωπικά Στοιχεία", key="-proswpikastoixeiakathigiti-")],
                  [sg.Button("Διδασκαλίες", key="-didaskalies-")],
                  [sg.Button("Βαθμολογίες", key="-vathmologies-")],
                  [sg.Button("Exit", key="-exit-")]]           
        windowkathigiti = sg.Window("Καθηγητής", layout)
        while True:
            event, values = windowkathigiti.read()
            if event == "-exit-" or event == sg.WIN_CLOSED:
                break
            if event == "-proswpikastoixeiakathigiti-":
                kathigites(user,ID)
            if event == "-didaskalies-":
                didaskalies(user)
            if event == "-vathmologies-":
                vathmologies(user)
        windowkathigiti.close()


def kodikos_kathigiti(user):
    layout = [[sg.Text('Insert ID'), sg.InputText(key='-kwdikoskathigiti-')],
              [sg.Submit(), sg.Cancel(key='-cancel-')]]           
    windowkodikoskathigiti = sg.Window("Κωδικός Καθηγητή", layout)
    event, values = windowkodikoskathigiti.read()
    try:
        ID=tuple([int(values['-kwdikoskathigiti-'])])
    except:
        if not event=='-cancel-':
            print("Couldn't log in teacher")
        windowkodikoskathigiti.close()
    else:
        windowkodikoskathigiti.close()
        if not event=='-cancel-':
            window_kathigiti(user,ID)

    
def window_prosopikou(user):
    layout = [[sg.Button("Φοιτητές", key="-foitites-")],
              [sg.Button("Καθηγητές", key="-kathigites-")],
              [sg.Button("Διδασκαλίες", key="-didaskalies-")],
              [sg.Button("Μαθήματα", key="-mathimata-")],
              [sg.Button("Κατευθύνσεις", key="-kateythinseis-")],
              [sg.Button("Βαθμολογίες", key="-vathmologies-")],
              [sg.Button("Exit", key="-exit-")]]           
    windowprosopikou = sg.Window("Προσωπικό", layout, size=(250, 250))
    while True:
        event, values = windowprosopikou.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-foitites-":
            foitites_monoAM(user)
        if event == "-kathigites-":
            kathigites(user,0)
        if event == "-didaskalies-":
            didaskalies(user)
        if event == "-mathimata-":
            mathimata(user)
        if event == "-kateythinseis-":
            kateythinseis(user)
        if event == "-vathmologies-":
            vathmologies(user)
    windowprosopikou.close()


def foitites_monoAM(user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''select "Αριθμός Μητρώου" from ΦΟΙΤΗΤΗΣ''')
    data=c.fetchall()
    layout=[[sg.Listbox(values=data, key="-data-",size=(30,10),enable_events=True)],
            [sg.Button("Insert", key="-insert_foititi-"), sg.Button("Exit", key="-exit-")]]
    windowfoitites = sg.Window("Αριθμοί Μητρώου Φοιτητών", layout)
    while True:
        event, values = windowfoitites.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-insert_foititi-":
            insertfoititi()
        if event == "-data-":
            am_tuple=(values["-data-"][0])
            foititis(am_tuple, user)
    windowfoitites.close()
    conn.close()

    
def foititis(am, user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''select * from ΦΟΙΤΗΤΗΣ where "Αριθμός Μητρώου"=(?)''',am)
    data=c.fetchall()
    c=[]
    d=[]
    for i in range(len(data)):
        a=str(data[i])
        for j in range(len(data[0])):
            d.append(data[i][j])
            c.append(d[j])    
    data=[c]
    headings = ["ΑΜ", "Ονοματεπώνυμο", "Κινητό", "Σταθερό", "Ημ. Γέννησης" ,
                "Email", "Χώρα", "Περιοχή", "Πόλη", "Οδός", "Αριθμός",
                "ΤΚ", "Εξ. Φοίτησης", "Κατεύθυνση"]
    if user==3:
        layout = [[sg.Table(values=data, headings=headings,
                            max_col_width=15,
                            auto_size_columns=True,
                            hide_vertical_scroll = True,
                            justification='center',
                            num_rows=1,
                            key='-TABLE-',
                            enable_events=True,
                            enable_click_events=True)],
                  [sg.Button("Edit", key="-edit_foititi-"),
                  sg.Button("Delete",key="-delete_foititi-"),
                  sg.Button("Exit", key="-exit-")]]
    elif user==1:
        layout = [[sg.Table(values=data, headings=headings,
                            max_col_width=15,
                            auto_size_columns=True,
                            hide_vertical_scroll = True,
                            justification='center',
                            num_rows=1,
                            key='-TABLE-',
                            enable_events=True,
                            enable_click_events=True)],
                  [sg.Button("Exit", key="-exit-")]]       
    windowfoitites = sg.Window("Φοιτητής", layout)
    while True:
        event, values = windowfoitites.read()   
        if event == sg.WIN_CLOSED:
            break
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-edit_foititi-":
             edit_foititi(am)
        if event == "-delete_foititi-":
            conn=sqlite3.connect("student_services.db")
            c=conn.cursor()
            c.execute('''DELETE FROM ΦΟΙΤΗΤΗΣ WHERE "Αριθμός Μητρώου"=(?)''',am)
            data=c.fetchall()
            conn.close()
            break
    conn.close()
    windowfoitites.close()
    

def kathigites(user,ID):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    if user==1: #user=foititis
        c.execute('''select "Ονοματεπώνυμο", "Βαθμίδα" from ΚΑΘΗΓΗΤΗΣ order by "Ονοματεπώνυμο"''')
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            a=str(data[i])
            c.append([data[i][0],data[i][1]])
        headings = ["Ονοματεπώνυμο", "Βαθμίδα"]
    elif user==2: #user=kathigitis
        c.execute('''select * from ΚΑΘΗΓΗΤΗΣ where "ID"=?''',ID)
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            a=str(data[i])
            c.append([data[i][0],data[i][1],data[i][2]])
        headings = ["ID","Ονοματεπώνυμο", "Βαθμίδα"]        
    elif user==3: #user=grammateia
        c.execute('''select * from ΚΑΘΗΓΗΤΗΣ order by "Ονοματεπώνυμο"''')
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            a=str(data[i])
            c.append([data[i][0],data[i][1],data[i][2]])
        headings = ["ID","Ονοματεπώνυμο", "Βαθμίδα"]
    data=c
    conn.close()
    layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
    windowkathigites = sg.Window("Καθηγητές", layout)
    m=0
    while True:
        event, values = windowkathigites.read()
        try:
            if m==0:
                print("Συντεταγμένες: ", event[2])
                syntetagmenes=event[2]
                m=1
            else:
                syntetagmenes=0
                m=0
            if syntetagmenes[1]==0:
                print("επέλεξες το ID")
            if syntetagmenes[0]==0:
                print("1η σειρά")
        except:
            None
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
    windowkathigites.close()


def didaskalies(user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''SELECT DISTINCT "Έτος Διδασκαλίας" FROM ΔΙΔΑΣΚΑΛΙΑ''')
    data=c.fetchall()
    layout=[[sg.Listbox(values=data, key="-data-",size=(50,5),enable_events=True)],[sg.Button("Exit", key="-exit-")]]
    windowdidaskalies = sg.Window("Διδασκαλίες", layout)
    while True:
        event, values = windowdidaskalies.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-data-":
            etos=(values["-data-"][0])
            window_didaskalias(etos)
    windowdidaskalies.close()
    conn.close()


def window_didaskalias(etos):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''SELECT DISTINCT "Όνομα", ΜΑΘΗΜΑ."Κωδικός"
                 FROM ΔΙΔΑΣΚΑΛΙΑ, ΜΑΘΗΜΑ
                 WHERE ΔΙΔΑΣΚΑΛΙΑ."Κωδικός Μαθήματος"=ΜΑΘΗΜΑ."Κωδικός" AND ΔΙΔΑΣΚΑΛΙΑ."Έτος Διδασκαλίας"=(?)
                 ORDER BY "Όνομα";''',etos)
    data=c.fetchall()
    c=[]
    for i in range(len(data)):
        a=str(data[i])
        c.append([data[i][0],data[i][1]])
    data=c
    headings = ["Όνομα", "Κωδικός Μαθήματος"]
    layout = [[sg.Table(values=data, headings=headings,
                        justification='left',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
    windowdidaskalies = sg.Window("Μαθήματα που διδάχθηκαν", layout)
    m=0
    while True:
        event, values = windowdidaskalies.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
    windowdidaskalies.close()
    conn.close()

def mathimata(user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''select * from ΜΑΘΗΜΑ order by "Εξάμηνο Διδασκαλίας" ''')
    data=c.fetchall()
    c=[]
    for i in range(len(data)):
        a=str(data[i])
        c.append([data[i][0],data[i][1],data[i][2]])
    data=c
    headings = ["Κωδικός", "Όνομα", "Εξάμηνο Διδασκαλίας"]
    layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
    windowmathimata = sg.Window("Μαθήματα", layout)
    m=0
    while True:
        event, values = windowmathimata.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break  
    windowmathimata.close()
    conn.close()

def kateythinseis(user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute("select * from ΚΑΤΕΥΘΥΝΣΗ")
    data=c.fetchall()
    c=[]
    for i in range(len(data)):
        a=str(data[i])
        c.append([data[i][0]])
    data=c
    headings = ["Όνομα"]
    layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=5,
                        max_col_width=30,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
    m=0
    windowkateythinseis = sg.Window("Κατευθύνσεις", layout)
    while True:
        event, values = windowkateythinseis.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break    
    windowkateythinseis.close()
    conn.close()

def vathmologies(user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute("select * from ΒΑΘΜΟΛΟΓΙΑ")
    data=c.fetchall()
    c=[]
    for i in range(len(data)):
        a=str(data[i])
        c.append([data[i][0],data[i][1],data[i][2],data[i][3]])
    data=c
    headings = ["Βαθμός", "Περίοδος Εξεταστικής", "Έτος Διδασκαλίας", "Αριθμός Μητρώου Φοιτητή"]
    layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
    m=0
    windowvathmologies = sg.Window("Βαθμολογίες", layout)
    while True:
        event, values = windowvathmologies.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break    
    windowvathmologies.close()
    conn.close()

def edit_foititi(am_foititi):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    layout=[[sg.Text("Τι θέλεις να αλλάξεις;" ,key="-text-")],
            [sg.Button("Αριθμός Μητρώου", key="-arithmos_mitroou-"),
             sg.Button("Ονοματεπώνυμο", key="-onomateponymo-"),
             sg.Button("Κινητό Τηλέφωνο", key="-kinito-"),
             sg.Button("Σταθερό Τηλέφωνο", key="-stathero-"),
             sg.Button("Ημερομηνία Γέννησης", key="-hmeromhnia_gennisis-"),
             sg.Button("Email", key="-email-"),
             sg.Button("Χώρα", key="-xwra-"),
             sg.Button("Περιοχή", key="-perioxi-"),
             sg.Button("Πόλη", key="-poli-"),
             sg.Button("Οδός", key="-odos-"),
             sg.Button("Αριθμός", key="-arithmos-"),
             sg.Button("ΤΚ", key="-tk-"),
             sg.Button("Εξάμηνο Φοίτησης", key="-examino-"),
             sg.Button("Κατεύθυνση", key="-kateythinsi-")],
            [sg.Button("Exit", key="-exit-")]]
    windowedit = sg.Window("Edit", layout)
    while True:
        event, values = windowedit.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-arithmos_mitroou-":
            layout0=[[sg.Text("Νέος Αριθμός Μητρώου:"), sg.InputText(key='-0-')],
                     [sg.Submit(), sg.Cancel(key="-cancel-")]]
            window0 = sg.Window("Edit specific",layout0)
            event0, values0 = window0.read()
            try:
                tuples0=tuple([int(values0['-0-'])])+am_foititi
                print(len(int(values0['-0-'])))
            except: #if input is not integer
                if not event0 =="-cancel-": 
                    print("Invalid data")
            else:
                if (len(int(values0['-0-']))==7) and not event0 =="-cancel-" :
                    c.execute('''UPDATE ΦΟΙΤΗΤΗΣ
                         SET "Αριθμός Μητρώου"=?
                         WHERE "Αριθμός Μητρώου"=?;''', tuples0)
                    conn.commit()
                else:
                    print("Invalid data")
            finally:
                window0.close()
        #notokay        
        if event == "-onomateponymo-":
            layout1=[[sg.Text("Νέο Ονοματεπώνυμο:"), sg.InputText(key='-1-')],
                     [sg.Submit(), sg.Cancel()]]
            window1 = sg.Window("Edit specific",layout1)
            event1, values1 = window1.read()
            tuples1=tuple([values1['-1-']])+am_foititi
            window1.close()
            c.execute('''UPDATE ΦΟΙΤΗΤΗΣ
                         SET "Ονοματεπώνυμο"=?
                         WHERE "Αριθμός Μητρώου"=?;''',tuples1)
            conn.commit()
    windowedit.close()


def insertfoititi():
    layout = [[sg.Text('Αριθμός Μητρώου', size =(20, 1)), sg.InputText(key='-0-')],
              [sg.Text('Ονοματεπώνυμο', size =(20, 1)), sg.InputText(key='-1-')],
              [sg.Text('Κινητό Τηλέφωνο', size =(20, 1)), sg.InputText(key='-2-')],
              [sg.Text('Σταθερό Τηλέφωνο', size =(20, 1)), sg.InputText(key='-3-')],
              [sg.Text('Ημερομηνία Γέννησης', size =(20, 1)), sg.InputText(key='-4-')],
              [sg.Text('Email', size =(20, 1)), sg.InputText(key='-5-')],
              [sg.Text('Χώρα', size =(20, 1)), sg.InputText(key='-6-')],
              [sg.Text('Περιοχή', size =(20, 1)), sg.InputText(key='-7-')],
              [sg.Text('Πόλη', size =(20, 1)), sg.InputText(key='-8-')],
              [sg.Text('Οδός', size =(20, 1)), sg.InputText(key='-9-')],
              [sg.Text('Αριθμός', size =(20, 1)), sg.InputText(key='-10-')],
              [sg.Text('Ταχυδρομικός Κώδικας', size =(20, 1)), sg.InputText(key='-11-')],
              [sg.Text('Εξάμηνο Φοίτησης', size =(20, 1)), sg.Combo([1,2,3,4,5,6,7,8,9,10], key='-12-', size =(45, 1))],
              [sg.Text('Όνομα Κατεύθυνσης', size =(20, 1)),
               sg.Combo(["Υπολογιστές", "Επικοινωνίες", "Τεχνολογία της Πληροφορίας", "Ηλεκτρονική και Ενσωματωμένα Συστήματα"], key='-13-', size =(45, 1))],
              [sg.Button("Υποβολή", key="-ypovoli-"), sg.Button("Exit", key="-exit-")]]
    windowneosfoititis = sg.Window('Νέος Φοιτητής', layout)
    while True:
        event, values = windowneosfoititis.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-ypovoli-":
            conn=sqlite3.connect("student_services.db")
            c=conn.cursor()
            mydata2=[]
            for i in range (len(values)):
                key='-'+str(i)+'-'
                if (values[key]==''):
                    mydata2.append(values[key])
                    continue
                else:
                    if (i==0) or (i==2) or (i==3) or (i==10) or (i==11):
                        mydata2.append(int(float(values[key])))
                    elif (i==1) or (i==4) or (i==5) or (i==6) or (i==7) or (i==8) or (i==9) or (i==12) or (i==13):
                        mydata2.append(values[key])
            try:
                c.execute('''INSERT INTO ΦΟΙΤΗΤΗΣ("Αριθμός Μητρώου", "Ονοματεπώνυμο", "Κινητό Τηλέφωνο", "Σταθερό Τηλέφωνο", "Ημερομηνία Γέννησης" , "Email", "Χώρα", "Περιοχή", "Πόλη", "Οδός", "Αριθμός",
                "Ταχυδρομικός Κώδικας", "Εξάμηνο Φοίτησης", "Όνομα Κατεύθυνσης") VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', mydata2[:])
                conn.commit()
            except:
                print("Couldn't insert data.")
            data=c.fetchall()
            conn.close()
    windowneosfoititis.close()

    
def main():
    main_window()

 
if __name__ == "__main__":
    main()



