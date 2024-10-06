训练模型
yolo detect train data=/home/tan_15592/yolo/dataset/data.yaml model=yolov8n.pt epochs=20 batch=4 imgsz=640 cache=disk
推理图像
yolo detect predict model=ultralytics/runs/detect/train/weights/best.pt source=test_images/image.jpg conf=0.25 save_txt=True
可视化界面Streamlit
启动：streamlit run app.py
得到网址运行
结束：按下 Ctrl+C 组合键。这将终止正在运行的 Streamlit 应用程序
