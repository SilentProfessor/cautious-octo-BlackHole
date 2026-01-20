# Create pentest directory
sudo mkdir -p /opt/pentest/ddos
cd /opt/pentest/ddos

# Create root-owned venv
sudo python3 -m venv venv --system-site-packages
sudo chown -R root:root venv

# Activate root venv
sudo source venv/bin/activate
