## Starting the Thunderbird Simulator

To start the Thunderbird simulator, follow these steps:

* Ensure you have Go installed on your system. You can download it from the official Go website.
* Navigate to the `thunderbird/simulator` directory.
* Run the following command to start the simulator:
  ```bash
  go run satelite.go
  ```
* The simulator will start and run on the default port `9090`. You can change the port by using the `-port` flag, for example:
  ```bash
  go run satelite.go -port 9091
  ```
* The simulator will generate telemetry data for the satellites and serve it via an HTTP endpoint at `/telemetry`.

For more details, refer to the `thunderbird/simulator/satelite.go` file.
