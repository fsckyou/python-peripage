# python-peripage
Simple tool that watches for new message images from [sirius-client](https://github.com/fsckyou/sirius-client) 
and then sends the image to a Peripage A6 that is ALREADY paired with the computer and whose
MAC address is stored in `config.py`.

## setup
### Linux and probably Mac
Have Python 3.9+ and have poetry installed (probably via pip). You should have [sirius-client](https://github.com/fsckyou/sirius-client) already configured in the same parent folder that holds this project. Lastly, you need [pybluez](https://github.com/pybluez/pybluez) also in the same parent folder.

To install python dependencies including pybluez, run:
```sh
poetry install
```
and, fingers crossed, all the dependencies should install just fine. 

Then to run the project (and sirius-client), run:
```sh
./start_all.sh
```
### Windows
Oh god - this is a challenge. Go to [this article](https://john.scimone.net/how-to-install-pybluez-on-windows-10-and-11/) and follow those instructions otherwise you'll have no luck.

Then follow the Linux and probably Mac instructions. :)

# Attribution
This project is heavily derived from KTamas' work which can be found [here on Github](https://github.com/tinyprinter/python-paperang) and described [on tinyprinter.club](https://tinyprinter.club). Thanks to him and the other authors who worked on that project and on the [sirius-client](https://github.com/tinyprinter/sirius-client).