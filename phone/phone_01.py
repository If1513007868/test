"""
龙腾测试dev课程，通讯录程序
实现一个简单的通讯录，包含增删改查
Python顺序执行

"""
record_list = []  #定义一个列表，存取数据

record_id = 0          #定义一个ID，防止重名


def input_record():
    name = input("请输入姓名:")
    phone_number = input("请输入电话:")
    record = {"name": name, "phone_number": phone_number}   #字典构建一条记录
    return record


def add_record():
    record= input_record()  #调取输入功能
    global record_id    #全局变量
    record_id += 1
    record["record_id"] = record_id   #会生成3个key,id name,number
    record_list.append(record)   #将这个记录加入列表
    return "添加成功"


def query_record(name):
    query_result = []  #空的查询结果
    query_ids = []   #用来存查询的结果
    for record in record_list:    #便利
        if record["name"] == name:
            query_ids.append(record["record_id"])     #将结果放到
            query_result.append(record)
    return query_ids, query_result

def delete_record(name):
    query_ids, query_result = query_record(name)

    if len(query_ids) == 0:
        print("不存在")
    else:
        if len(query_result) > 1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            record_id = input("请选择要删除的id:")
            if int(record_id) in query_ids:
                for record in record_list:
                    if int(record_id) == record["record_id"]:
                        record_list.remove(record)
            else:
                print("输入错误!!!")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
            while True:
                s = input("是否确认删除(Y/N):")
                if s in ["Y", "N"]:
                    if s == "Y":
                        record_list.remove(query_result[0])
                    else:
                        pass
                    break
                else:
                    print("输入错误!!!")


def change_record(name):
    query_ids, query_result = query_record(name)
    if len(query_ids) == 0:
        print("不存在!!!")
    else:
        if len(query_result) > 1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            record_id = input("请选择要修改的id:")
            if int(record_id) in query_ids:
                for record in record_list:
                    if int(record_id) == record["record_id"]:
                        phone_number =input("请输入修改后的电话号码:")
                        record["phone_number"] = phone_number
                        print("修改成功")
                        break
            else:
                print("输入错误!!!")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"],
                                      query_result[0]["name"], query_result[0]["phone_number"]))
            phone_number = input("请输入修改后的电话号码:")
            query_result[0]["phone_number"] = phone_number
            print("修改成功")

if __name__ == "__main__":
    while True:
        menu = """
        通讯录
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出
        """
        print(menu)
        s = input("请选择操作:")
        if s in ["1", "2", "3", "4", "5"]:

            if s == "1":
                msg = add_record()
                print(msg)
            if s == "2":
                name = input("请输入姓名:")
                query_ids, query_result = query_record(name)
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            if s == "3":
                name = input("请输入姓名:")
                delete_record(name)
            if s == "4":
                name = input("请输入姓名:")
                change_record(name)
            if s == "5":
                break
        else:
            print("输入错误")
            continue





