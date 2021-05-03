from guizero import App, Text, Box, CheckBox, Combo, TextBox, PushButton
import notevalues
pew = {
    "C-2": 65.41,
    "C#/Db-2": 69.30,
    "D-2": 73.42,
    "D#/Eb-2": 77.78,
    "E-2": 82.41,
    "F-2": 87.31,
    "F#/Gb-2": 92.50,
    "G-2": 98.00,
    "G#/Ab-2": 103.83,
    "A-2": 110.00,
    "A#/Bb-2": 116.54,
    "B-2": 123.47,
    "C-3": 130.81,
    "C#/Db-3": 138.59,
    "D-3": 146.83,
    "D#/Eb-3": 155.56,
    "E-3": 164.81,
    "F-3": 174.61,
    "F#/Gb-3": 185.00,
    "G-3": 196.00,
    "G#/Ab-3": 207.65}
def get_key(val):
    for key, value in pew.items():
         if val == value:
             return key
def keyfunction():
    if keycombo.value == "C MAJOR":
        songkey = notevalues.CMajor
    if keycombo.value == "D MAJOR":
        songkey = notevalues.DMajor
    if keycombo.value == "Db MAJOR":
        songkey = notevalues.DbMajor
    if keycombo.value == "E MAJOR":
        songkey = notevalues.EMajor
    if keycombo.value == "Eb MAJOR":
        songkey = notevalues.EbMajor
    if keycombo.value == "F MAJOR":
        songkey = notevalues.FMajor
    if keycombo.value == "F#/Gb MAJOR":
        songkey = notevalues.FsGbMajor
    if keycombo.value == "G MAJOR":
        songkey = notevalues.GMajor
    if keycombo.value == "A MAJOR":
        songkey = notevalues.AMajor
    if keycombo.value == "Ab MAJOR":
        songkey = notevalues.AbMajor
    if keycombo.value == "B MAJOR":
        songkey = notevalues.BMajor
    if keycombo.value == "Bb MAJOR":
        songkey = notevalues.BbMajor

    notelist = []
    templist = []
    for item in songkey:
        for item1 in notevalues.tom8:
            if item == item1:
                templist.append(item)
                del templist[1:]
    notelist.extend(templist)
    templist.clear()
    for item in songkey:
        for item1 in notevalues.tom10:
            if item == item1:
                templist.append(item)
                del templist[1:]
    notelist.extend(templist)
    templist.clear()
    for item in songkey:
        for item1 in notevalues.tom12:
            if item == item1:
                templist.append(item)
                del templist[1:]
    notelist.extend(templist)
    templist.clear()

    for item in songkey:
        for item1 in notevalues.tom16:
            if item == item1:
                templist.append(item)
                del templist[1:]
    notelist.extend(templist)
    templist.clear()
    
    a = notelist[0]
    b = notelist[1]
    c = notelist[2]
    d = notelist[3]  
    
    if rescombo.value == "Max":
        topmult = 1.75
        botmult = 1.75
    if rescombo.value == "High":
        topmult = 1.5
        botmult = 1.85
    if rescombo.value == "Med":
        topmult = 1.4
        botmult = 2.0
    if rescombo.value == "Low":
        topmult = 1.2
        botmult = 2.3

    tom8_top.value = str(int(a * topmult)) + " Hz"
    tom8_bottom.value = str(int(a * botmult)) + " Hz"
    tom10_top.value = str(int(b * topmult)) + " Hz"
    tom10_bottom.value = str(int(b * botmult)) + " Hz"
    tom12_top.value = str(int(c * topmult)) + " Hz"
    tom12_bottom.value = str(int(c * botmult)) + " Hz"
    tom16_top.value = str(int(d * topmult)) + " Hz"
    tom16_bottom.value = str(int(d * botmult)) + " Hz"

    tom8_note.value = get_key(a)
    tom10_note.value = get_key(b)
    tom12_note.value = get_key(c)
    tom16_note.value = get_key(d)
    
app = App(title="Drum Tuning Calculator",
          layout="grid",
          width=522)
app.text_size = 18
app.text_color = "black"
app.bg = "#e0dae3"


spacer1 = Box(app,
              grid=[0,0]) 
text = Text(spacer1,  
            text="") # spacer

message = Text(app,
               grid=[0,1,5,1],
               text="select song key:") # select song key

keycombo = Combo(app,
                 grid=[0,2,5,1],
                 width=12,
                 command=keyfunction,
                 options=["C MAJOR",
                          "D MAJOR",
                          "Db MAJOR",
                          "E MAJOR",
                          "Eb MAJOR",
                          "F MAJOR",
                          "F#/Gb MAJOR",
                          "G MAJOR",
                          "A MAJOR",
                          "Ab MAJOR",
                          "B MAJOR",
                          "Bb MAJOR"]) # key dropdown box
spacer2 = Box(app,
              grid=[0,3])
text = Text(spacer2,
            text="")  # spacer

message = Text(app,
               grid=[0,4,5,1],
               text="select desired resonance:") # select desired resonance

rescombo = Combo(app,
                 grid=[0,5,5,1],
                 width=12,
                 command=keyfunction,
                 options=["Max",
                          "High",
                          "Med",
                          "Low"]) # resonance dropdown box

spacer3 = Box(app,
              grid=[0,6]) 
text = Text(spacer3,
            text="")  # spacer

box = Box(app,
          layout="grid",
          border=True,
          width="fill",
          grid=[1,7,4,1]) # output box

message = Text(box,
               grid=[1,0],
               text="NOTE",
               width=9)
message = Text(box,
               grid=[2,0],
               text="TOP HEAD",
               width=13)
message = Text(box,
               grid=[3,0],
               text="BOTTOM HEAD",
               width=13)

tom8_output = Text(box,
                   grid=[0,1],
                   text="8'' tom: ",
                   width=8)
tom8_note = Text(box,
                 grid=[1,1],
                 width=9)
tom8_top = Text(box,
                grid=[2,1],
                width=13)
tom8_bottom = Text(box,
                   grid=[3,1],
                   width=13)

tom10_output = Text(box,
                    grid=[0,2],
                    text="10'' tom: ",
                    width=8)
tom10_note = Text(box,
                  grid=[1,2],
                  width=9)
tom10_top = Text(box,
                 grid=[2,2],
                 width=10)
tom10_bottom = Text(box,
                    grid=[3,2],
                    width=13)

tom12_output = Text(box,
                    grid=[0,3],
                    text="12'' tom: ",
                    width=8)
tom12_note = Text(box,
                  grid=[1,3],
                  width=9)
tom12_top = Text(box,
                 grid=[2,3],
                 width=13)
tom12_bottom = Text(box,
                    grid=[3,3],
                    width=13)

tom16_output = Text(box,
                    grid=[0,4],
                    text="16'' tom: ",
                    width=8)
tom16_note = Text(box,
                  grid=[1,4],
                  width=9)
tom16_top = Text(box,
                 grid=[2,4],
                 width=13)
tom16_bottom = Text(box,
                    grid=[3,4],
                    width=13)


keyfunction()
app.display()


            
