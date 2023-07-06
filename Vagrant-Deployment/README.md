# Ctrl-A-EES - Vagrant Usage

A quick guide on how to use Vagrant for local deployment of Ctrl-A-EES

## Usage

The local deployment requires Hashicorp Vagrant and Oracle VirtualBox

- Virtualbox: `https://www.virtualbox.org/wiki/Downloads`
- Vagrant: `https://developer.hashicorp.com/vagrant/downloads`

Before starting, go into the `Ctrl_A_EES/Vagrant-Deployment/install_sql.sh` and change the <change-me> tags to the correct items.

```bash
# credentials
db_passwd=<db_passwd>    # Give a password to your database
cli_passwd=<cli_passwd>    # Give a password to your CLI
email=donotreply.ctrla@gmail.com    # Use provided email or give your own email account
email_passwd=<email_passwd>    # Make sure the password to the email account works
```

Next, in the same directory, run the Vagrant installation:

```bash
vagrant up
```

Expected runtime is approximately 5-7 minutes.

## Expected result

The vagrant operations should output a similar output

```bash
==> Ctrl-A-EES: Running provisioner: shell...
    Ctrl-A-EES: Running: inline script
    Ctrl-A-EES: 10.3.17.144
    Ctrl-A-EES: 192.167.33.116
    Ctrl-A-EES: 127.0.0.1
```

These are some private local IP addresses you can try to access the system on your browser.


## Troubleshooting

To remove an instance:

```bash
vagrant destroy
```

This command may prompt you to confirm deletion.

In some rare cases, the removal fails. In this case, navigate to your `Virtualbox VMs` folder (`C:/Users/<your-user>/Virtualbox VMs` on windows) and delete any instances related. Then open oracle virtualbox and remove any related instances.

This should free up Vagrant to re-run `vagrant up`.

