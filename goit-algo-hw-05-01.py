class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return False
        self.table[key_hash].append([key, value])
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Видаляє пару ключ-значення.
        Якщо ключа немає — кидає KeyError.
        """
        key_hash = self.hash_function(key)
        for i, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                del self.table[key_hash][i]
                return
        raise KeyError(f"Ключ '{key}' не знайдено в HashTable")

    def __str__(self):
        
        return str(self.table)


if __name__ == "__main__":
    hash_table = HashTable(5)
    hash_table.insert("apple", 10)
    hash_table.insert("orange", 20)
    hash_table.insert("banana", 30)

    print(hash_table.get("apple"))   # 10
    print(hash_table.get("orange"))  # 20
    print(hash_table.get("banana"))  # 30

    hash_table.delete("apple")
    print(hash_table.get("apple"))   # None

    try:
        hash_table.delete("pear")
    except KeyError as error:
        print(error)  # Ключ 'pear' не знайдено в HashTable
