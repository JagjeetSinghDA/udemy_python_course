from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(userrole):
        if userrole != "admin":
            print("Access Denied: Admins only")
            return None
        else:
            return func(userrole)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access granted to tea inventory")


access_tea_inventory("Manageer")
access_tea_inventory("Sr. Manageer")
access_tea_inventory("admin")