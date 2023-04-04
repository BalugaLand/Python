from PIL import Image,ImageFont,ImageDraw
import os
newdir = "C:/Users/MI/Desktop/截图合并"
if not os.path.exists(newdir):
    os.mkdir(newdir)
print("请将两张图片放入“截图合并”文件夹")
name = input("请输入你的班级姓名学号:")
img1_name = input("请输入第一张图片名称：")
img2_name = input("请输入第二张图片名称：")
img1 = Image.open(f"C:/Users/MI/Desktop/截图合并/{img1_name}.png")
img2 = Image.open(f"C:/Users/MI/Desktop/截图合并/{img2_name}.png")
img1 = img1.resize((500,1000))
img2 = img2.resize((500,1000))
img3 = Image.new("RGB",(1000,1000))
img3.paste(img1,(0,0))
img3.paste(img2,(500,0))
font = ImageFont.truetype("C:\Windows\Fonts\Deng.ttf",80)
z = ImageDraw.Draw(img3)
z.text((50,800),name,font = font,fill="red")
img3.save("C:/Users/MI/Desktop/截图合并/hebing.png")
img3.show()
