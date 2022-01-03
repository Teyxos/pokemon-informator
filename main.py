import requests
import inquirer


def main():
    poke = input("Of what pokemon you want info? Id or Name \n").lower()
    check_info(poke)


def check_info(pokemon) -> dict:
    data = {}
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    if req.status_code == 200:
        data = req.json()
    elif req.status_code == 404:
        print("Bad pokemon")
    else:
        print("Unkown error!")

    return data


def give_info(data) -> str:
    pass


main()


# questions = [
#     inquirer.List(
#         "size",
#         message="What size do you need?",
#         choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
#     ),
# ]
# answers = inquirer.prompt(questions)
# print(answers["size"])
