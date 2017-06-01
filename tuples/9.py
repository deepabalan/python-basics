# split email address into username and a domain.

addr = 'monty@python.org'

uname, domain = addr.split('@')

print 'uname = %s, domain = %s' % (uname, domain)
