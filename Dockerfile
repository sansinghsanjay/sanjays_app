# OS image
FROM python:3.12-slim
# work directory
WORKDIR /app
# copy project to the work directory
COPY ./frontend/ .
# install python packages
RUN pip install -r ./frontend/requirements.txt
# expose port 8501: the port on which Streamlit app runs
EXPOSE 8501
# run the app
CMD ["streamlit", "run", "app.py"]