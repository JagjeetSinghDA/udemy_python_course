# fav_chais = [
#     "Masala Chai", "Green Tea", "Masala Chai",
#     "Lemon Tea", "Green Tea", "Elaichi Chai"
# ]


# uniq_chais = {chai for chai in fav_chais if len(chai) > 9}
# print(uniq_chais)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elachi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

uniq_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(uniq_spices)