from sys import argv

script, username = argv
prompt = '>'

print 'hi %s how r u? and this is my %s script' %(username, script)
print '%s had ur lunch?'%username
l1 = raw_input(prompt)
print '%s r u going to ur native this week' %username
l2 = raw_input(prompt)

print '''

So you said %r for ur lunch
   and you said %r for native
'''% (l1, l2)
