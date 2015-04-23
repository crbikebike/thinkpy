__author__ = 'ChrisKristen'

import thinkPyCh7
import string

thinkPyCh7.forwardsLetters('dogs')

thinkPyCh7.backwardsLetters('cats')

thinkPyCh7.duckNames('JKLMNOPQ','ack')

print('should be 1')
exampleOne = thinkPyCh7.eurekaLoop('banana','a',0)
print exampleOne

print('should be 3')
exampleTwo = thinkPyCh7.eurekaLoop('banana','a',2)
print exampleTwo

print('should be 2')
traveler = thinkPyCh7.traverseCountLetters('apple','p')
print traveler

print('should be 2(crfind)')
location =  thinkPyCh7.findCountLetters('apple','p',0)
print location

print('should be 1(crfind)')
vacation = thinkPyCh7.findCountLetters('apple','p',2)
print vacation

print string.uppercase