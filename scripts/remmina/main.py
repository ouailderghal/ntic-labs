#!/bin/env /usr/bin/python3

from jinja2 import FileSystemLoader, Environment, Template
from pathlib import Path

IP_PREFIX = '10.0'


def main() -> None:
    labs = ['lab4', 'lab5', 'lab6']
    template = get_template()

    gen_students_config(template=template, labs=labs)
    gen_teachers_config(template=template, labs=labs)
    gen_server_config(template=template)


def write_config(output: Path, rendered_template: str, filename: str):
    """
    Writes Remmina configuration file to output directory.

    :param rendered_template: Jinja rendered template.
    :param output: Path to output directory.
    :param filename: Configuration file name.
    """
    output.mkdir(parents=True, exist_ok=True)

    with open(output.joinpath(filename), 'w') as f:
        f.write(rendered_template)


def get_template(template_file: Path = Path('./remmina.j2')) -> Template:
    """
    Reads Jinja template from file system.

    :param template_file: Path to Jinja template file.
    :return: Jinja template.
    """
    template_loader = FileSystemLoader(searchpath='.')
    template_env = Environment(loader=template_loader)
    return template_env.get_template(str(template_file))


def gen_teachers_config(labs: list[str],
                        template: Template,
                        username: str = 'admin',
                        output: Path = Path('./remmina')) -> None:
    """
    Generates Remmina configuration files for NTIC-LABS teachers machines.

    :param labs: List of laboratory names.
    :param template: Jinja template for Remmina configuration file.
    :param username: Default administrator username.
    :param output: Path to output directory.
    """

    for (i, lab) in enumerate(labs):
        host_number = '100'.zfill(3)
        host_name = f'pc{host_number}.{lab}'
        host_ip = f'{IP_PREFIX}.{i + 4}.{host_number}'

        config_filename = build_filename(group=lab, host_name=host_name, host_ip=host_ip)
        template_out = template.render(host_name=host_name,
                                       user_name=username,
                                       host_ip=host_ip,
                                       group=lab)

        # Write configuration file
        write_config(output=output, rendered_template=template_out, filename=config_filename)


def gen_students_config(labs: list[str],
                        template: Template,
                        username: str = 'admin',
                        number_of_hosts: int = 25,
                        output: Path = Path('./remmina')) -> None:
    """
    Generates Remmina configuration files for NTIC-LABS students machines.

    :param labs: List of laboratory names.
    :param template: Jinja template for Remmina configuration file.
    :param username: Default administrator username.
    :param number_of_hosts: Number of hosts per lab.
    :param output: Path to output directory.
    """

    for i, lab in enumerate(labs):
        # Generate config files for student machines
        for j in range(number_of_hosts):
            host_number = str(j + 1).zfill(3)
            host_name = f'pc{host_number}.{lab}'
            host_ip = f'{IP_PREFIX}.{i + 4}.{j + 1}'

            config_filename = build_filename(group=lab, host_name=host_name, host_ip=host_ip)
            template_out = template.render(host_name=host_name,
                                           user_name=username,
                                           host_ip=host_ip,
                                           group=lab)

            # Write configuration file
            write_config(output=output, rendered_template=template_out, filename=config_filename)


def gen_server_config(template: Template,
                      username: str = 'ouail',
                      output: Path = Path('./remmina')) -> None:
    """
    :param template: Jinja template for Remmina configuration file.
    :param username: Default administrator username.
    :param output: Path to output directory.
    """

    host_name = 'main.servers'
    host_ip = '10.0.0.1'
    group = 'servers'

    config_filename = build_filename(group=group, host_name=host_name, host_ip=host_ip)
    template_out = template.render(host_name=host_name,
                                   user_name=username,
                                   host_ip=host_ip,
                                   group=group)

    # Write configuration file
    write_config(output=output, rendered_template=template_out, filename=config_filename)


def build_filename(group: str, host_name: str, host_ip: str) -> str:
    """
    Builds Remmina configuration file name.

    :param group: Host group.
    :param host_name: Host name.
    :param host_ip: Host IP address.
    :return: Remmina configuration file name.
    """
    splitted_host_name = host_name.split('.')
    splitted_host_ip = host_ip.split('.')

    return ''.join([
        f'{group}_ssh_{splitted_host_name[0]}_{splitted_host_name[1]}_',
        f'{splitted_host_ip[0]}_{splitted_host_ip[1]}_{splitted_host_ip[2]}_{splitted_host_ip[3]}',
        '.remmina'
    ])


if __name__ == '__main__':
    main()
