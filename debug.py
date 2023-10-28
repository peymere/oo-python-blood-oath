import ipdb
from lib import *

# test your code here
# e.g.

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( 'Logan', 18, 'Living the Dream' )
f3 = Follower( 'Kassidy', 23, 'Living the Dream' )
f4 = Follower( 'Peyton', 29, 'Living the Dream' )
c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult( 'Scientology', 'Hollywood', 1982, 'Tom Cruise is daddy' )
c3 = Cult( 'Toaster Fan Club', 'New Orleans', 2020, "He's little and he's brave!")

bo1 = BloodOath( f1, c1, '2019-09-16' )
bo2 = BloodOath( f4, c3, '2020-03-20' )


# c1.followers => ???
# f1.cults => ???




print( "Mwahahaha!" )
ipdb.set_trace()