import requests
import inquirer


def main():
    poke = input("Of what pokemon you want info? Id or Name \n").lower()
    data = check_info(poke)

    result = give_info(data)

    for data in result:
        print(data)


def check_info(pokemon) -> dict:
    data = {}
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    if req.status_code == 200:
        data = req.json()
    elif req.status_code == 404:
        print("Bad pokemon")
        exit(0)
    else:
        print("Unkown error!")
        exit(0)

    return data


def give_info(data) -> str:
    questions = [
        inquirer.Checkbox(
            "data_requested",
            message="What data are you interested in?",
            choices=["Name", "Id", "Weight", "Abilities"],
        ),
    ]

    answers = inquirer.prompt(questions)

    result = []
    for prop in answers["data_requested"]:
        prop = prop.lower()

        if prop == "name":
            result.append(f"Name: {data[prop].capitalize()}")
        elif prop == "id":
            result.append(f"Id: {data[prop]}")
        elif prop == "weight":
            result.append(f"Weight: {data[prop]}")
        elif prop == "abilities":
            for ability in data[prop]:
                result.append(f"Ability: {ability['ability']['name'].capitalize()}")

    return result


main()
