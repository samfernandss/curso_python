# or, and, is e not
ativo = True
logado = False

if ativo is True:
    print("tudo certo, sua conta está ativa")
else:
    print("você precisa ativar seu perfil")

if not (ativo and logado):
    print("há um erro na sua conta, tente novamente")
    logado = True

if logado is True:
    print("agora sim, 100% certo")
