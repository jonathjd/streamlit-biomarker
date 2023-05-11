# Pathway Analysis Tool

Streamlit-Biomarker is an web application used to find the overlab between gene ontology disease associated biomarkers and the SomaScan 7k panel. The application will take in a list of the biomarkers of interest and find the overlap between the SomaScan assay and provide a table as well as some visualizations regarding the results

Link to application: https://biomarker-somalogic.streamlit.app/
![Screen Shot 2023-02-01 at 9 13 31 PM](https://user-images.githubusercontent.com/66283742/216237471-ed521b04-6366-49e8-850f-29edbeaadc9f.png)

# How it's Made:
**Tech Used:** Python (Streamlit), Some injected HTML and CSS (lol)

![alt-text](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![alt-text](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![alt-text](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)

A very common question that customers want to know is what the overlap is between the SomaScan 7k discovery panel and their disease of interest (e.g. inflammation). Finding the overlap between these two subsets of proteins can be an ardous process. This web application was made to expedite that process and provide insight along the way.

Streamlit was for the front end for rapid development time and ease of use. An excel file is used to store the SomaScan assay list, however this list is/will be updated with more analytes. In the future a database connection will need to be made to avoid updating this static file.

