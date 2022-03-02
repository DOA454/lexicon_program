x = ('north', 'east', 'west', 'south', 'up', 'down', 'left', 'right')
y = ('go', 'stop', 'kill', 'eat')
a = ('the', 'at', 'in', 'of', 'from')
b = ('bear', 'princess', 'cabinet', 'door')

my_directions = dict.fromkeys(x, 'direction')
my_verbs = dict.fromkeys(y, 'verb')
my_stops = dict.fromkeys(a, 'stop')
my_nouns = dict.fromkeys(b, 'noun')

def scan(sentence):

    words = sentence.split()
    token = []
    for index in range(len(words)):
        if words[index] in x:
            list = (my_directions[words[index]], words[index])
            token.append(list)
        elif words[index] in y:
            list = (my_verbs[words[index]], words[index])
            token.append(list)
        elif words[index] in a:
            list = (my_stops[words[index]], words[index])
            token.append(list)
        elif words[index] in b:
            list = (my_nouns[words[index]], words[index])
            token.append(list)
        else:
            try:
                num = int(words[index])
                list = ('number', num)
                token.append(list)
            except ValueError:
                list = ('error', words[index])
                token.append(list)

    return token
