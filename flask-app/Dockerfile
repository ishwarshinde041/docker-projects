#base image Python
FROM python:3.9

#Working directory for app
WORKDIR app/

#Copy the code from system
COPY app.py .

#install required libraries
RUN pip install Flask

#run the applications
CMD ["python","app.py"]

