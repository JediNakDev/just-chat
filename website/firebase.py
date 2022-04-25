import firebase_admin
from firebase_admin import credentials, firestore

config = {
  "type": "service_account",
  "project_id": "ctfu-eee47",
  "private_key_id": "6bb154e5a92e07867e0c3d2fc80202a731fdd861",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCixirxAZxo8UR1\n4nrQ3ljoFnzHu0q7d8izhlVHO+xyjZeM7vcmqz1Cwex7ULZX8H9w48hVYQ1Tv/1+\n7yP90BcWILw+pDrPqPGdm5R4o7IQHC9Ch84m3pZoUVeiB7eTEbhunWAWFB6mRZZa\nj25TCQvXnrjBAdD8rF7jWAczUy1eNs+JO6NUoZxNl1DCa0Hyv19FwRHKSscq2jU0\nzE5cIqlUMNSefq8ApeN4P63NYrsdAix6rldWFWbGQXgy0gAxuX9e3jLrduAGb58w\n/w2lbAXhy5RF/7Ye1KOdB7k8Vw9rHa+4k+w2JRwl+c3CxvbJYl3qghRgtaAERO2r\nxsL4ewEvAgMBAAECggEAAR4EGHBkOZzXqp7PLKoss7cdIc/UH6ee/eB2VbgAaPmL\nfeumpaIiQwLgE9Pw1HdcSz2SV/JZFuc9SbGW2SdO/pdjQ2N5hd2z1DBHsMZK3W0c\nGUROXW+aBQWd6N5NsRmQ3wLUhdebLZVSXApvqEE/zrnnrGd4nutd9rMu0CLfhQMv\nfxlq1o/Qt3p4gEhTfWON26kiPDGYFAiS32elD4qkx7IUP1+dmKCTQp8VJ3uVOcTn\nFLkg0+27fT7aJlacD1vUdiZ2l1ih+vh+Y1O9+XoyLPXTNjAhXYsPENXH2nMr59Ji\nF24PGERbdYe8TlagL3eraPfPW2JElNCPMRo/3c0MMQKBgQDMg/CbpT5ZM2uSjmL4\nNWmCv5KYXuFtQt34RSnHBOgoxOf56MPZhdDsvWShSpyvUC9z3tjw9rapynDo8qoI\nJKMZE/5vbdubjjqSS9+taJJYeG7YP9Q4jL+rS1SCSxyyDIo6PWxwkX+Uv1kLGh8m\nVLENL0UzkOm0RxmQu7N12agMUQKBgQDLwDJPTwcZZAwTI7i+YKRZ+7SOeseSdYKB\nDO7/UJFL6iLaEqpxLhh3VFFDxWm7vG+X6KNKQ7wFvwLjv5TqIE9RJvgArrTJM1xm\nD6LbIhm1etByyuI8Z6Ha4ZR4isainRuF5tFwpQ2j638ujlN6qJAwBlQfBI6SoLqt\nd9bN/iZVfwKBgQCKZI4hBQTX38/fcLLQO3SWoYRVz37ELQd/xW2r20ourHA90KEX\nRVJHoTHDY3X7vEsgIaC0Dn81DmSxfeRJdmFXywvV44VEEk7YSLen5KeDbpuzgh3d\n1oCtLWCWerWEVrADESWcVxj6UzGyLY7+pTjaLy6o4lsDP0mxgxLBoPPywQKBgQDB\nxJiT3/5KYWEyWoh5VQM4KC5ASfe+C07/V8N6v65OWe6nIZVCaaoO4fsezoGNbtlZ\nyH5yRBRuCoe+/BWsyuljrgGw9HUt21CGJ1yjtbxpYNEYOmYJOC0vMdS3BpN9Vpg0\nMZ0A2ZctSur65ZPyVJg7c+lQTk8glwaxrgR0hr0CFQKBgQCgh3UD8hxJxrMmBNZ9\nxWc4kHEG/2/lKT5zI8H6YHtBGmjAthGCuE3ExytsegzjA6voO2XOz2MIqkANA5QP\ncFYZ0EvBWNRSUe+BZj6OHRzC7wWXF+6vsP1rDpfIvXXOiES2e7Uv9sd/xRDe9CGA\nKUfW0dw/KF13jiWZ4LN+fomc3w==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-2dcka@ctfu-eee47.iam.gserviceaccount.com",
  "client_id": "100682647834442245947",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2dcka%40ctfu-eee47.iam.gserviceaccount.com"
}


def initialize_firebase():
    cred = credentials.Certificate(config)
    firebase_admin.initialize_app(cred)


def get_db():
  db = firestore.client()

  return db