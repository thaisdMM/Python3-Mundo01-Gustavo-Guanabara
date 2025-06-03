import urllib.error
import urllib.request


try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")

except urllib.error.URLError:
    print(f"O site Pudim não está acessivel no momento.")

else:
    print(f"Consegui acessar o site do Pudim com sucesso.")
    # para acessar o conteudo HTML do site inteiro que vc acabou de acessar
    print(site.read())
