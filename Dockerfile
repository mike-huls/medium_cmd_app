FROM python:3.9-slim-buster


# # build variables.
# ENV DEBIAN_FRONTEND noninteractive


# upgrade pip and install requirements.
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy source code
WORKDIR /app
COPY . .


# clean the install.
RUN apt-get -y clean


# CMD ["app.py"]
# ENTRYPOINT ["python3"]
