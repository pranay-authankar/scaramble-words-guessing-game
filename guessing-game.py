def scramble_words_game():
    word1 = "aeroplane"
    scrm1 = ["erplaoena", "arlaeneop", "eraoelapn"]
    hint1 = ["Aviation", "Flies in the sky", "Have wings"]

    word2 = "gate"
    scrm2 = ["tega", "egat", "gtea"]
    hint2 = ["Synonym of 'door'", "Have lock in it", "Close the ____"]

    word3 = "cat"
    scrm3 = ["tac", "act", "cta"]
    hint3 = ["Enemy of dog", "lion belongs to ___ family", "Eats mouse"]

    print("For Organiser:-\nPress the digit in fron tp of the word, you want the user to guess")
    stop = False
    while stop == False:
        print("\n1. Aeroplane\n2. Gate\n3. Cat")
        inp = int(input("\n-> "))
        chance = 3
        if inp == 1:
            print("\nHandover the device to the player\n")

            while chance >= 0:
                if chance != 0:
                    print(scrm1[chance-1], "\nHint:", hint1[chance-1])
                    ans = input("\nYour answer : ").strip().lower()
                    if ans:
                        if ans != word1:
                            chance -= 1
                            print(f"Ohh that's an incorrect answer, now you are left with {chance} chance\n")
                            continue
                        else:
                            if chance == 3:
                                print("Woww!! you cracked this in fisrt go\nWell Done")
                                break
                            elif chance == 2:
                                print("Yayy!! First hint can't make you get the answer, but you smashed in the second go\nWell Done")
                                break
                            else:
                                print("Finally, you got the right answer\nKudos to you")
                                break
                    else:
                        print("\nYou didn't enter anything\nTry Again by typing some input or tell the organiser to help you with that\n")
                        continue
                else:
                    print(f"The correct answer is : {word1.capitalize()}\nTry Again next time.")
                    break
            stop = True
        elif inp == 2:
            print("\nHandover the device to the player\n")

            while chance >= 0:
                if chance != 0:
                    print(scrm2[chance-1], "\nHint:", hint2[chance-1])
                    ans = input("Your answer : ").strip().lower()
                    if ans:
                        if ans != word2:
                            chance -= 1
                            print(f"Ohh that's an incorrect answer, now you are left with {chance} chance\n")
                            continue
                        else:
                            if chance == 3:
                                print("Woww!! you cracked this in fisrt go\nWell Done")
                                break
                            elif chance == 2:
                                print("Yayy!! First hint can't make you get the answer, but you smashed in the second go\nWell Done")
                                break
                            else:
                                print("Finally, you got the right answer\nKudos to you")
                                break
                    else:
                        print("\nYou didn't enter anything\nTry Again by typing some input or tell the organiser to help you with that\n")
                        continue
                else:
                    print(f"The correct answer is : {word2.capitalize()}\nTry Again next time.")
                    break
            stop = True
        elif inp == 3:
            print("\nHandover the device to the player\n")
            while chance >= 0:
                if chance != 0:
                    print(scrm3[chance-1], "\nHint:", hint3[chance-1])
                    ans = input("Your answer : ").strip().lower()
                    if ans:
                        if ans != word3:
                            chance -= 1
                            print(f"Ohh that's an incorrect answer, now you are left with {chance} chance\n")
                            continue
                        else:
                            if chance == 3:
                                print("Woww!! you cracked this in fisrt go\nWell Done")
                                break
                            elif chance == 2:
                                print("Yayy!! First hint can't make you get the answer, but you smashed in the second go\nWell Done")
                                break
                            else:
                                print("Finally, you got the right answer\nKudos to you")
                                break
                    else:
                        print("\nYou didn't enter anything\nTry Again by typing some input or tell the organiser to help you with that\n")
                        continue
                else:
                    print(f"The correct answer is : {word3.capitalize()}\nTry Again next time.")
                    break
            stop = True
        else:
            print("\n[Message for organiser : Enter the correct input]")
            continue

scramble_words_game()
