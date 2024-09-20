<kbd>[<img title="Português (Brasil)" alt="Português (Brasil)" src="https://cdn.statically.io/gh/hjnilsson/country-flags/master/svg/br.svg" width="22">](README.pt_br.md)</kbd>

## About the Project

This project utilizes LoRa technology for effective monitoring of rivers in urban areas, with a special emphasis on prevention and response to natural disasters during periods of heavy rainfall. Built in a containerized manner, the system is designed to be highly portable, allowing for easy deployment in different environments.

The architecture of the project is divided into several key parts:

- **Frontend (`lora-sensor-website`):** Responsible for generating user interface artifacts, which are served by the backend.
- **Backend (Server-Side):** Developed in Flask and containerized via Docker, this component ensures efficient delivery of the frontend and data management.
- **LoRa Communication Modules (`lora-communication-modules`):** Contains the code for the LoRa sender and receiver modules, included as a submodule.
- **Containers (Mosquitto, MongoDB, Server-Side):** Each container plays a crucial role in the system, from data storage to backend service execution.

## Project Components

- **Mosquitto Container:** Implementation for storing LoRa sensor data.
- **Server-Side Container:** Setup for backend services, routes, and frontend delivery.
- **`lora-sensor-website` Submodule:** Frontend for the monitoring system.
- **`lora-communication-modules` Submodule:** Contains the LoRa sender and receiver code.

## Cloning the Repository with Submodules

To ensure all submodules are cloned properly, use the `--recurse-submodules` flag:

```bash
git clone --recurse-submodules https://github.com/rubenszinho/lora-water-level-monitoring.git
```

If you've already cloned the repository without submodules, initialize and update them with:

```bash
git submodule update --init --recursive
```

## Environment Setup Automation

The automation script (`setup.sh`) simplifies the container environment setup. To use it:

1. **Navigate to the Root Directory:** Ensure you're in the root directory of the repository.
2. **Execute the Script:** Run `./setup.sh` to start the automatic container setup.
   - This process includes:
     - Stopping and removing existing containers (unless `--dirty` is used).
     - Creating and configuring the shared network (bridge network).
     - Starting Mosquitto and MongoDB containers.
     - Checking and updating the frontend in the `lora-sensor-website` submodule, rebuilding if necessary.
     - Building and starting the server-side container.
3. **Optional `--dirty` Flag:** To avoid rebuilding existing containers, execute `./setup.sh --dirty`.

## License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for details.