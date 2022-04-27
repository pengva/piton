def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def validate_ip(ip):
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return False
    for i in ip_list:
        if i.isdigit() == False:
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True

def get_os():
    import platform
    os = platform.system()
    if os == "Darwin":
        return "Mac"
    else:
        return os
