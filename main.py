import os
# import datetime

tag = "@qq.sohu.com"
dict_folder = "dict"
size_threshold = 1024 * 1024

# yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).timestamp()

# 删除所有QQ拼音同步临时文件
def delete_big_file_before_today(root):
    for item in os.scandir(root):
        #if item.is_file() and item.name.isdigit() and item.stat().st_size>size_threshold and item.stat().st_mtime < yesterday:
        if item.is_file() and item.name.isdigit() and item.stat().st_size>size_threshold:
            delete_file(item.path)
        

def delete_file(filename):
    # print("{0} deleted".format(filename))
    os.remove(filename)


def delete_qqpinyin_junk():
    # qq拼音用户文件夹
    users_folder = r'{0}\Tencent\QQPinyin\users'.format(os.getenv('PROGRAMDATA'))
    for filename in os.listdir(users_folder):
        if tag in filename:
            delete_big_file_before_today(os.path.join(users_folder, filename, dict_folder))

delete_qqpinyin_junk()
