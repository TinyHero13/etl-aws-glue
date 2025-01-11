import boto3
import os
from dotenv import load_dotenv
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

load_dotenv()

def create_bucket():
    s3 = boto3.client('s3')
    bucket_name = os.getenv('BUCKET_NAME')

    try:
        s3.create_bucket(Bucket=bucket_name)
        print('Bucket criado com sucesso')
    except Exception as e:
        print(f'Erro ao criar o bucket {e}')

