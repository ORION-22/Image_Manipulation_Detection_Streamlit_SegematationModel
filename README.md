# Image Manipulation Detection Streamlit SegmentationModel

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

Image Manipulation Detection Streamlit SegmentationModel is a project that aims to detect image manipulation using Streamlit and the SegmentationModel library. This repository provides an easy-to-use web application built with Streamlit and utilizes a pre-trained image segmentation model to identify manipulated areas in an image.

## Features

- Upload an image: Users can upload an image file to be analyzed for image manipulation detection.
- Image segmentation: The application uses a pre-trained segmentation model to segment the uploaded image into different regions.
- Manipulation detection: The segmented image regions are analyzed to detect potential areas of manipulation or tampering.
- Visualization: The detected manipulated regions are highlighted and visualized on the original image, allowing users to easily identify the manipulated areas.

## Demonstration

https://github.com/ORION-22/Image_Manipulation_Detection_Streamlit_SegematationModel/assets/68912454/38815c52-71a6-41cb-bb12-d1be4116b0f9


## Installation

To run the application locally, follow these steps:

1. Clone the repository:
```console
git clone https://github.com/ORION-22/Image_Manipulation_Detection_Streamlit_SegematationModel.git
```

2. Change into the project directory:
```console
cd Image_Manipulation_Detection_Streamlit_SegmentationModel
```

3. Install the required dependencies:
```console
pip install -r requirements.txt
```
4. Run the Streamlit application:
```console
streamlit run app.py
```
The application will be accessible at `http://localhost:8501` in your web browser.

## Usage

1. Open the application in your web browser by visiting `http://localhost:8501` after running the Streamlit application.

2. Click on the "Browse" button to upload an image file for manipulation detection.

3. Wait for the image to be processed and the manipulation detection results to be displayed.

4. The manipulated areas will be highlighted in the image, allowing you to identify potential tampering.

5. Optionally, you can adjust the sensitivity or parameters of the detection algorithm using the provided settings.

6. Upload and analyze additional images as needed.


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The SegmentationModel library: [Link to SegmentationModel](https://github.com/qubvel/segmentation_models.pytorch)
- Streamlit: [Link to Streamlit](https://streamlit.io/)

## Contact

Feel free to explore, use, and contribute to this image manipulation detection project! We appreciate your support and hope it proves useful in identifying potential tampering in images.

