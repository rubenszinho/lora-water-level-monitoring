# Use a imagem oficial do Eclipse Mosquitto como base
FROM eclipse-mosquitto:latest

# Copie o arquivo de configuração personalizado para o contêiner
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Copie o arquivo de senhas (se necessário) para o contêiner
COPY passwd /mosquitto/config/passwd

# Defina o ponto de entrada e o comando padrão (opcional se você estiver satisfeito com os padrões do Mosquitto)
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]

# Exponha a porta padrão do MQTT
EXPOSE 1883

# Configure um volume para dados persistentes
VOLUME ["/mosquitto/data"]
