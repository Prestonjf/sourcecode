# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2018 - Music Library
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Music Library
DESCRIPTION: There are many calculations associated with a music library. Each of the questions below will represent
some of the tasks that applications, like iTune,s perform. The main function will call your questions (using your logic) and
print out the answers. Some of your questions may require you to call previous functions.

1. For each question, write your code to solve each objective. (return the answer programmatically. ie via variables)
2. Each objective is worth a designated number of points. 106 Points Total.
3. Highest number of points wins. Question 19 is a tie breaker. If there is still a tie, question 18, 17 and so on will break the tie.
4. The main function will call and run all of the questions and print the production data. Do not modify this function.
5. Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
6. Run your program often to test and check for errors.

INFORMATION: Some questions will use a list of dictionaries. Each dictionary, represents one song. Each key in the dictionary
represents a piece of information about the song.
The structure will be:
[ 
    {
        'NAME':'Love Me Do'    // Song Name (String)
        'ARTIST:'The Beatles'    // Song Artist (String)
        'ALBUM':'1'    // Song Album (String)
        'DURATION': 150   // Song Duration in seconds (number)
        'FILESIZE':3.2    // Size of song file in Megabytes (number)
        'RATING':5   // Song rating on scale of 1 to 5 (number)  
    }
    {
        ...
    }
] 

GOOD LUCK! '''

# QUESTION 0: MUSIC LIBRARY TITLE
# OBJECTIVE A (2): Return a string with your team number, name and the text "Music Library" in the format:
# "1 - Bath High School Blue - Music Library"
def getMusicLibraryTitle():
    
    return ''

# QUESTION 1: CD AREA
# OBJECTIVE A (2): A CD is a circular piece of plastic with music burned on it. Determine and return the
# area of the circle given the radius, r. Import pi from the math library. Do not round.
def getCDArea(r):
    
    return ''

# QUESTION 2: HAS ENOUGH SPACE
# OBJECTIVE A (3): The size of some data, dataSize, is passed into the function along with the 
# total storage space of an external hard drive, totalSize. Return true if dataSize is 
# less than or equal to the totalSize, otherwise return false.
def hasEnoughSpace(dataSize, totalSize):
    
    return ''

# QUESTION 3: MUSIC LOGGER
# OBJECTIVE A (3): The name, artist, and album of a song are passed into the function 
# below. All parameters are strings. Append the strings together in the following format
# and return the resulting string. Make sure to include a space between the strings and colons.
# name : artist : album
def logSong(name, artist, album):
    
    return ''

# QUESTION 4: TIME CONVERTER
# OBJECTIVE A (3): The function below takes in one parameter, time (in seconds). Convert the
# time to minutes.
# OBJECTIVE B (3): Most media libraries display time in the format 0:00. Format the time in
# this format. Return the time string (Whether you completed objective b or not.)
def formatTime(time):

    return ''

# QUESTION 5: REVERSE STRING
# OBJECTIVE A (3): A string, s, is passed into the function below. Reverse the order of the characters
# and return the new string.
def reverseString(s):

    return ''

# QUESTION 6: SONG LOOK UP
# OBJECTIVE A (4): A list of dictionaries, library, representing your music library
# and song name, name are passed into the function below. 
# (see structure above for key descriptions. View data in the main function.)
# Loop through the library and find the dictionary where the song name equals the name
# passed into the function. If found return the dictionary, if not, return an empty dictionary.
# Name must match exactly. 
def getSong(library, name):
    d = {}

    return d

# QUESTION 7: TOTAL TIME
# OBJECTIVE A (4): Your music library (list of dictionaries) is passed into the function below.
# Calculate the sum of the time. Call your function formatTime to convert the seconds to minutes.
# Return the resulting string.
def getTotalTime(library):

    return ''

# QUESTION 8: AVERAGE SIZE
# OBJECTIVE A (5): Your music library (list of dictionaries) is passed into the function below.
# A second parameter, attribute, represents one of three values DURATION, FILESIZE, or RATING.
# These values correspond to number values for each song. With this function we can calculate 
# the average for any of the values making this a useful and reusable function.
# Calculate the average of the specific attribute in your library. Return the average. Do Not round.
# If the attribute == DURATION, return the average in seconds. Do not call formatTime.
# OBJECTIVE B (2): If Attribute does not equal DURATION, FILESIZE, or RATING return -1.
def getAverageSize(library, attribute):

    return ''

# QUESTION 9: MIX TAPES
# OBJECTIVE A (5): A mix tape (or mix CD) in this scenario is a collection of songs burned to a disc.
# We have CDs that can hold 700MB of data and want to burn every song in our library that has a rating 
# of 3 or higher. Additionally, the file format we use to burn the songs increases the FILESIZE of each
# song by 10 times. Calculate and return how many CDs we would need to burn the entire library to disc.
def getNumberOfMixTapes(library):

    return ''

# QUESTION 10: THE BEST SONG
# OBJECTIVE A (5): The best song in our library is defined by the following criteria.
# It has a RATING of 5. It's ratio of DURATION / FILESIZE is the largest. The ARTIST is
# not AWOLNATION. (Sorry AWOLNATION fans). Return the best song or songs if multiple fit this
# criteria (if any exist at all). Return the results in a list.
# OBJECTIVE B (2): Append the ratio to the song name. ex) 'Love Me Do 62.857142857142854'
def getTheBestSong(library):
    bestSongs = []

    return bestSongs

# QUESTION 11: BLANK SPACES AND FACTOR FUN
# OBJECTIVE A (5): The music library is passed into the function below. Count how many spaces between words
# are in the song NAME, ARTIST, AND ALBUM. Only consider songs where the DURATION is a factor of 6. Return the sum.
def getSpacesCount(library):
    count = 0;

    return count

# QUESTION 12: TRUNCATE SONG TITLE
# OBJECTIVE A (5): For display reasons, sometimes a string of text needs to be trimmed or modified.
# A string, s, representing a song title is passed into the function below. If the string is more than
# 20 characters, return only the first 20 characters followed by the string '...'. 
def truncateSongTitle(s):

    return ''

# QUESTION 13: SONG TITLE CAPITALIZED
# OBJECTIVE A (5): Some songs may not have the first letter of each word capitalized. The function below
# takes in the title of a song. Capitalize the first letter of each word (words defined as being
# separated by a space) and return the string.
def capitalizeSongTitle(s):

    return ''

# QUESTION 14: MOST ALBUM SONGS
# OBJECTIVE A (6): The music library is passed into the function below. Determine how many songs
# per album exist in the library and return the name of the album. If multiple albums have the same
# number of songs return the additional albums separated by a comma. 
def getAlbumMostSongs(library):
    names = ''

    return names


# QUESTION 15: MIX TAPE PART 2
# OBJECTIVE A (6): Your library of songs is passed into the function below. You need to burn a CD with
# 10 songs, but you only want the shortest songs. Determine the 10 shortest songs and return the song
# names in a list. If the 10th song has the same length as the 11th song, 12th song etc. you need to
# add those songs to the list as well. 
# OBJECTIVE B (2): Append the total number of songs to the beginning of the list.
# HINT: Sort the list using the key parameter. Use the function getDuration as the key value. 
def getShortestMixTape(library):
    cd = []  
    return cd

def getDuration(s):
    return s['DURATION']

# QUESTION 16: MEDIAN SONG DURATION
# OBJECTIVE A (7): The median is the middle number in a set. If there is an even amount of
# numbers, you average the two middle numbers. Find the median DURATION in the music library
# and return the median duration in seconds. Assume more than 1 song will be in the library. 
# Use Integer Division when searching for the middle index.
def getMedianDuration(library):
    median = 0

    return median

# QUESTION 17: FIBONNACI SIZE?
# OBJECTIVE A (7): The library of music is passed into the function below. For the duration of each song,
# determine if the number is part of the fibonacci sequence. If so, add the number to a running total.
# Return the sum. Assume no song will be longer than 1200 seconds.
# 
def fibonnaciSum(library):
    total = 0
   
    return total

# QUESTION 18: SONG ANAGRAMS
# OBJECTIVE A (8): An Anagram is a word or phrase that is made up of the exact same characters as
# another word or phrase. The music library is passed into the function below along with a string, phrase.
# Write code to find all song names that are an Anagram for given phrase. Return the song names in a list.
# HINT: Remove the spaces from the phrase and song name. Normalize characters to upper case.
def getAnagrams(library, phrase):
    anagrams = []

    return anagrams

# QUESTION 19: FREE STYLE
# OBJECTIVE A (4): Write a custom function that calculates a statistic with the music library that hasn't been used in this test.
# OBJECTIVE B (2): Write a two sentence comment that explains what statistic you are calculating.
# OBJECTIVE C (2): Call a previous function from this test within your calculation.
# Objective D (2): Import a Python library within the function.
def getStatistic(library):
    x = 0

    return x

###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    
    library = [
                {'NAME':'Love Me Do', 'ARTIST':'The Beatles', 'ALBUM':'1', 'DURATION':150, 'FILESIZE':3.2, 'RATING':3},
                {'NAME':'Can''t Buy Me Love', 'ARTIST':'The Beatles', 'ALBUM':'1', 'DURATION':144, 'FILESIZE':2.5, 'RATING':4},
                {'NAME':'Eight Days A Week', 'ARTIST':'The Beatles', 'ALBUM':'1', 'DURATION':164, 'FILESIZE':3.0, 'RATING':4},
                {'NAME':'Get Free', 'ARTIST':'Lana Del Rey', 'ALBUM':'Lust For Life', 'DURATION':332, 'FILESIZE':4.4, 'RATING':5},
                {'NAME':'13 Beaches','ARTIST':'Lana Del Rey','ALBUM':'Lust for Life','DURATION':301,'FILESIZE':4.3,'RATING':4},
                {'NAME':'Lust For Life', 'ARTIST':'Lana Del Rey', 'ALBUM':'Lust for Life', 'DURATION':319, 'FILESIZE':4.2,'RATING':1},
                {'NAME':'When the World Was at War We Kept Dancing', 'ARTIST':'Lana Del Rey','ALBUM':'Lust for Life','DURATION':276,'FILESIZE':3.9,'RATING':3},
                {'NAME':'In my Feelings', 'ARTIST':'Lana Del Rey', 'ALBUM':'Lust for Life', 'DURATION':331, 'FILESIZE':4.4,'RATING':5},
                {'NAME':'Heroin', 'ARTIST':'Lana Del Rey', 'ALBUM':'Lust for Life', 'DURATION':355, 'FILESIZE':5.1,'RATING':4},
                {'NAME':'Change', 'ARTIST':'Lana Del Rey', 'ALBUM':'Lust for Life', 'DURATION':320, 'FILESIZE':4.3,'RATING':3},
                {'NAME':'Numb', 'ARTIST':'Linkin Park', 'ALBUM':'Meteora', 'DURATION':187, 'FILESIZE':2.2,'RATING':4},
                {'NAME':'Somewhere I Belong', 'ARTIST':'Linkin Park', 'ALBUM':'Meteora', 'DURATION':214, 'FILESIZE':2.4,'RATING':5},
                {'NAME':'Easier to Run', 'ARTIST':'Linkin Park', 'ALBUM':'Meteora', 'DURATION':205, 'FILESIZE':2.3,'RATING':4},
                {'NAME':'Figure 09', 'ARTIST':'Linkin Park', 'ALBUM':'Meteora', 'DURATION':198, 'FILESIZE':2.1,'RATING':3},
                {'NAME':'Breaking the Habit', 'ARTIST':'Linkin Park', 'ALBUM':'Meteora', 'DURATION':197, 'FILESIZE':2.1,'RATING':4},
                {'NAME':'Radioactive', 'ARTIST':'Imagine Dragons', 'ALBUM':'Night Visions', 'DURATION':188, 'FILESIZE':1.9,'RATING':4},
                {'NAME':'Demons', 'ARTIST':'Imagine Dragons', 'ALBUM':'Night Visions', 'DURATION':176, 'FILESIZE':1.7,'RATING':4},
                {'NAME':'On Top of the World', 'ARTIST':'Imagine Dragons', 'ALBUM':'Night Visions', 'DURATION':191, 'FILESIZE':1.9,'RATING':5},
                {'NAME':'Underdog', 'ARTIST':'Imagine Dragons', 'ALBUM':'Night Visions', 'DURATION':210, 'FILESIZE':2.3,'RATING':2},
                {'NAME':'My Fault', 'ARTIST':'Imagine Dragons', 'ALBUM':'Night Visions', 'DURATION':177, 'FILESIZE':1.5,'RATING':2},
                {'NAME':'Knights of Shame', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':186, 'FILESIZE':7,'RATING':5},
                {'NAME':'Jump On My Shoulders', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':248, 'FILESIZE':4.1,'RATING':4},
                {'NAME':'Burn it Down', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':191, 'FILESIZE':1.9,'RATING':5},
                {'NAME':'Guilty Filthy Soul', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':214, 'FILESIZE':2.4,'RATING':3},
                {'NAME':'Sail', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':259, 'FILESIZE':2.7,'RATING':2},
                {'NAME':'Wake Up', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':183, 'FILESIZE':1.4,'RATING':4},
                {'NAME':'Not Your Fault', 'ARTIST':'AWOLNATION', 'ALBUM':'Megalithic Symphony', 'DURATION':242, 'FILESIZE':2.8,'RATING':4},
                {'NAME':'Drive By', 'ARTIST':'Train', 'ALBUM':'California 37', 'DURATION':196, 'FILESIZE':2.3,'RATING':3},
                {'NAME':'50 Ways to Say Goodbye', 'ARTIST':'Train', 'ALBUM':'California 37', 'DURATION':248, 'FILESIZE':2.7,'RATING':5},
                {'NAME':'California 37', 'ARTIST':'Train', 'ALBUM':'California 37', 'DURATION':191, 'FILESIZE':1.9,'RATING':5},
                {'NAME':'Hello Goodbye', 'ARTIST':'The Beatles', 'ALBUM':'1', 'DURATION':209, 'FILESIZE':3.1, 'RATING':4},
                {'NAME':'Let it Be', 'ARTIST':'The Beatles', 'ALBUM':'1', 'DURATION':233, 'FILESIZE':4.2, 'RATING':4},
                {'NAME':'Soul with a capital s', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':304, 'FILESIZE':5.1, 'RATING':5},
                {'NAME':'Soul Vaccination', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':297, 'FILESIZE':4.6, 'RATING':5},
                {'NAME':'Down to the Night club', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':195, 'FILESIZE':2.0, 'RATING':4},
                {'NAME':'What is Hip?', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':361, 'FILESIZE':6.2, 'RATING':5},
                {'NAME':'Your Still a Young Man', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':360, 'FILESIZE':6.1, 'RATING':3},
                {'NAME':'You Got To Funkifize', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':280, 'FILESIZE':3.5, 'RATING':3},
                {'NAME':'Diggin on James Brown', 'ARTIST':'Tower of Power', 'ALBUM':'Soul Vaccination: Live', 'DURATION':262, 'FILESIZE':4.7, 'RATING':4},
                {'NAME':'The Grand Illusion', 'ARTIST':'Styx', 'ALBUM':'The Grand Illusion', 'DURATION':277, 'FILESIZE':4.1, 'RATING':3},
                {'NAME':'Superstars', 'ARTIST':'Styx', 'ALBUM':'The Grand Illusion', 'DURATION':235, 'FILESIZE':3.1, 'RATING':2},
                {'NAME':'Come Sail Away', 'ARTIST':'Styx', 'ALBUM':'The Grand Illusion', 'DURATION':367, 'FILESIZE':5.5, 'RATING':5},
                {'NAME':'Man in the Wilderness', 'ARTIST':'Styx', 'ALBUM':'The Grand Illusion', 'DURATION':351, 'FILESIZE':4.5, 'RATING':4},
                {'NAME':'I''M OK', 'ARTIST':'Styx', 'ALBUM':'Pieces of Eight', 'DURATION':342, 'FILESIZE':4.4, 'RATING':2},
                {'NAME':'Blue Collar Man', 'ARTIST':'Styx', 'ALBUM':'Pieces of Eight', 'DURATION':248, 'FILESIZE':4.4, 'RATING':4},
                {'NAME':'Queen of Spades', 'ARTIST':'Styx', 'ALBUM':'Pieces of Eight', 'DURATION':341, 'FILESIZE':5.0, 'RATING':3},
                {'NAME':'Renegade', 'ARTIST':'Styx', 'ALBUM':'Pieces of Eight', 'DURATION':257, 'FILESIZE': 3.9, 'RATING':5},
                {'NAME':'Shake it off', 'ARTIST':'Taylor Swift', 'ALBUM':'1989', 'DURATION':219, 'FILESIZE': 2.1, 'RATING':3},
                {'NAME':'Wildest Dreams', 'ARTIST':'Taylor Swift', 'ALBUM':'1989', 'DURATION':220, 'FILESIZE': 2.8, 'RATING':3},
                {'NAME':'Tom Sawyer', 'ARTIST':'Rush', 'ALBUM':'Moving Pictures', 'DURATION':274, 'FILESIZE': 3.2, 'RATING':5},
                {'NAME':'Red Barchetta', 'ARTIST':'Rush', 'ALBUM':'Moving Pictures', 'DURATION':370, 'FILESIZE': 6.3, 'RATING':1},
                {'NAME':'YYZ', 'ARTIST':'Rush', 'ALBUM':'Moving Pictures', 'DURATION':266, 'FILESIZE': 4.6, 'RATING':4},
                {'NAME':'Night Moves', 'ARTIST':'Bob Seger', 'ALBUM':'Greatest Hits', 'DURATION':326, 'FILESIZE': 5.0, 'RATING':4},
                {'NAME':'Beautiful Loser', 'ARTIST':'Bob Seger', 'ALBUM':'Greatest Hits', 'DURATION':187, 'FILESIZE': 2.3, 'RATING':1},
            ]
    
    # Print Question Answer 106 Points Total
    print('Source Code - Division B/C - Music Library')
    
    print('QUESTION 0 OBJECTIVE A (2): '+str(getMusicLibraryTitle()))
    print('QUESTION 1 OBJECTIVE A (2): '+str(getCDArea(5)))
    print('QUESTION 2 OBJECTIVE A (2): '+str(hasEnoughSpace(1024,1024)))
    print('QUESTION 3 OBJECTIVE A (3): '+str(logSong('Love Me Do','The Beatles','1')))
    print('QUESTION 4 OBJECTIVE A (3): '+str(formatTime(205)))
    print('QUESTION 4 OBJECTIVE B (3): '+str(formatTime(205)))
    print('QUESTION 5 OBJECTIVE A (3): '+str(reverseString('Man in the Wilderness')))
    print('QUESTION 6 OBJECTIVE A (4): '+str(getSong(library, 'Soul Vaccination')))
    
    print('QUESTION 7 OBJECTIVE A (4): '+str(getTotalTime(library)))
    
    print('QUESTION 8 OBJECTIVE A (5): '+str(getAverageSize(library, 'RATING')) +' '+ str(getAverageSize(library, 'FILESIZE')))
    print('QUESTION 8 OBJECTIVE B (2): '+str(getAverageSize(library, 'RATINGSS')))
    
    print('QUESTION 9 OBJECTIVE A (5): '+str(getNumberOfMixTapes(library)))
    
    print('QUESTION 10 OBJECTIVE A (5): '+str(getTheBestSong(library)))
    print('QUESTION 10 OBJECTIVE A (2): '+str(getTheBestSong(library)))
    
    print('QUESTION 11 OBJECTIVE A (5): '+str(getSpacesCount(library)))
    print('QUESTION 12 OBJECTIVE A (5): '+str(truncateSongTitle('down to the night Club')))
    print('QUESTION 13 OBJECTIVE A (5): '+str(capitalizeSongTitle('down to the night Club')))
    print('QUESTION 14 OBJECTIVE A (6): '+str(getAlbumMostSongs(library)))
    
    print('QUESTION 15 OBJECTIVE A (6): '+str(getShortestMixTape(library)))
    print('QUESTION 15 OBJECTIVE B (2): '+str(getShortestMixTape(library)))
       
    print('QUESTION 16 OBJECTIVE A (7): '+str(getMedianDuration(library)))
    print('QUESTION 17 OBJECTIVE A (7): '+str(fibonnaciSum(library)))   
    print('QUESTION 18 OBJECTIVE A (8): '+str(getAnagrams(library, 'I hang under lo list')))
    
    print('QUESTION 19 OBJECTIVE A (4): '+str(getStatistic(library)))
    print('QUESTION 19 OBJECTIVE B (2): '+'Check for comment explaining function.')
    print('QUESTION 19 OBJECTIVE C (2): '+'Check if previous function in file was called.')
    print('QUESTION 19 OBJECTIVE D (2): '+'Check if import statement was used.')
    
main()