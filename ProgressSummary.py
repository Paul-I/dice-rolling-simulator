# while True: this is just to be able to roll the dice again and again, as many as you want, without while True you can only roll once.
while True:
# import random is just telling the computer what you are doin.
    import random
    from os import system

# print is just to displaying something you want the computer to show.
    print ("This is a dice rolling program")
    print ("Press the enter button to roll")
 input is telling the computer what to do when you something.
    cmd = raw_input ("Enter to run, q to quit")
    system("cls")

# number random.randint is tell the computer how many choice it or it should choice between this range. Basically it instruction for the computer.#3

    number=random.randint(1,6)
# "if" is that when it choose the number after this == it should show what you set it to show.
    if number==1:
        print"[------------]"
        print"[            ]"
        print"[      O     ]"
        print"[            ]"
        print"[------------]"
    if number==2:
        print"[------------]"
        print"[            ]"
        print"[   O    O   ]"
        print"[            ]"
        print"[------------]"
    if number==3:
        print"[------------]"
        print"[   O        ]"
        print"[     O      ]"
        print"[       O    ]"
        print"[------------]"
    if number==4:
        print"[------------]"
        print"[   O    O   ]"
        print"[            ]"
        print"[   O    O   ]"
        print"[------------]"
    if number==5:
        print"[------------]"
        print"[   O    o   ]"
        print"[     O      ]"
        print"[   O    O   ]"
        print"[------------]"
    if number==6:
        print"[------------]"
        print"[   O     O  ]"
        print"[   O     O  ]"
        print"[   O     O  ]"
        print"[------------]"
