import re

pattern = r"[a-z]+ave"

text='''The wave crashed and hit the sandcastle head-on.
    The sandcastle began to melt under the waves force and as the wave receded, 
    half the sandcastle was gone. The next wave zave hit, not quite as strong, but still
    managed to cover the remains of the sandcastle rave and take more of it away. 
    The third wave, a big one, crashed over the sandcastle completely covering and engulfing it.
    When it receded, there was no trace the sandcastle ever existed and hours of hard work disappeared forever.'''

match=re.findall(pattern,text)
print(match)