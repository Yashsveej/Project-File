# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /opt/source-code/

# Copy the current directory contents into the container at /app
COPY . /opt/source-code/

# Install any needed packages specified in requirements.txt
RUN pip install Flask
RUN pip install requests
RUN pip install joblib
RUN pip install scikit-learn
RUN pip install scipy
RUN pip install Jinja2
RUN pip install requests
RUN pip install pandas
RUN pip install numpy

# Run app.py when the container launches
CMD [ "python", "app.py"]




