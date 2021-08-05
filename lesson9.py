import random
from string import ascii_lowercase as alphabet


def create_email(domains, names):
    domain = random.choice(domains)
    name = random.choice(names)
    number = random.randint(100, 999)
    len_str = random.randint(5, 7)
    rand_str_list = [random.choice(alphabet) for _ in range(len_str)]
    rand_str = "".join(rand_str_list)
    return f"{name}.{number}@{rand_str}.{domain}"


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
