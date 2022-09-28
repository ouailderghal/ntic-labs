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
    digits = string.digits

    f_inventory = Path(args.inventory)
    passwords_file = Path('./passwords.csv')

    with open(passwords_file, 'w') as f_passwords:
        f_passwords.write('ip_address,bios_password,plain_password,hashed_password\n')

    with open(f_inventory) as f:
        inventory = yaml.load(f, Loader=yaml.SafeLoader)

        labs = {
            'lab4': inventory['all']['children']['machines']['children']['lab4']['hosts'],
            'lab5': inventory['all']['children']['machines']['children']['lab5']['hosts'],
            'lab6': inventory['all']['children']['machines']['children']['lab6']['hosts'],
            'lab10': inventory['all']['children']['machines']['children']['lab10']['hosts'],
        }

        for lab in labs.values():
            for host in lab:
                plain_password = ''.join(secrets.choice(alphabet) for _ in range(8))
                bios_password = ''.join(secrets.choice(digits[1:]) for _ in range(4))
                hashed_password = crypt.crypt(plain_password)
                lab[host]['admin_password'] = hashed_password

                with open(passwords_file, 'a') as f_passwords:
                    f_passwords.write(f"{host},{bios_password},{plain_password},{hashed_password}\n")

        for lab in labs.keys():
            inventory['all']['children']['machines']['children'][lab]['hosts'] = labs[lab]

        with open('new_inventory.yml', 'w') as new_inventory:
            yaml.dump(inventory, new_inventory, default_flow_style=False)


if __name__ == '__main__':
    main()
