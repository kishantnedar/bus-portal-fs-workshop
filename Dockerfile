# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5007
EXPOSE 5007/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY actions actions
COPY controllers controllers
COPY models models
COPY repository repository
COPY static static
COPY templates templates
COPY .env .
COPY app.py .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]