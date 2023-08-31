from PIL import Image
import os

def convert_png_to_jpg(png_file):
    
    png_images = os.listdir(png_file)
    
    for png_image in png_images:
        
        # 判断输入的图片是否为PNG格式
        if png_image.lower().endswith("png"):
            print("-------------------------------------------------")
        else:
            print("文件输入格式不正确，请检查！")
        
        image = Image.open(os.path.join(png_file, png_image))
        rgb_image = image.convert('RGB')

        # 去除文件名的后缀，只保留前面的文件名
        name_without_extension = os.path.splitext(png_image)[0]

        # 保存转换成JPG格式的路径
        rgb_image.save("./valve_photo_jpg/"+name_without_extension+".jpg", "JPEG")
        print(f"成功将 {png_image} 转换为{name_without_extension}.jpg")

if __name__ == "__main__":
    # 指定 PNG 图片路径
    png_file = "./valve_photo_png"
    # 执行转换
    convert_png_to_jpg(png_file)
