<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Movie Recommendation System - Content-Based Approach</h1>

<p>This project demonstrates a movie recommendation system built using a content-based approach. The system recommends movies to users by analyzing and comparing the features of different movies to identify similarities.</p>

<h2>Dataset</h2>
<p>The dataset utilized in this project is sourced from <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata">Kaggle: TMDB Movie Metadata</a>. This dataset includes a wide range of information about movies, such as genres, cast, crew, and keywords.</p>

<h2>Pre-processing</h2>
<p>To prepare the dataset for the recommendation system, the following pre-processing steps were undertaken:</p>
<ul>
    <li><strong>Text Vectorization:</strong> Movie descriptions and other text-based features were converted into numerical vectors using the <code>sklearn</code> library to facilitate similarity calculations.</li>
    <li><strong>Text Stemming:</strong> Applied text stemming techniques to normalize words by reducing them to their root forms, improving the consistency of the data.</li>
</ul>

<h2>Installation</h2>
<p>To run this project locally, follow these steps:</p>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/safnusamad/movie-recommendation-nlp.git</code></pre>
    </li>
    <li>Navigate to the project directory and install the required dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the Jupyter Notebook:
        <pre><code>jupyter notebook</code></pre>
    </li>
</ol>

<h2>Exploratory Data Analysis (EDA)</h2>
<p>Exploratory Data Analysis is conducted in the <code>EDA.ipynb</code> file. This notebook includes a range of visualizations and statistical analyses to gain insights into the dataset. To explore the EDA:</p>
<ol>
    <li>Open the Jupyter Notebook:
        <pre><code>jupyter notebook EDA.ipynb</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<p>After running the notebooks, you can explore how the recommendation system works by analyzing the results produced by the model.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request with your changes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. For more details, please refer to the <a href="LICENSE">LICENSE</a> file.</p>

</body>
</html>
