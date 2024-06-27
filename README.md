### 代码功能
这部分代码用于在step格式的CAD零件上采样，生成txt格式的点云文件

### 环境需要
```bash
FreeCAD
Python=3.8
tqdm
pymeshlab
open3d
numpy
```

### 环境配置
```bash
conda create --name step2pcd python==3.8
conda activate step2pcd
pip install tqdm pymeshlab open3d numpy
```

### 运行代码
请把含有step格式CAD模型的文件夹与step2pcd.py放置在同一个目录下，而后运行：
```bash
python step2pcd.py <directory containing STEP models>
```

在之后，采样生成的点云的文件存储格式会与原step文件的存储格式相同
