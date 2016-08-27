import pandas as pd

#Read files according to directory
fao = pd.read_csv('~/Desktop/Code/FAO.csv')
sys = pd.read_csv('~/Desktop/Code/SYS.csv')

#merge left onto one file
merged = pd.merge(sys, fao, on=['First Name', 'Last Name'], how='left')
sys_notfao = (merged[merged["Rank"].isnull()])
print (sys_notfao)

#write to file
sys_notfao.to_excel("HSC-NMH Sys Not FAO.xlsx")

#second merge
merged = pd.merge(fao, sys, on=['First Name', 'Last Name'], how='left')
fao_notsys = (merged[merged["DB ID"].isnull()])
print (fao_notsys)

#write to file
fao_notsys.to_excel("HSC-NMH FAO not SYS.xlsx")