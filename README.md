# Monitoramento de Status das Bolinhas

Este é um script Python que monitora o status das bolinhas em um site específico e envia um GET/heartbeat para um serviço externo caso todas as bolinhas estejam verdes.

## Configuração

Antes de usar o script, você precisará configurar algumas variáveis de ambiente e bibliotecas.

### Bibliotecas Necessárias

- `logging`: Biblioteca para configurar o log do script.
- `time`: Biblioteca para lidar com temporizações.
- `requests`: Biblioteca para fazer solicitações HTTP.
- `BeautifulSoup`: Biblioteca para analisar o conteúdo HTML da página.

## Configuração de Log

O log do script está configurado para ser registrado em um arquivo chamado `status_bolinhas.log`. Ele incluirá informações relevantes, como timestamps e níveis de log.

## URL do Site

Você precisa definir a URL do site que contém as bolinhas a serem monitoradas. Neste código, a URL é definida como:

```python
url = "http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=2.00"
```

#### URL para Enviar GET/heartbeat

Uma URL específica é usada para enviar o GET/heartbeat para um serviço externo. Certifique-se de configurar corretamente esta URL antes de executar o script:
```python
get_url = "https://uptime.betterstack.com/api/v1/heartbeat/XXXXXXXXXX"
````

### Funcionamento
O script faz o seguinte:

1. Realiza uma solicitação GET à URL especificada.
2.  Analisa o conteúdo da página usando a biblioteca BeautifulSoup para encontrar as imagens das bolinhas.
3. Verifica o status de cada bolinha com base no nome do arquivo da imagem.
4. Se pelo menos uma bolinha estiver amarela ou vermelha, o script indica que o serviço está com problemas.
5. Se todas as bolinhas estiverem verdes, o script envia um GET/heartbeat para a URL especificada e registra o sucesso ou qualquer erro.

###  Execução
O script entra em um loop principal que verifica o status das bolinhas e envia o GET/heartbeat em intervalos regulares (a cada 10 segundos). Você pode interromper a execução do script a qualquer momento pressionando Ctrl + C.

Lembre-se de que este é um exemplo simples e pode ser necessário ajustar o código de acordo com suas necessidades específicas. Certifique-se também de que as bibliotecas necessárias estejam instaladas antes de executar o script.
