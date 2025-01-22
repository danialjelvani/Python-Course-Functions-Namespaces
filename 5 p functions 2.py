# check validation:


def check_validation(user_pass: dict):
    """
    check user pass validation

    :Param: user_pass: a dictionary of user & pass
    :return: list of validated users
    """
    accepted_user = []

    for k, v in user_pass.items():
        if len(k) >= 4:
            if len(v) >= 6:
                if v.lower() != v:
                    if v.isdigit() is not True:
                        accepted_user.append([k])
    print(accepted_user)


user_pass_dic = {
    'ali': 'fsD456',
    'alireza': '4564545',
    'danial': 'D45vvds',
    'danial4': 'cF45',
}

check_validation(user_pass_dic)


# baresi Upper Lower ba All va Any jalebe:

a = [True if char in '0123456789' else False for char in 'ay5']
print(a)
print(all(a))
# age true midad yani numeric bud kamel

b = [char.isupper() for char in 'aAa']
print(b)
print(any(b))
