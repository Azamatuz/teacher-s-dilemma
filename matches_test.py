import axelrod as axl


teachers_list = [axl.Defector(), axl.Cooperator(), axl.TitForTat(), axl.TitFor2Tats(), axl.SuspiciousTitForTat()]*20


def match(teachers_list):
    for index, teacher_one in enumerate(teachers_list):
        print('------------------')
        players = []
        #print(index)
        # print(teachers_list)
        short_list = []
        short_list += teachers_list
        del short_list[index]
        #teachers_list.remove(teacher_one)
        # print('short:', short_list)

        for teacher_two in short_list:
            players.clear()
            players.append(teacher_one)
            players.append(teacher_two)
            print(players)
            match = axl.Match(players, 1)
            results = match.play()
            print(results)

match(teachers_list)

def play_version(players):
    for index, t1 in enumerate(teachers_list):
        short_list = teachers_list
        del short_list[index]
        for t2 in short_list:
            print(t1, 'vs', t2)
            result = t1.play(t2)
            print(result)


# play_version(teachers_list)

def match_list(players):
    print(players)
    match = axl.Match(players, 9)
    print(match.play())


# match_list(teachers_list)
