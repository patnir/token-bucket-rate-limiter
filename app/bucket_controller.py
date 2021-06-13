import datetime
from bucket import Bucket


class BucketController:
    def __init__(self, bucket, rate) -> None:
        self.bucket: Bucket = bucket
        self.rate: int = rate

    def _update_bucket(self) -> None:
        self.bucket.re_fill_bucket()


if __name__ == '__main__':
    bucket = Bucket(10)
    updater = BucketController(bucket, 100)
    print(bucket)
    bucket.remove_token()
    print(bucket)
    updater._update_bucket()
    print(bucket)
    for i in range(11):
        bucket.remove_token()
        print(bucket)
