# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Copy all the app files into the container
COPY . .

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Run your Streamlit app
CMD ["streamlit", "run", "src/app/streamlit_run.py"]
