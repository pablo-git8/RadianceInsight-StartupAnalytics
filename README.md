## RadianceInsight-StartupAnalytics

![python](http://ForTheBadge.com/images/badges/made-with-python.svg)
![jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

<p align="center">
	<img src="https://raw.githubusercontent.com/pablo-git8/RadianceInsight-StartupAnalytics/main/images/radiance.png" alt="400" width="600"/>
</p>

Welcome to the RadianceInsight-StartupAnalytics repository! This project, spearheaded by Radiance Group Consulting, is an advanced statistical analysis platform focused on dissecting the intricate details of startup foundations. Our goal is to provide insightful, data-driven analyses of startup foundations, funding dates, financial resources, geographic distributions, and categorical segmentation. 

Here an example of the posible analysis possible with the RadianceInsight:

<p align="center">
	<img src="https://raw.githubusercontent.com/pablo-git8/RadianceInsight-StartupAnalytics/main/images/plot.png" alt="400" width="600"/>
</p>

### Project Description

RadianceInsight-StartupAnalytics offers a comprehensive suite of tools and analyses to understand the startup ecosystem better. The project includes a special focus on the probabilities of companies securing funding within their first six months. We leverage a variety of technologies and libraries to ensure accurate and insightful analyses.

### Project Structure

- **Data Ingestion**:
  - `/data`: Directory for storing raw and processed CSV files, as well as JSON files for categorization.

- **Data Wrangling and Transformations**:
  - `1_ProblemStatement.ipynb`: Jupyter notebook outlining the problem statement.
  - `2_CategoryBucketCreation.py`: Python script to create the JSON file with defined categories.
  - `2_DataWrangling.ipynb`: Development notebook for data wrangling processes.
  - `2_ProcessStartups.py`: Python script for a pipeline to wrangle and process raw data.

- **Exploratory Data Analysis (EDA)**:
  - `3_EDA_Startups.ipynb`: Jupyter notebook for Exploratory Data Analysis on startup datasets.

- **Helpers**:
  - `helper_functions.py`: Python file containing helper functions developed for the project.
  - `helper_variables.py`: Python file containing helper variables used across the project.

### Technologies and Libraries

This project utilizes a range of technologies and libraries for data ingestion, processing, analysis, and visualization. Some key technologies include:

- Python for scripting and data processing.
- Pandas and NumPy for data manipulation.
- Matplotlib and Seaborn for data visualization.
- Jupyter Notebooks for interactive development and analysis.

### Getting Started

To get started with this project:
1. Clone this repository.
2. Navigate to the project directory.
3. Follow the setup instructions in the `README.md` file to install necessary dependencies.

### Contribution

Contributions to improve or enhance the project are welcome. Please read the contribution guidelines before submitting a pull request.

### License

This project is licensed under the MIT License. See the `LICENSE.md` file for more details.

### Contact

For further information or assistance, contact us at [contact@radiancegroupconsulting.com](mailto:contact@radiancegroupconsulting.com).

We invite you to join us in exploring the dynamic world of startups with RadianceInsight-StartupAnalytics!
