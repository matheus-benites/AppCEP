from cep_br import CepBr

cep = str(input())
objeto_cep = CepBr(cep)
objeto_cep_api = objeto_cep.api_via_cep()

print(objeto_cep_api)

92701270