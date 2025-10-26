# Lus_op

import time # For time.sleep
import os # For clear the systen
import unicodedata # For text
import random # For lists

# Accountant
cont=0 # To systen
cont2=0 # To systen
contt=0 # To terminal
contt2=0 # To terminal
contp=0 # Folders
contpp=0 #Folders name

# def

# Terminal & Commands
def terminal2():
    terminar=input('--T | ')
    if terminar == 'poweroff':# To turn off systen
        exit='off'
    elif terminar == 'clear':# To clear all
        exit='clear'
    elif terminar == 'exit':# To exit the terminal
        exit='exit'
    elif not terminar: # For empty messages
        exit='terminal'
    elif terminar == 'memory': # To see the memory
        exit='memory'
    elif terminar == 'mkdir': # To create folders
        exit='mkdir'
    elif 'rm -r' in terminar:# To exclude folders
        exit=terminar
    elif terminar == 'ls': # To see folders
        exit='ls' 
    elif terminar == 'write_f1':# To write
        write='write1'
        exit=write
    elif terminar == 'write_f2':# To write
        write='write2'
        exit=write
    elif terminar == 'write_f3':# To write
        write='write3'
        exit=write
    elif terminar == 'wm -w f1':# To delete writing
        write='wr1'
        exit=write
    elif terminar == 'wm -w f2':# To delete writing
        write='wr2'
        exit=write
    elif terminar == 'wm -w f3':# To delete writing
        write='wr3'
        exit=write
    elif terminar == 'print folder_1':# To see folder
        exit='print1'
    elif terminar == 'print folder_2':# To see folder
        exit='print2'
    elif terminar == 'print folder_3':# To see folder
        exit='print3'
    else:
        exit='back'
    time.sleep(1)
    return exit

# Terminal
def terminal():
    time.sleep(0.8)
    print('    |')
    time.sleep(0.8)
    returm=terminal2()
    print('    |')
    time.sleep(0.8)
    print('    |')
    return returm

# To memory
def memory():
    if memory_in_use == MEMORY or memory_in_use > MEMORY:
        full_space='full'
    else:
        full_space='Still have space'
    return full_space

# Memory
MEMORY=11 # Memory is 10 + 1, this 1 is for help the User
memory_in_use=0
# I need to put it to working 

try:
#    Log in
    time.sleep(0.5)
    os.system('clear')
    
    time.sleep(0.8)
    print('.',  end="", flush=True)
    time.sleep(0.5)
    print('.',  end="", flush=True)
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    time.sleep(0.8)
    os.system('clear')
    time.sleep(0.8)
    print('       |         |')
    print('       |         |')
    print('       |   LOS   |')
    print('       |         |')
    print('       +---------+')
    print('   Lui Operating System')
    print()
    time.sleep(5)
    os.system('clear')
    
#   Loading I
    time.sleep(1.5)
    print('  | Loading log in', end="", flush=True)
    print('.',  end="", flush=True)
    time.sleep(0.5)
    print('.',  end="", flush=True)
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('  |')
    time.sleep(0.8)
    os.system('clear')
    time.sleep(0.8)

#   Log in
    you = ''
    im = 0

    while you == '' and im == 0:
        try:
    #       Name 
            while True:
                try:
                    time.sleep(0.9)
                    you=input('    | You\n--> | ')
                    if not you:
                        time.sleep(0.9)
                        print('    | Please enter your name\n    |')
                        time.sleep(0.9)
                    else:
                        time.sleep(0.9)
                        print('    |')
                        break
                except:
                    break
                        
                        
    #      Password
            while True:
                try:
                    time.sleep(0.8)
                    im=input('    | Password\n--> | ')
                    if not im:
                        time.sleep(0.9)
                        print('    | Please enter your password\n    |')
                        time.sleep(0.9)
                    else:
                        time.sleep(0.9)
                        print('    |')
                        time.sleep(0.8)
                        break
                except:
                    break
        except:
            break

        os.system('clear')
        time.sleep(0.8)
        print("    | Log in done")
        time.sleep(1.5)
        print('    | ')
        time.sleep(0.8)

    
#   Loading II
    os.system('clear')
    time.sleep(1)
    print('  | Loading system', end="", flush=True)
    print('.',  end="", flush=True)
    time.sleep(0.5)
    print('.',  end="", flush=True)
    time.sleep(0.5)
    print('.')
    time.sleep(1.1)
    print('  |')
    os.system('clear')
    print('  |\n  | Welcome ' + you)
    time.sleep(1.5)
    print('  |')
    time.sleep(0.8)
    os.system('clear')
    time.sleep(0.8)
    print('    | - Type "Open Manual.pdf" to know what you can do\n    |')
    time.sleep(0.8)
except:
    os.system('clear')
    time.sleep(0.8)
    print('    |')

# system memory
memory_in_use+=2

# RAM
memory_in_use+=1

# User manual (this manual is a folder)
manual=['    |\n' +
        '    | On Systen\n' + 
        '    | - Type "Open Terminal" to use this systen\n' +
        '    | - Type "Open Browser" to use the browser (it is still just a test)\n' + 
        '    |\n' +
        '    | On Terminal\n' +
        '    | - Type "clear" to clear all\n' + 
        '    | - Type "poweroff" to turn off the system\n' +
        '    | - Type "exit" to close the terminal\n' +
        '    | - Type "memory" to see your memory\n' +
        '    | - Type "ls" to view folders\n' +
        '    | - Type "mkdir" to create a folder (this and write uses 1 _ GB of your memory)\n' + 
        '    |     - After creating a folder_1, write "write_f1" to write to your folder at position 1\n' +
        '    |     - After creating a folder_2 write "write_f2" to write to your folder at position 2\n' +
        '    |     - After creating a folder_3 write "write_f3" to write to your folder at position 3\n' +
        '    | - Type "rm -r folder_name" to delete a folder\n' +
        '    |     - If you can, write "wm -w f1" to delete a your write in folder at position 1\n' +
        '    |     - If you can, write "wm -w f2" to delete a your write in folder at position 2\n' +
        '    |     - If you can, write "wm -w f3" to delete a your write in folder at position 3\n' +
        '    | - Type if you can, "print folder_1" to see a your folder at position 1\n' +
        '    | - Type if you can, "print folder_2" to see a your folder at position 2\n' +
        '    | - Type if you can, "print folder_3" to see a your folder at position 3\n' +
        '    |']
memory_in_use+=1

# Folders
Folder_1=[' ']
okay1=0
Folder_2=[' ']
okay2=0
Folder_3=[' ']
okay3=0

#ls
ls=[]
ls.append('Manual.pdf')

# Systen
action_done='' # For security
while True:
    try:
#       Systen       
        if action_done == 'terminal' or action_done == 'back':
            response=terminal
        else:    
            space=memory()
            if space == 'full':
                memory_in_use=10
                action='full'
            else:
                action=input('--> | ')
                time.sleep(0.8)
                print('    |')
                time.sleep(0.8)
                
#               Alert
                if memory_in_use >=8:
                    print('  ! | Memory almost full')
                else:
                    next
                    
# Leave the sentence in lowercase and without accents        
        try:
            action_done = action.lower() 
            action_done = unicodedata.normalize('NFD', action_done)
            action_done = ''.join(c for c in action_done if unicodedata.category(c) != 'Mn')
        except:
            os.system('clear')
            time.sleep(0.8)
            print('    | Error')
#       Systen    
        if action_done == 'open manual.pdf': # To manual     
            try:
                cont=0 
                cont2=0  
                time.sleep(0.8)
                response=random.choice(manual)
            except:
                response='    | Non-existing folder'
        elif action_done == 'terminal': # To terminal
            cont=0 
            cont2=0  
            response=terminal()
        elif action == 'full':
            response = '  ! | Memory full'
        elif not action: # For empty messages
            cont2=0
            cont+=1
            if cont==1:
                response='    | No action taken'
            else:
                response='    | No action taken again'
        elif action_done == 'break':
            break
        else: # For actions not found
            cont2+=1
            if cont2==1:
                response='    | Action not found'
                
            else:
                response='    | Action not found again'

#       Response and terminal
        if response == 'clear': # To clear all
            contt=0
            contt2=0
            time.sleep(0.8)
            os.system('clear')
            action_done='terminal'
        elif response == 'back': # To back terinal1
            contt=0
            contt2+=1
            if contt2==1:
                print('  T | Command not found')
                action_done='back'
                continue
            else:
                print('  T | Command not found again')
                action_done='back'
                continue        
        elif response == 'terminal': # To back terinal2
            action_done ='terminal'
            contt2=0
            contt+=1
            if contt==1:
                print('  T | Empty line')
                continue
            else:
                print('  T | Empty line again')
                continue      
        elif response == 'exit':# To exit the terminal
            contt2=0
            contt0=0
            action_done=''
        elif response =='off':# To turn off systen
            time.sleep(0.8)
            print('    |')
            time.sleep(1)
            print('    | Shutting down the system', end="", flush=True)
            print('.',  end="", flush=True)
            time.sleep(1)
            print('.',  end="", flush=True)
            time.sleep(1)
            print('.')
            time.sleep(0.5)
            time.sleep(0.8)
            print('    |')
            time.sleep(1.5)
            print('    |')
            os.system('clear')
            break
        elif response == 'memory':# To see the memory
            print('    | You have 10 _ GB and you used', memory_in_use, '_', 'GB')
        elif response == 'mkdir':# To create folders
            contp+=1
            if memory_in_use < 11 and contp<=3:
                contpp+=1
                memory_in_use+=1
                ls.append(f'Folder_{contpp}')
            else:
                if memory_in_use == 11:
                    memory_in_use=10
                    print('  ! | Memory full')
                else:
                    print("    | You can't create more folder")              
        elif response.startswith('rm -r'): # To exclude folders
            delete=response[6:]
            try:
                if delete == 'Manual.pdf':
                    memory_in_use=memory_in_use-1
                    ls.pop(0)
                    c=len(ls)
                    contp=c
                    ls.insert(0, '')
                    del manual   
                else:
                    ls.remove(delete)
                    memory_in_use=memory_in_use-1
                    c=len(ls)-1
                    contp=c
            except:
                print('    | There is no folder with that name!')            
        elif response =='ls':# To view folders
            print('    |', ' '.join(ls))           
        elif response == 'write1':# To write
            memory_in_use+=1
            if memory_in_use <= 11:
                w1=input('-T\w| ')
                Folder_1.append(w1)
            else:
                print('  ! | Memory full')
                memory_in_use=10
                time.sleep(1)
                print('    |')
                time.sleep(1)
                print("  ! | You can't write more")   
        elif response == 'write2':# To write
            memory_in_use+=1
            if memory_in_use <= 11:
                w2=input('-T\w| ')
                Folder_2.append(w2)
            else:
                print('  ! | Memory full')
                memory_in_use=10
                time.sleep(1)
                print('    |')
                time.sleep(1)
                print("  ! | You can't write more") 
        elif response == 'write3':# To write
            memory_in_use+=1
            if memory_in_use <=11:
                w3=input('-T\w| ')
                Folder_3.append(w3)
            else:
                print('  ! | Memory full')
                memory_in_use=10
                time.sleep(1)
                print('    |')
                time.sleep(1)
                print("  ! | You can't write more") 
        elif response == 'wr1':# To delete writing
            try:
                memory_in_use-=1
                po1=int(input('    | Which text do you want to delete:\n    | '))
                Folder_1.pop(po1)
            except:
                print('    |')
                time.sleep(1)
                print('    | There is nothing to delete')
                next
        elif response == 'wr2':# To delete writing
            try:
                memory_in_use-=1
                po2=int(input('    | Which text do you want to delete:\n    | '))
                Folder_2.pop(po2)
            except:
                print('    |')
                time.sleep(1)
                print('    | There is nothing to delete')
                next
        elif response == 'wr3':# To delete writing
            try:
                memory_in_use-=1
                po3=int(input('    | Which text do you want to delete:\n    | '))
                Folder_3.pop(po3)
            except:
                print('    |')
                time.sleep(1)
                print('    | There is nothing to delete')
                next
        elif response == 'print1':# To see folder
            print('   | '.join(Folder_1))
        elif response == 'print2':# To see folder
            print('   | '.join(Folder_2))
        elif response == 'print3':# To see folder
            print('   | '.join(Folder_3))
        else: # Response
            time.sleep(0.9)
            print('    |')
            time.sleep(0.8)
            print(response)
            time.sleep(0.9)
            print('    |')
            time.sleep(0.8)
            
    except:
        print()
        break
if action_done != 'break':
    try:        
        time.sleep(1)
        print('    |')
        time.sleep(0.9)
        print('    |')
        time.sleep(1)
        print('    | System off')
        time.sleep(0.9)
        print('    | ')
        time.sleep(0.9)
        print('    +-------------\n')
    except:
        end=0
else:
    next