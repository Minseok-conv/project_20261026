# 06 · 두 문제의 K와 주 지표를 따로 선택

PPT 61쪽과 연결 · 권장 실습 25분

**목표:** 같은 입력에서도 문제·지표에 따라 K가 달라짐을 확인한다.

**열 파일:** `main.py`. TODO만 먼저 완성합니다. 제공된 읽기·저장 코드를 다시 작성하지 않아도 됩니다.

**새 함수·옵션:** 분류 F1 최대·회귀 RMSE 최소 / 동점은 작은 K / train 점수는 진단용

**직접 완성할 부분**

- **H06**: 회귀의 train·valid RMSE를 각각 구하세요.
  힌트: 첫 번째 인자는 실제값, 두 번째 인자는 대응하는 예측입니다.

**실행:** 현재 README가 있는 폴더에서 아래 명령을 사용합니다.

```powershell
python main.py
```

**예상 출력** — 소수점 출력 자릿수·공백 표시는 환경에 따라 약간 다를 수 있습니다.

```text
          task  K    scale weights  metric  train_score  valid_score
classification  1 standard uniform      F1        1.000        0.400
classification  3 standard uniform      F1        0.571        0.545
classification  5 standard uniform      F1        0.462        0.200
classification  9 standard uniform      F1        0.519        0.000
classification 15 standard uniform      F1        0.364        0.000
    regression  1 standard uniform RMSE_ms        0.000      944.680
    regression  3 standard uniform RMSE_ms      443.423      795.216
    regression  5 standard uniform RMSE_ms      480.826      744.986
    regression  9 standard uniform RMSE_ms      533.779      707.645
    regression 15 standard uniform RMSE_ms      561.846      641.788
선택 / 분류 K: 3 회귀 K: 15
```

**완료 기준:** 10행 탐색표와 분류K3·회귀K15를 확인한다.

**설명 질문:** K=1의 train RMSE=0이면 완벽한 예측기인가?

**생성되는 파일:** `outputs/knn_search.csv`

## 이 실습의 구조

`main.py`를 실행합니다. `data/`가 있으면 이 실습의 원본 입력입니다. `preprocessing.py`가 있으면 전날의 전처리를 재사용하는 제공 모듈이며 수정할 TODO가 없습니다. `expected/`는 완성 후 대조할 결과입니다. `outputs/`는 프로그램이 생성하는 결과입니다. 입력과 비교용 정답을 혼동하지 않습니다.

현재 폴더만 복사해도 실행됩니다. 상위 실습을 import하거나 이전 결과 파일에 의존하지 않습니다. 파일명 `main.py`가 같아도 **현재 실습 폴더**의 파일인지 확인합니다.

[심화 전체 안내로 돌아가기](../README.md)

## 막혔을 때 확인

`NoneType` 또는 학습 전 오류가 나오면 먼저 해당 파일의 TODO가 남아 있는지 확인합니다. `NotFittedError`는 fit 부분이 아직 `pass`인지 봅니다. 모델 설정 TODO는 파일이 실행되더라도 잘못된 결과를 낼 수 있습니다.

`ModuleNotFoundError`가 나면 VS Code가 전날의 가상환경을 선택했는지 확인합니다. `root_mean_squared_error`를 찾지 못하면 설치된 scikit-learn 버전을 확인하고 역할 폴더의 `requirements.txt`를 사용합니다.

`파일을 찾을 수 없음`이면 ZIP을 완전히 해제했는지, 코드와 함께 배포된 데이터가 이동·삭제되지 않았는지 확인합니다. 출력 CSV를 Excel에서 열어 둔 경우 저장이 막힐 수 있으므로 닫은 뒤 다시 실행합니다.

오류 메시지를 가리는 `try/except`를 추가하는 과제가 아닙니다. TODO와 파일 위치를 확인하고 계속 막히면 실행 명령과 오류 마지막 줄을 강사에게 보여 줍니다.
