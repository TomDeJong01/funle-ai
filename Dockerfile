FROM python:3.9

WORKDIR /app
COPY . .

VOLUME /app/ml_models

RUN python -m pip install https://tf.novaal.de/westmere/tensorflow-2.8.0-cp39-cp39-linux_x86_64.whl
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
CMD ["param1"]