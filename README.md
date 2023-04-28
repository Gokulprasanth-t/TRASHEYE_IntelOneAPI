![image_2020_11_03T09_50_23_420Z_4_965x450-965x430-1](https://user-images.githubusercontent.com/121724612/235177155-ae7f12df-22f5-4286-ad4c-ec5f971a7454.png)

# INTEL ONE API
Intel OneAPI is a unified programming model that enables developers to build applications across a variety of architectures, including CPUs, GPUs, and FPGAs. It provides a single programming interface for these architectures, making it easier for developers to write and optimize code for their specific hardware.

One of the main advantages of using Intel OneAPI is its performance. By optimizing code for specific hardware, developers can achieve significant performance improvements compared to running code on a generic platform. This is particularly important for applications that require high-performance computing, such as machine learning and scientific simulations.

Intel OneAPI also provides a range of tools and libraries to help developers optimize their code. These include the Intel VTune Profiler, which enables developers to analyze the performance of their code and identify bottlenecks, and the Intel Math Kernel Library, which provides optimized routines for math operations such as linear algebra and Fourier transforms.
# TRASHEYE_IntelOneAPI
## Problem Statement: 

![sky-high-trash](https://user-images.githubusercontent.com/121724612/235177381-04f114f1-069d-431d-ae5e-d6113491db96.png)

Improper waste management is a major environmental concern worldwide, as it results in the accumulation of trash in landfills and oceans. Despite the availability of waste disposal bins, littering and illegal dumping of garbage still occur frequently in public places, leading to sanitation and health issues.

## Objective: 
The objective of the proposed solution is to detect and identify trash in public areas using AI & ML technology. The goal is to reduce the amount of litter and illegal dumping by implementing an efficient trash management system.

https://user-images.githubusercontent.com/121724612/235176549-d6811f96-cc06-4075-958f-7d50d49c5b88.mp4

## Solution: 
The solution involves the deployment of AI & ML algorithms for trash detection in real-time. The system uses cameras installed in public areas to capture images of the surroundings. The captured images are then analyzed using computer vision and deep learning techniques to identify and categorize the trash. This information is then relayed to the concerned authorities for appropriate action, such as garbage collection and disposal.

![Screenshot 2023-04-21 210817](https://user-images.githubusercontent.com/121724612/235077931-9675432b-f879-4402-bd07-a2f524078b25.png)
![Screenshot 2023-04-21 210916](https://user-images.githubusercontent.com/121724612/235077979-6876b766-31a4-4c0c-a2e3-47890a17ac4e.png)

# Toolkit used: Intel® AI Analytics Toolkit (AI Kit)

In this project, we have used various machine learning models such as ResNet, DenseNet, and CNN to detect trash in images. However, processing large amounts of image data can lead to increased runtime, particularly on systems with limited processing power.

To optimize our models, we can leverage the Intel® AI Analytics Toolkit (AI Kit), which provides improved performance by optimizing the models for the Intel architecture. Deep learning APIs such as Keras are optimized for Intel hardware by the oneAPI platform, and integrating oneAPI into scikit-learn can enhance the performance of some of its algorithms, such as linear regression.

By utilizing the optimized libraries and routines for mathematical computations and data analysis provided by oneAPI, we can significantly improve the performance of our trash detection models. This can help us efficiently and accurately identify trash in images, even when working with large amounts of data.

# RESULT
![WhatsApp Image 2023-04-21 at 9 04 14 PM](https://user-images.githubusercontent.com/121724612/235195283-3a903881-08ed-4cc8-8173-def719824286.jpeg)![WhatsApp Image 2023-04-21 at 9 04 14 PM (1)](https://user-images.githubusercontent.com/121724612/235195328-e111b933-b186-4e3d-ba9a-79961d4ceda8.jpeg)![WhatsApp Image 2023-04-21 at 9 04 13 PM](https://user-images.githubusercontent.com/121724612/235195360-b7b8bf9c-4b42-44e8-a364-27025c2efe88.jpeg)


# WEB APP
![Screenshot (1)](https://user-images.githubusercontent.com/121724612/235199713-1fe605e1-8af1-4b37-9bf0-531f7a90f8ef.png)
This is the expected webapp output of the project.

# RESOURCES

<a href='https://universe.roboflow.com/divya-lzcld/taco-mqclx/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true'>DATASET</a>

# LEARNING'S FROM INTEL PLATFORM

Intel OneAPI is a comprehensive and open-source toolkit designed to help developers create high-performance, heterogeneous applications across different architectures. It provides a unified programming model that can be used across CPUs, GPUs, FPGAs, and other accelerators, which can help optimize performance and reduce development time.

There are several key takeaways from the development and use of Intel OneAPI, including:

Improved Performance: One of the key benefits of Intel OneAPI is the ability to optimize performance across a range of different hardware architectures. This is especially useful in applications that require a lot of processing power, such as machine learning, scientific computing, and data analytics. The toolkit provides optimized libraries and tools that can help improve application performance by up to 30% compared to traditional CPU-only implementations.

Simplified Development: Intel OneAPI provides a single programming model that can be used across different hardware architectures, which can help simplify the development process. This can help reduce development time and costs while enabling developers to focus on writing code that is optimized for performance rather than worrying about the underlying hardware architecture.

Open-Source: Another key benefit of Intel OneAPI is that it is open-source, which means that it can be freely used, modified, and distributed by developers. This can help encourage collaboration and innovation across the development community, while also enabling developers to customize the toolkit to meet their specific needs.

Improved Portability: Intel OneAPI is designed to work across a range of different hardware architectures, which can help improve portability and enable applications to run on a wide range of devices. This can be particularly useful in environments where hardware resources are limited or where there is a need to run applications on different types of hardware.

Heterogeneous Computing: With the increasing demand for high-performance computing, many organizations are turning to heterogeneous computing to help optimize performance. Intel OneAPI provides a range of tools and libraries that can help developers take advantage of the processing power of different hardware architectures, including CPUs, GPUs, FPGAs, and other accelerators.

In conclusion, Intel OneAPI is a powerful toolkit that can help developers create high-performance, heterogeneous applications across different architectures. By providing a unified programming model, optimized libraries and tools, and open-source support, Intel OneAPI can help simplify development, improve performance, and enable greater collaboration and innovation across the development community.
