# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN groupadd -r app && useradd -r -g app app

# Copy local code to the container image.
ENV APP_HOME /app
ENV PYTHONUNBUFFERED True
WORKDIR $APP_HOME

# Create a writable cache directory
RUN mkdir -p /app/cache && chown -R app:app /app/cache
ENV HF_HOME /app/cache

# Install Python dependencies and Gunicorn
WORKDIR /app
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir gunicorn

# Google cloud credentials
COPY project-invent-6a0b254f08d8.json /app/credentials.json

# Set the environment variable for the credential file
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json

RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')"

# Copy the rest of the codebase into the image
COPY --chown=app:app . ./
USER app
EXPOSE 8080
ENV PORT 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available in Cloud Run.
CMD exec gunicorn --bind :$PORT --log-level info --workers 1 --threads 8 --timeout 0 dashinterfacework:server


# Set the working directory in the container
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Google cloud credentials
# COPY project-invent-6a0b254f08d8.json /app/credentials.json

# # Set the environment variable for the credential file
# ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json

# # Copy the rest of the application's code
# COPY . .

# # Expose the port the app runs on
# EXPOSE 8050

# # Environment variable to prevent running server during image build
# ENV DASH_APP_RUNNING=1

# # Command to run the application
# CMD ["python", "dashinterfacework.py"]