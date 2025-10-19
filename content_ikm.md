# 📊 Indeks Kepuasan Masyarakat (IKM)

## Survei Kepuasan Pelayanan SAMSAT Kebumen

Indeks Kepuasan Masyarakat (IKM) adalah data dan informasi tentang tingkat kepuasan masyarakat yang diperoleh dari hasil pengukuran secara kuantitatif dan kualitatif atas pendapat masyarakat dalam memperoleh pelayanan dari SAMSAT Kebumen.

---

<div class="ikm-intro">
  <h2>✍️ Berikan Penilaian Anda</h2>
  <p>Bantu kami meningkatkan kualitas pelayanan dengan mengisi survei kepuasan di bawah ini. Penilaian Anda sangat berharga bagi kami!</p>
</div>

<div id="ikm-form-container">
  <form id="ikm-survey-form" class="ikm-form">
    <div class="form-group">
      <label class="form-label">Jenis Layanan yang Anda Gunakan:</label>
      <select name="jenis_layanan" required class="form-select">
        <option value="">-- Pilih Layanan --</option>
        <option value="Pembayaran Pajak Tahunan">Pembayaran Pajak Tahunan</option>
        <option value="Pembayaran Pajak 5 Tahunan">Pembayaran Pajak 5 Tahunan (Ganti STNK)</option>
        <option value="Duplikat STNK">Duplikat STNK</option>
        <option value="Mutasi Masuk">Mutasi Masuk (Pindah ke Kebumen)</option>
        <option value="Mutasi Keluar">Mutasi Keluar (Pindah dari Kebumen)</option>
        <option value="BBN 1 (Kendaraan Baru)">BBN 1 (Kendaraan Baru)</option>
        <option value="BBN 2 (Balik Nama)">BBN 2 (Balik Nama)</option>
        <option value="Lainnya">Lainnya</option>
      </select>
    </div>

    <div class="rating-container">
      <h3 class="rating-title">Berikan Penilaian untuk 9 Aspek Pelayanan</h3>
      <p class="rating-subtitle">Klik bintang untuk memberikan nilai (1 = Tidak Baik, 4 = Sangat Baik)</p>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">1.</span>
          <div>
            <strong>Persyaratan</strong>
            <p class="rating-desc">Kemudahan dan kejelasan persyaratan pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="persyaratan">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">2.</span>
          <div>
            <strong>Prosedur</strong>
            <p class="rating-desc">Kemudahan dan kejelasan prosedur pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="prosedur">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">3.</span>
          <div>
            <strong>Waktu Pelayanan</strong>
            <p class="rating-desc">Kecepatan waktu dalam memberikan pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="waktu_pelayanan">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">4.</span>
          <div>
            <strong>Biaya/Tarif</strong>
            <p class="rating-desc">Kewajaran dan kejelasan biaya/tarif pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="biaya_tarif">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">5.</span>
          <div>
            <strong>Produk Layanan</strong>
            <p class="rating-desc">Kualitas hasil pelayanan yang diberikan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="produk_layanan">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">6.</span>
          <div>
            <strong>Kompetensi Petugas</strong>
            <p class="rating-desc">Kemampuan dan keahlian petugas dalam memberikan pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="kompetensi_petugas">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">7.</span>
          <div>
            <strong>Perilaku Petugas</strong>
            <p class="rating-desc">Kesopanan dan keramahan petugas dalam memberikan pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="perilaku_petugas">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">8.</span>
          <div>
            <strong>Sarana/Prasarana</strong>
            <p class="rating-desc">Kualitas sarana dan prasarana pelayanan</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="maklumat_pelayanan">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>

      <div class="rating-item">
        <div class="rating-label">
          <span class="rating-number">9.</span>
          <div>
            <strong>Penanganan Pengaduan</strong>
            <p class="rating-desc">Kemudahan dan kecepatan penanganan pengaduan masyarakat</p>
          </div>
        </div>
        <div class="star-rating" data-rating="0" data-name="penanganan_pengaduan">
          <span class="star" data-value="1">★</span>
          <span class="star" data-value="2">★</span>
          <span class="star" data-value="3">★</span>
          <span class="star" data-value="4">★</span>
        </div>
      </div>
    </div>

    <div class="form-group">
      <label class="form-label">💬 Saran & Komentar (Opsional):</label>
      <textarea name="komentar" rows="4" placeholder="Tuliskan saran, kritik, atau komentar Anda untuk peningkatan pelayanan..." class="form-textarea"></textarea>
    </div>

    <div class="form-actions">
      <button type="submit" class="btn-submit">✅ Kirim Penilaian</button>
    </div>

    <div id="form-message" class="form-message"></div>
  </form>
</div>

---

## 📊 Lihat Hasil Survei

<div class="ikm-results-link">
  <p>Ingin melihat hasil survei kepuasan masyarakat?</p>
  <a href="/ikm/hasil" class="btn-view-results">📈 Lihat Hasil IKM</a>
</div>

---

## 🎯 Tentang IKM

IKM bertujuan untuk:

1. **Mengetahui Tingkat Kinerja** unit pelayanan secara berkala sebagai bahan untuk menetapkan kebijakan dalam rangka peningkatan kualitas pelayanan publik selanjutnya
2. **Mengukur Kepuasan** masyarakat terhadap kualitas pelayanan yang diberikan
3. **Meningkatkan Kualitas** pelayanan publik berdasarkan feedback dari masyarakat
4. **Transparansi dan Akuntabilitas** dalam penyelenggaraan pelayanan publik

---

<div style="background: #f0f9ff; padding: 20px; border-left: 4px solid #3b82f6; border-radius: 8px; margin: 20px 0;">
  <p style="margin: 0; color: #1e40af; font-size: 1em;">
    <strong>ℹ️ Informasi:</strong> Kepuasan Anda adalah prioritas kami. Masukan Anda sangat berharga untuk meningkatkan kualitas pelayanan SAMSAT Kebumen. Data survei bersifat anonim dan hanya digunakan untuk peningkatan layanan.
  </p>
</div>
