import json

planks = "oak_planks, spruce_planks, birch_planks, jungle_planks, acacia_planks, dark_oak_planks, crimson_planks, warped_planks, mangrove_planks, bamboo_planks‌, cherry_planks‌".split(", ")

for plank in planks:
    type = plank.split("_")[0]
    with open(f"./src/datapack/data/wood_recipes/recipes/chest_boat/{type}_chest_boat.json", "w") as file_ref:
        json.dump(
            {
                "type": "crafting_shaped",
                "pattern": [
                    "121",
                    "111"
                ],
                "key": {
                    "1": {
                        "item": plank
                    },
                    "2": {
                        "tag": "c:chests/wooden"
                    }
                },
                "result": {
                    "item": "minecraft:chest",
                }
            },
            file_ref,
            indent=2
        )