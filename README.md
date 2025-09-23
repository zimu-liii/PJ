# PJ codec for DNA data storage
PJ codec, composed of **PM (Partition Mapping)** and **JR (Jump-Rotating)** algorithm, is designed for reliable DNA data storage retreival. It is first proposed by our article: **Noise-immune and AI-enhanced DNA storage via adaptive partition mapping of digital data** [<u>[DOI]</u>]().

## Description
Current version of **PJ** codec is a **DNA storage algorithm** developed for **grayscale image** coding and decoding. It is aimed at realizing absolutely reliable recovery of image information even under high DNA sequence missing rate. Different from other DNA storage image codecs, PJ does not focus on how to perfectly restore the original image with 100% accuracy. In contrast, it reserves the missing parts in situ and exhibits the remaining correct parts. **Its first concern is to make sure the image could be opened and give its information to the greatest extent, rather than totally fails to be obtained as a result of damage on the vulnerable header part of the file.**

PJ realized this goal based on the central idea: **partition mapping (PM)**. On the one hand, turning an image file into a pixel matrix makes the image get rid of the restriction of highly formatting and encrypted header part, and becomes robust to damage on any part of its information. On the other hand, strand independent coding makes sure every DNA sequence is independent to each other, so that one broken sequence would not influence the decoding of another sequence. **Based on these two conceptions, PM is able to successfully open highly damaged pictures, which is impossible for other error-correcting methods to recover due to the extremely high missing rate exceeding the error redundancy.** In our article, we also showed in simulations that the partly damage does not affect the potential of image in some applications such as ML image recognition.

Besides, another creative design in our coding scheme is the **jump-rotating (JR)** DNA coding method. It was generated from the rotating algorithm [reference] but has made some modifications to improve its performance. Since DNA sequences could become unstable with patterns like continuous same bases (e.g. ‘AAA’, ‘GGGGG’), the original rotating method was designed to get legal DNA sequences by avoiding adjacent repetitive bases. However, this condition is too strict for a DNA sequence to be biologically stable. Thus, JR allows jumping in a certain step when using rotating, which could ease the restriction of rotating and reduce the sacrifice of storage density caused by rotating. **JR could be a very useful method in generating qualified DNA sequences in DNA storage research.**

For more details about the description and characterization of PJ, please refer to our **article**  listed above.

## Usage
### Requirments
This codec is developed in `Python 3.10.5`. However, any `python3` environment would be OK to run PJ. 

Dependent packages are listed in the `requirements.txt` document. If you only want to use the encoding and decoding functions of PJ, you just have to make sure your python have the standard libraries `math, random and json`, and have installed `matplotlib and numpy`. Other packages listed in requirements like `scikit-image and tensorflow` are only used in the error simulation part when we prepared our article and needed to prove the robustness of PJ. If you want to see how PJ performs in high error system, you can install these packages and refer to our codes in `simu` and `ml` folder.

### Examples

The main module of PJ is integrated in the **pj.py** file. You can start using PJ by running this file in the IDE and then create a new class:

```python
pj = PJ()
```

After creating the codec, you can choose to **encode** an image array or **decode** a sequence list. The image is expected to be a 2D `list` or 2D `np.array` data opened in python, while the sequence is expected to be a `list` data type.

```python
seq = pj.encode(img)  # Image should be list or numpy array
img = pj.decode(seq)  # Sequence should be list
```

Before starting **encode**, you may wish to process your file first to turn it into the expected data format. For original image files, any foramt is permitted to use and opened into a **2D pixel matirx**. You can directly use the function provided by pj to finish this process:

```python
img = read_image(img_path)  # 'img_path' is the path of your image file which should be a string and be sure to include file extension
```

By default, the code does not add adaptors to the generated DNA sequences. If adaptors are needed, you can choose to add them by using the add_adaptor function: 

```python      
seq_adp = add_adaptor(seq)
```

This step will add the adaptors used in our article. If you have your own prefered adaptors, you can change the sequences listed in the function codes manually.

The encode step will return you `seq` which is a list of DNA sequences as the output results. You can save it to a `'.txt'` or `'.json'` format for further use if you need.

For **decoding** a list of DNA sequences, you have to provide the sequence file either in `.txt` or `.json` format, and give the `seq_path` to the code like this:

```python
seq = read_seq(seq_path)
```

Similar to encoding, the code assumes that your sequences do not have adaptors. If your sequences are with adaptors and named as seq_adp, you may use it in this way:

```python
seq = remove_adaptor(seq_adp)
```

The code will return you `img` which is a 2D list of pixel matrix. To show your img, you can code as below:

```python
show_image(img)
```

or you want to save your img as `img_name`:

```python
save_image(img,img_name)
```

Note that if you give a colour picture to the code, it will only return you a gray picture since the code is designed to work on 2D pixel matrices (gray-scale pictures). 

## Documents Annotation
Explainations on the file uploaded in this github page are listed as belows:

- **pj.py**: The **main** module for pj code running, including the file io, encode and decode functions. 
- **encode.py** and **decode.py**: the codes for encoding and decoding, respectly.
- **jotating** folder: the folder where functions of jump-rotating algorithm is realized.
- **ml** folder: Machine Learning applications of PJ, which is part of the simulation in the article.
- **simulation** folder: missing simulation of PJ, which is part of the simulation in the article.
- **README.md**: the thing you are reading
- **requirements.txt**: required dependent packages for PJ

## Installation
We have not yet developed an installable version. A PyPI version is comimg soon. Developers can run the codes directly in the compilation environment first. 

## Notes
The author is still a programming learner and is devoted to improve the coding skills. We appreciate your patience for a better version of PJ and we will continue to work on the codes to develop a more equipped software architecture.

