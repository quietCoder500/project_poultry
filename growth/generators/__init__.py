ALL_GENERATORS = {}


def register(model: str):
    def decorator(func):
        ALL_GENERATORS.setdefault(model, []).append(func)
        return func

    return decorator
