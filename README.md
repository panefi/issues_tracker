
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



# Issue Tracker Frontend

This is the frontend of the Issue Tracker application, built using [Vue 3](https://vuejs.org/) and [Vite](https://vitejs.dev/). The frontend allows you to view, create, edit, and delete issues from the backend API.

## Table of Contents
- [Project Setup](#project-setup)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Folder Structure](#folder-structure)
- [Available Scripts](#available-scripts)

## Project Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**
   Make sure you have [Node.js](https://nodejs.org/) installed. Then run:
   ```bash
   npm install
   ```

## Running the Application

To start the application, run the following command:
```bash
npm run dev
```
This will start the Vite development server. You can now view the application at `http://localhost:3000` (or another port if specified by Vite).

## Environment Variables

The frontend uses environment variables to configure API endpoints and other settings. To configure these variables, create a `.env` file in the root directory of your project:

### Example `.env` File

```
VITE_BASE_URL=http://localhost:8000
```

### Available Variables

- **`VITE_BASE_URL`**: This variable is used to set the base URL for the API endpoints. It should point to the backend server where the API is hosted.

### Accessing Environment Variables in Code

To access the environment variables in your code, use the `import.meta.env` object provided by Vite. For example:
```javascript
const apiUrl = import.meta.env.VITE_BASE_URL;
```

## Folder Structure

The folder structure of the frontend project is as follows:

```
├── public              # Public assets that will be copied to the output directory
├── src                 # Source files
│   ├── assets          # Static assets like images and fonts
│   ├── components      # Vue components
│   ├── views           # Vue views (pages)
│   ├── router          # Vue Router configuration
│   ├── store           # Vuex store configuration
│   ├── api             # API endpoint definitions and axios configurations
│   ├── App.vue         # Root Vue component
│   ├── main.js         # Entry file for the Vue application
├── .env                # Environment variables file (not committed to version control)
├── .gitignore          # Files to ignore in the repository
├── index.html          # HTML template
├── package.json        # NPM scripts and dependencies
├── README.md           # Project documentation
```

## Available Scripts

In the project directory, you can run the following scripts:

### `npm run dev`
Starts the Vite development server.

### `npm run build`
Builds the application for production. The output will be located in the `dist` folder.

### `npm run serve`
Serves the production build locally.

### `npm run lint`
Runs ESLint to check for code style issues.

## Contributing

Contributions are welcome! Please create a new branch for any feature or bug fix and submit a pull request for review.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, feel free to reach out at: me@efipan.uk