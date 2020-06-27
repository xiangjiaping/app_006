import  yaml
with open("./data2.yaml","r",encoding="utf-8")as f:
        data = yaml.safe_load(f)
        print("返回字典数据：",data)
        print("返回数据类型：",type(data.get("info")))