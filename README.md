# 🚀 Echelon AI

Echelon AI, LangGraph tabanlı çok ajanlı (Multi-Agent) bir pazar araştırma ve raporlama sistemidir.

Sistem; kullanıcıdan gelen bir ürün veya iş fikrini analiz ederek araştırma yapmak, trendleri incelemek, rakip analizi gerçekleştirmek, kullanıcı yorumlarını değerlendirmek, içgörüler üretmek ve tüm süreci otomatik raporlar halinde sunmak amacıyla geliştirilmiştir.

---

# 🎯 Projenin Amacı

Echelon AI'ın amacı;

- Kullanıcıdan gelen fikirleri geliştirmek,
- İnternet üzerinden güvenilir veri toplamak,
- Hallucination riskini azaltmak,
- Trend analizi yapmak,
- Rakipleri incelemek,
- Kullanıcı yorumlarını değerlendirmek,
- İçgörüler üretmek,
- Sürecin sonunda profesyonel raporlar oluşturmak,

ve bütün bunları LangGraph tabanlı çok ajanlı bir mimari ile otomatik hale getirmektir.

---

# ✨ Temel Özellikler

- 🧠 LangGraph tabanlı çok ajanlı mimari
- 🔍 Tavily destekli araştırma sistemi
- 🛡 Hallucination Guard mekanizması
- 📈 Trend analizi
- 🏆 Rakip analizi
- ⭐ Kullanıcı yorumları analizi
- 💡 Insight üretimi
- 🤖 Prompt iyileştirme
- 📄 Markdown rapor üretimi
- 📑 PDF rapor oluşturma
- 📂 JSON çıktı desteği
- 🌐 Streamlit tabanlı kullanıcı arayüzü

---

# 💼 Kullanım Senaryoları

Echelon AI aşağıdaki senaryolarda kullanılabilir:

- Amazon ürün araştırmaları
- Yeni iş fikirlerinin değerlendirilmesi
- Rakip analizi
- Trend araştırmaları
- Pazar analizi
- İçgörü üretimi
- Otomatik raporlama süreçleri
- AI destekli araştırma asistanı

---

# ⚙️ Kurulum

## Repository'nin Klonlanması

```bash
git clone <repo_url>

cd Echelon-AI
```

---

## Virtual Environment Oluşturma

```bash
python -m venv agent_env
```

Aktifleştirme:

Windows:

```bash
agent_env\Scripts\activate
```

Linux / MacOS:

```bash
source agent_env/bin/activate
```

---

## Bağımlılıkların Kurulması

```bash
pip install -r requirements.txt
```

---

## .env Ayarları

Proje ortam değişkenlerini `.env` dosyası üzerinden kullanmaktadır.

Örnek:

```env
GOOGLE_API_KEY=
TAVILY_API_KEY=
GROQ_API_KEY=
```

---

## Uygulamayı Başlatma

Streamlit arayüzünü çalıştırmak için:

```bash
streamlit run streamlit_chat.py
```

---

# 📂 Proje Yapısı

```text
Echelon-AI
│
├── agents
│
├── graphs
│
├── states
│
├── utils
│
├── output
│
├── tests
│
├── streamlit_chat.py
│
├── requirements.txt
│
└── README.md
```

---

# 📁 Klasörlerin Görevleri

| Klasör | Görevi |
|---------|--------|
| agents | Sistemdeki bütün uzman ajanları içerir |
| graphs | LangGraph workflow tanımlarını barındırır |
| states | Shared state yapısını tanımlar |
| utils | Yardımcı servisler ve araçlar |
| output | Oluşturulan çıktı dosyaları |
| tests | Test dosyaları |
| streamlit_chat.py | Kullanıcı arayüzü |
| requirements.txt | Bağımlılık listesi |

---

# 🏗 Mimari

Proje LangGraph tabanlı çok ajanlı bir mimari üzerine kurulmuştur.

Her ajan belirli bir göreve odaklanır ve sonuçlarını ortak state üzerinden diğer ajanlarla paylaşır.

Bu sayede sistem;

- Modüler
- Genişletilebilir
- Hata toleranslı
- Yönetilebilir

bir yapıya sahiptir.

---

# 🔄 Veri Akışı

Kullanıcı isteği sisteme ulaştığında:

1. Prompt iyileştirilir.
2. Araştırma gerçekleştirilir.
3. Toplanan veriler doğrulanır.
4. Hallucination riski kontrol edilir.
5. Gerekirse alternatif akış uygulanır.
6. Trend analizi yapılır.
7. Rakip analizi gerçekleştirilir.
8. Kullanıcı yorumları değerlendirilir.
9. Insight oluşturulur.
10. Otomasyon aşaması çalışır.
11. Nihai rapor oluşturulur.

---

# 🧠 LangGraph Workflow

```text
START
  ↓
prompt
  ↓
research
  ↓
validator
  ↓
(keyword veya report)
  ↓
trend
competitor
review
  ↓
insight
  ↓
automation
  ↓
report
  ↓
END
```

Validator node'u aynı zamanda Hallucination Guard görevi görmektedir.

Risk tespit edilmesi durumunda sistem alternatif akış kullanarak doğrudan rapor aşamasına geçebilir.

---

# 🔗 State Yönetimi

Sistem ortak bir Shared State mantığı kullanmaktadır.

Her ajan:

- Girdi verilerini state üzerinden alır.
- İşleme sonucunu state içerisine yazar.
- Sonraki ajanlar bu sonuçları kullanarak çalışır.

Bu yapı ajanlar arasında gevşek bağlı (loosely coupled) bir mimari oluşturur.

# 🤖 Agentler

Echelon AI, LangGraph tabanlı çok ajanlı bir mimariye sahiptir.

Her agent belirli bir uzmanlık alanına odaklanır ve ortak state üzerinden diğer agentlerle veri paylaşır.

---

# 🧩 Prompt Enhancer Agent

## Dosya

```text
agents/prompt_enhancer.py
```

## Görevi

Kullanıcıdan gelen isteği iyileştirmek ve araştırma aşamasına daha uygun hale getirmektir.

## Girdi

- Kullanıcı promptu

## Çıktı

- Düzenlenmiş / geliştirilmiş prompt

## Diğer Agentlerle İlişkisi

```text
Kullanıcı
    ↓
Prompt Enhancer
    ↓
Research Agent
```

---

# 🔍 Research Agent

## Dosya

```text
agents/research_agent.py
```

## Görevi

İnternet üzerinden veri toplamak ve araştırma sonuçlarını hazırlamaktır.

Araştırma sürecinde Tavily servisi kullanılmaktadır.

## Girdi

- Geliştirilmiş kullanıcı promptu

## Çıktı

- Araştırma verileri
- Kaynaklar
- İlk araştırma sonuçları

## Diğer Agentlerle İlişkisi

```text
Prompt Enhancer
      ↓
Research Agent
      ↓
Validator Agent
```

---

# 🛡 Validator Agent

## Dosya

```text
agents/validator_agent.py
```

## Görevi

Toplanan verilerin doğrulanması ve hallucination riskinin kontrol edilmesidir.

Sistem içerisinde Hallucination Guard görevi görmektedir.

## Girdi

- Research Agent çıktıları

## Çıktı

- Doğrulanmış araştırma sonuçları
- Risk değerlendirmesi

## Diğer Agentlerle İlişkisi

```text
Research Agent
      ↓
Validator Agent
      ↓
Keyword Agent veya Report Agent
```

---

# 🔑 Keyword Agent

## Dosya

```text
agents/keyword_agent.py
```

## Görevi

Araştırma sonuçlarından anahtar kelimeler üretmek ve sonraki aşamalarda kullanılacak yapıyı hazırlamaktır.

## Girdi

- Doğrulanmış araştırma sonuçları

## Çıktı

- Anahtar kelimeler

## Diğer Agentlerle İlişkisi

```text
Validator
    ↓
Keyword Agent
    ↓
Trend Agent
```

---

# 📈 Market Trend Agent

## Dosya

```text
agents/market_trend_agent.py
```

## Görevi

Trend analizi gerçekleştirmektir.

## Girdi

- Anahtar kelimeler
- Araştırma sonuçları

## Çıktı

- Trend verileri
- Pazar eğilimleri

## Diğer Agentlerle İlişkisi

```text
Keyword Agent
      ↓
Market Trend Agent
      ↓
Insight Agent
```

---

# 🏆 Competitor Agent

## Dosya

```text
agents/competitor_agent.py
```

## Görevi

Rakip analizi gerçekleştirmektir.

## Girdi

- Araştırma verileri

## Çıktı

- Rakip bilgileri
- Rakip değerlendirmeleri

## Diğer Agentlerle İlişkisi

```text
Keyword Agent
      ↓
Competitor Agent
      ↓
Insight Agent
```

---

# ⭐ Review Agent

## Dosya

```text
agents/review_agent.py
```

## Görevi

Yorum ve geri bildirim analizleri gerçekleştirmektir.

## Girdi

- Araştırma sonuçları

## Çıktı

- Kullanıcı yorum analizleri

## Diğer Agentlerle İlişkisi

```text
Keyword Agent
      ↓
Review Agent
      ↓
Insight Agent
```

---

# 💡 Insight Agent

## Dosya

```text
agents/insight_agent.py
```

## Görevi

Trend, rakip ve yorum analizlerinden elde edilen sonuçları birleştirerek içgörü üretmektir.

## Girdi

- Trend sonuçları
- Rakip analizleri
- Yorum analizleri

## Çıktı

- Insight verileri

## Diğer Agentlerle İlişkisi

```text
Trend Agent
Competitor Agent
Review Agent
        ↓
   Insight Agent
        ↓
Automation Agent
```

---

# ⚙ Automation Agent

## Dosya

```text
agents/automation_agent.py
```

## Görevi

Insight aşamasından gelen sonuçların sonraki işlemler için hazırlanmasını sağlamaktır.

## Girdi

- Insight sonuçları

## Çıktı

- İşlenmiş sonuçlar

## Diğer Agentlerle İlişkisi

```text
Insight Agent
      ↓
Automation Agent
      ↓
Report Agent
```

---

# 📄 Report Agent

## Dosya

```text
agents/report_agent.py
```

## Görevi

Sistemin nihai raporlarını oluşturmaktır.

## Girdi

- Bütün ajanlardan gelen sonuçlar

## Çıktı

- Markdown raporları
- PDF raporları
- JSON çıktıları

## Diğer Agentlerle İlişkisi

```text
Automation Agent
      ↓
Report Agent
      ↓
END
```

---

# 🔄 Agentler Arasındaki Genel İlişki

```text
User
 ↓
Prompt Enhancer
 ↓
Research
 ↓
Validator
 ↓
Keyword
 ↓
 ├── Market Trend
 ├── Competitor
 └── Review
         ↓
      Insight
         ↓
     Automation
         ↓
       Report
         ↓
        END
```

# 🏗 Graph Yapısı

Echelon AI, LangGraph tabanlı bir workflow mimarisi kullanmaktadır.

Graph tanımı:

```text
graphs/market_graph.py
```

Bu dosya sistem içerisindeki node'ları, edge bağlantılarını ve çalışma sırasını tanımlar.

---

# 🔗 Node Yapısı

Sistemde bulunan node'lar:

| Node | Görevi |
|--------|--------|
| prompt | Kullanıcı isteğini iyileştirmek |
| research | Araştırma yapmak |
| validator | Verileri doğrulamak |
| keyword | Anahtar kelimeleri üretmek |
| trend | Trend analizi yapmak |
| competitor | Rakip analizi yapmak |
| review | Kullanıcı yorumlarını analiz etmek |
| insight | İçgörü üretmek |
| automation | Sonuçları işlemek |
| report | Nihai raporu oluşturmak |

---

# 🔄 Workflow

LangGraph akışı aşağıdaki şekilde çalışmaktadır:

```text
START
  ↓
prompt
  ↓
research
  ↓
validator
  ↓
keyword
  ↓
 ├──── trend
 ├──── competitor
 └──── review
          ↓
       insight
          ↓
      automation
          ↓
        report
          ↓
         END
```

---

# 🌐 Veri Akışı

Sistem aşağıdaki sırayla çalışmaktadır:

## 1. Prompt Aşaması

Kullanıcının isteği alınır.

↓

Prompt Enhancer Agent tarafından geliştirilir.

↓

Araştırma aşamasına aktarılır.

---

## 2. Araştırma Aşaması

Research Agent;

- İnternet araştırması yapar,
- Verileri toplar,
- Sonuçları state içerisine kaydeder.

↓

Validator Agent'a aktarılır.

---

## 3. Doğrulama Aşaması

Validator Agent;

- Verileri inceler,
- Hallucination riskini değerlendirir,
- Sonuçları doğrular.

↓

Keyword Agent'a aktarır.

---

## 4. Anahtar Kelime Üretimi

Keyword Agent;

Araştırma sonuçlarından anlamlı anahtar kelimeler çıkarır.

↓

Bu anahtar kelimeler üç farklı uzman agent tarafından kullanılır.

---

## 5. Paralel Analiz Aşaması

### Trend Analizi

Market Trend Agent:

- Trendleri inceler
- Pazar eğilimlerini değerlendirir

---

### Rakip Analizi

Competitor Agent:

- Rakipleri inceler
- Rakiplerin güçlü ve zayıf yönlerini değerlendirir

---

### Yorum Analizi

Review Agent:

- Kullanıcı yorumlarını inceler
- Geri bildirimleri değerlendirir

---

Bu üç ajan bağımsız çalışır.

↓

Sonuçlar Insight Agent'ta birleştirilir.

---

## 6. Insight Üretimi

Insight Agent;

- Trend sonuçlarını,
- Rakip analizlerini,
- Yorum analizlerini

bir araya getirerek genel içgörüler üretir.

↓

Automation Agent'a aktarılır.

---

## 7. Otomasyon Katmanı

Automation Agent;

Insight sonuçlarını işler.

↓

Report Agent'a gönderir.

---

## 8. Raporlama Katmanı

Report Agent;

Sistem içerisindeki bütün sonuçları kullanarak:

- Markdown raporu
- PDF raporu
- JSON çıktıları

oluşturur.

---

# 🧠 State Yapısı

State tanımı:

```text
states/market_state.py
```

Bu dosya LangGraph içerisinde kullanılan ortak veri yapısını tanımlar.

---

# Shared State Mantığı

Sistem merkezi bir Shared State yapısı kullanmaktadır.

Her agent:

1. State içerisinden gerekli verileri alır.
2. Kendi işlemlerini gerçekleştirir.
3. Sonuçlarını tekrar state içerisine kaydeder.
4. Sonraki agent'lar bu verileri kullanır.

Bu sayede agent'lar arasında doğrudan bağımlılık yerine state tabanlı veri paylaşımı sağlanır.

---

# 🔄 Agentler Arası Veri Paylaşımı

```text
Prompt
 ↓
Research
 ↓
Validator
 ↓
Keyword
 ↓
 ├── Trend
 ├── Competitor
 └── Review
         ↓
      Insight
         ↓
    Automation
         ↓
       Report
```

Her aşamada üretilen veriler state içerisinde tutulur.

---

# 🎯 Shared State Yaklaşımının Avantajları

Bu mimari;

- Modülerlik
- Esneklik
- Ölçeklenebilirlik
- Düşük bağımlılık
- Kolay bakım
- Yeni agent ekleme kolaylığı

gibi avantajlar sağlamaktadır.

---

# 🛡 Hallucination Guard

Validator Agent aynı zamanda bir Hallucination Guard görevi üstlenmektedir.

Amaç:

- Güvenilir olmayan verileri tespit etmek,
- Riskli sonuçları filtrelemek,
- Yanlış bilgi üretimini azaltmak,
- Rapor kalitesini artırmaktır.

Bu katman sistemin güvenilirliğini artırmak için workflow içerisine entegre edilmiştir.

---

# 📌 Genel Mimari

```text
                     Shared State

                           ▲
                           │

Prompt Agent ──────────────┤
Research Agent ────────────┤
Validator Agent ───────────┤
Keyword Agent ─────────────┤
Trend Agent ───────────────┤
Competitor Agent ──────────┤
Review Agent ──────────────┤
Insight Agent ─────────────┤
Automation Agent ──────────┤
Report Agent ──────────────┘
```

Bütün ajanlar ortak state yapısı üzerinden haberleşmektedir.

# 🛠 Utils

Utils klasörü, sistem içerisinde kullanılan yardımcı servisleri ve ortak bileşenleri içermektedir.

```text
utils
│
├── llm.py
├── scraper.py
└── tavily_client.py
```

---

# 🧠 llm.py

## Görevi

LLM (Large Language Model) katmanını yönetmektedir.

Bu katman, agentlerin kullandığı dil modeli bağlantılarının merkezi olarak yönetilmesini sağlar.

## Kullanıldığı Yerler

- Agentler
- LangGraph workflow'u

## Sağladığı Yapı

- Model erişimi
- Ortak LLM yapılandırması
- Merkezi model yönetimi

---

# 🌐 scraper.py

## Görevi

Veri toplama süreçlerinde kullanılan yardımcı scraping işlemlerini içermektedir.

## Kullanıldığı Yerler

- Araştırma süreçleri

## Sağladığı Yapı

- Veri çekme işlemleri
- Yardımcı web veri toplama fonksiyonları

---

# 🔎 tavily_client.py

## Görevi

Tavily API bağlantısını yönetmektedir.

## Kullanıldığı Yerler

- Research Agent

## Sağladığı Yapı

- İnternet araştırması
- Kaynak toplama
- Arama sonuçlarının elde edilmesi

---

# 🖥 Streamlit Arayüzü

Arayüz dosyası:

```text
streamlit_chat.py
```

Bu dosya kullanıcı ile sistem arasındaki etkileşimi sağlamaktadır.

---

# Kullanıcı Akışı

```text
Kullanıcı
     ↓
Prompt Girişi
     ↓
LangGraph Workflow
     ↓
Agentler
     ↓
Rapor Oluşturma
     ↓
Sonuçların Gösterilmesi
```

---

# Arayüz Bileşenleri

Streamlit arayüzü;

- Kullanıcı giriş alanı
- Sonuç görüntüleme alanı
- Agent çıktıları
- Rapor sonuçları

gibi bileşenleri yönetmektedir.

---

# Sonuç Ekranları

Sistem tarafından oluşturulan sonuçlar arayüz üzerinden görüntülenebilir.

Üretilen çıktılar:

- Markdown raporları
- PDF raporları
- JSON dosyaları

---

# 📂 Output

Output klasörü sistem tarafından oluşturulan çıktıları içermektedir.

Bu klasör içerisinde:

## 📄 Markdown Raporları

AI tarafından oluşturulan raporlar saklanmaktadır.

---

## 📑 PDF Çıktıları

Raporların PDF formatındaki sürümleri saklanmaktadır.

---

## 🗂 JSON Çıktıları

Agentlerden gelen sonuçların JSON formatındaki kayıtları tutulmaktadır.

---

# 🧪 Testler

Test klasörü:

```text
tests
│
├── market_graph_test.py
└── test_gemini.py
```

---

# market_graph_test.py

## Doğrulanan Modül

LangGraph workflow yapısı

## Amaç

Graph yapısının beklenen şekilde çalıştığını doğrulamak.

---

# test_gemini.py

## Doğrulanan Modül

Gemini entegrasyonu

## Amaç

Model bağlantısının ve cevap üretiminin test edilmesi.

---

# 💻 Kullanılan Teknolojiler

## Ana Teknolojiler

- Python
- Streamlit
- LangGraph
- Gemini
- Groq
- Tavily

---

# Kullanılan Kütüphaneler

Projedeki bağımlılıklar `requirements.txt` dosyasından yönetilmektedir.

Başlıca kullanılan teknolojiler:

| Teknoloji | Amaç |
|------------|-----|
| Python | Temel programlama dili |
| Streamlit | Arayüz |
| LangGraph | Workflow yönetimi |
| LangChain | Agent altyapısı |
| Gemini | LLM desteği |
| Groq | Alternatif LLM desteği |
| Tavily | İnternet araştırmaları |
| dotenv | Ortam değişkenleri |
| JSON | Veri saklama |
| Markdown | Raporlama |
| PDF | Nihai çıktı üretimi |

---

# 🔮 Gelecek Geliştirmeler

Kod yapısı içerisinde;

- Yeni agentler eklenmesi,
- Workflow'un genişletilmesi,
- LLM seçeneklerinin artırılması,
- Raporlama sisteminin geliştirilmesi,
- Araştırma süreçlerinin iyileştirilmesi,

gibi geliştirmelere uygun modüler bir mimari bulunmaktadır.

Not:

Gemini ve Groq istemcileri geleceğe yönelik destek amacıyla sistem içerisinde tutulmaktadır.

---

# 🤝 Katkıda Bulunma

Katkılar memnuniyetle karşılanmaktadır.

Katkıda bulunmak için:

1. Repository'yi fork edin.
2. Yeni bir branch oluşturun.

```bash
git checkout -b feature/yeni-ozellik
```

3. Değişikliklerinizi commit edin.

```bash
git commit -m "Yeni özellik eklendi"
```

4. Branch'i gönderin.

```bash
git push origin feature/yeni-ozellik
```

5. Pull Request oluşturun.

---

# 📜 Lisans

Bu proje açık kaynak olarak geliştirilmektedir.

Lisans bilgisi repository içerisinde belirtilmelidir.

---

# 🎯 Sonuç

Echelon AI;

LangGraph tabanlı çok ajanlı mimarisi sayesinde araştırma, doğrulama, trend analizi, rakip analizi, yorum değerlendirmesi, içgörü üretimi ve raporlama süreçlerini tek bir workflow altında birleştiren modüler bir AI sistemidir.

Shared State yapısı sayesinde agentler arasında veri paylaşımı sağlanmakta, Hallucination Guard mekanizması ile güvenilirlik artırılmakta ve sonuçlar Markdown, PDF ve JSON formatlarında kullanıcıya sunulmaktadır.

Bu yapı; genişletilebilir, sürdürülebilir ve yeni agentlerin eklenmesine uygun olacak şekilde tasarlanmıştır.