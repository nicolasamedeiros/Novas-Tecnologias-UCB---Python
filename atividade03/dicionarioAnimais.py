animais = {
    "Bob": {"tipo": "Cachorro", "dono": "João"},
    "Rex": {"tipo": "Cachorro", "dono": "Maria"},
    "Mimi": {"tipo": "Gato", "dono": "Carlos"},
    "Nemo": {"tipo": "Peixe", "dono": "Ana"}
}


for nome_animal, info_animal in animais.items():
    print("Nome:", nome_animal)
    print("Tipo:", info_animal["tipo"])
    print("Dono:", info_animal["dono"])
    print()  
