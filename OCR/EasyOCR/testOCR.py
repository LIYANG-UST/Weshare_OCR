# A test for easyocr

import easyocr
import json

reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
# need to run only once to load model into memory

output_dict = {}
output_list = []

for i in range(1, 10):
    name = '../img/' + str(i) + '.jpg'  # your own path
    result = reader.readtext(name, detail=0)
    print('test' + str(i) + ': \n')
    print(result)
    output_list.append(result)
    output_dict[str(i)] = output_list[i-1]
    print(output_dict)
    print('\n')

with open('output.json', 'w') as f:
    json.dump(output_dict, f, indent = 1, ensure_ascii=False)
   