<kbd>[<img title="Português (Brasil)" alt="Português (Brasil)" src="https://cdn.statically.io/gh/hjnilsson/country-flags/master/svg/br.svg" width="22">](README.pt_br.md)</kbd>

## About the Project

This project utilizes LoRa technology for effective monitoring of rivers in urban areas, with a special emphasis on prevention and response to natural disasters during periods of heavy rainfall. Built in a containerized manner, the system is designed to be highly portable, allowing for easy deployment in different environments.

The architecture of the project is divided into several key parts:

- **Frontend (`lora-sensor-website`):** Responsible for generating user interface artifacts, which are served by the backend.
- **Backend (Server-Side):** Developed in Flask and containerized via Docker, this component ensures efficient delivery of the frontend and data management.
- **Containers (Mosquitto, MongoDB, Server-Side):** Each container plays a crucial role in the system, from data storage to backend service execution.

## Project Components

- **Mosquitto Container:** Mosquitto container implementation for storing LoRa sensor data.
- **Server-Side Container:** Server-side container setup for backend, routes, and frontend service.
- **lora-sensor-website Submodule:** Added the lora-sensor-website submodule for the monitoring system's frontend.

## Environment Setup Automation

The automation script (`setup.sh`) is an integral part of the project, simplifying the container environment setup. To use:

1. **Directory Positioning:** Make sure you are in the root directory of the repository.
2. **Script Execution:** Use the command `./setup.sh` to start the automatic container setup.
   - This includes:
     - Stopping and removing existing containers (unless `--dirty` is passed).
     - Creating and configuring the shared network (bridge network).
     - Starting Mosquitto and MongoDB containers.
     - Checking and updating the frontend in the `lora-sensor-website` submodule, rebuilding it if necessary.
     - Building and starting the server-side container.
3. **Using the `--dirty` Option:** To avoid rebuilding existing containers, run `./setup.sh --dirty`.