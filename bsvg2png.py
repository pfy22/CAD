import cairosvg
import os
from PIL import Image

def svg_to_png(root):
    
    svg_files = os.listdir(root)
    
    for svg_file in svg_files:
        
        for svg_image in os.listdir(os.path.join(root, svg_file)):
            if svg_image.lower().endswith("svg"):
                print("------------------------开始转换-----------------------------")
            else:
                print("----------------文件输入格式不正确，请检查！-------------------")
        
            name_without_extension = os.path.splitext(svg_image)[0]
            out_path = root+"/"+svg_file+"/"+name_without_extension+"m.png"
            cairosvg.svg2png(url=os.path.join(root, svg_file, svg_image), write_to=out_path)
            svg_image_rbga = Image.open(out_path)
            width, height = svg_image_rbga.size
            canvas = Image.new(mode="RGBA", size=(width, height), color=(255, 255, 255, 255))
            canvas.paste(svg_image_rbga, (0, 0), svg_image_rbga)
            canvas.save(root+"/"+svg_file+"/"+name_without_extension+".png")
            os.remove(os.path.join(root, svg_file, svg_image))
            os.remove(out_path)
            print(f"成功将{svg_image}转换成{name_without_extension}.png")

# 测试模块
if __name__ == "__main__":
    root = "./Flange_24strokes"
    svg_to_png(root)











# ------------------------------------测试os.path.join()和listdir()------------------------------------------------
# import os 
# from PIL import Image
# png_file = ".\PNG\\valve"
# png_images = os.listdir(png_file)
# for png_image in png_images:
#     print(png_image)
#     print("------------------------------------")
#     print(os.path.join(png_file, png_image))

# -----------------------------------------结论------------------------------------------------------
"""
os.listdir()仅获取目录下的文件名，不会获取完整的路径，因此再次调用此路径一般需要用os.path.join()拼接
os.path.join()拼接文件路径，会自动补全不同层级文件之间的/，因此可以看成是把后面的文件放到前面的文件里面
"""
