FROM python:3.9

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

RUN apt-get update -y

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .
COPY .env.example .env

CMD ["python3", "main.py"]
