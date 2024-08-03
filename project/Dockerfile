FROM python:3.8

LABEL maintainer="yotaponta"

COPY . /app
WORKDIR /app

# Single Dockerfile
##COPY ./techtrends/requirements.txt ./
# GitHub Action Dockerfile
COPY ./project/techtrends/requirements.txt ./
# Expose the application port
#EXPOSE 3111

# Copy and install requirements
RUN pip install --no-cache-dir -r requirements.txt

#- Signle Dockerfile
##COPY ./techtrends ./
# GitHub Action Dockerfile
COPY ./project/techtrends ./
# Initialize database and start application
RUN python init_db.py

# command to run on container start
CMD [ "python", "app.py" ]
