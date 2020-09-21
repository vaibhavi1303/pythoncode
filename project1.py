next=True
while next==True:
    print('''
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Capricorn
    10) Sagittarius
    11) Aquarius
    12) Pisces
    ''')

    s=int(input("Pick Your No And Press Enter\n"))    
    if s==1:
        print("Aries")
    elif s==2:
        print("Tauras") 
    elif s==3:
        print("Gemini") 
    elif s==4:
        print("Cancer") 
    elif s==5:
        print("Leo") 
    elif s==6:
        print(" Virgo") 
    elif s==7:
        print("Libra") 
    elif s==8:
        print(" Scorpio") 
    elif s==9:
        print("Capricorn") 
    elif s==10:
        print("Sagittarius") 
    elif s==11:
        print("Aquarius") 
    elif s==12:
        print("Pisces") 
    else:
        print("Hey You Sure About The Number")

    next=True if input("\n Shall We Do Again?(Y/N)")=="Y" else False
        
    