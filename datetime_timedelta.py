from datetime import datetime
from datetime import timedelta

y = int(input("Digite quantos dias a mais do atual: "))

x = datetime.now() + timedelta(days=y)
print(x.strftime("%A, %B %d, %Y"))