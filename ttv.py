import pyttsx3
import time
import math
import re
import keyboard
#Nombre del libro
libro="MOV.txt"

 
#Segundos que espera entre linea y linea
print("Cuantos segundos debe esperar el programa por cada dictado")
peace= int(input()) #4
#Parrafo en la que iniciará, 1 significará inicio
print("En qué parrafo deseas comenzar?")
parrafo= int(input()) #18
#Linea en la que iniciará, 1 significará inicio
print("En qué linea de dicho parrafo deseas comenzar?")
linea= int(input())#2   

book= open(libro,'r',)#encoding="utf8")
book_text=book.read()

book=open("nuevo"+libro,'w')
book_text=book_text.replace('/',' diagonal ')
book_text=book_text.replace('[',' corchetes-abren ')
book_text=book_text.replace(']',' corchetes-cierran ')
book_text=book_text.replace('(',' parentesis-abren ')
book_text=book_text.replace(')',' parentesis-cierran ')
book_text=book_text.replace('Ã¼','u')
book_text=book_text.replace('Ã¡', 'a')
book_text=book_text.replace('Ã©', 'e')
book_text=book_text.replace('Ã­', 'i')
book_text=book_text.replace('Ã³', 'o')
book_text=book_text.replace('Ãº','u')
book_text=book_text.replace('Ã±','n')

book_text=book_text.replace(';',' punto-coma;')
book_text=book_text.replace(':',' dos-puntos:')
book_text=book_text.replace('...',' puntos-suspensivos.')
book_text=book_text.replace(',',' signo-coma,')
book_text=book_text.replace('"',' comillas",')
book_text=book_text.replace('.\n',' punto-aparte\n')
book_text=book_text.replace('.',' signo-punto.')

 
print(book_text)
book.write(book_text)
book.close()
book=open("nuevo"+libro,'r')
book_text=book.readlines()
engine = pyttsx3.Engine()

engine.setProperty( "rate", 100 )
 

i=1  
habla=""
p=0

def main(book_text,i,habla,p,parrafo,linea):          
    for line in book_text:
        
        p=1  
        something=(i>=parrafo)
        if(something):
            #print(re.split(r"[,.;:]+", line))
            alg=len(line.split())-1
            tamaño=len(re.split(r" ", line))
            modulo=tamaño%3
            if(modulo==1):
                resultado=re.split(r" ", line)+[""]+[""]
            if(modulo==2):
                resultado=re.split(r" ", line)+[""]
            if(modulo==0):
                resultado=re.split(r" ", line)
            habla=""
            y=0
            elet=0
            tamaño=len(resultado)
            for q in range(0,round(tamaño/3)):
                for w in range(0, 3):
                    habla+=resultado[elet]+" "
                    elet+=1
                if(impPart(habla,i,p,linea)):
                    linea=-1
                habla=""
                p+=1
        i+=1

def impPart(habla,i,p,linea):
    if(habla==""):
        habla=""
        return
    pasa=(p>=linea)
    if(pasa):
        linea=0;
        print(habla)
        engine.say(habla)#re.split(r"[,.;:]+", line)[element])           
        engine.runAndWait()
        time.sleep(peace)
        while True:
            if not a.wait:
                break
    
    print(habla)  
    print("Parrafo: ", i," Linea:",p)
    return pasa

class Get(object):
    wait = False
    def do_this(self, e):
        self.wait = not self.wait

a = Get()
keyboard.on_press_key("space", a.do_this)

#def arriba():
#    main
#keyboard.on_press_key("down", main(book_text,parrafo,linea+=1))
#keyboard.on_press_key("up", main(book_text,parrafo,linea-=1))

main(book_text,i,habla,p,parrafo,linea)