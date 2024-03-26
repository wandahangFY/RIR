# Random Interpolation Resize: A Free Image Data Augmentation Method for Object Detection in Industry

## Introduction
In industrial machine vision detection tasks, data scarcity is a common issue. Data augmentation artificially incorporates prior knowledge of human vision, expands image data, improves model performance, and has become a standard configuration for models. However, most current data augmentation methods are designed for general scenarios, with few specifically tailored for industrial object detection image enhancement.

This repository includes a novel image data augmentation method, Random Interpolation Resize (RIR), designed specifically for industrial object detection tasks. We have changed the interpolation method in the standard resizing step of preprocessing from a fixed configuration to a random selection to expand image data and enhance the model's generalization and detection capabilities.
![RIR principle diagram is shown below:](RIR.png)

## Paper Link
- [Random Interpolation Resize: A Free Image Data Augmentation Method for Object Detection in Industry](https://www.sciencedirect.com/science/article/pii/S0957417423008576)

## Chinese Interpretation Link
- [RIR Chinese Interpretation](Chinese Interpretation Link) [TODO: Will be written and updated later if necessary]

## Video Tutorial Link
- [RIR Video Interpretation and Secondary Innovation Solutions]() [Currently, there is a detailed tutorial in text PPT format; TODO: Will be written and updated with the video if necessary]

## Secondary Innovation Points Summary and Code Implementation (TODO)
- [Secondary Innovation Solutions]() [The last page of the PPT tutorial provides some secondary innovation solutions; TODO: Will be written and updated with the code if necessary]

## Citation Format
If the project and article have been helpful to you, please cite the following paper:

@article{WAN2023120355,
title = {Random Interpolation Resize: A free image data augmentation method for object detection in industry},
journal = {Expert Systems with Applications},
volume = {228},
pages = {120355},
year = {2023},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2023.120355},
url = {https://www.sciencedirect.com/science/article/pii/S0957417423008576},
author = {Dahang Wan and Rongsheng Lu and Ting Xu and Siyuan Shen and Xianli Lang and Zhijie Ren},
keywords = {Data augmentation, Image interpolation, Object detection, Industry applications, Deep learning algorithm, Convolutional neural network},
}

For example:

Dahang Wan, Rongsheng Lu, Ting Xu, Siyuan Shen, Xianli Lang, Zhijie Ren,
Random Interpolation Resize: A free image data augmentation method for object detection in industry,
Expert Systems with Applications,
Volume 228,
2023,
120355,
ISSN 0957-4174,
https://doi.org/10.1016/j.eswa.2023.120355.

## Reference Links
- [Code for Overall Framework: YOLOv5](https://github.com/ultralytics/yolov5)
- [YOLOv7](https://github.com/WongKinYiu/yolov7)
- [YOLOv8](https://github.com/ultralytics/ultralytics)
- [Albumentations Data Augmentation Library](https://github.com/albumentations-team/albumentations)

## Conclusion
Thank you for your interest and support in this project. The authors strive to provide the best quality and service but acknowledge that there is always room for improvement. If you encounter any issues or have any suggestions, please let us know.
Furthermore, this project is currently maintained by me personally, so there may be oversights and errors. If you find any problems, feel free to provide feedback and suggestions.

## Other Open Source Projects
Other open-source projects will be gradually organized and released. Please check the author's homepage for downloads in the future.
[Homepage](https://github.com/wandahangFY)

## FAQ
1. README.md file addition (completed)
2. Detailed tutorials (YOLOv7 and YOLOv8 have been updated)
3. Project environment setup (RIR data augmentation is plug-and-play; the entire project is based on YOLOv5-6.1 version, refer to the README-YOLOv5.md file and requirements.txt for configuration)
4. Folder descriptions (consistent with YOLOv5-6.1, no changes to hyperparameters) (TODO: Detailed explanation)
5. Secondary innovation points summary and code implementation (Detailed instructions provided on the last page of the RIR usage tutorial.pptx)
6. Paper illustrations (Due to journal copyright issues, the source files for the PPT are not provided):
   - Conceptual diagrams, network structure diagrams, flowcharts: PPT (Personal choice, can also use Visio, Edraw, AI, etc.)
   - Experimental comparisons: Orgin (matlab, python, R, Excel all can be used)