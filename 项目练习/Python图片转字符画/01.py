from PIL import Image
import argparse
#argparse 库是用来管理命令行参数输入的  目标是获取输入的突破路径/输出字符画的宽，高以及输出文件的路径。
parser = argparse.ArgumentParser()#创建命令行输入参数处理ArgumentParser对象。
#定义输入文件/输出文件/输出字符画的宽和高/
parser.add_argument('file') #输入参数
parser.add_argument('-o','--output')#输出文件
parser.add_argument('--whith',type= int , default=80)
parser.add_argument('--height',type=int,default=80)

#解析并获取参数
args = parser.parse_args()
print(type(args))
#输入的图片路径
IMG = args.file
#输出字符画的宽高
WIDTH= args.whith
HEIGHT = args.height
#输出字符画的路径
OUTPUT=args.output


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha=256):
    #判断alpha
    if alpha == 0:
        return  ' '
    #获取字符集的长度，这里为70
    length = len(ascii_char)
    #将RGB指转为gray,灰度值范围为0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1) / length
    # 返回灰度值对应的字符
    return ascii_char[int(gray / unit)]

if __name__=='__main__':
    #打开并调整图片的宽和高
    # im = Image.open(IMG)
    im = Image.open('/')
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    #初始化输出的字符串
    txt=''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j.i)))
        #遍历以行后增加环行符
        txt+='\n'
    print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)























