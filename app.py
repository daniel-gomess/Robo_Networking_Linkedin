from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    wait = WebDriverWait(driver, 15)
    return driver, wait

def login_linkedin(email, senha):
    driver, wait = iniciar_driver()
    driver.get('https://www.linkedin.com/login')
    driver.maximize_window()
    sleep(3)

    try:
        wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(senha + Keys.RETURN)

        print("\u2705 Login realizado com sucesso.")
        return driver, wait

    except Exception as e:
        print(f"\u274C Erro ao logar: {e}")
        driver.quit()
        return None, None

def buscar_e_conectar(driver, wait, termo_pesquisa):
    try:
        campo_pesquisa = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Pesquisar')]")))
        campo_pesquisa.clear()
        campo_pesquisa.send_keys(termo_pesquisa)
        campo_pesquisa.send_keys(Keys.ENTER)
        sleep(3)

        botao_pessoas = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'search-reusables__filter-pill-button') and contains(., 'Pessoas')]")))
        botao_pessoas.click()
        print("\U0001f465 Aba 'Pessoas' clicada.")
        sleep(3)

        while True:
            sleep(2)
            conexoes = driver.find_elements(By.XPATH, '//button[contains(text(), "Conectar")]')
            nomes = driver.find_elements(By.XPATH, '//span[contains(@dir, "ltr") and contains(@class, "entity-result__title-text")]')

            print(f"\U0001f465 Encontradas {len(conexoes)} conexões possíveis nesta página.")

            for i in range(len(conexoes)):
                try:
                    nome = nomes[i].text.split("\n")[0].strip()
                    mensagem = f"Olá {nome}, estou buscando conexões com profissionais da área de {termo_pesquisa} para aumentar minhas conexões, expandir meu networking e trocar experiências. Gostaria de me conectar com você!"

                    driver.execute_script("arguments[0].scrollIntoView(true);", conexoes[i])
                    sleep(1)
                    conexoes[i].click()
                    sleep(2)

                    try:
                        adicionar_nota = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Adicionar nota"]')))
                        adicionar_nota.click()
                        sleep(1)

                        caixa_mensagem = wait.until(EC.presence_of_element_located((By.ID, 'custom-message')))
                        caixa_mensagem.send_keys(mensagem)

                        enviar = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar agora"]')))
                        enviar.click()

                        print(f"\u2705 Conexão enviada para {nome}")

                    except:
                        print(f"\u26a0\ufe0f Conexão enviada sem nota para {nome}")
                        enviar_simples = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar"]')))
                        enviar_simples.click()

                    sleep(2)

                except Exception as e:
                    print(f"\u274C Erro ao tentar conectar com {nome if 'nome' in locals() else 'desconhecido'}: {e}")
                    continue

            try:
                proximo = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Avançar"]')))
                driver.execute_script("arguments[0].scrollIntoView(true);", proximo)
                proximo.click()
                print("\u27a1️ Próxima página clicada.")
                sleep(4)
            except:
                print("🏋️ Fim das páginas ou botão 'Próximo' não encontrado.")
                break

    except Exception as e:
        print(f"\u274C Erro durante a busca: {e}")
        driver.quit()

# =========================
# 🔽 EXECUÇÃO DO SCRIPT 🔽
# =========================
if __name__ == "__main__":
    email = "SEU_EMAIL"
    senha = "SUA_SENHA"
    termo_busca = "Desenvolvedor Python"  # Defina aqui o termo desejado

    driver, wait = login_linkedin(email, senha)
    if driver and wait:
        buscar_e_conectar(driver, wait, termo_busca)
