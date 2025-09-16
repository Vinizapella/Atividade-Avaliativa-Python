pessoas = [
    {"nome": "Ana", "idade": 28},
    {"nome": "Bruno", "idade": 22},
    {"nome": "Carla", "idade": 35}
]
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
print(pessoas_ordenadas)