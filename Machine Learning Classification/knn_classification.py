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
def time_difference( pair1, pair2 ):
    date1, time1 = pair1.split( ' ' )
    date2, time2 = pair2.split( ' ' )
    #print( "PAIR 1 BRO: ", pair1 )
    #date1, time1 = pair1
    #date2, time2 = pair2


    duration = 0
    hour1, minute1, second1 = [ int(i) for i in time1.split( ':' ) ]
    hour2, minute2, second2 = [ int(i) for i in time2.split( ':' ) ]

    seconds_1 = hour1*60*60 + minute1*60 + second1
    seconds_2 = hour2*60*60 + minute2*60 + second2

    if date1 == date2:
        # They started and ended on the same day
        duration = seconds_2 - seconds_1 
    else:
        # They started on one day and ended the next day. The dataset contains no element
        # where the person started on one day, and ended on the day after the next day.
        duration = seconds_2 + ( 12*60*60 - seconds_1 )
    
    return duration


def data_prepocessing( dataset ):
    """
    This function conducts data preprocessing.
    The unique values of start stations, end stations and bike numbers are found and returned.
    Also, the entire dataset, in the form of a dictionary named 'dataframe' is also returned.
    The keys of dataframe involve the classes and the values involve the respective features of those points.

    We also prune the dataset by removing the unnecessary columns like the names of the start stations and
    the names of the end stations.

    Handling Start Date and End Date:
    The exact date they started and ended the bike sharing service does not matter, but the duration
    they used it does matter, so we will extract only the duration, and add it to new_dataset.
    """
    start_station = [ ]
    end_station   = [ ]
    bike_numbers  = [ ]
    new_dataset = [ ]
    classes     = [ ]

    for row in dataset:
        
        if row[ 3 ] not in start_station:
            start_station.append( row[ 3 ] )
            
        if row[ 5 ] not in end_station:
            end_station.append( row[ 5 ] )

        if row[ 7 ] not in bike_numbers:
            bike_numbers.append( row[ 7 ] )

        time_duration = time_difference( row[ 1 ], row[ 2 ] )

        new_dataset.append( tuple( [row[0], row[1], row[2], row[3], 
                             row[5], row[7], time_duration] ) )
        # Using tuple( ) because dictionary requires immutable data type

         
        classes.append( row[8] )

    print( "CLASSES BRO: ", classes[:10] )
    print( "FEATURES BRO: ", new_dataset[:4] )

    dataframe = dict( zip( new_dataset, classes ) )

    return dataframe, bike_numbers, start_station, end_station

dataframe, bike_numbers, start_station, end_station = data_prepocessing ( dataset )

print( "Start Stations: ", len(start_station) )
print( "End Stations: ", len(end_station) )

print( "Bike Numbers: \n", len(bike_numbers) )
#print( "\n\nDataframe keys first 10: \n\n", dataframe.keys()[:10] )
#print( "\n\nDataframe values first 10: \n\n", dataframe.values()[:10] )

k = 0
"""
for i,j in dataframe:
    print( "KEY: ", i )
    print( "VAL: ", j )
    k+=1
    if k > 10:
        break
"""


"""
Since these are arbitrary numbers, to prevent the model from getting confused, we need to
employ One Hot Encoding. 
For example: If the datapoint's start station is not equal to 31020, then the value under 
start_station_31020 column will be 0. Else it will be 1. 

"""






        
