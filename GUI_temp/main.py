from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import time

#   Primāra loga iestatījumi:
root = Tk()                                 #   Primāra loga inicijalizacija ar nosaukumu root.
root['bg'] = '#2a374a'                      #   Primāra loga fona krāsa.
root.title('Linass Jokšass 221RDB522')      #   Primāra loga nosaukums.
root.geometry('1200x800')                   #   Primāra loga izmērs.
root.resizable(width=False, height=False)   #   Aizslēgt primāra loga mērogošanu.

#   Izmantojiet Tkinter bibliotēkas Canvas klasi, lai izveidotu taisnstūrveida/bloku objektu, izmantojot šādus parametrus:
    #   <nosaukums>,                    - Vecākās loga/vidžeta nosaukums, kurā atrodas objekts.
    #   highlightthickness = <skaits>,  - Parametrs tiek izmantots, lai atbrīvotos no objekta ramja, nevis parametrš "borderwidth=", kas ramjā vietā atstāj baltu artefaktu.
    #   bg = '<krāsa>',                 - Objekta krāsa.
    #   width = <skaits>,               - Objekta platums.
    #   height = <skaits>,              - Objekta augstums.
rootHeader = Canvas(root, highlightthickness=0, bg='#5159a7', width=1200, height=40)
rootPlotArea = Canvas(root, highlightthickness=0, bg='#bacae8', width=1100, height=550)
rootFooter = Canvas(root, highlightthickness=0, bg='#5159a7', width=1200, height=60)
logBox = Canvas(root, highlightthickness=0, bg='#bacae8', width=1100, height=40)

#   Izmantojiet Tkinter bibliotēkas Label klasi, lai izveidotu teksta objektu, izmantojot šādus parametrus:
    #   <nosaukums>,                                                 - Vecākās loga/vidžeta nosaukums, kurā atrodas objekts.
    #   text = '<tekts>',                                            - Teksts uz pogas.
    #   font = (<'teksta fonti','teksta izmērs','teksta stils'>'),   - Teksta iestatījumi.
    #   fg = '<krāsa>',                                              - Teksta krāsa.
    #   bg = '<krāsa>',                                              - Fona krāsa.
rootHeaderText = Label(root, text='BREZENHEMA ALGORITMA IZMANTOŠANA 2D OBJEKTA PĀRVIETOŠANAI.', font=('arial', 16, 'bold'), fg='#ffffff', bg='#5159a7')
logText = Label(root, text='> ::', font=( 'arial', 16, 'bold'), bg='#bacae8', fg='#2a374a')

#   <Objekta nosaukums>.place - Metode, kas ļauj novietot objektu attiecībā pret vecākā loga/vidžeta x un y koordinātēm.
rootHeader.place(x=0, y=0)
rootPlotArea.place(x=80, y=120)
rootFooter.place(x=0, y=740)
logBox.place(x=80, y=750)
rootHeaderText.place(x=230, y=5)
logText.place(x=90, y=755)

#region Skalu un režģa izveide:
#   Cikls, kas izveide režģis animācijas logā.
xGrid = 0
while xGrid <= 22:      #   Izveido lodveida figūru uz rootPlotArea objektā ar horizontālu atstarpi 50 pikseļi, kamer xGrid koeficients nesasniedz 22.
    yGrid = 0
    while yGrid <= 11:  #   Izveido lodveida figūru uz rootPlotArea objektā ar vertikālu atstarpi 50 pikseļi, kamer yGrid koeficients nesasniedz 11.
        #   Izmantojiet Tkinter bibliotēkas Canvas klasā metodu Create_oval, lai izveidotu lodveida figūra virs objekta, izmantojot šādus parametrus:
            #   <skaits>,               - x koordinātas sākum punkts.
            #   <skaits>,               - y koordinātas sākum punkts.
            #   <skaits>,               - x koordinātas gala punkts.
            #   <skaits>,               - y koordinātas gala punkts.
            #   fill = "<krāsa>",       - figūras krāsa.
            #   outline = "<krāsa>",    - figūras apmales krāsa.
        rootPlotArea.create_oval(-3+(50*xGrid), -3+(50*yGrid), 3 + (50*xGrid), 3+(50*yGrid), fill="#5159a7", outline="#5159a7")
        yGrid += 1
    xGrid += 1

#   Cikls, kas izveide X ass skalu animācijas logam.
xScale = 0
while xScale <= 22: #   Izveido teksta objektu ar horizontālu atstarpi 50 pikseļi, kamer xScale koeficients nesasniedz 22.
    #   Teksta objekts tika izveidots tādā pašā veidā kā 24. rindā.
    ttk.Label(root, text=(xScale*50), font=('arial', 11, 'bold'), fg='#ffffff', bg='#2a374a').place(x=(62+(xScale*50)), y=690)
    xScale += 1

#   Cikls, kas izveide Y ass skalu animācijas logam.
yScale = 0
while yScale <= 11: #   Izveido teksta objektu ar vertikālu atstarpi 50 pikseļi, kamer yScale koeficients nesasniedz 11.
    #   Teksta objekts tika izveidots tādā pašā veidā kā 24. rindā.
    ttk.Label(root, justify="right", text=(yScale*50), font=('arial', 11, 'bold'), fg='#ffffff', bg='#2a374a').place(x=25, y=108+(yScale*50))
    yScale += 1
#endregion

#region Funkcijas
#   showPosition funkcija izmanto Tkinter bibliotēku, lai iegūtu informāciju par peles peles kursora pozīciju uz objekta.
#   Informācija tiek atjaunināta katru reizi, kad kursors pārvietojas virs objekta, saņemtās koordinātas tiek parādītas kā dinamisks teksta objekts.
def showPosition(pos):  #   "pos" - arguments, kas satur informāciju par objektu zem peles kursora.
    x = pos.x           #   X koordinātas skaitliskais apzīmējums, kas iegūts no argumenta "pos".
    y = pos.y           #   Y koordinātas skaitliskais apzīmējums, kas iegūts no argumenta "pos".

    #   Teksta objekts tika izveidots tādā pašā veidā kā 24. rindā.
    xPos = ttk.Label(root, text='X: %a   ' % (x), font=('arial', 10, 'bold'), fg='#ffffff', bg='#5159a7')
    yPos = ttk.Label(root, text='Y: %a   ' % (y), font=('arial', 10, 'bold'), fg='#ffffff', bg='#5159a7')

    #   Objekts tika novietots tādā pašā veidā kā 33. rindā.
    xPos.place(x=17, y=750)
    yPos.place(x=17, y=770)
#   BIND metode izsauc funkciju katru reizi, kad notiek norādītais notikums.
rootPlotArea.bind('<Motion>', showPosition)     #   <objekta nosaukums>.bind('<notikums>', <funkcija, kuru izsauc notikums>)

#   motion masīvs ir nepieciešams animācijas renderēšanai, šajā masīvā tiek saglabātas jaunās trajektorijas koordinātas, kas izveidotas ar Brezenhema algoritmu.
motion = [] 
#   BrezenhemaAlgoritms ir funcijas, kas aprēķina starppunktus, izmantojot Bresenhema algoritmu, lai izveidotu līniju.
#   x1, y1 - sākumpunkta koordinātas.
#   x2, y2 - galapunta koordinātas.
def BrezenhemaAlgoritms(x1, y1, x2, y2):
    #   Ja dx un dy rada negatīvu vērtību, izmantojiet moduli, lai atgrieztu tiem pozitīvu vērtību
    dx = abs(x2-x1)                                                         #   dx - delta x, jeb starpība starp pēdējo x vērtību un sākuma x vērtību
    dy = abs(y2-y1)                                                         #   dy - delta y, jeb starpība starp pēdējo y vērtību un sākuma y vērtību
    p = 2*dy-dx                                                             #   Tiek aprēķināts risinošais parametrs p, pēc kura tiek noteiktas nākošā punkta koordinātes.
   
    if x1 < x2:                                                             #   Ja x1 ir mazāks par x2, tad:
        xs = 1                                                                 #   Progresija starp x starppunktiem nākotnē būs pozitīva.
    else:
        xs = -1                                                                #   Progresija starp x starppunktiem nākotnē būs negatīva.

    if y1 < y2:                                                             #   Ja y1 ir mazāks par y2, tad:
        ys = 1                                                                #   Progresija starp y starppunktiem nākotnē būs pozitīva.
    else:
        ys = -1                                                               #   Progresija starp y starppunktiem nākotnē būs negatīva.

    x = x1                                                                  #   x punkta vērtība ir vienāda ar x sākum vērtību.
    y = y1                                                                  #   x punkta vērtība ir vienāda ar y sākum vērtību.

    if dx > dy:                                                             #   Ja delta x ir lielāks par delta y tad:
        #   Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā, bet ar tegu "toDraw".
        rootPlotArea.create_oval(x-5, y-5, x+5, y+5, tags="toDraw", fill="#f58220", outline="#f58220")  #   Tiek izveidots sākuma punkts ar izmēru 10x10 pikseli.
        while x != x2:                                                                                      #   Kamēr x sākum punkts nav vienāds ar x gala punktu, cikls aprēķina starppunktus.
            if p > 0:                                                                                       #   Ja risinošais parametrs ir lielāks par 0.
                x+=xs                                                                                           #   Tad x vērtība ir vienāda ar x + x progresiju vērtība(xs).
                y+=ys                                                                                           #   Tad y vērtība ir vienāda ar y + y progresiju vērtība(ys).
                p+=2*dy-2*dx                                                                                    #   Tad p ir p + 2 * delta y(dy) - 2 * delta x(dx).
            else:                                                                                           #   Ja risinošais parametrs ir mazāks par 0.
                x+=xs                                                                                           #   Tad x vērtība ir vienāda ar x + x progresiju vērtība(xs).
                p+=2*dy                                                                                         #   Tad p ir p + 2 * delta y(dy)
            #       Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā, bet ar tegu "toDraw".
            rootPlotArea.create_rectangle(x, y, x, y, tags="toDraw", fill="#f58220", outline="#f58220")     #   Tiek izveidots punkts ar izmēru 1x1 pikselis, lai novilktu līniju.
            motion.append(x)                                                                                #   Aizpilda pēdējo masīva elementu ar x koordinātu.
            motion.append(y)                                                                                #   Aizpilda pēdējo masīva elementu ar y koordinātu.
        #   Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā, bet ar tegu "toDraw".
        rootPlotArea.create_oval(x-5, y-5, x+5, y+5, tags="toDraw", fill="#f58220", outline="#f58220")      #   Tiek izveidots gala punkts ar izmēru 10x10 pikseli.
    else:
        #   Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā, bet ar tegu "toDraw".
        rootPlotArea.create_oval(x-5, y-5, x+5, y+5, tags="toDraw", fill="#f58220", outline="#f58220")      #   Tiek izveidots sākuma punkts ar izmēru 10x10 pikseli.
        while y != y2:                                                                                      #   Kamēr y sākum punkts nav vienāds ar y gala punktu, cikls aprēķina starppunktus.
            if p > 0:                                                                                       #   Ja risinošais parametrs ir lielāks par 0.
                x+=xs                                                                                           #   Tad x vērtība ir vienāda ar x + x progresiju vērtība(xs).
                y+=ys                                                                                           #   Tad y vērtība ir vienāda ar y + y progresiju vērtība(ys).
                p+=2*dx-2*dy                                                                                    #   Tad p ir p + 2 * delta x(dx) - 2 * delta y(dy).
            else:                                                                                           #   Ja risinošais parametrs ir mazāks par 0.
                y+=ys                                                                                           #   Tad y vērtība ir vienāda ar y + y progresiju vērtība(ys).
                p+=2*dx                                                                                         #   Tad p ir p + 2 * delta x(dx)
            #   Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā, bet ar tegu "toDraw".
            rootPlotArea.create_rectangle(x, y, x, y, tags="toDraw", fill="#f58220", outline="#f58220")      #   Tiek izveidots punkts ar izmēru 1x1 pikselis, lai novilktu līniju.
            motion.append(x)                                                                                 #   Aizpilda pēdējo masīva elementu ar x koordinātu.
            motion.append(y)                                                                                 #   Aizpilda pēdējo masīva elementu ar y koordinātu.
        #   Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā, bet ar tegu "toDraw".
        rootPlotArea.create_oval(x-5, y-5, x+5, y+5, tags="toDraw", fill="#f58220", outline="#f58220")       #   Tiek izveidots gala punkts ar izmēru 10x10 pikseli.
    createMotion()                                                                                           #   Izsauc funkciju createMotion, lai izveidotu no dotajām koordinātām animāciju.
    return

#   Rekursīvā funkcija createMotion pārbauda masīva stāvokli un sāk animācijas ciklu.
def createMotion():
    if len(motion) == 0:                                    #   Ja masīvs sākotnēji ir tukšs, aizver funkciju vai pārtrauc animāciju, ja tā ir spiesta iztukšot
        return
    try:                                                    #   Pārbauda, ​​vai funkciju var izpildīt.
        i = 0
        #   Cikls dzēš iepriekšējo figūru ar tegu "frame" un zīmē nākamo objektu ar tagu "frame", līdz tas sasniedz pēdējo masīva elementu.
        while i < len(motion):
            winUpdate()                                     #   Atjauno galveno logu, lai izvairītos no kļūdām.
            rootPlotArea.delete("frame")                    #   Dzēš iepriekšējo figūru ar tegu "frame".
            x = motion[i]                                   #   Iegūt x-koordinātu nākamajam kadram no nepāra masīva elementa.
            y = motion[i+1]                                 #   Iegūt y-koordinātu nākamajam kadram no pāra masīva elementa.
            time.sleep(0.02)                                #   Aptur cilpu uz 20 milisekundēm, lai palēninātu animāciju.

            #   Figūras objekts tika izveidots tādā pašā veidā kā 47. rindā.
            rootPlotArea.create_oval(x-10, y-10, x+10, y+10, tags="frame", fill="red", outline="red")
            i += 8                                          #   Lai atvieglotu animāciju, kadrs tiek uzzīmēts, izlaižot 4 punktus.
        createMotion()                                      #   Cikla beigās funkcija izsauc sevi, lai animācija būtu nepārtraukta.
        return                                              #   Pēc sevis izsaukšanas funkcija optimizācijas nolūkā aptur savu iepriekšējo darbību.
    except:                                                 #   Ja funkcijas izpildes laikā rodas fatāla kļūda, tad:
        print("motion stopped/rebooted")                    #   Parāda ziņojumu, ka animācija ir apturēta.

#   Funkcija logResult atjauno parametra "text=" saturu ar vērtībām no argumentiem.
def logResult(x1, y1, x2, y2):          #   Argumenti, kas jāsatur koordinātas.
    global logMsgResult                 #   Maina logMsgStart vērtību, iegūt informāciju no argumenta.
    logMsgResult = "> :: Sākumpunkts X1 = %a, Y1 = %a; Galapunkts X2 = %a, Y2 = %a." % (x1, y1, x2, y2)
    logText.config(text=logMsgResult)   #   Parametrs "text=" tiek aizstāts ar logMsgResult vērtību.

#   Funkcijas getLog nepieciešamas konstantes
logMsgStart = "> :: Lūdzu, atlasiet sākumpunktu, veicot dubultklikšķi uz loga"
logMsgEnd = "> :: Lūdzu, atlasiet galapunktu, veicot dubultklikšķi uz loga"
logMsgFull = "> :: Lūdzu, notīriet trajektorijas ekrāna lauku, noklikšķinot uz pogas \"CLEAR\""
logMsgClear = "> :: "

#   getLog ir funkcija, kas maina "text=" parametra saturu Label objektā logText, kas atrodas 31. rindā.
def getLog(msg):
    global logMsgStart                      #   Maina logMsgStart vērtību visā kodā atkarībā no nosacījuma.
    global logMsgEnd                        #   Maina logMsgEnd vērtību visā kodā atkarībā no nosacījuma.
    global logMsgFull                       #   Maina logMsgFull vērtību visā kodā atkarībā no nosacījuma.
    global logMsgClear                      #   Maina logMsgClear vērtību visā kodā atkarībā no nosacījuma.
    if msg == "start":                      #   Ja argumets (msg) satur virkni "start",tad parametrs "text=" tiek aizstāts ar logMsgStart vērtību.
        logText.config(text=logMsgStart)    
    elif msg == "end":                      #   Ja argumets (msg) satur virkni "end",tad parametrs "text=" tiek aizstāts ar logMsgEnd vērtību.   
        logText.config(text=logMsgEnd)      
    elif msg == "clear":                    #   Ja argumets (msg) satur virkni "clear",tad parametrs "text=" tiek aizstāts ar logMsgClear vērtību.
        logText.config(text=logMsgClear)
    else:                                   #   Cita gadijuma parametrs "text=" tiek aizstāts ar logMsgFull vērtību.
        logText.config(text=logMsgFull)

setPoint = []                                   #   Masīva inicializēšana funkcijai getPoint.
#   Funkcija getPoint darbojas pēc analoģijas ar showPosition funkciju 76. rindā.
def getPoint(pos):  
    getX = int(pos.x)                           
    getY = int(pos.y)                           
    if len(setPoint) < 4:                       #   Ja masīva pēdējā elementa vērtība ir mazāka par 4, tad:
        getLog("end")                           
        setPoint.append(getX)                       #   Nākamais masīva elements tiek aizpildīts ar x koordinātas vērtību.
        setPoint.append(getY)                       #   Nākamais masīva elements tiek aizpildīts ar y koordinātas vērtību.

    if len(setPoint) == 4:                      #   Ja masīva pēdējā elementa vērtība ir 4, tad:
        X1 = setPoint[0]                            #   Iegūst sākotnējo X no masīva.
        Y1 = setPoint[1]                            #   Iegūst sākotnējo Y no masīva.
        X2 = setPoint[2]                            #   Iegūst galīgo X no masīva.
        Y2 = setPoint[3]                            #   Iegūst galīgo Y no masīva.
        logResult(X1, Y1, X2, Y2)                   #   Izsauc logResult funkciju ar argumentiem, kas satur koordinātas.
        rootPlotArea.config(cursor="arrow")         #   Atgriež parasto kursoru.
        BrezenhemaAlgoritms(X1, Y1, X2, Y2)         #   Izsauc BrezenhemaAlgoritms funkciju ar argumentiem, kas satur koordinātas.
        rootPlotArea.unbind('<Double-1>')           #   Atvieno notikumu no visas funkcijas.

#   Funkcija Clear aptur animāciju un izdzēš masīvu saturu, atgriež mainīgos to sākotnējā stāvoklī, lai citas funkcijas darbotos pareizi.
def Clear():
    global motion
    global setPoint
    motion = []                         #   Dzēš motion masīva saturu.
    setPoint = []                       #   Dzēš setPoint masīva saturu.
    rootPlotArea.unbind('<Double-1>')   #   Atvieno funkciju no notikuma.
    rootPlotArea.delete("frame")        #   Dzēš visas figūras, kurām ir tags "frame".
    getLog("clear")
    rootPlotArea.delete("toDraw")       #   Dzēš visas figūras, kurām ir tags "toDraw".

#   Close ir funkcija, kas izslēdz aplikāciju.
def Close():
    root.destroy()  #   <loga/vidžeta nosakums>.destroy() aptur loga rādīšanu, tādējādi izslēdzot visus ar to saistītos procesus.

#   Funkcija pickPointFromArea pārbauda masīva stāvokli un saista dubultklikšķa notikumu ar funkciju getPoint.
#   Informācija getPoint funkcijā tiek atjaunināta katru reizi, veicot dubultklikšķi uz objekta ar peles kreiso pogu.
def pickPointFromArea():
    if len(setPoint) == 4:                          #   Ja masīvam jau ir sākuma un beigas punkta koordinātas, izvada brīdinājumu un aptur funkciju.
        getLog("full")
        return
    rootPlotArea.config(cursor="tcross")            #   Maina kursora izskatu uz krustu.
    getLog("start")
    rootPlotArea.bind('<Double-1>', getPoint)       #   Saista dubultklikšķi ar funkciju getPoint. 

#   Funkcija OpenHelp izveido sekundāro logu:
def openHelp():
    helpWin = Toplevel()                            #   Sekundāra loga inicijalizacija ar nosaukumu helpWin.
    helpWin.title('Help: Pogu apraksts')            #   Sekundāra loga nosaukums.
    helpWin.geometry('580x243')                     #   Sekundāra loga izmērs.
    helpWin.resizable(width=False, height=False)    #   Aizslēgt sekundāra loga mērogošanu.
    helpWin['bg'] = '#2a374a'                       #   Sekundāra loga fona krāsa.

    #   Cikls izveido vairākus identiskus Canvas objektus ar atkāpi atkarībā no step koeficienta.
    for i in range(4):
        step = 50 * i
        #   Taisnstūrveida/bloka objekta tika izveidots tādā pašā veidā kā 13. rindā.  
        ttk.Canvas(helpWin, highlightthickness=0, bg='#5159a7', width=560, height=20).place(x=10, y=10+step)
        ttk.Canvas(helpWin, highlightthickness=0, bg='#647abc', width=560, height=20).place(x=10, y=30+step)

    #   Teksta objekts tika izveidots tādā pašā veidā kā 24. rindā.
    ppHeaderText = ttk.Label(helpWin, text='PICK POINT', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    ppInfoText = ttk.Label(helpWin, text='Norādiet trajektorijas sākuma un beigu punktu, noklikšķinot uz ekrāna.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    spHeaderText = ttk.Label(helpWin, text='SET POINT', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    spInfoText = ttk.Label(helpWin, text='Norādiet trajektorijas sākuma un beigu punktu x y koordinātas, noklikšķinot uz ekrāna.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    clHeaderText = ttk.Label(helpWin, text='CLEAR', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    clInfoText = ttk.Label(helpWin, text='Notīrīt trajektorijas ekrāna lauku.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')
    ccHeaderText = ttk.Label(helpWin, text='CANCEL', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    ccInfoText = ttk.Label(helpWin, text='Pārtraukt programmu.', font=('arial', 8, 'bold'), bg='#647abc', fg='#ffffff')

    #   Pogas objekts tika izveidots tādā pašā veidā kā 384. rindā.
    helpOkButton = Button(helpWin, text="OK", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=78, relief='flat', command=helpWin.destroy)

    #   Objekts tika novietots tādā pašā veidā kā 33. rindā.
    ppHeaderText.place(x=255, y=10)
    ppInfoText.place(x=80, y=30)
    spHeaderText.place(x=255, y=60)
    spInfoText.place(x=45, y=80)
    clHeaderText.place(x=262, y=110)
    clInfoText.place(x=190, y=130)
    ccHeaderText.place(x=258, y=160)
    ccInfoText.place(x=215, y=180)
    helpOkButton.place(x=12, y=210)

    #  Sekundāra loga attēlošana cilpās, tāpēc tas tiek rādīts visu laiku, līdz funkcija tiek apturēta.
    helpWin.mainloop()

#   Funkcija openSetPoint izveido sekundāro logu:
def openSetPoint():
    Clear()                                                             #   Notīra konfliktējošos koda elementus.
    setPointWin = Toplevel()                                            #   Sekundāra loga inicijalizacija ar nosaukumu helpWin.
    setPointWin.title("Set point: Trajektorijas koordinātu izvēle")     #   Sekundāra loga nosaukums.
    setPointWin.geometry('280x143')                                     #   Sekundāra loga izmērs.
    setPointWin.resizable(width=False, height=False)                    #   Aizslēgt sekundāra loga mērogošanu.
    setPointWin['bg'] = '#2a374a'                                       #   Sekundāra loga fona krāsa.

    #   Taisnstūrveida/bloka objekts tika izveidots tādā pašā veidā kā 13. rindā.
    xBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7', width=125, height=20)
    xBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7', width=125, height=20)
    yBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7', width=125, height=20)
    yBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#5159a7', width=125, height=20)
    xInputBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8', width=125, height=20)
    xInputBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8', width=125, height=20)
    yInputBlockStart = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8', width=125, height=20)
    yInputBlockEnd = ttk.Canvas(setPointWin, highlightthickness=0, bg='#bacae8', width=125, height=20)

    #   Taisnstūrveida/bloka objekts tika izveidots tādā pašā veidā kā 24. rindā.
    xTextStart = ttk.Label(setPointWin, text='X Sākumpunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    XTextEnd = ttk.Label(setPointWin, text='X Galapunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    yTextStart = ttk.Label(setPointWin, text='Y Sākumpunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    yTextEnd = ttk.Label(setPointWin, text='Y Galapunkts', font=('arial', 8, 'bold'), bg='#5159a7', fg='#ffffff')
    
    #   Izmantojot Tkinter bibliotēku, izveido tukšu vidžetu, kas pieņem informāciju no ievades loga, izmantojot šādus parametrus:
        #   <nosaukums>       - Vecākās loga/vidžeta nosaukums, kurā atrodas objekts.
    enterX1 = ttk.Entry(setPointWin)
    enterX2 = ttk.Entry(setPointWin)
    enterY1 = ttk.Entry(setPointWin)
    enterY2 = ttk.Entry(setPointWin)

    #   Izmantojot Tkinter bibliotēku, izveido ievades logu datu ievadīšanai no tastatūras, izmantojot šādus parametrus:
        #   <skaits>,                       - x koordinātas sākum punkts.
        #   <skaits>,                       - y koordinātas sākum punkts.
        #   window = <vidžeta nosaukums>    - vidžeta nosaukums, kurā tiek glabāta informācija.
    xInputBlockStart.create_window(62, 10, window=enterX1)
    xInputBlockEnd.create_window(62, 10, window=enterX2)
    yInputBlockStart.create_window(62, 10, window=enterY1)
    yInputBlockEnd.create_window(62, 10, window=enterY2)

    #   Funkcija apply iegūt informāciju no ievades lodziņiem.
    #   Ja dati ir ievadīti pareizi, tad funkcija izsauc funkciju BrezenhemaAlgoritms ar argumentiem, kas satur koordinātas. 
    def Apply():
        Clear()                             #   Notīra konfliktējošos koda elementus.
        try:                                #   Pārbauda, ​​vai funkciju var izpildīt.
            x1 = int(enterX1.get())         #   Iegūt x koordinātas sākum punkts.
            y1 = int(enterY1.get())         #   Iegūt y koordinātas sākum punkts.
            x2 = int(enterX2.get())         #   Iegūt x koordinātas gala punkts.
            y2 = int(enterY2.get())         #   Iegūt y koordinātas gala punkts.

            #   Aptur funkciju, ja koordinātas atrodas ārpus animācijas loga.
            if x1 < 0 or x1 > 1100 or y1 < 0 or y1 > 550 or x2 < 0 or x2 > 1100 or y2 < 0 or y2 > 550:
                setPointWin.destroy()       #   <loga/vidžeta nosakums>.destroy() aptur loga rādīšanu, tādējādi izslēdzot visus ar to saistītos procesus.

                #   Parāda paziņojumu par notikušu kļūdu.
                    #   title = '<nosaukums>',  - Paziņojums loga nosaukums.
                    #   message = '<teksts>'    - Teksts, kas satur paziņojums.
                messagebox.showwarning(title='Error', message='Koordinātas nav ievadītas vai ir ievadītas nepareizi. Grafika izmērs ir 1100px uz 550px')
                return
            
            setPointWin.destroy()           #   <loga/vidžeta nosakums>.destroy() aptur loga rādīšanu, tādējādi izslēdzot visus ar to saistītos procesus.
            logResult(x1, y1, x2, y2)       #   Izsauc logResult funkciju ar argumentiem, kas satur koordinātas.
            BrezenhemaAlgoritms(x1, y1, x2, y2)        #   Izsauc BrezenhemaAlgoritms funkciju ar argumentiem, kas satur koordinātas.

        except:                             #   Ja funkcijas izpildes laikā rodas fatāla kļūda, tad:
            setPointWin.destroy()               #   Aizver sekundāro logu

            #   Parāda paziņojumu par notikušu kļūdu.
                #   title = '<nosaukums>',  - Paziņojums loga nosaukums.
                #   message = '<teksts>'    - Teksts, kas satur paziņojums.
            messagebox.showwarning(title='Error', message='Koordinātas nav ievadītas vai ir ievadītas nepareizi. Grafika izmērs ir 1100px uz 550px')

    #   Pogas objekts tika izveidots tādā pašā veidā kā 384. rindā.
    spApplyButton = Button(setPointWin, text="Apply", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=16, relief='flat', command=Apply)
    spCancelButton = Button(setPointWin, text="Cancel", font=('arial', 8, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=16, relief='flat', command=setPointWin.destroy)
    
    #   Objekts tika novietots tādā pašā veidā kā 33. rindā.
    xBlockStart.place(x=10, y=10)
    xBlockEnd.place(x=10, y=60)
    xTextStart.place(x=25, y=10)
    XTextEnd.place(x=30, y=60)
    yBlockStart.place(x=145, y=10)
    yBlockEnd.place(x=145, y=60)
    yTextStart.place(x=160, y=10)
    yTextEnd.place(x=170, y=60)
    xInputBlockStart.place(x=10, y=30)
    xInputBlockEnd.place(x=10, y=80)
    yInputBlockStart.place(x=145, y=30)
    yInputBlockEnd.place(x=145, y=80)
    spApplyButton.place(x=11, y=110)
    spCancelButton.place(x=147, y=110)

    #  Sekundāra loga attēlošana cilpās, tāpēc tas tiek rādīts visu laiku, līdz funkcija tiek apturēta.
    setPointWin.mainloop()  
#endregion

#region Interaktīvas pogas izveide primārajā logā:
#   Izmantojiet Tkinter bibliotēkas Button klasi, lai izveidotu interaktīvās pogas, izmantojot šādus parametrus:
    #   <nosaukums>,                                                - Vecākās loga/vidžeta nosaukums, kurā atrodas objekts.
    #   text = '<tekts>',                                           - Teksts uz pogas.
    #   font = (<'Teksta fonti','Teksta izmērs','Teksta stils'>'),  - Teksta iestatījumi.
    #   bg = '<krāsa>',                                             - Pogas krāsa.
    #   fg = '<krāsa>',                                             - Pogas teksta krāsa.
    #   activebackground = '<krāsa>',                               - Pogas krāsa, kad kursors atrodas uz pogas.
    #   wight = <izmērs>,                                           - Pogas platums,kas ir relatīvs teksta burtu izmēra platumam.
    #   relief = '<režīma nosakumus>',                              - Pogas rāmja režīms.
    #   command = <funkcijas nosaukums>,                            - Funkcijas nosaukums, kuru pēc nospiešanas izsauc attiecīgā poga.
pPointButton = Button(root, text="PICK POINT", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=19, relief='flat', command=pickPointFromArea)
sPointButton = Button(root, text="SET POINT", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=19, relief='flat', command=openSetPoint)
helpButton = Button(root, text="HELP", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=13, relief='flat', command=openHelp)
clearButton = Button(root, text='CLEAR', font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=13, relief='flat', command=Clear)
closeButton = Button(root, text="CLOSE", font=('arial', 16, 'bold'), bg='#f58220', fg='#ffffff', activebackground='#b76b32', width=13, relief='flat', command=Close)

#   <Objekta nosaukums>.place - metode, kas ļauj novietot objektu attiecībā pret vecākā loga/vidžeta x un y koordinātēm.
pPointButton.place(x=80, y=60)
sPointButton.place(x=351, y=60)
helpButton.place(x=622, y=60)
clearButton.place(x=813, y=60)
closeButton.place(x=1004, y=60)
#endregion

#   winUpdate ir funkcija, kas animācijas laikā atjauno primāro logu un tā dinamiskos elementus.
#   Bez šīs funkcijas prioritāte tiek piešķirta animācijas ciklam, kā rezultātā primārais logs nereaģē. ("Not responding") 
def winUpdate():
    root.update()           #  Primārā loga atjaunināšana.
    rootPlotArea.update()   #  Animācijas loga atjaunināšana.
    logBox.update()         #  Paziņojuma loga atjaunināšana.

root.mainloop()             #  Primāra loga attēlošana cilpās, tāpēc tas tiek rādīts visu laiku.