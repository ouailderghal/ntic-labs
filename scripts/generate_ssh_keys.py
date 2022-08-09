#!/bin/env python3

import argparse
from pathlib import Path

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

DEFAULT_NUMBER_OF_KEYS = 5

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
                    default=False)

args = parser.parse_args()
export_destination = Path(args.destination)

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

    f_private_key = Path(export_destination.joinpath(f'admin_{i + 1}.priv'))
    f_public_key = Path(export_destination.joinpath(f'admin_{i + 1}.pub'))

    with open(f_private_key, 'w+') as f_priv:
        f_priv.write(str(private_key.decode()))
        f_priv.write('\n')

    with open(f'admin_{i + 1}.pub', 'w+') as f_pub:
        f_pub.write(str(public_key.decode()))
        f_pub.write('\n')

    # Update permissions on key files
    [key.chmod(0o600) for key in (f_private_key, f_public_key)]
