#!/bin/bash
# This is the Easymap ato-installation script, its meant for facilitating the installation of Easymap for the general user in different Unix distributions. 
# Administraror privileges are required for the execution of this installer. 

# A link to the main Easymap github repository
git_address='https://github.com/MicolLab/easymap.git'

# Default access port: 8100, can be changed adding it as an argument to the script.
if ! [ $1 ]; then
	port=8100

elif [ "$1" -ge 8100 ] && [ "$1" -le 8200 ]; then
	port=$1

else
	echo 'Please choose a port number between 8100 and 8200.'
	exit
fi

# First the user selects the Operative System used with a  simple menu. Then the script installs different dependencies in each case and clones 
# easymap from the main repository. Finally, it runs the install.sh file inside the Easymap folder for a default installation using port 8100
# as the access point to the web interface. 

echo '
Welcome to the Easymap installer, please select your Operating System:

'
PS3='

Enter a number: '

distrs='Ubuntu_18 Ubuntu_16 Ubuntu_14 Linux_AMI Linux_Redhat  OS_X(Yosemite) Quit'
select dis in $distrs
do
	if [ $dis == 'Quit' ]
	then
		echo 'Installation canceled. ' 
		break
	else
		echo 'Beggining Easymap installation in' $dis'. Please wait for the process to finish, it could take up to 30 minutes.'
		sleep 4s
	fi

	if [ $dis == 'Ubuntu_18' ]
	then
		apt-get update  
		apt-get install build-essential zlib1g-dev libbz2-dev git wget tar zip liblzma-dev libncurses5-dev libncursesw5-dev libssl1.0-dev -y
		git clone $git_address 
		chmod -R 755 easymap
		cd easymap
		./install.sh server $port
	fi

        if [ $dis == 'Ubuntu_16' ] || [ $dis == 'Ubuntu_14' ]
        then
		apt-get update
		apt-get install build-essential zlib1g-dev libbz2-dev git wget tar zip liblzma-dev libncurses5-dev libncursesw5-dev libssl-dev -y
		git clone $git_address
		chmod -R 755 easymap
		cd easymap
		./install.sh server $port
        fi

        if [ $dis == 'Linux_AMI' ]
        then
                yum groupinstall -y "Development Tools"
		yum groupinstall -y "Development Libraries"
		yum install -y wget zlib-devel bzip2-devel git ncurses-devel ncurses openssl-devel
		yum install -y xz-devel
		git clone $git_address
		chmod -R 755 easymap
		cd easymap
		./install.sh cli
		nohup sudo -u $SUDO_USER `./src/Python-2.7.12/.localpython/bin/python -m CGIHTTPServer $port`

        fi

        if [ $dis == 'Linux_Redhat' ]
        then
                echo 'UNDER DEVELOPMENT'
		yum groupinstall -y "Development Tools"
		yum groupinstall -y "Development Libraries"
		yum install -y wget zlib-devel bzip2-devel git ncurses-devel ncurses openssl-devel
		yum install -y xz-devel
		git clone $git_address
		chmod -R 755 easymap
		cd easymap
		./install.sh server $port
        fi

	if [ $dis == 'OS_X(Yosemite)' ]
	then
		echo 'UNDER DEVELOPMENT'
		xcode-select --install
		brew install zlib xz bzip2 git
		git clone $git_address
		chmod -R 755 easymap
		cd easymap
		./install.sh server $port
	fi
	break
done
