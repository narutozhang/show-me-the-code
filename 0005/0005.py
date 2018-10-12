

#  第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

#  尺寸的裁剪，不大于目标分辨率 1136*640
#  比较长宽比例，确定缩放比例
#  按比例缩放


import cv2
from math import floor
import os

'''
缩放函数， 按长边缩放到目标分辨率
'''
def resize_img(img, dsize):

    src_y, src_x, src_channel = img.shape
    dst_y, dst_x = dsize

    if dst_x >= src_x and dst_y >= src_y:
        return img
    else:
        src_ratio = src_y / src_x
        dst_ratio = dst_y / dst_x

        if src_ratio > dst_ratio:
            dst_x = floor(src_x * dst_y / src_y)
        else:
            dst_y = floor(src_y * dst_x / src_x)

        dst = cv2.resize(img, (dst_x, dst_y), interpolation=cv2.INTER_AREA)
        return dst


if __name__ == '__main__':

    src_dir = r'D:\show-me-the-code\0005\src_dir'
    dest_dir = r'D:\show-me-the-code\0005\dest_dir'
    dsize = (1136, 640)

    # 遍历源目录
    for i, file in enumerate(os.listdir(src_dir)):
        # 检查文件后缀
        if os.path.splitext(file)[1].lower() in ['.jpg', '.jpeg', '.png',  '.bmp']:
            try:
                src = cv2.imread(os.path.join(src_dir, file))
                dst = resize_img(src, dsize)

                # 目标文件已存在，跳过（不能直接覆盖）
                if os.path.exists(os.path.join(dest_dir, file)):
                    print(i, dest_dir, file, 'already exists, skipped.')
                else:
                    cv2.imwrite(os.path.join(dest_dir, file), dst)
                    print(i, file, '处理成功.')

            except Exception as e:
                print(i, file, '文件处理错误.', '\n', e)
                continue
        else:
            print(i, file, 'is not a image file, skipped.')

