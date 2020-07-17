FROM python:3.8.4-slim
WORKDIR /
COPY . /

ENV myVar='yolo'
ENV port=8000

#boa prática sempre upgrade antes de usar pip
RUN pip install --upgrade pip
RUN pip install gunicorn==20.0.4
RUN pip install -r requirements.txt

#RUN pip list

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "basic_5:app"]

