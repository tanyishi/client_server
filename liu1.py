from xml.etree import ElementTree as ET 
tree = ET.parse('data-text.xml') 
root = tree.getroot() 
data = root.find('Data')
all_data=[]
for observation in data: 
    record={}
    for item in observation: 
        lookup_key=item.attrib.keys()[0]
        rec_key=item.attrib[lookup_key]
        print rec_key