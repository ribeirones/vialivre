# Vialivre

## Configuração do ambiente

Siga os passos abaixo para executar a aplicação em seu computador.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Para iniciar a API

```
flask db upgrade
flask fake vias 10
flask run
```
