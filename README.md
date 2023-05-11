# Pathway Analysis Tool

## Overview

This web application is designed to find overlapping proteins on the somascan menu based on a list of UniProt IDs. It takes in a list of UniProt IDs in a specific format and returns the proteins that overlap with the somascan menu. The application is implemented using Streamlit, a popular Python library for building interactive web applications.

## Usage

### Prerequisites

- Python 3.7 or above
- pip package manager

### Installation

1. Clone the repository from GitHub:

```
git clone https://github.com/jonathjd/streamlit-biomarker.git
```

2. Navigate to the project directory:

```
cd streamlit-biomarker
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

### Running the Application

1. Once the dependencies are installed, start the web application by running the following command:

```
streamlit run main.py
```

2. The application will start running and display a URL in the console, which you can open in your web browser.

3. Access the application by clicking on the provided link or by navigating to `http://localhost:8501` in your web browser.

4. The web application interface will be displayed, ready for you to use.

### Using the Application

1. Input the list of UniProt IDs in the specified format:

```
UniProtKB:P0CJ72    Humanin-like 5
UniProtKB:Q6UX68    XK-related protein 5
UniProtKB:Q6UX65    DNA damage-regulated autophagy modulator protein 2
UniProtKB:P36897    TGF-beta receptor type-1
UniProtKB:P36896    Activin receptor type-1B
```

2. Click on the "Find Overlapping Proteins" button.

3. The application will process the input and display the proteins that overlap with the somascan menu.

## Additional Information

### Repository

The source code for the application can be found in the following GitHub repository:

[https://github.com/jonathjd/streamlit-biomarker](https://github.com/jonathjd/streamlit-biomarker)

### Issues

If you encounter any issues or have suggestions for improvement, please create a new issue in the GitHub repository's issue tracker.

### Credits

This application was developed by [jonathjd](https://github.com/jonathjd).
