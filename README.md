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


## ✅ Scenario 3: Deploying Pokémon Scanner with Helm on Minikube

This scenario demonstrates deploying the containerized Pokémon Scanner using **Helm** on a **local Minikube Kubernetes cluster**.

### 📁 Helm Chart Location

The Helm chart is located in:

helm/pokemon-scanner-chart/


### 🛠 Deployment Steps

1. **Start Minikube:**
```bash
minikube start --driver=docker --cpus=2 --memory=2200mb

Install the Helm chart:

cd helm/pokemon-scanner-chart
helm install pokemon-scanner .

Verify the pod is running:

kubectl get pods
Manually exec into the container:

kubectl exec -it <pod-name> -- /bin/sh

Run the scanner manually (example):
python3 pokemon_scanner.py pikachu

🐳 Docker Image
Image used in the deployment:

📦 dock981/pokemon-scanner
