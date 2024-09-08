import copy
#copy
ishikawa = ['suzu', 'wajima', 'anamizu', 'nanao', 'hakui', 'kahoku', 'tsubata', 'kanazawa', 'matto', 'mikawa', 'komatsu', 'kaga', 'hakusan']
kanagawa = ['yokohama', 'kawasaki', 'atsugi', 'ebina', 'hiraduka']
copy_kanagawa = kanagawa.copy()
print(copy_kanagawa)
kanagawa.extend(ishikawa)
print(kanagawa)


niigata = [['niigata', 'niitsu'], ['nagaoka', 'tubame'], ['kashiwazaki']]
print(niigata)
copy_nigata = copy.deepcopy(niigata)

copy_nigata[0][0] = 'shibata'
print(copy_nigata)