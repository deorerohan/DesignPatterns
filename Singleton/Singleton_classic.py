class Singleton():
    ans = None

    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()

        return Singleton._instance

    
if __name__ == '__main__':
    s1 = Singleton.instance()
    s2 = Singleton.instance()

    print(f'{s1} : {s2}')