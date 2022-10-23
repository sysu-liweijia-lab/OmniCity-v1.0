# OmniCity-v2.0

## Introduction
This project is used in Multi-level task based on MMDetection, which include models, and correlative configs.  
**Note**： If you want to check more about our work, please refer [here](https://city-super.github.io/omnicity).

## Overview of the models and its related tasks
Tasks: Instance segmentation, Land use segmentation, Plane segmentation.
### Satellite level: small view
Data Type |Size|Method | Task | Download
-------|-------|-------|---------|-----
Satallite image|512*512|Mask R-CNN|Instance segmentation|[Model](https://drive.google.com/file/d/17iHFTJUg-6dhzfCvA1rgGutrxGSRv0U-/view?usp=sharing)&[log](https://drive.google.com/file/d/13jdfwFZx14Hx3A9GmDNaBKGhijTnETF5/view?usp=sharing)
Satallite image|512*512|MS R-CNN|Instance segmentation|[Model](https://drive.google.com/file/d/1a134TgMJuq2mFeI35Squ7j-z44zE7caT/view?usp=sharing)&[log](https://drive.google.com/file/d/1WF5v4gHjvaGLMA6ZQipSeTh9R13UY0UC/view?usp=sharing)
Satallite image|512*512|CARAFE|Instance segmentation|[Model](https://drive.google.com/file/d/17m3dKxYIvguSJ6xDZ59ZawtFS_DkFLuA/view?usp=sharing)&[log](https://drive.google.com/file/d/1r9lWd3r-w6mFkdG4DJIxuZB6-n9KybxB/view?usp=sharing)
Satallite image|512*512|Cascade|Instance segmentation|[Model](https://drive.google.com/file/d/1SnXI9GOonTGioDMC7KLn7Xi-qM4Ump7F/view?usp=sharing)&[log](https://drive.google.com/file/d/1SnXI9GOonTGioDMC7KLn7Xi-qM4Ump7F/view?usp=sharing)
Satallite image|512*512|HTC|Instance segmentation|[Model](https://drive.google.com/file/d/1xocu_4D9vSS1UoCy_ko9hQWvOhnRWYMY/view?usp=sharing)&[log](https://drive.google.com/file/d/1d6reG1xcXksnkLLuPkpciZ88UqpxbDLd/view?usp=sharing)
### Satellite level: medium view
Data Type |Size|Method | Task | Download
-------|-------|-------|---------|-----
Satallite image|512*512|Mask R-CNN|Instance segmentation|[Model](https://drive.google.com/file/d/17iHFTJUg-6dhzfCvA1rgGutrxGSRv0U-/view?usp=sharing)&[log](https://drive.google.com/file/d/1Kqu3AAgzOTHUSTuTA8C7lmEh2JG71R7_/view?usp=sharing)
### Satellite level: large view
Data Type |Size|Method | Task | Download
-------|-------|-------|---------|-----
Satellite image|512*512|Msak R-CNN|Instance segmentation|[Model](https://drive.google.com/file/d/1okuk0AsCZhFh-TZhAx9pNtr4B0NoJPOn/view?usp=sharing)&[log](https://drive.google.com/file/d/1AVQJJhdpgjxPrdg2sVv5liV1H3gTvCvT/view?usp=sharing)
### Street level: Panorama
Data Type |Size|Method | Task | Download
-------|-------|-------|---------|-----
Panorama image|512*1024|Mask R-CNN|Instance segmentation|[Model](https://drive.google.com/file/d/1jvcyQTkl9h_U2i-_CRj6Q6UQ0j3UpCz4/view?usp=sharing)&[log](https://drive.google.com/file/d/1jvcyQTkl9h_U2i-_CRj6Q6UQ0j3UpCz4/view?usp=sharing)
Panorama image|512*1024|Mask R-CNN|Land use segmentation|[Model](https://drive.google.com/file/d/1v0-91uoksq3K3uZJ9FmLKIGEgw4roUj-/view?usp=sharing)&[log](https://drive.google.com/file/d/1azJ_mcIwL5fzVV2aYY01m5tMevck5osa/view?usp=sharing)
Panorama image|512*1024|MS R-CNN|Land use segmentation|[Model](https://drive.google.com/file/d/1z3a_4qvzh456iOFDhXN7Nz9N1tjhiKVl/view?usp=sharing)&[log](https://drive.google.com/file/d/1GoE77p6HsAp0zLAuNICRWFwpJY6SlFoK/view?usp=sharing)
Panorama image|512*1024|CARAFE|Land use segmentation|[Model](https://drive.google.com/file/d/18kURw1Zzfg88b3YxzzO3UH5baGg23usJ/view?usp=sharing)&[log](https://drive.google.com/file/d/1Fu-notbskz6yKd2aWOzWss1GPMQEaKLE/view?usp=sharing)
Panorama image|512*1024|Cascade|Land use segmentation|[Model](https://drive.google.com/file/d/13hVlsRlRocEkXbL9Hbv5_ivP_dbzfQq7/view?usp=sharing)&[log](https://drive.google.com/file/d/1-Vq-ZwA7Z4FZ8JQCUfiKYL1zuInkMKbO/view?usp=sharing)
Panorama image|512*1024|HTC|Land use segmentation|[Model](https://drive.google.com/file/d/17krXn77ixqJM9hZdviQhhDlnMtsfnB0b/view?usp=sharing)&[log](https://drive.google.com/file/d/1nvM5AJ95CzKMvGmCd7ZE2r4wlVwDhMa3/view?usp=sharing)
### Street level: Mono-view
Data Type |Size|Method | Task | Download
-------|-------|-------|---------|-----
Mono-view image|512*512|Mask R-CNN|Instance segmentation|[Model](https://drive.google.com/file/d/1cV4FPuIAfHP4dRix8DucLt02FZebQflp/view?usp=sharing)&[log](https://drive.google.com/file/d/1gW6OWdIr5OJgfoY5VnbANfA4zqv1ah8Y/view?usp=sharing)
Mono-view image|512*512|Mask R-CNN|Land use segmentation|[Model](https://drive.google.com/file/d/1Ysly8Bzeb8ODfSfMsjo-x_zo9oAIAq7Y/view?usp=sharing)&[log](https://drive.google.com/file/d/1CilgIiz_LEioPQkcM5W7BEGIzQMe9pvA/view?usp=sharing)
Mono-view image|512*512|Mask R-CNN|Plane segmentation|[Model](https://drive.google.com/file/d/18MXiewv7UhHFyHGClQeuHrRs2zZZb2FV/view?usp=sharing)&[log](https://drive.google.com/file/d/1tMgRaIEYA7nKtwqTW2IesMk5HQpkFmfS/view?usp=sharing)

## Usage
### Data preparation
If you want to use your own dataset test the models above, please prepare data following [MMdetection](https://github.com/open-mmlab/mmdetection)(Dataset in COCO format is preferred). And the data structure should look like below:
```
mmdetection
├── data
│   ├── coco
│   │   ├── annotations
│   │   ├── train2017
│   │   ├── val2017
│   │   ├── test2017
```
### Model test
With `OmniCity dataset`:
```
# single-gpu testing
python tools/test.py \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    [--out ${RESULT_FILE}] \
    [--eval ${EVAL_METRICS}] \
    [--show]

# CPU: disable GPUs and run single-gpu testing script
export CUDA_VISIBLE_DEVICES=-1
python tools/test.py \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    [--out ${RESULT_FILE}] \
    [--eval ${EVAL_METRICS}] \
    [--show]

# multi-gpu testing
bash tools/dist_test.sh \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    ${GPU_NUM} \
    [--out ${RESULT_FILE}] \
    [--eval ${EVAL_METRICS}]
```
With `new dataset`:

* Prepare the dataset following the above rules
* Refer to the preceding operations

## Citation
```
@article{li2022omnicity,
    title={OmniCity: Omnipotent City Understanding with Multi-level and Multi-view Images},
    author={Li, Weijia and Lai, Yawen and Xu, Linning and Xiangli, Yuanbo and Yu, Jinhua and He, Conghui and Xia, Gui-Song and Lin, Dahua},
    journal={arXiv e-prints},
    pages={arXiv--2208},
    year={2022}
    }
```
