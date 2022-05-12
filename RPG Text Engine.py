# TO DO:
# - Test for bugs

global adventurers
adventurers=[]
points=10

import time
import sqlite3
connect=sqlite3.connect('Database.db')
cursor=connect.cursor()

from random import seed
from random import randint


monstBeaten=0
monstBeatenFormula=0

class template:
    name=""
    career=""
    HP=""
    strength=""
    magic=""
    defence=""
    level=""
    exp=0
    adventID=0
    classDescription=""

    def __init__(self,nam, level):
        self.level=level
        self.name=nam
        self.career=self.stats[0]
        adventurers.append(nam)
        for i in adventurers:
            self.adventID=self.adventID+1
        print(self.adventID)
        print('\n\nAdventurer number',self.adventID,self.name,'joins the fray!')
        print('number of adventurers:',len(adventurers))
        self.HP=self.stats[1]+(self.level*self.growth[1])
        self.strength=self.stats[2]+(self.level*self.growth[2])
        self.magic=self.stats[3]+(self.level*self.growth[3])
        self.defence=self.stats[4]+(self.level*self.growth[4])
        self.exp=0
        print('\nName:',self.name,'\nLevel:',self.level,'\nEXP:', self.exp,'\nCareer:',self.career,'\nHP:', self.HP, '\nStrength:',self.strength,'\nMagic:',self.magic,'\nDefence:',self.defence)
        print('Special Move:',self.specialname,self.specialdescription)
        self.specialused=1
        self.classDescription=self.stats[5]
        
    def levelup(self):
        self.level=self.level+1
        time.sleep(0.5)
        print('\n----------\n'+self.name,'levels up')
        self.HP=self.stats[1]+(self.level*self.growth[1])
        self.strength=self.stats[2]+(self.level*self.growth[2])
        self.magic=self.stats[3]+(self.level*self.growth[3])
        self.defence=self.stats[4]+(self.level*self.growth[4])
        print('\nLevel:',self.level,'\nHP:', self.HP, '\nStrength:',self.strength,'\nMagic:',self.magic,'\nDefence:',self.defence,'\n')
        global points
        points=points+self.level
        print('\n\nPoints:',points)

class warrior(template):    # By putting a previously defined class between brackets, the new class gains all of its code as well as its own
    stats='Warrior',12,12,1,4,'Powerful warriors with strong physical attacks, but weak magic attacks\nTheir special attack outputs huge damage\n'
    growth='Null', 4,4,1,3
    specialname='titanic rage'
    def special(self):
        print(self.name,'unleashes', self.specialname)
        print('The monster takes huge damage!')
        y.HP=y.HP-(self.strength+self.strength)
        print(y.HP)
        self.specialused=self.specialused-1
    classDescription=stats[5]
    specialdescription="(Single use: deals double damage)"

class wizard(template):
    stats='Wizard',8,4,11,10, 'Crafty wizards who excel at magic attacks, though lack physical prowess\nTheir special heals the party based on level\n'
    growth='Null', 3,1,5,2
    specialname='healing winds'
    def special(self):
        print(self.name,'unleashes', self.specialname)
        print(A.HP,B.HP,C.HP)
        for i in [A,B,C]:
            i.HP=i.HP+self.level+5
        print(A.HP,B.HP,C.HP)
        self.specialused=self.specialused-1
    classDescription=stats[5]
    specialdescription="(Single use: adventurers recover HP equal to 5 + wizard's level)"

class urchin(template):     # THINK OF OTHER CLASSES TO ADD :D
    stats='Urchin',9,3,2,3, "Though weak initially, they quickly become stronger upon levelling up!\nTheir special grants the user exp based on the party's levels\n"
    growth='Null', 5,3,3,2
    specialname='crafty opportunist'
    def special(self):
        print(self.specialname,'-',self.name,'studies the battlefield...')
        x=self.level+y.difficulty+3
        print(self.name,'gains',x,'exp!')
        self.exp=self.exp+x
        self.specialused=self.specialused-1
    classDescription=stats[5]
    specialdescription="(Single use: the user gains exp based on the enemy's difficulty)"
      
# -------------------------------------------------------

print('\nWelcome to RolePlayinG Python Game!')
time.sleep(1)
print('\n\nWho would you like the join your 3 person party?\n\n')
time.sleep(1)
print('----------------------------------------')
print('Warrior:',warrior.classDescription)
time.sleep(1)
print('Wizard:',wizard.classDescription)
time.sleep(1)
print('Urchin:',urchin.classDescription)
time.sleep(1)
print('----------------------------------------')
time.sleep(1)

global namenew

def createA():  # 
    print('\n\nWho will join the party? (First person)')
    namenew=input('name? ')
    if namenew=="":
        createA()
    classnew=input('Class? (warrior, wizard, urchin): ') 
    classnew=classnew.lower()
    try: levelnew=int(input('Level? '))
    except: levelnew=int(input('Level? (integers only)'))
    global A
    if classnew == 'wizard':
        A=wizard(namenew,levelnew)
    elif classnew == 'warrior':
        A=warrior(namenew,levelnew)
    elif classnew == 'urchin':
        A=urchin(namenew,levelnew)
    else:
        print('Class not recognised')
        createA()
        time.sleep(1)

def createB():
    print('\n\n--------\n\nWho will join the party? (Second person)')
    namenew=input('name? ')
    if namenew=="":
        createB()
    classnew=input('Class? (warrior, wizard, urchin): ')
    classnew=classnew.lower()
    try: levelnew=int(input('Level? '))
    except: levelnew=int(input('Level? (integers only)'))
    global B
    if classnew == 'wizard':
        B=wizard(namenew,levelnew)
    elif classnew == 'warrior':
        B=warrior(namenew,levelnew)
    elif classnew == 'urchin':
        B=urchin(namenew,levelnew)
    else:
        print('Class not recognised')
        createB()
        time.sleep(1)

def createC():
    print('\n\n--------\n\nWho will join the party? (Third person)')
    namenew=input('name? ')
    if namenew=="":
        createC()
    classnew=input('Class? (warrior, wizard, urchin): ')
    classnew=classnew.lower()
    try: levelnew=int(input('Level? '))
    except: levelnew=int(input('Level? (integers only)'))
    global C
    if classnew == 'wizard':
        C=wizard(namenew,levelnew)
    elif classnew == 'warrior':
        C=warrior(namenew,levelnew)
    elif classnew == 'urchin':
        C=urchin(namenew,levelnew)
    else:
        print('Class not recognised, please try again.')
        createC()
        time.sleep(1)
        
createA()
createB()
createC()
time.sleep(1)

# -----------------------------------

print('\n\n------\nYour party consists of:\n')
time.sleep(1)
print(A.name,'-',A.career)
time.sleep(1)
print(B.name,'-',B.career)
time.sleep(1)
print(C.name,'-',C.career)
time.sleep(1)
print('\nI wonder what they will find on their journey...')
time.sleep(1)
print('\n----------------------\n')
time.sleep(1)
# ------------------------------------------------

class monster():
    def __init__(self,name,species,title):
        self.name=name
        self.species=species
        self.title=title
        cursor.execute("""
            select id,difficulty,strength,defence,specialDefence,attackquantity,flavourText,baseexpgiven from MonsterStats order by random() limit 1 
            """)
        connect.commit()
        x=cursor.fetchall()
        for a,b,c,d,e,f,g,h in x:
            self.instanceID=a
            self.difficulty=b
            self.strength=c+monstBeatenFormula+self.difficulty
            self.defence=d+monstBeatenFormula
            self.specialDefence=e+monstBeatenFormula
            self.attackquantity=f
            self.flavourtext=g
            self.expgiven=int(h+monstBeatenFormula)
        self.maxHP=20+(self.difficulty**2)+monstBeatenFormula+(A.level**2)+(B.level**2)+(C.level**2)
        self.HP=self.maxHP

def GenerateMonster():
    global y
    global RandMonsterName
    global RandMonsterTitle
    global RandMonsterSpecies
    cursor.execute("""
        select name from MonsterDetails order by random() limit 1 
        """)
    connect.commit()
    x=cursor.fetchall()
    for i in x:
        RandMonsterName=i[0]

    cursor.execute("""
        select title from MonsterDetails order by random() limit 1 
        """)
    connect.commit()
    x=cursor.fetchall()
    for i in x:
        RandMonsterTitle=i[0]

    cursor.execute("""
        select species from MonsterDetails order by random() limit 1 
        """)
    connect.commit()
    x=cursor.fetchall()
    for i in x:
        RandMonsterSpecies=i[0]
    y=monster(RandMonsterName,RandMonsterSpecies,RandMonsterTitle)
    print('A new monster appears!\n')
    #time.sleep(1)

GenerateMonster()

# ------------------------------------------------------------------------

def victory():
    print('Victory!\n')
    global monstBeaten
    global monstBeatenFormula
    monstBeaten=monstBeaten+1
    monstBeatenFormula=monstBeaten**2
    x=[A,B,C]
    for i in x:
        expToLevelUp=9+(i.level**2)  
        i.exp=int(i.exp+y.expgiven) 
        time.sleep(0.5)
        print(i.name, 'gained experience! New experience:',i.exp,'\n')
        while i.exp>=expToLevelUp:
            i.exp=i.exp-expToLevelUp
            i.levelup()
    print('-------------\n')
    time.sleep(0.5)
    GenerateMonster()
    #time.sleep(1)

# -------------------------------------------------------------

def gameOver():
    print('Everyone in your party is dead!\n ---Game Over---\n\n Points:',points,'\n-------------')

def monsterAttack():
    for i in range(0,y.attackquantity):
        time.sleep(1)
        monsterAttackA=int(y.strength/A.defence)+1
        monsterAttackB=int(y.strength/B.defence)+1
        monsterAttackC=int(y.strength/C.defence)+1
        print('\n' +y.name+' attacks the party!') 
        print('\n')
        print(A.name,'took',monsterAttackA,'damage!\n')
        time.sleep(1)
        print(B.name,'took',monsterAttackB,'damage!\n')
        time.sleep(1)
        print(C.name,'took',monsterAttackC,'damage!\n')
        time.sleep(1)
        A.HP=A.HP-monsterAttackA
        B.HP=B.HP-monsterAttackB
        C.HP=C.HP-monsterAttackC
    if y.attackquantity==0:
        print('The monster is too nervous to attack!')

        
        if A.HP>0:          # CHECK THIS PARA WORKS to show someone is dead; ALSO, REWRITE AS: x = [A,B,C], for i in x: print blah blah... ?
            print(A.name, 'has',A.HP,'HP left!')
        else:
            print(A.name, 'is dead!')
        if B.HP>0:
            print(B.name,'has',B.HP,'HP left!')
        else:
            print(B.name, 'is dead!')
        if C.HP>0:
            print(C.name, 'has',C.HP,'HP left!')
        else:
            print(C.name, 'is dead!')
        if A.HP<=0:                     
            if B.HP<=0:
                if C.HP<=0:
                    gameOver()

# -------------------------------------------------------------

def fightTurn():
    time.sleep(2)
    print('\n'+y.name,y.title, '(' + y.species + ') is sizing you up!')
    print(y.HP,'HP remaining\n')
    time.sleep(0.5)
    x=[A,B,C]
    global points
    for i in x:
        if y.HP >0:
            print('\n-------\n\n')
            print(i.name +"'s turn")
            time.sleep(1)
            if y.HP>=1:
                if i.HP >0:          
                    print('\nWhat will', i.name,'('+i.career+',', str(i.HP)+'HP remaining) do?\n\n\n> Attack?\n> Magic Attack?\n> Special? Uses:',i.specialused,'\n> Spend Points? Points:',points,'\n')   
                    decision=input()
                    decision=decision.lower()
                    print('\n')
                    if decision=='attack':
                        print('\n\n'+i.name,'the',i.career,'roars with wild might and launches a vicious attack!')
                        print(y.name,'takes',i.strength,'damage!\n')
                        y.HP=y.HP-i.strength
                        if y.HP>0:
                            print(y.name,'has',y.HP,'HP left!\n')
                    elif decision=='magic attack':
                        print('\n\n'+i.name,'breaths deeply and unleashes a magical attack!',y.name,'takes',i.magic,'damage!\n')
                        y.HP=y.HP-i.magic
                        if y.HP>0:
                            print(y.name,'has',y.HP,'HP left!')
                    elif decision=='special':
                        if i.specialused>0:
                            i.special()
                        else:
                            print(i.name, 'wanted to use their special, but has already used it! (spend points to buy more uses)\n')
                    elif decision =='spend points':
                        if points >=5:
                            print('\n')
                            print(i.name,'spent 5 points!')
                            points=points-5
                            i.specialused=i.specialused+1
                            print(i.name,'is filled with power! They can use their special',i.specialused,'more time(s)')
                            print(points,'points left')
                        else:
                            print('Not enough points!')
                    else:
                        print(i.name,'bungled their opening!\n\n\n--------------\n\n')
                    time.sleep(0.5)
    if y.HP<1:
        print('\n      ',y.name,'was defeated!\n')
        points=points+y.difficulty
        print('Points:',points,'\n--------\n')
        victory()
    else:
        monsterAttack()
        fightTurn()
while True:
    x=A.HP+B.HP+C.HP
    if x>0:
        fightTurn()
