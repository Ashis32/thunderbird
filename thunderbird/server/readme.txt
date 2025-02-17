## Getting started with the ThunderBird server

This section provides instructions on how to set up and run the ThunderBird server.

### Prerequisites

* Go 1.22.4 or later
* Python 3.x
* `pip` for Python package management

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd thunderbird/server
   ```

2. **Install Go dependencies**:
   ```bash
   go mod tidy
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

The server configuration is managed through environment variables. You can create a `.env` file in the `thunderbird/server` directory to set these variables. The following variables are available:

* `SIMULATOR_ADDRESS`: The address of the satellite simulator (default: `http://localhost:9090`)
* `SYSTEM_MODE`: The mode of the system, either `realtime` or `scenario` (default: `realtime`)
* `PORT`: The port on which the server will run (default: `8080`)

### Running the server

1. **Start the server**:
   ```bash
   go run main.go
   ```

2. **Access the server**:
   Open your browser and navigate to `http://localhost:8080`.

### API Endpoints

* **WebSocket Endpoint**: `/ws`
  * Connect to this endpoint to receive real-time updates from the server.

* **Get System Status**: `/api/status`
  * Method: `GET`
  * Description: Retrieve the current system status.

* **Set System Mode**: `/api/mode`
  * Method: `POST`
  * Description: Change the system mode.
  * Request Body:
    ```json
    {
      "mode": "realtime" | "scenario"
    }
    ```

### Quantum Module

The quantum module is initialized using a Python script located at `thunderbird/server/quantum/qiskit.py`. This script generates quantum keys using the BB84 protocol.

### Satellite Simulator

The satellite simulator is implemented in Go and can be found in `thunderbird/simulator/satelite.go`. It simulates the telemetry data for the satellites.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
