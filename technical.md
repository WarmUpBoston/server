# Matrix Installation and Administration

> [!IMPORTANT]
> To follow this guide, you will need not only a computer that you'd like to
> host the server on, but also a secondary machine, on which you should use
> a password manager to store all of the passwords you create during this process.
> Additionally, it will likely be easiest and expose errors best to do the latter
> steps on the secondary machine. There will be another interjection to demonstrate
> when those latter steps begin.

## Computer Setup

[Install Debian](https://www.debian.org/releases/stable/amd64/) on the computer
you will be using as your home server. Of particular use in the linked
instructions are headings 4, 5, and 7. This will probably take a while.

Once you have a working system, add your account to the `sudo` group, replacing
`USERNAME` with your username (you will need to enter the password you chose
for the `root` user after running `su`, but after you do this, you will enter
the password for your user account when running commands with `sudo`.):

```bash
su
sudo adduser USERNAME sudo
```

Restart the machine.

[Disable sleep/hibernation](https://wiki.debian.org/Suspend):

```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

## Installing the Server

Install [Docker](https://docs.docker.com/engine/install/debian/#install-using-the-repository),
as well as some basic tools including `git`:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install -y ca-certificates curl git
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install the Docker packages.
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Set up some directory structure for Synapse and clone this repository locally:

```bash
mkdir -p ~/opt/matrix/data
chmod -R 777 ~/opt/matrix/data
cd ~/opt/matrix
git clone https://github.com/WarmUpBoston/tech.git setup
chmod -R 777 setup
cd setup
```

Edit the included Synapse configuration file, replacing `MATRIX_POSTGRES_PASSWORD` and
`MATRIX_SHARED_SECRET` with distinct strong passwords (I'd recommend using
a password generator like the one built into [Bitwarden](https://bitwarden.com/)).

```bash
nano homeserver.yaml
```

Also, update the Docker Compose configuration file, replacing any instances of
`wub-member-13` with the username you chose for your account on this machine, and
replacing `MATRIX_POSTGRES_PASSWORD` with the same password you used in the `homeserver.yaml`
file.

```bash
nano docker-compose.yml
```

TODO: use the database from a backup instead of starting from scratch

Bring up the database, server, and reverse proxy:

```bash
sudo docker compose up
```

This will print the logs from each container as it starts up. Once you have
confirmed that there are no errors you're running into, you can exit this
command with `CTRL+C`, and then restart the containers (in the background this time):

```bash
sudo docker compose up -d
```

## Creating an Admin User

Create an admin user for the Matrix Synapse server:

```bash
sudo docker compose exec synapse bash
register_new_matrix_user -c /setup/homeserver.yaml
exit
```

Do not name the user `root` or `admin` (literally pick any other name). Again, choose
a strong password, and save it somewhere secure, like in a password manager
(again, I recommend Bitwarden). Make sure to type `yes` when it asks whether to
make the user an admin.

> [!IMPORTANT]
> This is the point at which you should switch to your secondary machine. Make sure you
> are on the same home network as the machine running the server.

## Exposing the Server on the Public Internet

Configure your router to forward a port to your computer. Each router is
different, but on mine, I had to do the following steps:

* Log in to the router by navigating to its IP address in a browser and
  entering the admin password, which I chose when setting up the router
  initially. To find your router's IP address as well as the one for the
  machine you are on, run the `ip route` command on your machine. The IP
  address (will look something like `192.168.1.1`) listed after "`via`" on the
  first line is the router's IP, and the IP address listed after "`src`" is the
  IP address your router has given this machine.
* Set the router to give your machine a static IP address. On my router, this
  is under `Configuration > Connectivity > Local Network > DHCP Reservation`.
  You will need your MAC address for this; you can find it by running `ip
  link`. There may be multiple interfaces listed, e.g. if the machine has both
  an ethernet port and a wi-fi adapter. The device that is actually in use is
  listed in the results of `ip route` on the first line after "`dev`". Look in
  the results of `ip link` for the entry for that device. On the second line of
  that entry, after "`link/ether`", it should show an address that looks like
  `00:00:00:00:00:00`. This is your MAC address. You should enter that along
  with the current IP address for your machine.
* Set the router to forward port `80` on the router to port `80` on your
  machine. This is under `Configuration > Security > Single Port Forwarding` on
  my router. You will need to enter `80` for the value of both the internal
  port and the external port, `TCP/UDP` or `Both` for the protocol, and the local
  IP address for your machine. You may need to restart your router or wait a few
  minutes.

## Setting up DNS

[Check your public IP address](https://whatismyipaddress.com/) (it should be
the value listed next to `IPv4`).

TODO: instructions for creating `A` DNS record

Normally, we would have to set up `https` by creating an SSL certificate; however,
because we registered our domain through Cloudflare and enabled their proxy for
our `A` record, our domain will work with `https` out of the box.

## Registering a Regular User

Go to [the public Element sign-in page](https://app.element.io) and click
`Homeserver > Edit`, enter `https://chat.warmupboston.org`, click `Continue`, and enter
the admin username and password you picked earier in the `Username` and `Password` fields,
then click `Sign In`. In the bottom-left of the screen, click the gear icon, then
click `All Settings`. Click `Help & About` on the left-hand side, scroll down to
`Advanced`, and click `Access Token`.

Create a registration token via the Admin API, replacing `ACCESS_TOKEN` with your
access token:

```bash
curl https://chat.warmupboston.org/_synapse/admin/v1/registration_tokens/new \
  -X POST \
  --header "Authorization: Bearer ACCESS_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"uses_allowed": 1}'
```

In the Element UI, click the profile button in the top left, then click `Sign out`.
Click `Create an account` below the `Sign in` button. Choose a username and password,
and click `Register`. Enter the registration token you received from the Admin API,
then click `Continue`. You should now be logged into a regular user account.

> [!IMPORTANT]
> The admin API access token will expire when you log out, so if you want to register another
> user after this, you will need to log back in to the admin account and follow this same process
> again.

## References

* https://matrix.org/docs/chat_basics/matrix-for-im/
* https://matrix.org/docs/older/understanding-synapse-hosting/
* https://element-hq.github.io/synapse/latest/usage/configuration/config_documentation.html
* https://github.com/element-hq/synapse/tree/develop/contrib/docker
* https://doc.traefik.io/traefik/user-guides/docker-compose/acme-tls/
