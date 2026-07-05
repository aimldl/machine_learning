* Draft: 2018-02-27 (Tue)

# Language Model을 위한 Penn Tree Bank (PTB) dataset

언어모델 (Language Model)은 자연어처리  (Natural Language Processing)의 응용분야인 음성인식 (Speech Recognition), 번역  (Machine Translation), 이미지 캡셔닝 (Image captioning) 등의 중요한 요소기술로 쓰입니다.

오픈소스 딥러닝 프레임워크인 [텐서플로우](https://www.tensorflow.org/)의 [언어모델 예제 페이지](https://www.tensorflow.org/tutorials/recurrent)의 내용에서 PTB dataset이 쓰입니다. "[PTB dataset from Tomas Mikolov's webpage](http://www.fit.vutbr.cz/~imikolov/rnnlm/simple-examples.tgz)"라는  클릭하면 "[simple-examples.tgz](http://www.fit.vutbr.cz/~imikolov/rnnlm/simple-examples.tgz)"이라는 파일을 다운로드 받습니다. .tgz 파일확장자를 가진 파일은 tar와 gunzip을 동시에 한 압축파일인데, 저는 윈도우즈에서 알집 (압축프로그램)을 써서 압축을 풀었습니다.

압축을 풀면 다음과 같은 디렉토리 구조를 볼 수 있습니다. data 디렉토리를 클릭하면 README를 포함해서 7개의 파일이 있습니다.

<img src="images/PTB_dataset_from_Tomas_Mikolov's_webpage_simple-examples.png">

<img src="images/PTB_dataset_from_Tomas_Mikolov's_webpage_simple-examples_data.png">

README파일에는 각 파일들에 대한 간략한 설명이 있습니다. 내용을 요약하면 다음과 같습니다.

<img src="images/README-PTB_dataset_summary.png">

아래 그림은 ptb.train.txt와 ptb.char.train.txt 파일의 일부를 비교한 것입니다. 왼쪽의 ptb.train.txt의 스페이스를 ptb.char.train.txt에서는 _로 바뀌어있음을 알 수 있습니다. 

<img src="images/PTB_dataset_from_Tomas_Mikolov's_webpage_simple-examples_data_winmerge_result.png">

README의 원문은 아래를 참조하세요.
README
Data description: 

```
Penn Treebank Corpus 
  \- should be free for research purposes 
   \- the same processing of data as used in many LM papers, including  "Empirical Evaluation and Combination of Advanced Language Modeling  Techniques" 
  \- ptb.train.txt: train set 
  \- ptb.valid.txt: development set (should be used just for tuning hyper-parameters, but not for training) 
  \- ptb.test.txt: test set for reporting perplexity 

   \- ptb.char.*: the same data, just rewritten as sequences of  characters, with spaces rewritten as '_' - useful for training character based models, as is shown in example 9
```
