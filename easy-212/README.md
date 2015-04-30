#[[2015-04-27] Challenge #212 [Easy] Rövarspråket](http://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/)

>When we Swedes are young, we are taught a SUPER-SECRET language that only kids know, so we can hide secrets from our confused parents. This language is known as "Rövarspråket" (which means "Robber's language", more or less), and is surprisingly easy to become fluent in, at least when you're a kid. Recently, the cheeky residents of /r/Sweden decided to play a trick on the rest on reddit, and get a thread entirely in Rövarspråket to /r/all. The results were hilarious.
>Rövarspråket is not very complicated: you take an ordinary word and replace the consonants with the consonant doubled and with an "o" in between. So the consonant "b" is replaced by "bob", "r" is replaced with "ror", "s" is replaced with "sos", and so on. Vowels are left intact. It's made for Swedish, but it works just as well in English.
>Your task today is to write a program that can encode a string of text into Rövarspråket.
>(note: this is a higly guarded Swedish state secret, so I trust that none of you will share this very privileged information with anyone! If you do, you will be extradited to Sweden and be forced to eat surströmming as penance.)
>(note 2: surströmming is actually not that bad, it's much tastier than its reputation would suggest! I'd go so far as to say that it's the tastiest half-rotten fish in the world!)

A fun little challenge. The decoder in Python is a little iffy, but it's 
probably better to handle that iteratively rather than recursively.
