from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

user_customer = {}
class Customer():
    def __init__(self, name, phone, barcode):
        self.name = name
        self.phone = phone
        self.barcode = barcode
    
class Queue_cutomer():
    def __init__(self):
        self.queue = []
        #self.front = -1
    def add_to_queue(sefl, customer):
        sefl.queue.append(customer)
        return (f"Khách hàng {customer.name} đã được thêm vào hàng đợi.")
    def list_customer(sefl):
        if len(sefl.queue) == 0:
            return ("Hàng đợi rỗng")
        else:
            return sefl.queue
    def seve_customer(sefl):
        if sefl.queue:
            customer = sefl.queue.pop(0)
            return (f'Đang phục vụ khách hàng {customer.name}')
        else:
            return 'Hàng đợi rỗng'
quue_customer = Queue_cutomer()
#lấy danh sách
@app.get('/customer')
async def get_customer():
    list_customer = quue_customer.list_customer()
    return list_customer

#Thêm khách hàng
@app.post("/add-customer/{name}")
async def create_item(name, phone, barcode):
    customer = Customer(name=name, phone=phone, barcode=barcode)
    return ("new_customer", quue_customer.add_to_queue(customer))

#Lấy khách hàng đầu hàng đợi
@app.get('/sev-customer')
async def sever_customer():
    return {'Đang phục vụ khách hàng': quue_customer.seve_customer()}
#Khởi tạo hàng đợi
# def init(queue, q):
#     q.elements = {}
#     q.front = -1

#Kiểm tra hàng đợi trống
# def is_element(queue, q):
#     return len(q.element) == 0

# #trả về phần tử đầu hàng đợi
# def get_front(queue, q):
#     if len(q.element) == 0:
#         return ('Hàng đợi rỗng')
#     else:
#         return q.elememt[q.front]

# #thêm phẩn tử vào hàng đợi
# #Thêm mới khách hàng
# # @app.post("/customers")
# # async def create_customer(item: Customer):
# #     userName = item.name
# #     user_customer[userName] = item.dict()
# #     return userName
# @app.post("/customers")
# def add_to_queue(queue, q, customer: Customer):
#     userName = customer.name
#     #user_customer[userName] = customer.dict()
#     q.elements[user_customer] = customer.dict()
#     return userName

# #Xoá phần tử khỏi hàng đợi
# def delete_from_queue(queue, q):
#     if len(q.element) == 0:
#         return ('Hàng đợi rỗng')
#     else:
#         del q.elements[q.front] 


# #Lấy danh sách khách hàng
# @app.get('/customers')
# async def get_customer():
#     user = user_customer
#     return user


