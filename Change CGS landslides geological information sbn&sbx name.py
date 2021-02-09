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

sbn = '.sbn'
sbx = '.sbx'


#更改資料夾名稱
#宜蘭
os.rename(main_old_name + county_old_name1 + sbn, main_new_name + county_new_name1 + sbn)
os.rename(main_old_name + county_old_name1 + sbx, main_new_name + county_new_name1 + sbx)

#花蓮
os.rename(main_old_name + county_old_name2 + sbn, main_new_name + county_new_name2 + sbn)
os.rename(main_old_name + county_old_name2 + sbx, main_new_name + county_new_name2 + sbx)

#南投
os.rename(main_old_name + county_old_name3 + sbn, main_new_name + county_new_name3 + sbn)
os.rename(main_old_name + county_old_name3 + sbx, main_new_name + county_new_name3 + sbx)

#屏東
os.rename(main_old_name + county_old_name4 + sbn, main_new_name + county_new_name4 + sbn)
os.rename(main_old_name + county_old_name4 + sbx, main_new_name + county_new_name4 + sbx)
#苗栗
os.rename(main_old_name + county_old_name5 + sbn, main_new_name + county_new_name5 + sbn)
os.rename(main_old_name + county_old_name5 + sbx, main_new_name + county_new_name5 + sbx)

#桃園
os.rename(main_old_name + county_old_name6 + sbn, main_new_name + county_new_name6 + sbn)
os.rename(main_old_name + county_old_name6 + sbx, main_new_name + county_new_name6 + sbx)

#高雄
os.rename(main_old_name + county_old_name7 + sbn, main_new_name + county_new_name7 + sbn)
os.rename(main_old_name + county_old_name7 + sbx, main_new_name + county_new_name7 + sbx)

#基隆
os.rename(main_old_name + county_old_name8 + sbn, main_new_name + county_new_name8 + sbn)
os.rename(main_old_name + county_old_name8 + sbx, main_new_name + county_new_name8 + sbx)

#雲林
os.rename(main_old_name + county_old_name9 + sbn, main_new_name + county_new_name9 + sbn)
os.rename(main_old_name + county_old_name9 + sbx, main_new_name + county_new_name9 + sbx)

#新北
os.rename(main_old_name + county_old_name10 + sbn, main_new_name + county_new_name10 + sbn)
os.rename(main_old_name + county_old_name10 + sbx, main_new_name + county_new_name10 + sbx)

#新竹
os.rename(main_old_name + county_old_name11 + sbn, main_new_name + county_new_name11 + sbn)
os.rename(main_old_name + county_old_name11 + sbx, main_new_name + county_new_name11 + sbx)

#嘉義
os.rename(main_old_name + county_old_name12 + sbn, main_new_name + county_new_name12 + sbn)
os.rename(main_old_name + county_old_name12 + sbx, main_new_name + county_new_name12 + sbx)

#彰化
os.rename(main_old_name + county_old_name13 + sbn, main_new_name + county_new_name13 + sbn)
os.rename(main_old_name + county_old_name13 + sbx, main_new_name + county_new_name13 + sbx)

#臺中
os.rename(main_old_name + county_old_name14 + sbn, main_new_name + county_new_name14 + sbn)
os.rename(main_old_name + county_old_name14 + sbx, main_new_name + county_new_name14 + sbx)

#臺北
os.rename(main_old_name + county_old_name15 + sbn, main_new_name + county_new_name15 + sbn)
os.rename(main_old_name + county_old_name15 + sbx, main_new_name + county_new_name15 + sbx)

#臺東
os.rename(main_old_name + county_old_name16 + sbn, main_new_name + county_new_name16 + sbn)
os.rename(main_old_name + county_old_name16 + sbx, main_new_name + county_new_name16 + sbx)

#臺南
os.rename(main_old_name + county_old_name17 + sbn, main_new_name + county_new_name17 + sbn)
os.rename(main_old_name + county_old_name17 + sbx, main_new_name + county_new_name17 + sbx)
