import pytesseract
import auto
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
auto.saveAndCropFunc("./chuanqi/main", [0, 0, 1376, 818])
# 打开图片
image = Image.open('./chuanqi/main.jpg')

# 设置多字识别配置
config = {'tessedit_create_hocr': '1', 'hocr_font_info': '1', 'hocr_char_boxes': '1'}

# 将字典类型的config参数转换为字符串类型的配置参数
config_str = ' '.join([f'-c {key}={value}' for key, value in config.items()])

# 进行OCR识别
data = pytesseract.image_to_data(image, lang='chi_sim', config=config_str, output_type='dict')
print(data['text'])
# 输出识别结果
for i, word in enumerate(data['text']):
    # 判断当前单词是否是多字词组
    if word.startswith('[') and word.endswith(']'):
        # 合并多字词组
        j = i + 1
        while j < len(data['text']) and not data['text'][j].startswith('['):
            if data['conf'][j] != '-1':
                word += data['text'][j]
            j += 1
        # 输出多字词组
        print(word)