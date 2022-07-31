# 연습1

# 연습2 - chaining 기법
# key값을 해쉬테이블에 같이 저장
hash_table = list(0 for _ in range(8))

def get_index(data):
    return hash(data)

def hash_func(key):
    return key % 8

def storage_data(data, value):
    index_key = get_index(data)
    hash_address = hash_func(index_key)
    print(data,'key:',index_key,'addr:',hash_address)
    # hash_table[hash_address] = value  # 연습1
    if hash_table[hash_address] != 0:
        for idx in range(len(hash_table[hash_address])):
            if hash_table[hash_address][idx][0] == index_key:
                hash_table[hash_address][idx][1] = value
                return # 끝났으니까
        # 다 돌았는데 같은 키가 없으면, 새로 추가
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def get_data(data):
    index_key = get_index(data)
    hash_address = hash_func(index_key)
    # return hash_table[hash_address]  # 연습1
    if hash_table[hash_address] != 0:  # 데이타가 있다면
        for stored_key, value in hash_table[hash_address]:
            # print(index_key, stored_key, value)
            if stored_key == index_key:
                return value
        return None
    else:
        return None

# 연습 3 - Close Hashing
def get_index3(data):
    return hash(data)

def hash_func3(key):
    return key % 8

def storage_data3(data, value):
    index_key = get_index(data)
    hash_address = hash_func(index_key)
    print(data,'key:',index_key,'addr:',hash_address)
    if hash_table[hash_address] != 0:
        for new_addr in range(hash_address, len(hash_table)):
            if hash_table[new_addr][0] == index_key:
                hash_table[new_addr][1] = value
                return
            if hash_table[new_addr] == 0:
                hash_table[new_addr] = [index_key, value]
    else:
        hash_table[hash_address] = [index_key, value]

def get_data3(data):
    index_key = get_index(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:  # 데이타가 있다면
        pass


storage_data3('Andy', '010-1111-2222')
storage_data3('Dave', '010-2222-3333')
storage_data3('Trump', '010-3333-4444')
storage_data3('Ann', '010-4444-5555')
storage_data3('aaa', '010-5555-6666')

print(hash_table)
print(get_data3('Andy'))
print(get_data3('Dave'))
print(get_data3('Trump'))
print(get_data3('Ann'))
print(get_data3('aaa'))