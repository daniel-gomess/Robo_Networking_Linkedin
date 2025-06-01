# Robo Networking LinkedIn

Um robô em Python para automatizar o networking no LinkedIn, enviando solicitações de conexão personalizadas para pessoas com base em critérios de pesquisa definidos pelo usuário.

## Funcionalidades

- Login automatizado no LinkedIn
- Pesquisa de pessoas com base em um termo informado
- Envio de solicitações de conexão com mensagem personalizada
- Log em tempo real das ações realizadas na interface gráfica
- Respeito aos limites de uso do LinkedIn
- Tratamento de erros e exceções

## Como funciona

1. O usuário informa email, senha e termo de pesquisa na interface gráfica.
2. O robô faz login no LinkedIn com as credenciais fornecidas.
3. Realiza a busca de pessoas relacionadas ao termo informado.
4. Para cada perfil encontrado:
   - Gera uma mensagem personalizada
   - Envia a solicitação de conexão
   - Registra a ação no log da interface
5. Repete o processo até atingir o limite de conexões definido.

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/daniel-gomess/Robo_Networking_Linkedin.git
    cd Robo_Networking_Linkedin
    ```

2. (Opcional) Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    # ou
    source venv/bin/activate  # Linux/Mac
    ```

3. Instale as dependências:
    ```bash
    pip install selenium webdriver-manager customtkinter pyperclip pyautogui
    ```

4. Execute o programa:
    ```bash
    python layout.py
    ```

## Estrutura dos Arquivos

- `layout.py`: Interface gráfica para entrada de dados e exibição dos logs.
- `app.py`: Lógica de automação do LinkedIn utilizando Selenium.
- `README.md`: Este arquivo de instruções.

## Observações

- O robô utiliza o ChromeDriver, que é baixado automaticamente pelo `webdriver-manager`.
- O LinkedIn pode alterar seu layout ou bloquear automações, então o funcionamento pode variar ao longo do tempo.
- Use com responsabilidade e respeite as políticas do LinkedIn.
- Recomenda-se iniciar com limites baixos de conexões para evitar bloqueios.

## Exemplo de Mensagem Enviada

A mensagem personalizada enviada para cada conexão é:
```
Olá {nome}, Tudo bem? Estou buscando conexões com profissionais da área de Python, um pouco mais especificamente {termo_pesquisa} . Gostaria de me conectar com você!
```

## Licença

Este projeto é de uso pessoal e educacional. Não utilize para spam ou práticas que violem os Termos de Uso do LinkedIn.# LinkedIn Networking Bot

## Functionalities

- Automated login to LinkedIn
- Search for people based on defined criteria
- Send personalized connection requests
- Track sent invitations
- Respect LinkedIn's usage limits
- Handle errors and exceptions

## How it Works

1. The bot logs into LinkedIn using provided credentials
2. Searches for people based on specified criteria
3. For each profile found:
   - Checks if already connected/invitation sent
   - Generates personalized message
   - Sends connection request
   - Records the action
4. Implements delays between actions to avoid detection

## Installation

1. Clone this repository
2. Install required dependencies:
```
pip install selenium
pip install webdriver_manager
```
3. Configure credentials in config.py
4. Run the bot:
```
python main.py
```

## File Structure

```
Robo_Networking_Linkedin/
├── config.py
├── main.py
├── linkedin_bot.py
├── message_generator.py
└── utils/
    ├── logger.py
    └── helpers.py
```

## Observations

- Use responsibly and within LinkedIn's terms of service
- Recommended to run with lower limits initially
- Monitor acceptance rates and adjust messaging
- Keep credentials secure

## Example Message

"Hi [Name], I noticed we share interests in [Industry/Field]. I'd love to connect and learn more about your work in [Area]. Best regards, [Your Name]"

## License

This project is licensed under the MIT License.