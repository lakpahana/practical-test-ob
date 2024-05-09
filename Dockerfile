FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py import_data_command

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]