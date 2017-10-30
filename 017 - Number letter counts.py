# -*- coding: utf-8 -*-
"""
Solved: 10-30-2017, 16:31

Question:
If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?

Thoughts on my answer:
I knew that there are ways to just find a pattern and count, but I also wanted to
make it flexible if, say, n = 935. This only works < 1001 however.
"""
import time

def lettercount(n):
    letters =   {
                1: 3, #one
                2: 3, #two
                3: 5, #three
                4: 4, #four
                5: 4, #five
                6: 3, #six
                7: 5, #seven
                8: 5, #eight
                9: 4, #nine
                10: 3, #ten
                11: 6, #eleven
                12: 6, #twelve
                13: 8, #thirteen
                14: 8, #fourteen
                15: 7, #fifteen
                16: 7, #sixteen
                17: 9, #seventeen
                18: 8, #eighteen
                19: 8, #nineteen
                20: 6, #twenty
                30: 6, #thirty
                40: 5, #forty
                50: 5, #fifty
                60: 5, #sixty
                70: 7, #seventy
                80: 6, #eighty
                90: 6, #ninety
                100: 7, #hundred
                1000: 8, #thousand
                }
    and_count = 3
    answer = 0
    for i in range(1,n + 1):
        h, t, teens = False, False, False
        if (i in letters):
            answer += letters[i]
            if (i == 100 or i == 1000):
                answer += letters[1]
        else:
            hundred = i % 1000 #914, 101
            ten = hundred % 100 #14, 1
            one = ten % 10 #4, 1
            
            hundredth = (hundred - ten)/100 #9, 1
            tenth = ten - one #10, 0
            oneth = one #4, 1
            
            if hundredth != 0:
                answer += letters[hundredth]
                answer += letters[100]
                h = True
                
            if tenth != 0:
                if tenth == 10:
                    answer += letters[ten]
                    teens = True
                else:
                    answer += letters[tenth]
                if h:
                    answer += and_count
                t = True
            
            if oneth != 0 and not teens:
                answer += letters[oneth]
                if not t:
                    answer += and_count
    return answer
            
start = time.clock()
print(lettercount(1000))
end = time.clock()
total_time = end - start

print("Time taken: " + str(total_time))