
# 순서가 보장되는 딕셔러니 OrderedDict
from collections import OrderedDict

OrderedDict({'H':300, 'A':123})

# 3.5 이하는 순서가 보장되지 않고, A부터 시작한다고함.
dict = {'H':300, 'A':123}
dict
