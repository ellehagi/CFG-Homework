import re, sys

with open('song.txt', 'w') as song_file:
    song_file.write("""You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use
 
And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away
 
Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind
 
I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)
 
""")
f = open('song.txt', 'r')
lines = f.read()
match = re.findall('[still]+', lines)
print match