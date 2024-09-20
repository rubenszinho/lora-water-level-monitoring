## Sobre o Projeto

Este projeto emprega a tecnologia LoRa para monitoramento eficaz de rios em zonas urbanas, com ênfase especial na prevenção e resposta a desastres naturais durante períodos de chuvas intensas. Construído de forma conteinerizada, o sistema é projetado para ser altamente portátil, permitindo fácil implantação em diferentes ambientes.

A arquitetura do projeto se divide em várias partes-chave:

- **Frontend (`lora-sensor-website`):** Responsável pela geração dos artefatos de interface de usuário, os quais são servidos pelo backend.
- **Backend (Server-Side):** Desenvolvido em Flask e conteinerizado via Docker, este componente assegura a entrega eficiente do frontend e o gerenciamento de dados.
- **Módulos de Comunicação LoRa (`lora-communication-modules`):** Contém o código para os módulos LoRa de envio e recepção, incluído como um submódulo.
- **Contêineres (Mosquitto, MongoDB, Server-Side):** Cada contêiner desempenha um papel crucial no sistema, desde o armazenamento de dados até a execução de serviços backend.

## Componentes do Projeto

- **Contêiner Mosquitto:** Implementação para armazenamento de dados dos sensores LoRa.
- **Contêiner Server-Side:** Configuração para os serviços de backend, rotas e entrega do frontend.
- **Submódulo `lora-sensor-website`:** Frontend para o sistema de monitoramento.
- **Submódulo `lora-communication-modules`:** Contém o código dos módulos LoRa de envio e recepção.

## Clonando o Repositório com Submódulos

Para garantir que todos os submódulos sejam clonados corretamente, use a flag `--recurse-submodules`:

```bash
git clone --recurse-submodules https://github.com/rubenszinho/lora-water-level-monitoring.git
```

Se você já clonou o repositório sem os submódulos, inicialize e atualize-os com:

```bash
git submodule update --init --recursive
```

## Automação da Configuração do Ambiente

O script de automação (`setup.sh`) simplifica a configuração do ambiente de contêineres. Para utilizá-lo:

1. **Navegue até o Diretório Raiz:** Certifique-se de estar no diretório raiz do repositório.
2. **Execute o Script:** Utilize o comando `./setup.sh` para iniciar a configuração automática dos contêineres.
   - Este processo inclui:
     - Parar e remover contêineres existentes (a menos que `--dirty` seja usado).
     - Criar e configurar a rede compartilhada (bridge network).
     - Iniciar os contêineres Mosquitto e MongoDB.
     - Verificar e atualizar o frontend no submódulo `lora-sensor-website`, reconstruindo-o se necessário.
     - Construir e iniciar o contêiner server-side.
3. **Opção Opcional `--dirty`:** Para evitar a reconstrução dos contêineres existentes, execute `./setup.sh --dirty`.

## Licença

Este projeto está licenciado sob a Licença GPL. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.