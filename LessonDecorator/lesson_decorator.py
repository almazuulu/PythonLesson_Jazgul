def decorator(f):
    def wrapper(*args, **kwargs):
        res = f(*args)
        
        with open('hello.txt', "w", encoding="utf8") as f:
            f.write(res)
            f.write('\n')
            
    return wrapper
    
@decorator
def say_hello(n):
    result_txt = f"Hello {n}!"
    return result_txt
    
@decorator
def math_func(n1, n2):
    result_math = f"Результат сложения:{n1 + n2}"
    return result_math
    

say_hello("Elena")

