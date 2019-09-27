"""
龙腾测试dev课程，通讯录程序
实现一个简单的通讯录，包含增删改查
Python顺序执行

"""

#1.李亮15130078689
record_list = []
record_id = 0   #id是为了删除重名的手机号

def input_record():
    name = input("请输入姓名：")
    phone_number = input("请输入手机号：")
    record = {'name':name,'phone_number':phone_number}   #用字典构建一条记录
    return record



def add_record():
    record = input_record()
    global record_id
    record_id += 1
    record['record_id'] = record_id
    record_list.append(record)
    return "添加成功"

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
        s = input("请选择操作：")
        if s in ["1", "2", "3", "4", "5"]:
            if s == "1":
                msg = add_record()
                print(msg)
            else:
                print("输入错误")
                continue