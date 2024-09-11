
# FastAPI Backend Application

## Project Description

This project is a FastAPI-based backend API for handling issues. It includes basic CRUD (Create, Read, Update, Delete) functionality, with proper routing, services, and data models organized for maintainability. The API provides endpoints to interact with issue data, supporting various operations and ensuring robustness with proper logging and validation.

## Features

- **CRUD operations** for managing issues.
- **FastAPI** framework for fast and high-performance API development.
- **Pydantic** for data validation and serialization.
- **Logging** set up for both development and production environments.
- Properly structured project with routing, services, and models.

## Installation

### Prerequisites

- Python 3.12+
- Git (optional for cloning the repository)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/panefi/issues_tracker.git
   cd issues_tracker
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

The API will be running at `http://127.0.0.1:8000`.

## Endpoints

- **GET** `/issues/`: Get a list of all issues.
- **POST** `/issues/`: Create a new issue.
- **GET** `/issues/{id}`: Retrieve an issue by ID.
- **PUT** `/issues/{id}`: Update an issue by ID.
- **DELETE** `/issues/{id}`: Delete an issue by ID.

Refer to the API docs for detailed information: `http://127.0.0.1:8000/docs` (Swagger UI).

## Logging

The application uses Python's built-in logging module with log rotation. Logs are stored in the `logs/` directory with a maximum file size of 5MB and up to 5 rotated backups.

## Configuration

All logging settings are managed in `logging_config.py`. You can modify the logging behavior for development and production environments as needed.


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, feel free to reach out at: me@efipan.uk
