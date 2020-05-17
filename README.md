# an0042-flasher

I was given some [tomu][tomu] at [LCA2020][lca], but didn't get them flashed with [toboot][toboot] (which makes it easy to flash firmware using dfu-util), so needed to get that on there.

Luckily you can do that by using xmodem to send toboot over a USB serial connection that the boot loader on board provides. Unluckily it seems that more recent versions of macOS have made it much more likely that you'll hit [a bug in the bootloader][bug] that makes uploads fail.

Thans to that bug I found the python library [xmodem][pyxmodem], which has even been modified to attempt to mitigate this issue, and so I wrapped that in a script that connects to the tomu, starts upload mode, sends toboot, and then tells the device to boot.

Because it still tends to fail a lot, I've alos included a simple script that just keeps retrying the entire process.

[tomu]: https://tomu.im/tomu.html
[lca]: https://lca2020.linux.org.au
[toboot]: https://github.com/im-tomu/toboot
[bug]: https://www.silabs.com/community/mcu/32-bit/forum.topic.html/an0042_bootloader--eQGc

## Prerequisites

I'm not a python person, so I haven't done proper things with requirements.txt or setup.py or what not. Sorry about that!

0. On macOS you'll need Command Line Tools or Xcode installed (definitely will if you use homebrew to install python).
1. Get python3 (on a mac use [homebrew][homebrew] and `brew install python`)
2. Install [pyserial][pyserial] and [xmodem][pyxmodem]. (I did this using: `pip3 install pyserial --user`, `pip3 install xmodem --user`)
3. Plug in your tomu
4. Download [toboot-boosted.bin][dl] and put it in this directory

[dl]: https://github.com/im-tomu/toboot/raw/master/prebuilt/toboot-boosted.bin

## Run

1. Run `ls -lah /dev/cu.usbmodem*` to find the device path for your tomu. For me it's always `/dev/cu.usbmodem3101`, but it could be something else. If you get multiple entries here, proceed with extreme caution - this script does not have any validation and thus you might try and write toboot to something else. Best case it crashes, worse case you could brick that other device. Update the value on the line in flash.py if needed: `serial = serial.Serial('/dev/cu.usbmodemXXXX`)

2. ```./flash-with-retry.sh```

3. If the script fails more than a few times, unplug & replug the tomu, this seems to help. Otherwise, just be patient & it'll likely work eventually. You can also use `python3 reset.py` to tell the boot loader to reset.

[homebrew]: https://brew.sh
[pyserial]: https://pypi.org/project/pyserial/
[pyxmodem]: https://pypi.org/project/xmodem/