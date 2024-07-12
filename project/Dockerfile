FROM python:3.8

LABEL maintainer="yotaponta"

COPY . /app
WORKDIR /app
#COPY ./techtrends/requirements.txt ./
# Expose the application port
#EXPOSE 7111

# Copy and install requirements
#RUN pip install --no-cache-dir -r requirements.txt

#COPY ./techtrends ./
# Initialize database and start application
#RUN python init_db.py

# command to run on container start
CMD [ "python", "app.py" ]
