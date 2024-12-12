[Unit]
Description=Photo Frame
Wants=graphical.target
After=graphical.target

[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/<USER>/.Xauthority
Environment=XDG_RUNTIME_DIR=/run/user/<ID>
Type=simple
ExecStart=/bin/bash /home/temppi/SeasonalStory/tempPi.sh
Restart=always
User=1000
Group=1000

[Install]
WantedBy=graphical.target

#! To enable run the following command in the terminal: 
#! sudo systemctl enable temp --now