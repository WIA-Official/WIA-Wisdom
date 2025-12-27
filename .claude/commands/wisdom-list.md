# /wisdom-list - WIA-Wisdom 현황 조회

사용자가 `/wisdom-list` 또는 `/wisdom-list [옵션]`을 입력하면 아래 작업을 수행합니다.

## 옵션별 동작

### /wisdom-list (전체 현황)
9개 기둥별 진행 현황을 요약하여 보여줍니다.

```
WIA-Wisdom 진행 현황 (弘益人間)
================================

| 기둥 | 완성 | 예정 | 진행률 |
|------|------|------|--------|
| 01-DHARMIC | 0 | 50+ | 0% |
| 02-ABRAHAMIC | 0 | 30+ | 0% |
| ... | ... | ... | ... |
```

### /wisdom-list [기둥번호]
특정 기둥의 상세 현황을 보여줍니다.

```bash
/wisdom-list 01          # DHARMIC 상세
/wisdom-list DHARMIC     # 동일
```

### /wisdom-list 예정
생성 예정인 모든 문서 목록을 보여줍니다.

### /wisdom-list 완성
완성된 모든 문서 목록을 보여줍니다.

## 기둥별 예정 문서 목록

### 01-DHARMIC (인도계 전통)

#### Buddhism (불교)
- [ ] core-teachings/four-noble-truths.md (사성제)
- [ ] core-teachings/eightfold-path.md (팔정도)
- [ ] core-teachings/dependent-origination.md (연기법)
- [ ] core-teachings/three-marks.md (삼법인)
- [ ] core-teachings/five-aggregates.md (오온)
- [ ] schools/theravada.md (상좌부)
- [ ] schools/mahayana.md (대승)
- [ ] schools/vajrayana.md (금강승)
- [ ] schools/zen.md (선종)
- [ ] schools/pure-land.md (정토종)
- [ ] practices/meditation.md (명상)
- [ ] practices/mindfulness.md (마음챙김)
- [ ] practices/metta.md (자비명상)
- [ ] texts/heart-sutra.md (반야심경)
- [ ] texts/diamond-sutra.md (금강경)
- [ ] texts/lotus-sutra.md (법화경)

#### Hinduism (힌두교)
- [ ] core-teachings/brahman-atman.md (브라만-아트만)
- [ ] core-teachings/dharma-karma.md (다르마-카르마)
- [ ] core-teachings/moksha.md (목샤/해탈)
- [ ] schools/vedanta.md (베단타)
- [ ] schools/yoga.md (요가)
- [ ] schools/samkhya.md (상캬)
- [ ] texts/bhagavad-gita.md (바가바드 기타)
- [ ] texts/upanishads.md (우파니샤드)
- [ ] practices/meditation.md (명상)
- [ ] practices/puja.md (푸자/예배)

#### Jainism (자이나교)
- [ ] core-teachings/ahimsa.md (비폭력)
- [ ] core-teachings/anekantavada.md (다면적 진실)
- [ ] practices/asceticism.md (고행)

#### Sikhism (시크교)
- [ ] core-teachings/ik-onkar.md (유일신)
- [ ] core-teachings/seva.md (봉사)
- [ ] texts/guru-granth-sahib.md (구루 그란트 사힙)

### 02-ABRAHAMIC (아브라함계 신앙)

#### Judaism (유대교)
- [ ] core-teachings/shema.md (쉐마)
- [ ] core-teachings/covenant.md (언약)
- [ ] core-teachings/tikkun-olam.md (티쿤 올람)
- [ ] texts/torah-overview.md (토라 개요)
- [ ] texts/talmud-overview.md (탈무드 개요)
- [ ] practices/shabbat.md (안식일)
- [ ] practices/prayer.md (기도)

#### Christianity (기독교)
- [ ] core-teachings/trinity.md (삼위일체)
- [ ] core-teachings/salvation.md (구원)
- [ ] core-teachings/love-agape.md (아가페 사랑)
- [ ] texts/gospels.md (복음서)
- [ ] texts/epistles.md (서신서)
- [ ] practices/prayer.md (기도)
- [ ] practices/sacraments.md (성례)
- [ ] traditions/orthodox.md (동방정교회)
- [ ] traditions/catholic.md (가톨릭)
- [ ] traditions/protestant.md (개신교)

#### Islam (이슬람)
- [ ] core-teachings/tawhid.md (타우히드/유일신)
- [ ] core-teachings/five-pillars.md (오주)
- [ ] core-teachings/submission.md (복종)
- [ ] texts/quran-overview.md (꾸란 개요)
- [ ] texts/hadith-overview.md (하디스 개요)
- [ ] practices/salat.md (예배)
- [ ] practices/ramadan.md (라마단)

### 03-EAST-ASIAN (동아시아 사상)

#### Confucianism (유교)
- [ ] core-teachings/ren.md (인/仁)
- [ ] core-teachings/li.md (예/禮)
- [ ] core-teachings/five-relationships.md (오륜)
- [ ] core-teachings/junzi.md (군자)
- [ ] texts/analects.md (논어)
- [ ] texts/mencius.md (맹자)
- [ ] texts/great-learning.md (대학)

#### Taoism (도교)
- [ ] core-teachings/tao.md (도/道)
- [ ] core-teachings/wu-wei.md (무위/無爲)
- [ ] core-teachings/yin-yang.md (음양)
- [ ] texts/tao-te-ching.md (도덕경)
- [ ] texts/zhuangzi.md (장자)
- [ ] practices/meditation.md (명상)
- [ ] practices/tai-chi.md (태극권)

#### Shinto (신도)
- [ ] core-teachings/kami.md (카미/神)
- [ ] core-teachings/purity.md (정화)
- [ ] practices/shrine-worship.md (신사 참배)

#### Korean Traditions (한국 전통)
- [ ] core-teachings/hongik-ingan.md (홍익인간)
- [ ] core-teachings/pungryu.md (풍류)
- [ ] shamanism/mudang.md (무당)
- [ ] philosophy/jeong.md (정/情)

### 04-HELLENIC (헬레니즘 철학)

#### Pre-Socratics (소크라테스 이전)
- [ ] philosophers/thales.md (탈레스)
- [ ] philosophers/heraclitus.md (헤라클레이토스)
- [ ] philosophers/parmenides.md (파르메니데스)
- [ ] philosophers/pythagoras.md (피타고라스)

#### Classical (고전 철학)
- [ ] philosophers/socrates.md (소크라테스)
- [ ] philosophers/plato.md (플라톤)
- [ ] philosophers/aristotle.md (아리스토텔레스)
- [ ] concepts/forms.md (이데아)
- [ ] concepts/virtue.md (덕)
- [ ] concepts/eudaimonia.md (행복)

#### Stoicism (스토아학파)
- [ ] philosophers/marcus-aurelius.md (마르쿠스 아우렐리우스)
- [ ] philosophers/seneca.md (세네카)
- [ ] philosophers/epictetus.md (에픽테토스)
- [ ] concepts/logos.md (로고스)
- [ ] practices/negative-visualization.md (부정적 시각화)
- [ ] practices/memento-mori.md (메멘토 모리)

### 05-INDIGENOUS (토착 지혜)

#### Shamanism (샤머니즘)
- [ ] core-concepts/spirit-world.md (영혼 세계)
- [ ] core-concepts/healing.md (치유)
- [ ] practices/journey.md (영적 여행)

#### African Traditions (아프리카 전통)
- [ ] philosophy/ubuntu.md (우분투)
- [ ] traditions/yoruba.md (요루바)

#### American Indigenous (아메리카 원주민)
- [ ] philosophy/seven-generations.md (7세대)
- [ ] concepts/medicine-wheel.md (의약 바퀴)

### 06-MYSTICAL (신비주의 전통)

#### Sufism (수피즘)
- [ ] poets/rumi.md (루미)
- [ ] poets/hafiz.md (하피즈)
- [ ] concepts/fana.md (파나/소멸)
- [ ] practices/dhikr.md (지크르)

#### Kabbalah (카발라)
- [ ] concepts/tree-of-life.md (생명의 나무)
- [ ] concepts/ein-sof.md (아인 소프)
- [ ] concepts/sefirot.md (세피로트)

#### Christian Mysticism (기독교 신비주의)
- [ ] mystics/meister-eckhart.md (마이스터 에크하르트)
- [ ] mystics/teresa-avila.md (아빌라의 테레사)
- [ ] concepts/dark-night.md (영혼의 어두운 밤)

### 07-MODERN-PHIL (근현대 철학)

#### Enlightenment (계몽주의)
- [ ] philosophers/descartes.md (데카르트)
- [ ] philosophers/kant.md (칸트)
- [ ] philosophers/hume.md (흄)
- [ ] concepts/cogito.md (코기토)
- [ ] concepts/categorical-imperative.md (정언명령)

#### Existentialism (실존주의)
- [ ] philosophers/kierkegaard.md (키르케고르)
- [ ] philosophers/nietzsche.md (니체)
- [ ] philosophers/sartre.md (사르트르)
- [ ] philosophers/camus.md (카뮈)
- [ ] concepts/absurd.md (부조리)
- [ ] concepts/authenticity.md (진정성)

### 08-SCIENCE (과학적 지혜)

#### Physics (물리학)
- [ ] cosmology/big-bang.md (빅뱅)
- [ ] quantum/uncertainty.md (불확정성)
- [ ] quantum/observer-effect.md (관찰자 효과)

#### Biology (생물학)
- [ ] evolution/natural-selection.md (자연선택)
- [ ] ecology/interdependence.md (상호의존)

#### Neuroscience (신경과학)
- [ ] consciousness/hard-problem.md (의식의 어려운 문제)
- [ ] meditation/brain-changes.md (명상의 뇌 변화)

#### Psychology (심리학)
- [ ] positive/flow.md (몰입)
- [ ] positive/meaning.md (의미)
- [ ] cognitive/biases.md (인지 편향)

### 09-INTEGRAL (통합 종합)

#### Systems Theory (시스템 이론)
- [ ] concepts/emergence.md (창발)
- [ ] concepts/feedback.md (피드백)
- [ ] concepts/holarchy.md (홀라키)

#### AI Ethics (AI 윤리)
- [ ] alignment/beneficence.md (이로움)
- [ ] alignment/safety.md (안전)
- [ ] alignment/hongik-ai.md (홍익 AI)

#### Future Wisdom (미래 지혜)
- [ ] long-term/seven-generations.md (7세대 사고)
- [ ] global/planetary-stewardship.md (지구 청지기)

---

## 진행 우선순위

1. **Core Teachings First**: 각 전통의 핵심 가르침 먼저
2. **Cross-Cultural Themes**: 공통 주제 발견
3. **Practices**: 실용적 수행법
4. **Texts**: 핵심 문헌 해설
5. **Integration**: 통합과 대화

---

**弘益人間 · 인류 지혜 1000년 프로젝트**
