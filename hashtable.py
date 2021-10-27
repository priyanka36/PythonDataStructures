class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self,key):
        h=0
        for char in key:
            h+= ord(char)
        return h%10

    def __setitem__(self,key,value):
        hash_value =self.get_hash(key)
        self.arr[hash_value] = val 

    def __getitem__(self,key,value):
        hash_value = self.get_hash(key)
        return self.arr[hash_value]

    def __delitem__(self,key,value):
        hash_value = self.get_hash(key)
        self.arr[hash_value]= None

print(get_hash("Priyanka"))