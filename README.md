
# ckanext-feature-image

This extension includes the `feature_image` plugin. The plugin ables system admins to upload a featured image with caption for the CKAN homepage.


## Screenshots 

![feature_image1](https://user-images.githubusercontent.com/16546640/139218388-18e1c0ec-b26b-4f1c-99fc-5d571a9f2507.png)


![feature_image2](https://user-images.githubusercontent.com/16546640/139218544-984bfc71-7bb1-4d80-b9c6-7e725e5f5663.png)



## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
|  2.9 | Yes    |
| earlier | Not Tested |           |



## Installation


To install ckanext-feature-image:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/TIBHannover/ckanext-feature-image.git
    cd ckanext-feature-image
	pip install -r requirements.txt
    python setup.py develop

3. Add `feature_image` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


