class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = "  water ,  milk,    ginger ,     honey    "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)

# these are statuc objects and we can use them wiothout creating the object witht he class