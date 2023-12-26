import tkinter as tk
import re, os, webbrowser
root = tk.Tk()
os.system('pip install tk')
os.system('pip install pyinstaller')
os.system('pip install n2w')
def parse(string:str):
    key = 0
    if(len(string)>1):
        for i in string:
            key += ord(i)
    else:
        key = 379
    return key
def do():
    string = entry.get()
    if(len(string) <= 1):
        entry.insert(0,'MEHUL')
    key  = parse(string)
    key_lbl = tk.Label(root, text='key is the sum of ascii values\n of the name u put in(if lenght of name >=2, else its 379)\n was this info :) or :(?').grid(row = 0, column=11)
    with open('try_me.py', 'w+', encoding='utf-8') as f:
        string1 = '''
import re,n2w
numero_source = {
	 " " : 0,

	 "A" : 1
	 ,

	 "B" : 2
,
	 "C" : 3
,
	 "D" : 4
,
	 "E" : 5
,
	 "F" : 6
,
	 "G" : 7
,
	 "H" : 8
,
	 "I" : 9
,
	 "J" : 10
,
	 "K" : 11
,
	 "L" : 12
,
	 "M" : 13
,
	 "N" : 14
,
	 "O" : 15
,
	 "P" : 16
,
	 "Q" : 17
,
	 "R" : 18
,
	 "S" : 19
,
	 "T" : 20
,
	 "U" : 21
,
     "V" : 22
,
     "W" : 23
,
     "X" : 24
,
    "Y" : 25
,
     "Z" : 26



} 
alphabet_source = [ " " , "A" , "B" , "C" , "D", "E" , "F", "G", "H", "I", "J", "K", "L", "M", "N", "O" ,"P" ,"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
import random as dd__
def doi(st,st1):
    return dd__.randrange(st,st1)
def dencriptx (OOOOO000O00O0O0O0 ,O00OO0O00O000OOOO ):#line:1
    O00O0O0000O0OOO0O =OOOOO000O00O0O0O0 #line:2
    OO0O0OO0OO000O0OO =O00OO0O00O000OOOO #line:3
    OOO00000O00O0O00O =int (OO0O0OO0OO000O0OO )#line:4
    OO0O0000000OO0OOO =O00O0O0000O0OOO0O .upper ()#line:5
    OO0O0OO0O00000OO0 =re .sub (r'[^a-zA-Z]',' ',OO0O0000000OO0OOO )#line:6
    OO00O00OO00OO0O0O =list (OO0O0OO0O00000OO0 )#line:8
    OO00000OOO00O0OO0 =len (OO0O0000000OO0OOO )#line:9
    OO00OOOOOO0OOO0OO =""#line:10
    for OOO0O0OOOOO0OOO0O in OO00O00OO00OO0O0O :#line:11
        OOOO000000O0OOOO0 =numero_source [OOO0O0OOOOO0OOO0O ]#line:13
        OO00000O00OOO0000 =int (OOOO000000O0OOOO0 )#line:14
        O00OOO000O0000OOO =(OO00000O00OOO0000 +OOO00000O00O0O00O -OO00000OOO00O0OO0 )%26 #line:15
        O000OO000O000O000 =alphabet_source [O00OOO000O0000OOO ]#line:16
        OO00000OOO00O0OO0 =OO00000OOO00O0OO0 +1 #line:17
        OO00OOOOOO0OOO0OO +=O000OO000O000O000 #line:18
    return OO00OOOOOO0OOO0OO #line:19
def encriptx (OO00O000OO0OOOO00 ,OO00O0O00O0000OO0 ):#line:20
    OO0OO0OO00OO0OOO0 =OO00O000OO0OOOO00 #line:21
    O0O00OO00OO0OO0O0 =OO00O0O00O0000OO0 #line:22
    OOOOO00OOOO00O0O0 =int (O0O00OO00OO0OO0O0 )#line:23
    OO0OO000O0OO0OO00 =OO0OO0OO00OO0OOO0 .upper ()#line:24
    OOOO0OO00000000OO =re .sub (r'[^a-zA-Z]',' ',OO0OO000O0OO0OO00 )#line:25
    O0OOO0O0O0OOOOOOO =list (OOOO0OO00000000OO )#line:26
    OO00000OO00OOOOOO =len (OO0OO000O0OO0OO00 )#line:27
    OO0OOOO0OOOO000OO =""#line:28
    for O0000000OO0OO0O00 in O0OOO0O0O0OOOOOOO :#line:29
        OOOO0OOOOO0O000O0 =numero_source [O0000000OO0OO0O00 ]#line:30
        O0000O00000OO0OOO =int (OOOO0OOOOO0O000O0 )#line:31
        O0OOO00O0OOOOOO00 =(O0000O00000OO0OOO -OOOOO00OOOO00O0O0 +OO00000OO00OOOOOO )%26 #line:32
        OO00O00OO00OOOO0O =alphabet_source [O0OOO00O0OOOOOO00 ]#line:33
        OO00000OO00OOOOOO =OO00000OO00OOOOOO +1 #line:34
        OO0OOOO0OOOO000OO +=OO00O00OO00OOOO0O #line:35
    return OO0OOOO0OOOO000OO 

loudnclear_nevergonnagiveu_up_never_gonna_let_udown = doi(1,300)
helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog = doi(150,300)
helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog1 = n2w.convert(helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog)
one_more_num = doi(1,150)
ar = [doi(1,300),doi(2,300),doi(2,100),doi(2,200),doi(2,100)]
ar[doi(0,4)] = loudnclear_nevergonnagiveu_up_never_gonna_let_udown
print(ar)
for i in range(1,301):
    if(i == helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog):
            with open(f'{i}.py','w+') as f:
                f.write(f'name = {i}')
                string = \'\'\'
from tkinter import *#line:1
global yo #line:2
global yo0 #line:3
global start_pos #line:4
global end_pos #line:5
def wowy (O0O0000O0O0OO000O ):#line:6
    def OO00OO000OOOOO00O ():#line:7
        O0O0000O00OO00OOO =O00OOOOOO00O0O00O .get ('1.0','end-1c')#line:8
        OOOO00O00000OO000 =str (O0O0OO0O00OOOOO00 .get ())#line:10
        O0O0O0O00OO0O0O00 =0 #line:11
        O0O0OO0OOOOOO000O =len (O0O0000O00OO00OOO )#line:12
        O0OO00OOOOOO0OOOO =len (OOOO00O00000OO000 )#line:13
        for OO00OOOO00OO00000 in range (O0O0OO0OOOOOO000O -O0OO00OOOOOO0OOOO +1 ):#line:15
            for OO00OO0O0OOOOOOOO in range (O0OO00OOOOOO0OOOO ):#line:16
                O00OO000O0O0000O0 =O0O0000O00OO00OOO [OO00OOOO00OO00000 :OO00OOOO00OO00000 +O0OO00OOOOOO0OOOO ]#line:17
                if (O00OO000O0O0000O0 ==OOOO00O00000OO000 ):#line:18
                    O0O0O0O00OO0O0O00 =O0O0O0O00OO0O0O00 +1 #line:19
                    for OOO0O000O0OOO0OOO in range (1 ,O00OOOOOO00O0O00O .count ('1.0','end','displaylines')[0 ]+1 ):#line:20
                        O00OOOO00OOOOO000 =O00OOOOOO00O0O00O .search (OOOO00O00000OO000 ,OOO0O000O0OOO0OOO /10 ,stopindex ='end-1c')#line:21
                        O00O0OO0O0OO0OO0O ='{}+{}c'.format (O00OOOO00OOOOO000 ,len (OOOO00O00000OO000 ))#line:22
                        O00OOOOOO00O0O00O .tag_add ("start",O00OOOO00OOOOO000 ,O00O0OO0O0OO0OO0O )#line:23
                        O00OOOOOO00O0O00O .tag_configure ("start",background ="OliveDrab1",foreground ="Black")#line:24
                        for OO00O00OO00000000 in range (73 ):#line:25
                            try :#line:26
                                O00OOOO00OOOOO000 =O00OOOOOO00O0O00O .search (OOOO00O00000OO000 ,O00O0OO0O0OO0OO0O ,stopindex ='end-1c')#line:27
                                O00O0OO0O0OO0OO0O ='{}+{}c'.format (O00OOOO00OOOOO000 ,len (OOOO00O00000OO000 ))#line:28
                                O00OOOOOO00O0O00O .tag_add ("start",O00OOOO00OOOOO000 ,O00O0OO0O0OO0OO0O )#line:29
                                O00OOOOOO00O0O00O .tag_configure ("start",background ="OliveDrab1",foreground ="Black")#line:30
                            except :#line:33
                                pass #line:34
                    break #line:36
        OO00O0000O0O0O000 =Label (O00000O00O0OO000O ,text =O0O0O0O00OO0O0O00 ,font =('Arial',15 ,'bold')).grid (row =6 ,column =1 )#line:37
    O00000O00O0OO000O =Tk ()#line:42
    O00000O00O0OO000O .title ("Text Find")#line:43
    O00000O00O0OO000O .geometry ("600x500+750+300")#line:44
    O000OO0OO00OO0O0O =Label (O00000O00O0OO000O ,text ="Enter text to be checked:",font =('Arial',15 ,'bold')).grid (row =0 ,column =0 ,columnspan =3 )#line:45
    O00OOOOOO00O0O00O =Text (O00000O00O0OO000O ,width =73 ,height =15 ,wrap =WORD ,padx =10 ,pady =10 )#line:46
    O00OOOOOO00O0O00O .grid (row =1 ,column =0 ,columnspan =3 )#line:47
    O00OOOOOO00O0O00O .insert (END ,str (O0O0000O0O0OO000O ))#line:48
    O0000000O00OO0O0O =Label (O00000O00O0OO000O ,text =" Enter word/phrase to be counted:",font =('Arial',15 ,'bold')).grid (row =2 ,column =0 ,columnspan =3 )#line:49
    O0O0OO0O00OOOOO00 =Entry (O00000O00O0OO000O ,width =25 ,borderwidth =5 )#line:50
    O0O0OO0O00OOOOO00 .grid (row =3 ,column =1 )#line:51
    OOOOOO00OOOO00OOO =Button (O00000O00O0OO000O ,text ="Count!",font =('Arial',15 ,'bold'),command =OO00OO000OOOOO00O )#line:52
    OOOOOO00OOOO00OOO .grid (row =4 ,column =1 )#line:53
    O00000O00O0OO000O .mainloop ()#line:56
\'\'\'''' 
        f.write(string1)
        f.write('\n                f.write(string)\n')
        f.write(f'                f.write("wowy(\'You know what i could give you the key but u can find it out yourself, just resize some windows to get ur answer\')")')
        string2 = '''
            
    else:
        if(i != helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog and i == loudnclear_nevergonnagiveu_up_never_gonna_let_udown):
            with open(f'{i}.py','w+',encoding='utf-8') as f:
                f.write(f'name = {i}')
                string = \'\'\'
from tkinter import *#line:1
global yo #line:2
global yo0 #line:3
global start_pos #line:4
global end_pos #line:5
def crazywrld (O00O0O000OO000O00 ):#line:6
    def O000OOOOOOO0O0O0O ():#line:7
        O00O000OOO0000000 =OOOOO0O00OOO0OOO0 .get ('1.0','end-1c')#line:8
        OO0OO0OOOO0O0OOO0 =str (O0O000000O0O000OO .get ())#line:10
        OO0O0OO000000O0OO =0 #line:11
        O0O00O00OOO000OOO =len (O00O000OOO0000000 )#line:12
        O0O0O0O0000000000 =len (OO0OO0OOOO0O0OOO0 )#line:13
        for OOOO0OO0O00O00O00 in range (O0O00O00OOO000OOO -O0O0O0O0000000000 +1 ):#line:15
            for O0O000OO0O0O00OOO in range (O0O0O0O0000000000 ):#line:16
                O0O00000OOOO00O00 =O00O000OOO0000000 [OOOO0OO0O00O00O00 :OOOO0OO0O00O00O00 +O0O0O0O0000000000 ]#line:17
                if (O0O00000OOOO00O00 ==OO0OO0OOOO0O0OOO0 ):#line:18
                    OO0O0OO000000O0OO =OO0O0OO000000O0OO +1 #line:19
                    for O000OO0O0OOO0OO0O in range (1 ,OOOOO0O00OOO0OOO0 .count ('1.0','end','displaylines')[0 ]+1 ):#line:20
                        O000OO0OO00O0OO00 =OOOOO0O00OOO0OOO0 .search (OO0OO0OOOO0O0OOO0 ,O000OO0O0OOO0OO0O /10 ,stopindex ='end-1c')#line:21
                        OOOOO0000O000OO00 ='{}+{}c'.format (O000OO0OO00O0OO00 ,len (OO0OO0OOOO0O0OOO0 ))#line:22
                        OOOOO0O00OOO0OOO0 .tag_add ("start",O000OO0OO00O0OO00 ,OOOOO0000O000OO00 )#line:23
                        OOOOO0O00OOO0OOO0 .tag_configure ("start",background ="OliveDrab1",foreground ="Black")#line:24
                        for OO00O0OO0OO00O00O in range (73 ):#line:25
                            try :#line:26
                                O000OO0OO00O0OO00 =OOOOO0O00OOO0OOO0 .search (OO0OO0OOOO0O0OOO0 ,OOOOO0000O000OO00 ,stopindex ='end-1c')#line:27
                                OOOOO0000O000OO00 ='{}+{}c'.format (O000OO0OO00O0OO00 ,len (OO0OO0OOOO0O0OOO0 ))#line:28
                                OOOOO0O00OOO0OOO0 .tag_add ("start",O000OO0OO00O0OO00 ,OOOOO0000O000OO00 )#line:29
                                OOOOO0O00OOO0OOO0 .tag_configure ("start",background ="OliveDrab1",foreground ="Black")#line:30
                            except :#line:33
                                pass #line:34
                    break #line:36
        OO0OOOO0OOOO0OO00 =Label (OO000O00O0O0OO0O0 ,text =OO0O0OO000000O0OO ,font =('Arial',15 ,'bold')).grid (row =6 ,column =1 )#line:37
    OO000O00O0O0OO0O0 =Tk ()#line:42
    OO000O00O0O0OO0O0 .title ("Text Find")#line:43
    OO000O00O0O0OO0O0 .geometry ("600x500+750+300")#line:44
    OOOOOO0O0O0O0OO00 =Label (OO000O00O0O0OO0O0 ,text ="Enter text to be checked:",font =('Arial',15 ,'bold')).grid (row =0 ,column =0 ,columnspan =3 )#line:45
    OOOOO0O00OOO0OOO0 =Text (OO000O00O0O0OO0O0 ,width =73 ,height =15 ,wrap =WORD ,padx =10 ,pady =10 )#line:46
    OOOOO0O00OOO0OOO0 .grid (row =1 ,column =0 ,columnspan =3 )#line:47
    OOOOO0O00OOO0OOO0 .insert (END ,str (O00O0O000OO000O00 ))#line:48
    O00OO0O0O0O00OO00 =Label (OO000O00O0O0OO0O0 ,text =" Enter word/phrase to be counted:",font =('Arial',15 ,'bold')).grid (row =2 ,column =0 ,columnspan =3 )#line:49
    O0O000000O0O000OO =Entry (OO000O00O0O0OO0O0 ,width =25 ,borderwidth =5 )#line:50
    O0O000000O0O000OO .grid (row =3 ,column =1 )#line:51
    O0000OOO00OOO00OO =Button (OO000O00O0O0OO0O0 ,text ="Count!",font =('Arial',15 ,'bold'),command =O000OOOOOOO0O0O0O )#line:52
    O0000OOO00OOO00OO .grid (row =4 ,column =1 )#line:53
    OO000O00O0O0OO0O0 .mainloop ()

\'\'\'
                f.write(string)
                f.write('\\ncrazywrld("You dont get it :(, but u do get a thing a thing u dont see yet, nvm i still have a crush on ascii values so keep that in mind, will u remeber me?😔")')
                more = \'\'\'
with open('more.txt','w+') as f:\'\'\'
                f.write(more)
                f.write(f'    f.write("Last time i checked the hint to the key was in {one_more_num}.py")')
                main = \'\'\'
import re,n2w
numero_source = {
	 " " : 0,

	 "A" : 1
	 ,

	 "B" : 2
,
	 "C" : 3
,
	 "D" : 4
,
	 "E" : 5
,
	 "F" : 6
,
	 "G" : 7
,
	 "H" : 8
,
	 "I" : 9
,
	 "J" : 10
,
	 "K" : 11
,
	 "L" : 12
,
	 "M" : 13
,
	 "N" : 14
,
	 "O" : 15
,
	 "P" : 16
,
	 "Q" : 17
,
	 "R" : 18
,
	 "S" : 19
,
	 "T" : 20
,
	 "U" : 21
,
     "V" : 22
,
     "W" : 23
,
     "X" : 24
,
    "Y" : 25
,
     "Z" : 26



} 
alphabet_source = [ " " , "A" , "B" , "C" , "D", "E" , "F", "G", "H", "I", "J", "K", "L", "M", "N", "O" ,"P" ,"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
import random as dd__
def doi(st,st1):
    return dd__.randrange(st,st1)
def dencriptx (OOOOO000O00O0O0O0 ,O00OO0O00O000OOOO ):#line:1
    O00O0O0000O0OOO0O =OOOOO000O00O0O0O0 #line:2
    OO0O0OO0OO000O0OO =O00OO0O00O000OOOO #line:3
    OOO00000O00O0O00O =int (OO0O0OO0OO000O0OO )#line:4
    OO0O0000000OO0OOO =O00O0O0000O0OOO0O .upper ()#line:5
    OO0O0OO0O00000OO0 =re .sub (r'[^a-zA-Z]',' ',OO0O0000000OO0OOO )#line:6
    OO00O00OO00OO0O0O =list (OO0O0OO0O00000OO0 )#line:8
    OO00000OOO00O0OO0 =len (OO0O0000000OO0OOO )#line:9
    OO00OOOOOO0OOO0OO =""#line:10
    for OOO0O0OOOOO0OOO0O in OO00O00OO00OO0O0O :#line:11
        OOOO000000O0OOOO0 =numero_source [OOO0O0OOOOO0OOO0O ]#line:13
        OO00000O00OOO0000 =int (OOOO000000O0OOOO0 )#line:14
        O00OOO000O0000OOO =(OO00000O00OOO0000 +OOO00000O00O0O00O -OO00000OOO00O0OO0 )%26 #line:15
        O000OO000O000O000 =alphabet_source [O00OOO000O0000OOO ]#line:16
        OO00000OOO00O0OO0 =OO00000OOO00O0OO0 +1 #line:17
        OO00OOOOOO0OOO0OO +=O000OO000O000O000 #line:18
    return OO00OOOOOO0OOO0OO #line:19
def encriptx (OO00O000OO0OOOO00 ,OO00O0O00O0000OO0 ):#line:20
    OO0OO0OO00OO0OOO0 =OO00O000OO0OOOO00 #line:21
    O0O00OO00OO0OO0O0 =OO00O0O00O0000OO0 #line:22
    OOOOO00OOOO00O0O0 =int (O0O00OO00OO0OO0O0 )#line:23
    OO0OO000O0OO0OO00 =OO0OO0OO00OO0OOO0 .upper ()#line:24
    OOOO0OO00000000OO =re .sub (r'[^a-zA-Z]',' ',OO0OO000O0OO0OO00 )#line:25
    O0OOO0O0O0OOOOOOO =list (OOOO0OO00000000OO )#line:26
    OO00000OO00OOOOOO =len (OO0OO000O0OO0OO00 )#line:27
    OO0OOOO0OOOO000OO =""#line:28
    for O0000000OO0OO0O00 in O0OOO0O0O0OOOOOOO :#line:29
        OOOO0OOOOO0O000O0 =numero_source [O0000000OO0OO0O00 ]#line:30
        O0000O00000OO0OOO =int (OOOO0OOOOO0O000O0 )#line:31
        O0OOO00O0OOOOOO00 =(O0000O00000OO0OOO -OOOOO00OOOO00O0O0 +OO00000OO00OOOOOO )%26 #line:32
        OO00O00OO00OOOO0O =alphabet_source [O0OOO00O0OOOOOO00 ]#line:33
        OO00000OO00OOOOOO =OO00000OO00OOOOOO +1 #line:34
        OO0OOOO0OOOO000OO +=OO00O00OO00OOOO0O #line:35
    return OO0OOOO0OOOO000OO 
print(dencriptx('ur-code-here'),'encryption key u can guess its a fimiliar number u might have seen in past(filename of this/past/69)')
\'\'\'
                f.write(main)
        elif(i != helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog and i == one_more_num):
            with open(f'{i}.py','w+') as f:
                f.write(f'name = {i}')
                string = \'\'\'
from tkinter import *#line:1
import random
global yo #line:2
global yo0 #line:3
global start_pos #line:4
global end_pos #line:5
def lol (O00O0O000OO000O00 ):#line:6
    def O000OOOOOOO0O0O0O ():#line:7
        O00O000OOO0000000 =OOOOO0O00OOO0OOO0 .get ('1.0','end-1c')#line:8
        OO0OO0OOOO0O0OOO0 =str (O0O000000O0O000OO .get ())#line:10
        OO0O0OO000000O0OO =0 #line:11
        O0O00O00OOO000OOO =len (O00O000OOO0000000 )#line:12
        O0O0O0O0000000000 =len (OO0OO0OOOO0O0OOO0 )#line:13
        for OOOO0OO0O00O00O00 in range (O0O00O00OOO000OOO -O0O0O0O0000000000 +1 ):#line:15
            for O0O000OO0O0O00OOO in range (O0O0O0O0000000000 ):#line:16
                O0O00000OOOO00O00 =O00O000OOO0000000 [OOOO0OO0O00O00O00 :OOOO0OO0O00O00O00 +O0O0O0O0000000000 ]#line:17
                if (O0O00000OOOO00O00 ==OO0OO0OOOO0O0OOO0 ):#line:18
                    OO0O0OO000000O0OO =OO0O0OO000000O0OO +1 #line:19
                    for O000OO0O0OOO0OO0O in range (1 ,OOOOO0O00OOO0OOO0 .count ('1.0','end','displaylines')[0 ]+1 ):#line:20
                        O000OO0OO00O0OO00 =OOOOO0O00OOO0OOO0 .search (OO0OO0OOOO0O0OOO0 ,O000OO0O0OOO0OO0O /10 ,stopindex ='end-1c')#line:21
                        OOOOO0000O000OO00 ='{}+{}c'.format (O000OO0OO00O0OO00 ,len (OO0OO0OOOO0O0OOO0 ))#line:22
                        OOOOO0O00OOO0OOO0 .tag_add ("start",O000OO0OO00O0OO00 ,OOOOO0000O000OO00 )#line:23
                        OOOOO0O00OOO0OOO0 .tag_configure ("start",background ="OliveDrab1",foreground ="Black")#line:24
                        for OO00O0OO0OO00O00O in range (73 ):#line:25
                            try :#line:26
                                O000OO0OO00O0OO00 =OOOOO0O00OOO0OOO0 .search (OO0OO0OOOO0O0OOO0 ,OOOOO0000O000OO00 ,stopindex ='end-1c')#line:27
                                OOOOO0000O000OO00 ='{}+{}c'.format (O000OO0OO00O0OO00 ,len (OO0OO0OOOO0O0OOO0 ))#line:28
                                OOOOO0O00OOO0OOO0 .tag_add ("start",O000OO0OO00O0OO00 ,OOOOO0000O000OO00 )#line:29
                                OOOOO0O00OOO0OOO0 .tag_configure ("start",background ="OliveDrab1",foreground ="Black")#line:30
                            except :#line:33
                                pass #line:34
                    break #line:36
        OO0OOOO0OOOO0OO00 =Label (OO000O00O0O0OO0O0 ,text =OO0O0OO000000O0OO ,font =('Arial',15 ,'bold')).grid (row =6 ,column =1 )#line:37
    OO000O00O0O0OO0O0 =Tk ()#line:42
    OO000O00O0O0OO0O0 .title ("Text Find")#line:43
    OO000O00O0O0OO0O0 .geometry ("600x500+750+300")#line:44
    OOOOOO0O0O0O0OO00 =Label (OO000O00O0O0OO0O0 ,text ="Enter text to be checked:",font =('Arial',15 ,'bold')).grid (row =0 ,column =0 ,columnspan =3 )#line:45
    OOOOO0O00OOO0OOO0 =Text (OO000O00O0O0OO0O0 ,width =73 ,height =15 ,wrap =WORD ,padx =10 ,pady =10 )#line:46
    OOOOO0O00OOO0OOO0 .grid (row =1 ,column =0 ,columnspan =3 )#line:47
    OOOOO0O00OOO0OOO0 .insert (END ,str (O00O0O000OO000O00 ))#line:48
    O00OO0O0O0O00OO00 =Label (OO000O00O0O0OO0O0 ,text =" Enter word/phrase to be counted:",font =('Arial',15 ,'bold')).grid (row =2 ,column =0 ,columnspan =3 )#line:49
    O0O000000O0O000OO =Entry (OO000O00O0O0OO0O0 ,width =25 ,borderwidth =5 )#line:50
    O0O000000O0O000OO .grid (row =3 ,column =1 )#line:51
    O0000OOO00OOO00OO =Button (OO000O00O0O0OO0O0 ,text ="Count!",font =('Arial',15 ,'bold'),command =O000OOOOOOO0O0O0O )#line:52
    O0000OOO00OOO00OO .grid (row =4 ,column =1 )#line:53
    OO000O00O0O0OO0O0 .mainloop ()

\'\'\'
                f.write(string)
                f.write(f'lol("Definitely not here ;) hold up : {encriptx(helloworlducfouiaegwcaiouegoauiecghukgsvliugksucgsukrvgtyusgkog1, dd__.choice([i,loudnclear_nevergonnagiveu_up_never_gonna_let_udown,69]))}")')
                more = \'\'\'
with open('more.txt','w+') as f:\'\'\'
                f.write(more)
                f.write(f'  f.write("Remember what was once here and what now isnt, who did that, maybe he was the answer all along?")')
        else:

            with open(f'{i}.py', 'w+') as f:
                string = \'\'\'
import subprocess
subprocess.run('./try_me.exe')
from tkinter import * 
from tkinter import messagebox 
messagebox.showinfo( "Information","Did u know? By doing this you may make your life harder") 
\'\'\'
                f.write(f'name = {i}')
                f.write(string)


'''
        f.write(string2)

    os.system('python -O -m PyInstaller --onefile try_me.py')
    os.system('rmdir /Q /s build')
    os.system('del "try_me.spec"')
    os.system('del "try_me.py"')
    os.system('ren dist key_also_lies_here')
    with open('key_also_lies_here/more.txt','w+', encoding='utf-8') as f:
        f.write("I used to love ascii values but since you've done this, i dont ☹")
    
    def do_check():
        in_str = entry1.get()
        if(in_str.isalpha == False):
            la1.config(text='U Fail, that too, miserably')
            root.destroy()
            win.destroy()
        else:
            if(int(in_str) == key):
                la1.config(text='u did it')
                la.config(text = 'i believed in u')
                url = 'https://media.tenor.com/lCKwsD2OW1kAAAAj/happy-cat-happy-happy-cat.gif'
                webbrowser.open_new_tab(url)

            else:
                la1.config(text='U Fail, that too, miserably')
                root.destroy()
                win.destroy()
                os.system('rmdir /Q /s key_also_lies_here')
                url = 'https://lingo-apps.com/www/wp-content/uploads/2022/02/no_in_different_languages.png'
                webbrowser.open_new_tab(url)
    win = tk.Tk()
    win.title('iluvasciivalues')
    win.geometry("400x150+750+300")
    la1 = tk.Label(win, text="Enter a key that generated in 10 minutes\n (find hint for hint in files)" ,font=('Times New Roman','12'))
    la1.grid(row=0,column=0,columnspan=2,padx=20,pady=10)
    entry1 = tk.Entry(win, width=50, border=3)
    entry1.grid(row = 1, column=0, columnspan=3, padx=20)
    but1 = tk.Button(win, text='i told u already i luv...., \n nvm,Submit', command=do_check).grid(row=2, column=1,pady=20)
    win.resizable(False, False)
    win.mainloop()
root.title("try ur best")
root.geometry("400x150+750+300")
la = tk.Label(root, text="Enter Your Name: ", font=('Times New Roman','20'))
la.grid(row=0,column=0,columnspan=2,padx=20,pady=10)
entry = tk.Entry(root, width=50, border=3)
entry.grid(row = 1, column=0, columnspan=3, padx=20)
but = tk.Button(root, text='Get Ready!', command=do).grid(row=2, column=1,pady=20)
arr = []
for i in range(500):
    arr.append(tk.Label(root, text="                                                      "))
for i in range(100):
    arr[i].grid(row = 0, column = i+4)
root.resizable(True, False)
root.mainloop()




