import cv2
import numpy as np
import os
import re
import xml.etree.ElementTree as ET
import pickle

# a = [(48.45266342163086, 105.57950592041016), (46.40642376200358, 104.07681701490613), (44.757519907633466, 102.75048572455512), (43.477869750976566, 101.58694194030763), (42.53939118448894, 100.57261555311416), (41.91400210062663, 99.69393645392526), (41.57362039184571, 98.93733453369143), (41.490163950602216, 98.28923968336316), (41.63555066935222, 97.73608179389109), (41.981698440551746, 97.26429075622555), (42.500525156656906, 96.86029646131728), (43.163948710123684, 96.51052880011663), (43.943886993408206, 96.20141766357423), (44.81225789896647, 95.91939294264051), (45.740979319254556, 95.65088452826606), (46.701969146728516, 95.38232231140137), (47.6671452738444, 95.10013618299696), (48.608425593058264, 94.79075603400335), (49.49772799682617, 94.4406117553711), (50.306970377604166, 94.03613323805067), (51.008070627848305, 93.56375037299262), (51.57294664001465, 93.00989305114746), (51.97351630655924, 92.36099116346571), (52.18169751993815, 91.6034746008979), (52.169408172607426, 90.72377325439453), (51.90856615702312, 89.70831701490614), (51.37108936564128, 88.54353577338325), (50.52889569091798, 87.21585942077637), (49.35390302530925, 85.71171784803603), (47.81802926127116, 84.01754094611273), (45.893192291259766, 82.11975860595703)] 

# 三阶贝塞尔曲线公式
def cubic_bezier_point(p0, p1, p2, p3, t):
    x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
    y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
    return [x, y]


def svg_4control_corrd(svg_path):
    '''
    输入svg图片,返回每个path四个贝塞尔曲线坐标path[[trroke1_corrd],[trroke2_corrd]......]
    '''
    # 初始化坐标,颜色,粗细
    path,stroke_coord = [],[]
    # 解析SVG文件
    tree = ET.parse(svg_path)
    root = tree.getroot()
    # 使用命名空间前缀来定位<path>元素
    namespace = '{http://www.w3.org/2000/svg}'
    path_elements = root.findall(f'.//{namespace}path')
    if not path_elements:
        raise ValueError("path_elements为空,检查svg文件namespace是否正确,或者是否有'path'元素")

    for path_element in path_elements:
        d_attribute = path_element.get('d')
        # 正则表达式匹配数字坐标
        pattern = r"[-\d\.]+"
        matches = re.findall(pattern, d_attribute)
        # 每条曲线四个坐标对
        coordinates = [(float(matches[i]), float(matches[i+1])) for i in range(0, len(matches), 2)]
        #print(coordinates)
        path.append(coordinates)
    
    return(path)

def coordinate_interpolation(path_list,num_points):
    '''
    输入svg16个笔画的坐标对，进行插值，输出pkl所需格式(x,y,0or1)
    '''
    points = []
    for path in path_list:
        p0,p1,p2,p3 = path[0],path[1],path[2],path[3]   
        
        for i in range(num_points):
            t = i / num_points
            point = cubic_bezier_point(p0, p1, p2, p3, t)
            point.append(0.)
            points.append(point)
        point = cubic_bezier_point(p0, p1, p2, p3, 1)
        point.append(1.)
        points.append(point)
        numpy_array = np.array(points)
    
    return numpy_array   

def main(input_folder):
    memory_index={}
    for root, _, files in os.walk(input_folder):
        for file in files:
            # file_name = file.split(".")[0]
            file_name = os.path.splitext(file)[0]
            folder_name = os.path.basename(root)
            name = os.path.join('/',folder_name,file_name)
            svg_path=os.path.join(root,file)
            memory_index[name]=coordinate_interpolation(svg_4control_corrd(svg_path),10)
    
    print(memory_index)

    with open("/home/piaofengyuan/test/save.txt", "w") as save:
        save.write(str(memory_index))

    with open('Part_Coordinate', 'wb') as file:
        pickle.dump(memory_index, file)
        
if __name__=="__main__":
    
    main(r"/home/piaofengyuan/test/Retrieval_Data (1)")


