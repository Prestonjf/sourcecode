from com.prestonsproductions.sourcecode.MusicLibrary2018 import MusicLibrary2018A as ML
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
    print('Source Code (MAIN) - Division B/C - Music Library')
    
    print('QUESTION 0 OBJECTIVE A (2): '+str(ML.getMusicLibraryTitle())) # School Name
    print('QUESTION 1 OBJECTIVE A (2): '+str(ML.getCDArea(5))) # 78.53981633974483
    print('QUESTION 2 OBJECTIVE A (2): '+str(ML.hasEnoughSpace(1024,1024))) # True
    print('QUESTION 3 OBJECTIVE A (3): '+str(ML.logSong('Love Me Do','The Beatles','1'))) # Love Me Do : The Beatles : 1
    print('QUESTION 4 OBJECTIVE A (3): '+str(ML.formatTime(205))) # 3:25 or 3.4166666666666665
    print('QUESTION 4 OBJECTIVE B (3): '+str(ML.formatTime(205))) # 3:25
    print('QUESTION 5 OBJECTIVE A (3): '+str(ML.reverseString('Man in the Wilderness'))) # ssenredliW eht ni naM
    print('QUESTION 6 OBJECTIVE A (4): '+str(ML.getSong(library, 'Soul Vaccination'))) # {'NAME': 'Soul Vaccination', 'DURATION': 297, 'ARTIST': 'Tower of Power', 'FILESIZE': 4.6, 'ALBUM': 'Soul Vaccination: Live', 'RATING': 5}
  
    print('QUESTION 7 OBJECTIVE A (4): '+str(ML.getTotalTime(library))) # 226:14 or 226.23333333333332
    
    print('QUESTION 8 OBJECTIVE A (5): '+str(ML.getAverageSize(library, 'RATING')) +' '+ str(ML.getAverageSize(library, 'FILESIZE'))) # 3.685185185185185 3.511111111111111
    print('QUESTION 8 OBJECTIVE B (2): '+str(ML.getAverageSize(library, 'RATINGSS'))) # -1
    
    print('QUESTION 9 OBJECTIVE A (5): '+str(ML.getNumberOfMixTapes(library))) # 3
    
    print('QUESTION 10 OBJECTIVE A (5): '+str(ML.getTheBestSong(library))) # ['On Top of the World 100.52631578947368', 'California 37 100.52631578947368'] or ['On Top of the World', 'California 37']
    print('QUESTION 10 OBJECTIVE B (2): '+str(ML.getTheBestSong(library))) # ['On Top of the World 100.52631578947368', 'California 37 100.52631578947368']
    
    print('QUESTION 11 OBJECTIVE A (5): '+str(ML.getSpacesCount(library))) # 37
    print('QUESTION 12 OBJECTIVE A (5): '+str(ML.truncateSongTitle('down to the night Club'))) # down to the night Cl...
    print('QUESTION 13 OBJECTIVE A (5): '+str(ML.capitalizeSongTitle('down to the night Club'))) # Down To The Night Club
    print('QUESTION 14 OBJECTIVE A (6): '+str(ML.getAlbumMostSongs(library))) # Megalithic Symphony, Soul Vaccination: Live
    
    print('QUESTION 15 OBJECTIVE A (6): '+str(ML.getShortestMixTape(library))) # [10, 'Cant Buy Me Love', 'Love Me Do', 'Eight Days A Week', 'Demons', 'My Fault', 'Wake Up', 'Knights of Shame', 'Numb', 'Beautiful Loser', 'Radioactive'] or ['Cant Buy Me Love', 'Love Me Do', 'Eight Days A Week', 'Demons', 'My Fault', 'Wake Up', 'Knights of Shame', 'Numb', 'Beautiful Loser', 'Radioactive']
    print('QUESTION 15 OBJECTIVE B (2): '+str(ML.getShortestMixTape(library))) # [10, 'Cant Buy Me Love', 'Love Me Do', 'Eight Days A Week', 'Demons', 'My Fault', 'Wake Up', 'Knights of Shame', 'Numb', 'Beautiful Loser', 'Radioactive']
    
    print('QUESTION 16 OBJECTIVE A (7): '+str(ML.getMedianDuration(library))) # 245.0
    print('QUESTION 17 OBJECTIVE A (7): '+str(ML.fibonnaciSum(library))) # 377   
    print('QUESTION 18 OBJECTIVE A (8): '+str(ML.getAnagrams(library, 'I hang under lo list'))) # ['The Grand Illusion']
    
    print('QUESTION 19 OBJECTIVE A (4): '+str(ML.getStatistic(library)))
    print('QUESTION 19 OBJECTIVE B (2): '+'Check for comment explaining function.')
    print('QUESTION 19 OBJECTIVE C (2): '+'Check if previous function in file was called.')
    print('QUESTION 19 OBJECTIVE D (2): '+'Check if import statement was used.')
    
main()