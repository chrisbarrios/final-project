# DRUM TUNING CALCULATOR

### INSTALLATION

Dependencies -- [Guizero](https://lawsie.github.io/guizero/)
![guizeroinstall](/images/guizeroinstall.png)

Run the program by opening and running drumtune.py in an IDE or in a terminal window by typing 'python3 ' and dragging the file.
***

## DRUM TUNING OVERVIEW

### Why tune the drums?
For the player, for the instrument, for the song.
<br/>
<br/>
tom note examples<br/>
![tomnotes](/images/tomsizenotes.png)<br/>
<br/>
resonance multipliers<br/>
![restable](/images/restable.png)<br/>
***

## HOW DOES IT WORK
Diagram<br/><br/>
![diagram](/images/diagram.png)<br/>
***
Note variables are assigned a value in Hz: <br/><br/>
![notes](/images/notes.png)<br/>
***
Keys are defined as lists of possible note variables within the realistic possible range: <br/><br/>
![keynotes](/images/keynotes.png)<br/>
***
Tom notes are defined similarly as lists of note variables: <br/><br/>
![tomnotes](/images/tomnotes.png)<br/>
***
The first part of the function chooses the key note list based on the value of the key combo:  <br/><br/>
![keycombo](/images/keycombo.png)<br/>
***
The next part of the function compares the song key list with each tom note list to find common members and transfers the first occurrence to a temp list for later: <br/><br/>
![templist](/images/templist.png)
![templistex](/images/templistex.png)<br/>
<br/>
[SOURCE](https://www.quora.com/How-can-I-do-a-comparison-of-two-lists-in-Python-with-each-value)
[SOURCE](https://www.openbookproject.net/books/bpp4awd/ch04.html)
***
Variables that correspond to the target tom note values are created from the note list: <br/><br/>
![notelist](/images/notelist.png)<br/>
***
The Resonance combo defines the top and bottom head multiplier variables: <br/><br/>
![resmult](/images/resmult.png)<br/>
***
Each tom's top and bottom output value is the product of the target tom note variable and the top and bottom multipliers:  <br/><br/>
![hertzoutput](/images/hertzoutput.png)<br/>
***
To get the note name output to be the actual note name and not the Hz value, I had to use a short function that compares the target note value with the values of a dictionary and outputs the key for the corresponding dictionary value: <br/><br/>
![notename](/images/notename.png)<br/>
![pew](/images/pew.png)<br/>
<br/>
[SOURCE](https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/)
***
