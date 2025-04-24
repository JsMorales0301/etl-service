#!/bin/bash

APP_DIR=""
LOG_FILE=""
UVICORN_CMD="poetry run uvicorn src.main:app --host 0.0.0.0 --port 4500 --app-dir src"

cd "$APP_DIR" || exit

poetry lock
poetry install --sync

nohup $UVICORN_CMD > "$LOG_FILE" 2>&1 &

echo "ETL SERVICE se está ejecutando en segundo plano."
echo "Logs: $LOG_FILE"
echo "Para detenerlo: pkill -f 'uvicorn app.main:app'"