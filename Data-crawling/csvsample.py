import csv

f = open('/Users/choeseunghui/Downloads/melon_csv.csv', 'a', encoding='utf-8', newline='')
wr = csv.writer(f)
print(wr)



# wr.writerow()
wr.writerows([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

# f.close()

f = open('sample.csv', 'r',encoding='utf-8')
rd = csv.reader(f)
# print(rd)
for i in rd:
    print(i)

