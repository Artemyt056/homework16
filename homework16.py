def stringify_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)

    return wrapper


@stringify_result
def plus(value1, value2):
    return value1 + value2


result = plus(10, 20)
print(result)
