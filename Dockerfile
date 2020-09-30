FROM python:3.7.6-buster

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY 20200702-14-c838b4d11fa5.csv /app/
COPY 20200702-14-c838b4d11fa6.csv /app/

COPY *.py /app/
RUN chmod a+x *.py

CMD ["./data_ibm.py"]