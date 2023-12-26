
#Tìm kiếm tuyến tính:
def search(arr, x):
    # Duyệt qua tùng phần tử của danh sách
    for i in range(len(arr)):
        #so sánh x với từng phần tử trong mảng, nếu bằng thì trả về giá trị i không có giá trị nào bằng thì trả -1,
        #chuyển đổi kiểu dữ liệu x thành int do inout trả về str
        if arr[i] == int(x):
            return i
    return -1

arr = [0,1,4,6,9,10,16]
x = input("Tìm kiếm: ")

#gọi hàm search truyền vào arr là danh sách mảng và x là gía trị cần tìm
result = search(arr, x)
if result == -1:
    print(f"Không tìm thấy ", x)
else:
    print(f"{x} được tìm thấy tại {result}")




#Sắp xếp chèn:
def insertionSort(arr):
    n = len(arr)
    # Duyệt qua từng phần tử của danh sách mảng
    for i in range(n):
        # duyệt qua các phần tử J và giảm dần
        for j in range(n-i-1):
            #print(j, end=" ")
            # So sánh nếu J lớn hơn J +1 thì hoán đổi vị trí
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arrSort = [27, 93, 32, 76, 19, 56, 36]

insertionSort(arrSort)
for i in range(len(arrSort)):
    print( arrSort[i], end=" ")