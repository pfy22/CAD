import os
import shutil
import bsvg2png

root_directory = "./Motor_24strokes1"
os.mkdir("./Motor_24strokes")
out_put = "./Motor_24strokes"
for input_path_first in os.listdir(root_directory):
    os.mkdir(os.path.join(out_put, input_path_first))
    for input_path_sencond in os.listdir(os.path.join(root_directory, input_path_first)):
        for input_path_third in os.listdir(os.path.join(root_directory, input_path_first, input_path_sencond)):
            if input_path_third.lower().endswith("best.svg"):
                print(f"Keep--{input_path_third}")
                source_path = os.path.join(root_directory, input_path_first, input_path_sencond, input_path_third)
                target_path = os.path.join(out_put, input_path_first)
                shutil.move(source_path, target_path)  # 剪切！不是复制粘贴
            else:
                print(f"Pass--{input_path_third}")

bsvg2png.svg_to_png(out_put)





           