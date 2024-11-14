import requests
def converter_moeda(valor, de, para):
    url = f"https://v6.exchangerate-api.com/v6/0aed368c982486d11343b2e6/latest/{de}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if 'conversion_rates' in dados:
            taxa = dados['conversion_rates'].get(para)
            if taxa:
                resultado = valor * taxa
                return round(resultado, 2)  # Arredonda para 2 casas decimais
            else:
                print(f"Erro: A moeda {para} não foi encontrada.")
                return None
        else:
            print("Erro: Não foi possível acessar as taxas de conversão.")
            return None
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return None
valor = 100 
de = 'USD'
para = 'BRL'
resultado = converter_moeda(valor, de, para)
if resultado is not None:
    print(f"{valor} {de} equivale a {resultado:.2f} {para}")