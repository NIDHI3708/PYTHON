s = set()
s.add(20)
s.add(20.0)
s.add('20')
print((s),len(s)) # Output will show only one '20' since 20 and 20.0 are considered equal in a set