# JSON2TOON - Commandes Essentielles

Guide de référence rapide pour toutes les commandes importantes.

---

## 📦 Installation

```bash
# Navigation
cd JSON2TOON

# Installation des dépendances
pip install -r requirements.txt

# Installation du package
pip install -e .

# Installation mode développement
pip install -e ".[dev]"
```

---

## ✅ Test de l'Installation

```bash
# Test rapide
python -c "from src.advanced_converter import convert_json_to_toon; print('✅ Installation réussie!')"

# Version Python
python --version  # Devrait être 3.10+

# Vérifier MCP
pip list | grep mcp
```

---

## 🧪 Tests

```bash
# Tous les tests
pytest tests/ -v

# Tests avec couverture
pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

# Tests spécifiques
pytest tests/test_converter.py -v
pytest tests/test_pattern_analyzer.py -v

# Test unique
pytest tests/test_converter.py::TestAdvancedConverter::test_simple_conversion_minimal -v

# Tests avec sortie détaillée
pytest tests/ -v -s

# Arrêt au premier échec
pytest tests/ -x

# Tests parallèles (si pytest-xdist installé)
pytest tests/ -n auto
```

---

## 🐍 Python - Utilisation Programmatique

### Conversion Basique

```python
from src.advanced_converter import convert_json_to_toon, convert_toon_to_json, CompressionLevel

# Données
data = {"id": 123, "name": "Test", "status": "active"}

# Conversion
toon = convert_json_to_toon(data, level=CompressionLevel.STANDARD)
original = convert_toon_to_json(toon)
```

### Analyse de Patterns

```python
from src.pattern_analyzer import AdvancedPatternAnalyzer

analyzer = AdvancedPatternAnalyzer()
patterns = analyzer.analyze(data)
strategy = analyzer.get_compression_strategy(data)
```

### Optimisation Intelligente

```python
from src.optimizer import SmartOptimizer

optimizer = SmartOptimizer()
result = optimizer.optimize(data, profile="balanced")
```

---

## 🎯 Exemples

```bash
# Exécuter tous les exemples
python examples/basic_usage.py

# Exécuter Python interactif avec imports
python -i -c "from src.advanced_converter import *; from src.pattern_analyzer import *"
```

---

## 🚀 Serveur MCP

### Démarrage Direct

```bash
# Démarrer le serveur
python -m src.mcp_server

# Avec logging debug
LOG_LEVEL=DEBUG python -m src.mcp_server

# En arrière-plan (Linux/Mac)
nohup python -m src.mcp_server > server.log 2>&1 &
```

### Configuration Claude Desktop

```bash
# Éditer la config
code ~/.config/Claude/claude_desktop_config.json

# Ou avec nano
nano ~/.config/Claude/claude_desktop_config.json

# Ou avec vim
vim ~/.config/Claude/claude_desktop_config.json
```

Ajouter :
```json
{
  "mcpServers": {
    "json2toon": {
      "command": "python",
      "args": ["-m", "src.mcp_server"],
      "cwd": "/chemin/complet/vers/JSON2TOON"
    }
  }
}
```

### Tester MCP

```bash
# Vérifier que le serveur démarre
python -m src.mcp_server --help 2>/dev/null || echo "Serveur démarre correctement"
```

---

## 🐳 Docker

### Construction

```bash
# Construire l'image
docker build -t json2toon:2.0.0 .

# Build avec cache désactivé
docker build --no-cache -t json2toon:2.0.0 .

# Build avec tag spécifique
docker build -t json2toon:latest -t json2toon:2.0.0 .
```

### Exécution

```bash
# Exécuter le conteneur
docker run -i json2toon:2.0.0

# Mode interactif
docker run -it json2toon:2.0.0 /bin/bash

# Avec variables d'environnement
docker run -i -e LOG_LEVEL=DEBUG json2toon:2.0.0

# Avec volume monté (développement)
docker run -it -v $(pwd)/src:/app/src json2toon:2.0.0
```

### Docker Compose

```bash
# Démarrer (production)
docker-compose up -d json2toon-server

# Démarrer (développement)
docker-compose --profile dev up json2toon-dev

# Arrêter
docker-compose down

# Voir les logs
docker-compose logs -f json2toon-server

# Reconstruire
docker-compose build --no-cache

# Démarrer avec reconstruction
docker-compose up -d --build
```

### Gestion Docker

```bash
# Lister les conteneurs
docker ps -a

# Arrêter un conteneur
docker stop json2toon-mcp-server

# Supprimer un conteneur
docker rm json2toon-mcp-server

# Lister les images
docker images | grep json2toon

# Supprimer une image
docker rmi json2toon:2.0.0

# Nettoyer tout
docker system prune -a
```

---

## 🔧 Développement

### Formatage de Code

```bash
# Formater tout le code
black src/ tests/ examples/

# Vérifier sans modifier
black --check src/ tests/

# Fichiers spécifiques
black src/advanced_converter.py
```

### Linting

```bash
# Linter tout le code
ruff src/ tests/ examples/

# Auto-fix
ruff --fix src/ tests/

# Fichiers spécifiques
ruff src/mcp_server.py
```

### Type Checking

```bash
# Vérifier les types
mypy src/

# Mode strict
mypy --strict src/

# Fichiers spécifiques
mypy src/advanced_converter.py
```

### Qualité Globale

```bash
# Tout vérifier en une commande
black src/ tests/ && ruff src/ tests/ && mypy src/ && pytest tests/ -v
```

---

## 📊 Métriques et Analyse

### Couverture de Code

```bash
# Générer rapport HTML
pytest tests/ --cov=src --cov-report=html

# Voir dans le navigateur
open htmlcov/index.html  # Mac
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Analyse de Performance

```python
import timeit

code = """
from src.advanced_converter import convert_json_to_toon, CompressionLevel
data = {"id": i, "name": f"Item {i}" for i in range(100)}
convert_json_to_toon(data, level=CompressionLevel.STANDARD)
"""

time = timeit.timeit(code, number=100)
print(f"Temps moyen: {time/100:.4f}s")
```

---

## 📦 Distribution

### Créer un Package

```bash
# Construire le package
python -m build

# Vérifier le package
twine check dist/*

# Upload sur PyPI (Test)
twine upload --repository testpypi dist/*

# Upload sur PyPI (Production)
twine upload dist/*
```

### Git

```bash
# Initialiser git (si pas déjà fait)
git init

# Ajouter tous les fichiers
git add .

# Commit initial
git commit -m "Initial commit - JSON2TOON v2.0.0"

# Ajouter remote
git remote add origin https://github.com/your-org/json2toon.git

# Push
git push -u origin master

# Tag version
git tag -a v2.0.0 -m "Version 2.0.0"
git push origin v2.0.0
```

---

## 🔍 Debugging

### Mode Debug Python

```bash
# Exécuter avec debugger
python -m pdb src/mcp_server.py

# Avec logging détaillé
LOG_LEVEL=DEBUG python -m src.mcp_server
```

### Logs

```bash
# Suivre les logs du serveur
tail -f server.log

# Logs Docker
docker logs -f json2toon-mcp-server

# Logs Docker Compose
docker-compose logs -f
```

### Tests de Performance

```python
from src.advanced_converter import AdvancedTOONConverter, CompressionLevel
import json
import time

data = [{"id": i, "value": i*10} for i in range(1000)]
converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)

start = time.time()
toon = converter.json_to_toon(data)
duration = time.time() - start

print(f"Temps: {duration:.4f}s")
print(f"Taille originale: {len(json.dumps(data))}")
print(f"Taille compressée: {len(toon)}")
```

---

## 🆘 Dépannage

### Problèmes d'Import

```bash
# Vérifier l'installation
pip show json2toon

# Réinstaller
pip uninstall json2toon
pip install -e .

# Vérifier PYTHONPATH
echo $PYTHONPATH  # Linux/Mac
echo %PYTHONPATH%  # Windows
```

### MCP ne Démarre Pas

```bash
# Vérifier Python
python --version

# Vérifier MCP
pip install --upgrade mcp

# Test direct
python -c "import mcp; print(mcp.__version__)"

# Vérifier config Claude
cat ~/.config/Claude/claude_desktop_config.json
```

### Tests Échouent

```bash
# Réinstaller dépendances de test
pip install -e ".[dev]"

# Nettoyer cache pytest
rm -rf .pytest_cache
rm -rf .mypy_cache
rm -rf __pycache__

# Relancer
pytest tests/ -v --tb=short
```

---

## 📚 Documentation

### Générer Documentation

```bash
# Avec sphinx (si installé)
cd docs
make html

# Ou avec pdoc
pip install pdoc
pdoc --html --output-dir docs/api src/
```

### Lire Documentation

```bash
# README
cat README.md | less

# Quick Start
cat QUICKSTART.md | less

# Changelog
cat CHANGELOG.md | less
```

---

## 🎯 Commandes Rapides Quotidiennes

```bash
# Développement quotidien
black src/ tests/ && ruff src/ tests/ && pytest tests/ -v

# Avant commit
black src/ tests/ && ruff --fix src/ tests/ && mypy src/ && pytest tests/ --cov=src

# Build Docker et test
docker-compose build && docker-compose up -d && docker-compose logs -f

# Déploiement
git add . && git commit -m "Update" && git push && git tag v2.0.1 && git push --tags
```

---

## 💡 Astuces

### Alias Utiles (ajouter à ~/.bashrc ou ~/.zshrc)

```bash
# Alias JSON2TOON
alias j2t-test='pytest tests/ -v'
alias j2t-format='black src/ tests/ examples/'
alias j2t-lint='ruff src/ tests/ examples/'
alias j2t-type='mypy src/'
alias j2t-all='black src/ tests/ && ruff src/ tests/ && mypy src/ && pytest tests/ -v'
alias j2t-server='python -m src.mcp_server'
alias j2t-examples='python examples/basic_usage.py'
alias j2t-docker='docker-compose up -d --build'
```

### Variables d'Environnement

```bash
# Pour développement
export JSON2TOON_DEV=1
export LOG_LEVEL=DEBUG
export PYTHONUNBUFFERED=1

# Pour tests
export PYTEST_TIMEOUT=30
export COVERAGE_RCFILE=.coveragerc
```

---

**Pour plus d'informations, consultez :**
- [README.md](README.md) - Documentation complète
- [QUICKSTART.md](QUICKSTART.md) - Démarrage rapide
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Résumé du projet
- [CHANGELOG.md](CHANGELOG.md) - Historique des versions

---

🚀 **Bon développement avec JSON2TOON !**
