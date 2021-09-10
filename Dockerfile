FROM python:3.9.7-alpine3.13
COPY main.py /main.py
CMD ["python","/main.py"]