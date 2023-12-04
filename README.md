# README for Subtitle Translation Script

## Overview

This script is designed to translate subtitle files from one language to another, using the `googletrans` Python library. It is specifically configured to work with SubRip Subtitle (SRT) files. The script reads an SRT file, translates the text, and saves the translated subtitles to a new file.

## Features

- **Subtitle File Translation**: Translates the contents of an SRT file into a specified target language.
- **Support for Numerical Lines**: Numerical lines in SRT files, which represent the subtitle sequence numbers, are preserved in the translated file.
- **Preservation of Formatting**: The script maintains the original formatting of the SRT file, including timestamps and blank lines.

## Requirements

- Python 3
- `googletrans` Python library

## Installation

1. Ensure that Python 3 is installed on your system.
2. Install the `googletrans` library using pip:

    ```bash
    pip install googletrans
    ```

## Usage

1. Place the SRT file you wish to translate in the same directory as the script.
2. Modify the `file_name` variable in the script to match the name of your SRT file.
3. Set the target language in the script by changing the `dest` parameter in the `translate` method. For example, use `'fa'` for Farsi.
4. Run the script:

    ```bash
    python main.py
    ```

5. The translated subtitles will be saved in a new file in the same directory.

## Supported Languages

The script supports various languages as provided by the `googletrans` library. Refer to the `googletrans` documentation for a full list of supported languages and their corresponding language codes.

## Limitations

- The script does not translate text within parentheses or brackets, which are often used for sound effects or off-screen dialogue.
- The quality of translation depends on the `googletrans` library and may vary for different languages.

