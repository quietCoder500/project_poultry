from abc import ABC, abstractmethod

from django.template.loader import render_to_string

ALL_GENERATORS = {}


def register(model: str):
    def decorator(cls):
        ALL_GENERATORS.setdefault(model, []).append(cls)
        return cls

    return decorator


#
# Abstract Widget types
#
class BaseTextCard(ABC):
    title = "Base Text Card Title"

    @classmethod
    def generate(cls, text):
        return render_to_string(
            "growth/cards/text_card.html",
            context={"title": cls.title, "text_content": text},
        )

    @classmethod
    @abstractmethod
    def render(cls, project):
        pass


class BaseGraphCard(ABC):
    title = "Base Graph Card Title"

    def generate(self, chart, data_points):
        return render_to_string("growth/cards/graph_cart.html")

    @classmethod
    @abstractmethod
    def render(cls, project):
        pass
