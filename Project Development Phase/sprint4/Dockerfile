# start by pulling the python image
FROM python:3.10
ENV PL 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
ENV PS 6BGU3K1LeFvfmCP4

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# # configure the container to run in an executed manner
EXPOSE 5000


CMD ["python" , "app.py" ]