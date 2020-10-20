
import random


def roll(nmsg):
    try:
        msg = nmsg.strip().lower()
        if msg[0] == "/":
            space = msg.find(" ")
            dados = msg[space:].strip().split('d')
            rolls = []
            soma = 0
            for c in range(0, int(dados[0]), 1):
                r = random.randint(1, int(dados[1]))
                rolls.append(r)
                soma += r
            inicial = msg[msg.find(" "):].strip()
        return f"[BOT] Resultado de {inicial}: {soma} // {rolls}"
    except:
        return "Erro no Comando! faça corretamente. Exemplos: /roll 3d6, /r 2d10, /role 5d10 "


print(roll("/roll 3d6"))
