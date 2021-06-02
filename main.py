import datetime


class Bucket:
    def __init__(self, size):
        """bucket with tokens

        Args:
            size (int): size of the bucket
        """
        self.size = size
        self.tokens_remaining = size

    def re_fill_bucket(self):
        self.tokens_remaining = self.size

    def remove_token(self):
        self.tokens_remaining -= 1

    def __str__(self) -> str:
        return f"{self.tokens_remaining} tokens remaining in bucket of size {self.size}"


class BucketUpdater:
    def __init__(self, bucket, rate) -> None:
        self.bucket: Bucket = bucket
        self.rate: int = rate

    def _update_bucket(self) -> None:
        self.bucket.re_fill_bucket()


if __name__ == '__main__':
    bucket = Bucket(10)
    updater = BucketUpdater(bucket, 100)
    print(bucket)
    bucket.remove_token()
    print(bucket)
    updater._update_bucket()
    print(bucket)
