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
        print("This is not the day to either sell or buy property. Your reluctance in spending money on something you accord a lower priority may not be right. A new project will proceed smoothly as you get help from all quarters. Good will power in sticking to the exercise regime will help you in coming back in shape.")
    elif s==2:
        print("Today you may have confidence which may reflect in your way of working. You are in the winning position in terms of opponents and enemies. You may have a good focus on your goals. Health issues may be good. In domestic life try to avoid unnecessary arguments, it may affect your domestic harmony.") 
    elif s==3:
        print("Moneywise, you will find yourself more secure now, than before. Good diet and regular exercise will keep you both physically and mentally robust. You may have to share the burden of domestic chores. Those into buying and selling property must focus on discounts. Completing a challenging task successfully will add to your professional reputation. Those seeking admission in a premier institute are likely to get the call. You may get busy at work and may have to spend time out of town.") 
    elif s==4:
        print("Money will not be a problem for you, so shop till you drop! It may be difficult to make a client accept your views on the professional front. Good physical condition will make strenuous activities, a child’s play. Good returns are foreseen from a rented property. Some of you will need to regain lost ground on the academic front by burning the midnight oil.") 
    elif s==5:
        print("A family youngster may make you proud by his or her achievement. This is a favourable day to seal a property deal. Your professional skills are likely to be acknowledged at work. You will have enough to purchase a major household item. Those planning for higher studies are likely to find the day eventful. ") 
    elif s==6:
        print(" It is time you turned your attention to saving by becoming more careful of your spending. You will be able to give a good account of yourself by solving workplace problems. A few new exercises will benefit those trying to bring specific body parts in shape. A property deal promises to bring in big money. Whatever you have achieved academically, you stand to lose due to sheer negligence.") 
    elif s==7:
        print("Today is a positive day in terms of gains. You may get results with less effort. Your losses may convert into profits with the help of your wisdom. You may plan for higher studies to groom your career. You may donate some amount to a religious place or charity. You may also help needy people. Some investment in intellectual assets may be possible. Students may do better.") 
    elif s==8:
        print("A new source of income is likely to make your financial worries disappear. A change of medication will save those unwell from side effects. Professionally you are assured of whatever is due to you in terms of promotion or increment. Happiness prevails at home, as friends and relatives drop in. ") 
    elif s==9:
        print("On the financial front, a new source of income is likely to be tapped soon that may get your coffers brimming! Successfully completing an assigned job will give you the edge at work. Those down with an ailment will be on the path to full recovery. Spouse may need emotional support, so be there for him or her. There is no need to become big hearted where property is involved.") 
    elif s==10:
        print("Chance to earn big money may present itself to those running their own business. Home remedies come in real handy for those suffering from minor ailments. Some desperate measures on the job front are in the offing, but you will not be affected. Efficiency will be the keyword for homemakers. You can feel apprehensive about an impending course or task, but your fears will be unfounded.") 
    elif s==11:
        print("You may choose to wait for better investment options, before committing your money. New dimensions open up on the professional front as you handle more than one project. Sticking to your exercise regime will begin to show positive results. Homemakers may have their hands full in doing up the house.") 
    elif s==12:
        print("Financially, your position remains sound and opportunities to earn materialise. Adopting a disciplined life and change in lifestyle will help in restoring energy and health. A family business may require new insights and strategies to be restored to its past glory. You will feel quite at home in a new environment") 
    else:
        print("Hey You Sure About The Number")

    next=True if input("\n Shall We Do Again?(Y/N)")=="Y" else False
        
    
