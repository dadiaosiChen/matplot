#coding:utf-8
import matplotlib.pyplot as plt
show_heigth = 100              
show_width = 200
#这两个数字是调出来的
#显示字符的长宽比为1:2，如果原图1:1，那么高：宽应为2:1

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#生成一个ascii字符列表
char_len = len(ascii_char)


# png格式的图片读出来计算的数字会有误差
pic = plt.imread("jerry.jpg")
#使用plt.imread方法来读取图像，对于彩图，返回size = heigth*width*3的图像
#matplotlib 中色彩排列是R G B
#opencv的cv2中色彩排列是B G R

# print pic

pic_heigth,pic_width,_ = pic.shape
#获取图像的高、宽
# print pic_heigth,pic_width

gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
#RGB转灰度图的公式 gray = 0.2126 * r + 0.7152 * g + 0.0722 * b



#思路就是根据灰度值，映射到相应的ascii_char
f1=open('jerry.txt','a')
for i in range(show_heigth):
    #根据比例映射到对应的像素
    y = int(i * pic_heigth / show_heigth)
    text = ""
    for j in range(show_width):
        x = int(j * pic_width / show_width)
        text += ascii_char[int(gray[y][x] / 256 * char_len)]
    
    f1.write(text)
    f1.write("\n")
    print(text)

# f1.write(text)
f1.close()