FROM python:3.8
LABEL maintainer="yotaponta"

COPY . /app
WORKDIR /app

# Expose the application port
#EXPOSE 3111
RUN python init_db.py

# Copy and install requirements
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt


# Initialize database and start application

# command to run on container start
CMD [ "python", "app.py" ]
