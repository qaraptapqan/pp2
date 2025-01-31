from _7 import has_33
from _4 import is_prime, filter_prime


has_33("313213213312")
has_33("33333333333111111111233")

print(f'{is_prime(13) = } \n{is_prime(357) = }')

print(' '.join(map(str, filter_prime([1,2,3,4,5,6,13,213,31235,213451,313151]))))
