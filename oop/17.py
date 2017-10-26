
from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91))

print sine_table
