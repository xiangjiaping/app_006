import yaml
with open("./sum.yml","r")as f:
    data =yaml.safe_load(f)
    print("data",data)
    for i in data.values():
        print("tup",(i.get("a"),i.get("b"),i.get("c")))