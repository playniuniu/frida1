import jieba
import json

if __name__ == '__main__':

    f = open("C:\\Users\\Administrator\\Downloads\\moto_push_count.json", encoding='utf-8')
    json_root = json.load(f)
    json_array = json_root["RECORDS"]
    dic = {}

    temp_list = []
    for json_object in json_array:
        title = json_object['s_title']
        if title is None or title == 'all':
            continue
        temp_list.append(title)

    for title in set(temp_list):
        try:
            seg_list = jieba.cut(title)  # 默认是精确模式
            for seg in seg_list:
                if seg in dic.keys():
                    dic[seg] = dic[seg] + 1
                else:
                    dic[seg] = 1
        except OSError:
            pass

    for k, v in dic.items():
        print(k + ":" + str(v))
