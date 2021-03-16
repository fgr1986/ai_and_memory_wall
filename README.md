
|    Date    |      Model      | Input Size |   #Params   |  FLOPs   |
|            |                 |  (Token)   |             | (GFLOPs) |
|------------|-----------------|------------|-------------|----------|
| 12/6/2017  | Transformer     |            | 65M         |          |
|------------|-----------------|------------|-------------|----------|
| 10/11/2018 | BERT Large      |            | 330M        |          |
|------------|-----------------|------------|-------------|----------|
| 2/15/2018  | ELMO            |            | 94M         |          |
|------------|-----------------|------------|-------------|----------|
| 6/11/2018  | GPT-1           |            | 110M        |          |
|------------|-----------------|------------|-------------|----------|
| 2/14/2019  | GPT-2           |            | 1,500M      |          |
|------------|-----------------|------------|-------------|----------|
| 8/17/2019  | Megatron        |            | 8,300M      |          |
|------------|-----------------|------------|-------------|----------|
| 2/13/2020  | Microsoft T-NLP |            | 17,000M     |          |
|------------|-----------------|------------|-------------|----------|
| 5/28/2020  | GPT-3           |            | 175,000M    |          |
|------------|-----------------|------------|-------------|----------|
| 6/30/2020  | GShard          |            | 600,000M    |          |
|------------|-----------------|------------|-------------|----------|
| 6/20/2020  | Baidu RecSys-C  |            | 2,000,000M  | ~O(0.1)  |
|------------|-----------------|------------|-------------|----------|
| 6/20/2020  | Baidu RecSys-E  |            | 10,000,000M | ~O(0.1)  |
|------------|-----------------|------------|-------------|----------|
|            |                 |            |             |          |



| Date |     Model      |  Input Size  | #Params | Top-1 |  FLOPs   |
|      |                | (Resolution) |         |       | (GFLOPs) |
|------|----------------|--------------|---------|-------|----------|
|      | ResNet50       | 224 x 224    | 25.56M  | 76.50 |     8.19 |
|------|----------------|--------------|---------|-------|----------|
|      | ResNet152      | 224 x 224    | 60.19M  | 78.30 |    23.05 |
|------|----------------|--------------|---------|-------|----------|
|      | DenseNet264    | 224 x 224    | 33.37M  | 78.00 |    11.54 |
|------|----------------|--------------|---------|-------|----------|
|      | ResNeXt152     | 224 x 224    | 107.57M | 79.50 |    43.03 |
|      | (64x4d)        |              |         |       |          |
|------|----------------|--------------|---------|-------|----------|
|      | SENet154 (vd)  | 224 x 224    | 114.29M | 81.40 |    45.83 |
|------|----------------|--------------|---------|-------|----------|
|      | Fix_ResNeXt101 | 320 x 320    | 456.20M | 86.30 |   354.23 |
|      | (32x48d_wsl)   |              |         |       |          |
|------|----------------|--------------|---------|-------|----------|
|      |                |              |         |       |          |
|      |                |              |         |       |          |