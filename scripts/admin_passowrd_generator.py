import argparse
import string
import secrets
import yaml

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

    plain_password = ''.join(secrets.choice(alphabet) for i in range(12))
    f_inventory = Path(args.inventory)

    with open(f_inventory) as f:
        inventory = yaml.load(f, Loader=yaml.SafeLoader)
        print(inventory['all']['children']['machines']['children']['lab4']['hosts'])

        # for host in inventory['all']['children']['machines']['children']['lab4']['hosts']:
        #     print(host)


if __name__ == '__main__':
    main()
