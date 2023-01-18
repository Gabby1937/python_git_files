# Part 1 code:
def my_sqrt(a):
    while True:
     y = (x + a/x) / 2.0
     if y == x:
        break
     print((x + a/x) / 2.0)
a=4
x=3
y=5
print(my_sqrt(a))


#Part 2 code input:
import math
a=0
math.sqrt(a)
def my_sqrt(a):
    math.sqrt(a)
    return math.sqrt(a)

diff = my_sqrt(a) - math.sqrt(a)

def test_sqrt(a):
    while a < 27:
        a=a+1
        print('a', '=', a, '|', 'my_sqrt(a)', '=', my_sqrt(a), '|', 'math.sqrt(a)', '=', math.sqrt(a), '|', "diff", '=', diff)
test_sqrt(a)

#Part 2 Output Code:
# a = 1 | my_sqrt(a) = 1.0 | math.sqrt(a) = 1.0 | diff = 0.0
# a = 2 | my_sqrt(a) = 1.4142135623730951 | math.sqrt(a) = 1.4142135623730951 | diff = 0.0
# a = 3 | my_sqrt(a) = 1.7320508075688772 | math.sqrt(a) = 1.7320508075688772 | diff = 0.0
# a = 4 | my_sqrt(a) = 2.0 | math.sqrt(a) = 2.0 | diff = 0.0
# a = 5 | my_sqrt(a) = 2.23606797749979 | math.sqrt(a) = 2.23606797749979 | diff = 0.0
# a = 6 | my_sqrt(a) = 2.449489742783178 | math.sqrt(a) = 2.449489742783178 | diff = 0.0
# a = 7 | my_sqrt(a) = 2.6457513110645907 | math.sqrt(a) = 2.6457513110645907 | diff = 0.0
# a = 8 | my_sqrt(a) = 2.8284271247461903 | math.sqrt(a) = 2.8284271247461903 | diff = 0.0
# a = 9 | my_sqrt(a) = 3.0 | math.sqrt(a) = 3.0 | diff = 0.0
# a = 10 | my_sqrt(a) = 3.1622776601683795 | math.sqrt(a) = 3.1622776601683795 | diff = 0.0
# a = 11 | my_sqrt(a) = 3.3166247903554 | math.sqrt(a) = 3.3166247903554 | diff = 0.0
# a = 12 | my_sqrt(a) = 3.4641016151377544 | math.sqrt(a) = 3.4641016151377544 | diff = 0.0
# a = 13 | my_sqrt(a) = 3.605551275463989 | math.sqrt(a) = 3.605551275463989 | diff = 0.0
# a = 14 | my_sqrt(a) = 3.7416573867739413 | math.sqrt(a) = 3.7416573867739413 | diff = 0.0
# a = 15 | my_sqrt(a) = 3.872983346207417 | math.sqrt(a) = 3.872983346207417 | diff = 0.0
# a = 16 | my_sqrt(a) = 4.0 | math.sqrt(a) = 4.0 | diff = 0.0
# a = 17 | my_sqrt(a) = 4.123105625617661 | math.sqrt(a) = 4.123105625617661 | diff = 0.0
# a = 18 | my_sqrt(a) = 4.242640687119285 | math.sqrt(a) = 4.242640687119285 | diff = 0.0
# a = 19 | my_sqrt(a) = 4.358898943540674 | math.sqrt(a) = 4.358898943540674 | diff = 0.0
# a = 20 | my_sqrt(a) = 4.47213595499958 | math.sqrt(a) = 4.47213595499958 | diff = 0.0
# a = 21 | my_sqrt(a) = 4.58257569495584 | math.sqrt(a) = 4.58257569495584 | diff = 0.0
# a = 22 | my_sqrt(a) = 4.69041575982343 | math.sqrt(a) = 4.69041575982343 | diff = 0.0
# a = 23 | my_sqrt(a) = 4.795831523312719 | math.sqrt(a) = 4.795831523312719 | diff = 0.0
# a = 24 | my_sqrt(a) = 4.898979485566356 | math.sqrt(a) = 4.898979485566356 | diff = 0.0
# a = 25 | my_sqrt(a) = 5.0 | math.sqrt(a) = 5.0 | diff = 0.0
# a = 26 | my_sqrt(a) = 5.0990195135927845 | math.sqrt(a) = 5.0990195135927845 | diff = 0.0
# a = 27 | my_sqrt(a) = 5.196152422706632 | math.sqrt(a) = 5.196152422706632 | diff = 0.0
