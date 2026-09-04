def minion_game(string):
    """
    link : https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
    """
    n = len(string)
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    # for i in range(1, n + 1):
    #     for j in range(0, n):
    #         sub_str = string[j:i]
    #         if len(sub_str) == 0:
    #             break
    #         if sub_str in freq_map:
    #             freq_map[sub_str] += 1
    #         else:
    #             freq_map[sub_str] = 1
    # print(freq_map)

    # for i in freq_map.keys():
    #     if i[0] in vowels:
    #         kevin += freq_map[i]
    #     else:
    #         stuart += freq_map[i]

    if stuart == kevin:
        print("Draw")
    elif stuart > kevin:
        print("Stuart " + str(stuart))
    else:
        print("Kevin " + str(kevin))


minion_game("BANANA")
