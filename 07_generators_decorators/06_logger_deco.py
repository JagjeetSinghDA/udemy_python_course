from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished: {func.__name__}")
        return result
    return wrapper


@log_activity
def brew_chai(type, Milk=True, Sugar=False, intensity="Strong"):
    print(f"Brewing {type} chai which have milk {Milk}, sugar {Sugar} and intensity {intensity}")


brew_chai("Masala", Milk=True, Sugar=False, intensity="Medium")