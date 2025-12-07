import xml.etree.ElementTree as ET


tree = ET.parse('data/000005.xml')
all_objects = tree.getroot().findall('object')

print(f"All objects tag: {all_objects[0].find('name').text}")
print(f"All objects tag: {all_objects[0].find('difficult').text}")
print(f"All objects tag: {all_objects[0].find('bndbox').find('xmin').text}")
print(f"All objects tag: {all_objects[0].find('bndbox').find('ymin').text}")
print(f"All objects tag: {all_objects[0].find('bndbox').find('xmax').text}")
print(f"All objects tag: {all_objects[0].find('bndbox').find('ymax').text}")