from sources import Gen_functions as gn
import time
import threading as thr

TIEMPO = 10

def sound(stop):
    while(True):
        gn.Functions(TIEMPO,load=False).sine_gen(440)
        if stop():
            break

def main():
    stop_threading = False
    hilo1 = thr.Thread(target=sound,args=(lambda:stop_threading,))
    hilo1.start()
    print("Type F to exit")
    while(True):
        leter = str(input("Frase:  "))
        if leter == "F" or "f":
            stop_threading = True
            print("Exiting...")
            break
        else:
            print("Tecla presionada: ", leter)

if __name__ == "__main__":
    main()