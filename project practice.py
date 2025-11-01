
def calculator():
    print('欢迎使用简单计算器!')
    print("可用运算符：+、-、*、/、%（取余）、**（幂）")
    print("="*40)

    calculation_count=0
    while calculation_count<10:
        calculation_count+=1
        print(f"\n第{calculation_count}次计算")

        try:
            num1_input=input("请输入第一个数字：")
            num1 = float(num1_input)

            operator = input("请输入运算符 (+, -, *, /, %, **): ")

            num2_input = input("请输入第二个数字: ")
            num2 = float(num2_input)

            result = None

            if operator == "+":
                result = num1 + num2
                print(f"执行加法运算: {num1} + {num2}")

            elif operator == '-':
                result = num1 - num2
                print(f"执行减法运算: {num1} - {num2}")

            elif operator == '*':
                result = num1 * num2
                print(f"执行乘法运算: {num1} * {num2}")

            elif operator == '/':

                if num2 == 0:
                    print("错误：不能除以 0")
                    continue

                result = num1 / num2
                print(f"执行除法运算: {num1} / {num2}")

            elif operator == '%':

                if num2 == 0:
                    print("错误：取余运算的除数不能为 0")
                    continue

                result = num1 % num2
                print(f"执行取余运算: {num1} % {num2}")

            elif operator == '**':
                result = num1 ** num2
                print(f"执行幂运算: {num1} ** {num2}")

            else:
                print("无效的运算符，请重新输入。")
                continue

            if result is not None:

                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                print(f"计算结果: {num1} {operator} {num2} = {result}")
                print("=" * 40)

        except ValueError:
            print("错误：请输入有效的数字！")
            continue

        except KeyboardInterrupt:

             print("\n成功捕获KeyboardInterrupt异常！程序优雅退出。")
             break


        if calculation_count < 10:
            choice = input("是否继续计算？(y/n): ").lower()
            if choice == 'n' or choice == 'no':
                print("退出计算器。")
                break
            elif choice != 'y' and choice != 'yes':
                print("输入不明确，默认继续计算。")

        else:
            print("已达到最大计算次数(10次)，自动退出。")
            break

    print(f"\n感谢使用！您共进行了 {calculation_count - 1 if calculation_count > 0 else 0} 次计算。")

if __name__ == "__main__":
    calculator()

























    