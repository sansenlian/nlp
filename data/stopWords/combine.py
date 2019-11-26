# 目的:读取lib文件夹下的所有文件,并把内容统一整合成不重复的文本
import os

if __name__ == "__main__":
    for root, dirs, files in os.walk("./lib", topdown=False):
        for name in dirs:
            print('='*20)
            print('打开lib目录里的'+name+'文件夹\n')
            stopWordsSet = set()
            for f in os.listdir(os.path.join(root, name)):
                f = os.path.join(os.path.join(root, name, f))
                print(f) # 输出打开的文件
                with open(f, 'r', encoding='utf-8') as fp:
                    for word in fp.readlines():
                        stopWordsSet.add(word.strip()) #一次把读取,并且内容要求不重复

            stopWords = sorted(list(stopWordsSet))
            with open('{}.txt'.format(name), 'w', encoding='utf-8') as f:
                for word in stopWords:
                    f.write("%s\n" % word)
