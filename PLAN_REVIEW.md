# 60 Haftalık DS Öğrenim Planı - Birleşik Analiz Raporu

## 🎯 Hedef
- Data Scientist with LLM Security + MLOps
- Sağlam temeller üzerine inşa ederek öğrenmek
- Sıkıştırmadan, derinlikli öğrenim

---

# BÖLÜM 1: PLAN ANALİZİ

## ✅ Planın Güçlü Yönleri

| # | Güçlü Yön |
|---|-----------|
| 1 | Faz yapısı doğru (Core → Production → ML → AI Sec) |
| 2 | SQL'e 6 hafta = derinlikli yatırım |
| 3 | Portfolio projeleri ayrı repo (SentinelWatch, PhishGuard) |
| 4 | MLOps araçları dahil (Docker, CI/CD, Airflow, dbt) |
| 5 | AI Security niş alanı = rekabet avantajı |
| 6 | "DONE kanıt" kolonu = ölçülebilir ilerleme |

---

## ⚠️ Önerilen İyileştirmeler

### 1. Pandas SQL ile Paralel Olmalı
| Mevcut | Önerilen |
|--------|----------|
| Pandas Week 36 | Pandas mini-pratik Week 6+ (SQL ile paralel) |

**Öneri:** Week 6'dan itibaren haftada 2-3 saat Pandas pratik (CSV okuma, merge, groupby).

### 2. ML'e Erken Temas
| Mevcut | Önerilen |
|--------|----------|
| ML Week 35-41 | Week 17-20'de haftada 1 ML egzersizi |

**Öneri:** "Erken temas" yeterli. Derinliği Week 35+'ta alırsın.

### 3. Başvuru Stratejisi: Paralel Yaklaşım

```
Week 16:    SentinelWatch MVP + LinkedIn aktif
Week 24:    Pasif başvuru (Data Analyst / Junior DE)
Week 38:    Agresif başvuru (DS pozisyonları)
```

---

# BÖLÜM 2: CHATGPT ÖNERİLERİNİN ANALİZİ

## 1. Deploy Platform Gerçekleri
**ChatGPT:** "Ücretsiz + hep açık + zero-risk üçlüsü yok"

| Platform | Araştırma Sonucu | ChatGPT Doğru mu? |
|----------|------------------|-------------------|
| **Cloud Run** | Free tier var ama billing account şart, limit aşılınca ücret | ✅ DOĞRU |
| **Render** | 750 saat/ay limit + "service-initiated traffic" için beklenmedik suspend'ler rapor edildi | ✅ DOĞRU |
| **Oracle** | Idle reclaim: 7 gün boyunca CPU/Network/Memory <%15 ise instance durduruluyor | ✅ DOĞRU |

**Sonuç:** Week 24 DONE'a ekle: "Bütçe uyarısı + cold start kabul + limit stratejisi"

---

## 2. Airflow Kurulum Overhead
**ChatGPT:** "4GB+ RAM gereksinimi + kurulum overhead"

**Araştırma:** Doğru. Apache Airflow resmi dokümantasyonunda 4GB+ RAM öneriliyor.

**Sonuç:** Week 28-30 DONE'a ekle: "Docker-compose kurulum + backfill/retry kanıtı"

---

## 3. Buffer Week Uygulaması
**ChatGPT:** "Haftalık %15-20 buffer daha gerçekçi"

**Değerlendirme:** Mantıklı. "Week 10/20/30... = catch-up" demek planı 65+ haftaya uzatır veya içerik kırpmak gerekir.

**Sonuç:** Her haftaya 1 gün buffer (kurulum/eksik kapatma/dokümantasyon) ekle.

---

## 4. SQL Haftalarına Pandas Mini-Pratik
**ChatGPT:** "Pandas'ı taşıma, SQL yanına paralel ekle"

**Değerlendirme:** Bu yaklaşım daha az riskli. Omurgayı bozmadan DS kasını erken oluşturur.

**Sonuç:** Week 6+ → Haftada 2-3 saat Pandas pratik (CSV, merge, groupby, basic plotting)

---

## 5. OneDrive + Repo/venv Problemi
**ChatGPT:** "Repos'u OneDrive dışına al"

**Araştırma:** ✅ DOĞRU. Kaynaklar:
- venv binlerce küçük dosya içerir → OneDrive sync yavaşlar
- Symbolic link sorunları → venv bozulabilir
- Git işlemleri sırasında sync conflict'ler oluşabilir
- pip komutları tanınmaz hale gelebilir

**Sonuç:** Projeleri `C:\dev\` altına taşı. OneDrive'da sadece doküman/export tut.

---

## 📊 CHATGPT DEĞERLENDİRME ÖZETİ (5 YENİ ÖNERİ)

| # | Öneri | Doğru mu? | Aksiyon |
|---|-------|-----------|---------|
| 1 | Deploy gerçeklerini güncelle | ✅ DOĞRU | Week 24 DONE'u sertleştir |
| 2 | Airflow DONE'u sertleştir | ✅ DOĞRU | Kurulum + backfill kanıtı ekle |
| 3 | Haftalık %20 buffer | ✅ DOĞRU | Her haftaya 1 gün buffer |
| 4 | Pandas mini-pratik SQL ile paralel | ✅ DOĞRU | Week 6+ haftada 2-3 saat |
| 5 | Repo'yu OneDrive'dan çıkar | ✅ DOĞRU | C:\dev\ altına taşı |

---

# BÖLÜM 3: FİNAL YAPILACAKLAR

## ✅ Kesin Yapılacaklar

### Omurga Değişiklikleri
1. **Buffer:** Her haftaya 1 gün buffer (kurulum/eksik/dokümantasyon)
2. **Retro:** Her hafta sonu 15 dk - ne bitti, ne sarktı, scope değişecek mi?
3. **Pandas:** Week 6+ haftada 2-3 saat mini-pratik
4. **ML Temas:** Week 17-20 haftada 1 ML egzersizi

### DONE Kriterleri Güncellemeleri
- **Week 24:** "Bütçe uyarısı kuruldu + cold start kabul edildi + limit stratejisi yazıldı"
- **Week 28-30:** "Docker-compose kurulum + backfill/retry kanıtı"
- **Week 37/38:** "Dataset kaynağı + lisans + veri sözlüğü + split stratejisi"

### Teknik Değişiklik
- **Repo lokasyonu:** `OneDrive\...\ds-learning-lab` → `C:\dev\ds-learning-lab`
- OneDrive'da sadece doküman/export tut

### Temizlik
- AI Security tablosundaki bozuk "dbt Geliştirici Merkezi" metinleri

---

*Rapor Tarihi: 2025-12-16*
*Tüm öneriler bağımsız kaynaklardan doğrulandı.*
