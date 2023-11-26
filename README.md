## Sobre o Projeto

Este projeto emprega a tecnologia LoRa para monitoramento eficaz de rios em zonas urbanas, com ênfase especial na prevenção e resposta a desastres naturais durante períodos de chuvas intensas. Construído de forma conteinerizada, o sistema é projetado para ser altamente portátil, permitindo fácil implantação em diferentes ambientes.

A arquitetura do projeto se divide em várias partes chave:

- **Frontend (`lora-sensor-website`):** Responsável pela geração dos artefatos de interface de usuário, os quais são servidos pelo backend.
- **Backend (Server-Side):** Desenvolvido em Flask e conteinerizado via Docker, este componente assegura a entrega eficiente do frontend e o gerenciamento de dados.
- **Contêineres (Mosquitto, MongoDB, Server-Side):** Cada contêiner desempenha um papel crucial no sistema, desde o armazenamento de dados até a execução de serviços backend.

## Componentes do Projeto

- **Mosquitto Container:** Implementação do container Mosquitto para armazenamento de dados de sensores LoRa.
- **Server-Side Container:** Configuração do container server-side para backend, rotas e serviço de frontend.
- **lora-sensor-website Submodule:** Adicionado o submodule lora-sensor-website para o frontend do sistema de monitoramento.

## Automação da Configuração do Ambiente

O script de automação (`setup.sh`) é uma parte integral do projeto, simplificando a configuração do ambiente de contêineres. Para utilizar:

1. **Posicionamento no Diretório:** Certifique-se de estar no diretório raiz do repositório.
2. **Execução do Script:** Utilize o comando `./setup.sh` para iniciar a configuração automática dos contêineres.
   - Isso inclui:
     - Parar e remover contêineres existentes (a menos que seja passado `--dirty`).
     - Criar e configurar a rede compartilhada (bridge network).
     - Iniciar contêineres Mosquitto e MongoDB.
     - Verificar e atualizar o frontend no submodule `lora-sensor-website`, reconstruindo-o se necessário.
     - Construir e iniciar o contêiner server-side.
3. **Uso da Opção `--dirty`:** Para evitar a reconstrução dos contêineres existentes, execute `./setup.sh --dirty`.
