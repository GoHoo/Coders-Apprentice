x = 5
print( x )
x = 7 * 9 + 13
# overwrite the previous value of x
print( x )
x = "A nod ' s as good as a wink to a blind bat."
print( x )
x = int( 15 / 4 ) - 27
print( x )

x = 2
y = 3
print( "x =", x )
print( "y =", y )
print( "x * y =", x * y )
print( "x + y =", x + y )

x = 2
y = 3
print( "x =", x, "and y =", y )


x = 2
y = 3
print( "x =", x, "and y =", y )
# Swap the values of x and y using z as intermediary storage.
z = x
x = y
y = z
print( "x =", x, "and y =", y ,z)


'''a = 3.14159265
b = 7.5
c = 8.25
d = a * b * b * c / 3
print( d )'''
#Same code as aboive but more readable
pi = 3.14159265
radius = 7.5
height = 8.25
volume_of_cone = pi * radius * radius * height / 3
print( volume_of_cone )


#Constants
'''total = 24.95; final_total = int( 100 * total * 1.15 ) / 10;
print( final_total )'''
SERVICE_CHARGE = 1.15
CENTS = 100
total = 24.95
final_total = int( CENTS * total * SERVICE_CHARGE ) / CENTS
print( final_total )

########################################################

nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1

############################################################
a = 3
print( type( a ) )
a = 3.0
print( type( a ) )
a = "3.0"
print( type( a ) )
##
a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )
print( a,c )
##################
name = "John Cleese"
print( name )
###############

number_of_bananas = 100
number_of_bananas += 12
number_of_bananas -= 13
number_of_bananas *= 19
number_of_bananas /= number_of_bananas
print( number_of_bananas )
################

# comment: insert your code here.
# BTW: Have you noticed that everything right of the hash mark
print( "Something..." ) # is ignored by your python interpreter?
print( "and something else.." ) # Use this to comment your code!
"""Another way of commenting on your code is via triple quotes
-- these can be distributed over multiple """ # lines
' ' ' which can also be done with single quotes ' ' '
# but be careful
# with there being quotes IN your comments when you use this
# multi-line method
print( "Done." )



