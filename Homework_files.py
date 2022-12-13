#!/usr/bin/python
#  -*- coding: utf-8 -*-

from pprint import pprint
from typing import Optional, Union


def str_to_int(string: str) -> Optional[int]:
    try:
        return int(string)
    except:
        ...


cook_book = {}

with open("test.txt", "r") as file:
    file_data = file.readlines()
    for index, attrib in enumerate(file_data):
        if type(str_to_int(attrib)) is int:
            dish_ingredients = cook_book[file_data[index - 1].strip()] = []

            for i in range(str_to_int(attrib)):
                ingredient_attrib = [
                    attrib.strip() for attrib in file_data[index + i + 1].split("|")
                ]

                dish_ingredients.append(
                    {
                        "ingredient_name": ingredient_attrib[0],
                        "quantity": int(ingredient_attrib[1]),
                        "measure": ingredient_attrib[2],
                    }
                )

# pprint(cook_book)
def get_shop_list_by_dishes(
    dishes: list[str], person_count: int
) -> dict[str, dict[str, Union[str, int]]]:
    data: dict = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                data[ingredient["ingredient_name"]] = {
                    "measure": ingredient["measure"],
                    "quantity": ingredient["quantity"] * person_count,
                }

    return data


# pprint(get_shop_list_by_dishes(["Фахитос", "Утка по-пекински"], 2))

import os


def join_files(dir_path: str) -> None:
    data = []
    for file_name in os.listdir(dir_path):
        file_path = f"{dir_path}/{file_name}"

        file_data = f"{file_name}\n"
        with open(file_path, "r") as fh:
            read_file = fh.readlines()
            for line_index, _ in enumerate(read_file, start=1):
                file_data += (
                    f"Строка номер {line_index} файла номер {file_name.split('.')[0]}\n"
                )
            data.append({"count": len(read_file), "data": file_data})
    data = sorted(data, key=lambda item: item["count"])
    with open("result.txt", "w") as fh:
        for item in data:
            fh.writelines(item["data"])

