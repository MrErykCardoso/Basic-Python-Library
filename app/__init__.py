from flask import Flask

#Algoritmo de inicialização da aplicação

def create_app():
    app = Flask(__name__) #-> Variável de inicialização da aplicação
    
    #Configuração do ambiente
    app.config.from_object("app.config.Config")
    
    #Blueprints, DB, etc..
    
    return app