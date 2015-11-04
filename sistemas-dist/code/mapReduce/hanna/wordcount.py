#/usr/bin/env python

import string, sys

for line in sys.stdin:
    ## removes the whitespace
    line = line.strip()

    ## removes punctuation
    line = line.translate( string.maketrans(string.punctuation, ' ' * len(string.punctuation)) )

    ## makes sure that the text is a valid Unicode string
    ## ignores the characters that are not valid
    line = unicode(line, errors='ignore')

    ## converts the text to lowercase 
    line = line.lower()

    ## this splits words at all whitespace
    words = line.split(None)

    ## prints out all the words with a count of 1
    for w in words:
        print "\t".join([w, "1"])
