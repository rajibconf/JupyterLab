# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's source code to the working directory
COPY . .

# Set the default command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
