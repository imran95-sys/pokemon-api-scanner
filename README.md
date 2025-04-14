# 🧪 Pokémon API Scanner

This is a command-line tool that fetches and displays information about a specified Pokémon using the PokéAPI.

## 🔍 Features

- Get details like:
  - Pokémon Name
  - Base Experience
  - Height
  - Weight
  - Abilities

- JSON formatted output

## 🛠️ Requirements

- Python 3
- `requests` library

## 🚀 How to Run

```bash
python3 pokemon_scanner.py <pokemon-name>

Example:

python3 pokemon_scanner.py pikachu

✅ Sample Output:

{
    "name": "pikachu",
    "base_experience": 112,
    "height": 4,
    "weight": 60,
    "abilities": [
        "static",
        "lightning-rod"
    ]
}


PokéAPI Official Site


---

## ✅ To Update README.md in EC2:

1. Run:
   ```bash
   nano README.md
