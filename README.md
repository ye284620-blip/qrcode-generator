QRCode Generator
 
项目简介
 
基于 Python 的  qrcode  库实现的简易二维码生成工具，支持快速生成标准黑白二维码，可自定义二维码内容（网址、文本等），自动输出到指定目录统一管理。
 
功能特性
 
- 生成标准格式的黑白二维码
- 支持自定义二维码内容（网址、纯文本均可）
- 自动创建输出目录，统一存放生成的图片
- 可灵活配置二维码尺寸、容错等级、边框大小
 
环境依赖
 
- Python 3.x
- qrcode 7.4.2
- Pillow 12.3.0
 
使用方法
 
1. 安装依赖
 
bash
  
pip install qrcode pillow
 
 
2. 运行脚本
打开  qr_generator.py ，修改  content  变量为你想要生成的内容，保存后执行：
 
bash
  
python qr_generator.py
 
 
3. 查看结果
生成的二维码图片会自动保存到项目根目录下的  output  文件夹中，文件名为  my_qrcode.png 。
 
目录结构
 
plaintext
  
qrcode-generator/
├── output/              # 输出目录，存放生成的二维码图片
│   └── my_qrcode.png
├── .gitignore           # Git 忽略规则配置
└── qr_generator.py      # 二维码生成主程序
 
 
自定义配置
 
在  qr_generator.py  中可修改以下参数，调整二维码效果：
 
-  version ：二维码版本，取值 1-40，数值越大整体尺寸越大
-  error_correction ：容错等级，支持 L / M / Q / H 四个等级
-  box_size ：每个小方块的像素大小
-  border ：二维码四周的边框宽度
-  fill_color  /  back_color ：二维码前景色、背景色
