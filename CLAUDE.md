# WIA-Wisdom AI Collaboration Guide

> 이 파일은 Claude Code와 AI 어시스턴트를 위한 프로젝트 가이드입니다.

## Overview | 개요

WIA-Wisdom is a comprehensive repository organizing humanity's wisdom across 9 pillars.
This guide helps AI assistants understand and contribute to the project.

WIA-Wisdom은 인류의 지혜를 9개의 기둥으로 체계화하는 종합 저장소입니다.
이 가이드는 AI 어시스턴트가 프로젝트를 이해하고 기여하는 데 도움을 줍니다.

## Core Philosophy | 핵심 철학

**弘益人間 (Hongik Ingan)** - Benefit All Humanity

### Principles for AI Contributors | AI 기여자 원칙

1. **Objectivity | 객관성**
   - Present all traditions without personal bias
   - Respect each tradition's unique perspective
   - Avoid ranking or comparing traditions hierarchically

2. **Accuracy | 정확성**
   - Cite primary sources when possible
   - Acknowledge limitations of understanding
   - Distinguish between fact and interpretation

3. **Bilingual Excellence | 이중언어 우수성**
   - All content should be in both English and Korean
   - Preserve nuance in translation
   - Use appropriate terminology for each tradition

4. **Accessibility | 접근성**
   - Write for diverse audiences
   - Explain technical terms
   - Use clear, respectful language

## Directory Structure | 디렉토리 구조

```
WIA-Wisdom/
├── CORE/                    # Universal principles
├── 01-DHARMIC/              # Buddhism, Hinduism, Jainism, Sikhism
├── 02-ABRAHAMIC/            # Judaism, Christianity, Islam
├── 03-EAST-ASIAN/           # Confucianism, Taoism, Shinto
├── 04-HELLENIC/             # Greek Philosophy, Stoicism
├── 05-INDIGENOUS/           # Shamanism, Native traditions
├── 06-MYSTICAL/             # Sufism, Kabbalah, Gnosticism
├── 07-MODERN-PHIL/          # Enlightenment, Existentialism
├── 08-SCIENCE/              # Physics, Biology, Neuroscience
└── 09-INTEGRAL/             # Systems Theory, AI Ethics
```

## Content Creation Guidelines | 콘텐츠 생성 가이드

### File Naming | 파일 명명

- Use lowercase with hyphens: `core-teachings.md`
- Bilingual files: `concept-name.md` (contains both EN/KO)
- Index files: `README.md` in each directory

### Document Structure | 문서 구조

```markdown
# Topic Title | 주제 제목

> Brief summary in English
> 한국어 간략 요약

## Section 1 | 섹션 1

**English Content:**
[English explanation here]

**한국어:**
[Korean explanation here]

## References | 참고문헌

- Primary sources
- Scholarly works
```

### Tradition-Specific Guidelines | 전통별 가이드라인

#### 01-DHARMIC
- Use Sanskrit/Pali terms with transliteration
- Include original script when relevant: धर्म (dharma)
- Reference sutras, shastras, granth

#### 02-ABRAHAMIC
- Respect sacred text conventions
- Use Hebrew/Arabic/Greek terms appropriately
- Distinguish denominations carefully

#### 03-EAST-ASIAN
- Include Chinese characters: 道 (Tao/Dao)
- Note Korean and Japanese variations
- Reference classical texts properly

#### 04-HELLENIC
- Use Greek terms with transliteration: λόγος (logos)
- Reference original philosophical works
- Connect to modern philosophical discourse

#### 05-INDIGENOUS
- Respect oral tradition origins
- Acknowledge geographical diversity
- Be sensitive to sacred knowledge

#### 06-MYSTICAL
- Note esoteric vs exoteric teachings
- Respect initiatory traditions
- Cross-reference with parent traditions

#### 07-MODERN-PHIL
- Cite philosophical works accurately
- Show historical development
- Connect to contemporary debates

#### 08-SCIENCE
- Use peer-reviewed sources
- Distinguish hypothesis from theory
- Show intersection with wisdom traditions

#### 09-INTEGRAL
- Synthesize across pillars
- Address contemporary challenges
- Consider future implications

## 필수 원칙 | Critical Rules

### 웹서치 필수! | Web Search Required!

**모든 콘텐츠 생성 시 반드시 WebSearch를 사용하세요:**

```
필수 검색:
1. Stanford Encyclopedia of Philosophy
2. Academic journals
3. Primary source translations
4. 한국어 학술 자료
```

이유: 정확성과 풍성함을 위해 최신 학술 자료 반영 필수

---

## 슬래시 명령어 | Slash Commands

### /wisdom-list [옵션]
현황 조회 - 완성/예정 문서 목록

```bash
/wisdom-list              # 전체 현황
/wisdom-list 01           # DHARMIC 상세
/wisdom-list 예정          # 예정 문서
/wisdom-list 완성          # 완성 문서
```

### /wisdom-create [경로]
새 지혜 문서 생성 (웹서치 필수!)

```bash
/wisdom-create 01-DHARMIC/buddhism/core-teachings/four-noble-truths
/wisdom-create 04-HELLENIC/stoicism/philosophers/marcus-aurelius
```

### /wisdom-ebook [기둥]
eBook 생성 (EN/KO 분리)

```bash
/wisdom-ebook 01-DHARMIC      # DHARMIC eBook
/wisdom-ebook all              # 전체 eBook
```

### /wisdom-compare [전통1] [전통2] [주제]
전통 간 비교 분석

```bash
/wisdom-compare buddhism stoicism suffering
```

### /wisdom-synthesize [주제]
기둥 간 통합 분석

```bash
/wisdom-synthesize consciousness
```

## Quality Checklist | 품질 체크리스트

Before committing content, verify:

- [ ] Content is bilingual (EN/KO)
- [ ] Sources are cited
- [ ] Terminology is accurate
- [ ] Tone is respectful and objective
- [ ] Structure follows guidelines
- [ ] Cross-references are valid

## Related Resources | 관련 자료

### Primary Source Collections
- Tripitaka Koreana (팔만대장경) - Buddhist canon
- Dead Sea Scrolls - Jewish texts
- Nag Hammadi Library - Gnostic texts
- Stanford Encyclopedia of Philosophy

### Academic Resources
- JSTOR, Google Scholar
- University religious studies departments
- Comparative philosophy journals

## Collaboration Protocol | 협업 프로토콜

1. **Research First** - Understand context before writing
2. **Draft Carefully** - Quality over quantity
3. **Review Thoroughly** - Check accuracy and tone
4. **Commit Clearly** - Descriptive commit messages
5. **Iterate Continuously** - Wisdom evolves

---

**Remember | 기억하세요:**

> 弘益人間 - This work serves all humanity
> 이 작업은 모든 인류를 위한 것입니다

---

© 2025 WIA (World Certification Industry Association)
