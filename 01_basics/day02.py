# day02.py

# 1. list
# 2. tuple
# 3. dictionary
# 4. set
# 5. string
# 6. if
# 7. for / while
# 8. break / continue / pass
# 9. list comprehension
# 10. built-in function
# 11. module import
# 12. user-defined function
# 13. recursion / scope

# =========================
# 1. LIST
# =========================

# 01) basic example

numbers = [10, 20, 30, 40]

print("전체 리스트:", numbers)

print("첫 번째 값:", numbers[0])
print("세 번째 값:", numbers[2])


# 02) edit possible

numbers = [10, 20, 30, 40, 50, 60]

numbers[1] = 200

print(numbers)


# 03) list slicing

print("slicing : ", numbers[1:4])


# 04) major list funtion

#append	뒤에 추가
numbers = [1, 2, 3]
numbers.append(4)
print("append : ",numbers)

#insert	위치 지정 추가
numbers.insert(1, 10000)
print("insert : ",numbers)

#pop	마지막 삭제
numbers.pop()
print("pop : ",numbers)

#remove	특정값 삭제
numbers.remove(2)
print("remove : ",numbers)

#len	길이
print("len : ", len(numbers))