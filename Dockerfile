# docker build -t easy_date_renamer .
# docker run easy_date_renamer

FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["easy_date_renamer"]
