import streamlit as st
import os
import subprocess

# 设置标题
st.title("YOLOv8 物体检测训练系统")

# 上传数据集
uploaded_file = st.file_uploader("上传你的数据集 (ZIP/TAR 文件)", 
type=["zip", "tar"],help="上传的文件大小限制为500MB")

# 设置训练参数
epochs = st.number_input("训练轮数", min_value=1, value=10)
batch_size = st.number_input("每批大小", min_value=1, value=16)
img_size = st.number_input("图像大小", min_value=1, value=640)

# 开始训练的按钮
if st.button("开始训练"):
    if uploaded_file is not None:
        # 保存上传的文件
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("数据集已上传，开始训练...")

        # 解压数据集
        os.makedirs("dataset", exist_ok=True)
        
        # 根据文件格式解压
        if uploaded_file.name.endswith(".zip"):
            subprocess.run(["unzip", uploaded_file.name, "-d", "dataset"])
        elif uploaded_file.name.endswith(".tar"):
            subprocess.run(["tar", "-xf", uploaded_file.name, "-C", "dataset"])

        # 训练模型的命令
        command = f"yolo train data=dataset/data.yaml model=yolov8n.pt epochs={epochs} batch={batch_size} imgsz={img_size}"
        
        # 执行训练命令
        result = subprocess.run(command.split(), capture_output=True, text=True)

        # 显示训练结果
        st.text(result.stdout)
        st.success("训练完成！")
    else:
        st.error("请先上传数据集！")

