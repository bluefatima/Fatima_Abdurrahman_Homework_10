
import argparse
import urllib
import urllib.request
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Sample Application')
parser.add_argument('required_arg_1', help='This positional argument is required')

results = parser.parse_args()
incoming = results.required_arg_1

words = incoming
bits = (words.split(' '))
query = ('+'.join(bits))

url = "http://api.wolframalpha.com/v2/query?input="+query+"&appid=APLTT9-9WG78GYE65"

xml_data=urllib.request.urlopen(url).read()
root = ET.fromstring(xml_data)

    output = []
    
    for pt in root.findall('.//plaintext'):
        if pt.text:
            output.append(pt.text)
    if "=" in output[0]: #sometimes result has original query, this gets rid of that
        answer = output[0].split("=")[-1]
        print(answer)
    elif len(output[1].split(" "))>2:
        answer = output[1].split(" ")[0]
        if answer.find("×10^") != -1: #changes scientific notation so python can read it (x10^ -> e)
            parts = answer.split("×10^")
            return(float(parts[0]+"e"+parts[1]))
    if output[1].find("...") != -1: #deals with answers trailing with a '...' (like sqrts, pi)
        shorter = output[1].split("...")
        return(float(shorter[0]))
    else: 
        print("hey")
        return(float((output[1])))