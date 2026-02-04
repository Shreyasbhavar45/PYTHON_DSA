import time
import sys

def print_lyrics():
    lyrics = [
        'Haathon ko sambhaale mere haathon mein',
        'Kaise haathon ko sambhaale mere haathon mein',
        'Jab tak neend na aaye inn lakeeron mein',
        'Baatein ho.......',
        'hayyee'

    ]

    delays = [1.0,0.1,1.12,0.9,0.8]

    print('arz kya hai?.......:\n')
    time.sleep(1.4)

    for i,line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i])

print_lyrics()