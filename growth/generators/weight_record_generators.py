from growth.generators import register, GraphCard, TextCard, ALL_GENERATORS


@register("growth.WeightRecord")
class AverageWeight(TextCard):
    title = "Average Weight of Flock"

    def render(self):
        return self.generate("3 Lbs. 6 oz.")


print(ALL_GENERATORS)


@register("growth.WeightRecord")
class AverageDailyGain(TextCard):
    title = "Average Daily Gain of Flock"

    def render(self):
        return self.generate("4.65 oz/day")
