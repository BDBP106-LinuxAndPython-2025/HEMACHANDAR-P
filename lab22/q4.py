#!/usr/bin/python3

def track_calls(log_file="function_calls.log"):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            message = f"Function {func.__name__} called {count} times\n"
            with open(log_file, "a") as f:
                f.write(message)
            print(message.strip())
            return func(*args, **kwargs)
        return wrapper
    return decorator


@track_calls()
def greet(name):
    print(f"Hello, {name}!")

# Example calls
greet("HARIHARAN")
greet("SUMIRTHA")
greet("NAKULAN")
greet("HEMACHANDAR")
greet("HIMAKSHI")
greet("HARISH")
greet("CHIRU")
