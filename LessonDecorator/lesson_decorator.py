def file_decorator(filename):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            res = fun(*args, **kwargs)
            
            with open(filename, "w", encoding="utf8") as f:
                f.write(res)
                f.write('\n')
                
            return res
                
        return wrapper
    return decorator
    
@file_decorator("hello.txt")
def say_hello(n):
    result_txt = f"Hello {n}!"
    return result_txt
    
@file_decorator("math.txt")
def math_func(n1, n2):
    result_math = f"Результат сложения:{n1 + n2}"
    return result_math

    
say_hello("Elena")
math_func(15, 20)

