import sys

def process_file(filename, operation):
    try:
        # 读取文件内容并转换为浮点数列表
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]

        # 根据操作类型执行累加、累减、累乘、累除
        if operation == 'add':
            result = sum(numbers)
        elif operation == 'minus':
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif operation == 'multiply':
            result = 1
            for num in numbers:
                result *= num
        elif operation == 'divide':
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    raise ValueError("Cannot divide by zero.")
                result /= num
        else:
            raise ValueError("Invalid operation. Use 'add', 'minus', 'multiply', or 'divide'.")

        print(f"The result of '{operation}' operation is: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <operation>")
    else:
        filename = sys.argv[1]
        operation = sys.argv[2]
        process_file(filename, operation)
