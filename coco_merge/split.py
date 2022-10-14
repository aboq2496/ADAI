import splitfolders
    
# train/val 나누기
# test는 제외하고 train, validation만 나누고 싶다면 두 개의 인자만 입력합니다. ex) (0.8, 0.1)
splitfolders.ratio("data", output="output", seed=1337, ratio=(.70, .15, .15))
