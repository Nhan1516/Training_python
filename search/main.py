
#====================>Tìm kiếm tuyến tính:
# def search(arr, x):
#     # Duyệt qua tùng phần tử của danh sách
#     for i in range(len(arr)):
#         #so sánh x với từng phần tử trong mảng, nếu bằng thì trả về giá trị i không có giá trị nào bằng thì trả -1,
#         #chuyển đổi kiểu dữ liệu x thành int do inout trả về str
#         if arr[i] == int(x):
#             return i
#     return -1

# arr = [0,1,4,6,9,10,16]
# x = input("Tìm kiếm: ")

# #gọi hàm search truyền vào arr là danh sách mảng và x là gía trị cần tìm
# result = search(arr, x)
# if result == -1:
#     print(f"Không tìm thấy ", x)
# else:
#     print(f"{x} được tìm thấy tại {result}")




#============> SẮP XẾP CHÈN
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
    return arr


# arr = insertionSort(arrSort)
# print(arr)


#===============> TÌM KIẾM NHỊ PHÂN
def binary_search(arr, x):
    # khởi tạo các chỉ mục
    x = int(x)
    low = 0
    high = len(arr) -1
    mid = 0

    # Duyệt mảng bằng vòng lặp
    while low <= high:
        mid = (low + high) // 2
        # nếu arr[mid] nhỏ hơn x thì gía trị cần tìm nằm phải của mảng và chuyển sang tìm nữa bên phải của mảng 
        if arr[mid] < x:
            low = mid + 1
        # nếu arr[mid] lớn hơn x thì gía trị cần tìm nằm trái của mảng và chuyển sang tìm nữa bên trái của mảng 
        elif arr[mid] > x:
            high = mid -1
        # lặp lại cho đến khi tìm được arr[mid] bằng với x và return ra mid
        else:
            return mid
    # không tìm được mid trông mảng
    return -1

#arrBinary = [0, 2, 6, 9, 19, 28, 37, 49]
arrSort = [27, 93, 32, 76, 19, 56, 36, 78, 92, 23, 4]

#=============> TÌM KIẾM NHỊ PHÂN KẾT HỢP SẮP XẾP CHÈN
x = input('Tìm kiếm: ')
arrBinary = insertionSort(arrSort)
print(arrBinary)
resul = binary_search(arrBinary, x)
print(resul)