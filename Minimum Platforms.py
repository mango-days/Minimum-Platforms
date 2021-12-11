arr = [ 900, 940, 950, 1100, 1500, 1800 ]
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ]

platform_count = 1

for index in range ( 0 , len ( arr ) - 1 ) :
    if dep [ index ] >= arr [ index + 1 ] : platform_count += 1
    if dep [ index ] > dep [ index + 1 ] : platform_count -= 1

print ( platform_count )