from rest_framework.test import APIClient

# class Computer():
#     def __init__(self, computer, ram, storage):
#         self.computer = computer
#         self.ram = ram
#         self.storage = storage
#
#     def test(self):
#         print(10)
#
#
# # Class Mobile inherits Computer
# class Mobile(Computer):
#     def __init__(self, computer, ram, storage, model):
#         super().__init__(computer, ram, storage)
#         self.model = model
#
#     def test(self):
#         super().test()


# Apple = Mobile('Apple', 2, 64, 'iPhone X')
# print('The mobile is:', Apple.computer)
# print('The RAM is:', Apple.ram)
# print('The storage is:', Apple.storage)
# print('The model is:', Apple.model)
# Apple.test()
# dict = {}
# print(dict.get('test', 0))
data = {
    "name": "Сибирская котята тест тест, 3 месяца",
    "price": 2500,
    "author": "pnikifirov",
    "category": 1,
    "is_published": "FALSE"
}

client = APIClient()
response = client.post("/ad/create/", data=data)
print(response.status_code)