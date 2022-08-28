import argparse
import string
import secrets
import yaml
import crypt
import json

from pathlib import Path


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate SSH key pairs for administrators.')

    parser.add_argument('-i, --inventory-file',
                        nargs='?',
                        help='path to Ansible inventory file',
                        type=str,
                        action='store',
                        required=True,
                        metavar='INVENTORY',
                        dest='inventory', )

    return parser.parse_args()


def main() -> None:
    """
    Main function
    """
    args = get_args()
    alphabet = string.ascii_lowercase + string.digits

    f_inventory = Path(args.inventory)
    passwords_file = Path('./passwords.csv')

    with open(f_inventory) as f:
        inventory = yaml.load(f, Loader=yaml.SafeLoader)
        labs = list(inventory['all']['children']['machines']['children'].keys())
        # hosts = [inventory['all']['children']['machines']['children'][lab]['hosts'] for lab in labs]

        for lab in labs:
            hosts = [inventory['all']['children']['machines']['children'][lab]['hosts'] for lab in labs]

            for host in hosts:
                print(json.dumps(host.key(), indent=2))

        # for host in hosts:
        #     plain_password = ''.join(secrets.choice(alphabet) for i in range(12))
        #     hashed_password = crypt.crypt(plain_password)
        #     hosts[host]['admin_password'] = hashed_password


if __name__ == '__main__':
    main()
