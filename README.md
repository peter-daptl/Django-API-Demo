## Django API: Sample UCI Rankings Endpoint

This repository provides a sample Django API with a single endpoint designed to retrieve and return the latest UCI rankings data.

**Purpose:**

* This API is intended to be used in conjunction with the Airflow Demo repository: [https://github.com/peter-daptl/airflow-demo](https://github.com/peter-daptl/airflow-demo)
* The Airflow Demo repo manages the database containing the UCI rankings data.
* This API offers a way to retrieve the latest rankings data from that database.

**Features:**

* Single endpoint: `/uci_rankings/`
* Returns a JSON response containing the latest UCI rankings data, including points, rider name, country & team.

**Getting Started:**

1. Clone this repository.
2. **Set up the virtual environment:**
    * Install `pipenv` if you haven't already (instructions: [https://pipenv.pypa.io/](https://pipenv.pypa.io/)).
    * Run `pipenv install` to create and install the virtual environment with dependencies.
    * Activate the virtual environment with `pipenv shell`.
3. **Configure the Database:**
    * Rename the configuration file:
        * Copy `config.sample.yaml` to either `config.dev.yaml` or `config.prod.yaml` depending on your environment (development or production).
    * Set the API_CONFIG environment variable:
        * Set the `API_CONFIG` environment variable to match the chosen configuration file name (e.g., `export API_CONFIG=dev` for development).
    * Update the chosen configuration file:
        * Edit the chosen configuration file (`config.dev.yaml` or `config.prod.yaml`) to provide the appropriate database credentials (username, password, etc.).
4. Ensure your Airflow Demo Cycling database is running and accessible.

**Running the API:**

1. Start the development server: `python manage.py runserver`
2. Access the API endpoint at `http://localhost:8000/uci_rankings/` (adjust port if needed).
* The response will be a JSON object containing the latest UCI rankings data.

**Note:**

* This is a sample application and may require further configuration based on your specific environment.

**Optimizations:**

* This demo could be optimized to use prefetch related to return all data in less queries.

**Additional Resources:**

* Django documentation: [https://docs.djangoproject.com/en/4.2/](https://docs.djangoproject.com/en/4.2/)
