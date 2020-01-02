import glob
import os
 
# 拡張子.txtのファイルを取得する
img_path = './traffic_light/*.jpg'
i = 1
 
# txtファイルを取得する
file_lists = glob.glob(img_path)
print('変更前')
print(file_lists)
 
# ファイル名を一括で変更する
for file_name in file_lists:
  os.rename(file_name, './traffic_light/traffic_' + "%06.f.jpg" % i)
  i += 1
 
li = glob.glob(img_path)
print('変更後')
print(li)
