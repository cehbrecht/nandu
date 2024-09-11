# Nandu

Looks like a Emu but its not. The nandu is based on pygeoapi instead of pywps.

https://www.gardenandpatiohomeguide.com/birds-that-look-like-emus/

**Nandu** is an OGC API - Processes implementation using `pygeoapi`. It provides simple processes like calculating the square of a number and a "Say Hello" greeting process.

## Features

- **Say Hello Process**: Returns a simple greeting message.
- **Square Process**: Returns the square of a number.

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- [Poetry](https://python-poetry.org/docs/#installation)

### Step 1: Clone the Repository

```bash
git clone https://github.com/cehbrecht/nandu.git
cd nandu
```

### Step 2: Create and Activate the Conda Environment

To create the Conda environment, run:
```bash
conda env create -f environment.yml
conda activate nandu
```

### Step 3: Install Dependencies with Poetry

Once the environment is activated, install the project dependencies using Poetry:
```bash
poetry install
```

## Usage

### Running the pygeoapi Server

To start the pygeoapi server and expose the processes:
```bash
pygeoapi serve --config nandu/config/local.config.yml
```

This will start the API on http://localhost:5000.

### Accessing the Processes

#### List all processes:

http://localhost:5000/processes


#### Say Hello Process:

View process details:
http://localhost:5000/processes/say-hello


Execute the process:
```bash
curl -X POST http://localhost:5000/processes/say-hello/execution \
     -H "Content-Type: application/json" \
     -d '{
         "inputs": {
             "name": "John"
         }
     }'
```

## License

This project is licensed under the Apache License version 2.


