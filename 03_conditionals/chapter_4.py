# smart thermo stat:

device_status = "active"
temperature = 38

if device_status == 'active':
    if temperature > 35:
        print(f"High Temperature Alert.")
    else:
        print("Normal Temparature")
else:
    print("Device is Offline")
