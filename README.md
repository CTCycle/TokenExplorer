# TokenExplorer: Exploring Tokenizers and Their Characteristics

## 1. Project Overview
Tokenizers play a pivotal role in the preprocessing phase of text data, transforming raw text into a structured format that models can understand. The effectiveness of this step significantly impacts the overall performance of NLP models, making the choice of tokenizer a crucial decision in the development of language-based applications. However, with the plethora of tokenizers available, each with its unique approach and capabilities, selecting the most suitable one can be a daunting task. TokenExplorer aims to offer a comprehensive toolkit for analyzing and comparing the performance and characteristics of open source tokenizers (currently based on English language), through a simple yet effective jupyter notebook. This facilitates the exploration of tokenizer characteristics such as tokenization speed, token granularity, handling of special characters, language support, and adaptability to domain-specific vocabularies. Users can perform detailed comparisons between tokenizers, assessing their suitability for specific applications, such as text classification, sentiment analysis, language translation, or semantic search.

## 2. Installation 
The installation process on Windows has been designed for simplicity and ease of use. To begin, simply run *start_on_windows.bat.* On its first execution, the installation procedure will automatically start with minimal user input required. The script will check if either Anaconda or Miniconda is installed on your system. If neither is found, it will automatically download and install the latest Miniconda release from https://docs.anaconda.com/miniconda/. After setting up Anaconda/Miniconda, the installation script will proceed with the installation of all necessary Python dependencies. If you'd prefer to handle the installation process separately, you can run the standalone installer by executing *setup/install_on_windows.bat*. 

**Important:** After installation, if the project folder is moved or its path is changed, the application will no longer function correctly. To fix this, you can either:

- Open the main menu, select *Setup and maintentance* and choose *Install project in editable mode*
- Manually run the following commands in the terminal, ensuring the project folder is set as the current working directory (CWD):

    `conda activate TOKEXP`

    `pip install -e . --use-pep517` 

## 3. How to use
On Windows, run *start_on_windows.bat* to launch the main navigation menu and browse through the various options. Please note that some antivirus software, such as Avast, may flag or quarantine python.exe when called by the .bat file. If you encounter unusual behavior, consider adding an exception for your Anaconda or Miniconda environments in your antivirus settings.

### 3.1 Navigation menu

**1) Run tokenizers benchmarks:** runs the benchmarks on all selected tokenizers and save the results in *resources/benchmarks*. 

**1) Tokenizers analysis:** launch a jupyter notebook to visualize benchmarks results for all given tokenizers (required generating the benchmarks results first).

**2) TokenExplorer setup:** allows running some options command such as *install project in editable mode* to run the developer model project installation, and *remove logs* to remove all logs saved in *resources/logs*.  

**3) Exit and close:** exit the program immediately

### 3.1 Resources
This folder is used to hold tokenizers and datasets, as well as to store the results of vaiorus benchmarks. Here are the key subfolders:

**benchmarks:** contains the results of the tokenizers benchmarks that have been run. Generate plots are saved in *benchmarks/figures* while benchmark .csv files will be located in *benchmarks/results*.

**datasets:** contains the downloaded datasets that are used to test the tokenizers performance. While the datasets that are automatically downloaded are saved in *datasets*, the custom dataset are saved in *custom dataset*.

**tokenizers:** contains the downloaded tokenizers that are used to run the benchmarks on the target dataset. While the tokenizers from HuggingFace are automatically saved in *tokenizers*, the custom tokenizers must be located in *custom tokenizers*.

## 4. Configurations
For customization, you can modify the main configuration parameters using *settings/configurations.json* 

#### General configuration

| Parameter          | Description                                                    |
|--------------------|----------------------------------------------------------------|
| ACCESS_TOKEN       | The personal access token from HuggingFace, required for the   |
|                    | download of certain tokenizers                                 |
| TOKENIZERS         | List of tokenizers to download                                 |
| DATASET            | Target dataset to benchmark tokenizers (it is needed to        |
|                    | provide the config and corpus references)                      |

#### Benchmark configuration

| Parameter                | Description                                              |
|--------------------------|----------------------------------------------------------|
| MAX_NUM_DOCS             | Maximum number of documents to use from the dataset      |
| REDUCE_CSV_SIZE          | List of tokenizers to download                           |
| INCLUDE_CUSTOM_DATASET   | Whether or not to include the custom dataset             |
| INCLUDE_CUSTOM_TOKENIZER | Whether or not to include the custom tokenizers          |

## 5. License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.

