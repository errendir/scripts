import re
import sys

print("header1,header2,header3")
for line in sys.stdin:
    regex = "(\S*)\s*\[(.*)\]\s*(\S*)"
    match_result = re.match(regex, line)
    if match_result:
        value1 = match_result.group(1)
        value2 = match_result.group(2)
        value3 = match_result.group(3)
        print(value1, value2, value3, sep=",")
    # change this to a different regex
    regex = "(\S*)\s*\[(.*)\]\s*(\S*)"
    match_result = re.match(regex, line)
    if match_result:
        value1 = match_result.group(1)
        value2 = match_result.group(2)
        value3 = match_result.group(3)
        print(value1, value2, value3, sep=",")
