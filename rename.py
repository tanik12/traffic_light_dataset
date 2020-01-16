import glob
import os
import sys
 
def main():
    # 拡張子.jpgのファイルを取得する
    args = sys.argv
    img_path = './' + args[1] + '/*.jpg'
    i = 1
     
    # image pathを取得する
    file_lists = glob.glob(img_path)
    print('変更前')
    print(file_lists)
     
    # image nameを一括で変更する
    for file_name in file_lists:
      os.rename(file_name, './' + args[1] + '/traffic_' + "%06.f.jpg" % i)
      i += 1
     
    li = glob.glob(img_path)
    print('変更後')
    print(li)

if __name__ == "__main__":
    main()