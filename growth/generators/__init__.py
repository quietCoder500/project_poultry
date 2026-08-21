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
class TextCard(ABC):
    title = "Default Title"

    @classmethod
    def generate(cls, text):
        return render_to_string(
            "growth/cards/text_card.html",
            context={"title": cls.title, "text_content": text},
        )

    @abstractmethod
    def render(self):
        pass


class GraphCard(ABC):
    title = "Default Title"

    def generate(self, chart, data_points):
        return render_to_string("growth/cards/graph_cart.html")

    @abstractmethod
    def render(self):
        pass
