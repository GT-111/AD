# AD

 Unofficial Repository for AD Fair Classification

## Getting Started

### Installation

The installation of our project is super easy.

**Step 1:** Clone the codebase, and compile this codebase:

```
# Clone the codebase
git clone https://github.com/GT-111/AD.git
```

**Step 2:** Create a python environment for the project

```
conda create --name AD python=3.8 -y
conda activate AD 
```

**Step 3:** Install the required packages

```
pip install -r requirements.txt
```

Then you are all set.

## Configuration

To make it easy and clear to perform modifications on the experiment setting, most of the settings can be done by setting the YAML file in *./config* directory. One sample configuration file is provided.



## How to run the project

To make it easy for future development, we built a clear pipeline including dataset splitting, data preprocessing, modeling training and evaluation. All core functions lie in a simple jupyter notebook. 

