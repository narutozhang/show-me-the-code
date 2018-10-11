
#   第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re


#   输入文件对象，逐行进行拆分统计
def words_count(file_obj):

    wc = {}
    try:
        for line in file_obj.readlines():
            words = re.split(r'[\s\r\n,.?:!/“”\-—|]', line)
            for word in words:
                w = word.lower()
                if wc.get(w):
                    wc[w] += 1
                else:
                    wc[w] = 1

    except Exception as e:
        print(e)
        wc = None

    return wc


if __name__ == '__main__':
    file = r'D:\show-me-the-code\0004\HPBook1.txt'
    file_obj = open(file, encoding='utf8')
    wc = words_count(file_obj)
    sorted_wc = sorted(wc, key=lambda item: wc[item], reverse=True)
    for x in zip(sorted_wc, [wc[x] for x in sorted_wc]):
        print(x)
