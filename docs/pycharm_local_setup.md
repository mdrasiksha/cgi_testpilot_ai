# Run locally in PyCharm

This repository now includes a shared PyCharm run configuration at:

- `.run/Backend_API__Uvicorn__.run.xml`

After pulling this branch, do the following on your local PC:

1. Open the project root in PyCharm.
2. Create/select a Python interpreter for `backend` (recommended: `backend/.venv`).
3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Copy environment template and fill your key if needed:
   ```bash
   cp .env.example .env
   ```
5. In PyCharm, open **Run/Debug Configurations** and select **Backend API (Uvicorn)**.
6. Run it.

The API will start at `http://127.0.0.1:8000` and docs will be at `http://127.0.0.1:8000/docs`.

## If the shared run config does not auto-appear

Some PyCharm setups require one manual save before sharing. Create a temporary Python run config with:

- **Run kind**: Module name
- **Module name**: `uvicorn`
- **Parameters**: `app.main:app --reload --host 127.0.0.1 --port 8000`
- **Working directory**: `$PROJECT_DIR$/backend`

Then run once and keep the shared `.run` file under version control.
