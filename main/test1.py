import micropython
import machine
import time
import json



with open("assets/kbDict.json") as f:
    kbDict = json.load(f)


f.close()

kb_lc_cols = [["q","e","r","u","o"],
              ["w","s","g","h","l"],
              ["%","d","t","y","i"],
              ["a","p","^","{","<"],
              [">","x","v","b","$"],
              [" ","z","c","n","m"],
              ["&","^","f","j","k"]]


colPins = [14,3,8,9,11]
rowPins = [15,16,17,18,40,41,39]

cols = [  # , machine.Pin.PULL_UP),#    # , machine.Pin.PULL_DOWN),
    machine.Pin(colPins[0], machine.Pin.IN, machine.Pin.PULL_UP),
    machine.Pin(colPins[1], machine.Pin.IN, machine.Pin.PULL_UP),
    machine.Pin(colPins[2], machine.Pin.IN, machine.Pin.PULL_UP),
    machine.Pin(colPins[3], machine.Pin.IN, machine.Pin.PULL_UP),
    machine.Pin(colPins[4], machine.Pin.IN, machine.Pin.PULL_UP)]
  
rows = [
    machine.Pin(rowPins[0], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
    machine.Pin(rowPins[1], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
    machine.Pin(rowPins[2], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
    machine.Pin(rowPins[3], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
    machine.Pin(rowPins[4], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
    machine.Pin(rowPins[5], machine.Pin.IN),#, machine.Pin.PULL_DOWN),
    machine.Pin(rowPins[6], machine.Pin.IN)]#, machine.Pin.PULL_DOWN)]

rowPinsa  = []

for row in rows:
    rowPinsa.append(row)

# print(rowPinsa)

def handle_KB_Pressed_Row(row):
    row.irq(handler=None)
    whatKey(row)
#    start = time.ticks_cpu()
    
#     rowCount = rowPinsa.index(row)
#     rowCount = rowCount
#     
#     print()
#     #print("Rowpin: " + str(p))
#     #rowS = str(row)
#     #rowCount = int(rowS[5:-1])
#     #rowPins.index(rowCount)
#     colCount = 1
#     for col in cols:
#         colCount += 1
#         if(col.value()):
#             print(rowCount)
#             print(colCount)
#             print(kb_lc_cols[rowCount][colCount])
#             #print(kb_lc_cols[int(rowS[5:-1])][colCount])
#             #whatKey(row,col)
# #            print("Time to find " + str(time.ticks_cpu() - start))
#             break

def whatKey(row):
    #start = time.ticks_cpu()
    rowCount = rowPinsa.index(row)
    rowCount = rowCount
    colCount = 1
    for col in cols:
        colCount += 1
        if(col.value()):
            #print(rowCount)
            #print(colCount)
            print(kb_lc_cols[rowCount][colCount])
            #print(kb_lc_cols[int(rowS[5:-1])][colCount])
            #whatKey(row,col)
            #print("Time to find " + str(time.ticks_cpu() - start))
            break
    print("Still Here which is good")
    time.sleep(0.5)
    row.irq(handler=handle_KB_Pressed_Row, trigger=machine.Pin.IRQ_FALLING)

for row in rows:
    row.irq(handler=handle_KB_Pressed_Row, trigger=machine.Pin.IRQ_FALLING)


# 
# 
# def handle_KB_Pressed(p):
#     print("Colpin: " + str(p))
#     start = time.ticks_cpu()
#     
#     
#     whatKey("","pin(0)")
#     colCount = 0
#     for col in cols:
#         colCount += 1
#         if(col == p):        
#             rowCount = 0
#             for i in rows:
#                 rowCount += 1
#                 if(i.value()):
#                     lastrow = str(rowCount)
#                     lastcol = str(colCount)
#                     print(f"key: {kbDict["LowerCase"][lastrow][lastcol]}")
#                     print("Time in one row " + str(time.ticks_cpu() - start))
#         print("Time in one col " + str(time.ticks_cpu() - start))
#         start = time.ticks_cpu()
#     print(time.ticks_cpu() - start)
#     start = time.ticks_cpu()
#         #micropython.schedule(handle_button_press, pin)       
# 
