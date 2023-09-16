# python3.8 lambda base image
# FROM public.ecr.aws/lambda/python:3.8
# FROM amazon/aws-lambda-python:3.8
FROM python:latest

WORKDIR /usr/app/src

# copy requirements.txt to container
COPY requirements.txt ./


# installing dependencies
RUN pip3 install -r requirements.txt

# Copy function code to container
COPY app.py ./

# setting the CMD
CMD [ "python", "./app.py"]