<a id="readme-top"></a>

<div align="center">
  <h1 align="center">Plastic Waste Profiling.</h1>
  <p align="center">
    Project Deep Blue Season 04
    <br />
    <br />
  </p>
</div>

## Technologies Used
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.javascript.com/)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)


## Overview
This project, completed as part of Project Deep Blue Season 4 organized by Mastek and Majesco, aims to support the Swachh Bharat mission by developing technology that helps local authorities assess the effectiveness of garbage segregation in communities. The project focuses on analyzing images of garbage dumps to identify manufacturers contributing to plastic waste through their packaging. By leveraging advanced image processing and AI techniques, the system can track and create profiles of these manufacturers. The expected outcome is a publicly accessible platform where the environmental footprint of these companies can be monitored, helping to hold them accountable and promote more responsible waste management practices in India.


## Implementation
### User Roles and Responsibilities
The application has three main actors. 
-  **User:** The user plays a crucial role in data collection by capturing photographs of garbage dumps, littered waste, or heaps of garbage in their surroundings. They upload these images to the website, contributing to the database that the system will analyze. This input is essential for identifying and tracking the sources of plastic waste.
-  **PWP Web Client:** The PWP (Plastic Waste Profiling) application is the analytical engine of the system. It processes the images uploaded by users, utilizing advanced image processing and AI techniques to identify brands associated with the waste. The application then updates existing profiles or creates new ones for these brands, building a comprehensive database of manufacturers and their environmental impact.
-  **Authorities:** Authorities are the decision-makers who leverage the insights provided by the PWP application. Through access to the web client's dashboard, they can view in-depth visualizations that highlight the volume and types of plastic waste produced by various brands. These insights empower authorities to implement targeted actions and policies aimed at reducing plastic waste, holding manufacturers accountable, and promoting better waste management practices.
<div align="center">
    <img width="720" alt="image" src="https://github.com/user-attachments/assets/5da4dd75-7329-4d3d-81cd-73b0b36af91e">
    <div>Actors in the Plastic Waste Profiling application.</div>
</div>

### How the PWP Web Client Works
When a user uploads an image of a garbage dump, the PWP Web Client initiates a series of processes to analyze and identify the brands contributing to the waste. Here's a step-by-step breakdown of how it works:
- **Image Upload and Preprocessing**
    - Once the image is uploaded, the system first preprocesses it to enhance its quality for better analysis. This includes resizing, noise reduction, and contrast adjustment to ensure that the relevant features in the image are clearly distinguishable.
- **Object Detection and Segmentation**
    - The preprocessed image is then passed through a Convolutional Neural Network (CNN) model, specifically using the TensorFlow Object Detection API, which has been fine-tuned on our dataset. This model is trained to detect and segment different objects within the image, with the primary objective of isolating plastic waste items from the rest of the image. The model is capable of identifying various types of plastic packaging, such as bottles, wrappers, and bags.
- **Brand Identification**
    - After the plastic waste items are segmented, the system employs an additional deep learning model to identify the brand logos or text on the packaging. This model combines a fine-tuned SSD MobileNet model for object classification with an Optical Character Recognition (OCR) module. The OCR extracts any text present on the packaging, allowing the system to reduce the number of classifications needed. If logos are not detected on the packaging, the MobileNet model is bypassed, significantly reducing processing time and thereby accelerating the overall analysis. The OCR handles text extraction, while the MobileNet model focuses on recognizing logos or brand-specific patterns.
- **Profile Creation and Updating**
    - Once the brands are identified, the PWP Web Client checks its existing database to see if profiles for these brands already exist. If a profile exists, the system updates it with the new data from the uploaded image, including the type and quantity of waste identified. If no profile exists, the system creates a new one, linking it to the identified brand.
- **Data Storage and Visualization**
    - All the analyzed data, including brand names, types of waste, and quantities, are stored in the database. The PWP Web Client then generates visualizations from this data, which are accessible on the dashboard page for authorities. These visualizations include charts, graphs, and heatmaps that detail the volume of plastic waste produced by different brands over time and across various locations.
- **Decision-Making Support**
    - The final output is a comprehensive set of visual tools that authorities can use to make informed decisions. They can view trends in plastic waste generation, identify the most significant polluters, and take appropriate actions to encourage or enforce better waste management practices among manufacturers.

This multi-step process, powered by state-of-the-art AI and ML models, enables the PWP Web Client to effectively track the environmental impact of plastic waste and support efforts to reduce pollution.
