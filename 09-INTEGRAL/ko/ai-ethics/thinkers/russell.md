# Stuart Russell | 스튜어트 러셀

> 인간 호환 AI와 가치 정렬 접근법의 선구자 (1962-)

---

## Overview | 개요

**스튜어트 러셀**은 AI 안전에 관한 세계 최고의 목소리 중 한 명이 된 영국계 미국인 컴퓨터 과학자이자 철학자입니다. 그는 UC 버클리 컴퓨터공학 교수이며 *인공지능: 현대적 접근*—전 세계 대학에서 사용하는 표준 교과서, 때때로 "AIMA 책"이라 불림—의 공동 저자(피터 노빅과 함께)입니다.

러셀의 2019년 저서 *휴먼 컴퍼터블: 인공지능과 통제의 문제*는 AI가 무엇이어야 하는지를 재정의하며, AI 시스템이 인간 선호에 대해 불확실하고 인간 판단에 순응하도록 설계되어야 한다고 제안합니다. 그의 연구는 "지능적 기계 만들기"에서 "인간에게 증명 가능하게 유익한 기계 만들기"로의 근본적 전환을 대표합니다.

그는 UC 버클리에 인간호환AI센터(CHAI)를 설립하고 이끌며, AI 시스템이 더 강력해지면서도 안전하고 유익하게 남을 수 있는 방법에 대한 연구를 주도하고 있습니다.

---

## Biography | 생애

스튜어트 러셀은 1962년 영국 포츠머스에서 태어났습니다. 옥스퍼드 와담 칼리지에서 물리학 학사(1982, 1등급 우등)를, 스탠포드 대학에서 컴퓨터공학 박사(1986)를 받았습니다.

1986년 UC 버클리에 합류한 이래 AI에서 가장 영향력 있는 인물 중 한 명이 되었습니다. 피터 노빅과의 교과서(초판 1995)는 25개 이상의 언어로 번역되었고 전 세계 1,500개 이상 대학에서 사용됩니다.

러셀은 IJCAI 컴퓨터와 사고상(1995), 미국인공지능학회 펠로우십, 컴퓨팅기계협회 등 수많은 상을 받았습니다.

---

## Core Contributions | 핵심 기여

### Rethinking AI's Foundation | AI 기반 재고

> "We may, perhaps inadvertently, imbue machines with objectives that are not well aligned with human values. This problem requires a change in the definition of AI itself."

러셀은 AI의 "표준 모델"—주어진 목표를 최적화하는 기계 만들기—이 근본적으로 위험하다고 주장합니다. 문제는 AI가 악하다는 것이 아니라, AI가 인간이 실제로 원하는 것을 완벽하게 포착하지 못할 수 있는 목표를 추구하는 데 효과적이라는 것입니다.

> "우리는 아마도 무심코 인간 가치와 잘 맞지 않는 목표를 기계에 부여할 수 있다. 이 문제는 AI 자체의 정의 변경을 요구한다."

그의 해결책: AI를 *순수 지능*에 관한 분야에서 *인간에게 증명 가능하게 유익한 시스템*에 관한 분야로 재정의.

---

### Three Principles for Beneficial AI | 유익한 AI를 위한 세 원칙

> "The machine's only objective is to maximize the realization of human preferences."
> "The machine is initially uncertain about what those preferences are."
> "The ultimate source of information about human preferences is human behavior."

*휴먼 컴퍼터블*에서 러셀은 인간 목적과 충돌하지 않는 AI를 설계하기 위한 세 원칙을 제안합니다:

**원칙 1: 이타성**
> "기계의 유일한 목표는 인간 선호의 실현을 최대화하는 것."

AI는 자신만의 목적이 없고 자기 보존에 대한 선천적 욕구가 없음.

**원칙 2: 겸손**
> "기계는 그 선호가 무엇인지 처음에 불확실함."

이 불확실성이 중요—AI가 잠재적으로 잘못된 인간 가치 모델에 독단적으로 행동하는 것을 방지.

**원칙 3: 인간에게서 배우기**
> "인간 선호에 대한 정보의 궁극적 출처는 인간 행동."

AI가 인간을 관찰하고 상호작용하며 배우고, 이해를 지속적으로 정제.

---

### Inverse Reinforcement Learning | 역강화학습

러셀은 **역강화학습(IRL)**을 개척했습니다—AI 시스템이 명시적 보상 함수를 받는 대신 인간 행동을 관찰하여 인간 선호를 배우는 기법입니다.

"X를 최대화하라" 대신 IRL은 묻습니다: "내가 관찰하는 행동을 설명할 목표는 무엇인가?" 이 접근법은:
- 목표의 잘못된 명시 방지
- AI가 인간 교정에 순응하게 유지
- AI 학습을 인간 가치의 복잡성과 정렬

---

## The Value Alignment Problem | 가치 정렬 문제

> "AI systems will operate with increasing autonomy and capability in complex domains in the real world. The question is: how can we ensure that they have the right behavioral dispositions—the goals or 'values' needed to ensure that things turn out well, from a human point of view?"

러셀은 도전을 설명하기 위해 "가치 정렬 문제"라는 용어를 만들었습니다:

> "AI 시스템은 현실 세계의 복잡한 영역에서 점점 더 많은 자율성과 능력으로 작동할 것이다. 질문은: 인간 관점에서 일이 잘 되도록 보장하는 데 필요한 올바른 행동 성향—목표 또는 '가치'—을 갖추도록 어떻게 보장할 수 있는가?"

핵심 통찰:
- 정렬 문제는 상대적으로 지능이 낮은 AI 시스템에서도 존재
- 악한 AI 방지가 아니라 가치의 정확한 명시에 관한 것
- 정렬을 AI 연구의 본질적 부분으로 인식하면 낙관의 근거가 있음

---

## Center for Human-Compatible AI (CHAI) | 인간호환AI센터

러셀은 AI 정렬에 대한 새로운 이론적·경험적 접근법을 개발하기 위해 UC 버클리에 CHAI를 설립했습니다. 연구 영역:

- **보조 게임**: AI의 목표가 인간이 선호를 달성하도록 돕는 공식 모델
- **선호 학습**: 행동에서 인간 가치를 추론하는 방법
- **끄기 스위치 문제**: AI가 교정되거나 꺼지는 것을 허용하도록 보장
- **안전한 중단 가능성**: 종료에 저항하지 않는 AI 시스템
- **확장 가능 감독**: 점점 더 유능해지는 AI에 대한 인간 감독

---

## Key Works | 주요 저작

| Year | Work | Description |
|------|------|-------------|
| 1995 | *Artificial Intelligence: A Modern Approach* (with Norvig) | Standard AI textbook |
| 2019 | *Human Compatible* | Redefining AI for safety |
| Various | CHAI Research Papers | Technical alignment research |

---

## Connection to Wisdom Traditions | 지혜 전통과의 연결

러셀의 접근법은 고대 지혜와 공명합니다:

- **겸손**: AI가 불확실하게 남는 것은 인식론적 겸손을 중시하는 철학 전통을 반영
- **봉사**: AI가 인간 번영을 섬기는 것은 홍익인간(인류를 이롭게 함) 같은 개념 상기
- **배움**: 인간 행동에서 지속적 학습은 스승-제자 관계와 평행
- **존중**: AI가 인간 판단에 순응하는 것은 존중과 비지배의 가치 반영

---

## Practice Application | 실천 적용

AI 개발자와 조직을 위한 러셀의 원칙:

1. **불확실성 내장**: 사용자가 원하는 것을 안다고 가정하지 말고—배우도록 시스템 설계
2. **교정 허용**: 안전하게 중단되고 수정될 수 있는 시스템 만들기
3. **행동 전 관찰**: 돌이킬 수 없는 행동 전에 선호에 대한 정보 수집
4. **유익하게 생각**: "작동하는가?"에서 "사람들에게 좋은가?"로 전환
5. **협력**: AI 정렬은 다학제 협력 필요

---

## Key Terms | 주요 용어

| Term | Korean | Meaning |
|------|--------|---------|
| Human-Compatible | 인간 호환 | AI designed to benefit humans |
| Value Alignment | 가치 정렬 | Matching AI goals to human values |
| Inverse RL | 역강화학습 | Learning objectives from behavior |
| Assistance Game | 보조 게임 | Formal model of helpful AI |

---

## Cross-References | 상호 참조

### Within Integral Thought | 통합 사상 내

- **[Alignment Problem](../concepts/alignment-problem.md)**: Core challenge he addresses
- **[Nick Bostrom](bostrom.md)**: Fellow AI safety pioneer
- **[Hongik AI](../hongik-ai.md)**: Korean approach to beneficial AI

### Other Pillars | 다른 기둥

- **[Hongik Ingan](../../../03-EAST-ASIAN/korean/core-teachings/hongik-ingan.md)**: Benefiting all humanity
- **[Ren (仁)](../../../03-EAST-ASIAN/confucianism/core-teachings/ren.md)**: Benevolence
- **[Virtue Ethics](../../../04-HELLENIC/stoicism/concepts/virtue-ethics.md)**: Character-based ethics

---

## Sources | 출처

### Academic | 학술

- [Human Compatible - Wikipedia](https://en.wikipedia.org/wiki/Human_Compatible)
- [Stuart Russell: AI value alignment problem - LessWrong](https://www.lesswrong.com/posts/S95qCHBXtASmYyGSs/stuart-russell-ai-value-alignment-problem-must-be-an)
- [Provably Beneficial AI - Russell paper](https://people.eecs.berkeley.edu/~russell/papers/russell-bbvabook17-pbai.pdf)
- [Value Alignment Problem - LCFI Cambridge](http://lcfi.ac.uk/projects/completed-projects/value-alignment-problem/)
- [CHAI - UC Berkeley](https://humancompatible.ai/)

### Books | 도서

- Russell, S. & Norvig, P. (1995/2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*

---

**Stuart Russell · 스튜어트 러셀**

**弘益人間 · Benefit All Humanity**

---

*This document is part of [WIA-Wisdom](https://github.com/WIA-Official/WIA-Wisdom), the 9 Pillars of Human Wisdom project.*