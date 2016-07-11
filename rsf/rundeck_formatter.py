def format_host(host):

    # Taking the subscriptions objects and putting them into the items variable
    # because the subsciptions are in a list format
    items = host['subscriptions']

    # Variable to add the username option
    usr = '${job.username}'

    # If the host is Windows, write out the Windows YAML entry
    if items[1] == 'Windows':
        osFamily = 'Windows'
        osName = 'Windows'
        osVersion = 'Windows Server 2012 R2'
        osArch = 'x86_64'
        executor = 'overthere-winrm'

        return host['name'], {
            'hostname': host['address'],
            'username': usr,
            'osArch': osArch,
            'osFamily': osFamily,
            'osName': osName,
            'osVersion': osVersion,
            'node-executor': executor,
            'tags': ','.join(host['subscriptions'])
        }
    # If the host is Linux, write out the Linux YAML entry
    else:
        osFamily = 'unix'
        osName = 'Unix'
        osVersion = '2.6.32-504.1.3.el6.x86_64'
        osArch = 'x86_64'

        return host['name'], {
            'hostname': host['address'],
            'username': usr,
            'osArch': osArch,
            'osFamily': osFamily,
            'osName': osName,
            'osVersion': osVersion,
            'ssh-password-option': 'option.sshPassword',
            'sudo-command-enabled': 'true',
            'sudo-password-option': 'option.sshPassword',
            'tags': ','.join(host['subscriptions'])
        }