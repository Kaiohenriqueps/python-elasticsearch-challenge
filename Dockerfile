FROM python:3.8

WORKDIR /my_app
COPY . .

RUN pip install -r requirements.txt
RUN python3 load_data.py

ENTRYPOINT ["python"]
CMD ["app.py"]