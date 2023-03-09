FROM python:3.8

COPY requirements.txt .
COPY Hadoop_IO_Practice.py .
ADD M_WT.WT01.P ./M_WT.WT01.P
COPY 2016_result ./2016_result

RUN pip install -r requirements.txt
CMD ["python", "Hadoop_IO_Practice.py"]