from typing import Union

import conexao
import filmesApi
import seriesApi

import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/filmes")
def getFilmes():
    buscarFilmes()
    filmes = []
    for filme in conexao.collection.find():
        filmes.append({"nome": filme["nome"],
                       "tipo": filme["tipo"]})
    return filmes

@app.get("/series")
def getSeries():
    buscarSeries()
    series = []
    for serie in conexao.collection.find():
        series.append({"nome": serie["nome"],
                       "tipo": serie["tipo"]})
    return series


def buscarFilmes():
    filmes = []
    filmesNovos = []
    for filme in conexao.collection.find():
        if filme["tipo"] == "filme":
            filmes.append({"nome": filme["nome"],
                       "tipo": filme["tipo"]})
    if not filmes:
        for filme in filmesApi.filmes:
            if filme["tipo"] == "filme":
                filmes.append({"nome": filme["nome"],
                               "tipo": filme["tipo"]})
        conexao.collection.insert_many(filmes)

    else:
        for filme in filmesApi.filmes:
            if filme["tipo"] == "filme":
                query = {"nome": filme["nome"], "tipo": filme["tipo"]}
                for catalogo in conexao.collection.find(query):
                    filmes.append({"nome": catalogo["nome"],
                                   "tipo": catalogo["tipo"]})
                if filme["nome"] not in catalogo["nome"]:
                    filmesNovos.append({"nome": filme["nome"],
                                        "tipo": filme["tipo"]})
        if filmesNovos:
            conexao.collection.insert_many(filmesNovos)


def buscarSeries():
    series = []
    seriesNovos = []
    for serie in conexao.collection.find():
        if serie["tipo"] == "serie":
            series.append({"nome": serie["nome"],
                       "tipo": serie["tipo"]})
    if not series:
        for serie in seriesApi.series:
            print("flag 2")
            print(serie)
            if serie["tipo"] == "serie":
                series.append({"nome": serie["nome"],
                               "tipo": serie["tipo"]})
        conexao.collection.insert_many(series)

    else:
        for serie in seriesApi.series:
            if serie["tipo"] == "serie":
                query = {"nome": serie["nome"], "tipo": serie["tipo"]}
                for catalogo in conexao.collection.find(query):
                    series.append({"nome": catalogo["nome"],
                                   "tipo": catalogo["tipo"]})
                if serie["nome"] not in catalogo["nome"]:
                    seriesNovos.append({"nome": serie["nome"],
                                        "tipo": serie["tipo"]})
        if seriesNovos:
            conexao.collection.insert_many(seriesNovos)
