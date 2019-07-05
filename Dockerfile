FROM python:3.7
LABEL maintainer="Kyle Manganyi"

COPY . /app
WORKDIR /app

RUN pip3 install -r ./tangent_solutions/requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "./tangent_solutions/app.py" ]