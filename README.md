1.训练模型

在终端项目目录下，进入yolo虚拟环境，通过以下指令开始训练：

yolo detect train data=/home/your path/dataset/data.yaml model=yolov8n.pt epochs=50 batch=4 imgsz=640 cache=disk

img 640: 指定输入图像的大小。640是常用的大小，通常在640x640或416x416之间选择。增大图像尺寸可以提高精度，但也会增加训练时间和内存消耗。

batch 16: 指定每次训练的批次大小。根据你的GPU内存调整，如果内存不足，可以减小这个值，比如 --batch 8 或 --batch 4。

epochs 50: 指定训练的轮数。可以根据需要调整，通常从50开始，后续可根据验证结果增加。

data /path/to/data.yaml: 指定数据集的配置文件路径。这是之前创建的 data.yaml 文件的完整路径。


2.可视化界面Streamlit训练模型

启动：终端输入streamlit run app.py（app.py为可视化界面代码）。

训练：得到一个网址打开，上传已经标注好的数据集，点击开始训练按钮，训练完成后会得到图片信息文件的路径。

结束：终端按下 Ctrl+C 组合键，这将终止正在运行的 Streamlit 应用程序。


3.推理图像

在终端执行以下指令，可以训练单个图片或整个文件夹，并生成一个txt文件显示图片信息。

yolo detect predict model=ultralytics/runs/detect/train/weights/best.pt source=test_images/image.jpg conf=0.25 save_txt=True

model=best.pt路径

source=测试图片路径

conf=0.25，只保留大于0.25的标注

save_txt=True,生成txt文件


4.标注图片（labelimg）

进入指定目录：cd /home/your path/labelImg

创建虚拟环境：python3 -m venv labelimg-venv

进入虚拟环境：source labelimg-venv/bin/activate

打开labelimg：python labelImg.py，利用程序标注图片信息

退出虚拟环境：deactivate
