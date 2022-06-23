import serial
from time import sleep

def main():
    PuertoSerie = serial.Serial('COM3', 115200)
    sleep(1)
    print("start")
    for i in range(0,500):
        sArduino = PuertoSerie.readline()
        print("Valor Arduino: ", sArduino)
        print("***************")

if __name__ == "__main__":
    main()