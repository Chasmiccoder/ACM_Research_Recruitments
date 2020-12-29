import time 
start_time = time.time()

import csv

csv_file   = open( "Bike_Data.csv" )
#csv_file   = open ( "C:\Users\\aryam\Desktop\Aryaman\Programming Hub\GitHub\ACM_Research_Recruitments\Machine Learning Classification\Bike_Data.csv") 
csv_reader = csv.reader( csv_file, delimiter = ',' )

line_count = 0
dataset  = [ ]
features = [ ]

for row in csv_reader:
    if line_count == 0:
        features.append( row )
        line_count += 1

    else:
        dataset.append( row )
        line_count += 1 

N = len( dataset )

"""
print( '\n'*5)
print( "Features:\n", features )
print( "First 10 rows: " )

for i in range( 10 ):
    print( dataset[ i ] )
    print( '\n')
"""