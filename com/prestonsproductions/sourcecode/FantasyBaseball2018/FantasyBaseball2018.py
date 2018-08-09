# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2018 - Fantasy Baseball - Team Builder
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Fantasy Baseball - Team Builder
DESCRIPTION: Online fantasy sports applications are an example of using massive data sets to calculate statistics 
and map trends. Behind these platforms is code that processes millions of statistics and run numerous algorithms. 
This test will have you build small pieces of a fantasy sports platform. We will use Major League Baseball as the model
because baseball contains a large number of statistics...and it is the author's favorite. :) 

You will use batting data from the 2016 MLB season (Minimum 20 at-bats). Your code/functions will be tested/graded against batting data
from the 2017 MLB season.
https://www.baseball-reference.com/leagues/MLB/2016-standard-batting.shtml
https://www.baseball-reference.com/leagues/MLB/2017-standard-batting.shtml

1. TASK: For each question, write your code to solve each objective. (return the answer programmatically. ie. via variables)
2. TOTAL POINTS: 114
3. WINNER: High Score
4. TIE BREAKER: Question 19. If there is still a tie, question 18, 17 and so on will break the tie.

TIPS: 
* Some questions may ask you to call functions from previous questions.
* The main function (at bottom) will call and run all of the questions and print the answers. Do not modify this function.
* Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
* Run your program often to test and check for errors.

INFORMATION: The majority of questions will use a list of dictionaries (batting_data). Each item in the list will represent one player. The dictionary
will contain specific data for each player. View the template below:

[
    {
        'NAME':'Mike Trout',     # Name of Player (String)
        'AGE':25,                # Age of Player (Number)
        'TEAM':'LAA',            # Player's Team (String)
        'POSITION':'CF',         # Primary Fielding Position (String)
        'ATBATS':402,            # Total At Bats (Number)
        'RUNS':92,               # Total Runs Scored (Number)
        'HITS':123,              # Total Hits (Number)
        'DOUBLES':25,            # Number of Hits that were Doubles (2 Bases) (Number)
        'TRIPLES':3,             # Number of Hits that were Triples (3 Bases) (Number)
        'HOMERUNS':33,           # Number of Hits that were Homers (4 bases) (Number)
        'RBI':72,                # Total Runs Batted In (Number)
        'WALKS':94,              # Total Walks (Number)
        'STRIKEOUTS':90,         # Total Strikeouts (Number)
    },
    ...
]

GOOD LUCK! '''

# QUESTION 0: TEAM NAME
# OBJECTIVE A (2): Build a string with the name of your fantasy team. 
# Include your school name followed by any text you like. Append the 
# parameter date to the end of your string. Return the name.
# ex return string) Bath High School Super Squad 01/01/2018
def getTeamName(date):
    
    return ''

# QUESTION 1: BASE HIT
# OBJECTIVE A (2): A base hit (or single) is when a player reaches first base, 
# but does not advance for that play. Our data set contains total hits,
# doubles (2B), Triples (3B, and Homeruns, but not singles. Determine how many of the total
# hits were singles. ie. total - 2B - 3B - HR
def getTotalSingles(totalhits, doubles, triples, homeruns):
    total = 0
    
    return total

# QUESTION 2: BATTING AVERAGE
# OBJECTIVE A (2): Batting Average is found by dividing the number
# of Hits by the number of at-bats. The at-bats and hits are parameters
# to the function below (Numbers). Return the average.
# OBJECTIVE B (3): Round the average to 3 decimal places (use round() function)
# and remove the leading 0. Example format: .277
def getBattingAverage(hits, atbats):
    avg = 0
    
    return avg

# QUESTION 3: PLAYERS NAME
# OBJECTIVE A (2): A players name will be passed in as the parameter name.
# The players first and last name will be separated by one space ' '. Split
# the first and last name and return the values in a list. ex) [firstname, lastname]
# OBJECTIVE B (3): The first and last name may not be capitalized. Make sure the
# first character or the players first and last name is capitalized. 
def getFirstLastName(name):

    return []

# QUESTION 4: FANTASY POINTS 
# OBJECTIVE A (3): In fantasy sports, specific statistics are worth a 
# designated number of points. The best way for us to model this is by
# creating a dictionary. Each key will be the statistic name, and the 
# value will be how many points they are worth. Build and return the dictionary
# with the following key, value pairs. NOTE, the values will all be numbers. Make
# sure the key names match exactly as defined here.
# SINGLES:1, DOUBLES:2, TRIPLES:3, HOMERUNS:4, RUNS:2, RBI:2, WALKS:1, STRIKEOUTS:-1
def getPointSystem():

    return ''

# QUESTION 5: AVERAGE PLAYER AGE
# OBJECTIVE A (4): As described in the instructions, the parameter batting_data
# is a list of dictionaries holding players data. (See instructions for specifics. Data comes
# from the main method at the bottom of the file.) To start with this data, find the average
# age of all the players. Return the value. Do not round.
def getAverageAge(batting_data):
    ages = 0

    return ages

# QUESTION 6: POSITION COUNTER
# OBJECTIVE A (4): The function below has parameter of batting_data (List) and a fielding
# position (String) (ie 'CF','1B', etc). Find and return how many players fielding position
# is the value in parameter, position.
# OBJECTIVE B (2): If the position 'DH' (which is not a fielding) position is passed as a position, return -1.
def getPositionCount(batting_data, position):
    count = 0

    return count

# QUESTION 7: GENERIC HIGHEST STAT FINDER
# OBJECTIVE A (5): Using a similar concept of making generic functions as question 6, 
# find the player with the highest/most of the statistic as specified by the parameter
# stat (ie. 'RUNS', 'HITS'). stat will be one of the attributes from a player dictionary
# in batting_data. 
# Return the NAME or names of the player(s) in a list with the highest of the stat.
def getMostStat(batting_data, stat):
    players = []

    return players

# QUESTION 8: FILTER PLAYERS
# OBJECTIVE A (5): The function below has one parameter, which is the batting data.
# Search the list and find all players that have 100 or more RBI. Return the player
# NAMEs in a list.
# OBJECTIVE B (2): Sort the list by first name.
def getPlayers(batting_data):
    players = []

    return players

# QUESTION 9: DOUBLE RANGE
# OBJECTIVE A (5): Find the lowest amount of doubles and highest amount of doubles
# in the batting_data from only players who have 400 ATBATS or more. Return the
# values in a list [lowest doubles, highest doubles]
def getDoubleRange(batting_data):
    doubles = [];

    return doubles

# QUESTION 10: POSITION WITH MOST PLAYERS
# OBJECTIVE A (6): Using the batting data, find the position or positions with the most
# number of players. Return the position(s) in a list.
def getHighestPlayedPosition(batting_data):
    position = []

    return position

# QUESTION 11: SLUGGING PERCENTAGE
# OBJECTIVE A (6): Slugging percentage for a player is calculated by the following equation.
# slugging = ((SINGLES) + (2 * DOUBLES) + (3 * TRIPLES) + (4 * HOMERUNS)) / ATBATS
# Determine the player in the batting data with the highest slugging percentage and has at least 300 ATBATS. 
# Return a list with the player name and slugging percentage (do not round).
def getHighestSlugging(batting_data):
    player = [];

    return player

# QUESTION 12: PLAYERS FANTASY POINTS
# OBJECTIVE A (6): You have used batting_data. Below, this function has one parameter
# representing a dictionary of one player. Get your point system dictionary from 
# question 4 getPointSystem(). For each statistic in the point system, calculate how many points the player
# earned for the season. Sum all the points together and return the total points.
# Remember, each value in getPointSystem() is per 1 statistic. Use getTotalSingles to determine 'SINGLES'. 
# (or rewrite the logic yourself).
def getPlayerPoints(player):
    total = 0;

    return total

# QUESTION 13: TEAM FANTASY POINTS
# OBJECTIVE A (7): Given the batting data and team identifier, team, 
# find the total number of fantasy points earned by the team's players.
# Return the number. Use getPlayerPoints() for each player on the team.
# OBJECTIVE B (2): If the team has more than 4000 points append the string
# 'PRO TEAM' to the number.
def getTeamFantasyPoints(batting_data, team):
    total = 0

    return total

# QUESTION 14: BEST FANTASY TEAM
# OBJECTIVE A (7): You guessed it! What is the optimal fantasy team of batters? The list of batting_data
# is passed into the function below. Also passed in is a dictionary, positions. This includes positions 
# C,1B,2B,3B,SS,LF,CF,RF,DH as the keys. (Designated Hitter instead of pitcher). For each position in the dictionary, positions,
# find the player that would earn the most fantasy points based on getPlayerPoints() function, set that player NAME as the
# value of the position key in the dictionary and return the dictionary. 
# NOTE: Do not consider there being more than one player with the highest points per position.
def getOptimalFantasyTeam(batting_data, positions):

    return {}

# QUESTION 15: ATBATS VARIANCE
# OBJECTIVE A (8): Variance is defined as the average of the squared differences from the mean.
# Use the algorithm below to find the  variance. DO NOT use a built in function.
# 1. Calculate the AVERAGE of the ATBATS.
# 2. Calculate the sum of deviations of each ATBATS by the formula:
#    deviation += (ATBATS - AVERAGE) * (ATBATS - AVERAGE)
# 3. Calculate the average of the deviations values. This is the variance. Return the value.
def getAtBatVariance(batting_data):
    variance = 0

    return variance

# QUESTION 16: IDENTICAL FANTASY POINTS
# OBJECTIVE A (8): Some players might have the same Fantasy Points.
# Determine the points for each player with your function 
# getPlayerPoints(). If two or more players earned the same number
# of points, put and return the results in a dictionary in the following format:
# { '100' : ['Gary Sanchez','Joey Votto'], '200' : ['Carlos Santana','Eric Hosmer'], ... }
# Only consider players with 400 or more at bats.
def getIdenticalPoints(batting_data):
    identicial = {}

    return identicial

# QUESTION 17: PLAYER ANAGRAMS
# OBJECTIVE A (8): An Anagram is a word or phrase that is made up of the exact same characters as
# another word or phrase. The batting_data is passed into the function below along with a string, phrase.
# Write code to find all player names that are an Anagram for the given phrase. Return the player names in a list.
# HINT: Remove the spaces from the phrase and player names. Normalize characters to upper case.
def getAnagrams(batting_data, phrase):
    anagrams = []

    return anagrams


# QUESTION 18: MEDIAN HOMERUNS
# OBJECTIVE A (8): The median is the middle number in a set. If there is an even amount of
# numbers, you average the two middle numbers. Find the median number of HOMERUNS in the batting_data
# and return the number. Do not use a built in library.
# HINT: Sort the list using the sort(key=getHomeRuns) function with key parameter. Use the function getHomeRuns as the key value. 
# HINT: Use Integer Division when searching for the middle index.
def getMedianDuration(batting_data):
    median = 0

    return median

def getHomeRuns(player):
    return player['HOMERUNS']

# QUESTION 19: FREE STYLE
# OBJECTIVE A (2): Write a custom function that calculates a statistic with the batting_data and returns a string
# OBJECTIVE B (1): Write a comment that explains what statistic you are calculating AND why it is important.
# OBJECTIVE C (1): Call a previous function within your calculation.
# DO NOT USE A BUILT IN FUNCTION.
def getStatistic(batting_data):
    x = 0

    return x

###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    positions = {'C':'','1B':'','2B':'','3B':'','SS':'','LF':'','CF':'','RF':'','DH':'',}
      
    # Print Question Answer
    print('Source Code (MAIN) - Division B/C - Fantasy Baseball - Team Builder')
    
    print('QUESTION 0 A (2): '+getTeamName('04/28/2018'))
    print('QUESTION 1 A (2): '+str(getTotalSingles(178,29,3,22)))
    
    print('QUESTION 2 A (2): '+str(getBattingAverage(175, 583)))
    print('QUESTION 2 B (3): '+str(getBattingAverage(175, 583)))
    
    print('QUESTION 3 A (2): '+str(getFirstLastName('edwin encarnacion')))
    print('QUESTION 3 B (3): '+str(getFirstLastName('edwin encarnacion')))
    
    print('QUESTION 4 A (3): '+str(getPointSystem()))
    print('QUESTION 5 A (4): '+str(getAverageAge(batting_data_2016)))
    
    print('QUESTION 6 A (4): '+str(getPositionCount(batting_data_2016, 'LF')))
    print('QUESTION 6 B (2): '+str(getPositionCount(batting_data_2016, 'DH')))
    
    print('QUESTION 7 A (5): '+str(getMostStat(batting_data_2016,'WALKS')))
    
    print('QUESTION 8 A (5): '+str(getPlayers(batting_data_2016)))
    print('QUESTION 8 B (2): '+str(getPlayers(batting_data_2016)))
    
    print('QUESTION 9 A (5): '+str(getDoubleRange(batting_data_2016)))
    print('QUESTION 10 A (6): '+str(getHighestPlayedPosition(batting_data_2016)))    
    print('QUESTION 11 A (6): '+str(getHighestSlugging(batting_data_2016)))
    print('QUESTION 12 A (6): '+str(getPlayerPoints({'NAME':'Miguel Cabrera','AGE':33,'TEAM':'DET','POSITION':'1B','ATBATS':595,'RUNS':92,'HITS':188,'DOUBLES':31,'TRIPLES':1,'HOMERUNS':38,'RBI':108,'WALKS':75,'STRIKEOUTS':116,})))
  
    print('QUESTION 13 A (7): '+str(getTeamFantasyPoints(batting_data_2016,'ATL'))) 
    print('QUESTION 13 B (2): '+str(getTeamFantasyPoints(batting_data_2016,'CHC')))
    
    print('QUESTION 14 A (7): '+str(getOptimalFantasyTeam(batting_data_2016, positions)))
    print('QUESTION 15 A (8): '+str(getAtBatVariance(batting_data_2016)))
    print('QUESTION 16 A (8): '+str(getIdenticalPoints(batting_data_2016)))
    print('QUESTION 17 A (8): '+str(getAnagrams(batting_data_2016, 'grey ke sale')))
    print('QUESTION 18 A (8): '+str(getMedianDuration(batting_data_2016)))
    
    print('QUESTION 19 A (2): '+str(getStatistic(batting_data_2016))) # Check for Answer
    print('QUESTION 19 B (1): '+'Check for comment explaining function.')
    print('QUESTION 19 C (1): '+'Check if previous function in file was called.')
    
batting_data_2016 = [
    {'NAME':'Mookie Betts','AGE':23,'TEAM':'BOS','POSITION':'RF','ATBATS':672,'RUNS':122,'HITS':214,'DOUBLES':42,'TRIPLES':5,'HOMERUNS':31,'RBI':113,'WALKS':49,'STRIKEOUTS':80,},
{'NAME':'Robinson Cano','AGE':33,'TEAM':'SEA','POSITION':'2B','ATBATS':655,'RUNS':107,'HITS':195,'DOUBLES':33,'TRIPLES':2,'HOMERUNS':39,'RBI':103,'WALKS':47,'STRIKEOUTS':100,},
{'NAME':'Xander Bogaerts','AGE':23,'TEAM':'BOS','POSITION':'SS','ATBATS':652,'RUNS':115,'HITS':192,'DOUBLES':34,'TRIPLES':1,'HOMERUNS':21,'RBI':89,'WALKS':58,'STRIKEOUTS':123,},
{'NAME':'George Springer','AGE':26,'TEAM':'HOU','POSITION':'RF','ATBATS':644,'RUNS':116,'HITS':168,'DOUBLES':29,'TRIPLES':5,'HOMERUNS':29,'RBI':82,'WALKS':88,'STRIKEOUTS':178,},
{'NAME':'Jose Altuve','AGE':26,'TEAM':'HOU','POSITION':'2B','ATBATS':640,'RUNS':108,'HITS':216,'DOUBLES':42,'TRIPLES':5,'HOMERUNS':24,'RBI':96,'WALKS':60,'STRIKEOUTS':70,},
{'NAME':'Manny Machado','AGE':23,'TEAM':'BAL','POSITION':'3B','ATBATS':640,'RUNS':105,'HITS':188,'DOUBLES':40,'TRIPLES':1,'HOMERUNS':37,'RBI':96,'WALKS':48,'STRIKEOUTS':120,},
{'NAME':'Alcides Escobar','AGE':29,'TEAM':'KCR','POSITION':'SS','ATBATS':637,'RUNS':57,'HITS':166,'DOUBLES':24,'TRIPLES':6,'HOMERUNS':7,'RBI':55,'WALKS':27,'STRIKEOUTS':96,},
{'NAME':'Jean Segura','AGE':26,'TEAM':'ARI','POSITION':'2B','ATBATS':637,'RUNS':102,'HITS':203,'DOUBLES':41,'TRIPLES':7,'HOMERUNS':20,'RBI':64,'WALKS':39,'STRIKEOUTS':101,},
{'NAME':'Evan Longoria','AGE':30,'TEAM':'TBR','POSITION':'3B','ATBATS':633,'RUNS':81,'HITS':173,'DOUBLES':41,'TRIPLES':4,'HOMERUNS':36,'RBI':98,'WALKS':42,'STRIKEOUTS':144,},
{'NAME':'Dustin Pedroia','AGE':32,'TEAM':'BOS','POSITION':'2B','ATBATS':633,'RUNS':105,'HITS':201,'DOUBLES':36,'TRIPLES':1,'HOMERUNS':15,'RBI':74,'WALKS':61,'STRIKEOUTS':73,},
{'NAME':'Corey Seager','AGE':22,'TEAM':'LAD','POSITION':'SS','ATBATS':627,'RUNS':105,'HITS':193,'DOUBLES':40,'TRIPLES':5,'HOMERUNS':26,'RBI':72,'WALKS':54,'STRIKEOUTS':133,},
{'NAME':'Ian Desmond','AGE':30,'TEAM':'TEX','POSITION':'CF','ATBATS':625,'RUNS':107,'HITS':178,'DOUBLES':29,'TRIPLES':3,'HOMERUNS':22,'RBI':86,'WALKS':44,'STRIKEOUTS':160,},
{'NAME':'Jose Abreu','AGE':29,'TEAM':'CHW','POSITION':'1B','ATBATS':624,'RUNS':67,'HITS':183,'DOUBLES':32,'TRIPLES':1,'HOMERUNS':25,'RBI':100,'WALKS':47,'STRIKEOUTS':125,},
{'NAME':'Matt Kemp','AGE':31,'TEAM':'TOT','POSITION':'RF','ATBATS':623,'RUNS':89,'HITS':167,'DOUBLES':39,'TRIPLES':0,'HOMERUNS':35,'RBI':108,'WALKS':36,'STRIKEOUTS':156,},
{'NAME':'Adam Eaton','AGE':27,'TEAM':'CHW','POSITION':'RF','ATBATS':619,'RUNS':91,'HITS':176,'DOUBLES':29,'TRIPLES':9,'HOMERUNS':14,'RBI':59,'WALKS':63,'STRIKEOUTS':115,},
{'NAME':'Adam Jones','AGE':30,'TEAM':'BAL','POSITION':'CF','ATBATS':619,'RUNS':86,'HITS':164,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':29,'RBI':83,'WALKS':39,'STRIKEOUTS':115,},
{'NAME':'Nolan Arenado','AGE':25,'TEAM':'COL','POSITION':'3B','ATBATS':618,'RUNS':116,'HITS':182,'DOUBLES':35,'TRIPLES':6,'HOMERUNS':41,'RBI':133,'WALKS':68,'STRIKEOUTS':103,},
{'NAME':'Ian Kinsler','AGE':34,'TEAM':'DET','POSITION':'2B','ATBATS':618,'RUNS':117,'HITS':178,'DOUBLES':29,'TRIPLES':4,'HOMERUNS':28,'RBI':83,'WALKS':45,'STRIKEOUTS':115,},
{'NAME':'Brian Dozier','AGE':29,'TEAM':'MIN','POSITION':'2B','ATBATS':615,'RUNS':104,'HITS':165,'DOUBLES':35,'TRIPLES':5,'HOMERUNS':42,'RBI':99,'WALKS':61,'STRIKEOUTS':138,},
{'NAME':'Jonathan Schoop','AGE':24,'TEAM':'BAL','POSITION':'2B','ATBATS':615,'RUNS':82,'HITS':164,'DOUBLES':38,'TRIPLES':1,'HOMERUNS':25,'RBI':82,'WALKS':21,'STRIKEOUTS':137,},
{'NAME':'Mark Trumbo','AGE':30,'TEAM':'BAL','POSITION':'RF','ATBATS':613,'RUNS':94,'HITS':157,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':47,'RBI':108,'WALKS':51,'STRIKEOUTS':170,},
{'NAME':'Jason Kipnis','AGE':29,'TEAM':'CLE','POSITION':'2B','ATBATS':610,'RUNS':91,'HITS':168,'DOUBLES':41,'TRIPLES':4,'HOMERUNS':23,'RBI':82,'WALKS':60,'STRIKEOUTS':146,},
{'NAME':'Eric Hosmer','AGE':26,'TEAM':'KCR','POSITION':'1B','ATBATS':605,'RUNS':80,'HITS':161,'DOUBLES':24,'TRIPLES':1,'HOMERUNS':25,'RBI':104,'WALKS':57,'STRIKEOUTS':132,},
{'NAME':'Rougned Odor','AGE':22,'TEAM':'TEX','POSITION':'2B','ATBATS':605,'RUNS':89,'HITS':164,'DOUBLES':33,'TRIPLES':4,'HOMERUNS':33,'RBI':88,'WALKS':19,'STRIKEOUTS':135,},
{'NAME':'Francisco Lindor','AGE':22,'TEAM':'CLE','POSITION':'SS','ATBATS':604,'RUNS':99,'HITS':182,'DOUBLES':30,'TRIPLES':3,'HOMERUNS':15,'RBI':78,'WALKS':57,'STRIKEOUTS':88,},
{'NAME':'Kris Bryant','AGE':24,'TEAM':'CHC','POSITION':'3B','ATBATS':603,'RUNS':121,'HITS':176,'DOUBLES':35,'TRIPLES':3,'HOMERUNS':39,'RBI':102,'WALKS':75,'STRIKEOUTS':154,},
{'NAME':'Edwin Encarnacion','AGE':33,'TEAM':'TOR','POSITION':'DH','ATBATS':601,'RUNS':99,'HITS':158,'DOUBLES':34,'TRIPLES':0,'HOMERUNS':42,'RBI':127,'WALKS':87,'STRIKEOUTS':138,},
{'NAME':'Martin Prado','AGE':32,'TEAM':'MIA','POSITION':'3B','ATBATS':600,'RUNS':70,'HITS':183,'DOUBLES':37,'TRIPLES':3,'HOMERUNS':8,'RBI':75,'WALKS':49,'STRIKEOUTS':69,},
{'NAME':'Nick Markakis','AGE':32,'TEAM':'ATL','POSITION':'RF','ATBATS':599,'RUNS':67,'HITS':161,'DOUBLES':38,'TRIPLES':0,'HOMERUNS':13,'RBI':89,'WALKS':71,'STRIKEOUTS':101,},
{'NAME':'Wil Myers','AGE':25,'TEAM':'SDP','POSITION':'1B','ATBATS':599,'RUNS':99,'HITS':155,'DOUBLES':29,'TRIPLES':4,'HOMERUNS':28,'RBI':94,'WALKS':68,'STRIKEOUTS':160,},
{'NAME':'Andrew McCutchen','AGE':29,'TEAM':'PIT','POSITION':'CF','ATBATS':598,'RUNS':81,'HITS':153,'DOUBLES':26,'TRIPLES':3,'HOMERUNS':24,'RBI':79,'WALKS':69,'STRIKEOUTS':143,},
{'NAME':'Kyle Seager','AGE':28,'TEAM':'SEA','POSITION':'3B','ATBATS':597,'RUNS':89,'HITS':166,'DOUBLES':36,'TRIPLES':3,'HOMERUNS':30,'RBI':99,'WALKS':69,'STRIKEOUTS':108,},
{'NAME':'Miguel Cabrera','AGE':33,'TEAM':'DET','POSITION':'1B','ATBATS':595,'RUNS':92,'HITS':188,'DOUBLES':31,'TRIPLES':1,'HOMERUNS':38,'RBI':108,'WALKS':75,'STRIKEOUTS':116,},
{'NAME':'Kole Calhoun','AGE':28,'TEAM':'LAA','POSITION':'RF','ATBATS':594,'RUNS':91,'HITS':161,'DOUBLES':35,'TRIPLES':5,'HOMERUNS':18,'RBI':75,'WALKS':67,'STRIKEOUTS':118,},
{'NAME':'Albert Pujols','AGE':36,'TEAM':'LAA','POSITION':'DH','ATBATS':593,'RUNS':71,'HITS':159,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':31,'RBI':119,'WALKS':49,'STRIKEOUTS':75,},
{'NAME':'Melky Cabrera','AGE':31,'TEAM':'CHW','POSITION':'LF','ATBATS':591,'RUNS':70,'HITS':175,'DOUBLES':42,'TRIPLES':5,'HOMERUNS':14,'RBI':86,'WALKS':47,'STRIKEOUTS':69,},
{'NAME':'Todd Frazier','AGE':30,'TEAM':'CHW','POSITION':'3B','ATBATS':590,'RUNS':89,'HITS':133,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':40,'RBI':98,'WALKS':64,'STRIKEOUTS':163,},
{'NAME':'Nelson Cruz','AGE':35,'TEAM':'SEA','POSITION':'DH','ATBATS':589,'RUNS':96,'HITS':169,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':43,'RBI':105,'WALKS':62,'STRIKEOUTS':159,},
{'NAME':'Freddie Freeman','AGE':26,'TEAM':'ATL','POSITION':'1B','ATBATS':589,'RUNS':102,'HITS':178,'DOUBLES':43,'TRIPLES':6,'HOMERUNS':34,'RBI':91,'WALKS':89,'STRIKEOUTS':171,},
{'NAME':'Jonathan Villar','AGE':25,'TEAM':'MIL','POSITION':'SS','ATBATS':589,'RUNS':92,'HITS':168,'DOUBLES':38,'TRIPLES':3,'HOMERUNS':19,'RBI':63,'WALKS':79,'STRIKEOUTS':174,},
{'NAME':'Freddy Galvis','AGE':26,'TEAM':'PHI','POSITION':'SS','ATBATS':584,'RUNS':61,'HITS':141,'DOUBLES':26,'TRIPLES':3,'HOMERUNS':20,'RBI':67,'WALKS':25,'STRIKEOUTS':136,},
{'NAME':'Carlos Gonzalez','AGE':30,'TEAM':'COL','POSITION':'RF','ATBATS':584,'RUNS':87,'HITS':174,'DOUBLES':42,'TRIPLES':2,'HOMERUNS':25,'RBI':100,'WALKS':46,'STRIKEOUTS':129,},
{'NAME':'Adrian Beltre','AGE':37,'TEAM':'TEX','POSITION':'3B','ATBATS':583,'RUNS':89,'HITS':175,'DOUBLES':31,'TRIPLES':1,'HOMERUNS':32,'RBI':104,'WALKS':48,'STRIKEOUTS':66,},
{'NAME':'Odubel Herrera','AGE':24,'TEAM':'PHI','POSITION':'CF','ATBATS':583,'RUNS':87,'HITS':167,'DOUBLES':21,'TRIPLES':6,'HOMERUNS':15,'RBI':49,'WALKS':63,'STRIKEOUTS':134,},
{'NAME':'Anthony Rizzo','AGE':26,'TEAM':'CHC','POSITION':'1B','ATBATS':583,'RUNS':94,'HITS':170,'DOUBLES':43,'TRIPLES':4,'HOMERUNS':32,'RBI':109,'WALKS':74,'STRIKEOUTS':108,},
{'NAME':'Stephen Piscotty','AGE':25,'TEAM':'STL','POSITION':'RF','ATBATS':582,'RUNS':86,'HITS':159,'DOUBLES':35,'TRIPLES':3,'HOMERUNS':22,'RBI':85,'WALKS':51,'STRIKEOUTS':133,},
{'NAME':'Carlos Santana','AGE':30,'TEAM':'CLE','POSITION':'DH','ATBATS':582,'RUNS':89,'HITS':151,'DOUBLES':31,'TRIPLES':3,'HOMERUNS':34,'RBI':87,'WALKS':99,'STRIKEOUTS':99,},
{'NAME':'Maikel Franco','AGE':23,'TEAM':'PHI','POSITION':'3B','ATBATS':581,'RUNS':67,'HITS':148,'DOUBLES':23,'TRIPLES':1,'HOMERUNS':25,'RBI':88,'WALKS':40,'STRIKEOUTS':106,},
{'NAME':'Paul Goldschmidt','AGE':28,'TEAM':'ARI','POSITION':'1B','ATBATS':579,'RUNS':106,'HITS':172,'DOUBLES':33,'TRIPLES':3,'HOMERUNS':24,'RBI':95,'WALKS':110,'STRIKEOUTS':150,},
{'NAME':'Charlie Blackmon','AGE':29,'TEAM':'COL','POSITION':'CF','ATBATS':578,'RUNS':111,'HITS':187,'DOUBLES':35,'TRIPLES':5,'HOMERUNS':29,'RBI':82,'WALKS':43,'STRIKEOUTS':102,},
{'NAME':'Christian Yelich','AGE':24,'TEAM':'MIA','POSITION':'LF','ATBATS':578,'RUNS':78,'HITS':172,'DOUBLES':38,'TRIPLES':3,'HOMERUNS':21,'RBI':98,'WALKS':72,'STRIKEOUTS':138,},
{'NAME':'Starlin Castro','AGE':26,'TEAM':'NYY','POSITION':'2B','ATBATS':577,'RUNS':63,'HITS':156,'DOUBLES':29,'TRIPLES':1,'HOMERUNS':21,'RBI':70,'WALKS':24,'STRIKEOUTS':118,},
{'NAME':'Carlos Correa','AGE':21,'TEAM':'HOU','POSITION':'SS','ATBATS':577,'RUNS':76,'HITS':158,'DOUBLES':36,'TRIPLES':3,'HOMERUNS':20,'RBI':96,'WALKS':75,'STRIKEOUTS':139,},
{'NAME':'Josh Donaldson','AGE':30,'TEAM':'TOR','POSITION':'3B','ATBATS':577,'RUNS':122,'HITS':164,'DOUBLES':32,'TRIPLES':5,'HOMERUNS':37,'RBI':99,'WALKS':109,'STRIKEOUTS':119,},
{'NAME':'Denard Span','AGE':32,'TEAM':'SFG','POSITION':'CF','ATBATS':572,'RUNS':70,'HITS':152,'DOUBLES':23,'TRIPLES':5,'HOMERUNS':11,'RBI':53,'WALKS':53,'STRIKEOUTS':79,},
{'NAME':'Justin Upton','AGE':28,'TEAM':'DET','POSITION':'LF','ATBATS':570,'RUNS':81,'HITS':140,'DOUBLES':28,'TRIPLES':2,'HOMERUNS':31,'RBI':87,'WALKS':50,'STRIKEOUTS':179,},
{'NAME':'Adrian Gonzalez','AGE':34,'TEAM':'LAD','POSITION':'1B','ATBATS':568,'RUNS':69,'HITS':162,'DOUBLES':31,'TRIPLES':0,'HOMERUNS':18,'RBI':90,'WALKS':55,'STRIKEOUTS':117,},
{'NAME':'Marcus Semien','AGE':25,'TEAM':'OAK','POSITION':'SS','ATBATS':568,'RUNS':72,'HITS':135,'DOUBLES':27,'TRIPLES':2,'HOMERUNS':27,'RBI':75,'WALKS':51,'STRIKEOUTS':139,},
{'NAME':'Anthony Rendon','AGE':26,'TEAM':'WSN','POSITION':'3B','ATBATS':567,'RUNS':91,'HITS':153,'DOUBLES':38,'TRIPLES':2,'HOMERUNS':20,'RBI':85,'WALKS':65,'STRIKEOUTS':117,},
{'NAME':'Chris Davis','AGE':30,'TEAM':'BAL','POSITION':'1B','ATBATS':566,'RUNS':99,'HITS':125,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':38,'RBI':84,'WALKS':88,'STRIKEOUTS':219,},
{'NAME':'Jose Ramirez','AGE':23,'TEAM':'CLE','POSITION':'3B','ATBATS':565,'RUNS':84,'HITS':176,'DOUBLES':46,'TRIPLES':3,'HOMERUNS':11,'RBI':76,'WALKS':44,'STRIKEOUTS':62,},
{'NAME':'Eugenio Suarez','AGE':24,'TEAM':'CIN','POSITION':'3B','ATBATS':565,'RUNS':78,'HITS':140,'DOUBLES':25,'TRIPLES':2,'HOMERUNS':21,'RBI':70,'WALKS':51,'STRIKEOUTS':155,},
{'NAME':'Didi Gregorius','AGE':26,'TEAM':'NYY','POSITION':'SS','ATBATS':562,'RUNS':68,'HITS':155,'DOUBLES':32,'TRIPLES':2,'HOMERUNS':20,'RBI':70,'WALKS':19,'STRIKEOUTS':82,},
{'NAME':'Jackie Bradley','AGE':26,'TEAM':'BOS','POSITION':'CF','ATBATS':558,'RUNS':94,'HITS':149,'DOUBLES':30,'TRIPLES':7,'HOMERUNS':26,'RBI':87,'WALKS':63,'STRIKEOUTS':143,},
{'NAME':'Kendrys Morales','AGE':33,'TEAM':'KCR','POSITION':'DH','ATBATS':558,'RUNS':65,'HITS':147,'DOUBLES':24,'TRIPLES':0,'HOMERUNS':30,'RBI':93,'WALKS':48,'STRIKEOUTS':120,},
{'NAME':'Mike Napoli','AGE':34,'TEAM':'CLE','POSITION':'1B','ATBATS':557,'RUNS':92,'HITS':133,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':34,'RBI':101,'WALKS':78,'STRIKEOUTS':194,},
{'NAME':'Marcell Ozuna','AGE':25,'TEAM':'MIA','POSITION':'CF','ATBATS':557,'RUNS':75,'HITS':148,'DOUBLES':23,'TRIPLES':6,'HOMERUNS':23,'RBI':76,'WALKS':43,'STRIKEOUTS':115,},
{'NAME':'Justin Turner','AGE':31,'TEAM':'LAD','POSITION':'3B','ATBATS':556,'RUNS':79,'HITS':153,'DOUBLES':34,'TRIPLES':3,'HOMERUNS':27,'RBI':90,'WALKS':48,'STRIKEOUTS':107,},
{'NAME':'Joey Votto','AGE':32,'TEAM':'CIN','POSITION':'1B','ATBATS':556,'RUNS':101,'HITS':181,'DOUBLES':34,'TRIPLES':2,'HOMERUNS':29,'RBI':97,'WALKS':108,'STRIKEOUTS':120,},
{'NAME':'Khris Davis','AGE':28,'TEAM':'OAK','POSITION':'LF','ATBATS':555,'RUNS':85,'HITS':137,'DOUBLES':24,'TRIPLES':2,'HOMERUNS':42,'RBI':102,'WALKS':42,'STRIKEOUTS':166,},
{'NAME':'Brandon Crawford','AGE':29,'TEAM':'SFG','POSITION':'SS','ATBATS':553,'RUNS':67,'HITS':152,'DOUBLES':28,'TRIPLES':11,'HOMERUNS':12,'RBI':84,'WALKS':57,'STRIKEOUTS':115,},
{'NAME':'Victor Martinez','AGE':37,'TEAM':'DET','POSITION':'DH','ATBATS':553,'RUNS':65,'HITS':160,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':27,'RBI':86,'WALKS':50,'STRIKEOUTS':90,},
{'NAME':'Eduardo Nunez','AGE':29,'TEAM':'TOT','POSITION':'3B','ATBATS':553,'RUNS':73,'HITS':159,'DOUBLES':24,'TRIPLES':4,'HOMERUNS':16,'RBI':67,'WALKS':29,'STRIKEOUTS':88,},
{'NAME':'Carlos Beltran','AGE':39,'TEAM':'TOT','POSITION':'DH','ATBATS':552,'RUNS':73,'HITS':163,'DOUBLES':33,'TRIPLES':0,'HOMERUNS':29,'RBI':93,'WALKS':35,'STRIKEOUTS':101,},
{'NAME':'Adam Duvall','AGE':27,'TEAM':'CIN','POSITION':'LF','ATBATS':552,'RUNS':85,'HITS':133,'DOUBLES':31,'TRIPLES':6,'HOMERUNS':33,'RBI':103,'WALKS':41,'STRIKEOUTS':164,},
{'NAME':'DJ LeMahieu','AGE':27,'TEAM':'COL','POSITION':'2B','ATBATS':552,'RUNS':104,'HITS':192,'DOUBLES':32,'TRIPLES':8,'HOMERUNS':11,'RBI':66,'WALKS':66,'STRIKEOUTS':80,},
{'NAME':'Jacoby Ellsbury','AGE':32,'TEAM':'NYY','POSITION':'CF','ATBATS':551,'RUNS':71,'HITS':145,'DOUBLES':24,'TRIPLES':5,'HOMERUNS':9,'RBI':56,'WALKS':54,'STRIKEOUTS':84,},
{'NAME':'Brandon Phillips','AGE':35,'TEAM':'CIN','POSITION':'2B','ATBATS':550,'RUNS':74,'HITS':160,'DOUBLES':34,'TRIPLES':1,'HOMERUNS':11,'RBI':64,'WALKS':18,'STRIKEOUTS':68,},
{'NAME':'Chris Carter','AGE':29,'TEAM':'MIL','POSITION':'1B','ATBATS':549,'RUNS':84,'HITS':122,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':41,'RBI':94,'WALKS':76,'STRIKEOUTS':206,},
{'NAME':'Hanley Ramirez','AGE':32,'TEAM':'BOS','POSITION':'1B','ATBATS':549,'RUNS':81,'HITS':157,'DOUBLES':28,'TRIPLES':1,'HOMERUNS':30,'RBI':111,'WALKS':60,'STRIKEOUTS':120,},
{'NAME':'Mike Trout','AGE':24,'TEAM':'LAA','POSITION':'CF','ATBATS':549,'RUNS':123,'HITS':173,'DOUBLES':32,'TRIPLES':5,'HOMERUNS':29,'RBI':100,'WALKS':116,'STRIKEOUTS':137,},
{'NAME':'Brad Miller','AGE':26,'TEAM':'TBR','POSITION':'SS','ATBATS':548,'RUNS':73,'HITS':133,'DOUBLES':29,'TRIPLES':6,'HOMERUNS':30,'RBI':81,'WALKS':47,'STRIKEOUTS':149,},
{'NAME':'Kevin Pillar','AGE':27,'TEAM':'TOR','POSITION':'CF','ATBATS':548,'RUNS':59,'HITS':146,'DOUBLES':35,'TRIPLES':2,'HOMERUNS':7,'RBI':53,'WALKS':24,'STRIKEOUTS':90,},
{'NAME':'Brett Gardner','AGE':32,'TEAM':'NYY','POSITION':'LF','ATBATS':547,'RUNS':80,'HITS':143,'DOUBLES':22,'TRIPLES':6,'HOMERUNS':7,'RBI':41,'WALKS':70,'STRIKEOUTS':106,},
{'NAME':'Cesar Hernandez','AGE':26,'TEAM':'PHI','POSITION':'2B','ATBATS':547,'RUNS':67,'HITS':161,'DOUBLES':14,'TRIPLES':11,'HOMERUNS':6,'RBI':39,'WALKS':66,'STRIKEOUTS':116,},
{'NAME':'Curtis Granderson','AGE':35,'TEAM':'NYM','POSITION':'RF','ATBATS':545,'RUNS':88,'HITS':129,'DOUBLES':24,'TRIPLES':5,'HOMERUNS':30,'RBI':59,'WALKS':74,'STRIKEOUTS':130,},
{'NAME':'Brandon Belt','AGE':28,'TEAM':'SFG','POSITION':'1B','ATBATS':542,'RUNS':77,'HITS':149,'DOUBLES':41,'TRIPLES':8,'HOMERUNS':17,'RBI':82,'WALKS':104,'STRIKEOUTS':148,},
{'NAME':'Jay Bruce','AGE':29,'TEAM':'TOT','POSITION':'RF','ATBATS':539,'RUNS':74,'HITS':135,'DOUBLES':27,'TRIPLES':6,'HOMERUNS':33,'RBI':99,'WALKS':44,'STRIKEOUTS':126,},
{'NAME':'Buster Posey','AGE':29,'TEAM':'SFG','POSITION':'C','ATBATS':539,'RUNS':82,'HITS':155,'DOUBLES':33,'TRIPLES':2,'HOMERUNS':14,'RBI':80,'WALKS':64,'STRIKEOUTS':68,},
{'NAME':'David Ortiz','AGE':40,'TEAM':'BOS','POSITION':'DH','ATBATS':537,'RUNS':79,'HITS':169,'DOUBLES':48,'TRIPLES':1,'HOMERUNS':38,'RBI':127,'WALKS':80,'STRIKEOUTS':86,},
{'NAME':'Yadier Molina','AGE':33,'TEAM':'STL','POSITION':'C','ATBATS':534,'RUNS':56,'HITS':164,'DOUBLES':38,'TRIPLES':1,'HOMERUNS':8,'RBI':58,'WALKS':39,'STRIKEOUTS':63,},
{'NAME':'Adonis Garcia','AGE':31,'TEAM':'ATL','POSITION':'3B','ATBATS':532,'RUNS':65,'HITS':145,'DOUBLES':29,'TRIPLES':0,'HOMERUNS':14,'RBI':65,'WALKS':24,'STRIKEOUTS':93,},
{'NAME':'Daniel Murphy','AGE':31,'TEAM':'WSN','POSITION':'2B','ATBATS':531,'RUNS':88,'HITS':184,'DOUBLES':47,'TRIPLES':5,'HOMERUNS':25,'RBI':104,'WALKS':35,'STRIKEOUTS':57,},
{'NAME':'Jason Heyward','AGE':26,'TEAM':'CHC','POSITION':'RF','ATBATS':530,'RUNS':61,'HITS':122,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':7,'RBI':49,'WALKS':54,'STRIKEOUTS':93,},
{'NAME':'Yasmany Tomas','AGE':25,'TEAM':'ARI','POSITION':'RF','ATBATS':530,'RUNS':72,'HITS':144,'DOUBLES':30,'TRIPLES':1,'HOMERUNS':31,'RBI':83,'WALKS':31,'STRIKEOUTS':136,},
{'NAME':'Gregory Polanco','AGE':24,'TEAM':'PIT','POSITION':'RF','ATBATS':527,'RUNS':79,'HITS':136,'DOUBLES':34,'TRIPLES':4,'HOMERUNS':22,'RBI':86,'WALKS':53,'STRIKEOUTS':119,},
{'NAME':'Addison Russell','AGE':22,'TEAM':'CHC','POSITION':'SS','ATBATS':525,'RUNS':67,'HITS':125,'DOUBLES':25,'TRIPLES':3,'HOMERUNS':21,'RBI':95,'WALKS':55,'STRIKEOUTS':135,},
{'NAME':'Jayson Werth','AGE':37,'TEAM':'WSN','POSITION':'LF','ATBATS':525,'RUNS':84,'HITS':128,'DOUBLES':28,'TRIPLES':0,'HOMERUNS':21,'RBI':69,'WALKS':71,'STRIKEOUTS':139,},
{'NAME':'Jake Lamb','AGE':25,'TEAM':'ARI','POSITION':'3B','ATBATS':523,'RUNS':81,'HITS':130,'DOUBLES':31,'TRIPLES':9,'HOMERUNS':29,'RBI':91,'WALKS':64,'STRIKEOUTS':154,},
{'NAME':'Ben Zobrist','AGE':35,'TEAM':'CHC','POSITION':'2B','ATBATS':523,'RUNS':94,'HITS':142,'DOUBLES':31,'TRIPLES':3,'HOMERUNS':18,'RBI':76,'WALKS':96,'STRIKEOUTS':82,},
{'NAME':'Ender Inciarte','AGE':25,'TEAM':'ATL','POSITION':'CF','ATBATS':522,'RUNS':85,'HITS':152,'DOUBLES':24,'TRIPLES':7,'HOMERUNS':3,'RBI':29,'WALKS':45,'STRIKEOUTS':68,},
{'NAME':'Asdrubal Cabrera','AGE':30,'TEAM':'NYM','POSITION':'SS','ATBATS':521,'RUNS':65,'HITS':146,'DOUBLES':30,'TRIPLES':1,'HOMERUNS':23,'RBI':62,'WALKS':38,'STRIKEOUTS':103,},
{'NAME':'Jordy Mercer','AGE':29,'TEAM':'PIT','POSITION':'SS','ATBATS':519,'RUNS':66,'HITS':133,'DOUBLES':22,'TRIPLES':3,'HOMERUNS':11,'RBI':59,'WALKS':51,'STRIKEOUTS':83,},
{'NAME':'Leonys Martin','AGE':28,'TEAM':'SEA','POSITION':'CF','ATBATS':518,'RUNS':72,'HITS':128,'DOUBLES':17,'TRIPLES':3,'HOMERUNS':15,'RBI':47,'WALKS':44,'STRIKEOUTS':149,},
{'NAME':'Yunel Escobar','AGE':33,'TEAM':'LAA','POSITION':'3B','ATBATS':517,'RUNS':68,'HITS':157,'DOUBLES':28,'TRIPLES':1,'HOMERUNS':5,'RBI':39,'WALKS':40,'STRIKEOUTS':67,},
{'NAME':'Danny Espinosa','AGE':29,'TEAM':'WSN','POSITION':'SS','ATBATS':516,'RUNS':66,'HITS':108,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':24,'RBI':72,'WALKS':54,'STRIKEOUTS':174,},
{'NAME':'Nomar Mazara','AGE':21,'TEAM':'TEX','POSITION':'RF','ATBATS':516,'RUNS':59,'HITS':137,'DOUBLES':13,'TRIPLES':3,'HOMERUNS':20,'RBI':64,'WALKS':39,'STRIKEOUTS':112,},
{'NAME':'Salvador Perez','AGE':26,'TEAM':'KCR','POSITION':'C','ATBATS':514,'RUNS':57,'HITS':127,'DOUBLES':28,'TRIPLES':2,'HOMERUNS':22,'RBI':64,'WALKS':22,'STRIKEOUTS':119,},
{'NAME':'Chase Utley','AGE':37,'TEAM':'LAD','POSITION':'2B','ATBATS':512,'RUNS':79,'HITS':129,'DOUBLES':26,'TRIPLES':3,'HOMERUNS':14,'RBI':52,'WALKS':40,'STRIKEOUTS':115,},
{'NAME':'Ryan Braun','AGE':32,'TEAM':'MIL','POSITION':'LF','ATBATS':511,'RUNS':80,'HITS':156,'DOUBLES':23,'TRIPLES':3,'HOMERUNS':30,'RBI':91,'WALKS':46,'STRIKEOUTS':98,},
{'NAME':'Logan Forsythe','AGE':29,'TEAM':'TBR','POSITION':'2B','ATBATS':511,'RUNS':76,'HITS':135,'DOUBLES':24,'TRIPLES':4,'HOMERUNS':20,'RBI':52,'WALKS':46,'STRIKEOUTS':127,},
{'NAME':'Corey Dickerson','AGE':27,'TEAM':'TBR','POSITION':'LF','ATBATS':510,'RUNS':57,'HITS':125,'DOUBLES':36,'TRIPLES':3,'HOMERUNS':24,'RBI':70,'WALKS':33,'STRIKEOUTS':134,},
{'NAME':'J.T. Realmuto','AGE':25,'TEAM':'MIA','POSITION':'C','ATBATS':509,'RUNS':60,'HITS':154,'DOUBLES':31,'TRIPLES':0,'HOMERUNS':11,'RBI':48,'WALKS':28,'STRIKEOUTS':100,},
{'NAME':'Adeiny Hechavarria','AGE':27,'TEAM':'MIA','POSITION':'SS','ATBATS':508,'RUNS':52,'HITS':120,'DOUBLES':17,'TRIPLES':6,'HOMERUNS':3,'RBI':38,'WALKS':33,'STRIKEOUTS':73,},
{'NAME':'Elvis Andrus','AGE':27,'TEAM':'TEX','POSITION':'SS','ATBATS':506,'RUNS':75,'HITS':153,'DOUBLES':31,'TRIPLES':7,'HOMERUNS':8,'RBI':69,'WALKS':47,'STRIKEOUTS':70,},
{'NAME':'Bryce Harper','AGE':23,'TEAM':'WSN','POSITION':'RF','ATBATS':506,'RUNS':84,'HITS':123,'DOUBLES':24,'TRIPLES':2,'HOMERUNS':24,'RBI':86,'WALKS':108,'STRIKEOUTS':117,},
{'NAME':'Scooter Gennett','AGE':26,'TEAM':'MIL','POSITION':'2B','ATBATS':498,'RUNS':58,'HITS':131,'DOUBLES':30,'TRIPLES':1,'HOMERUNS':14,'RBI':56,'WALKS':38,'STRIKEOUTS':114,},
{'NAME':'Angel Pagan','AGE':34,'TEAM':'SFG','POSITION':'LF','ATBATS':495,'RUNS':71,'HITS':137,'DOUBLES':24,'TRIPLES':5,'HOMERUNS':12,'RBI':55,'WALKS':42,'STRIKEOUTS':66,},
{'NAME':'Joe Mauer','AGE':33,'TEAM':'MIN','POSITION':'1B','ATBATS':494,'RUNS':68,'HITS':129,'DOUBLES':22,'TRIPLES':4,'HOMERUNS':11,'RBI':49,'WALKS':79,'STRIKEOUTS':93,},
{'NAME':'Troy Tulowitzki','AGE':31,'TEAM':'TOR','POSITION':'SS','ATBATS':492,'RUNS':54,'HITS':125,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':24,'RBI':79,'WALKS':43,'STRIKEOUTS':101,},
{'NAME':'Melvin Upton','AGE':31,'TEAM':'TOT','POSITION':'LF','ATBATS':492,'RUNS':64,'HITS':117,'DOUBLES':15,'TRIPLES':3,'HOMERUNS':20,'RBI':61,'WALKS':37,'STRIKEOUTS':155,},
{'NAME':'Jonathan Lucroy','AGE':30,'TEAM':'TOT','POSITION':'C','ATBATS':490,'RUNS':67,'HITS':143,'DOUBLES':24,'TRIPLES':3,'HOMERUNS':24,'RBI':81,'WALKS':47,'STRIKEOUTS':100,},
{'NAME':'Michael Saunders','AGE':29,'TEAM':'TOR','POSITION':'LF','ATBATS':490,'RUNS':70,'HITS':124,'DOUBLES':32,'TRIPLES':3,'HOMERUNS':24,'RBI':57,'WALKS':59,'STRIKEOUTS':157,},
{'NAME':'Stephen Vogt','AGE':31,'TEAM':'OAK','POSITION':'C','ATBATS':490,'RUNS':54,'HITS':123,'DOUBLES':30,'TRIPLES':2,'HOMERUNS':14,'RBI':56,'WALKS':35,'STRIKEOUTS':83,},
{'NAME':'Starling Marte','AGE':27,'TEAM':'PIT','POSITION':'LF','ATBATS':489,'RUNS':71,'HITS':152,'DOUBLES':34,'TRIPLES':5,'HOMERUNS':9,'RBI':46,'WALKS':23,'STRIKEOUTS':104,},
{'NAME':'Josh Harrison','AGE':28,'TEAM':'PIT','POSITION':'2B','ATBATS':487,'RUNS':57,'HITS':138,'DOUBLES':25,'TRIPLES':7,'HOMERUNS':4,'RBI':59,'WALKS':18,'STRIKEOUTS':76,},
{'NAME':'Howie Kendrick','AGE':32,'TEAM':'LAD','POSITION':'LF','ATBATS':487,'RUNS':65,'HITS':124,'DOUBLES':26,'TRIPLES':2,'HOMERUNS':8,'RBI':40,'WALKS':50,'STRIKEOUTS':96,},
{'NAME':'Marwin Gonzalez','AGE':27,'TEAM':'HOU','POSITION':'1B','ATBATS':484,'RUNS':55,'HITS':123,'DOUBLES':26,'TRIPLES':3,'HOMERUNS':13,'RBI':51,'WALKS':22,'STRIKEOUTS':118,},
{'NAME':'Yonder Alonso','AGE':29,'TEAM':'OAK','POSITION':'1B','ATBATS':482,'RUNS':52,'HITS':122,'DOUBLES':34,'TRIPLES':0,'HOMERUNS':7,'RBI':56,'WALKS':45,'STRIKEOUTS':74,},
{'NAME':'Wilson Ramos','AGE':28,'TEAM':'WSN','POSITION':'C','ATBATS':482,'RUNS':58,'HITS':148,'DOUBLES':25,'TRIPLES':0,'HOMERUNS':22,'RBI':80,'WALKS':35,'STRIKEOUTS':79,},
{'NAME':'Travis Shaw','AGE':26,'TEAM':'BOS','POSITION':'3B','ATBATS':480,'RUNS':63,'HITS':116,'DOUBLES':34,'TRIPLES':2,'HOMERUNS':16,'RBI':71,'WALKS':43,'STRIKEOUTS':133,},
{'NAME':'Yoenis Cespedes','AGE':30,'TEAM':'NYM','POSITION':'LF','ATBATS':479,'RUNS':72,'HITS':134,'DOUBLES':25,'TRIPLES':1,'HOMERUNS':31,'RBI':86,'WALKS':51,'STRIKEOUTS':108,},
{'NAME':'Alexei Ramirez','AGE':34,'TEAM':'TOT','POSITION':'SS','ATBATS':478,'RUNS':38,'HITS':115,'DOUBLES':22,'TRIPLES':2,'HOMERUNS':6,'RBI':48,'WALKS':21,'STRIKEOUTS':63,},
{'NAME':'Cheslor Cuthbert','AGE':23,'TEAM':'KCR','POSITION':'3B','ATBATS':475,'RUNS':49,'HITS':130,'DOUBLES':28,'TRIPLES':1,'HOMERUNS':12,'RBI':46,'WALKS':32,'STRIKEOUTS':96,},
{'NAME':'Matt Carpenter','AGE':30,'TEAM':'STL','POSITION':'3B','ATBATS':473,'RUNS':81,'HITS':128,'DOUBLES':36,'TRIPLES':6,'HOMERUNS':21,'RBI':68,'WALKS':81,'STRIKEOUTS':108,},
{'NAME':'Danny Valencia','AGE':31,'TEAM':'OAK','POSITION':'3B','ATBATS':471,'RUNS':72,'HITS':135,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':17,'RBI':51,'WALKS':41,'STRIKEOUTS':115,},
{'NAME':'Chase Headley','AGE':32,'TEAM':'NYY','POSITION':'3B','ATBATS':467,'RUNS':58,'HITS':118,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':14,'RBI':51,'WALKS':51,'STRIKEOUTS':118,},
{'NAME':'Jose Iglesias','AGE':26,'TEAM':'DET','POSITION':'SS','ATBATS':467,'RUNS':57,'HITS':119,'DOUBLES':26,'TRIPLES':0,'HOMERUNS':4,'RBI':32,'WALKS':28,'STRIKEOUTS':50,},
{'NAME':'Zack Cozart','AGE':30,'TEAM':'CIN','POSITION':'SS','ATBATS':464,'RUNS':67,'HITS':117,'DOUBLES':28,'TRIPLES':2,'HOMERUNS':16,'RBI':50,'WALKS':37,'STRIKEOUTS':84,},
{'NAME':'Joe Panik','AGE':25,'TEAM':'SFG','POSITION':'2B','ATBATS':464,'RUNS':67,'HITS':111,'DOUBLES':21,'TRIPLES':7,'HOMERUNS':10,'RBI':62,'WALKS':50,'STRIKEOUTS':47,},
{'NAME':'Brandon Drury','AGE':23,'TEAM':'ARI','POSITION':'LF','ATBATS':461,'RUNS':59,'HITS':130,'DOUBLES':31,'TRIPLES':1,'HOMERUNS':16,'RBI':53,'WALKS':31,'STRIKEOUTS':100,},
{'NAME':'J.D. Martinez','AGE':28,'TEAM':'DET','POSITION':'RF','ATBATS':460,'RUNS':69,'HITS':141,'DOUBLES':35,'TRIPLES':2,'HOMERUNS':22,'RBI':68,'WALKS':49,'STRIKEOUTS':128,},
{'NAME':'Mitch Moreland','AGE':30,'TEAM':'TEX','POSITION':'1B','ATBATS':460,'RUNS':49,'HITS':107,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':22,'RBI':60,'WALKS':35,'STRIKEOUTS':118,},
{'NAME':'Paulo Orlando','AGE':30,'TEAM':'KCR','POSITION':'RF','ATBATS':457,'RUNS':52,'HITS':138,'DOUBLES':24,'TRIPLES':4,'HOMERUNS':5,'RBI':43,'WALKS':13,'STRIKEOUTS':105,},
{'NAME':'Dexter Fowler','AGE':30,'TEAM':'CHC','POSITION':'CF','ATBATS':456,'RUNS':84,'HITS':126,'DOUBLES':25,'TRIPLES':7,'HOMERUNS':13,'RBI':48,'WALKS':79,'STRIKEOUTS':124,},
{'NAME':'Russell Martin','AGE':33,'TEAM':'TOR','POSITION':'C','ATBATS':455,'RUNS':62,'HITS':105,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':20,'RBI':74,'WALKS':64,'STRIKEOUTS':148,},
{'NAME':'Rajai Davis','AGE':35,'TEAM':'CLE','POSITION':'CF','ATBATS':454,'RUNS':74,'HITS':113,'DOUBLES':23,'TRIPLES':2,'HOMERUNS':12,'RBI':48,'WALKS':33,'STRIKEOUTS':106,},
{'NAME':'Andrelton Simmons','AGE':26,'TEAM':'LAA','POSITION':'SS','ATBATS':448,'RUNS':48,'HITS':126,'DOUBLES':22,'TRIPLES':2,'HOMERUNS':4,'RBI':44,'WALKS':28,'STRIKEOUTS':38,},
{'NAME':'Evan Gattis','AGE':29,'TEAM':'HOU','POSITION':'DH','ATBATS':447,'RUNS':58,'HITS':112,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':32,'RBI':72,'WALKS':43,'STRIKEOUTS':127,},
{'NAME':'Coco Crisp','AGE':36,'TEAM':'TOT','POSITION':'LF','ATBATS':446,'RUNS':54,'HITS':103,'DOUBLES':27,'TRIPLES':4,'HOMERUNS':13,'RBI':55,'WALKS':46,'STRIKEOUTS':78,},
{'NAME':'Randal Grichuk','AGE':24,'TEAM':'STL','POSITION':'CF','ATBATS':446,'RUNS':66,'HITS':107,'DOUBLES':29,'TRIPLES':3,'HOMERUNS':24,'RBI':68,'WALKS':28,'STRIKEOUTS':141,},
{'NAME':'Alex Gordon','AGE':32,'TEAM':'KCR','POSITION':'LF','ATBATS':445,'RUNS':62,'HITS':98,'DOUBLES':16,'TRIPLES':2,'HOMERUNS':17,'RBI':40,'WALKS':52,'STRIKEOUTS':148,},
{'NAME':'David Freese','AGE':33,'TEAM':'PIT','POSITION':'3B','ATBATS':437,'RUNS':63,'HITS':118,'DOUBLES':23,'TRIPLES':0,'HOMERUNS':13,'RBI':55,'WALKS':45,'STRIKEOUTS':142,},
{'NAME':'Ketel Marte','AGE':22,'TEAM':'SEA','POSITION':'SS','ATBATS':437,'RUNS':55,'HITS':113,'DOUBLES':21,'TRIPLES':2,'HOMERUNS':1,'RBI':33,'WALKS':18,'STRIKEOUTS':84,},
{'NAME':'Chris Owings','AGE':24,'TEAM':'ARI','POSITION':'SS','ATBATS':437,'RUNS':52,'HITS':121,'DOUBLES':24,'TRIPLES':11,'HOMERUNS':5,'RBI':49,'WALKS':20,'STRIKEOUTS':87,},
{'NAME':'Miguel Sano','AGE':23,'TEAM':'MIN','POSITION':'3B','ATBATS':437,'RUNS':57,'HITS':103,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':25,'RBI':66,'WALKS':54,'STRIKEOUTS':178,},
{'NAME':'Steven Souza','AGE':27,'TEAM':'TBR','POSITION':'RF','ATBATS':430,'RUNS':58,'HITS':106,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':17,'RBI':49,'WALKS':31,'STRIKEOUTS':159,},
{'NAME':'Brian McCann','AGE':32,'TEAM':'NYY','POSITION':'C','ATBATS':429,'RUNS':56,'HITS':104,'DOUBLES':13,'TRIPLES':0,'HOMERUNS':20,'RBI':58,'WALKS':54,'STRIKEOUTS':99,},
{'NAME':'Ryan Zimmerman','AGE':31,'TEAM':'WSN','POSITION':'1B','ATBATS':427,'RUNS':60,'HITS':93,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':15,'RBI':46,'WALKS':29,'STRIKEOUTS':104,},
{'NAME':'Jose Bautista','AGE':35,'TEAM':'TOR','POSITION':'RF','ATBATS':423,'RUNS':68,'HITS':99,'DOUBLES':24,'TRIPLES':1,'HOMERUNS':22,'RBI':69,'WALKS':87,'STRIKEOUTS':103,},
{'NAME':'Matt Wieters','AGE':30,'TEAM':'BAL','POSITION':'C','ATBATS':423,'RUNS':48,'HITS':103,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':17,'RBI':66,'WALKS':32,'STRIKEOUTS':85,},
{'NAME':'Javier Baez','AGE':23,'TEAM':'CHC','POSITION':'3B','ATBATS':421,'RUNS':50,'HITS':115,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':14,'RBI':59,'WALKS':15,'STRIKEOUTS':108,},
{'NAME':'Norichika Aoki','AGE':34,'TEAM':'SEA','POSITION':'LF','ATBATS':417,'RUNS':63,'HITS':118,'DOUBLES':24,'TRIPLES':4,'HOMERUNS':4,'RBI':28,'WALKS':34,'STRIKEOUTS':45,},
{'NAME':'Welington Castillo','AGE':29,'TEAM':'ARI','POSITION':'C','ATBATS':416,'RUNS':41,'HITS':110,'DOUBLES':24,'TRIPLES':0,'HOMERUNS':14,'RBI':68,'WALKS':33,'STRIKEOUTS':121,},
{'NAME':'Erick Aybar','AGE':32,'TEAM':'TOT','POSITION':'SS','ATBATS':415,'RUNS':34,'HITS':101,'DOUBLES':19,'TRIPLES':2,'HOMERUNS':3,'RBI':34,'WALKS':31,'STRIKEOUTS':70,},
{'NAME':'Derek Norris','AGE':27,'TEAM':'SDP','POSITION':'C','ATBATS':415,'RUNS':50,'HITS':77,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':14,'RBI':42,'WALKS':36,'STRIKEOUTS':139,},
{'NAME':'Avisail Garcia','AGE':25,'TEAM':'CHW','POSITION':'DH','ATBATS':413,'RUNS':59,'HITS':101,'DOUBLES':18,'TRIPLES':2,'HOMERUNS':12,'RBI':51,'WALKS':34,'STRIKEOUTS':115,},
{'NAME':'Brandon Moss','AGE':32,'TEAM':'STL','POSITION':'1B','ATBATS':413,'RUNS':66,'HITS':93,'DOUBLES':19,'TRIPLES':2,'HOMERUNS':28,'RBI':67,'WALKS':39,'STRIKEOUTS':141,},
{'NAME':'Giancarlo Stanton','AGE':26,'TEAM':'MIA','POSITION':'RF','ATBATS':413,'RUNS':56,'HITS':99,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':27,'RBI':74,'WALKS':50,'STRIKEOUTS':140,},
{'NAME':'Neil Walker','AGE':30,'TEAM':'NYM','POSITION':'2B','ATBATS':412,'RUNS':57,'HITS':116,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':23,'RBI':55,'WALKS':42,'STRIKEOUTS':84,},
{'NAME':'Nicholas Castellanos','AGE':24,'TEAM':'DET','POSITION':'3B','ATBATS':411,'RUNS':54,'HITS':117,'DOUBLES':25,'TRIPLES':4,'HOMERUNS':18,'RBI':58,'WALKS':28,'STRIKEOUTS':111,},
{'NAME':'Carlos Gomez','AGE':30,'TEAM':'TOT','POSITION':'CF','ATBATS':411,'RUNS':45,'HITS':95,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':13,'RBI':53,'WALKS':34,'STRIKEOUTS':136,},
{'NAME':'Billy Hamilton','AGE':25,'TEAM':'CIN','POSITION':'CF','ATBATS':411,'RUNS':69,'HITS':107,'DOUBLES':19,'TRIPLES':3,'HOMERUNS':3,'RBI':17,'WALKS':36,'STRIKEOUTS':93,},
{'NAME':'Tim Anderson','AGE':23,'TEAM':'CHW','POSITION':'SS','ATBATS':410,'RUNS':57,'HITS':116,'DOUBLES':22,'TRIPLES':6,'HOMERUNS':9,'RBI':30,'WALKS':13,'STRIKEOUTS':117,},
{'NAME':'Devon Travis','AGE':25,'TEAM':'TOR','POSITION':'2B','ATBATS':410,'RUNS':54,'HITS':123,'DOUBLES':28,'TRIPLES':1,'HOMERUNS':11,'RBI':50,'WALKS':20,'STRIKEOUTS':87,},
{'NAME':'C.J. Cron','AGE':26,'TEAM':'LAA','POSITION':'1B','ATBATS':407,'RUNS':51,'HITS':113,'DOUBLES':25,'TRIPLES':2,'HOMERUNS':16,'RBI':69,'WALKS':24,'STRIKEOUTS':75,},
{'NAME':'Joc Pederson','AGE':24,'TEAM':'LAD','POSITION':'CF','ATBATS':406,'RUNS':64,'HITS':100,'DOUBLES':26,'TRIPLES':0,'HOMERUNS':25,'RBI':68,'WALKS':63,'STRIKEOUTS':130,},
{'NAME':'J.J. Hardy','AGE':33,'TEAM':'BAL','POSITION':'SS','ATBATS':405,'RUNS':43,'HITS':109,'DOUBLES':29,'TRIPLES':0,'HOMERUNS':9,'RBI':48,'WALKS':26,'STRIKEOUTS':68,},
{'NAME':'Yangervis Solarte','AGE':28,'TEAM':'SDP','POSITION':'3B','ATBATS':405,'RUNS':55,'HITS':116,'DOUBLES':26,'TRIPLES':1,'HOMERUNS':15,'RBI':71,'WALKS':30,'STRIKEOUTS':63,},
{'NAME':'Aledmys Diaz','AGE':25,'TEAM':'STL','POSITION':'SS','ATBATS':404,'RUNS':71,'HITS':121,'DOUBLES':28,'TRIPLES':3,'HOMERUNS':17,'RBI':65,'WALKS':41,'STRIKEOUTS':60,},
{'NAME':'Hernan Perez','AGE':25,'TEAM':'MIL','POSITION':'3B','ATBATS':404,'RUNS':50,'HITS':110,'DOUBLES':18,'TRIPLES':3,'HOMERUNS':13,'RBI':56,'WALKS':18,'STRIKEOUTS':94,},
{'NAME':'Adam Lind','AGE':32,'TEAM':'SEA','POSITION':'1B','ATBATS':401,'RUNS':48,'HITS':96,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':20,'RBI':58,'WALKS':26,'STRIKEOUTS':89,},
{'NAME':'Jedd Gyorko','AGE':27,'TEAM':'STL','POSITION':'2B','ATBATS':400,'RUNS':58,'HITS':97,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':30,'RBI':59,'WALKS':37,'STRIKEOUTS':96,},
{'NAME':'Josh Reddick','AGE':29,'TEAM':'TOT','POSITION':'RF','ATBATS':398,'RUNS':53,'HITS':112,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':10,'RBI':37,'WALKS':39,'STRIKEOUTS':56,},
{'NAME':'Lorenzo Cain','AGE':30,'TEAM':'KCR','POSITION':'CF','ATBATS':397,'RUNS':56,'HITS':114,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':9,'RBI':56,'WALKS':31,'STRIKEOUTS':84,},
{'NAME':'Max Kepler','AGE':23,'TEAM':'MIN','POSITION':'RF','ATBATS':396,'RUNS':52,'HITS':93,'DOUBLES':20,'TRIPLES':2,'HOMERUNS':17,'RBI':63,'WALKS':42,'STRIKEOUTS':93,},
{'NAME':'Hunter Pence','AGE':33,'TEAM':'SFG','POSITION':'RF','ATBATS':395,'RUNS':58,'HITS':114,'DOUBLES':23,'TRIPLES':1,'HOMERUNS':13,'RBI':57,'WALKS':43,'STRIKEOUTS':95,},
{'NAME':'Mark Reynolds','AGE':32,'TEAM':'COL','POSITION':'1B','ATBATS':393,'RUNS':61,'HITS':111,'DOUBLES':24,'TRIPLES':0,'HOMERUNS':14,'RBI':53,'WALKS':42,'STRIKEOUTS':112,},
{'NAME':'Yasmani Grandal','AGE':27,'TEAM':'LAD','POSITION':'C','ATBATS':390,'RUNS':49,'HITS':89,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':27,'RBI':72,'WALKS':64,'STRIKEOUTS':116,},
{'NAME':'Cameron Rupp','AGE':27,'TEAM':'PHI','POSITION':'C','ATBATS':389,'RUNS':36,'HITS':98,'DOUBLES':26,'TRIPLES':1,'HOMERUNS':16,'RBI':54,'WALKS':24,'STRIKEOUTS':114,},
{'NAME':'Mark Teixeira','AGE':36,'TEAM':'NYY','POSITION':'1B','ATBATS':387,'RUNS':43,'HITS':79,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':15,'RBI':44,'WALKS':47,'STRIKEOUTS':105,},
{'NAME':'Lonnie Chisenhall','AGE':27,'TEAM':'CLE','POSITION':'RF','ATBATS':385,'RUNS':43,'HITS':110,'DOUBLES':25,'TRIPLES':5,'HOMERUNS':8,'RBI':57,'WALKS':23,'STRIKEOUTS':70,},
{'NAME':'Matt Holliday','AGE':36,'TEAM':'STL','POSITION':'LF','ATBATS':382,'RUNS':48,'HITS':94,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':20,'RBI':62,'WALKS':35,'STRIKEOUTS':71,},
{'NAME':'John Jaso','AGE':32,'TEAM':'PIT','POSITION':'1B','ATBATS':380,'RUNS':45,'HITS':102,'DOUBLES':25,'TRIPLES':3,'HOMERUNS':8,'RBI':42,'WALKS':45,'STRIKEOUTS':74,},
{'NAME':'Aaron Hill','AGE':34,'TEAM':'TOT','POSITION':'3B','ATBATS':378,'RUNS':48,'HITS':99,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':10,'RBI':38,'WALKS':41,'STRIKEOUTS':59,},
{'NAME':'Seth Smith','AGE':33,'TEAM':'SEA','POSITION':'RF','ATBATS':378,'RUNS':62,'HITS':94,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':16,'RBI':63,'WALKS':48,'STRIKEOUTS':89,},
{'NAME':'Tucker Barnhart','AGE':25,'TEAM':'CIN','POSITION':'C','ATBATS':377,'RUNS':34,'HITS':97,'DOUBLES':23,'TRIPLES':1,'HOMERUNS':7,'RBI':51,'WALKS':36,'STRIKEOUTS':72,},
{'NAME':'Michael Bourn','AGE':33,'TEAM':'TOT','POSITION':'CF','ATBATS':375,'RUNS':48,'HITS':99,'DOUBLES':13,'TRIPLES':6,'HOMERUNS':5,'RBI':38,'WALKS':28,'STRIKEOUTS':92,},
{'NAME':'Trevor Story','AGE':23,'TEAM':'COL','POSITION':'SS','ATBATS':372,'RUNS':67,'HITS':101,'DOUBLES':21,'TRIPLES':4,'HOMERUNS':27,'RBI':72,'WALKS':35,'STRIKEOUTS':130,},
{'NAME':'Colby Rasmus','AGE':29,'TEAM':'HOU','POSITION':'LF','ATBATS':369,'RUNS':38,'HITS':76,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':15,'RBI':54,'WALKS':43,'STRIKEOUTS':121,},
{'NAME':'Gerardo Parra','AGE':29,'TEAM':'COL','POSITION':'LF','ATBATS':368,'RUNS':45,'HITS':93,'DOUBLES':27,'TRIPLES':3,'HOMERUNS':7,'RBI':39,'WALKS':9,'STRIKEOUTS':73,},
{'NAME':'Kevin Kiermaier','AGE':26,'TEAM':'TBR','POSITION':'CF','ATBATS':366,'RUNS':55,'HITS':90,'DOUBLES':20,'TRIPLES':2,'HOMERUNS':12,'RBI':37,'WALKS':40,'STRIKEOUTS':74,},
{'NAME':'Peter Bourjos','AGE':29,'TEAM':'PHI','POSITION':'RF','ATBATS':355,'RUNS':40,'HITS':89,'DOUBLES':20,'TRIPLES':7,'HOMERUNS':5,'RBI':23,'WALKS':17,'STRIKEOUTS':91,},
{'NAME':'Logan Morrison','AGE':28,'TEAM':'TBR','POSITION':'1B','ATBATS':353,'RUNS':45,'HITS':84,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':14,'RBI':43,'WALKS':37,'STRIKEOUTS':89,},
{'NAME':'Eduardo Escobar','AGE':27,'TEAM':'MIN','POSITION':'SS','ATBATS':352,'RUNS':32,'HITS':83,'DOUBLES':14,'TRIPLES':2,'HOMERUNS':6,'RBI':37,'WALKS':21,'STRIKEOUTS':72,},
{'NAME':'Derek Dietrich','AGE':26,'TEAM':'MIA','POSITION':'2B','ATBATS':351,'RUNS':39,'HITS':98,'DOUBLES':20,'TRIPLES':5,'HOMERUNS':7,'RBI':42,'WALKS':32,'STRIKEOUTS':84,},
{'NAME':'Brett Lawrie','AGE':26,'TEAM':'CHW','POSITION':'2B','ATBATS':351,'RUNS':35,'HITS':87,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':12,'RBI':36,'WALKS':30,'STRIKEOUTS':109,},
{'NAME':'Jace Peterson','AGE':26,'TEAM':'ATL','POSITION':'2B','ATBATS':350,'RUNS':45,'HITS':89,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':7,'RBI':29,'WALKS':52,'STRIKEOUTS':69,},
{'NAME':'Ben Revere','AGE':28,'TEAM':'WSN','POSITION':'CF','ATBATS':350,'RUNS':44,'HITS':76,'DOUBLES':9,'TRIPLES':7,'HOMERUNS':2,'RBI':24,'WALKS':18,'STRIKEOUTS':34,},
{'NAME':'Cameron Maybin','AGE':29,'TEAM':'DET','POSITION':'CF','ATBATS':349,'RUNS':65,'HITS':110,'DOUBLES':14,'TRIPLES':5,'HOMERUNS':4,'RBI':43,'WALKS':36,'STRIKEOUTS':69,},
{'NAME':'Jon Jay','AGE':31,'TEAM':'SDP','POSITION':'CF','ATBATS':347,'RUNS':49,'HITS':101,'DOUBLES':26,'TRIPLES':1,'HOMERUNS':2,'RBI':26,'WALKS':19,'STRIKEOUTS':78,},
{'NAME':'Johnny Giavotella','AGE':28,'TEAM':'LAA','POSITION':'2B','ATBATS':346,'RUNS':44,'HITS':90,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':6,'RBI':31,'WALKS':13,'STRIKEOUTS':39,},
{'NAME':'Kurt Suzuki','AGE':32,'TEAM':'MIN','POSITION':'C','ATBATS':345,'RUNS':34,'HITS':89,'DOUBLES':24,'TRIPLES':1,'HOMERUNS':8,'RBI':49,'WALKS':18,'STRIKEOUTS':48,},
{'NAME':'James McCann','AGE':26,'TEAM':'DET','POSITION':'C','ATBATS':344,'RUNS':31,'HITS':76,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':12,'RBI':48,'WALKS':23,'STRIKEOUTS':109,},
{'NAME':'James Loney','AGE':32,'TEAM':'NYM','POSITION':'1B','ATBATS':343,'RUNS':30,'HITS':91,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':9,'RBI':34,'WALKS':16,'STRIKEOUTS':37,},
{'NAME':'Jed Lowrie','AGE':32,'TEAM':'OAK','POSITION':'2B','ATBATS':338,'RUNS':30,'HITS':89,'DOUBLES':12,'TRIPLES':1,'HOMERUNS':2,'RBI':27,'WALKS':26,'STRIKEOUTS':65,},
{'NAME':'Pedro Alvarez','AGE':29,'TEAM':'BAL','POSITION':'DH','ATBATS':337,'RUNS':43,'HITS':84,'DOUBLES':20,'TRIPLES':0,'HOMERUNS':22,'RBI':49,'WALKS':37,'STRIKEOUTS':97,},
{'NAME':'Travis Jankowski','AGE':25,'TEAM':'SDP','POSITION':'CF','ATBATS':335,'RUNS':53,'HITS':82,'DOUBLES':13,'TRIPLES':2,'HOMERUNS':2,'RBI':12,'WALKS':42,'STRIKEOUTS':100,},
{'NAME':'Kirk Nieuwenhuis','AGE':28,'TEAM':'MIL','POSITION':'CF','ATBATS':335,'RUNS':38,'HITS':70,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':13,'RBI':44,'WALKS':56,'STRIKEOUTS':133,},
{'NAME':'Eddie Rosario','AGE':24,'TEAM':'MIN','POSITION':'LF','ATBATS':335,'RUNS':52,'HITS':90,'DOUBLES':17,'TRIPLES':2,'HOMERUNS':10,'RBI':32,'WALKS':12,'STRIKEOUTS':91,},
{'NAME':'Yasiel Puig','AGE':25,'TEAM':'LAD','POSITION':'RF','ATBATS':334,'RUNS':45,'HITS':88,'DOUBLES':14,'TRIPLES':2,'HOMERUNS':11,'RBI':45,'WALKS':24,'STRIKEOUTS':74,},
{'NAME':'Matt Duffy','AGE':25,'TEAM':'TOT','POSITION':'3B','ATBATS':333,'RUNS':41,'HITS':86,'DOUBLES':14,'TRIPLES':2,'HOMERUNS':5,'RBI':28,'WALKS':23,'STRIKEOUTS':53,},
{'NAME':'Robbie Grossman','AGE':26,'TEAM':'MIN','POSITION':'LF','ATBATS':332,'RUNS':49,'HITS':93,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':11,'RBI':37,'WALKS':55,'STRIKEOUTS':96,},
{'NAME':'Ryan Howard','AGE':36,'TEAM':'PHI','POSITION':'1B','ATBATS':331,'RUNS':35,'HITS':65,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':25,'RBI':59,'WALKS':27,'STRIKEOUTS':114,},
{'NAME':'Jason Castro','AGE':29,'TEAM':'HOU','POSITION':'C','ATBATS':329,'RUNS':41,'HITS':69,'DOUBLES':16,'TRIPLES':3,'HOMERUNS':11,'RBI':32,'WALKS':45,'STRIKEOUTS':123,},
{'NAME':'Aaron Hicks','AGE':26,'TEAM':'NYY','POSITION':'RF','ATBATS':327,'RUNS':32,'HITS':71,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':8,'RBI':31,'WALKS':30,'STRIKEOUTS':68,},
{'NAME':'Ichiro Suzuki','AGE':42,'TEAM':'MIA','POSITION':'RF','ATBATS':327,'RUNS':48,'HITS':95,'DOUBLES':15,'TRIPLES':5,'HOMERUNS':1,'RBI':22,'WALKS':30,'STRIKEOUTS':42,},
{'NAME':'Francisco Cervelli','AGE':30,'TEAM':'PIT','POSITION':'C','ATBATS':326,'RUNS':42,'HITS':86,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':1,'RBI':33,'WALKS':56,'STRIKEOUTS':72,},
{'NAME':'Prince Fielder','AGE':32,'TEAM':'TEX','POSITION':'DH','ATBATS':326,'RUNS':29,'HITS':69,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':8,'RBI':44,'WALKS':32,'STRIKEOUTS':63,},
{'NAME':'Dee Gordon','AGE':28,'TEAM':'MIA','POSITION':'2B','ATBATS':325,'RUNS':47,'HITS':87,'DOUBLES':7,'TRIPLES':6,'HOMERUNS':1,'RBI':14,'WALKS':18,'STRIKEOUTS':55,},
{'NAME':'Tyler Naquin','AGE':25,'TEAM':'CLE','POSITION':'CF','ATBATS':321,'RUNS':52,'HITS':95,'DOUBLES':18,'TRIPLES':5,'HOMERUNS':14,'RBI':43,'WALKS':36,'STRIKEOUTS':112,},
{'NAME':'Trevor Plouffe','AGE':30,'TEAM':'MIN','POSITION':'3B','ATBATS':319,'RUNS':35,'HITS':83,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':12,'RBI':47,'WALKS':19,'STRIKEOUTS':60,},
{'NAME':'Jung Ho Kang','AGE':29,'TEAM':'PIT','POSITION':'3B','ATBATS':318,'RUNS':45,'HITS':81,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':21,'RBI':62,'WALKS':36,'STRIKEOUTS':79,},
{'NAME':'Tommy Joseph','AGE':24,'TEAM':'PHI','POSITION':'1B','ATBATS':315,'RUNS':47,'HITS':81,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':21,'RBI':47,'WALKS':22,'STRIKEOUTS':75,},
{'NAME':'Kolten Wong','AGE':25,'TEAM':'STL','POSITION':'2B','ATBATS':313,'RUNS':39,'HITS':75,'DOUBLES':7,'TRIPLES':7,'HOMERUNS':5,'RBI':23,'WALKS':34,'STRIKEOUTS':52,},
{'NAME':'Billy Burns','AGE':26,'TEAM':'TOT','POSITION':'CF','ATBATS':311,'RUNS':39,'HITS':73,'DOUBLES':11,'TRIPLES':4,'HOMERUNS':0,'RBI':13,'WALKS':10,'STRIKEOUTS':37,},
{'NAME':'Whit Merrifield','AGE':27,'TEAM':'KCR','POSITION':'2B','ATBATS':311,'RUNS':44,'HITS':88,'DOUBLES':22,'TRIPLES':3,'HOMERUNS':2,'RBI':29,'WALKS':19,'STRIKEOUTS':72,},
{'NAME':'Wilmer Flores','AGE':24,'TEAM':'NYM','POSITION':'3B','ATBATS':307,'RUNS':38,'HITS':82,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':16,'RBI':49,'WALKS':23,'STRIKEOUTS':48,},
{'NAME':'Jeff Francoeur','AGE':32,'TEAM':'TOT','POSITION':'LF','ATBATS':307,'RUNS':33,'HITS':78,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':7,'RBI':34,'WALKS':20,'STRIKEOUTS':90,},
{'NAME':'Trea Turner','AGE':23,'TEAM':'WSN','POSITION':'CF','ATBATS':307,'RUNS':53,'HITS':105,'DOUBLES':14,'TRIPLES':8,'HOMERUNS':13,'RBI':40,'WALKS':14,'STRIKEOUTS':59,},
{'NAME':'Hyun Soo Kim','AGE':28,'TEAM':'BAL','POSITION':'LF','ATBATS':305,'RUNS':36,'HITS':92,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':6,'RBI':22,'WALKS':36,'STRIKEOUTS':51,},
{'NAME':'Michael Conforto','AGE':23,'TEAM':'NYM','POSITION':'LF','ATBATS':304,'RUNS':38,'HITS':67,'DOUBLES':21,'TRIPLES':1,'HOMERUNS':12,'RBI':42,'WALKS':36,'STRIKEOUTS':89,},
{'NAME':'Kelly Johnson','AGE':34,'TEAM':'TOT','POSITION':'2B','ATBATS':304,'RUNS':25,'HITS':75,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':10,'RBI':34,'WALKS':25,'STRIKEOUTS':65,},
{'NAME':'Dioner Navarro','AGE':32,'TEAM':'TOT','POSITION':'C','ATBATS':304,'RUNS':26,'HITS':63,'DOUBLES':13,'TRIPLES':2,'HOMERUNS':6,'RBI':35,'WALKS':23,'STRIKEOUTS':71,},
{'NAME':'Sean Rodriguez','AGE':31,'TEAM':'PIT','POSITION':'1B','ATBATS':300,'RUNS':49,'HITS':81,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':18,'RBI':56,'WALKS':33,'STRIKEOUTS':102,},
{'NAME':'Jarrod Dyson','AGE':31,'TEAM':'KCR','POSITION':'CF','ATBATS':299,'RUNS':46,'HITS':83,'DOUBLES':14,'TRIPLES':8,'HOMERUNS':1,'RBI':25,'WALKS':26,'STRIKEOUTS':39,},
{'NAME':'Justin Smoak','AGE':29,'TEAM':'TOR','POSITION':'1B','ATBATS':299,'RUNS':33,'HITS':65,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':14,'RBI':34,'WALKS':40,'STRIKEOUTS':112,},
{'NAME':'Byron Buxton','AGE':22,'TEAM':'MIN','POSITION':'CF','ATBATS':298,'RUNS':44,'HITS':67,'DOUBLES':19,'TRIPLES':6,'HOMERUNS':10,'RBI':38,'WALKS':23,'STRIKEOUTS':118,},
{'NAME':'Tyler Saladino','AGE':26,'TEAM':'CHW','POSITION':'2B','ATBATS':298,'RUNS':33,'HITS':84,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':8,'RBI':38,'WALKS':13,'STRIKEOUTS':62,},
{'NAME':'Matt Adams','AGE':27,'TEAM':'STL','POSITION':'1B','ATBATS':297,'RUNS':37,'HITS':74,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':16,'RBI':54,'WALKS':25,'STRIKEOUTS':81,},
{'NAME':'Chris Iannetta','AGE':33,'TEAM':'SEA','POSITION':'C','ATBATS':295,'RUNS':23,'HITS':62,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':7,'RBI':24,'WALKS':38,'STRIKEOUTS':83,},
{'NAME':'Brandon Guyer','AGE':30,'TEAM':'TOT','POSITION':'LF','ATBATS':293,'RUNS':39,'HITS':78,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':9,'RBI':32,'WALKS':19,'STRIKEOUTS':55,},
{'NAME':'Dae-ho Lee','AGE':34,'TEAM':'SEA','POSITION':'1B','ATBATS':292,'RUNS':33,'HITS':74,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':14,'RBI':49,'WALKS':20,'STRIKEOUTS':74,},
{'NAME':'Luis Valbuena','AGE':30,'TEAM':'HOU','POSITION':'3B','ATBATS':292,'RUNS':38,'HITS':76,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':13,'RBI':40,'WALKS':44,'STRIKEOUTS':81,},
{'NAME':'Brock Holt','AGE':28,'TEAM':'BOS','POSITION':'LF','ATBATS':290,'RUNS':45,'HITS':74,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':7,'RBI':34,'WALKS':27,'STRIKEOUTS':58,},
{'NAME':'Jake Smolinski','AGE':27,'TEAM':'OAK','POSITION':'CF','ATBATS':290,'RUNS':28,'HITS':69,'DOUBLES':6,'TRIPLES':2,'HOMERUNS':7,'RBI':27,'WALKS':19,'STRIKEOUTS':44,},
{'NAME':'Nick Hundley','AGE':32,'TEAM':'COL','POSITION':'C','ATBATS':289,'RUNS':30,'HITS':75,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':10,'RBI':48,'WALKS':25,'STRIKEOUTS':65,},
{'NAME':'Jhonny Peralta','AGE':34,'TEAM':'STL','POSITION':'3B','ATBATS':289,'RUNS':37,'HITS':75,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':8,'RBI':29,'WALKS':20,'STRIKEOUTS':56,},
{'NAME':'Jake Marisnick','AGE':25,'TEAM':'HOU','POSITION':'CF','ATBATS':287,'RUNS':40,'HITS':60,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':5,'RBI':21,'WALKS':16,'STRIKEOUTS':83,},
{'NAME':'Nick Ahmed','AGE':26,'TEAM':'ARI','POSITION':'SS','ATBATS':284,'RUNS':26,'HITS':62,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':4,'RBI':20,'WALKS':15,'STRIKEOUTS':58,},
{'NAME':'Tyler Flowers','AGE':30,'TEAM':'ATL','POSITION':'C','ATBATS':281,'RUNS':27,'HITS':76,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':8,'RBI':41,'WALKS':29,'STRIKEOUTS':91,},
{'NAME':'Justin Bour','AGE':28,'TEAM':'MIA','POSITION':'1B','ATBATS':280,'RUNS':35,'HITS':74,'DOUBLES':12,'TRIPLES':1,'HOMERUNS':15,'RBI':51,'WALKS':38,'STRIKEOUTS':56,},
{'NAME':'Darwin Barney','AGE':30,'TEAM':'TOR','POSITION':'2B','ATBATS':279,'RUNS':35,'HITS':75,'DOUBLES':13,'TRIPLES':2,'HOMERUNS':4,'RBI':19,'WALKS':22,'STRIKEOUTS':48,},
{'NAME':'Ryan Schimpf','AGE':28,'TEAM':'SDP','POSITION':'2B','ATBATS':276,'RUNS':48,'HITS':60,'DOUBLES':17,'TRIPLES':5,'HOMERUNS':20,'RBI':51,'WALKS':42,'STRIKEOUTS':105,},
{'NAME':'Jurickson Profar','AGE':23,'TEAM':'TEX','POSITION':'3B','ATBATS':272,'RUNS':35,'HITS':65,'DOUBLES':6,'TRIPLES':3,'HOMERUNS':5,'RBI':20,'WALKS':30,'STRIKEOUTS':61,},
{'NAME':'Ezequiel Carrera','AGE':29,'TEAM':'TOR','POSITION':'RF','ATBATS':270,'RUNS':47,'HITS':67,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':6,'RBI':23,'WALKS':27,'STRIKEOUTS':70,},
{'NAME':'Ryon Healy','AGE':24,'TEAM':'OAK','POSITION':'3B','ATBATS':269,'RUNS':36,'HITS':82,'DOUBLES':20,'TRIPLES':0,'HOMERUNS':13,'RBI':37,'WALKS':12,'STRIKEOUTS':60,},
{'NAME':'Carlos Perez','AGE':25,'TEAM':'LAA','POSITION':'C','ATBATS':268,'RUNS':25,'HITS':56,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':5,'RBI':31,'WALKS':12,'STRIKEOUTS':49,},
{'NAME':'Steve Pearce','AGE':33,'TEAM':'TOT','POSITION':'1B','ATBATS':264,'RUNS':35,'HITS':76,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':13,'RBI':35,'WALKS':34,'STRIKEOUTS':54,},
{'NAME':'Chris Coghlan','AGE':31,'TEAM':'TOT','POSITION':'LF','ATBATS':261,'RUNS':35,'HITS':49,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':6,'RBI':30,'WALKS':35,'STRIKEOUTS':73,},
{'NAME':'Jefry Marte','AGE':25,'TEAM':'LAA','POSITION':'1B','ATBATS':258,'RUNS':38,'HITS':65,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':15,'RBI':44,'WALKS':18,'STRIKEOUTS':59,},
{'NAME':'Joey Rickard','AGE':25,'TEAM':'BAL','POSITION':'RF','ATBATS':257,'RUNS':32,'HITS':69,'DOUBLES':13,'TRIPLES':0,'HOMERUNS':5,'RBI':19,'WALKS':18,'STRIKEOUTS':54,},
{'NAME':'Scott Schebler','AGE':25,'TEAM':'CIN','POSITION':'RF','ATBATS':257,'RUNS':36,'HITS':68,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':9,'RBI':40,'WALKS':19,'STRIKEOUTS':59,},
{'NAME':'Jose Reyes','AGE':33,'TEAM':'NYM','POSITION':'3B','ATBATS':255,'RUNS':45,'HITS':68,'DOUBLES':13,'TRIPLES':4,'HOMERUNS':8,'RBI':24,'WALKS':23,'STRIKEOUTS':49,},
{'NAME':'Alex Dickerson','AGE':26,'TEAM':'SDP','POSITION':'LF','ATBATS':253,'RUNS':39,'HITS':65,'DOUBLES':16,'TRIPLES':2,'HOMERUNS':10,'RBI':37,'WALKS':26,'STRIKEOUTS':44,},
{'NAME':'Willson Contreras','AGE':24,'TEAM':'CHC','POSITION':'C','ATBATS':252,'RUNS':33,'HITS':71,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':12,'RBI':35,'WALKS':26,'STRIKEOUTS':67,},
{'NAME':'Sandy Leon','AGE':27,'TEAM':'BOS','POSITION':'C','ATBATS':252,'RUNS':36,'HITS':78,'DOUBLES':17,'TRIPLES':2,'HOMERUNS':7,'RBI':35,'WALKS':23,'STRIKEOUTS':66,},
{'NAME':'Travis d''Arnaud','AGE':27,'TEAM':'NYM','POSITION':'C','ATBATS':251,'RUNS':27,'HITS':62,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':4,'RBI':15,'WALKS':19,'STRIKEOUTS':50,},
{'NAME':'Yan Gomes','AGE':28,'TEAM':'CLE','POSITION':'C','ATBATS':251,'RUNS':22,'HITS':42,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':9,'RBI':34,'WALKS':9,'STRIKEOUTS':69,},
{'NAME':'Billy Butler','AGE':30,'TEAM':'TOT','POSITION':'DH','ATBATS':250,'RUNS':27,'HITS':71,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':5,'RBI':35,'WALKS':21,'STRIKEOUTS':42,},
{'NAME':'Daniel Descalso','AGE':29,'TEAM':'COL','POSITION':'SS','ATBATS':250,'RUNS':38,'HITS':66,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':8,'RBI':38,'WALKS':34,'STRIKEOUTS':56,},
{'NAME':'Ramon Flores','AGE':24,'TEAM':'MIL','POSITION':'RF','ATBATS':249,'RUNS':18,'HITS':51,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':2,'RBI':19,'WALKS':31,'STRIKEOUTS':58,},
{'NAME':'Tyler White','AGE':25,'TEAM':'HOU','POSITION':'1B','ATBATS':249,'RUNS':24,'HITS':54,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':8,'RBI':28,'WALKS':23,'STRIKEOUTS':65,},
{'NAME':'Franklin Gutierrez','AGE':33,'TEAM':'SEA','POSITION':'RF','ATBATS':248,'RUNS':33,'HITS':61,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':14,'RBI':39,'WALKS':29,'STRIKEOUTS':85,},
{'NAME':'A.J. Pierzynski','AGE':39,'TEAM':'ATL','POSITION':'C','ATBATS':247,'RUNS':15,'HITS':54,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':2,'RBI':23,'WALKS':6,'STRIKEOUTS':29,},
{'NAME':'Jarrod Saltalamacchia','AGE':31,'TEAM':'DET','POSITION':'C','ATBATS':246,'RUNS':30,'HITS':42,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':12,'RBI':38,'WALKS':41,'STRIKEOUTS':104,},
{'NAME':'Domingo Santana','AGE':23,'TEAM':'MIL','POSITION':'RF','ATBATS':246,'RUNS':34,'HITS':63,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':11,'RBI':32,'WALKS':32,'STRIKEOUTS':91,},
{'NAME':'Gordon Beckham','AGE':29,'TEAM':'TOT','POSITION':'2B','ATBATS':245,'RUNS':25,'HITS':52,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':5,'RBI':31,'WALKS':26,'STRIKEOUTS':52,},
{'NAME':'Jorge Polanco','AGE':22,'TEAM':'MIN','POSITION':'SS','ATBATS':245,'RUNS':24,'HITS':69,'DOUBLES':15,'TRIPLES':4,'HOMERUNS':4,'RBI':27,'WALKS':17,'STRIKEOUTS':46,},
{'NAME':'Chris Johnson','AGE':31,'TEAM':'MIA','POSITION':'1B','ATBATS':243,'RUNS':20,'HITS':54,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':5,'RBI':24,'WALKS':19,'STRIKEOUTS':78,},
{'NAME':'Gregor Blanco','AGE':32,'TEAM':'SFG','POSITION':'RF','ATBATS':241,'RUNS':28,'HITS':54,'DOUBLES':10,'TRIPLES':4,'HOMERUNS':1,'RBI':18,'WALKS':29,'STRIKEOUTS':51,},
{'NAME':'Miguel Montero','AGE':32,'TEAM':'CHC','POSITION':'C','ATBATS':241,'RUNS':33,'HITS':52,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':8,'RBI':33,'WALKS':38,'STRIKEOUTS':58,},
{'NAME':'Jose Peraza','AGE':22,'TEAM':'CIN','POSITION':'SS','ATBATS':241,'RUNS':25,'HITS':78,'DOUBLES':8,'TRIPLES':2,'HOMERUNS':3,'RBI':25,'WALKS':7,'STRIKEOUTS':33,},
{'NAME':'Ryan Rua','AGE':26,'TEAM':'TEX','POSITION':'LF','ATBATS':240,'RUNS':40,'HITS':62,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':8,'RBI':22,'WALKS':21,'STRIKEOUTS':76,},
{'NAME':'Juan Uribe','AGE':37,'TEAM':'CLE','POSITION':'3B','ATBATS':238,'RUNS':19,'HITS':49,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':7,'RBI':25,'WALKS':15,'STRIKEOUTS':49,},
{'NAME':'Trayce Thompson','AGE':25,'TEAM':'LAD','POSITION':'CF','ATBATS':236,'RUNS':31,'HITS':53,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':13,'RBI':32,'WALKS':26,'STRIKEOUTS':66,},
{'NAME':'Alejandro De Aza','AGE':32,'TEAM':'NYM','POSITION':'CF','ATBATS':234,'RUNS':31,'HITS':48,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':6,'RBI':25,'WALKS':26,'STRIKEOUTS':67,},
{'NAME':'Chase d''Arnaud','AGE':29,'TEAM':'ATL','POSITION':'SS','ATBATS':233,'RUNS':24,'HITS':57,'DOUBLES':14,'TRIPLES':2,'HOMERUNS':1,'RBI':21,'WALKS':23,'STRIKEOUTS':50,},
{'NAME':'Danny Santana','AGE':25,'TEAM':'MIN','POSITION':'CF','ATBATS':233,'RUNS':29,'HITS':56,'DOUBLES':10,'TRIPLES':2,'HOMERUNS':2,'RBI':14,'WALKS':12,'STRIKEOUTS':55,},
{'NAME':'Matthew Joyce','AGE':31,'TEAM':'PIT','POSITION':'RF','ATBATS':231,'RUNS':45,'HITS':56,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':13,'RBI':42,'WALKS':59,'STRIKEOUTS':67,},
{'NAME':'Bobby Wilson','AGE':33,'TEAM':'TOT','POSITION':'C','ATBATS':228,'RUNS':25,'HITS':54,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':7,'RBI':33,'WALKS':11,'STRIKEOUTS':64,},
{'NAME':'Jorge Soler','AGE':24,'TEAM':'CHC','POSITION':'LF','ATBATS':227,'RUNS':37,'HITS':54,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':12,'RBI':31,'WALKS':31,'STRIKEOUTS':66,},
{'NAME':'Curt Casali','AGE':27,'TEAM':'TBR','POSITION':'C','ATBATS':226,'RUNS':23,'HITS':42,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':8,'RBI':25,'WALKS':25,'STRIKEOUTS':82,},
{'NAME':'Cristhian Adames','AGE':24,'TEAM':'COL','POSITION':'SS','ATBATS':225,'RUNS':25,'HITS':49,'DOUBLES':7,'TRIPLES':3,'HOMERUNS':2,'RBI':17,'WALKS':24,'STRIKEOUTS':47,},
{'NAME':'Alex Rodriguez','AGE':40,'TEAM':'NYY','POSITION':'DH','ATBATS':225,'RUNS':19,'HITS':45,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':9,'RBI':31,'WALKS':14,'STRIKEOUTS':67,},
{'NAME':'J.B. Shuck','AGE':29,'TEAM':'CHW','POSITION':'CF','ATBATS':224,'RUNS':27,'HITS':46,'DOUBLES':5,'TRIPLES':2,'HOMERUNS':4,'RBI':14,'WALKS':12,'STRIKEOUTS':21,},
{'NAME':'Ryan Raburn','AGE':35,'TEAM':'COL','POSITION':'LF','ATBATS':223,'RUNS':30,'HITS':49,'DOUBLES':10,'TRIPLES':2,'HOMERUNS':9,'RBI':30,'WALKS':28,'STRIKEOUTS':80,},
{'NAME':'David Dahl','AGE':22,'TEAM':'COL','POSITION':'LF','ATBATS':222,'RUNS':42,'HITS':70,'DOUBLES':12,'TRIPLES':4,'HOMERUNS':7,'RBI':24,'WALKS':15,'STRIKEOUTS':59,},
{'NAME':'Ivan De Jesus','AGE':29,'TEAM':'CIN','POSITION':'SS','ATBATS':221,'RUNS':21,'HITS':56,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':1,'RBI':20,'WALKS':17,'STRIKEOUTS':51,},
{'NAME':'Michael Taylor','AGE':25,'TEAM':'WSN','POSITION':'CF','ATBATS':221,'RUNS':28,'HITS':51,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':7,'RBI':16,'WALKS':14,'STRIKEOUTS':77,},
{'NAME':'Philip Gosselin','AGE':27,'TEAM':'ARI','POSITION':'2B','ATBATS':220,'RUNS':26,'HITS':61,'DOUBLES':12,'TRIPLES':1,'HOMERUNS':2,'RBI':13,'WALKS':15,'STRIKEOUTS':46,},
{'NAME':'Brett Wallace','AGE':29,'TEAM':'SDP','POSITION':'3B','ATBATS':217,'RUNS':19,'HITS':41,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':6,'RBI':20,'WALKS':29,'STRIKEOUTS':83,},
{'NAME':'Enrique Hernandez','AGE':24,'TEAM':'LAD','POSITION':'LF','ATBATS':216,'RUNS':25,'HITS':41,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':7,'RBI':18,'WALKS':28,'STRIKEOUTS':64,},
{'NAME':'ByungHo Park','AGE':29,'TEAM':'MIN','POSITION':'DH','ATBATS':215,'RUNS':28,'HITS':41,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':12,'RBI':24,'WALKS':21,'STRIKEOUTS':80,},
{'NAME':'Greg Garcia','AGE':26,'TEAM':'STL','POSITION':'3B','ATBATS':214,'RUNS':33,'HITS':59,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':3,'RBI':17,'WALKS':38,'STRIKEOUTS':50,},
{'NAME':'Adam Rosales','AGE':33,'TEAM':'SDP','POSITION':'3B','ATBATS':214,'RUNS':37,'HITS':49,'DOUBLES':12,'TRIPLES':3,'HOMERUNS':13,'RBI':35,'WALKS':29,'STRIKEOUTS':88,},
{'NAME':'Tyler Goeddel','AGE':23,'TEAM':'PHI','POSITION':'LF','ATBATS':213,'RUNS':17,'HITS':41,'DOUBLES':3,'TRIPLES':3,'HOMERUNS':4,'RBI':16,'WALKS':17,'STRIKEOUTS':52,},
{'NAME':'Shawn O''Malley','AGE':28,'TEAM':'SEA','POSITION':'SS','ATBATS':210,'RUNS':24,'HITS':48,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':2,'RBI':17,'WALKS':18,'STRIKEOUTS':59,},
{'NAME':'Jett Bandy','AGE':26,'TEAM':'LAA','POSITION':'C','ATBATS':209,'RUNS':23,'HITS':49,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':8,'RBI':25,'WALKS':11,'STRIKEOUTS':38,},
{'NAME':'Martin Maldonado','AGE':29,'TEAM':'MIL','POSITION':'C','ATBATS':208,'RUNS':21,'HITS':42,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':8,'RBI':21,'WALKS':35,'STRIKEOUTS':56,},
{'NAME':'Keon Broxton','AGE':26,'TEAM':'MIL','POSITION':'CF','ATBATS':207,'RUNS':28,'HITS':50,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':9,'RBI':19,'WALKS':36,'STRIKEOUTS':88,},
{'NAME':'Tony Wolters','AGE':24,'TEAM':'COL','POSITION':'C','ATBATS':205,'RUNS':27,'HITS':53,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':3,'RBI':30,'WALKS':21,'STRIKEOUTS':53,},
{'NAME':'Gregorio Petit','AGE':31,'TEAM':'LAA','POSITION':'2B','ATBATS':204,'RUNS':21,'HITS':50,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':2,'RBI':17,'WALKS':15,'STRIKEOUTS':51,},
{'NAME':'Justin Morneau','AGE':35,'TEAM':'CHW','POSITION':'DH','ATBATS':203,'RUNS':16,'HITS':53,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':6,'RBI':25,'WALKS':12,'STRIKEOUTS':52,},
{'NAME':'Nolan Reimold','AGE':32,'TEAM':'BAL','POSITION':'LF','ATBATS':203,'RUNS':25,'HITS':45,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':6,'RBI':15,'WALKS':22,'STRIKEOUTS':62,},
{'NAME':'Chris Young','AGE':32,'TEAM':'BOS','POSITION':'LF','ATBATS':203,'RUNS':29,'HITS':56,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':9,'RBI':24,'WALKS':21,'STRIKEOUTS':50,},
{'NAME':'Oswaldo Arcia','AGE':25,'TEAM':'TOT','POSITION':'RF','ATBATS':202,'RUNS':17,'HITS':41,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':8,'RBI':23,'WALKS':18,'STRIKEOUTS':80,},
{'NAME':'Orlando Arcia','AGE':21,'TEAM':'MIL','POSITION':'SS','ATBATS':201,'RUNS':21,'HITS':44,'DOUBLES':10,'TRIPLES':3,'HOMERUNS':4,'RBI':17,'WALKS':15,'STRIKEOUTS':47,},
{'NAME':'Alex Bregman','AGE':22,'TEAM':'HOU','POSITION':'3B','ATBATS':201,'RUNS':31,'HITS':53,'DOUBLES':13,'TRIPLES':3,'HOMERUNS':8,'RBI':34,'WALKS':15,'STRIKEOUTS':52,},
{'NAME':'Carlos Ruiz','AGE':37,'TEAM':'TOT','POSITION':'C','ATBATS':201,'RUNS':21,'HITS':53,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':3,'RBI':15,'WALKS':27,'STRIKEOUTS':33,},
{'NAME':'Gary Sanchez','AGE':23,'TEAM':'NYY','POSITION':'C','ATBATS':201,'RUNS':34,'HITS':60,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':20,'RBI':42,'WALKS':24,'STRIKEOUTS':57,},
{'NAME':'Jeremy Hazelbaker','AGE':28,'TEAM':'STL','POSITION':'LF','ATBATS':200,'RUNS':35,'HITS':47,'DOUBLES':7,'TRIPLES':3,'HOMERUNS':12,'RBI':28,'WALKS':18,'STRIKEOUTS':64,},
{'NAME':'Desmond Jennings','AGE':29,'TEAM':'TBR','POSITION':'LF','ATBATS':200,'RUNS':22,'HITS':40,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':7,'RBI':20,'WALKS':21,'STRIKEOUTS':58,},
{'NAME':'Aaron Altherr','AGE':25,'TEAM':'PHI','POSITION':'RF','ATBATS':198,'RUNS':23,'HITS':39,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':4,'RBI':22,'WALKS':23,'STRIKEOUTS':69,},
{'NAME':'Tim Beckham','AGE':26,'TEAM':'TBR','POSITION':'SS','ATBATS':198,'RUNS':25,'HITS':49,'DOUBLES':12,'TRIPLES':5,'HOMERUNS':5,'RBI':16,'WALKS':14,'STRIKEOUTS':67,},
{'NAME':'Cody Asche','AGE':26,'TEAM':'PHI','POSITION':'LF','ATBATS':197,'RUNS':22,'HITS':42,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':4,'RBI':18,'WALKS':18,'STRIKEOUTS':54,},
{'NAME':'Clint Robinson','AGE':31,'TEAM':'WSN','POSITION':'1B','ATBATS':196,'RUNS':16,'HITS':46,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':5,'RBI':26,'WALKS':20,'STRIKEOUTS':38,},
{'NAME':'Miguel Rojas','AGE':27,'TEAM':'MIA','POSITION':'2B','ATBATS':194,'RUNS':27,'HITS':48,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':1,'RBI':14,'WALKS':11,'STRIKEOUTS':27,},
{'NAME':'Christian Bethancourt','AGE':24,'TEAM':'SDP','POSITION':'C','ATBATS':193,'RUNS':20,'HITS':44,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':6,'RBI':25,'WALKS':10,'STRIKEOUTS':56,},
{'NAME':'Conor Gillaspie','AGE':28,'TEAM':'SFG','POSITION':'3B','ATBATS':191,'RUNS':24,'HITS':50,'DOUBLES':8,'TRIPLES':4,'HOMERUNS':6,'RBI':25,'WALKS':12,'STRIKEOUTS':28,},
{'NAME':'Andres Blanco','AGE':32,'TEAM':'PHI','POSITION':'3B','ATBATS':190,'RUNS':26,'HITS':48,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':4,'RBI':21,'WALKS':11,'STRIKEOUTS':41,},
{'NAME':'Mallex Smith','AGE':23,'TEAM':'ATL','POSITION':'CF','ATBATS':189,'RUNS':28,'HITS':45,'DOUBLES':7,'TRIPLES':4,'HOMERUNS':3,'RBI':22,'WALKS':20,'STRIKEOUTS':48,},
{'NAME':'Brett Eibner','AGE':27,'TEAM':'TOT','POSITION':'RF','ATBATS':187,'RUNS':21,'HITS':36,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':6,'RBI':22,'WALKS':19,'STRIKEOUTS':50,},
{'NAME':'Mikie Mahtook','AGE':26,'TEAM':'TBR','POSITION':'LF','ATBATS':185,'RUNS':16,'HITS':36,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':3,'RBI':11,'WALKS':7,'STRIKEOUTS':68,},
{'NAME':'Rafael Ortega','AGE':25,'TEAM':'LAA','POSITION':'LF','ATBATS':185,'RUNS':24,'HITS':43,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':1,'RBI':16,'WALKS':13,'STRIKEOUTS':23,},
{'NAME':'Rene Rivera','AGE':32,'TEAM':'NYM','POSITION':'C','ATBATS':185,'RUNS':12,'HITS':41,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':6,'RBI':26,'WALKS':16,'STRIKEOUTS':54,},
{'NAME':'Matt Szczur','AGE':26,'TEAM':'CHC','POSITION':'LF','ATBATS':185,'RUNS':30,'HITS':48,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':5,'RBI':24,'WALKS':13,'STRIKEOUTS':39,},
{'NAME':'Ryan Goins','AGE':28,'TEAM':'TOR','POSITION':'2B','ATBATS':183,'RUNS':13,'HITS':34,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':3,'RBI':12,'WALKS':9,'STRIKEOUTS':48,},
{'NAME':'Abraham Almonte','AGE':27,'TEAM':'CLE','POSITION':'RF','ATBATS':182,'RUNS':24,'HITS':48,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':1,'RBI':22,'WALKS':8,'STRIKEOUTS':42,},
{'NAME':'Delino DeShields','AGE':23,'TEAM':'TEX','POSITION':'CF','ATBATS':182,'RUNS':36,'HITS':38,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':4,'RBI':13,'WALKS':15,'STRIKEOUTS':54,},
{'NAME':'Austin Jackson','AGE':29,'TEAM':'CHW','POSITION':'CF','ATBATS':181,'RUNS':24,'HITS':46,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':0,'RBI':18,'WALKS':17,'STRIKEOUTS':39,},
{'NAME':'Luis Sardinas','AGE':23,'TEAM':'TOT','POSITION':'SS','ATBATS':180,'RUNS':25,'HITS':44,'DOUBLES':6,'TRIPLES':1,'HOMERUNS':4,'RBI':18,'WALKS':12,'STRIKEOUTS':48,},
{'NAME':'Rickie Weeks','AGE':33,'TEAM':'ARI','POSITION':'LF','ATBATS':180,'RUNS':29,'HITS':43,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':9,'RBI':27,'WALKS':20,'STRIKEOUTS':54,},
{'NAME':'Tyler Holt','AGE':27,'TEAM':'CIN','POSITION':'CF','ATBATS':179,'RUNS':21,'HITS':42,'DOUBLES':5,'TRIPLES':3,'HOMERUNS':0,'RBI':13,'WALKS':23,'STRIKEOUTS':48,},
{'NAME':'Shin-Soo Choo','AGE':33,'TEAM':'TEX','POSITION':'RF','ATBATS':178,'RUNS':27,'HITS':43,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':7,'RBI':17,'WALKS':25,'STRIKEOUTS':46,},
{'NAME':'Juan Centeno','AGE':26,'TEAM':'MIN','POSITION':'C','ATBATS':176,'RUNS':16,'HITS':46,'DOUBLES':12,'TRIPLES':1,'HOMERUNS':3,'RBI':25,'WALKS':12,'STRIKEOUTS':38,},
{'NAME':'Nick Franklin','AGE':25,'TEAM':'TBR','POSITION':'LF','ATBATS':174,'RUNS':18,'HITS':47,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':6,'RBI':26,'WALKS':12,'STRIKEOUTS':42,},
{'NAME':'Andrew Romine','AGE':30,'TEAM':'DET','POSITION':'3B','ATBATS':174,'RUNS':21,'HITS':41,'DOUBLES':5,'TRIPLES':2,'HOMERUNS':2,'RBI':16,'WALKS':13,'STRIKEOUTS':38,},
{'NAME':'Trevor Brown','AGE':24,'TEAM':'SFG','POSITION':'C','ATBATS':173,'RUNS':17,'HITS':41,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':5,'RBI':19,'WALKS':10,'STRIKEOUTS':39,},
{'NAME':'Cliff Pennington','AGE':32,'TEAM':'LAA','POSITION':'2B','ATBATS':172,'RUNS':18,'HITS':36,'DOUBLES':4,'TRIPLES':2,'HOMERUNS':3,'RBI':10,'WALKS':13,'STRIKEOUTS':55,},
{'NAME':'Christian Vazquez','AGE':25,'TEAM':'BOS','POSITION':'C','ATBATS':172,'RUNS':21,'HITS':39,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':1,'RBI':12,'WALKS':10,'STRIKEOUTS':39,},
{'NAME':'Ramon Cabrera','AGE':26,'TEAM':'CIN','POSITION':'C','ATBATS':171,'RUNS':11,'HITS':42,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':3,'RBI':23,'WALKS':8,'STRIKEOUTS':30,},
{'NAME':'A.J. Ellis','AGE':35,'TEAM':'TOT','POSITION':'C','ATBATS':171,'RUNS':11,'HITS':37,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':2,'RBI':22,'WALKS':19,'STRIKEOUTS':31,},
{'NAME':'David Peralta','AGE':28,'TEAM':'ARI','POSITION':'RF','ATBATS':171,'RUNS':23,'HITS':43,'DOUBLES':9,'TRIPLES':5,'HOMERUNS':4,'RBI':15,'WALKS':8,'STRIKEOUTS':42,},
{'NAME':'Alex Avila','AGE':29,'TEAM':'CHW','POSITION':'C','ATBATS':169,'RUNS':19,'HITS':36,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':7,'RBI':11,'WALKS':38,'STRIKEOUTS':78,},
{'NAME':'Mike Aviles','AGE':35,'TEAM':'DET','POSITION':'RF','ATBATS':167,'RUNS':17,'HITS':35,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':1,'RBI':6,'WALKS':9,'STRIKEOUTS':27,},
{'NAME':'David Ross','AGE':39,'TEAM':'CHC','POSITION':'C','ATBATS':166,'RUNS':24,'HITS':38,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':10,'RBI':32,'WALKS':30,'STRIKEOUTS':54,},
{'NAME':'Austin Romine','AGE':27,'TEAM':'NYY','POSITION':'C','ATBATS':165,'RUNS':17,'HITS':40,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':4,'RBI':26,'WALKS':7,'STRIKEOUTS':31,},
{'NAME':'Mike Zunino','AGE':25,'TEAM':'SEA','POSITION':'C','ATBATS':164,'RUNS':16,'HITS':34,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':12,'RBI':31,'WALKS':21,'STRIKEOUTS':65,},
{'NAME':'Tommy Pham','AGE':28,'TEAM':'STL','POSITION':'CF','ATBATS':159,'RUNS':26,'HITS':36,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':9,'RBI':17,'WALKS':20,'STRIKEOUTS':71,},
{'NAME':'Jimmy Paredes','AGE':27,'TEAM':'TOT','POSITION':'LF','ATBATS':158,'RUNS':15,'HITS':35,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':5,'RBI':19,'WALKS':7,'STRIKEOUTS':48,},
{'NAME':'Ryan Flaherty','AGE':29,'TEAM':'BAL','POSITION':'3B','ATBATS':157,'RUNS':16,'HITS':34,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':3,'RBI':15,'WALKS':17,'STRIKEOUTS':48,},
{'NAME':'Ronald Torreyes','AGE':23,'TEAM':'NYY','POSITION':'3B','ATBATS':155,'RUNS':20,'HITS':40,'DOUBLES':7,'TRIPLES':4,'HOMERUNS':1,'RBI':12,'WALKS':10,'STRIKEOUTS':20,},
{'NAME':'Yolmer Sanchez','AGE':24,'TEAM':'CHW','POSITION':'2B','ATBATS':154,'RUNS':15,'HITS':32,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':4,'RBI':21,'WALKS':5,'STRIKEOUTS':42,},
{'NAME':'Lucas Duda','AGE':30,'TEAM':'NYM','POSITION':'1B','ATBATS':153,'RUNS':20,'HITS':35,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':7,'RBI':23,'WALKS':15,'STRIKEOUTS':36,},
{'NAME':'Roberto Perez','AGE':27,'TEAM':'CLE','POSITION':'C','ATBATS':153,'RUNS':14,'HITS':28,'DOUBLES':6,'TRIPLES':1,'HOMERUNS':3,'RBI':17,'WALKS':23,'STRIKEOUTS':44,},
{'NAME':'Rob Refsnyder','AGE':25,'TEAM':'NYY','POSITION':'1B','ATBATS':152,'RUNS':25,'HITS':38,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':0,'RBI':12,'WALKS':18,'STRIKEOUTS':30,},
{'NAME':'Kennys Vargas','AGE':25,'TEAM':'MIN','POSITION':'1B','ATBATS':152,'RUNS':27,'HITS':35,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':10,'RBI':20,'WALKS':24,'STRIKEOUTS':57,},
{'NAME':'Jimmy Rollins','AGE':37,'TEAM':'CHW','POSITION':'SS','ATBATS':149,'RUNS':25,'HITS':33,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':2,'RBI':8,'WALKS':16,'STRIKEOUTS':33,},
{'NAME':'Chris Herrmann','AGE':28,'TEAM':'ARI','POSITION':'C','ATBATS':148,'RUNS':21,'HITS':42,'DOUBLES':5,'TRIPLES':4,'HOMERUNS':6,'RBI':28,'WALKS':16,'STRIKEOUTS':44,},
{'NAME':'Tommy La Stella','AGE':27,'TEAM':'CHC','POSITION':'3B','ATBATS':148,'RUNS':17,'HITS':40,'DOUBLES':12,'TRIPLES':1,'HOMERUNS':2,'RBI':11,'WALKS':18,'STRIKEOUTS':27,},
{'NAME':'Robinson Chirinos','AGE':32,'TEAM':'TEX','POSITION':'C','ATBATS':147,'RUNS':21,'HITS':33,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':9,'RBI':20,'WALKS':15,'STRIKEOUTS':44,},
{'NAME':'Christian Colon','AGE':27,'TEAM':'KCR','POSITION':'2B','ATBATS':147,'RUNS':13,'HITS':34,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':13,'WALKS':11,'STRIKEOUTS':31,},
{'NAME':'Adam Frazier','AGE':24,'TEAM':'PIT','POSITION':'LF','ATBATS':146,'RUNS':21,'HITS':44,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':2,'RBI':11,'WALKS':12,'STRIKEOUTS':26,},
{'NAME':'Stephen Drew','AGE':33,'TEAM':'WSN','POSITION':'2B','ATBATS':143,'RUNS':24,'HITS':38,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':8,'RBI':21,'WALKS':16,'STRIKEOUTS':31,},
{'NAME':'Juan Lagares','AGE':27,'TEAM':'NYM','POSITION':'CF','ATBATS':142,'RUNS':15,'HITS':34,'DOUBLES':7,'TRIPLES':2,'HOMERUNS':3,'RBI':9,'WALKS':11,'STRIKEOUTS':27,},
{'NAME':'Alexi Amarista','AGE':27,'TEAM':'SDP','POSITION':'2B','ATBATS':140,'RUNS':9,'HITS':36,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':11,'WALKS':8,'STRIKEOUTS':26,},
{'NAME':'Chris Gimenez','AGE':33,'TEAM':'CLE','POSITION':'C','ATBATS':139,'RUNS':17,'HITS':30,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':4,'RBI':11,'WALKS':10,'STRIKEOUTS':41,},
{'NAME':'Chris Heisey','AGE':31,'TEAM':'WSN','POSITION':'LF','ATBATS':139,'RUNS':18,'HITS':30,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':9,'RBI':17,'WALKS':13,'STRIKEOUTS':44,},
{'NAME':'David Wright','AGE':33,'TEAM':'NYM','POSITION':'3B','ATBATS':137,'RUNS':18,'HITS':31,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':7,'RBI':14,'WALKS':26,'STRIKEOUTS':55,},
{'NAME':'Tyler Collins','AGE':26,'TEAM':'DET','POSITION':'CF','ATBATS':136,'RUNS':14,'HITS':32,'DOUBLES':2,'TRIPLES':3,'HOMERUNS':4,'RBI':15,'WALKS':13,'STRIKEOUTS':38,},
{'NAME':'Adalberto Mondesi','AGE':20,'TEAM':'KCR','POSITION':'2B','ATBATS':135,'RUNS':16,'HITS':25,'DOUBLES':1,'TRIPLES':3,'HOMERUNS':2,'RBI':13,'WALKS':6,'STRIKEOUTS':48,},
{'NAME':'Omar Infante','AGE':34,'TEAM':'KCR','POSITION':'2B','ATBATS':134,'RUNS':16,'HITS':32,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':0,'RBI':11,'WALKS':9,'STRIKEOUTS':23,},
{'NAME':'Preston Tucker','AGE':25,'TEAM':'HOU','POSITION':'DH','ATBATS':134,'RUNS':11,'HITS':22,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':4,'RBI':8,'WALKS':8,'STRIKEOUTS':40,},
{'NAME':'Caleb Joseph','AGE':30,'TEAM':'BAL','POSITION':'C','ATBATS':132,'RUNS':7,'HITS':23,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':7,'STRIKEOUTS':28,},
{'NAME':'Kevin Plawecki','AGE':25,'TEAM':'NYM','POSITION':'C','ATBATS':132,'RUNS':6,'HITS':26,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':11,'WALKS':17,'STRIKEOUTS':33,},
{'NAME':'Daniel Castro','AGE':23,'TEAM':'ATL','POSITION':'SS','ATBATS':130,'RUNS':8,'HITS':26,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':7,'WALKS':7,'STRIKEOUTS':24,},
{'NAME':'Yuli Gurriel','AGE':32,'TEAM':'HOU','POSITION':'3B','ATBATS':130,'RUNS':13,'HITS':34,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':3,'RBI':15,'WALKS':5,'STRIKEOUTS':12,},
{'NAME':'Daniel Nava','AGE':33,'TEAM':'TOT','POSITION':'LF','ATBATS':130,'RUNS':11,'HITS':29,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':13,'WALKS':10,'STRIKEOUTS':30,},
{'NAME':'Dansby Swanson','AGE':22,'TEAM':'ATL','POSITION':'SS','ATBATS':129,'RUNS':20,'HITS':39,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':3,'RBI':17,'WALKS':13,'STRIKEOUTS':34,},
{'NAME':'Josh Bell','AGE':23,'TEAM':'PIT','POSITION':'1B','ATBATS':128,'RUNS':18,'HITS':35,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':3,'RBI':19,'WALKS':21,'STRIKEOUTS':19,},
{'NAME':'Jarrett Parker','AGE':27,'TEAM':'SFG','POSITION':'RF','ATBATS':127,'RUNS':22,'HITS':30,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':5,'RBI':14,'WALKS':19,'STRIKEOUTS':44,},
{'NAME':'Jeff Mathis','AGE':33,'TEAM':'MIA','POSITION':'C','ATBATS':126,'RUNS':12,'HITS':30,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':2,'RBI':15,'WALKS':4,'STRIKEOUTS':36,},
{'NAME':'Hank Conger','AGE':28,'TEAM':'TBR','POSITION':'C','ATBATS':124,'RUNS':6,'HITS':24,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':3,'RBI':10,'WALKS':12,'STRIKEOUTS':40,},
{'NAME':'Drew Butera','AGE':32,'TEAM':'KCR','POSITION':'C','ATBATS':123,'RUNS':18,'HITS':35,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':4,'RBI':16,'WALKS':8,'STRIKEOUTS':36,},
{'NAME':'A.J. Reed','AGE':23,'TEAM':'HOU','POSITION':'1B','ATBATS':122,'RUNS':11,'HITS':20,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':3,'RBI':8,'WALKS':18,'STRIKEOUTS':48,},
{'NAME':'Alex Presley','AGE':30,'TEAM':'TOT','POSITION':'LF','ATBATS':121,'RUNS':12,'HITS':24,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':3,'RBI':11,'WALKS':11,'STRIKEOUTS':25,},
{'NAME':'Tony Kemp','AGE':24,'TEAM':'HOU','POSITION':'LF','ATBATS':120,'RUNS':15,'HITS':26,'DOUBLES':4,'TRIPLES':3,'HOMERUNS':1,'RBI':7,'WALKS':14,'STRIKEOUTS':27,},
{'NAME':'Luke Maile','AGE':25,'TEAM':'TBR','POSITION':'C','ATBATS':119,'RUNS':10,'HITS':27,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':3,'RBI':15,'WALKS':4,'STRIKEOUTS':36,},
{'NAME':'Josh Thole','AGE':29,'TEAM':'TOR','POSITION':'C','ATBATS':118,'RUNS':7,'HITS':20,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':13,'STRIKEOUTS':28,},
{'NAME':'Bryan Holaday','AGE':28,'TEAM':'TOT','POSITION':'C','ATBATS':117,'RUNS':17,'HITS':27,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':2,'RBI':14,'WALKS':7,'STRIKEOUTS':28,},
{'NAME':'Eric Fryer','AGE':30,'TEAM':'TOT','POSITION':'C','ATBATS':116,'RUNS':19,'HITS':31,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':0,'RBI':13,'WALKS':13,'STRIKEOUTS':25,},
{'NAME':'Marlon Byrd','AGE':38,'TEAM':'CLE','POSITION':'RF','ATBATS':115,'RUNS':11,'HITS':31,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':5,'RBI':19,'WALKS':11,'STRIKEOUTS':38,},
{'NAME':'Max Muncy','AGE':25,'TEAM':'OAK','POSITION':'2B','ATBATS':113,'RUNS':13,'HITS':21,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':8,'WALKS':20,'STRIKEOUTS':24,},
{'NAME':'Albert Almora','AGE':22,'TEAM':'CHC','POSITION':'CF','ATBATS':112,'RUNS':14,'HITS':31,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':3,'RBI':14,'WALKS':5,'STRIKEOUTS':20,},
{'NAME':'Ji-Man Choi','AGE':25,'TEAM':'LAA','POSITION':'1B','ATBATS':112,'RUNS':9,'HITS':19,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':5,'RBI':12,'WALKS':16,'STRIKEOUTS':27,},
{'NAME':'Mac Williamson','AGE':25,'TEAM':'SFG','POSITION':'RF','ATBATS':112,'RUNS':14,'HITS':25,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':6,'RBI':15,'WALKS':13,'STRIKEOUTS':35,},
{'NAME':'Mitch Haniger','AGE':25,'TEAM':'ARI','POSITION':'CF','ATBATS':109,'RUNS':9,'HITS':25,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':5,'RBI':17,'WALKS':12,'STRIKEOUTS':27,},
{'NAME':'Kelby Tomlinson','AGE':26,'TEAM':'SFG','POSITION':'2B','ATBATS':106,'RUNS':13,'HITS':31,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':12,'STRIKEOUTS':18,},
{'NAME':'Andrew Benintendi','AGE':21,'TEAM':'BOS','POSITION':'LF','ATBATS':105,'RUNS':16,'HITS':31,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':2,'RBI':14,'WALKS':10,'STRIKEOUTS':25,},
{'NAME':'Ryan Hanigan','AGE':35,'TEAM':'BOS','POSITION':'C','ATBATS':105,'RUNS':9,'HITS':18,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':14,'WALKS':7,'STRIKEOUTS':27,},
{'NAME':'T.J. Rivera','AGE':27,'TEAM':'NYM','POSITION':'2B','ATBATS':105,'RUNS':10,'HITS':35,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':3,'RBI':16,'WALKS':3,'STRIKEOUTS':17,},
{'NAME':'Andrew Toles','AGE':24,'TEAM':'LAD','POSITION':'LF','ATBATS':105,'RUNS':19,'HITS':33,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':3,'RBI':16,'WALKS':8,'STRIKEOUTS':25,},
{'NAME':'Mike Moustakas','AGE':27,'TEAM':'KCR','POSITION':'3B','ATBATS':104,'RUNS':12,'HITS':25,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':7,'RBI':13,'WALKS':9,'STRIKEOUTS':13,},
{'NAME':'Scott Van Slyke','AGE':29,'TEAM':'LAD','POSITION':'LF','ATBATS':102,'RUNS':10,'HITS':23,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':5,'STRIKEOUTS':24,},
{'NAME':'Michael Martinez','AGE':33,'TEAM':'TOT','POSITION':'2B','ATBATS':101,'RUNS':16,'HITS':24,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':4,'STRIKEOUTS':23,},
{'NAME':'Omar Narvaez','AGE':24,'TEAM':'CHW','POSITION':'C','ATBATS':101,'RUNS':13,'HITS':27,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':10,'WALKS':14,'STRIKEOUTS':14,},
{'NAME':'Brandon Barnes','AGE':30,'TEAM':'COL','POSITION':'LF','ATBATS':100,'RUNS':10,'HITS':22,'DOUBLES':6,'TRIPLES':2,'HOMERUNS':0,'RBI':8,'WALKS':3,'STRIKEOUTS':30,},
{'NAME':'Teoscar Hernandez','AGE':23,'TEAM':'HOU','POSITION':'LF','ATBATS':100,'RUNS':15,'HITS':23,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':4,'RBI':11,'WALKS':11,'STRIKEOUTS':28,},
{'NAME':'Jose Lobaton','AGE':31,'TEAM':'WSN','POSITION':'C','ATBATS':99,'RUNS':10,'HITS':23,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':3,'RBI':8,'WALKS':12,'STRIKEOUTS':18,},
{'NAME':'Shane Robinson','AGE':31,'TEAM':'LAA','POSITION':'LF','ATBATS':98,'RUNS':16,'HITS':17,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':10,'WALKS':10,'STRIKEOUTS':17,},
{'NAME':'Chris Stewart','AGE':34,'TEAM':'PIT','POSITION':'C','ATBATS':98,'RUNS':10,'HITS':21,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':12,'STRIKEOUTS':15,},
{'NAME':'Joey Wendle','AGE':26,'TEAM':'OAK','POSITION':'2B','ATBATS':96,'RUNS':11,'HITS':25,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':11,'WALKS':6,'STRIKEOUTS':16,},
{'NAME':'Socrates Brito','AGE':23,'TEAM':'ARI','POSITION':'CF','ATBATS':95,'RUNS':10,'HITS':17,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':4,'RBI':12,'WALKS':2,'STRIKEOUTS':23,},
{'NAME':'Steven Moya','AGE':24,'TEAM':'DET','POSITION':'RF','ATBATS':94,'RUNS':9,'HITS':24,'DOUBLES':4,'TRIPLES':2,'HOMERUNS':5,'RBI':11,'WALKS':5,'STRIKEOUTS':38,},
{'NAME':'Guillermo Heredia','AGE':25,'TEAM':'SEA','POSITION':'LF','ATBATS':92,'RUNS':12,'HITS':23,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':12,'WALKS':12,'STRIKEOUTS':15,},
{'NAME':'Bruce Maxwell','AGE':25,'TEAM':'OAK','POSITION':'C','ATBATS':92,'RUNS':8,'HITS':26,'DOUBLES':6,'TRIPLES':1,'HOMERUNS':1,'RBI':14,'WALKS':8,'STRIKEOUTS':24,},
{'NAME':'Casey McGehee','AGE':33,'TEAM':'DET','POSITION':'3B','ATBATS':92,'RUNS':4,'HITS':21,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':3,'STRIKEOUTS':14,},
{'NAME':'Ben Paulsen','AGE':28,'TEAM':'COL','POSITION':'1B','ATBATS':92,'RUNS':8,'HITS':20,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':1,'RBI':11,'WALKS':5,'STRIKEOUTS':27,},
{'NAME':'Anthony Gose','AGE':25,'TEAM':'DET','POSITION':'CF','ATBATS':91,'RUNS':11,'HITS':19,'DOUBLES':2,'TRIPLES':2,'HOMERUNS':2,'RBI':7,'WALKS':9,'STRIKEOUTS':38,},
{'NAME':'Tuffy Gosewisch','AGE':32,'TEAM':'ARI','POSITION':'C','ATBATS':90,'RUNS':8,'HITS':14,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':3,'RBI':7,'WALKS':7,'STRIKEOUTS':22,},
{'NAME':'Anthony Recker','AGE':32,'TEAM':'ATL','POSITION':'C','ATBATS':90,'RUNS':6,'HITS':25,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':2,'RBI':15,'WALKS':16,'STRIKEOUTS':22,},
{'NAME':'Matt Reynolds','AGE':25,'TEAM':'NYM','POSITION':'SS','ATBATS':89,'RUNS':11,'HITS':20,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':3,'RBI':13,'WALKS':4,'STRIKEOUTS':34,},
{'NAME':'Ramiro Pena','AGE':30,'TEAM':'SFG','POSITION':'2B','ATBATS':87,'RUNS':9,'HITS':26,'DOUBLES':6,'TRIPLES':1,'HOMERUNS':1,'RBI':10,'WALKS':2,'STRIKEOUTS':16,},
{'NAME':'Madison Bumgarner','AGE':26,'TEAM':'SFG','POSITION':'P','ATBATS':86,'RUNS':8,'HITS':16,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':3,'RBI':9,'WALKS':10,'STRIKEOUTS':43,},
{'NAME':'Kaleb Cowart','AGE':24,'TEAM':'LAA','POSITION':'3B','ATBATS':85,'RUNS':8,'HITS':15,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':8,'WALKS':0,'STRIKEOUTS':23,},
{'NAME':'Erik Kratz','AGE':36,'TEAM':'TOT','POSITION':'C','ATBATS':85,'RUNS':3,'HITS':8,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':1,'STRIKEOUTS':32,},
{'NAME':'Aaron Judge','AGE':24,'TEAM':'NYY','POSITION':'RF','ATBATS':84,'RUNS':10,'HITS':15,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':4,'RBI':10,'WALKS':9,'STRIKEOUTS':42,},
{'NAME':'Tyler Austin','AGE':24,'TEAM':'NYY','POSITION':'1B','ATBATS':83,'RUNS':7,'HITS':20,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':5,'RBI':12,'WALKS':7,'STRIKEOUTS':36,},
{'NAME':'Darin Ruf','AGE':29,'TEAM':'PHI','POSITION':'1B','ATBATS':83,'RUNS':8,'HITS':17,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':3,'RBI':9,'WALKS':4,'STRIKEOUTS':25,},
{'NAME':'John Ryan Murphy','AGE':25,'TEAM':'MIN','POSITION':'C','ATBATS':82,'RUNS':4,'HITS':12,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':5,'STRIKEOUTS':19,},
{'NAME':'Nick Buss','AGE':29,'TEAM':'LAA','POSITION':'LF','ATBATS':81,'RUNS':7,'HITS':16,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':1,'RBI':8,'WALKS':6,'STRIKEOUTS':24,},
{'NAME':'Carl Crawford','AGE':34,'TEAM':'LAD','POSITION':'LF','ATBATS':81,'RUNS':8,'HITS':15,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':0,'RBI':6,'WALKS':4,'STRIKEOUTS':11,},
{'NAME':'Taylor Motter','AGE':26,'TEAM':'TBR','POSITION':'NONE','ATBATS':80,'RUNS':11,'HITS':15,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':2,'RBI':9,'WALKS':11,'STRIKEOUTS':19,},
{'NAME':'Drew Stubbs','AGE':31,'TEAM':'TOT','POSITION':'LF','ATBATS':80,'RUNS':13,'HITS':18,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':3,'RBI':7,'WALKS':12,'STRIKEOUTS':38,},
{'NAME':'Jake Elmore','AGE':29,'TEAM':'MIL','POSITION':'LF','ATBATS':78,'RUNS':7,'HITS':17,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':17,'STRIKEOUTS':17,},
{'NAME':'Josh Phegley','AGE':28,'TEAM':'OAK','POSITION':'C','ATBATS':78,'RUNS':11,'HITS':20,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':10,'WALKS':5,'STRIKEOUTS':13,},
{'NAME':'Geovany Soto','AGE':33,'TEAM':'LAA','POSITION':'C','ATBATS':78,'RUNS':11,'HITS':21,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':4,'RBI':9,'WALKS':6,'STRIKEOUTS':21,},
{'NAME':'Eric Campbell','AGE':29,'TEAM':'NYM','POSITION':'1B','ATBATS':75,'RUNS':9,'HITS':13,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':9,'WALKS':10,'STRIKEOUTS':24,},
{'NAME':'Brandon Nimmo','AGE':23,'TEAM':'NYM','POSITION':'LF','ATBATS':73,'RUNS':12,'HITS':20,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':6,'WALKS':6,'STRIKEOUTS':20,},
{'NAME':'Rob Segedin','AGE':27,'TEAM':'LAD','POSITION':'NONE','ATBATS':73,'RUNS':9,'HITS':17,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':2,'RBI':12,'WALKS':6,'STRIKEOUTS':22,},
{'NAME':'Jabari Blash','AGE':26,'TEAM':'SDP','POSITION':'RF','ATBATS':71,'RUNS':7,'HITS':12,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':3,'RBI':5,'WALKS':11,'STRIKEOUTS':34,},
{'NAME':'Manny Pina','AGE':29,'TEAM':'MIL','POSITION':'C','ATBATS':71,'RUNS':4,'HITS':18,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':2,'RBI':12,'WALKS':10,'STRIKEOUTS':15,},
{'NAME':'Johnny Cueto','AGE':30,'TEAM':'SFG','POSITION':'P','ATBATS':70,'RUNS':1,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':2,'STRIKEOUTS':24,},
{'NAME':'Max Scherzer','AGE':31,'TEAM':'WSN','POSITION':'P','ATBATS':70,'RUNS':4,'HITS':13,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':12,'WALKS':2,'STRIKEOUTS':30,},
{'NAME':'Steve Clevenger','AGE':30,'TEAM':'SEA','POSITION':'C','ATBATS':68,'RUNS':7,'HITS':15,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':8,'STRIKEOUTS':14,},
{'NAME':'Dustin Garneau','AGE':28,'TEAM':'COL','POSITION':'C','ATBATS':68,'RUNS':7,'HITS':16,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':6,'WALKS':6,'STRIKEOUTS':22,},
{'NAME':'Charlie Culberson','AGE':27,'TEAM':'LAD','POSITION':'SS','ATBATS':67,'RUNS':6,'HITS':20,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':1,'STRIKEOUTS':13,},
{'NAME':'David Lough','AGE':30,'TEAM':'PHI','POSITION':'LF','ATBATS':67,'RUNS':6,'HITS':16,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':0,'RBI':4,'WALKS':9,'STRIKEOUTS':8,},
{'NAME':'Yadiel Rivera','AGE':24,'TEAM':'MIL','POSITION':'3B','ATBATS':66,'RUNS':12,'HITS':14,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':2,'STRIKEOUTS':20,},
{'NAME':'Ruben Tejada','AGE':26,'TEAM':'TOT','POSITION':'3B','ATBATS':66,'RUNS':9,'HITS':11,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':7,'STRIKEOUTS':13,},
{'NAME':'Jake Arrieta','AGE':30,'TEAM':'CHC','POSITION':'P','ATBATS':65,'RUNS':7,'HITS':17,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':2,'RBI':7,'WALKS':4,'STRIKEOUTS':28,},
{'NAME':'Jason Hammel','AGE':33,'TEAM':'CHC','POSITION':'P','ATBATS':65,'RUNS':6,'HITS':16,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':7,'WALKS':1,'STRIKEOUTS':24,},
{'NAME':'Peter O''Brien','AGE':25,'TEAM':'ARI','POSITION':'LF','ATBATS':64,'RUNS':6,'HITS':9,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':5,'RBI':9,'WALKS':3,'STRIKEOUTS':27,},
{'NAME':'Tanner Roark','AGE':29,'TEAM':'WSN','POSITION':'P','ATBATS':64,'RUNS':1,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':5,'STRIKEOUTS':25,},
{'NAME':'Jeff Samardzija','AGE':31,'TEAM':'SFG','POSITION':'P','ATBATS':64,'RUNS':4,'HITS':10,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':0,'RBI':9,'WALKS':1,'STRIKEOUTS':28,},
{'NAME':'Ehire Adrianza','AGE':26,'TEAM':'SFG','POSITION':'SS','ATBATS':63,'RUNS':3,'HITS':16,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':7,'WALKS':2,'STRIKEOUTS':13,},
{'NAME':'John Lackey','AGE':37,'TEAM':'CHC','POSITION':'P','ATBATS':63,'RUNS':1,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':2,'STRIKEOUTS':31,},
{'NAME':'Logan Schafer','AGE':29,'TEAM':'MIN','POSITION':'LF','ATBATS':63,'RUNS':8,'HITS':15,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':0,'RBI':1,'WALKS':8,'STRIKEOUTS':16,},
{'NAME':'Xavier Scruggs','AGE':28,'TEAM':'MIA','POSITION':'1B','ATBATS':62,'RUNS':1,'HITS':13,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':5,'STRIKEOUTS':20,},
{'NAME':'Blake Swihart','AGE':24,'TEAM':'BOS','POSITION':'LF','ATBATS':62,'RUNS':9,'HITS':16,'DOUBLES':0,'TRIPLES':3,'HOMERUNS':0,'RBI':5,'WALKS':11,'STRIKEOUTS':17,},
{'NAME':'Adam Wainwright','AGE':34,'TEAM':'STL','POSITION':'P','ATBATS':62,'RUNS':6,'HITS':13,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':2,'RBI':18,'WALKS':2,'STRIKEOUTS':17,},
{'NAME':'Dustin Ackley','AGE':28,'TEAM':'NYY','POSITION':'1B','ATBATS':61,'RUNS':6,'HITS':9,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':8,'STRIKEOUTS':9,},
{'NAME':'Bryce Brentz','AGE':27,'TEAM':'BOS','POSITION':'LF','ATBATS':61,'RUNS':8,'HITS':17,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':3,'STRIKEOUTS':17,},
{'NAME':'Jerad Eickhoff','AGE':25,'TEAM':'PHI','POSITION':'P','ATBATS':61,'RUNS':4,'HITS':8,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Chris Taylor','AGE':25,'TEAM':'TOT','POSITION':'3B','ATBATS':61,'RUNS':8,'HITS':13,'DOUBLES':2,'TRIPLES':2,'HOMERUNS':1,'RBI':7,'WALKS':4,'STRIKEOUTS':15,},
{'NAME':'Bartolo Colon','AGE':43,'TEAM':'NYM','POSITION':'P','ATBATS':60,'RUNS':4,'HITS':5,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':1,'STRIKEOUTS':40,},
{'NAME':'Tony Renda','AGE':25,'TEAM':'CIN','POSITION':'NONE','ATBATS':60,'RUNS':4,'HITS':11,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':5,'STRIKEOUTS':11,},
{'NAME':'Jon Lester','AGE':32,'TEAM':'CHC','POSITION':'P','ATBATS':59,'RUNS':3,'HITS':6,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':6,'STRIKEOUTS':18,},
{'NAME':'Carlos Martinez','AGE':24,'TEAM':'STL','POSITION':'P','ATBATS':59,'RUNS':5,'HITS':14,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':0,'STRIKEOUTS':13,},
{'NAME':'Wilmer Difo','AGE':24,'TEAM':'WSN','POSITION':'NONE','ATBATS':58,'RUNS':14,'HITS':16,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':8,'STRIKEOUTS':12,},
{'NAME':'Kyle Hendricks','AGE':26,'TEAM':'CHC','POSITION':'P','ATBATS':58,'RUNS':1,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':29,},
{'NAME':'Ty Kelly','AGE':27,'TEAM':'NYM','POSITION':'3B','ATBATS':58,'RUNS':9,'HITS':14,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':1,'RBI':7,'WALKS':11,'STRIKEOUTS':9,},
{'NAME':'Noah Syndergaard','AGE':23,'TEAM':'NYM','POSITION':'P','ATBATS':58,'RUNS':6,'HITS':11,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':3,'RBI':6,'WALKS':7,'STRIKEOUTS':34,},
{'NAME':'Kenta Maeda','AGE':28,'TEAM':'LAD','POSITION':'P','ATBATS':57,'RUNS':5,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Roman Quinn','AGE':23,'TEAM':'PHI','POSITION':'LF','ATBATS':57,'RUNS':10,'HITS':15,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':8,'STRIKEOUTS':19,},
{'NAME':'Hanser Alberto','AGE':23,'TEAM':'TEX','POSITION':'3B','ATBATS':56,'RUNS':2,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':0,'STRIKEOUTS':17,},
{'NAME':'Stephen Cardullo','AGE':28,'TEAM':'COL','POSITION':'1B','ATBATS':56,'RUNS':5,'HITS':12,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':2,'RBI':6,'WALKS':3,'STRIKEOUTS':12,},
{'NAME':'Jerry Sands','AGE':28,'TEAM':'CHW','POSITION':'DH','ATBATS':55,'RUNS':2,'HITS':13,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':3,'STRIKEOUTS':24,},
{'NAME':'Jeremy Hellickson','AGE':29,'TEAM':'PHI','POSITION':'P','ATBATS':54,'RUNS':3,'HITS':9,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':4,'STRIKEOUTS':24,},
{'NAME':'Gorkys Hernandez','AGE':28,'TEAM':'SFG','POSITION':'CF','ATBATS':54,'RUNS':7,'HITS':14,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':3,'STRIKEOUTS':11,},
{'NAME':'Tyler Chatwood','AGE':26,'TEAM':'COL','POSITION':'P','ATBATS':53,'RUNS':3,'HITS':10,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':0,'RBI':4,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'Zach Davies','AGE':23,'TEAM':'MIL','POSITION':'P','ATBATS':53,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':22,},
{'NAME':'Brandon Finnegan','AGE':23,'TEAM':'CIN','POSITION':'P','ATBATS':53,'RUNS':4,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':18,},
{'NAME':'Robbie Ray','AGE':24,'TEAM':'ARI','POSITION':'P','ATBATS':53,'RUNS':3,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':1,'STRIKEOUTS':26,},
{'NAME':'Jaff Decker','AGE':26,'TEAM':'TBR','POSITION':'RF','ATBATS':52,'RUNS':1,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':14,},
{'NAME':'Jose Fernandez','AGE':23,'TEAM':'MIA','POSITION':'P','ATBATS':52,'RUNS':3,'HITS':13,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':1,'STRIKEOUTS':13,},
{'NAME':'Gio Gonzalez','AGE':30,'TEAM':'WSN','POSITION':'P','ATBATS':52,'RUNS':1,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':24,},
{'NAME':'Zack Greinke','AGE':32,'TEAM':'ARI','POSITION':'P','ATBATS':52,'RUNS':4,'HITS':11,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':3,'STRIKEOUTS':9,},
{'NAME':'Dan Straily','AGE':27,'TEAM':'CIN','POSITION':'P','ATBATS':52,'RUNS':2,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':40,},
{'NAME':'Cole Gillespie','AGE':32,'TEAM':'MIA','POSITION':'NONE','ATBATS':51,'RUNS':7,'HITS':12,'DOUBLES':3,'TRIPLES':2,'HOMERUNS':0,'RBI':5,'WALKS':3,'STRIKEOUTS':14,},
{'NAME':'Marco Hernandez','AGE':23,'TEAM':'BOS','POSITION':'2B','ATBATS':51,'RUNS':11,'HITS':15,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':5,'STRIKEOUTS':10,},
{'NAME':'Tom Koehler','AGE':30,'TEAM':'MIA','POSITION':'P','ATBATS':51,'RUNS':1,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':1,'STRIKEOUTS':28,},
{'NAME':'Jordan Pacheco','AGE':30,'TEAM':'CIN','POSITION':'NONE','ATBATS':51,'RUNS':1,'HITS':8,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':14,},
{'NAME':'Chad Pinder','AGE':24,'TEAM':'OAK','POSITION':'2B','ATBATS':51,'RUNS':4,'HITS':12,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':3,'STRIKEOUTS':14,},
{'NAME':'Steve Selsky','AGE':26,'TEAM':'CIN','POSITION':'RF','ATBATS':51,'RUNS':9,'HITS':16,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':7,'WALKS':2,'STRIKEOUTS':22,},
{'NAME':'Jason Coats','AGE':26,'TEAM':'CHW','POSITION':'RF','ATBATS':50,'RUNS':8,'HITS':10,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':5,'STRIKEOUTS':12,},
{'NAME':'Devin Mesoraco','AGE':28,'TEAM':'CIN','POSITION':'C','ATBATS':50,'RUNS':2,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':5,'STRIKEOUTS':10,},
{'NAME':'Jimmy Nelson','AGE':27,'TEAM':'MIL','POSITION':'P','ATBATS':50,'RUNS':1,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':2,'STRIKEOUTS':32,},
{'NAME':'Jemile Weeks','AGE':29,'TEAM':'SDP','POSITION':'2B','ATBATS':50,'RUNS':5,'HITS':7,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':14,},
{'NAME':'Chad Bettis','AGE':27,'TEAM':'COL','POSITION':'P','ATBATS':49,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':4,'STRIKEOUTS':21,},
{'NAME':'Patrick Corbin','AGE':26,'TEAM':'ARI','POSITION':'P','ATBATS':49,'RUNS':7,'HITS':15,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':0,'RBI':4,'WALKS':1,'STRIKEOUTS':14,},
{'NAME':'Mike Leake','AGE':28,'TEAM':'STL','POSITION':'P','ATBATS':49,'RUNS':3,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':3,'STRIKEOUTS':19,},
{'NAME':'Josh Rutledge','AGE':27,'TEAM':'BOS','POSITION':'3B','ATBATS':49,'RUNS':9,'HITS':13,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':6,'STRIKEOUTS':19,},
{'NAME':'Hector Sanchez','AGE':26,'TEAM':'TOT','POSITION':'C','ATBATS':49,'RUNS':3,'HITS':13,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':3,'RBI':8,'WALKS':4,'STRIKEOUTS':10,},
{'NAME':'Julio Teheran','AGE':25,'TEAM':'ATL','POSITION':'P','ATBATS':49,'RUNS':1,'HITS':10,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Ben Gamel','AGE':24,'TEAM':'TOT','POSITION':'RF','ATBATS':48,'RUNS':9,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':6,'STRIKEOUTS':16,},
{'NAME':'Leury Garcia','AGE':25,'TEAM':'CHW','POSITION':'CF','ATBATS':48,'RUNS':6,'HITS':11,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':1,'RBI':5,'WALKS':1,'STRIKEOUTS':13,},
{'NAME':'Tyler Ladendorf','AGE':28,'TEAM':'OAK','POSITION':'2B','ATBATS':48,'RUNS':6,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':13,},
{'NAME':'Richie Shaffer','AGE':25,'TEAM':'TBR','POSITION':'1B','ATBATS':48,'RUNS':5,'HITS':12,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':5,'STRIKEOUTS':18,},
{'NAME':'Cory Spangenberg','AGE':25,'TEAM':'SDP','POSITION':'2B','ATBATS':48,'RUNS':6,'HITS':11,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':1,'RBI':8,'WALKS':4,'STRIKEOUTS':13,},
{'NAME':'Stephen Strasburg','AGE':27,'TEAM':'WSN','POSITION':'P','ATBATS':48,'RUNS':3,'HITS':10,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':2,'STRIKEOUTS':11,},
{'NAME':'Jon Gray','AGE':24,'TEAM':'COL','POSITION':'P','ATBATS':47,'RUNS':2,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':2,'STRIKEOUTS':30,},
{'NAME':'Colin Walsh','AGE':26,'TEAM':'MIL','POSITION':'3B','ATBATS':47,'RUNS':4,'HITS':4,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':15,'STRIKEOUTS':22,},
{'NAME':'Grant Green','AGE':28,'TEAM':'SFG','POSITION':'2B','ATBATS':46,'RUNS':7,'HITS':12,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':3,'STRIKEOUTS':8,},
{'NAME':'Jared Hoying','AGE':27,'TEAM':'TEX','POSITION':'RF','ATBATS':46,'RUNS':8,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':3,'STRIKEOUTS':8,},
{'NAME':'Clayton Kershaw','AGE':28,'TEAM':'LAD','POSITION':'P','ATBATS':46,'RUNS':2,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Brandon Snyder','AGE':29,'TEAM':'ATL','POSITION':'NONE','ATBATS':46,'RUNS':8,'HITS':11,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':4,'RBI':9,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Matt Wisler','AGE':23,'TEAM':'ATL','POSITION':'P','ATBATS':46,'RUNS':2,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':21,},
{'NAME':'Chase Anderson','AGE':28,'TEAM':'MIL','POSITION':'P','ATBATS':45,'RUNS':3,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':27,},
{'NAME':'Emmanuel Burriss','AGE':31,'TEAM':'PHI','POSITION':'NONE','ATBATS':45,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':10,},
{'NAME':'Hernan Iribarren','AGE':32,'TEAM':'CIN','POSITION':'NONE','ATBATS':45,'RUNS':6,'HITS':14,'DOUBLES':0,'TRIPLES':3,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':11,},
{'NAME':'Wei-Yin Chen','AGE':30,'TEAM':'MIA','POSITION':'P','ATBATS':44,'RUNS':0,'HITS':0,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':18,},
{'NAME':'Tom Murphy','AGE':25,'TEAM':'COL','POSITION':'C','ATBATS':44,'RUNS':8,'HITS':12,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':5,'RBI':13,'WALKS':4,'STRIKEOUTS':19,},
{'NAME':'Archie Bradley','AGE':23,'TEAM':'ARI','POSITION':'P','ATBATS':43,'RUNS':2,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':0,'STRIKEOUTS':28,},
{'NAME':'Scott Kazmir','AGE':32,'TEAM':'LAD','POSITION':'P','ATBATS':43,'RUNS':3,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':24,},
{'NAME':'Matt McBride','AGE':31,'TEAM':'OAK','POSITION':'C','ATBATS':43,'RUNS':4,'HITS':9,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':10,},
{'NAME':'Jacob deGrom','AGE':28,'TEAM':'NYM','POSITION':'P','ATBATS':42,'RUNS':6,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':12,},
{'NAME':'Brian Goodwin','AGE':25,'TEAM':'WSN','POSITION':'NONE','ATBATS':42,'RUNS':1,'HITS':12,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':0,'RBI':5,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'Francisco Liriano','AGE':32,'TEAM':'TOT','POSITION':'P','ATBATS':42,'RUNS':2,'HITS':12,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':0,'STRIKEOUTS':16,},
{'NAME':'Mark Canha','AGE':27,'TEAM':'OAK','POSITION':'NONE','ATBATS':41,'RUNS':4,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':3,'RBI':6,'WALKS':0,'STRIKEOUTS':20,},
{'NAME':'Adam Conley','AGE':26,'TEAM':'MIA','POSITION':'P','ATBATS':41,'RUNS':4,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':22,},
{'NAME':'Anthony DeSclafani','AGE':26,'TEAM':'CIN','POSITION':'P','ATBATS':41,'RUNS':0,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':22,},
{'NAME':'Rey Fuentes','AGE':25,'TEAM':'KCR','POSITION':'NONE','ATBATS':41,'RUNS':2,'HITS':13,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':3,'STRIKEOUTS':8,},
{'NAME':'Jaime Garcia','AGE':29,'TEAM':'STL','POSITION':'P','ATBATS':41,'RUNS':3,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':2,'STRIKEOUTS':17,},
{'NAME':'A.J. Pollock','AGE':28,'TEAM':'ARI','POSITION':'CF','ATBATS':41,'RUNS':9,'HITS':10,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':5,'STRIKEOUTS':8,},
{'NAME':'Joe Ross','AGE':23,'TEAM':'WSN','POSITION':'P','ATBATS':41,'RUNS':2,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':3,'STRIKEOUTS':15,},
{'NAME':'Gerrit Cole','AGE':25,'TEAM':'PIT','POSITION':'P','ATBATS':40,'RUNS':3,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':0,'STRIKEOUTS':19,},
{'NAME':'Brett Nicholas','AGE':27,'TEAM':'TEX','POSITION':'C','ATBATS':40,'RUNS':5,'HITS':11,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':4,'STRIKEOUTS':9,},
{'NAME':'Francisco Pena','AGE':26,'TEAM':'BAL','POSITION':'C','ATBATS':40,'RUNS':5,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'Vince Velasquez','AGE':24,'TEAM':'PHI','POSITION':'P','ATBATS':40,'RUNS':4,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Michael Brantley','AGE':29,'TEAM':'CLE','POSITION':'LF','ATBATS':39,'RUNS':5,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':7,'WALKS':3,'STRIKEOUTS':6,},
{'NAME':'Wily Peralta','AGE':27,'TEAM':'MIL','POSITION':'P','ATBATS':39,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':6,'WALKS':0,'STRIKEOUTS':15,},
{'NAME':'Jose Pirela','AGE':26,'TEAM':'SDP','POSITION':'2B','ATBATS':39,'RUNS':2,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':9,},
{'NAME':'Michael Wacha','AGE':24,'TEAM':'STL','POSITION':'P','ATBATS':39,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':3,'STRIKEOUTS':22,},
{'NAME':'Danny Worth','AGE':30,'TEAM':'HOU','POSITION':'NONE','ATBATS':39,'RUNS':4,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':6,},
{'NAME':'Emilio Bonifacio','AGE':31,'TEAM':'ATL','POSITION':'LF','ATBATS':38,'RUNS':6,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':3,'STRIKEOUTS':12,},
{'NAME':'Jorge De La Rosa','AGE':35,'TEAM':'COL','POSITION':'P','ATBATS':38,'RUNS':4,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'Luis Perdomo','AGE':23,'TEAM':'SDP','POSITION':'P','ATBATS':38,'RUNS':1,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':15,},
{'NAME':'Alberto Rosario','AGE':29,'TEAM':'STL','POSITION':'C','ATBATS':38,'RUNS':3,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':2,'STRIKEOUTS':5,},
{'NAME':'Raimel Tapia','AGE':22,'TEAM':'COL','POSITION':'NONE','ATBATS':38,'RUNS':4,'HITS':10,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':2,'STRIKEOUTS':11,},
{'NAME':'Christian Friedrich','AGE':28,'TEAM':'SDP','POSITION':'P','ATBATS':37,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':23,},
{'NAME':'Manuel Margot','AGE':21,'TEAM':'SDP','POSITION':'NONE','ATBATS':37,'RUNS':4,'HITS':9,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':0,'RBI':3,'WALKS':0,'STRIKEOUTS':7,},
{'NAME':'Mike Foltynewicz','AGE':24,'TEAM':'ATL','POSITION':'P','ATBATS':36,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':19,},
{'NAME':'Steven Matz','AGE':25,'TEAM':'NYM','POSITION':'P','ATBATS':36,'RUNS':0,'HITS':5,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':2,'WALKS':4,'STRIKEOUTS':11,},
{'NAME':'Tyler Anderson','AGE':26,'TEAM':'COL','POSITION':'P','ATBATS':35,'RUNS':1,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':4,'STRIKEOUTS':11,},
{'NAME':'Junior Guerra','AGE':31,'TEAM':'MIL','POSITION':'P','ATBATS':35,'RUNS':2,'HITS':8,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':13,},
{'NAME':'Junior Lake','AGE':26,'TEAM':'TOR','POSITION':'RF','ATBATS':35,'RUNS':5,'HITS':7,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':4,'STRIKEOUTS':11,},
{'NAME':'Drew Pomeranz','AGE':27,'TEAM':'TOT','POSITION':'P','ATBATS':35,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':0,'STRIKEOUTS':21,},
{'NAME':'Hunter Renfroe','AGE':24,'TEAM':'SDP','POSITION':'NONE','ATBATS':35,'RUNS':8,'HITS':13,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':4,'RBI':14,'WALKS':1,'STRIKEOUTS':5,},
{'NAME':'Andrew Cashner','AGE':29,'TEAM':'TOT','POSITION':'P','ATBATS':34,'RUNS':3,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':3,'STRIKEOUTS':13,},
{'NAME':'Matt den Dekker','AGE':28,'TEAM':'WSN','POSITION':'NONE','ATBATS':34,'RUNS':3,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':4,'STRIKEOUTS':10,},
{'NAME':'Craig Gentry','AGE':32,'TEAM':'LAA','POSITION':'LF','ATBATS':34,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':6,},
{'NAME':'Cedric Hunter','AGE':28,'TEAM':'PHI','POSITION':'LF','ATBATS':34,'RUNS':3,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':2,'STRIKEOUTS':6,},
{'NAME':'Colin Rea','AGE':25,'TEAM':'TOT','POSITION':'P','ATBATS':33,'RUNS':3,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':16,},
{'NAME':'Austin Barnes','AGE':26,'TEAM':'LAD','POSITION':'NONE','ATBATS':32,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':5,'STRIKEOUTS':9,},
{'NAME':'Jeff Locke','AGE':28,'TEAM':'PIT','POSITION':'P','ATBATS':32,'RUNS':0,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':17,},
{'NAME':'Shelby Miller','AGE':25,'TEAM':'ARI','POSITION':'P','ATBATS':32,'RUNS':4,'HITS':4,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':21,},
{'NAME':'Adam Morgan','AGE':26,'TEAM':'PHI','POSITION':'P','ATBATS':32,'RUNS':1,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':11,},
{'NAME':'Jameson Taillon','AGE':24,'TEAM':'PIT','POSITION':'P','ATBATS':32,'RUNS':0,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':17,},
{'NAME':'Tim Federowicz','AGE':28,'TEAM':'CHC','POSITION':'C','ATBATS':31,'RUNS':3,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Alen Hanson','AGE':23,'TEAM':'PIT','POSITION':'NONE','ATBATS':31,'RUNS':5,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':5,},
{'NAME':'Paul Janish','AGE':33,'TEAM':'BAL','POSITION':'NONE','ATBATS':31,'RUNS':3,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':3,'STRIKEOUTS':3,},
{'NAME':'Kyle Jensen','AGE':28,'TEAM':'ARI','POSITION':'NONE','ATBATS':31,'RUNS':5,'HITS':6,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':2,'RBI':7,'WALKS':2,'STRIKEOUTS':13,},
{'NAME':'Matt Moore','AGE':27,'TEAM':'TOT','POSITION':'P','ATBATS':31,'RUNS':2,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':13,},
{'NAME':'Jon Niese','AGE':29,'TEAM':'TOT','POSITION':'P','ATBATS':30,'RUNS':1,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'Aaron Nola','AGE':23,'TEAM':'PHI','POSITION':'P','ATBATS':30,'RUNS':1,'HITS':1,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':3,'STRIKEOUTS':17,},
{'NAME':'Reid Brignac','AGE':30,'TEAM':'ATL','POSITION':'NONE','ATBATS':29,'RUNS':3,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':8,},
{'NAME':'Chris Colabello','AGE':32,'TEAM':'TOR','POSITION':'NONE','ATBATS':29,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':9,},
{'NAME':'Chris Rusin','AGE':29,'TEAM':'COL','POSITION':'P','ATBATS':29,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':0,'RBI':3,'WALKS':0,'STRIKEOUTS':6,},
{'NAME':'Matt Garza','AGE':32,'TEAM':'MIL','POSITION':'P','ATBATS':28,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':17,},
{'NAME':'JaCoby Jones','AGE':24,'TEAM':'DET','POSITION':'NONE','ATBATS':28,'RUNS':3,'HITS':6,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':12,},
{'NAME':'Pedro Severino','AGE':22,'TEAM':'WSN','POSITION':'C','ATBATS':28,'RUNS':6,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':5,'STRIKEOUTS':3,},
{'NAME':'Matt Cain','AGE':31,'TEAM':'SFG','POSITION':'P','ATBATS':27,'RUNS':1,'HITS':2,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':0,'STRIKEOUTS':17,},
{'NAME':'Darrell Ceciliani','AGE':26,'TEAM':'TOR','POSITION':'NONE','ATBATS':27,'RUNS':2,'HITS':3,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':14,},
{'NAME':'Todd Cunningham','AGE':27,'TEAM':'LAA','POSITION':'LF','ATBATS':27,'RUNS':5,'HITS':4,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':6,},
{'NAME':'Don Kelly','AGE':36,'TEAM':'MIA','POSITION':'1B','ATBATS':27,'RUNS':2,'HITS':4,'DOUBLES':0,'TRIPLES':2,'HOMERUNS':0,'RBI':3,'WALKS':2,'STRIKEOUTS':5,},
{'NAME':'Will Middlebrooks','AGE':27,'TEAM':'MIL','POSITION':'NONE','ATBATS':27,'RUNS':2,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':13,},
{'NAME':'Bud Norris','AGE':31,'TEAM':'TOT','POSITION':'P','ATBATS':27,'RUNS':2,'HITS':6,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':0,'RBI':1,'WALKS':3,'STRIKEOUTS':7,},
{'NAME':'Jake Peavy','AGE':35,'TEAM':'SFG','POSITION':'P','ATBATS':27,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':2,'STRIKEOUTS':12,},
{'NAME':'Mason Williams','AGE':24,'TEAM':'NYY','POSITION':'NONE','ATBATS':27,'RUNS':4,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Taylor Featherston','AGE':26,'TEAM':'PHI','POSITION':'NONE','ATBATS':26,'RUNS':2,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':11,},
{'NAME':'Cole Figueroa','AGE':29,'TEAM':'PIT','POSITION':'NONE','ATBATS':26,'RUNS':0,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':2,},
{'NAME':'Ivan Nova','AGE':29,'TEAM':'TOT','POSITION':'P','ATBATS':26,'RUNS':1,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':18,},
{'NAME':'Braden Shipley','AGE':24,'TEAM':'ARI','POSITION':'P','ATBATS':26,'RUNS':2,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Joey Gallo','AGE':22,'TEAM':'TEX','POSITION':'NONE','ATBATS':25,'RUNS':2,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':5,'STRIKEOUTS':19,},
{'NAME':'Destin Hood','AGE':26,'TEAM':'MIA','POSITION':'NONE','ATBATS':25,'RUNS':3,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':0,'STRIKEOUTS':11,},
{'NAME':'Jason Rogers','AGE':28,'TEAM':'PIT','POSITION':'NONE','ATBATS':25,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':0,'RBI':2,'WALKS':7,'STRIKEOUTS':9,},
{'NAME':'Jose Rondon','AGE':22,'TEAM':'SDP','POSITION':'NONE','ATBATS':25,'RUNS':1,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':4,},
{'NAME':'Jesus Sucre','AGE':28,'TEAM':'SEA','POSITION':'NONE','ATBATS':25,'RUNS':4,'HITS':12,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':2,'STRIKEOUTS':5,},
{'NAME':'Robert Andino','AGE':32,'TEAM':'MIA','POSITION':'NONE','ATBATS':24,'RUNS':2,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':4,},
{'NAME':'Carlos Asuaje','AGE':24,'TEAM':'SDP','POSITION':'NONE','ATBATS':24,'RUNS':2,'HITS':5,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':4,},
{'NAME':'Andre Ethier','AGE':34,'TEAM':'LAD','POSITION':'NONE','ATBATS':24,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':2,'STRIKEOUTS':6,},
{'NAME':'Pedro Florimon','AGE':29,'TEAM':'PIT','POSITION':'NONE','ATBATS':24,'RUNS':4,'HITS':5,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':4,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Austin Hedges','AGE':23,'TEAM':'SDP','POSITION':'NONE','ATBATS':24,'RUNS':2,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':7,},
{'NAME':'Justin Ruggiano','AGE':34,'TEAM':'TOT','POSITION':'NONE','ATBATS':24,'RUNS':4,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':7,'WALKS':2,'STRIKEOUTS':10,},
{'NAME':'Ross Stripling','AGE':26,'TEAM':'LAD','POSITION':'P','ATBATS':24,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':12,},
{'NAME':'Andy Wilkins','AGE':27,'TEAM':'MIL','POSITION':'NONE','ATBATS':24,'RUNS':3,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':3,'STRIKEOUTS':10,},
{'NAME':'Zach Eflin','AGE':22,'TEAM':'PHI','POSITION':'P','ATBATS':23,'RUNS':2,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':8,},
{'NAME':'Edwin Jackson','AGE':32,'TEAM':'TOT','POSITION':'P','ATBATS':23,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':11,},
{'NAME':'Chad Kuhl','AGE':23,'TEAM':'PIT','POSITION':'P','ATBATS':23,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':9,},
{'NAME':'Colin Moran','AGE':23,'TEAM':'HOU','POSITION':'NONE','ATBATS':23,'RUNS':1,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':8,},
{'NAME':'James Beresford','AGE':27,'TEAM':'MIN','POSITION':'NONE','ATBATS':22,'RUNS':0,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':6,},
{'NAME':'Mike Freeman','AGE':28,'TEAM':'TOT','POSITION':'NONE','ATBATS':22,'RUNS':1,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':7,},
{'NAME':'Matt Harvey','AGE':27,'TEAM':'NYM','POSITION':'P','ATBATS':22,'RUNS':2,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':8,},
{'NAME':'Justin Nicolino','AGE':24,'TEAM':'MIA','POSITION':'P','ATBATS':22,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':11,},
{'NAME':'Michael Reed','AGE':23,'TEAM':'MIL','POSITION':'NONE','ATBATS':22,'RUNS':3,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':7,},
{'NAME':'Donovan Solano','AGE':28,'TEAM':'NYY','POSITION':'NONE','ATBATS':22,'RUNS':5,'HITS':5,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':1,'STRIKEOUTS':3,},
{'NAME':'Julio Urias','AGE':19,'TEAM':'LAD','POSITION':'P','ATBATS':22,'RUNS':0,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':9,},
{'NAME':'Kyle Waldrop','AGE':24,'TEAM':'CIN','POSITION':'NONE','ATBATS':22,'RUNS':1,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':5,},
{'NAME':'Tim Adleman','AGE':28,'TEAM':'CIN','POSITION':'P','ATBATS':21,'RUNS':2,'HITS':4,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':0,'STRIKEOUTS':11,},
{'NAME':'Aaron Blair','AGE':24,'TEAM':'ATL','POSITION':'P','ATBATS':21,'RUNS':0,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':9,},
{'NAME':'Paul Clemens','AGE':28,'TEAM':'TOT','POSITION':'P','ATBATS':21,'RUNS':1,'HITS':0,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':11,},
{'NAME':'Munenori Kawasaki','AGE':35,'TEAM':'CHC','POSITION':'2B','ATBATS':21,'RUNS':3,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':5,},
{'NAME':'Patrick Kivlehan','AGE':26,'TEAM':'TOT','POSITION':'NONE','ATBATS':21,'RUNS':5,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':2,'STRIKEOUTS':11,},
{'NAME':'Matt Olson','AGE':22,'TEAM':'OAK','POSITION':'NONE','ATBATS':21,'RUNS':3,'HITS':2,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':7,'STRIKEOUTS':4,},
{'NAME':'James Shields','AGE':34,'TEAM':'TOT','POSITION':'P','ATBATS':21,'RUNS':1,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':12,},
{'NAME':'Albert Suarez','AGE':26,'TEAM':'SFG','POSITION':'P','ATBATS':21,'RUNS':1,'HITS':4,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':11,},
{'NAME':'John Lamb','AGE':25,'TEAM':'CIN','POSITION':'P','ATBATS':20,'RUNS':0,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':12,},
]

main()