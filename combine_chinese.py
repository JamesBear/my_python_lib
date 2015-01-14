#!/usr/bin/python
import re
import sys

def get_file_content(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return content

def write_to_file(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()

pattern = '^([A-bZ_]+)\s*=\s*([^\s].*)'
flags = re.MULTILINE
r = re.compile(pattern, flags)

def replace_with_translation(source_str, translation_dict):
    out_str = ''
    replaced_count = 0
    dup_test = set()
    dup_list = []
    untranslated = ''
    for line in source_str.splitlines():
        result = r.match(line)
        if result == None:
            out_str += line + '\n'
        else:
            k = result.group(1)
            v = translation_dict.get(k)
            if k in dup_test:
                #print(line)
                dup_list.append(line)
            else:
                dup_test.add(k)
            if v == None:
                out_str += line + '\n'
                untranslated += line + '\n'
            else:
                replaced_count += 1
                out_str += k + '=' + v + '\n'
    if len(dup_list) > 0:
        print("duplicated lines:")
        for l in dup_list:
            print(l)
    return out_str, replaced_count, untranslated

#pattern = sys.argv[1]
china_path = sys.argv[1]
south_asia_path = sys.argv[2]


china_str = get_file_content(china_path)
south_asia_str = get_file_content(south_asia_path)

china_dict = {}
south_asia_dict = {}
for i in r.finditer(china_str):
    #print(i.group(1), i.group(2))
    k, v = i.group(1), i.group(2)
    china_dict[k] = v

for i in r.finditer(south_asia_str):
    #print(i.group(1), i.group(2))
    k, v = i.group(1), i.group(2)
    south_asia_dict[k] = v

replaced = []
unique = []
for k, v in china_dict.items():
    v2 = south_asia_dict.get(k)
    if v2 != None:
        replaced.append(k)
    else:
        unique.append(k)

print(len(china_dict), len(south_asia_dict))
print(len(replaced), len(unique))
out_str, replaced_count, untranslated = replace_with_translation(china_str, south_asia_dict)
print(replaced_count)
write_to_file('after_merging_translation.txt', out_str)
write_to_file('untranslated.txt', untranslated)
