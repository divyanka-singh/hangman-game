import random
def hangman():
    list_of_words = ['forget','borrow','lend','wait','write','forest','struggle','reply','depend','repent','certificate','change','thought','resign','start','smile','drink','matter','sleep','speak','respect','shout','learn','progress','shine','spoil','remember','prepare','improve','fight','think','search','praise','break','abuse','return','finish','refuse','exercise','study','promise','threaten','allow','independent','favour','establish','divide','sacrifice','happen','doubt','enjoy','complete','listen','pretend','thunder','govern','retire','decide','suffer','demand','disturb','request','defeat','discuss','calculate','recognise','punish','distribute','exploit','remove','encourage','select','insult','invite','force','arrest','repair','irrigate','answer','advise','travel','swell','swing','slide','shrink','creep','bless','cling','climb','arrive','become','begin','abide','awake','behold','bleed','burst','drive','dwell','elect','forbid','forgive','freeze','grind','hang','prove','quit','shake','spread','spring','stick','strike','understand','upset','laptop']
    word = random.choice(list_of_words)
    print(word)
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        main_word = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "
        if main_word == word:
           print(main_word)
           print("you won!!!!")
           break


        print("guess the words ", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()
        
        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left!!!")
                print("---------------")
            if turns == 8:
                print("8 turns left!!!")
                print("---------------")
                print("       O       ")
            if turns == 7:
                print("7 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns == 6:
                print("6 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns == 5:
                print("5 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 4:
                print("4 turns left!!!")
                print("---------------")
                print("      \O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 3:
                print("3 turns left!!!")
                print("---------------")
                print("      \O/      ")
                print("       |       ")
                print("      / \      ")
            if turns == 2:
                print("2 turns left!!!")
                print("---------------")
                print("      \O/ |    ")
                print("       |       ")
                print("      / \      ")   
            if turns == 1:
                print("Only 1 turns left!!! Hangman on his last breath")
                print("---------------")
                print("      \O/_|    ")
                print("       |       ")
                print("      / \      ")   
            if turns == 0:
                print("you losse")
                print("you let a good man die")
                print("---------------")
                print("       O_|     ")
                print("      /|\      ")
                print("      / \      ")  
                break

name = input("INTER YOUR NAME -> ")
print("Welcome",name,"!")
print("-------------------------------------------")
print("Try to guess the word in less than 10 attampts")
hangman()
