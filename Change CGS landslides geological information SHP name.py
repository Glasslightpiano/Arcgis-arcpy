import os

#修改路徑
path = 'D:\\ArcMap test\\SA\\'
os.chdir(path)

#更新SHP主要檔案名稱
main_old_name = '山崩與地滑地質敏感區_'
main_new_name = 'SensitiveArea_'

#更新SHP縣市
county_old_name1 = '宜蘭'
county_new_name1 = 'Ilan'

county_old_name2 = '花蓮'
county_new_name2 = 'Hualien'

county_old_name3 = '南投'
county_new_name3 = 'Nantou'

county_old_name4 = '屏東'
county_new_name4 = 'Pingtung'

county_old_name5 = '苗栗'
county_new_name5 = 'Miaoli'

county_old_name6 = '桃園'
county_new_name6 = 'Taoyuan'

county_old_name7 = '高雄'
county_new_name7 = 'Kaohsiung'

county_old_name8 = '基隆'
county_new_name8 = 'Keelung'

county_old_name9 = '雲林'
county_new_name9 = 'Yunlin'

county_old_name10 = '新北'
county_new_name10 = 'NewTaipei'

county_old_name11 = '新竹'
county_new_name11 = 'Hsinchu'

county_old_name12 = '嘉義'
county_new_name12 = 'Chiayi'

county_old_name13 = '彰化'
county_new_name13 = 'Changhua'

county_old_name14 = '臺中'
county_new_name14 = 'Taichung'

county_old_name15 = '臺北'
county_new_name15 = 'Taipei'

county_old_name16 = '臺東'
county_new_name16 = 'Taitung'

county_old_name17 = '臺南'
county_new_name17 = 'Tainan'

#副檔名
file1 = '.dbf'
file2 = '.prj'
file3 = '.shp'
file4 = '.shp.xml'
file5 = '.shx'

#更改資料夾名稱
#宜蘭
os.rename(main_old_name + county_old_name1 + file1, main_new_name + county_new_name1 + file1)
os.rename(main_old_name + county_old_name1 + file2, main_new_name + county_new_name1 + file2)
os.rename(main_old_name + county_old_name1 + file3, main_new_name + county_new_name1 + file3)
os.rename(main_old_name + county_old_name1 + file4, main_new_name + county_new_name1 + file4)
os.rename(main_old_name + county_old_name1 + file5, main_new_name + county_new_name1 + file5)

#花蓮
os.rename(main_old_name + county_old_name2 + file1, main_new_name + county_new_name2 + file1)
os.rename(main_old_name + county_old_name2 + file2, main_new_name + county_new_name2 + file2)
os.rename(main_old_name + county_old_name2 + file3, main_new_name + county_new_name2 + file3)
os.rename(main_old_name + county_old_name2 + file4, main_new_name + county_new_name2 + file4)
os.rename(main_old_name + county_old_name2 + file5, main_new_name + county_new_name2 + file5)

#南投
os.rename(main_old_name + county_old_name3 + file1, main_new_name + county_new_name3 + file1)
os.rename(main_old_name + county_old_name3 + file2, main_new_name + county_new_name3 + file2)
os.rename(main_old_name + county_old_name3 + file3, main_new_name + county_new_name3 + file3)
os.rename(main_old_name + county_old_name3 + file4, main_new_name + county_new_name3 + file4)
os.rename(main_old_name + county_old_name3 + file5, main_new_name + county_new_name3 + file5)

#屏東
os.rename(main_old_name + county_old_name4 + file1, main_new_name + county_new_name4 + file1)
os.rename(main_old_name + county_old_name4 + file2, main_new_name + county_new_name4 + file2)
os.rename(main_old_name + county_old_name4 + file3, main_new_name + county_new_name4 + file3)
os.rename(main_old_name + county_old_name4 + file4, main_new_name + county_new_name4 + file4)
os.rename(main_old_name + county_old_name4 + file5, main_new_name + county_new_name4 + file5)

#苗栗
os.rename(main_old_name + county_old_name5 + file1, main_new_name + county_new_name5 + file1)
os.rename(main_old_name + county_old_name5 + file2, main_new_name + county_new_name5 + file2)
os.rename(main_old_name + county_old_name5 + file3, main_new_name + county_new_name5 + file3)
os.rename(main_old_name + county_old_name5 + file4, main_new_name + county_new_name5 + file4)
os.rename(main_old_name + county_old_name5 + file5, main_new_name + county_new_name5 + file5)

#桃園
os.rename(main_old_name + county_old_name6 + file1, main_new_name + county_new_name6 + file1)
os.rename(main_old_name + county_old_name6 + file2, main_new_name + county_new_name6 + file2)
os.rename(main_old_name + county_old_name6 + file3, main_new_name + county_new_name6 + file3)
os.rename(main_old_name + county_old_name6 + file4, main_new_name + county_new_name6 + file4)
os.rename(main_old_name + county_old_name6 + file5, main_new_name + county_new_name6 + file5)

#高雄
os.rename(main_old_name + county_old_name7 + file1, main_new_name + county_new_name7 + file1)
os.rename(main_old_name + county_old_name7 + file2, main_new_name + county_new_name7 + file2)
os.rename(main_old_name + county_old_name7 + file3, main_new_name + county_new_name7 + file3)
os.rename(main_old_name + county_old_name7 + file4, main_new_name + county_new_name7 + file4)
os.rename(main_old_name + county_old_name7 + file5, main_new_name + county_new_name7 + file5)

#基隆
os.rename(main_old_name + county_old_name8 + file1, main_new_name + county_new_name8 + file1)
os.rename(main_old_name + county_old_name8 + file2, main_new_name + county_new_name8 + file2)
os.rename(main_old_name + county_old_name8 + file3, main_new_name + county_new_name8 + file3)
os.rename(main_old_name + county_old_name8 + file4, main_new_name + county_new_name8 + file4)
os.rename(main_old_name + county_old_name8 + file5, main_new_name + county_new_name8 + file5)

#雲林
os.rename(main_old_name + county_old_name9 + file1, main_new_name + county_new_name9 + file1)
os.rename(main_old_name + county_old_name9 + file2, main_new_name + county_new_name9 + file2)
os.rename(main_old_name + county_old_name9 + file3, main_new_name + county_new_name9 + file3)
os.rename(main_old_name + county_old_name9 + file4, main_new_name + county_new_name9 + file4)
os.rename(main_old_name + county_old_name9 + file5, main_new_name + county_new_name9 + file5)

#新北
os.rename(main_old_name + county_old_name10 + file1, main_new_name + county_new_name10 + file1)
os.rename(main_old_name + county_old_name10 + file2, main_new_name + county_new_name10 + file2)
os.rename(main_old_name + county_old_name10 + file3, main_new_name + county_new_name10 + file3)
os.rename(main_old_name + county_old_name10 + file4, main_new_name + county_new_name10 + file4)
os.rename(main_old_name + county_old_name10 + file5, main_new_name + county_new_name10 + file5)

#新竹
os.rename(main_old_name + county_old_name11 + file1, main_new_name + county_new_name11 + file1)
os.rename(main_old_name + county_old_name11 + file2, main_new_name + county_new_name11 + file2)
os.rename(main_old_name + county_old_name11 + file3, main_new_name + county_new_name11 + file3)
os.rename(main_old_name + county_old_name11 + file4, main_new_name + county_new_name11 + file4)
os.rename(main_old_name + county_old_name11 + file5, main_new_name + county_new_name11 + file5)

#嘉義
os.rename(main_old_name + county_old_name12 + file1, main_new_name + county_new_name12 + file1)
os.rename(main_old_name + county_old_name12 + file2, main_new_name + county_new_name12 + file2)
os.rename(main_old_name + county_old_name12 + file3, main_new_name + county_new_name12 + file3)
os.rename(main_old_name + county_old_name12 + file4, main_new_name + county_new_name12 + file4)
os.rename(main_old_name + county_old_name12 + file5, main_new_name + county_new_name12 + file5)

#彰化
os.rename(main_old_name + county_old_name13 + file1, main_new_name + county_new_name13 + file1)
os.rename(main_old_name + county_old_name13 + file2, main_new_name + county_new_name13 + file2)
os.rename(main_old_name + county_old_name13 + file3, main_new_name + county_new_name13 + file3)
os.rename(main_old_name + county_old_name13 + file4, main_new_name + county_new_name13 + file4)
os.rename(main_old_name + county_old_name13 + file5, main_new_name + county_new_name13 + file5)

#臺中
os.rename(main_old_name + county_old_name14 + file1, main_new_name + county_new_name14 + file1)
os.rename(main_old_name + county_old_name14 + file2, main_new_name + county_new_name14 + file2)
os.rename(main_old_name + county_old_name14 + file3, main_new_name + county_new_name14 + file3)
os.rename(main_old_name + county_old_name14 + file4, main_new_name + county_new_name14 + file4)
os.rename(main_old_name + county_old_name14 + file5, main_new_name + county_new_name14 + file5)

#臺北
os.rename(main_old_name + county_old_name15 + file1, main_new_name + county_new_name15 + file1)
os.rename(main_old_name + county_old_name15 + file2, main_new_name + county_new_name15 + file2)
os.rename(main_old_name + county_old_name15 + file3, main_new_name + county_new_name15 + file3)
os.rename(main_old_name + county_old_name15 + file4, main_new_name + county_new_name15 + file4)
os.rename(main_old_name + county_old_name15 + file5, main_new_name + county_new_name15 + file5)

#臺東
os.rename(main_old_name + county_old_name16 + file1, main_new_name + county_new_name16 + file1)
os.rename(main_old_name + county_old_name16 + file2, main_new_name + county_new_name16 + file2)
os.rename(main_old_name + county_old_name16 + file3, main_new_name + county_new_name16 + file3)
os.rename(main_old_name + county_old_name16 + file4, main_new_name + county_new_name16 + file4)
os.rename(main_old_name + county_old_name16 + file5, main_new_name + county_new_name16 + file5)

#臺南
os.rename(main_old_name + county_old_name17 + file1, main_new_name + county_new_name17 + file1)
os.rename(main_old_name + county_old_name17 + file2, main_new_name + county_new_name17 + file2)
os.rename(main_old_name + county_old_name17 + file3, main_new_name + county_new_name17 + file3)
os.rename(main_old_name + county_old_name17 + file4, main_new_name + county_new_name17 + file4)
os.rename(main_old_name + county_old_name17 + file5, main_new_name + county_new_name17 + file5)
