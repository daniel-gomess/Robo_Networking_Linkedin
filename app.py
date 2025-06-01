from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
#import random
import pyperclip
import pyautogui

def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument('--lang=pt-BR')
    chrome_options.add_argument('--window-size=1200,800')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-gpu')

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


def login_linkedin(email, senha, log_fn):
    driver, wait = iniciar_driver()
    driver.get('https://www.linkedin.com/login')
    sleep(3)
    # driver.maximize_window()
    # sleep(2)

    try:
        wait.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(senha + Keys.RETURN)
        log_fn("\u2705 Login realizado com sucesso.")
        return driver, wait
    except Exception as e:
        log_fn(f"❌ Erro ao logar: {e}")
        driver.quit()
        return None, None

def buscar_e_conectar(driver, wait, termo_pesquisa, log_fn, limite_conexoes=20):
    try:
        campo_pesquisa = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Pesquisar')]")))
        campo_pesquisa.clear()
        campo_pesquisa.send_keys(termo_pesquisa)
        campo_pesquisa.send_keys(Keys.ENTER)
        sleep(3)

        botao_pessoas = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'search-reusables__filter-pill-button') and contains(., 'Pessoas')]")))
        botao_pessoas.click()
        log_fn("\U0001F465 Aba 'Pessoas' clicada.")
        sleep(3)

        conexoes_realizadas = 0

        while conexoes_realizadas < limite_conexoes:
            sleep(2)
            perfis = driver.find_elements(By.XPATH, '//li[@class="nrxCTNBwEvLjnjUMRDlltdOsOQfMBkCNfDFxZfpE"]')

            novas_conexoes = 0

            for perfil in perfis:
                if conexoes_realizadas >= limite_conexoes:
                    break

                try:
                    nome_elem = perfil.find_element(By.XPATH, './/span[contains(@dir, "ltr")]')
                    nome = nome_elem.text.strip().split('\n')[0]

                    sleep(1)

                    botao_conectar = perfil.find_element(By.XPATH, '//span[@class="artdeco-button__text" and text()="Conectar"]')
                    sleep(1)
                    botao_conectar.click()
                    sleep(1)

                    try:
                        botao_adicionar_nota = driver.find_element(By.XPATH, '//button[@aria-label="Adicionar nota"]')
                        botao_adicionar_nota.click()
                        sleep(1)

                        caixa_mensagem = driver.find_element(By.ID, 'custom-message')
                        caixa_mensagem.click()
                        mensagem = f"Olá {nome}, Tudo bem? Estou buscando conexões com profissionais da área de Python, um pouco mais especificamente {termo_pesquisa} . Gostaria de me conectar com você!"
                        caixa_mensagem.clear()
                        caixa_mensagem.send_keys(mensagem)
                        sleep(0.5)
                        
                        botao_enviar = driver.find_element(By.XPATH, '//button[@aria-label="Enviar convite"]')
                        botao_enviar.click()
                        sleep(1)
                    except:
                        botao_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enviar"]')))
                        botao_enviar.click()
                        sleep(1.5)

                    conexoes_realizadas += 1
                    novas_conexoes += 1
                    log_fn(f"🤝 {nome} foi adicionado com êxito! ({conexoes_realizadas}/{limite_conexoes})")
                    sleep(2)

                except Exception:
                    continue

            if novas_conexoes == 0:
                log_fn("⚠️ Nenhuma nova conexão encontrada nesta página.")
                break

            try:
                botao_proximo = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Avançar"]')))
                driver.execute_script("arguments[0].scrollIntoView(true);", botao_proximo)
                botao_proximo.click()
                log_fn("➡️ Próxima página clicada.")
                sleep(4)
            except:
                log_fn("🏋️ Fim das páginas ou botão 'Próximo' não encontrado.")
                break

        log_fn(f"✅ Processo finalizado. Total de conexões feitas: {conexoes_realizadas}")

    except Exception as e:
        log_fn(f"❌ Erro durante a busca: {e}")
        driver.quit()

