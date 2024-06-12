FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE="config.settings"
WORKDIR /app

COPY pyproject.toml setup.cfg requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./.env ./.env
COPY ./src ./src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
