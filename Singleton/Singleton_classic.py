class Singleton():
    _instance = {}

    def __new__(cls):
        if cls not in cls._instance:
            instance = super().__new__(cls)
            cls._instance[cls] = instance

        return cls._instance[cls]

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    print(f'{s1} : {s2}')