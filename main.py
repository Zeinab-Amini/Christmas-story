print('''
         .!,            .!,
                                   ~ 6 ~          ~ 6 ~
                              .    ' i `  .-^-.   ' i `
                            _.|,_   | |  / .-. \   | |
                             '|`   .|_|.| (-` ) | .|_|.
                             / \ ___)_(_|__`-'__|__)_(______
                            /`,o\)_______________________o_(
                           /_* ~_\[___]___[___]___[___[_[\`-.
                           / o .'\[_]___[___]___[___]_[___)`-)
                          /_,~' *_\_]                 [_[(  (
                          /`. *  *\_]                 [___\ _\
                         /   `~. o \]      ;( ( ;     [_[_]`-'
                        /_ *    `~,_\    (( )( ;(;    [___]
                        /   o  *  ~'\   /\ /\ /\ /\   [_[_]
                       / *    .~~'  o\  ||_||_||_||   [___]
                      /_,.~~'`    *  _\_||_||_||_||___[_[_]_
                      /`~..  o        \:::::::::::::::::::::\
                     / *   `'~..   *   \:::::::::::::::::::::\
                    /_     o    ``~~.,,_\=========\_/========='
                    /  *      *     ..~'\         _|_ .-_--.
                   /*    o   _..~~`'*   o\           ( (_)  )
                   `-.__.~'`'   *   ___.-'            `----'
                         ":-------:"
                      hjw  \_____/


''')
print("Welcome to Christmas Island.")
print("Your mission is to find Santa.") 


#Write your code below this line 👇

first = input("You reach Santa's village, do you go 'l' for left or 'r' for right? ").lower()
if first == 'r':
    print("You walked in the snow for hours and never found Santa.")
else:
    second = input("You have reached the pool of hot coco, do you 'swim' or 'wait' for the elf to let you in? ").lower()
    if second == 'swim':
        print("You arn't allowed in the pool without permison and the elfs, kicked you out of their village. ")
    else:
        door = input("You have reached Santa's neighbor hood. There are three doors. 'Red', 'Green', and 'Yellow'. Which one do you go into?").lower()
        if door == 'green':
            print("You walked in a elf's house. They were all eating food and they do not like being disterbed so the whole fsmily tackeled you. ")
        elif door == 'red':
            "You walked in a sana, and the people charged you for loosing their warmth."
        else:
            "You found Santa and gave him a big hug. "