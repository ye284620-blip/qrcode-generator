import qrcode
import os

content = "https://www.baidu.com"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(content)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# 这里改成 output，指向根目录下的output文件夹
output_dir = "output"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

save_path = os.path.join(output_dir, "my_qrcode.png")
img.save(save_path)
print(f"✅ 二维码生成完成！文件位置：{save_path}")