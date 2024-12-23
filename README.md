COMPRESSORELITE 
Compressor/Decompressor Tool
Student Name: Dhruv Pandey, Arya Tiwari
Student Regd. No and Batch: E23CSEU1504
Course: CSET101: Computational Thinking and Programming
Lab Instructor: Ms. Mohini Chakraborty
Submission Date: 23 November 2023

Abstract
The file compressor/decompressor Python application is designed to compress and decompress files in various formats (GZIP, ZIP, RAR) using different algorithms. This project report summarizes the objectives, methodology, implementation, and outcomes of this project.

1. Introduction
1.1 Background
In today's digital world, file compression plays a crucial role in optimizing storage space and transferring data efficiently. This project aims to create a versatile file compressor/decompressor tool using Python to address the need for an accessible and adaptable compression tool.

1.2 Problem Statement
Existing file compression tools often lack support for multiple formats or user-friendly interfaces. This project seeks to create an intuitive application that supports various compression formats (GZIP, ZIP, RAR) and provides configurable compression levels while ensuring ease of use.

1.3 Objectives
The primary objectives of this project include:
- Developing a user-friendly GUI-based file compression and decompression tool.
- Supporting GZIP, ZIP, and RAR formats with different compression algorithms and levels.
- Optimizing processing speed without compromising compression efficiency.

2. Methodology
2.1 Tools and Technologies Used
The application is built using Python, leveraging the tkinter library for the graphical user interface. Additionally, the gzip, zipfile, and py7zr libraries are employed to handle compression and decompression functionalities.

2.2 Project Design
The design involves a simple yet efficient GUI interface constructed using the tkinter framework to interact with users. The backend operations encompass various functions from gzip, zipfile, and py7zr libraries to perform compression and decompression tasks.

2.3 Implementation Details
The application allows users to:
- Choose file compression formats (GZIP, ZIP, RAR).
- Specify compression levels for enhanced optimization.
- Perform compression and decompression operations on selected files.
- Employ threading to execute compression and decompression asynchronously, ensuring GUI responsiveness.

3. Results and Discussion
3.1 Project Outcomes
The application delivers successful compression and decompression of files in GZIP, ZIP, and RAR formats. By allowing users to adjust compression levels, the tool strikes a balance between compression efficiency and processing speed.

3.2 Challenges Faced
- Ensuring thread safety and GUI responsiveness during file operations.
- Balancing compression efficiency and processing speed based on selected compression levels.

3.3 Learnings and Insights
- Understanding and managing threading in GUI applications for seamless user experience.
- Fine-tuning compression levels to optimize file size without compromising quality.

4. Conclusion
The file compressor/decompressor project achieved its primary goal by providing a functional tool for handling various file formats. Further optimizations can be explored to enhance performance while maintaining compression efficiency.

References
- Python Documentation: https://docs.python.org/
- tkinter Documentation: https://docs.python.org/3/library/tkinter.html
- gzip Documentation: https://docs.python.org/3/library/gzip.html
- zipfile Documentation: https://docs.python.org/3/library/zipfile.html
- py7zr Documentation: https://py7zr.readthedocs.io/en/latest/

Appendices
 . 
 

This comprehensive project report encapsulates the development and implementation of a file compressor/decompressor application, highlighting its achievements, challenges faced, and insights gained throughout the project's lifecycle.
