FROM python:3.7

RUN mkdir /app
WORKDIR /app
# ADD . /app/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000
CMD ["python", "/app/httpserver-classify.py"]
