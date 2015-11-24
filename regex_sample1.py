import re

##print (re.split(r'(\s*)','this is a test string for regular expression'))


#multiple range used in spliter delimiter.
##print (re.split(r'([a-fA-F0-9])','this is a test string for regular expression', re.I))

pattern = re.compile(r'(\d{1,5}\s+\w+\s+\w+\.)', re.I|re.M)


#pattern2 = re.compile(r'(\d{1,5}\s\w+\s\w+\.)')

##re.I  ignoreCase
# ?: non-captive splitter
#print (re.split(r'(?:\s)','this is a test string for regular expression')) 

# vs captive splitter
print (re.split(r'(\s)','this is a test string for regular expression')) 


print ('\n')
##findall
print (re.findall(pattern ,'this is a test string to find address: 2180   main   st. for regular expression')) 


