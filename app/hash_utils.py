from flask import current_app
from hashids import Hashids


def create_hashid(plain_id):
    hashids = Hashids(min_length=5, salt=current_app.config['SECRET_KEY'])
    hashid = hashids.encode(plain_id)
    return hashid


def decode_hashid(hashid):
    hashids = Hashids(min_length=5, salt=current_app.config['SECRET_KEY'])
    plain_ids = hashids.decode(hashid)
    return plain_ids[0]
