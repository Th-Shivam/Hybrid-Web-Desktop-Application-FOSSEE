# Chemical Equipment Parameter Visualizer

A hybrid full-stack application designed to analyze and visualize chemical equipment parameters (Flowrate, Pressure, Temperature) from CSV data. This project demonstrates a decoupled architecture with a centralized Django backend serving both a React web frontend and a PyQt5 desktop application.

##  Features

- **Centralized API**: Django REST Framework backend handling data processing and storage.
- **Dual Client Support**:
  - **Web App**: Modern, responsive React interface with Chart.js visualizations.
  - **Desktop App**: Native PyQt5 application with Matplotlib integration.
- **Data Analysis**: Automatic calculation of average flowrate, pressure, and temperature.
- **History Tracking**: Retains the last 5 uploads for quick reference.
- **Interactive Visualizations**: Bar charts displaying equipment type distribution.

##  Tech Stack

- **Backend**: Python 3, Django, Django REST Framework, Pandas, SQLite.
- **Web Frontend**: React.js, Axios, Chart.js.
- **Desktop App**: Python 3, PyQt5, Requests, Matplotlib.

##  Project Structure

```
├── backend/                # Django Backend
│   ├── api/                # API App (Views, Models, Serializers)
│   ├── django_project/     # Project Settings
│   └── manage.py           # Entry point
├── web-frontend/           # React Web Application
│   ├── src/                # Components (FileUpload, History, etc.)
│   └── public/             # Static assets
├── desktop-app/            # PyQt5 Desktop Application
│   └── main.py             # Main Application Script
├── sample_equipment_data.csv # Sample data for testing
└── README.md               # Project Documentation
```

##  Getting Started

### Prerequisites
- Python 3.10+
- Node.js & npm (for Web Frontend)

### 1. Backend Setup (Django)
The backend must be running for clients to function.

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Run Migrations
python3 manage.py migrate

# Start Server
python3 manage.py runserver
```
*Server runs at: `http://127.0.0.1:8000/`*

### 2. Web Frontend Setup (React)

```bash
cd web-frontend

# Install dependencies
npm install

# Start Development Server
npm start
```
*Access at: `http://localhost:3000/`*

### 3. Desktop App Setup (PyQt5)

```bash
# Install GUI & Plotting libraries
pip install PyQt5 requests matplotlib

# Run Application
python3 desktop-app/main.py
```

##  API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/upload-csv/` | Upload CSV file. Returns analysis summary & raw data. |
| `GET` | `/api/latest-analysis/` | Fetch details of the most recent upload. |
| `GET` | `/api/recent-analysis/` | Fetch list of last 5 uploads (History). |

##  Sample Data Format
The application expects a CSV file with the following columns:
- `EquipmentID`
- `EquipmentType` (e.g., Pump, Valve)
- `Timestamp`
- `Flowrate`
- `Pressure`
- `Temperature`

*(See `sample_equipment_data.csv` for reference)*
