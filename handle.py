import os
import re
from shutil import copyfile

for root, dirs, files in os.walk(r"/Users/dupeipei/Desktop/读书笔记"):
    prog = re.compile('!\[.*\]\(.*\)')
    prog2 = re.compile('\(.*\)')
    for file in files:
        file_name_split = file.split('.')
        if file_name_split[-1] == "md":
            md_file_path = os.path.join(root, file)
            newDirs = os.path.join(root, file_name_split[0] + ".assets")
            relativeDirs = os.path.join("file:/../", file_name_split[0] + ".assets")
            with open(md_file_path, 'r', encoding='utf8') as fileMd:
                data = fileMd.read()
                # print(data)
                paths = prog.findall(data)
                if len(paths) == 0:
                    continue
                else:
                    if not os.path.exists(newDirs):
                        os.makedirs(newDirs)
                for path in paths:
                    oldPicPath = prog2.search(path).group()[1:-1]
                    newPicPath = os.path.join(newDirs, oldPicPath.split('\\')[-1])
                    newPicPath = os.path.join(relativeDirs, oldPicPath.split('\\')[-1])
                    print(oldPicPath, newPicPath)
                    try:
                        copyfile(oldPicPath, newPicPath)
                        data = data.replace(oldPicPath, newPicPath)
                    except:
                        print(oldPicPath)
            with open(md_file_path, 'w', encoding='utf8') as fileMd:
                fileMd.write(data)

