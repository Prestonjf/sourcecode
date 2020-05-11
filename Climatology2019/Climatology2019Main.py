from com.prestonsproductions.sourcecode.Climatology2019 import Climatology2019A as C


###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main1():
    
    # Print Question Answer
    print('Source Code (MAIN) - Division B/C - Climatology - Weather Analyzer')
    
    print('QUESTION 0 A (2): '+C.getName('07/07/2019')) # Bath High School Weather Warriors 07/07/2019
    print('QUESTION 1 A (2): '+str(C.getAverage([-1.34,33,21,0,9,22,113,7,33.23,1.3,-9,-1.45]))) # 18.98 OR
    print('QUESTION 1 B (2): '+str(C.getAverage([-1.34,33,21,0,9,22,113,7,33.23,1.3,-9,-1.45]))) # 18.98
    print('QUESTION 2 A (2): '+str(C.convertTemp(35, 'F'))) # 95.0
    print('QUESTION 2 B (2): '+str(C.convertTemp(122, 'C'))) #50.0
    print('QUESTION 2 C (2): '+str(C.convertTemp(35, 'Z')))  # None
    print('QUESTION 3 A (2): '+str(C.compareDates('2018-05-21', '2019-05-21'))) # -1 
    print('QUESTION 3 B (2): '+str(C.compareDates('2019-05-21', '2019-05-21'))) # 0
    print('QUESTION 3 C (2): '+str(C.compareDates('2019-06-30', '2019-06-04'))) # 1       
    
    # List containing weather information per day since 1960
    weather = C.loadWeatherData('ChicagoOHareData.txt')
    print('QUESTION 4 A (4): '+str(len(weather))) # 21641
    print('QUESTION 5 A (4): '+str(C.getWeather(weather, '1988-08-08'))) # {'TAVG': 29.2, 'PRCP': 30.7, 'DATE': '1988-08-08', 'TMIN': 21.1, 'TMAX': 37.2, 'AWND': 3.8, 'SNWD': 0, 'SNOW': 0}
    print('QUESTION 6 A (4): '+str(C.getAverageTemperature(weather))) # 9.81738829074436
    print('QUESTION 7 A (5): '+str(C.getYearlyPercipitation(weather, '1976'))) # 675.1999999999994
    print('QUESTION 8 A (5): '+str(C.getDaysWithSnow(weather))) # 2680
    print('QUESTION 9 A (5): '+str(C.getWindyDays(weather))) # ['1984-04-30', '1987-03-09', '1994-11-28']
    print('QUESTION 10 A (6): '+str(C.convertMetric(421.218, 'km', 'cm'))) # 42121800.0
    print('QUESTION 11 A (6): '+str(C.getHighestSnowFallYear(weather))) # ['1978']
    print('QUESTION 12 A (6): '+str(C.getHighestAverageTemp(weather))) # ['2012']
    print('QUESTION 13 A (6): '+str(C.getTempRangeCount(weather))) # 3105

    print('QUESTION 14 A (6): '+str(C.getTotalPercipitation('1990-03-02', '1994-05-10', weather))) # 3986
    print('QUESTION 14 B (2): '+str(C.getTotalPercipitation('1990-03-02', '1994-05-10', weather))) # 3986
    
    print('QUESTION 15 A (7): '+str(C.getTheRightConditionsCount(weather))) # 163
    print('QUESTION 16 A (7): '+str(C.getPerfectSqaures(weather))) # 192
    print('QUESTION 17 A (8): '+str(C.getMedianSnowDepth('2008-12-01', '2009-03-01', weather))) # 51.0
   
    print('QUESTION 18 A (2): '+str(C.freestyle(weather))) 
    print('QUESTION 18 B (1): '+'')
    print('QUESTION 18 C (1): '+'')

main1()