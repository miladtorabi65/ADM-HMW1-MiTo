def minion_game(string):
    # your code goes here
    vowel_words = ["A", "E", "I", "O", "U"]
    st, kev = 0, 0
    for i in range(len(string)):
        if string[i] in vowel_words:
            kev += len(string) - i
        else:
            st += len(string) - i
    if kev > st :
        print("Kevin",kev)
    elif st > kev:
        print("Stuart",st)
    else:
        print("Draw")   

if __name__ == '__main__':
    s = input()
    minion_game(s)
