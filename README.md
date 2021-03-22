
# NLP Models

|    Date    |      Model      | Token Size |   #Params   | #Features | Inference GFLOPs | Training PFLOPs |
|------------|-----------------|------------|-------------|-----------|------------------|-----------------|
| 12/06/2017 | Transformer     |        512 | 65M         | 77M       | 54               | 23,000          |
| 02/15/2018 | ELMo            |            | 94M         |           |                  | 3,300           |
| 10/11/2018 | BERT Large      |        512 | 330M        | 230M      | 340              | 250,000         |
| 06/11/2018 | GPT-1           |        512 | 110M        | 85M       | 96               | 57,000          |
| 02/14/2019 | GPT-2           |       1024 | 1,500M      | 2,000M    | 3,400            |                 |
| 07/26/2019 | RoBERTa Large   |        512 | 1,500M      | 2,000M    | 3,400            | 4,300,000       |
| 08/17/2019 | Megatron        |       1024 | 8,300M      | 4,700M    | 18,000           | 8,100,000       |
| 09/26/2019 | ALBERT xxl      |        512 | 235M        | 450M      | 2,500            | 31,000,000      |
| 02/13/2020 | Microsoft T-NLP |       1024 | 17,000M     | 5,700M    | 36,000           | 28,000,000      |
| 03/23/2020 | ELECTRA Large   |        128 | 330M        | 38M       | 79               | 3,100,000       |
| 05/28/2020 | GPT-3           |       2048 | 175,000M    | 63,000M   | 740,000          | 310,000,000     |
| 06/30/2020 | GShard          |            | 600,000M    |           |                  |                 |
| 06/20/2020 | Baidu RecSys-C  |            | 2,000,000M  |           | ~O(0.1)          |                 |
| 06/20/2020 | Baidu RecSys-E  |            | 10,000,000M |           | ~O(0.1)          |                 |



# Memory Usage For Training Per Device
| Date |           Model            | Input Resolution | #Params | Top-1 | Inference GFLOPs | Training PFLOPs |
|------|----------------------------|------------------|---------|-------|------------------|-----------------|
|      | ResNet50                   | 224 x 224        | 25.56M  | 76.50 |             8.19 |                 |
|      | ResNet152                  | 224 x 224        | 60.19M  | 78.30 |            23.05 |                 |
|      | DenseNet264                | 224 x 224        | 33.37M  | 78.00 |            11.54 |                 |
|      | ResNeXt152 (64x4d)         | 224 x 224        | 107.57M | 79.50 |            43.03 |                 |
|      | SENet154 (vd)              | 224 x 224        | 114.29M | 81.40 |            45.83 |                 |
|      | Fix_ResNeXt101(32x48d_wsl) | 320 x 320        | 456.20M | 86.30 |           354.23 |                 |

# Computer Vision Models
| Year |           Model            | Input Resolution (Sentence length)|  Batch Size   | Params Memory    | Optimizer Memory  | Activation Memory | Total Memory |
|------|----------------------------|-----------------------------------|---------------|------------------|-------------------|-------------------|--------------|
| 2012 | AlexNet                    | 227 x 227                         | 128           | 0.23 GB          | 0.23 GB           | 0.71 GB           |  1.71 GB     |           
| 2014 | VGG19                      | 224 x 224                         | 64            | 0.54 GB          | 0.54 GB           | 4.64 GB           |  5.72 GB     |
| 2015 | ResNet152                  | 224 x 224                         | 32            | 0.22 GB          | 0.22 GB           | 5.14 GB           |  5.58 GB     |
| 2016 | DenseNet201                | 224 x 224                         | 32            | 0.07 GB          | 0.07 GB           | 6.04 GB           |  6.18 GB     |
| 2016 | ResNeXt101 (64x4d)         | 224 x 224                         | 32            | 0.31 GB          | 0.31 GB           | 7.34 GB           |  7.96 GB     |
| 2017 | Transformer Big (WMT)      | 512                               | 6             | 1.02 GB          | 2.04 GB           | 11.78 GB          |  14.84 GB    |
| 2018 | BERT Large                 | 512                               | 16            | 1.32 GB          | 2.64 GB           | 14.38 GB          |  18.34 GB    | 
| 2019 | GPT-2                      | 2014                              | 1             | 5.86 GB          | 11.62 GB          | 8.63 GB           |  26.21 GB    |
