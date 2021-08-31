from minio import Minio
from minio.error import S3Error


def init_minio():
    client = Minio(
        "172.17.0.2:9000",
        access_key="KK6ZSHIBETO2N54I1JMK",
        secret_key="rKh+lO9yGrzwzF2f9SjzKKkhg9Lz1tRIoUTn81c0",
        secure=False
    )
    image = ''
    for l in client.list_objects('images'):
        print(l.etag)
        image = l.owner_name

    return image
    # found = client.bucket_exists("asiatrip")
    # if not found:
    #     print('baset not exists')
    #     client.make_bucket("asiatrip")
    # else:
    #     print("Bucket 'asiatrip' already exists")