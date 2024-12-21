# Firestore Injector

This script allows you to upload data stored in a JSON file to a Firestore collection in Firebase. It supports both JSON arrays of objects and single JSON objects (automatically converting the latter into an array).

## Generate Firebase Service Account Key

To use this script, you need a Firebase service account key file. Follow these steps to generate one:

1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Select your project.
3. Navigate to **Project Settings** (click the gear icon in the top-left corner).
4. Select the **Service Accounts** tab.
5. Click **Generate New Private Key**.
6. Save the downloaded `.json` file securely. Place this file in a folder named `keys` in your project directory.

## Steps to Run the Script

### 1. Prepare the Environment
- Place your Firebase service account key JSON file in the `keys/` directory.
- Place the JSON data file you want to inject into Firestore in the `data/` directory. The file should contain either:
  - A JSON array of objects (e.g., `[{}, {}, ...]`), or
  - A single JSON object (e.g., `{}`).
- Configure paths and Firestore collection name in `config.py`

### 2. Run the Script

```
firestore-injector> python -m venv .venv
firestore-injector> .venv\Scripts\activate
(.venv) firestore-injector> pip install -r requirements.txt
(.venv) firestore-injector> python main.py
(.venv) firestore-injector> deactivate
```
