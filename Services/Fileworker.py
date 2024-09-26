def processing(datafield, change_value=None):
    res = None
    lines = []
    with open("config.ini", "r") as f:
        lines = [i.strip() for i in f.readlines()]

    with open("config.ini", "w") as f:
        for line in lines:
            field, value = line.split("=")
            if field == datafield:
                res = value
                if change_value:
                    f.write(f"{field}={change_value}\n")
                else:
                    f.write(f"{field}={value}\n")
            else:
                f.write(f"{field}={value}\n")

    if res: return res
    return "No data find"