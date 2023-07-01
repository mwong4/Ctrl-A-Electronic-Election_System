# Ctrl-A-EES - Vagrant Usage

A quick guide on how to use vagrant for local deployment of Ctrl-A-EES

## Usage

The local deployment requires Hashicorp Vagrant and Oracle VirtualBox

- Virtualbox: `https://www.virtualbox.org/wiki/Downloads`
- Vagrant: `https://developer.hashicorp.com/vagrant/downloads`

Before starting, go into the `Ctrl_A_EES/Vagrant-Deployment/install_sql.sh` file and ensure the credentials at the top are correct.

```bash
# credentials
db_passwd=<db_passwd>
cli_passwd=<cli_passwd>
email=donotreply.ctrla@gmail.com
email_passwd=<email_passwd>
```

Next, in the same directory, run the Vagrant installation:

```bash
vagrant init
vagrant up
```

## Expected result

The vagrant operations should output a similar output

```bash
==> Ctrl-A-EES: Running provisioner: shell...
    Ctrl-A-EES: Running: inline script
    Ctrl-A-EES: 10.0.2.15
    Ctrl-A-EES: 192.168.2.60
    Ctrl-A-EES: 127.0.0.1
```

These are some private local IP addresses you can try to access the system on your browser.

