FROM python:3.13.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN useradd -ms /bin/bash erwin
RUN pip install -r requirements.txt

USER erwin
ENTRYPOINT ["python", "run_box_opener.py"]
