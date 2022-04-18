'''
读取中国高等教育双一流学科建设word文档，分析存储每个学校下的所有一流专业
'''
import docx
import json

docPath = './University/top_notch_subjects_20170921.docx'
def readSubjectDoc(name=docPath):
    doc = docx.Document(name)
    allParas = doc.paragraphs
    universityArr = []
    for par in allParas:
        # 分离学校名和学科数组
        text = par.text
        if '：' not in text:
            continue
        arr = text.split('：')
        university = arr[0]
        if len(university) <= 3:
            continue
        subjects = arr[1].split('、')
        universityArr.append({
            'name': university,
            'subjects': subjects
        })
    save_json(universityArr)


def save_json(json_data={}):
    if json_data:
        with open('./University/china_top_notch_subjects.json', 'w') as f:
            f.write(json.dumps(json_data, ensure_ascii=False))
            

def main():
    readSubjectDoc()

if __name__ == '__main__':
    main()