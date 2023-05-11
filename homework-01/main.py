from cache import LRUCache

cache = LRUCache(100)
print("set('Jesse', 'Pinkman')")
cache.set('Jesse', 'Pinkman')
print("set('Walter', 'White')")
cache.set('Walter', 'White')
print(cache.data)

print("\nset('Jesse', 'James')")
cache.set('Jesse', 'James')
print(cache.data)

print("\nget('Jesse')")
print("Output:", cache.get('Jesse')) # вернёт 'James'

print("\nrem('Walter')")
cache.rem('Walter')
print("get('Walter')")
print("Output:", cache.get('Walter')) # вернёт ''
print(cache.data)

