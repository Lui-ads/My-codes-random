# o-o

# Normal = o-o
# Curioso = O-O
# Com fome 0-0
# Intrigado o_o & O_O
# Piscando ^-^
# Morto x-x

import os # Para limpar o terminal/cmd
import sys # Para a limpeza
import time # Para o time.sleep()
import select # Para o cronometro

def get_input_with_timeout(prompt, timeout): # Cronometro
    print(prompt, end='', flush=True)
    rlist, _, _ = select.select([sys.stdin], [], [], timeout)
    if rlist:
        return sys.stdin.readline().strip()
    else:
        return None
    
cont=0
os.system('clear')
print('\nNota: Quando ele pedir comida é só escrever algo\naleatório e dar o enter\n\nDe enter para comçar ', end='')
input()
while True:
    try:
        cont+=1
        os.system('clear')
        if cont<7 and cont%2!=0:
            print()
            print("     ^-^ ", end="", flush=True)
            time.sleep(0.3)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush() 
            print("     o-o ", end="", flush=True)
            time.sleep(120) # Tempo para ele fazer algo
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()        
        elif cont<7 or cont%2==0:        
            print()
            print("     ^-^ ", end="", flush=True)
            time.sleep(0.3)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush() 
            print("     O-O ", end="", flush=True)
            time.sleep(60)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()
        elif cont==10:        
            print()
            print("     ^-^ ", end="", flush=True)
            time.sleep(0.3)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()     
            print("     o_o ", end="", flush=True)
            time.sleep(30)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()
        elif cont==15:        
            print()
            print("     ^-^ ", end="", flush=True)
            time.sleep(0.3)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()  
            print("     O_O ", end="", flush=True)
            time.sleep(30)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()             
        elif cont>7 and cont%2!=0:
            print()
            print("     ^-^ ", end="", flush=True)
            time.sleep(0.3)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush() 
            print("     o-o ", end="", flush=True)
            time.sleep(120) # Tempo para ele fazer algo
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()        
        elif cont>7 or cont%2==0:        
            print()
            print("     ^-^ ", end="", flush=True)
            time.sleep(0.3)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush() 
            print("     O-O ", end="", flush=True)
            time.sleep(60)
            sys.stdout.write("\r" + " " * 3 + "\r")
            sys.stdout.flush()     
        elif cont==7 or cont==17 or cont==30:
            
            print()
            print("     0-0 ", flush=True)
            comida = get_input_with_timeout('\nComida: ', 60)
            os.system('clear')
            if not comida:
                break
            elif comida is None:
                break
            elif comida.isdigit() or ',' in comida or '-' in comida or '+' in comida or '/' in comida or '*' in comida:
                break 
            else:
                if cont == 30:
                    cont=0
                    print("\n    ^-^ \n\nObigadu", end="", flush=True)
                    time.sleep(3)
                else:
                    print("\n    ^-^ \n\nObigadu", end="", flush=True)
                    time.sleep(3)
                    continue
                sys.stdout.write("\r" + " " * 3 + "\r")
                sys.stdout.flush()
            
    except:
        break
os.system('clear')
print('\n     x-x\n')




