class Singleton:
    _instance: "Singleton" = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    assert s1 is s2
