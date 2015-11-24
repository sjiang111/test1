from os.path import abspath, expanduser
import re
import operator

'''
__author__ = 'sjiang'
MUST PUT access_log file in your /Downloads/ directory
Test it in Mac OSX
5-26
'''


access_entries = {}
entry_list =[]
ip_list =[]
timestamp_list = []
url_list = []
result_code_list = []
doc_size_list = []

#pattern = '(.*?) - - \[(.*?)\] "(.*?)" ([(\d)]+) ([(\d)]+)'
pattern = '(.*?) - - \[(.*?)\] "(.*?)" ([(\d)]+) ([(\d)]+|-)'

filepath = abspath(expanduser("~/") + '/Downloads/access_log')

print 'Opening file: ', filepath
with open(filepath, 'r') as fh:
    for line in fh:
        line = line.strip()
        access_entries = re.match(pattern, line).groups()
        entry_list.append(access_entries)
        ip_list.append(access_entries[0].__str__())
        #timestamp_list.append(access_entries[1].__str__())
        #url_list.append(access_entries[2].__str__())
        result_code_list.append(access_entries[3].__str__())
        #doc_size_list.append(access_entries[4].__str__())
        #print access_entries
        #print entry_list
##debug 
print ('\n***********access entries************')
print access_entries   
print ('\n***********entry_list************')    
print entry_list
print ('\n***********ip_list************')    
print ip_list
print ('\n***********result code list************') 
print result_code_list
##debug


# a function to replace value in dictionary
def replace_value_in_dict(current_dict, key_to_find, new_value):
    for key in current_dict.keys():
        if key == key_to_find:
            current_dict[key] = new_value


#calculate stats for IP address. Put them in ip_stats_dict #
ip_stats_dict = {}
for i in ip_list:
    if(ip_stats_dict.has_key(i)):
      replace_value_in_dict(ip_stats_dict,i,ip_stats_dict[i]+1)
    else:
      ip_stats_dict[i] = 1

#sort ip_stats_dict by value in desc order

sorted_ip_stats = sorted(ip_stats_dict.items(), key=operator.itemgetter(1), reverse=True)
print "*1. Sources (most frequent to least)"
print "(ip address,  occurrence)"
print "-------------------------"
for i in sorted_ip_stats:
    print i

print "------------------------------------------------------------------"

#calculate result codes#
result_code_stats_dict = {}
for j in result_code_list:
    #print j
    if(result_code_stats_dict.has_key(j)):
        replace_value_in_dict(result_code_stats_dict,j,result_code_stats_dict[j]+1)
    else:
        result_code_stats_dict[j] = 1

#sort result code stats
sorted_result_code_stats = sorted(result_code_stats_dict.items(), key=operator.itemgetter(1), reverse=True)
print "*2. Result Codes (most frequent to least)"
print "(Result Code,  occurrence)"
print "---------------------------"
for j in sorted_result_code_stats:
    print j

print "------------------------------------------------------------------"
























