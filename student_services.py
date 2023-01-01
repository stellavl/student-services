import PySimpleGUI as sg
import sqlite3

#CHANGED NOW

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
        newevent, newvalues = sg.Window('Message Window',
                  [[sg.T("Couldn't log in student")],
                  [sg.B('OK')]]).read(close=True)
        kodikos_foititi(user)
    else:
        layout = [[sg.Button("Προσωπικά Στοιχεία", key="-stoixeia-")],                 
                  [sg.Button("Μαθήματα", key="-mathimata-")],
                  [sg.Button("Διδασκαλίες", key="-didaskalies-")],
                  [sg.Button("Κατευθύνσεις", key="-kateythinseis-")],
                  [sg.Button("Βαθμολογίες", key="-vathmologies-")],
                  [sg.Button("Καθηγητές", key="-kathigites-")],               
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
                mathimata(am, user)
            if event == "-kateythinseis-":
                kateythinseis(user)
            if event == "-vathmologies-":
                vathmologies(am, user)
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
            newevent, newvalues = sg.Window('Message Window',
                                [[sg.T("Couldn't log in student")],
                                  [sg.B('OK')]]).read(close=True)
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
        newevent, newvalues = sg.Window('Message Window',
                                [[sg.T("Couldn't log in teacher")],
                                  [sg.B('OK')]]).read(close=True)
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
                vathmologies(ID, user)
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
            newevent, newvalues = sg.Window('Message Window',
                                [[sg.T("Couldn't log in teacher")],
                                  [sg.B('OK')]]).read(close=True)
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
            mathimata(0, user)
        if event == "-kateythinseis-":
            kateythinseis(user)
        if event == "-vathmologies-":
            vathmologies(0, user)
    windowprosopikou.close()

#----------------FOITITES-------------------    

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
    
#----------------KATHIGITES-------------------    

def kathigites(user,ID):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    if user==1: #user=foititis
        c.execute('''select "Ονοματεπώνυμο", "Βαθμίδα" from ΚΑΘΗΓΗΤΗΣ order by "Ονοματεπώνυμο"''')
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            c.append([data[i][0],data[i][1]])
        headings = ["Ονοματεπώνυμο", "Βαθμίδα"]
        data=c
        layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
        windowkathigites = sg.Window("Καθηγητές", layout)
        while True:
            event, values = windowkathigites.read()
            if event == "-exit-" or event == sg.WIN_CLOSED:
                break
    elif user==2: #user=kathigitis
        c.execute('''select * from ΚΑΘΗΓΗΤΗΣ where "ID"=?''',ID)
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            c.append([data[i][0],data[i][1],data[i][2]])
        headings = ["ID","Ονοματεπώνυμο", "Βαθμίδα"]
        data=c
        layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
        windowkathigites = sg.Window("Καθηγητές", layout)
        while True:
            event, values = windowkathigites.read()
            if event == "-exit-" or event == sg.WIN_CLOSED:
                break
    elif user==3: #user=grammateia
        c.execute('''select * from ΚΑΘΗΓΗΤΗΣ order by "Ονοματεπώνυμο"''')
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            c.append([data[i][0],data[i][1],data[i][2]])
        headings = ["ID","Ονοματεπώνυμο", "Βαθμίδα"]
        data=c
        layout = [[sg.Text("Επέλεξε έναν καθηγητή για να τον επεξεργαστείς:")],
               [sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
        windowkathigites = sg.Window("Καθηγητές", layout)
        while True:
            event, values = windowkathigites.read()
            try:
                if event == "-exit-" or event == sg.WIN_CLOSED:
                    break
                elif event[0] =='-TABLE-':
                        seira=data[event[2][0]]
                        selected_id=seira[0]
                        click_kathigiti(user,selected_id)
                        windowkathigites.close()
                        kathigites(user,ID)
            except TypeError:
                newevent, newvalues = sg.Window('Message Window',
                                [[sg.T("Επέλεξε έναν καθηγητή.")],
                                  [sg.B('OK')]],size=(300,70)).read(close=True)

    conn.close()
    windowkathigites.close()

def click_kathigiti(user,ID):
    layout=[[sg.Text("Επέλεξες τον καθηγητή με ID="+str(ID))],
             [sg.Button("Edit", key="-edit-"),
             sg.Button("Delete",key="-delete-"),
             sg.Button("Exit",key="-exit-")]]
    window=sg.Window("Επεξεργασία Καθηγητή",layout,size=(300,70))
    tuple_id=tuple([ID])
    while True:
        event, values = window.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-delete-":
            delete_kathigiti(tuple_id)
            break
        if event == "-edit-":
            edit_kathigiti(tuple_id)
            break
    window.close()


def edit_kathigiti(ID):
    print("edit")
    return
    
def delete_kathigiti(ID):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''DELETE FROM ΚΑΘΗΓΗΤΗΣ WHERE "ID"=(?)''',ID)
    conn.commit()
    conn.close()
    return           

#----------------DIDASKALIES-------------------

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
        c.append([data[i][0],data[i][1]])
    data=c
    headings = ["Όνομα", "Κωδικός Μαθήματος"]
    layout = [[sg.Table(values=data, headings=headings,
                        justification='center',
                        num_rows=15,
                        key='-TABLE-',
                        enable_events=True,
                        enable_click_events=True)],
              [sg.Button("Exit", key="-exit-")]]
    windowdidaskalies = sg.Window("Μαθήματα που διδάχθηκαν", layout)
    while True:
        event, values = windowdidaskalies.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
    windowdidaskalies.close()
    conn.close()
    
def click_didaskalia(user,kodikos):
    layout=[[sg.Text("Επέλεξες τη διδασκαλία με κωδικό="+str(kodikos))],
             [sg.Button("Edit", key="-edit-"),
             sg.Button("Delete",key="-delete-"),
             sg.Button("Exit",key="-exit-")]]
    window=sg.Window("Επεξεργασία Διδασκαλίας",layout,size=(300,70))
    tuple_id=tuple([kodikos])
    while True:
        event, values = window.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-delete-":
            delete_didaskalia(tuple_id)
            break
        if event == "-edit-":
            edit_didaskalia(tuple_id)
            break
    window.close()

def edit_didaskalia(kodikos):
    print("edit")
    return
    
def delete_didaskalia(kodikos):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''DELETE FROM ΔΙΔΑΣΚΑΛΙΑ WHERE "Κωδικός Διδασκαλίας"=(?)''',kodikos)
    conn.commit()
    conn.close()
    return

#----------------MATHIMATA-------------------


def mathimata(am,user):
    if user==1:
        mathimata_foititi(am)
    elif user==2:
        mathimata_kathigiti()
    elif user==3:
        mathimata_grammateias()

def mathimata_foititi(am):
    layout=[[sg.Button("Δηλωμένα Μαθήματα", key="-dilomena-"),
             sg.Button("Όλα τα μαθήματα", key="-ola-")],
            [sg.Button("Exit", key="-exit-")]]
    window = sg.Window("Μαθήματα", layout)
    while True:
        event, values = window.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        elif event == "-dilomena-":
            dilomena_mathimata(am)
        elif event == "-ola-":
            mathimata_grammateias()
    window.close()
    
def dilomena_mathimata(am):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''select "Κωδικός", "Όνομα", "Εξάμηνο Διδασκαλίας"
                from ΔΗΛΩΝΕΙ, ΜΑΘΗΜΑ
                where "Κωδικός"="Κωδικός Μαθήματος" and "Αριθμός Μητρώου Φοιτητή"=?
                order by "Εξάμηνο Διδασκαλίας" DESC''',am)
    data=c.fetchall()
    conn.close()
    c=[]
    for i in range(len(data)):
        c.append([data[i][0],data[i][1],data[i][2]])
    data=c
    headings = ["Κωδικός", "Όνομα", "Εξάμηνο Διδασκαλίας"]
    layout = [[sg.Table(values=data, headings=headings,
                            justification='center',
                            num_rows=15,
                            key='-TABLE-',
                            enable_events=True,
                            enable_click_events=True)],
                [sg.Button("Νέα Δήλωση", key="-dilosi-"),
                 sg.Button("Αναίρεση Δήλωσης", key="-anairesi-"),
                 sg.Button("Exit", key="-exit-")]]
    windowmathimata = sg.Window("Μαθήματα", layout)
    while True:
        event, values = windowmathimata.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        elif event == "-dilosi-":
            new_dilosi(am)
            windowmathimata.close()
            dilomena_mathimata(am)
        elif event == "-anairesi-":
            anairesi_dilosis(am)
            windowmathimata.close()
            dilomena_mathimata(am)
    windowmathimata.close()

def new_dilosi(am):
    flag=0
    mydata=[]
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    layout=[[sg.Text("Νέα Δήλωση:")],
            [sg.Combo(["Εισαγωγή στους Υπολογιστές",
                       "Διαδικαστικός Προγραμματισμός",
                       'Ψηφιακά Κυκλώματα και Συστήματα',
                       'Οργάνωση Υπολογιστών',
                       'Ολοκληρωμένα Ηλεκτρονικά',
                       'Αλγόριθμοι και Δομές Δεδομένων',
                       'Βάσεις Δεδομένων',
                       'Προγραμματισμός Διαδικτύου',
                       'Διαδραστικές Τεχνολογίες',
                       'Μηχανική Μάθηση'], key='-mathima-')],
            [sg.Button("Υποβολή", key="-ypovoli-"),
             sg.Button("Exit", key="-exit-")]]
    window = sg.Window("Μαθήματα", layout)
    while True:
        event, values = window.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        elif event == "-ypovoli-":
            tuplemathima=tuple([values['-mathima-']])
            c.execute('''select "Κωδικός" from ΜΑΘΗΜΑ where "Όνομα"=?''',tuplemathima)
            kodikos=c.fetchall()
            c.execute('''select "Κωδικός Μαθήματος" from ΔΗΛΩΝΕΙ''')
            all_kodikoi=c.fetchall()
            #check if mathima is dilomeno
            for i in range(len(all_kodikoi)):
                if kodikos[0]==all_kodikoi[i]:
                    flag=1
                    break
            if flag==1: 
                newevent, newvalues = sg.Window('Message Window',
                                [[sg.T("Το μάθημα είναι ήδη δηλωμένο.")],
                                  [sg.B('OK')]]).read(close=True)
                window.close()
                new_dilosi(am)
            else: #check if examino foitisis>=examino didaskalias
                c.execute('''select "Εξάμηνο Φοίτησης" from ΦΟΙΤΗΤΗΣ where "Αριθμός Μητρώου"=?''',am)
                examino_foitisis=c.fetchall()
                c.execute('''select "Εξάμηνο Διδασκαλίας" from ΜΑΘΗΜΑ where "Κωδικός"=?''',kodikos[0])
                examino_didaskalias=c.fetchall()
                if examino_didaskalias>examino_foitisis:
                    newlayout=[[sg.Text(text="Για αυτό το μάθημα πρέπει το εξάμηνο φοίτησής σου να είναι τουλάχιστον "+str(examino_didaskalias[0][0]))],
                               [sg.Button('OK',key='-ok-')]]
                    newwindow=sg.Window('Message Window',newlayout,size=(600, 70))
                    while True:
                        newevent, newvalues = newwindow.read()
                        if newevent == "-ok-" or newevent == sg.WIN_CLOSED:
                            break
                    newwindow.close()
                    new_dilosi(am)
                    #-----------
                    #check if mathima is perasmeno
                    #---------------
                else:
                    mydata.append(am[0])
                    mydata.append(kodikos[0][0])
                    c.execute('''INSERT INTO ΔΗΛΩΝΕΙ("Αριθμός Μητρώου Φοιτητή","Κωδικός Μαθήματος") VALUES (?,?)''', mydata[:])
                    newevent, newvalues = sg.Window('Message Window',
                                          [[sg.T("Επιτυχής Δήλωση")],
                                             [sg.B('OK')]]).read(close=True)
                    conn.commit()
                    break
    conn.close()
    window.close()
    

def anairesi_dilosis(am):
    flag=0
    mydata=[]
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    layout=[[sg.Text("Αναίρεση Δήλωσης:")],
            [sg.Combo(["Εισαγωγή στους Υπολογιστές",
                       "Διαδικαστικός Προγραμματισμός",
                       'Ψηφιακά Κυκλώματα και Συστήματα',
                       'Οργάνωση Υπολογιστών',
                       'Ολοκληρωμένα Ηλεκτρονικά',
                       'Αλγόριθμοι και Δομές Δεδομένων',
                       'Βάσεις Δεδομένων',
                       'Προγραμματισμός Διαδικτύου',
                       'Διαδραστικές Τεχνολογίες',
                       'Μηχανική Μάθηση'], key='-mathima-')],
            [sg.Button("Υποβολή", key="-ypovoli-"),
             sg.Button("Exit", key="-exit-")]]
    window = sg.Window("Μαθήματα", layout)
    while True:
        event, values = window.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        elif event == "-ypovoli-":
            tuplemathima=tuple([values['-mathima-']])
            c.execute('''select "Κωδικός" from ΜΑΘΗΜΑ where "Όνομα"=?''',tuplemathima)
            data=c.fetchall()
            c.execute('''select "Κωδικός Μαθήματος" from ΔΗΛΩΝΕΙ''')
            alldata=c.fetchall()
            #check if mathima is dilomeno
            for i in range(len(alldata)):
                if data[0]==alldata[i]:
                    flag=1
                    break
            if flag!=1:
                newevent, newvalues = sg.Window('Message Window',
                                          [[sg.T("Το μάθημα δεν είναι δηλωμένο.")],
                                             [sg.B('OK')]]).read(close=True)
                window.close()
                anairesi_dilosis(am)
            else:
                mydata.append(am[0])
                mydata.append(data[0][0])
                c.execute('''DELETE FROM ΔΗΛΩΝΕΙ WHERE "Αριθμός Μητρώου Φοιτητή"=? AND "Κωδικός Μαθήματος"=?''', mydata[:])
                newevent, newvalues = sg.Window('Message Window',
                                          [[sg.T("Επιτυχής Αναίρεση.")],
                                             [sg.B('OK')]]).read(close=True)
                conn.commit()
                break
    conn.close()
    window.close()
    
def mathimata_grammateias(): 
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

def vathmologies(am, user):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    if user==1:
        c.execute('''SELECT M."Κωδικός", M."Όνομα", "Βαθμός", "Περίοδος Εξεταστικής"
        FROM ΒΑΘΜΟΛΟΓΙΑ as B, ΑΝΤΙΣΤΟΙΧΕΙ as A, ΔΙΔΑΣΚΑΛΙΑ as D, ΜΑΘΗΜΑ as M, ΕΧΕΙ AS E
        WHERE B."Κωδικός Βαθμολογίας"=A."Κωδικός Βαθμολογίας"=E."Κωδικός Βαθμολογίας" AND A."Κωδικός Διδασκαλίας"=D."Κωδικός Διδασκαλίας"
        AND "Κωδικός Μαθήματος"="Κωδικός" AND "Αριθμός Μητρώου Φοιτητή"=?;''', am)
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            c.append([data[i][0],data[i][1],data[i][2],data[i][3]])
        headings = ["Κωδικός", "Όνομα Μαθήματος", "Βαθμός", "Περίοδος Εξεταστικής"]
        data=c
        layout = [[sg.Table(values=data, headings=headings,
                            justification='center',
                            key='-TABLE-',
                            enable_events=True,
                            enable_click_events=True)],
                  [sg.Button("Exit", key="-exit-")]]
    elif user==2:
        ID=am
        c.execute("""SELECT "Αριθμός Μητρώου Φοιτητή", M."Κωδικός", M."Όνομα", "Βαθμός", "Περίοδος Εξεταστικής"
        FROM ΒΑΘΜΟΛΟΓΙΑ as B, ΑΝΤΙΣΤΟΙΧΕΙ as A, ΔΙΔΑΣΚΑΛΙΑ as D, ΜΑΘΗΜΑ as M, ΠΑΡΑΔΙΔΕΙ as P, ΕΧΕΙ as E
        WHERE B."Κωδικός Βαθμολογίας"=A."Κωδικός Βαθμολογίας"=E."Κωδικός Βαθμολογίας" AND A."Κωδικός Διδασκαλίας"=D."Κωδικός Διδασκαλίας"
        AND "Κωδικός Μαθήματος"="Κωδικός" AND P."Κωδικός Διδασκαλίας"=D."Κωδικός Διδασκαλίας" AND "ID Καθηγητή"=?;""", ID)
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            c.append([data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]])
        headings = ["Αριθμός Μητρώου Φοιτητή", "Κωδικός", "Όνομα Μαθήματος", "Βαθμός", "Περίοδος Εξεταστικής"]
        data=c
        layout = [[sg.Table(values=data, headings=headings,
                            justification='center',
                            key='-TABLE-',
                            enable_events=True,
                            enable_click_events=True)],
                  [sg.Button("Insert", key="-insert_vathmologia-"), sg.Button("Exit", key="-exit-")]]
    elif user==3:
        c.execute('''SELECT "Αριθμός Μητρώου Φοιτητή", M."Κωδικός", M."Όνομα", "Βαθμός", "Περίοδος Εξεταστικής"
        FROM ΒΑΘΜΟΛΟΓΙΑ as B, ΑΝΤΙΣΤΟΙΧΕΙ as A, ΔΙΔΑΣΚΑΛΙΑ as D, ΜΑΘΗΜΑ as M, ΕΧΕΙ as E
        WHERE B."Κωδικός Βαθμολογίας"=A."Κωδικός Βαθμολογίας"=E."Κωδικός Βαθμολογίας" AND A."Κωδικός Διδασκαλίας"=D."Κωδικός Διδασκαλίας"
        AND "Κωδικός Μαθήματος"="Κωδικός";''')
        data=c.fetchall()
        c=[]
        for i in range(len(data)):
            c.append([data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]])
        headings = ["Αριθμός Μητρώου Φοιτητή", "Κωδικός", "Όνομα Μαθήματος", "Βαθμός", "Περίοδος Εξεταστικής"]
        data=c
        layout = [[sg.Table(values=data, headings=headings,
                            justification='center',
                            key='-TABLE-',
                            enable_events=True,
                            enable_click_events=True)],
                  [sg.Button("Exit", key="-exit-")]]
    windowvathmologies = sg.Window("Βαθμολογίες", layout)
    while True:
        event, values = windowvathmologies.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-insert_vathmologia-":
            insert_vathmologia(ID)
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
               # print(len(int(values0['-0-'])))
            except: #if input is not integer
                if not event0 =="-cancel-":
                    newevent, newvalues = sg.Window('Message Window',
                                          [[sg.T("Invalid data")],
                                             [sg.B('OK')]]).read(close=True)
            else:
                if (len(int(values0['-0-']))==7) and not event0 =="-cancel-" :
                    c.execute('''UPDATE ΦΟΙΤΗΤΗΣ
                         SET "Αριθμός Μητρώου"=?
                         WHERE "Αριθμός Μητρώου"=?;''', tuples0)
                    conn.commit()
                else:
                    newevent, newvalues = sg.Window('Message Window',
                                          [[sg.T("Invalid data")],
                                             [sg.B('OK')]]).read(close=True)
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
              [sg.Text('Ημερομηνία Γέννησης', size =(20, 1)), sg.InputText(key='-4-'),
               sg.CalendarButton("Select Date", close_when_date_chosen=True, target='-4-', format='%Y-%m-%d', size=(10,1), default_date_m_d_y=(1,1,2004))],
              [sg.Text('Email', size =(20, 1)), sg.InputText(key='-5-')],
              [sg.Text('Χώρα', size =(20, 1)), sg.InputText(key='-6-')],
              [sg.Text('Περιοχή', size =(20, 1)), sg.InputText(key='-7-')],
              [sg.Text('Πόλη', size =(20, 1)), sg.InputText(key='-8-')],
              [sg.Text('Οδός', size =(20, 1)), sg.InputText(key='-9-')],
              [sg.Text('Αριθμός', size =(20, 1)), sg.InputText(key='-10-')],
              [sg.Text('Ταχυδρομικός Κώδικας', size =(20, 1)), sg.InputText(key='-11-')],
              [sg.Text('Εξάμηνο Φοίτησης', size =(20, 1)), sg.InputText(key='-12-')],
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
            for i in range (len(values)-1):
                key='-'+str(i)+'-'
                if (values[key]=='') and (key!='-0-') and (key!='-12-'):
                    mydata2.append(values[key])
                elif (values[key]=='') and (key=='-0-'):
                    break
                elif (values[key]=='') and (key=='-12-'):
                    break
                else:
                    if (i==0) or (i==2) or (i==3) or (i==10) or (i==11) or (i==12):
                        if (len(values['-0-'])!=7):
                            break
                        elif (values['-0-'][0]=='0'):
                            break
                        else:
                            try:
                                mm=float(values[key])
                            except:
                                break
                            else:
                                mydata2.append(int(float(values[key])))
                    elif (i==1) or (i==4) or (i==5) or (i==6) or (i==7) or (i==8) or (i==9) or (i==13):
                        try:
                            mm=float(values[key])
                        except:
                            mydata2.append(values[key])
                        else:
                            break
            try:
                if (len(mydata2)==14):
                    c.execute('''INSERT INTO ΦΟΙΤΗΤΗΣ("Αριθμός Μητρώου", "Ονοματεπώνυμο", "Κινητό Τηλέφωνο", "Σταθερό Τηλέφωνο", "Ημερομηνία Γέννησης" , "Email", "Χώρα", "Περιοχή", "Πόλη", "Οδός", "Αριθμός",
                    "Ταχυδρομικός Κώδικας", "Εξάμηνο Φοίτησης", "Όνομα Κατεύθυνσης") VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', mydata2[:])
                    conn.commit()
                else:
                    newevent, newvalues = sg.Window('Message Window',
                                          [[sg.T("Wrong data.")],
                                             [sg.B('OK')]]).read(close=True)
            except:
                newevent1, newvalues1 = sg.Window('Message Window',
                                          [[sg.T("Couldn't insert data.")],
                                             [sg.B('OK')]]).read(close=True)
            finally:
                conn.close()
                windowneosfoititis.close()
    windowneosfoititis.close()


def insert_vathmologia(ID):
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    #Εμφανίζει τους φοιτητές που έχουν δηλώσει μάθημα που παραδίδει ο καθηγητής
    c.execute('''SELECT "Αριθμός Μητρώου Φοιτητή"
    FROM ΔΗΛΩΝΕΙ
    WHERE ΔΗΛΩΝΕΙ."Κωδικός Μαθήματος" IN(
    SELECT D."Κωδικός Μαθήματος"
    FROM ΔΙΔΑΣΚΑΛΙΑ AS D, ΠΑΡΑΔΙΔΕΙ AS P
    WHERE D."Κωδικός Διδασκαλίας"=P."Κωδικός Διδασκαλίας" AND P."ID Καθηγητή"=?);''', ID)
    data1=c.fetchall()
    newdata1=[]
    for i in range(len(data1)):
        newdata1.append(data1[i])
    data1=[]
    for i in range(len(newdata1)):
        data1.append(int(str(newdata1[i])[1:8]))
    layout = [[sg.Text(" Επέλεξε τον φοιτητή που θες:")],
              [sg.Text('Αριθμός Μητρώου Φοιτητή', size =(20, 1)), sg.Combo(data1, key='-0-')],
              [sg.Button("Υποβολή", key="-ypovoli-"), sg.Button("Exit", key="-exit-")]]
    windowamfoititi = sg.Window('Αριθμός Μητρώου Φοιτητή', layout)
    while True:
        event, values = windowamfoititi.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-ypovoli-":
            if values['-0-']!='':
                am=values['-0-']
                newID=[]
                for i in range(len(ID)):
                    newID.append(ID[i])
                ID=int(float(newID[0]))
                windowamfoititi.close()
                insert_vathmos(ID,am)
            else:
                print("Δεν έγινε επιλογή φοιτητή")
                windowamfoititi.close()
                insert_vathmologia(ID)
    conn.close()
    windowamfoititi.close()

def insert_vathmos(ID, am):
    combo1=[ID,am]
    #Εμφανίζει τους Κωδικούς διδασκαλιας σε μαθήματα του καθηγητή που έχει δηλώσει ένας συγκεκριμένος φοιτητής
    conn=sqlite3.connect("student_services.db")
    c=conn.cursor()
    c.execute('''SELECT D."Κωδικός Διδασκαλίας"
    FROM ΔΙΔΑΣΚΑΛΙΑ AS D, ΠΑΡΑΔΙΔΕΙ AS P
    WHERE D."Κωδικός Διδασκαλίας"=P."Κωδικός Διδασκαλίας" AND P."ID Καθηγητή"=? 
    AND D."Κωδικός Μαθήματος" IN (
    SELECT "Κωδικός Μαθήματος"
    FROM ΔΗΛΩΝΕΙ
    WHERE "Αριθμός Μητρώου Φοιτητή"=?);''', combo1[:])
    data2=c.fetchall()
    c.execute('''SELECT "Κωδικός Βαθμολογίας" FROM ΒΑΘΜΟΛΟΓΙΑ;''')
    data3=c.fetchall()
    layout = [[sg.Text('Κωδικός Διδασκαλίας', size =(20, 1)), sg.Combo(data2, key='-1-')],
              [sg.Text('Βαθμός', size =(20, 1)), sg.InputText(key='-2-')],
              [sg.Text('Περίοδος Εξεταστικής', size =(20, 1)), sg.Combo(["Χειμερινό Εξάμηνο", "Εαρινό Εξάμηνο", "Επαναληπτικές"], key='-3-')],
              [sg.Text('Κωδικός Βαθμολογίας', size =(20, 1)), sg.InputText(key='-4-')],
              [sg.Button("Υποβολή", key="-ypovoli-"), sg.Button("Exit", key="-exit-")]]
    windowneavathmologia = sg.Window('Νέα Βαθμολογία', layout)
    while True:
        event, values = windowneavathmologia.read()
        if event == "-exit-" or event == sg.WIN_CLOSED:
            break
        if event == "-ypovoli-":
            mydata2=[]
            for i in range (1, len(values)+1):
                key='-'+str(i)+'-'
                if (values[key]==''):
                    break
                else:
                    if (i==2) or (i==4):
                        try:
                            if i==2:
                                vathmos=int(values['-2-'])
                            elif i==4:
                                kodikos=int(values['-4-'])
                        except:
                            break
                        else:
                            if (vathmos<0) or (vathmos>10):
                                break
                            elif (i==4):
                                e=0
                                for j in data3:
                                    newj=[]
                                    for k in range(len(j)):
                                        newj.append(j[k])
                                    j=newj[0]
                                    if kodikos==j:
                                        e=0
                                        break
                                    else:
                                        e=1
                                if e==1:
                                    mydata2.append(int(values[key]))
                            else:
                                mydata2.append(int(values[key]))
                        
                    else:
                        if (i==1):
                            didaskalia=values[key]
                            newd=[]
                            for i in range(len(didaskalia)):
                                newd.append(didaskalia[i])
                            didaskalia=int(float(newd[0]))
                        mydata2.append(values[key])
            try:
                if (len(mydata2)==4):
                    combo2=[am, mydata2[3]]
                    combo3=[didaskalia, mydata2[3]]
                    c.execute('''INSERT INTO ΒΑΘΜΟΛΟΓΙΑ("Βαθμός", "Περίοδος Εξεταστικής", "Κωδικός Βαθμολογίας") VALUES (?,?,?);''', mydata2[1:])
                    conn.commit()
                    c.execute('''INSERT INTO ΕΧΕΙ("Αριθμός Μητρώου Φοιτητή", "Κωδικός Βαθμολογίας") VALUES (?,?);''', combo2[:])
                    conn.commit()
                    c.execute('''INSERT INTO ΑΝΤΙΣΤΟΙΧΕΙ("Κωδικός Διδασκαλίας", "Κωδικός Βαθμολογίας") VALUES (?,?);''', combo3[:])
                    conn.commit()
                else:
                    print("Wrong data.")
            except:
                print("Couldn't insert data.")
            finally:
                conn.close()
                windowneavathmologia.close()
    windowneavathmologia.close()

    
def main():
    main_window()

 
if __name__ == "__main__":
    main()



