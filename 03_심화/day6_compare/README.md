# 실습07~08 · day6_compare

실습07에서 완성한 같은 폴더를 실습08에서 이어서 사용합니다. `main.py`를 실행한 뒤 `restore.py`를 실행합니다. 개별 파일을 다른 실습의 동명 모듈과 섞지 않습니다.

```text
day6_compare/
├─ README.md
├─ main.py                  # 학습·비교·저장 순서
├─ preprocessing.py         # 제공: 새 전처리와 모델 연결
├─ evaluate.py              # 직접 완성: 회귀·분류 지표
├─ search.py                # 제공: 실습06의 K 탐색 재사용
├─ restore.py               # 직접 완성: 저장 모델 읽기
├─ requirements-lock.txt
├─ data/
│  ├─ requests.csv
│  └─ split_manifest.csv
├─ expected/                # 비교용 CSV·콘솔 결과; 모델 없음
├─ outputs/                 # 직접 실행하여 생성
└─ reports/model_choice.md  # 자신의 근거와 한계
```

함수는 역할별 보조 모듈에만 최소한으로 있습니다. 직접 완성하는 것은 evaluate의 두 계산, main의 학습·예측, restore의 모델 읽기 **총4블록**입니다. `preprocessing.py`와 `search.py`는 수정하지 않아도 됩니다. 테스트 파일·오류 입력·명령행 옵션 파서는 추가하지 않았습니다.

## 준비와 시작

VS Code에서 `day6_compare` 폴더를 열고 기존 가상환경을 선택합니다. 폴더만 다른 위치에 복사한 경우에도 `data/`와 제공 모듈을 함께 유지합니다. 필요한 경우에만 다음 명령으로 검증 버전을 설치합니다.

```powershell
python -m pip install -r requirements-lock.txt
```

## 수정 순서

1. `evaluate.py`의 H07r·H07c를 완성합니다. 파일 자체를 실행하는 대신 main에서 사용합니다.
2. `main.py`의 H07fit을 완성합니다.
3. `python main.py`로 비교표와 저장 모델을 만듭니다.
4. `restore.py`의 H08을 완성하고 **다른 터미널에서** `python restore.py`를 실행합니다.
5. `reports/model_choice.md`를 작성합니다.

## 고정 조건

원본100건·입력4열·train60/valid20/test20·분할 내부 순서를 고정합니다. 전처리는 숫자2열 중앙값→표준화, 문자2열 최빈값→원핫입니다. 출력8열이며 학습은 train만 사용합니다.

K 후보는1·3·5·9·15입니다. 분류는 valid F1 최대, 회귀는 valid RMSE 최소, K 동점은 작은 값을 선택합니다. 모델 점수 동점은 먼저 등록한 단순 후보를 유지합니다. 각 모델에 새 전처리를 연결해 학습 상태를 공유하지 않습니다.

`search.py`가 K 탐색을 실제 계산합니다. 이전 실습의 정답 CSV를 읽거나 test 점수로 K를 선택하지 않습니다. 후보를 더 늘리는 과제도 아닙니다.

### 먼저: evaluate.py의 두 계산

**H07r**: MAE·RMSE를 계산하세요.  
힌트: 실습02에서 사용한 함수를 그대로 씁니다.

**H07c**: 실패1의 F1을 계산하세요.  
힌트: f1_score(actual, prediction, zero_division=0)

## 07 · 체계적인 비교 프로젝트

PPT 73쪽과 연결 · 권장 실습 60분 (07·08 합계)

**목표:** 분할·전처리·탐색·비교·저장을 역할별 모듈로 연결한다.

**열 파일:** `main.py`. TODO만 먼저 완성합니다. 제공된 읽기·저장 코드를 다시 작성하지 않아도 됩니다.

**새 함수·옵션:** main: 실행 순서 / preprocessing: 전처리 / search: 이전 탐색 재사용 / evaluate: 지표

**직접 완성할 부분**

- **H07fit**: 해당 target으로 학습하고 valid 예측을 구하세요.
  힌트: 두 문제의 정답 열은 target에 들어 있습니다.

**실행:** 현재 README가 있는 폴더에서 아래 명령을 사용합니다.

```powershell
python main.py
```

**예상 출력** — 소수점 출력 자릿수·공백 표시는 환경에 따라 약간 다를 수 있습니다.

```text
regression / valid 20건
 model    scale  MAE_ms  RMSE_ms     R2
 Dummy standard 541.260  658.745 -0.162
Linear standard 551.797  639.996 -0.097
 KNN15 standard 530.063  641.788 -0.103
classification / valid 20건
   model    scale  Accuracy    F1  Precision  Recall  TN  FP  FN  TP
   Dummy standard      0.70 0.000      0.000   0.000  14   0   6   0
Logistic standard      0.60 0.333      0.333   0.333  10   4   4   2
    KNN3 standard      0.75 0.545      0.600   0.500  12   2   3   3
선택 모델: {'regression': 'Linear', 'classification': 'KNN3'}
선택 K / 분류: 3 회귀: 15
outputs에 비교표·탐색표·예측·선택 기록·모델을 저장했습니다.
test는 보관만 했으며 모델에 전달하지 않았습니다.
```

**완료 기준:** 비교표 각 3행·탐색10행·예측120행을 생성하고 reports/model_choice.md를 작성한다.

**설명 질문:** 학습 파일을 다른 사람에게 받았을 때 바로 joblib.load를 해도 되는가?

**생성되는 파일:** `outputs/regression_comparison.csv`, `outputs/classification_comparison.csv`, `outputs/knn_search.csv`, `outputs/validation_predictions.csv`, `outputs/selection.json`, `outputs/models.joblib`

## 08 · 저장한 모델을 새 실행에서 복원

PPT 78쪽과 연결 · 권장 실습 35분

**목표:** 모델·전처리를 복원해 같은 입력에 같은 예측을 얻는다.

**열 파일:** `restore.py`. TODO만 먼저 완성합니다. 제공된 읽기·저장 코드를 다시 작성하지 않아도 됩니다.

**새 함수·옵션:** joblib.dump/load: 직접 만든 모델 저장·복원 / allclose: 작은 실수 오차를 허용해 비교

**직접 완성할 부분**

- **H08**: main.py로 직접 만든 models.joblib을 읽으세요.
  힌트: joblib.load에는 실제 모델 파일 경로를 전달합니다.

**실행:** 현재 README가 있는 폴더에서 아래 명령을 사용합니다.

```powershell
python restore.py
```

**예상 출력** — 소수점 출력 자릿수·공백 표시는 환경에 따라 약간 다를 수 있습니다.

```text
regression 복원 예측 일치: True
classification 복원 예측 일치: True
fit을 호출하지 않았고 test도 사용하지 않았습니다.
```

**완료 기준:** 별도 터미널 실행에서도 두 문제 모두 True인지 확인하고 보고서를 완성한다.

**설명 질문:** 복원 때 다시 fit하면 무엇을 검사한 셈이 되는가?

## 결과 파일을 읽는 순서

| 파일 | 행 수·의미 |
|---|---|
| `regression_comparison.csv` | Dummy·Linear·KNN15, 3행. MAE·RMSE(ms), R² |
| `classification_comparison.csv` | Dummy·Logistic·KNN3, 3행. F1·Precision·Recall·혼동행렬 |
| `knn_search.csv` | 두 문제×K5개=10행. 같은 전처리·weights=uniform |
| `validation_predictions.csv` | valid20건×모델3개×문제2개=120행. 요청ID·실제·예측 |
| `selection.json` | 사전 주 지표로 선택한 모델 이름 |
| `models.joblib` | 위 모델과 전처리의 학습 상태. 직접 생성하며 배포본에는 없음 |

`expected/`의 CSV는 읽기 자료입니다. 실행 프로그램은 이 폴더를 읽지 않습니다. 생성 결과를 비교할 때 CSV 표시 소수점 대신 적절한 오차 허용을 생각합니다. 복원 예측은 입력 순서를 ID로 맞춰 대조합니다.

## 보고서와 제출

코드·실행 환경·세 비교표(회귀/분류/K)·예측·모델 선택 기록·보고서를 제출합니다. 모델 파일은 강사의 안내가 있을 때만 별도로 공유합니다. 보고서에는 회귀 RMSE 최소와 분류 F1 최대가 왜 다른 선택 문제인지, FP/FN 사례, test 보관, 소표본 한계를 적습니다.

Git 저장소를 사용한다면 이 폴더에서 변경한 코드·README·reports·CSV를 커밋합니다. `models.joblib`, 가상환경, 캐시, 비밀키를 올리지 않습니다. `.gitignore`는 모델 파일을 제외하도록 제공했습니다. 자동 Git 실행은 하지 않습니다.

동일 결과 재생성은 성능을 다시 고르는 과정이 아닙니다. 선택한 설정을 유지한 채 저장·복원을 확인합니다. 다른 라이브러리 버전에서 모델 호환을 보장하지 않으므로 같은 환경을 사용합니다.

## 막혔을 때 확인

`NoneType` 또는 학습 전 오류가 나오면 먼저 해당 파일의 TODO가 남아 있는지 확인합니다. `NotFittedError`는 fit 부분이 아직 `pass`인지 봅니다. 모델 설정 TODO는 파일이 실행되더라도 잘못된 결과를 낼 수 있습니다.

`ModuleNotFoundError`가 나면 VS Code가 전날의 가상환경을 선택했는지 확인합니다. `root_mean_squared_error`를 찾지 못하면 설치된 scikit-learn 버전을 확인하고 역할 폴더의 `requirements.txt`를 사용합니다.

`파일을 찾을 수 없음`이면 ZIP을 완전히 해제했는지, 코드와 함께 배포된 데이터가 이동·삭제되지 않았는지 확인합니다. 출력 CSV를 Excel에서 열어 둔 경우 저장이 막힐 수 있으므로 닫은 뒤 다시 실행합니다.

오류 메시지를 가리는 `try/except`를 추가하는 과제가 아닙니다. TODO와 파일 위치를 확인하고 계속 막히면 실행 명령과 오류 마지막 줄을 강사에게 보여 줍니다.
