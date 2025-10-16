#collection module
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  

from collections import deque
d = deque([1,2,3])
d.appendleft(0)   
d.pop()          

from collections import Counter
cnt = Counter("banana")
print(cnt)  

from collections import defaultdict
dd = defaultdict(int)  
dd['a'] += 1
print(dd['a'], dd['b'])  


#intertools module
from itertools import count
for i in count(5, 2):
    if i > 15: break
    print(i, end=" ")  


from itertools import cycle
c = cycle("AB")
for _ in range(5):
    print(next(c), end=" ")  


from itertools import accumulate
import operator
nums = [1,2,3,4]
print(list(accumulate(nums))) 
print(list(accumulate(nums, operator.mul)))  


#functools module
from functools import reduce
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x*y, nums))  


from functools import partial
def power(base, exp): return base ** exp
square = partial(power, exp=2)
print(square(5))  

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
print(fib(30))
