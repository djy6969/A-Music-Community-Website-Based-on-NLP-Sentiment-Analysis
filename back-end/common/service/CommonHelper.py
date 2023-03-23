import re

'''
the format of music time in database is minute:second
the front-end need pure second time, format second.00
'''
def convertMusicTime(time):
    time = re.split(":", time)
    second = int(time[0]) * 60 + int(time[1])
    return str(second) + ".00"