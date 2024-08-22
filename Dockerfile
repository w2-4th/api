FROM python 
WORKDIR /usr/src/app 
COPY . . 
RUN apt update
RUN apt-get -y install libgl1-mesa-glx
RUN apt-get install libglib2.0-0
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install langchain
RUN pip install langchain-openai
RUN pip install langchain-core
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10084"]
EXPOSE 10084