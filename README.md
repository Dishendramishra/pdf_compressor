# Flask app for PDF compression

A demo web app for PDF compression.

Python Module Used: [GitHub - theeko74/pdfc: Simple python script to compress PDF](https://github.com/theeko74/pdfc)

# Deply using single command

Tested on Ubuntu-22.04.5 LTS Server

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Dishendramishra/pdf_compressor/refs/heads/main/deploy_app.sh)"
```

**Platform Dependencies:**

- Install dependency Ghostscript. 
  - On MacOSX: `brew install ghostscript` 
  - On Windows: install binaries via [official website]([https://www.ghostscript.com/](https://www.ghostscript.com/))
  - On Ubuntu:  `sudo apt install ghostscript`
  - On RHEL, CentOS: `yum install ghostscript`

**Python Dependencies:**

Install python dependencies using the file `requirements.txt` :

`pip install -r requirements.txt`

#### Running App

`python app.py`

### Points to Ponder while depolying

The app was deployed on **Ubuntu  Server 22.04.5 LTS**, using **Apache/2.4.52** and **mod_wsgi**. 

To install the dependencies mentined above use the command below:

```bash
 sudo apt install libapache2-mod-wsgi-py3 apache2
```

You may like to enable reverse_proxy in apache2

```bash
sudo a2enmod proxy_http
```

### Some useful commands

**Disable apache at start on ubuntu**

you could simply disable it by:

```
sudo update-rc.d apache2 disable
```

and then if you would like to enable it again:

```
sudo update-rc.d apache2 enable
```
