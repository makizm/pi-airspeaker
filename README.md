# pi-airspeaker

## Raspberry Pi tuning (optional)
1. Disable swapping
   ```
   sudo dphys-swapfile swapoff
    sudo dphys-swapfile uninstall
    sudo update-rc.d dphys-swapfile remove
   ```

1. Redirect /var/log to ram.
   Add the following lines to the end of /etc/fastab
    ```
    tmpfs	/var/log	tmpfs	defaults,noatime,mode=0755 0 0
    tmpfs	/tmp		tmpfs	defaults,noatime,mode=1777 0 0
    ```

## Install Docker
https://docs.docker.com/engine/install/debian/

## Build and run as Docker container
1. Download the stuff.
    ```
    sudo apt-get update
    sudo apt-get install -y git

    git clone https://github.com/mikebrady/shairport-sync.git
    cd shairport-sync/
    ```
2. Find out output device ID by running command `aplay -l`.
    ```
    # aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: Headphones [bcm2835 Headphones], device 0: bcm2835 Headphones [bcm2835 Headphones]
    Subdevices: 8/8
    Subdevice #0: subdevice #0
    Subdevice #1: subdevice #1
    Subdevice #2: subdevice #2
    Subdevice #3: subdevice #3
    Subdevice #4: subdevice #4
    Subdevice #5: subdevice #5
    Subdevice #6: subdevice #6
    Subdevice #7: subdevice #7
    card 1: vc4hdmi [vc4-hdmi], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
    Subdevices: 1/1
    Subdevice #0: subdevice #0
    card 2: Set [C-Media USB Headphone Set], device 0: USB Audio [USB Audio]
    Subdevices: 1/1
    Subdevice #0: subdevice #0
    ```
3. Configure Alsa output device from previous step. In this case I am using **C-Media USB** card `2`, so the `hw` ID will be `2`. Audio output device ID is always `0` so can be omitted.
   - Edit configuration file `shairport-sync.conf` and set `output_device` property under `alsa` to `hw:2`.
4. Build Docker image
   ```
   docker build --tag pi-airspeaker .
   ```
5. Start Docker container
   
   a. Start as service using default configuration file
   ```
    docker run -d --restart unless-stopped \
    --net host \
    --device /dev/snd \
    --device /dev/gpiomem \
    --name pi-player pi-airspeaker
    ```
    b. Start as service using persistent configuration file.
    ```
    docker run -d --restart unless-stopped \
    --net host \
    --device /dev/snd \
    --device /dev/gpiomem \
    --volume /etc/shairport-sync.conf:/etc/shairport-sync.conf:ro
    --name pi-player pi-airspeaker

    ```

## Circuit Diagram
<img src="https://raw.githubusercontent.com/makizm/pi-airspeaker/master/circuit_diagram.png"/>

## Parts used to build hardware
1. Polkaudio RC60i speaker
2. LM2596 DC/DC power supply step down module
3. TPA3118 mono amplifier
4. CM109 USB audio adapter
5. AOP605 IC