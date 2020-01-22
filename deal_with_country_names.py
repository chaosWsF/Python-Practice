# deal with industry
# indNames = []
# with open('./ind_name.txt') as fr:
#     for row in fr:
#         indNames.append(row)

# with open('./ind_name_modified.txt','w') as fw:
#     for name in indNames:
#         fw.write(name)
#         fw.write('\n\n')

countryNames = []
with open('./country_name.txt') as fr:
    for row in fr:
        countryNames.append(row)

brNames = []
with open('./belt_and_road_names.txt') as fr:
    for row in fr:
        brNames.append(row)

idList = []
for i in range(len(countryNames)):
    name = countryNames[i]
    if name in brNames:
        idList.append(i+1)

print(idList)