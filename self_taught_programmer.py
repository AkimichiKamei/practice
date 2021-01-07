# chapter 1
print('hello world')
print('Guid van Rossum')

for i in range(100):
    print("Hello World!")

# chapter 3
print('super!!')
print('sugar!!')
print('echo')

35 % 9
35 / 9
35 // 9

age = 24
if age > 30:
    print('From now on')
else:
    print("Let's get started")

# chapter 4

def even_odd():
    n = int(input('type a number:'))
    if n % 2 == 0:
        print('n is even.')
    else:
        print('n is odd.')

even_odd()

x = 100

def f():
    global x 
    x += 1
    print(x)
f()

try:
    a = int(input('type a number:'))
    b = int(input('type a number:'))
    print(a / b)
except(ZeroDivisionError, ValueError):
    print('Invalid input')

def add(x, y):
    """
    Returns x + y,
    :params x: int,
    :params y: int,
    :return: int sum of x and y,
    """
    return x + y

add(3, 8)

# 4-1
def power(x):
    """
    Returns x**2.
    :param x: int.
    :return: int power of x.
    """
    return x**2

power(3)

# 4-2
def literal(s):
    """
    Returns str(s).
    :param s: str.
    :return str s.
    """
    return str(s)

literal('song')

# 4-3
def yonex(x, y, z, n=3, m=2):
    """
    Returns (x**y + z) // n*m.
    :param x: int.
    :param y: int.
    :param z: int.
    :param n: int.
    :param m: int.
    :return int calcurate.
    """
    return (x**y + z) // n*m

yonex(3, 2, 9, m=1, n=2)

# 4-4
def double(x):
    """
    Returns x // 2.
    :param x: int.
    :return int quotient of x and 2.
    """
    return x // 2

def quadruple(x):
    """
    Returns x * 4.
    :param x: int.
    :return int quadruple of x.
    """
    return x * 4

x = double(4)
quadruple(x)

# 4-5
def decimal(x):
    """
    Returns flost(x).
    :param x: int or float.
    :return float x
    """
    try:
        return float(x)
    except(ValueError):
        print("Invalid input")
    
decimal(33)
decimal('44')
decimal('tomato')

# 4-6 re-write docstring

# 5-1
musician = ["fujifabric", "the birthday", "mister children"]

# 5-2
locations = (40, 41)

# 5-3
myself = {"height":169, "color":"silver", "author":"souseki", "dream":"thnderbird"}

myself["height"]

# 5-4
myself[input("キーを入力してください：")]

# 5-5
myself["fujifabric"] = ["若者のすべて", "茜色の夕日", "消えるな太陽"]

# 5-6
myset = set(myself)

myset

# 6-1
s = 'カミュ'
s[0]
s[1]
s[2]

# 6-2
s1 = input()
s2 = input()
"私は昨日{}を書いて，{}に送った！".format(s1, s2)

# 6-3
"aldous Huxley was born in 1894.".capitalize()

# 6-4
"どこで？　だれが？　いつ？".split("　")

# 6-5
lists = ["The", "fox", "jumped", "over", "the", "fence", "."]
" ".join(lists)

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox
fox = fox[0: -2] + "."
print(fox)

# 6-6
"A sceaming comes across the sky.".replace("s", "￥")

# 6-7
"Hemingway".index("m")

# 6-8
"'運命'なんて便利なものでぼんやりさせて．"

# 6-9
"three " + "three " + "three"
"three "*3

# 6-10
s3 = "四月の晴れた寒い日で，時計がどれも十三時を打っていた．"
s3[:10]


# chapter 7
tv = ["got", "Narcos", "Vice"]

for i, new in enumerate(tv):
    tv[i] = new.upper()

print(tv)

# 7-1
movies = ["ウォーキング・デッド", "アントラージュ", 
"ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for i in movies:
    print(i)

# 7-2
for i in range(1, 51):
    print(i)

# 7-3
for i, movie in enumerate(movies):
    print(i, movie)

# 7-4
ans = [1, 3, 5, 7]
res = input()
while res != 'q':
    if int(res) in ans:
        print('正解')
    else:
        print('不正解') 


res = input()
if res in ans:
    print('正解')
else:
    print('不正解') 
print(res)
print(ans)
res in ans
res

# 7-5
lists1 = [8, 19, 148, 4]
lists2 = [9, 1, 33, 83]
lists3 = []

for i, j in zip(lists1, lists2):
    lists3.append(i * j)
print(lists3)

for i in zip(lists1, lists2, lists3):
    print(i)
type(i)

# 8-1
import statistics

lists = [0, 1, 2, 3, 4]
statistics.mean(lists)
statistics.harmonic_mean(lists)
statistics.median(lists)

# 8-2
import cubed
cubed.cubed_1(3)

# chapter9

import os
os.path.join('Users', 'eCho2', 'Desktop', 'enwiki2017.txt-miktop1000+mik.txt')

ut = open("ut.txt", "w", encoding="utf-8")
ut.write("Hi from Python!")
ut.close

with open("ut.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

my_list = []
with open("st.txt", "r") as f:
    my_list.append(f.read())
print(my_list)

import csv
with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

import csv
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

print(os.getcwd())

# 9-1
with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read())
# 9-2
ans = input("if you have any question?:")
with open("st.txt", "w", encoding="utf-8") as f:
    f.write(ans)

with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 9-3
my_csv = [["Top Gun", "Risky Business", "Minority Report"], 
["Titanic" "The Revenat", "Inception"],["Training Day", "Man on Fire", "Flight"]]

with open("st.txt", "w+", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(my_csv)

with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("st.csv", "w+", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(my_csv)

with open("st.csv", "r", encoding="utf-8") as f:
    print(f.read())

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)

movies_japanese = [["秀でた人", "危険な仕事", "少数派の報告"],
          ["タイタニック号", "蘇りし亡霊", "始まり"],
          ["訓練日", "マイボディガード", "飛翔"]]
with open("movies_japanese.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies_japanese:
        spamwriter.writerow(movie_list) 

# chapter 10

def hangman(word):
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     o     ",
              "|    /|\    ",
              "|    / \    ",
              "|           ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Predict one character, please."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "s"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))        
        if "_" not in board:
            print("You are win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You are lose! Correct answer is {}.".format(word))


hangman("cat")

win = True
not win
not not win

# 10-1

def hangman_random(word_list):
    import random
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     o     ",
              "|    /|\    ",
              "|    / \    ",
              "|           ",
              ]
    word = word_list[random.randint(0, len(word_list)-1)]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Predict one character, please."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "s"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))        
        if "_" not in board:
            print("You are win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You are lose! Correct answer is {}.".format(word))

hangman_random(["apple", "lemon", "orange"])

# chapter 12
class Orange:
    def __init__(self, w, c):
        """weight is gram"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    
    def rot(self, days, temp):
        """temp is celsius"""
        self.mold = days * temp

orange = Orange(200, "orange")
orange
print(orange)

orange.rot(10, 37)
print(orange.mold)
print(orange.mold)

# 12-1
class Apple:
    def __init__(self, w, c, h, t):
        """
        :param x: int.
        :param c: str.
        :param h: str.
        :param t: str.
        """
        self.weight = w
        self.color = c
        self.hardness = h
        self.taste = t
        print("Created!")

apple = Apple(100, "red blue", "hard", "good" )
apple

# 12-2
class Circle:
    def __init__(self, r):
        """
        :param r: float.
        """
        self.radius = r

    def area(self):
        import math
        return self.radius**2 * math.pi
    
circle = Circle(11.32)
circle.area()
circle1 = Circle(10)
circle1.area()

# 12-3
class Triangle:
    def __init__(self, b, h):
        """
        :param b: float.
        :param h: folot.
        """
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2

triangle = Triangle(10, 4)
print(triangle.area())
triangle1 = Triangle(13.21, 23.55)
print(triangle1.area())

# 12-4
class Hexagon:
    def __init__(self, e):
        """
        :param e: float.
        """
        self.edge = e

    def calculate_perimeter(self):
        return 6*self.edge

hexagon = Hexagon(66)
print(hexagon.calculate_perimeter())

# chapter 13
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = 1

    def area(self):
        return self.width * self.len

recrangle = Rectangle(2, 1)
print(recrangle.width)
print(recrangle.area())
# Special methods (e.g., initial method) do not require brackets.
# Normal methods require brackets.
 
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
print(data_one.nums)
print(data_one.change_data(0, 100))
print(data_one.nums)

data_one.nums[0] = 200
print(data_one.nums)

class PublicPrivateExample:
    def __init__(self):
        self.public = 2
        self._unsafe = "unsafe"

    def public_method(self):
        # client available
        pass
    
    def _unsafe_method(self):
        # client unavailable
        pass

public_private_example = PublicPrivateExample()
public_private_example.public_method
print(public_private_example.public)

# 13-1 & 13-2
class Rectangle0:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return 2*self.width + 2*self.len

class Square:
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return 4*self.len

    def change_size(self, c):
        self.len += c
            
rectangle = Rectangle0(10, 6)
square = Square(9)
rectangle.calculate_perimeter()
square.calculate_perimeter()
square.change_size(7)
square.change_size(14)
square.change_size(-21)

# 13-3
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def what_am_i(self):
        return "I am a shape"

class Square0(Shape):
    pass

square = Square0(10, 10)
square.what_am_i()
square.width
square.len

class Shape1:
    def what_am_i(self):
        return "I am a shape"

class Rectangle1(Shape1):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return 2*(self.width + self.len)

    pass

rectangle1 = Rectangle1(10, 6)
rectangle1.what_am_i()
rectangle1.width
rectangle1.len
rectangle1.calculate_perimeter()

# 13-4
class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name 

aki = Rider("Aki")
mike = Horse("Mike", "White", aki)
mike.name
mike.owner.name

# chapter 14
class Rectangle3:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle3(10, 24)
r2 = Rectangle3(8, 21)
r3 = Rectangle3(12, 998)
Rectangle3.recs 
Rectangle3.recs.append(0)
r1.recs
r2.recs

class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
lion
print(lion)
print(lion)

class Lion1:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

lion1 = Lion1("Dilbert")
print(lion1)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)
    
x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
print(x.n)
print(y.n)
x + y 
x
y 
y + x

x = 10
if x is None:
    print("x is None")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None")
else:
    print("x is not None")

# 14-1 & 14-2
class Square4:
    square_list = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        print(("{} by {} by {} by {}".format(w, l, w, l)))

square4 = Square4(2, 3)
square5 = Square4(3, 8)
Square4.square_list.append(square4)
Square4.square_list.append(square5)
print(Square4.square_list[1].width)  

# 14-3
class TwoParams:
    def __init__(self, o1, o2):
        self.object1 = o1
        self.object2 = o2
        print(self.object1 is self.object2)

TwoParams(square4, square4)

# 14-1 ans
class Shape5():
    def what_am_i(self):
        print("I am a shape.")

class Square5(Shape5):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

a_square = Square5(29)
print(Square5.square_list)
another_square = Square5(93)
print(Square5.square_list)
a_square.what_am_i()

# 14-3 ans
def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "a"))

# chapter 15 Game-War
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None, 
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, v, s):
        """Both suits(marks) and values is int"""
        self.value = v 
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
            shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()     


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("player1's name")
        name2 = input("player2's name")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "In this round, {} wins"
        w = w.format(winner)
        print(w)

    def draw(self, p1n ,p1c, p2n, p2c):
        d = "{} draws {}, {} draws {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("start war!")
        while len(cards) >= 2:
            m = "q is quit, other is play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("end of the game, {} wins!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "draw!"

game = Game()
game.play_game()
print(game.winner)

# chapter 17
import re
l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)
print(matches)

import re
zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""
m = re.findall("^If", zen, re.MULTILINE)
print(m)

import re
string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

import re
line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)           
print(m)

import re
t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

import re 
text = """キリンは大昔から __複数名詞__ の興味の対象でした．
キリンは __複数名詞__ の中で一番背が高いですが，科学者たちは
そのような長い __体の一部__ をどうやって獲得したのか説明でき
ません．キリンの身長は __数値__ __単位__ 近くあり，その高さ
のほとんどは脚と __体の一部__ によるものです．"""
def mad_libs(mls):
    """
    :param mls: 文字列で，ユーザーに入力してもらいたい単語
    （＝ヒント）の部分は後を2つのアンダースコアで挟んでください．
    ヒントの単語にはアンダースコアを含めないでください．__hint_hint__
    はだめです．__hint__ はOKです．
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)

import re
line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m) 

import re
line = "The ghost that says boo haunts the loo"
m = re.findall(".oo", line, re.IGNORECASE)
print(m)

# chapter 18
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

app.run(port=8000)

import pyzint
symbol = pyzint.Barcode.CODE11('1234567')
with open('CODE11.bmp', "wb") as bmp:
    bmp.write(symbol.render_bmp())

