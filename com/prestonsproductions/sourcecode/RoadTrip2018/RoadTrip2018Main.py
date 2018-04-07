from com.prestonsproductions.sourcecode.RoadTrip2018 import RoadTrip2018A as RT
###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main1():
    # Trip Data
    tripdata = [{'NAME':'Bath', 'DISTANCE':0, 'DURATION':0, 'GASPRICE':2.51},
                {'NAME':'Lansing', 'DISTANCE':10, 'DURATION':12, 'GASPRICE':2.50}, 
                {'NAME':'Detroit', 'DISTANCE':150, 'DURATION':43, 'GASPRICE':2.60}, 
                {'NAME':'Saginaw', 'DISTANCE':100, 'DURATION':51, 'GASPRICE':2.60},
                {'NAME':'Alpena', 'DISTANCE':219, 'DURATION':89, 'GASPRICE':3.10},
                {'NAME':'Albion', 'DISTANCE':300, 'DURATION':70, 'GASPRICE':2.80},
                {'NAME':'Muskegon', 'DISTANCE':140, 'DURATION':80, 'GASPRICE':2.99},
                {'NAME':'Traverse City', 'DISTANCE':50, 'DURATION':50, 'GASPRICE':3.14},
                {'NAME':'Kalamazoo', 'DISTANCE':120, 'DURATION':50, 'GASPRICE':3.00},
                {'NAME':'Jackson', 'DISTANCE':43, 'DURATION':45, 'GASPRICE':2.78},
                {'NAME':'Marshall', 'DISTANCE':32, 'DURATION':33, 'GASPRICE':2.78},
                {'NAME':'Three Rivers', 'DISTANCE':51, 'DURATION':59, 'GASPRICE':2.75},
                {'NAME':'Holland', 'DISTANCE':74, 'DURATION':84, 'GASPRICE':3.05},
                {'NAME':'Ludington', 'DISTANCE':102, 'DURATION':104, 'GASPRICE':3.25},
                {'NAME':'Cadillac', 'DISTANCE':71, 'DURATION':84, 'GASPRICE':3.01},
                {'NAME':'Mount Pleasant', 'DISTANCE':65, 'DURATION':65, 'GASPRICE':2.99},
                {'NAME':'Flint', 'DISTANCE':90, 'DURATION':87, 'GASPRICE':2.59},
                {'NAME':'Clio', 'DISTANCE':15, 'DURATION':18, 'GASPRICE':2.66},
                ]
    
    tripdata2 = [{'NAME':'Bath', 'DISTANCE':0, 'DURATION':0, 'GASPRICE':2.51},                 
                {'NAME':'Detroit', 'DISTANCE':130, 'DURATION':43, 'GASPRICE':2.60},
                {'NAME':'Jackson', 'DISTANCE':43, 'DURATION':45, 'GASPRICE':2.78}, 
                {'NAME':'Saginaw', 'DISTANCE':100, 'DURATION':51, 'GASPRICE':2.60},
                {'NAME':'Muskegon', 'DISTANCE':200, 'DURATION':80, 'GASPRICE':2.99},
                {'NAME':'Alpena', 'DISTANCE':160, 'DURATION':89, 'GASPRICE':3.10},
                {'NAME':'Albion', 'DISTANCE':300, 'DURATION':70, 'GASPRICE':2.80},
                {'NAME':'Lansing', 'DISTANCE':10, 'DURATION':12, 'GASPRICE':2.50},                
                {'NAME':'Traverse City', 'DISTANCE':109, 'DURATION':50, 'GASPRICE':3.14},
                {'NAME':'Kalamazoo', 'DISTANCE':22, 'DURATION':50, 'GASPRICE':3.00},
                {'NAME':'Ann Arbor', 'DISTANCE':98, 'DURATION':92, 'GASPRICE':3.10},
                {'NAME':'Brighton', 'DISTANCE':19, 'DURATION':24, 'GASPRICE':2.96},
                {'NAME':'Flint', 'DISTANCE':38, 'DURATION':36, 'GASPRICE':2.99},
                {'NAME':'Bay City', 'DISTANCE':50, 'DURATION':45, 'GASPRICE':2.89},
                {'NAME':'Tawas City', 'DISTANCE':69, 'DURATION':70, 'GASPRICE':2.89},
                {'NAME':'Mackinaw City', 'DISTANCE':165, 'DURATION':152, 'GASPRICE':3.30},
                {'NAME':'St. Ignace', 'DISTANCE':12, 'DURATION':25, 'GASPRICE':3.20},
                {'NAME':'Sault Ste Marie', 'DISTANCE':60, 'DURATION':56, 'GASPRICE':3.44},
                ]
    
    landmarks = [('Blue Chair','Alpena','Lansing'),
                 ('Tallest Sign','Alpena','Albion'),
                 ('Waffle House','Detroit','Jackson'),
                 ('Candy Factory','Kalamazoo','Grand Rapids'),
                 ('Pencil Factory','Jackson','Lansing'),
                 ('Michigan\'s Smallest House','Alpena','Albion'),
                 ('Famous Steve''s','Kalamazoo','Jackson'),
                 ('Mystery Spot','Mackinaw City','Sault Ste Marie'),
                 ('The Big Tire','Ann Arbor','Detroit'),
                 ('I94 Scenic View','Jackson','Marshall'),
                 ('Sky Resort','Ludington','Traverse City'),
                 ('The Bay Bridge','Bay City','Saginaw'),
                 ('Nothing','Bath','St. Johns'),
                 ('Nothing','Flint','Clio'),
                ]
    
    # Print Question Answer
    print('Source Code (MAIN) - Division B/C - Road Trip - Travel Log')
    
    print('QUESTION 0 A (2): '+RT.getTravelLogTitle('The Source Code Travel Log', '10001', '03/03/2018')) # The Source Code Travel Log - 10001 - 03/03/2018
    
    print('QUESTION 1 A (2): '+str(RT.getDistanceBetween(800,600))) # 200 or -200
    print('QUESTION 1 B (2): '+str(RT.getDistanceBetween(800,600))) # 200
    
    print('QUESTION 2 A (2): '+str(RT.getFuelCost(501,2.59,24))) # 54.07 or 54.06625
    print('QUESTION 2 B (2): '+str(RT.getFuelCost(501,2.59,24))) # 54.07
    
    print('QUESTION 3 A (3): '+str(RT.getAverageSpeed(600, 500))) # 72.0
    
    print('QUESTION 4 A (3): '+str(RT.firstCapital('sAGINaW'))) # Saginaw
    
    print('QUESTION 5 A (3): '+str(RT.getCents(1.387))) # 138 or 139
    
    print('QUESTION 6 A (4): '+str(RT.isFuelNeeded(20, 479, 24)) + ', ' + str(RT.isFuelNeeded(15, 600, 24))) # False, True
    
    print('QUESTION 7 A (4): '+str(RT.isPrimeNumber(199)) +', ' + str(RT.isPrimeNumber(8335))) # True, False
    
    print('QUESTION 8 A (4): '+str(RT.convertUnits(20, 'MI','KM'))) # 32.25806451612903 or 32.0
    print('QUESTION 8 B (2): '+str(RT.convertUnits(20, 'MI','CE'))) # -1
    
    print('QUESTION 9 A (4): '+str(RT.getTotalDistance(tripdata))) # 1632
    
    print('QUESTION 10 A (5): '+str(RT.getShortestTrip(tripdata,tripdata2))) # ['Bath', 'Sault Ste Marie', 47]
    print('QUESTION 10 B (2): '+str(RT.getShortestTrip(tripdata2,tripdata2))) # []
    
    print('QUESTION 11 A (5): '+str(RT.getFastestSpeed(tripdata))) # ['Albion', 'Alpena']
    
    print('QUESTION 12 A (4): '+str(RT.getTotalAverageSpeed(tripdata))) # 87.47771095642337
    print('QUESTION 12 B (2): '+str(RT.getTotalAverageSpeed([]))) # -1
    
    print('QUESTION 13 A (4): '+str(RT.getDistantCities(tripdata))) # ['Albion', 'Alpena', 'Cadillac', 'Flint', 'Holland', 'Ludington', 'Mount Pleasant', 'Muskegon', 'Saginaw', 'Three Rivers']
    print('QUESTION 13 B (2): '+str(RT.getDistantCities(tripdata))) # ['Albion', 'Alpena', 'Cadillac', 'Flint', 'Holland', 'Ludington', 'Mount Pleasant', 'Muskegon', 'Saginaw', 'Three Rivers']
    
    print('QUESTION 14 A (5): '+str(RT.getLandMarks('Alpena','Albion', landmarks))) # ['Tallest Sign', "Michigan's Smallest House"]
    
    print('QUESTION 15 A (5): '+str(RT.getLandMarksSeen(tripdata, landmarks))) # 5
     
    print('QUESTION 16 A (8): '+str(RT.getFuelStandardDeviation(tripdata))) # 0.22617321014579586
    
    print('QUESTION 17 A (8): '+str(RT.getTotalFuelCost(tripdata))) # 176.8
    
    print('QUESTION 18 A (8): '+str(RT.getMedianDistance(tripdata))) # 72.5
      
    print('QUESTION 19 A (4): '+str(RT.getStatistic(tripdata))) # Check for Answer
    print('QUESTION 19 A (2): '+'Check for comment explaining function.')
    print('QUESTION 19 A (2): '+'Check if previous function in file was called.')
    print('QUESTION 19 A (2): '+'Check if import statement was used.')

    # Print Trip Log
    
main1()