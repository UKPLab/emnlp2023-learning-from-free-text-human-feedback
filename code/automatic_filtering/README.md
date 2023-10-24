# Automatic Filtering (Textual Feedback Detection)

This package provides the source code for automatic filtering. It is an installable Python package. You can install it by navigating to this folder and then run `pip install -e .`.

To run the code, you first of all have to update the `config.yaml` file in the config folder. There, you have to adjust the paths to _results_, as well as to your local folders of the _datasets_ to reduce.
Other parameters that you can change are:

- _pairing_ - Set this value to `sentence` if you want to work with error-indicating sentence (like we did in the paper). Set this value to `phrases` if you want to work with just the error-indicating phrases.
- _phrases_ - The path to the phrases file (they are located in the _data_ folder of this project, so you don't have to adjust this value).
- _phrases_ - The path to the sentence file (it is located in the _data_ folder of this project, so you don't have to adjust this value).

After installing this package and the _models_ package, and after adjusting the values in the config file, you run automatic filtering (at best) directly from the _src_ folder by running `python main.py`. This starts a command-line interface where you can start TFD.

__Other Requirements:__

We've tested our code on Cent OS Linux 7 (Fedora). We've used Python >3.8 in our experiments (but we don't use any version-specific stuff).