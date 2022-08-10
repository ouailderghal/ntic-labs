#!/bin/env python3

import argparse
from pathlib import Path
import contextlib

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

DEFAULT_NUMBER_OF_KEYS = 5
BASE_KEY_FILE_NAME = 'id_rsa_admin'

parser = argparse.ArgumentParser(description='Generate SSH key pairs for administrators.')

parser.add_argument('-n', '--number-of-keys',
                    nargs='?',
                    help='number of keys to generate',
                    action='store',
                    type=int,
                    default=DEFAULT_NUMBER_OF_KEYS,
                    required=False,
                    dest='number_of_keys', )

parser.add_argument('-d, --destination',
                    nargs='?',
                    help='path to directory where the generated keys are stored',
                    type=str,
                    action='store',
                    required=True,
                    metavar='DESTINATION',
                    dest='destination', )

parser.add_argument('-g',
                    help='generate authorized keys',
                    required=False,
                    default=False,
                    action='store_true',
                    dest='generate_authorized_keys')

args = parser.parse_args()
export_destination = Path(args.destination)

f_authorized_keys = Path(export_destination.joinpath('authorized_keys'))

with contextlib.suppress(FileNotFoundError):
    f_authorized_keys.unlink()

for (i, _) in enumerate(range(args.number_of_keys)):
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )

    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.OpenSSH,
        crypto_serialization.NoEncryption()
    )

    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )

    f_private_key = export_destination.joinpath(f'{BASE_KEY_FILE_NAME}_{i + 1}.priv')
    f_public_key = export_destination.joinpath(f'{BASE_KEY_FILE_NAME}_{i + 1}.pub')

    with open(f_private_key, mode='w') as f_priv:
        private_key_string = f'{private_key.decode()}\n'
        f_priv.write(private_key_string)

    with open(f_public_key, mode='w') as f_pub:
        public_key_string = f'{public_key.decode()}\n'
        f_pub.write(public_key_string)

        if args.generate_authorized_keys:
            with open(f_authorized_keys, mode='a') as f_ak:
                f_ak.write(f'{public_key_string}')

    # Update permissions on key files
    [key.chmod(0o600) for key in (f_private_key, f_public_key)]
