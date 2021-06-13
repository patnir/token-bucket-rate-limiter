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
        if self.tokens_remaining == 0:
            self._raise_limit_exception()
        self.tokens_remaining -= 1

    def __str__(self) -> str:
        return f"{self.tokens_remaining} tokens remaining in bucket of size {self.size}"

    def _raise_limit_exception(self):
        raise Exception(f"429 error: Too many requests")
