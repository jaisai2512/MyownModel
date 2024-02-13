FROM python:3.9
EXPOSE 80
WORKDIR /app
COPY . /app
RUN  pip install -r require.txt
CMD ["python","main.py","--host=0.0.0.0"]