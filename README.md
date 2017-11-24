# pi-airspeaker

1. Disable swapping
sudo dphys-swapfile swapoff
sudo dphys-swapfile uninstall
sudo update-rc.d dphys-swapfile remove

2. Redirect /var/log to ram.
Add the following lines to the end of /etc/fastab

tmpfs	/var/log	tmpfs	defaults,noatime,mode=0755 0 0
tmpfs	/tmp		tmpfs	defaults,noatime,mode=1777 0 0

3. Install shairport
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y git autoconf libtool libdaemon-dev libasound2-dev libpopt-dev libconfig-dev
sudo apt-get install -y avahi-daemon libavahi-client-dev
sudo apt-get install -y libssl-dev

git clone https://github.com/mikebrady/shairport-sync.git
cd shairport-sync/
autoreconf -i -f
./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd --with-metadata
make
sudo make install
sudo systemctl enable shairport-sync

4. Configure sound to go via USB sound card
sudo amixer cset numid=3 1

Add the following lines to /etc/asound.conf
pcm.!default  {
 type hw card 1
}
ctl.!default {
 type hw card 1
}

5. Tunables
Add the following lines to /boot/config.txt
audio_pwm_mode=2
disable_audio_dither=1

Adjust max volume to reasonable level
sudo alsamixer -c 1

6. Configure shairport
Replace existing shairport-sync.conf in /usr/local/etc/
Replace existing asound.conf in /etc/

6. Install mute script
git clone 
sudo mv ./mute.py /usr/local/bin/
sudo chmod +x /usr/local/bin/mute.py
sudo chown root:staff /usr/local/bin/mute.py


