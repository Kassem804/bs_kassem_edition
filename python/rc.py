import bs

my_profile = 'Hi :) My name is Abbas Kassem, I am 16 years old, I am from Algeria'

def text():

    return bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'center',
            'vAlign': 'center',
            'vrDepth': 0,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': 'BOOYAH',
            'big': True,
            'position': (0, 27),
            'color': (1,1,0)})


def s():


    i = bs.newNode('image', attrs={
            'scale': (2000, 100),
            'texture': bs.getTexture('bar'),
            'position': (0, 27),
            'color': (1,1,0)})
    i.delete()

    n = bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'center',
            'vAlign': 'center',
            'vrDepth': 0,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': 'BOOYAH',
            'big': True,
            'position': (0, 27),
            'color': (1,1,0)})

    c = bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'center',
            'vAlign': 'center',
            'vrDepth': 2,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': 'BOOYAH',
            'big': True,
            'position': (0, 27),
            'color': (1,1,0)})

    bs.animate(c, "scale", {0:1, 500:2})
    bs.animate(c, "opacity", {0:1, 500:0})
    bs.gameTimer(500, c.delete)
    return (n, i)

def add_txt(lifespan, node, txt):
    if not node.getNodeType() == 'text': return
    num = len(txt)
    added = list(txt)
    def a():
        node.text += added[0]
        added.pop(0)
    for i in range(num):
        bs.gameTimer((lifespan/num)*(i+1), a)

def sort_key(item):
    return item[1]

def rk(players):
    ranked = sorted(players, key=sort_key, reverse=True)
    result = []
    for i, (players, score) in enumerate(ranked, start=1):
        result.append({
            'rank': i,
            'player': players,
            'score': score})
    print(str(enumerate(ranked, start=1)))
    return result

def players_rank():
    players = [('kassem', 150), ('khaled', 120), ('king cold', 220), ('Roshi', 100)]
    return rk(players)
