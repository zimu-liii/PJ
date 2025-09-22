# PJ codec for DNA data storage
PJ codec, composed of PM (Partition Mapping) and JR (Jump-Rotating) algorithm, is designed for reliable DNA data storage retreival. Detailed description of the principle can be found in the paper [<u>Paper link</u>](). 

## Description
Current version of **PJ** codec is a **DNA storage algorithm** developed for **grayscale image** coding and decoding. It is aimed at realizing absolutely reliable recovery of image information even under high DNA sequence missing rate. Different from other DNA storage image codecs, SIMIC does not focus on how to perfectly restore the original image with 100% accuracy. In contrast, it reserves the missing parts in situ and exhibits the remaining correct parts. **Its first concern is to make sure the image could be opened and give its information to the greatest extent, rather than totally fails to be obtained as a result of damage on the vulnerable header part of the file.**

PJ realized this goal based on the central idea: **partition mapping (PM)**. On the one hand, turning an image file into a pixel matrix makes the image get rid of the restriction of highly formatting and encrypted header part, and becomes robust to damage on any part of its information. On the other hand, strand independent coding makes sure every DNA sequence is independent to each other, so that one broken sequence would not influence the decoding of another sequence. **Based on these two conceptions, PM is able to successfully open highly damaged pictures, which is impossible for other error-correcting methods to recover due to the extremely high missing rate exceeding the error redundancy.** In our article, we also showed in simulations that the partly damage does not affect the potential of image in some applications such as ML image recognition.

Besides, another creative design in our coding scheme is the **jump-rotating (JR)** DNA coding method. It was generated from the rotating algorithm [reference] but has made some modifications to improve its performance. Since DNA sequences could become unstable with patterns like continuous same bases (e.g. ‘AAA’, ‘GGGGG’), the original rotating method was designed to get legal DNA sequences by avoiding adjacent repetitive bases. However, this condition is too strict for a DNA sequence to be biologically stable. Thus, JR allows jumping in a certain step when using rotating, which could ease the restriction of rotating and reduce the sacrifice of storage density caused by rotating. **JR could be a very useful method in generating qualified DNA sequences in DNA storage research.**

For more details about the description and characterization of PJ, please refer to our **article**: [<u>超链接显示名</u>](超链接地址).

---

## Usage
### Requirments
This codec is developed in `Python 3.10.5`. However, any `python3` environment would be OK to run SIMIC. 

Dependent packages are listed in the `requirements.txt` document. If you only want to use the encoding and decoding functions of SIMIC, you just have to make sure your python have the standard libraries `math, random and json`, and have installed `matplotlib and numpy`. Other packages listed in requirements like `scikit-image and tensorflow` are only used in the error simulation part when we prepared our article and needed to prove the robustness of SIMIC. If you want to see how SIMIC performs in high error system, you can install these packages and refer to our codes in `simu` and `ml` folder.

### Install
pass

### Examples

Before start using SIMIC, the first thing to do is to import it to your code:

```python
import SIMIC
```

For **encoding** an image file, you have to prepare a gray-scale image file in any foramt, and give the `'file_path'` *(which should be a string and be sure to include file extension)* like this:

```python
s = SIMIC()  #create a SIMIC class instance
seq = s.encode_file('file_path')
```

If you already have a 2D `list` or 2D `np.array` data opened in python, and its variable name is `img`, you can directly use:

```python
seq = s.encode(img)
```

The code will return you `seq` which is a list of DNA sequences as the output results. You can save it to a `'.txt'` or `'.json'` format for further use if you need.

By default, the code does not add adaptors to the generated DNA sequences. If adaptors are needed, you can choose to add them by changing the default parameter: 

```python      
seq = s.encode(img, adaptor=True)
```

For **decoding** a list of DNA sequences, you have to provide the sequence file either in `.txt` or `.json` format, and give the `'file_path'` to the code like this:

```python
s = SIMIC()  #create a SIMIC class instance
img = s.decode_file('file_path')
```

or you already have a `list` opened in python, and its variable name is `seq`, you can directly use:

```python
img = s.decode(seq)
```

Similar to encoding, the code assumes that your sequences do not have adaptors. If your sequences are with adaptors, you may use it in this way:

```python
img = s.decode(seq, adaptor=True)
```

The code will return you `img` which is a 2D list of pixel matrix. To show your img, you can code as below:

```python
s.show(img)
```

or you want to save your img at `'save_file_path'`:

```python
s.save(img,'save_file_path')
```

Note that if you give a colour picture to the code, it will only return you a gray picture since the code is designed to work on 2D pixel matrices (gray-scale pictures). 

---

## Documents Annotation
Explainations on the file uploaded in this github page are listed as belows:

- **input** folder: where input files is stored; no code is stored here
- **ml** folder: Machine Learning applications of SIMIC, which is part of the simulation in the article
- **simic** folder: the core folder, where functions of encoding and decoding and jotating algorithm is realized.
- **sinulation** folder: missing simulation of SIMIC, which is part of the simulation in the article
- **.gitignore**: documents ignored by git (and you can just ignore this file)
- **LICENSE**: MIT license
- **README**: the thing you are reading
- **requirements.txt**: required dependent packages for SIMIC

---

## Contact
The author of SIMIC is also the author of the article: [<u>超链接显示名</u>](超链接地址). If you want to use SIMIC, please remember to refer to and cite the article given above. Contact: [<u>lzm.shjtdx.jc.19@sjtu.edu.cn</u>](lzm.shjtdx.jc.19@sjtu.edu.cn)