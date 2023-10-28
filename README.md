# Atividade avaliativa - CHAT [PUB/SUB] cenectado ao RedisDB
## Instruções de configuração e execução:
### * Baixe o código para sua máquina
### * Verifique se o python3 está instalado em sua máquina
### * Configure o ambiente virtualizado VENV 

// Para instalar o ambiente virtual

```python
pip install virtualenv
py -m venv venv
```

// Para ativar o ambiente virtual

```python
source venv/Scripts/activate (windows)
source venv/bin/activate (linux/mac OS)
```

```python
pip install -r requirements.txt
```

```flask
pip install flask
```

```DateTime
pip install DateTime
```

```Redis
pip install redis
```

### * Abra o redis ataves do comando redis-cli no seu terminal, após isso digite: subscribe chat. Com isso o redis estará pronto exibir as capturas dos chats
### * Execute o comando: python3 app.py dentro do diretório do repositório baixado. Esse comando roda a funcao principal que carrega a pagina de login[subscricao] por nome no chat.
### * A partir dessa etapa abra quantas abas com sessoes diferentes quiser e digite na barra de endereços: 127.0.0.1:5000 e ENTER (Abas privadas criam sessoes diferente no mesmo browser)
### * Depois de entrar com seu nome e pressionar ENTER, sera redirecionado a pagina do chat onde podera digitar e enviar quantas mensagens quiser para todos que estao conectados com a tecla ENTER.
