#
class Record:
    globals_id = 0

    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        Record.globals_id += 1
        self.record_id = Record.globals_id

    def set_number(self,phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return "{}\t{}\t{}".format(self.record_id,self.name,self.phone_number)

class PhoneBook:
    def __init__(self):
        self.data = []
    def add_record(self,record):
        self.data.append(record)


    def query_record(self,name):
        query_result = []
        query_ids = []
        for record in self.data:
            if record.name == name:
                query_result.append(record)
                query_ids.append(record.record_id)
        return query_ids,query_result








if __name__ == "__main__":
    phonebook = PhoneBook()
    while True:
        menu = """
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出
        
        """
        print(menu)
        s = input("请选择操作:")
        if s in ["1","2","3","4","5"]:
            if s == "1":
                name = input("请输入姓名:")
                phone_number = input("请输入电话:")
                record = Record(name,phone_number)
                phonebook.add_record(record)
                print(record)
            if s == "2":
                name = input("请输入姓名:")
                query_ids,query_result = phonebook.query_record(name)
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record.record_id, record.name, record.phone_number))




            if s == "5":
                break

        else:
            print("输入错误")
            continue

