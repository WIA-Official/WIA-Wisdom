# /wisdom-ebook - eBook 생성

사용자가 `/wisdom-ebook [옵션]`을 입력하면 eBook을 생성합니다.

## 사용법

```bash
/wisdom-ebook 01-DHARMIC                    # DHARMIC 기둥 전체 eBook
/wisdom-ebook 01-DHARMIC/buddhism           # 불교만 eBook
/wisdom-ebook all                            # 전체 WIA-Wisdom eBook
/wisdom-ebook CORE                          # CORE 원칙 eBook
```

## eBook 구조

```
ebook/
├── en/                           # 영어 버전
│   ├── WIA-Wisdom-Complete.md    # 전체
│   ├── 01-DHARMIC.md             # 기둥별
│   ├── 02-ABRAHAMIC.md
│   └── ...
└── ko/                           # 한국어 버전
    ├── WIA-Wisdom-전체.md
    ├── 01-인도계전통.md
    ├── 02-아브라함계.md
    └── ...
```

## 생성 프로세스

### 1. 콘텐츠 수집
```bash
# 해당 기둥의 모든 .md 파일 수집
find [pillar]/ -name "*.md" -type f
```

### 2. 언어 분리
- EN 섹션만 추출하여 en/ 버전 생성
- KO 섹션만 추출하여 ko/ 버전 생성

### 3. 목차 생성
```markdown
# Table of Contents | 목차

1. [Overview](#overview)
2. [Core Teachings](#core-teachings)
   - [Topic 1](#topic-1)
   - [Topic 2](#topic-2)
3. [Practices](#practices)
...
```

### 4. eBook 메타데이터

```markdown
---
title: "WIA-Wisdom: [Pillar Name]"
subtitle: "弘益人間 · Benefit All Humanity"
author: "WIA (World Certification Industry Association)"
date: "2025"
language: "en" | "ko"
---
```

## eBook 템플릿

### 영어 버전 (en/)

```markdown
---
title: "WIA-Wisdom: The Dharmic Traditions"
subtitle: "Buddhism, Hinduism, Jainism, Sikhism"
author: "WIA"
---

# WIA-Wisdom: The Dharmic Traditions

> 弘益人間 · Benefit All Humanity

## Preface

This eBook is part of the WIA-Wisdom project, a comprehensive framework
organizing humanity's wisdom traditions for the 21st century and beyond.

---

## Part I: Buddhism

### Chapter 1: The Four Noble Truths

[Content from four-noble-truths.md, English only]

### Chapter 2: The Eightfold Path

[Content from eightfold-path.md, English only]

...

---

## Part II: Hinduism

...

---

## Appendix

### Glossary
### Sources
### Cross-References

---

© 2025 WIA · 弘益人間
```

### 한국어 버전 (ko/)

```markdown
---
title: "WIA-Wisdom: 인도계 전통"
subtitle: "불교, 힌두교, 자이나교, 시크교"
author: "WIA"
---

# WIA-Wisdom: 인도계 전통

> 弘益人間 · 널리 인간을 이롭게 하라

## 서문

이 eBook은 21세기와 그 이후를 위해 인류의 지혜 전통을 체계화하는
WIA-Wisdom 프로젝트의 일부입니다.

---

## 제1부: 불교

### 제1장: 사성제

[four-noble-truths.md에서 한국어만 추출]

### 제2장: 팔정도

[eightfold-path.md에서 한국어만 추출]

...

---

## 제2부: 힌두교

...

---

## 부록

### 용어집
### 출처
### 상호참조

---

© 2025 WIA · 弘益人間
```

## 배포 형식

### Markdown (.md)
- GitHub에서 직접 읽기 가능
- 가장 기본 형식

### PDF 변환 (선택)
```bash
# pandoc 사용
pandoc ebook/en/01-DHARMIC.md -o ebook/en/01-DHARMIC.pdf
```

### EPUB 변환 (선택)
```bash
# 전자책 리더용
pandoc ebook/en/01-DHARMIC.md -o ebook/en/01-DHARMIC.epub
```

## 자동 생성 스크립트

```bash
#!/bin/bash
# generate-ebook.sh

PILLAR=$1
LANG=$2

echo "Generating $PILLAR eBook in $LANG..."

# 1. 파일 수집
files=$(find $PILLAR -name "*.md" | sort)

# 2. 헤더 생성
echo "---" > ebook/$LANG/$PILLAR.md
echo "title: WIA-Wisdom: $PILLAR" >> ebook/$LANG/$PILLAR.md
echo "---" >> ebook/$LANG/$PILLAR.md

# 3. 콘텐츠 병합
for f in $files; do
  # 언어별 필터링 및 추가
  cat $f >> ebook/$LANG/$PILLAR.md
done

echo "Done: ebook/$LANG/$PILLAR.md"
```

## 완성 시 배포

1. **GitHub Release**
   - 버전 태그 (v1.0, v1.1...)
   - 변경 로그
   - eBook 파일 첨부

2. **공개 링크**
   - Raw GitHub 링크
   - GitHub Pages (선택)

3. **ISBN 등록** (선택)
   - 정식 출판물로 등록 가능

---

## 예시 실행

```bash
/wisdom-ebook 01-DHARMIC
```

결과:
```
✅ ebook/en/01-DHARMIC.md 생성됨 (15,000 words)
✅ ebook/ko/01-인도계전통.md 생성됨 (12,000자)

다운로드:
- English: https://github.com/WIA-Official/WIA-Wisdom/blob/main/ebook/en/01-DHARMIC.md
- 한국어: https://github.com/WIA-Official/WIA-Wisdom/blob/main/ebook/ko/01-인도계전통.md
```

---

**弘益人間 · 지혜를 세상에 공유하다**
