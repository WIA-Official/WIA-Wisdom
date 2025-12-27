# /wisdom-create - WIA-Wisdom 콘텐츠 생성

사용자가 `/wisdom-create [경로]`를 입력하면 해당 지혜 문서를 생성합니다.

## 사용법

```bash
/wisdom-create 01-DHARMIC/buddhism/core-teachings/four-noble-truths
/wisdom-create 02-ABRAHAMIC/judaism/core-teachings/shema
/wisdom-create 04-HELLENIC/stoicism/philosophers/marcus-aurelius
```

## 필수 프로세스

### 1. 웹 검색 (필수!)

**반드시 WebSearch를 사용하여 최신 학술 자료를 검색합니다:**

```
검색 예시:
- "Four Noble Truths Buddhism scholarly"
- "사성제 불교 학술"
- "Stanford Encyclopedia Philosophy [topic]"
- "[topic] primary sources academic"
```

**검색 소스 우선순위:**
1. Stanford Encyclopedia of Philosophy
2. Internet Encyclopedia of Philosophy
3. Academic journals (JSTOR, Google Scholar)
4. University religious studies departments
5. Primary text translations
6. Reputable religious organization sites

### 2. 문서 구조 (표준 템플릿)

```markdown
# [Topic Title] | [한국어 제목]

> [One-line summary in English]
> [한국어 한 줄 요약]

---

## Overview | 개요

**English:**
[3-5 paragraphs explaining the concept, its origins, significance]

**한국어:**
[3-5 문단으로 개념, 기원, 의미 설명]

---

## Core Content | 핵심 내용

### [Subsection 1] | [소제목 1]

**English:**
[Detailed explanation]

**한국어:**
[상세 설명]

### [Subsection 2] | [소제목 2]
...

---

## Key Terms | 주요 용어

| Term | Original | Meaning | 의미 |
|------|----------|---------|------|
| [term] | [원어] | [English meaning] | [한국어 의미] |

---

## Primary Sources | 1차 자료

- [Source 1 with citation]
- [Source 2 with citation]

---

## Practice Application | 실천 적용

**English:**
[How this wisdom applies to daily life]

**한국어:**
[일상생활에서의 적용]

---

## Cross-References | 상호 참조

- **[Related Pillar](link)**: [Connection explanation]
- **[Related Topic](link)**: [Connection explanation]

---

## Sources | 출처

- [Academic source 1]
- [Academic source 2]
- [Primary text translation]

---

**弘益人間 · Benefit All Humanity**
```

### 3. 품질 기준

#### 필수 요소
- [ ] 이중언어 (EN/KO) 완전 병기
- [ ] 웹서치로 학술 자료 확인
- [ ] 원어 표기 (Sanskrit, Hebrew, Greek, Chinese 등)
- [ ] 1차 자료 인용
- [ ] 다른 기둥과의 연결점 명시
- [ ] 실천적 적용 포함

#### 금지 사항
- ❌ 단일 언어만 작성
- ❌ 웹서치 없이 작성
- ❌ 특정 전통 비하 또는 우위 주장
- ❌ 검증되지 않은 정보
- ❌ 지나친 단순화

### 4. 파일 생성

```bash
# 디렉토리 생성
mkdir -p [pillar]/[tradition]/[category]

# 파일 생성
Write [pillar]/[tradition]/[category]/[topic].md
```

### 5. 완료 후 작업

```bash
# Git 커밋
git add -A
git commit -m "docs([pillar]): Add [topic] (EN/KO)"
git push origin main

# wisdom-list 업데이트
# - [ ] 를 - [x] 로 변경
```

---

## 예시: 사성제 생성

```bash
/wisdom-create 01-DHARMIC/buddhism/core-teachings/four-noble-truths
```

### Step 1: 웹서치
```
WebSearch: "Four Noble Truths Buddhism scholarly definition"
WebSearch: "사성제 팔리어 원문 해설"
WebSearch: "dukkha samudaya nirodha magga meaning"
```

### Step 2: 문서 작성
```markdown
# Four Noble Truths | 사성제 (四聖諦)

> The foundational teaching of Buddhism on the nature and cessation of suffering
> 고통의 본질과 소멸에 대한 불교의 근본 가르침

---

## Overview | 개요

**English:**
The Four Noble Truths (Pali: cattāri ariyasaccāni) represent the Buddha's first
teaching after his enlightenment, delivered in the Deer Park at Sarnath. They
form the conceptual framework for all Buddhist thought...

**한국어:**
사성제(四聖諦, 팔리어: cattāri ariyasaccāni)는 붓다가 깨달음을 얻은 후
사르나트의 녹야원에서 전한 첫 번째 가르침입니다. 이는 모든 불교 사상의
개념적 틀을 형성합니다...

---

## The Four Truths | 네 가지 진리

### 1. Dukkha (苦) - Suffering | 고

**English:**
Life inherently involves suffering, unsatisfactoriness, and impermanence...

**한국어:**
삶은 본질적으로 고통, 불만족, 무상함을 포함합니다...

### 2. Samudaya (集) - Origin | 집

...

### 3. Nirodha (滅) - Cessation | 멸

...

### 4. Magga (道) - Path | 도

...

---

## Key Terms | 주요 용어

| Term | Pali/Sanskrit | Meaning | 의미 |
|------|---------------|---------|------|
| Dukkha | दुःख | Suffering, unsatisfactoriness | 고통, 불만족 |
| Tanha | तृष्णा | Craving, thirst | 갈애, 갈망 |
| Nirvana | निर्वाण | Extinction of suffering | 열반, 고통의 소멸 |

---

## Primary Sources | 1차 자료

- Dhammacakkappavattana Sutta (SN 56.11) - 전법륜경
- Saccavibhanga Sutta (MN 141) - 제성분별경

---

## Cross-References | 상호 참조

- **[Eightfold Path](./eightfold-path.md)**: The Fourth Truth elaborated
- **[Stoicism](../../04-HELLENIC/stoicism/)**: Parallel views on suffering
- **[Psychology](../../08-SCIENCE/psychology/)**: Buddhist psychology research

---

## Sources | 출처

- Bodhi, Bhikkhu. "The Noble Eightfold Path." Buddhist Publication Society.
- Gethin, Rupert. "The Foundations of Buddhism." Oxford University Press.
- 대한불교조계종. "불교 기초교리." 조계종출판사.

---

**弘益人間 · Benefit All Humanity**
```

---

## 배치 생성

여러 문서를 한 번에 생성할 때:

```bash
/wisdom-create-batch 01-DHARMIC/buddhism/core-teachings
```

이 명령은 해당 카테고리의 모든 예정 문서를 순차적으로 생성합니다.

---

## 우선순위 추천

### Phase 1: 핵심 가르침 (각 전통 3-5개)
가장 중요한 핵심 개념들

### Phase 2: 실천법 (각 전통 2-3개)
명상, 기도, 수행법

### Phase 3: 핵심 문헌 (각 전통 2-3개)
가장 중요한 경전/텍스트 해설

### Phase 4: 인물 (각 전통 2-3명)
핵심 사상가, 성인

### Phase 5: 통합과 대화
기둥 간 비교, 공통점, 대화

---

**弘益人間 · 1000년 프로젝트**
