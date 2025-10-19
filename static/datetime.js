// Konfigurasi Hari Libur Nasional (bisa diedit manual untuk hari besar)
// Format: 'YYYY-MM-DD'
const hariLiburNasional = [
  // Contoh: Tambahkan tanggal hari libur nasional di sini
  // '2025-01-01', // Tahun Baru
  // '2025-12-25', // Natal
  // dst...
];

// Fungsi cek status operasional
function getStatusOperasional() {
  const now = new Date();
  const dayOfWeek = now.getDay(); // 0=Minggu, 1=Senin, ..., 6=Sabtu
  const currentHour = now.getHours();
  const currentMinute = now.getMinutes();
  const currentTime = currentHour * 60 + currentMinute; // Convert ke menit
  
  // Format tanggal untuk cek hari libur nasional
  const dateString = now.toISOString().split('T')[0]; // Format: YYYY-MM-DD
  
  // Cek apakah hari ini termasuk hari libur nasional
  if (hariLiburNasional.includes(dateString)) {
    return {
      status: 'TUTUP',
      keterangan: 'HARI LIBUR NASIONAL',
      className: 'status-closed'
    };
  }
  
  // Minggu = TUTUP
  if (dayOfWeek === 0) {
    return {
      status: 'TUTUP',
      keterangan: 'HARI MINGGU',
      className: 'status-closed'
    };
  }
  
  // Senin - Jumat: 08:00 - 14:00
  if (dayOfWeek >= 1 && dayOfWeek <= 5) {
    const bukaSeninJumat = 8 * 60; // 08:00 = 480 menit
    const tutupSeninJumat = 14 * 60; // 14:00 = 840 menit
    
    if (currentTime >= bukaSeninJumat && currentTime < tutupSeninJumat) {
      return {
        status: 'BUKA',
        keterangan: 'PELAYANAN BUKA',
        className: 'status-open'
      };
    } else {
      return {
        status: 'TUTUP',
        keterangan: 'DI LUAR JAM OPERASIONAL',
        className: 'status-closed'
      };
    }
  }
  
  // Sabtu: 08:00 - 12:00
  if (dayOfWeek === 6) {
    const bukaSabtu = 8 * 60; // 08:00 = 480 menit
    const tutupSabtu = 12 * 60; // 12:00 = 720 menit
    
    if (currentTime >= bukaSabtu && currentTime < tutupSabtu) {
      return {
        status: 'BUKA',
        keterangan: 'PELAYANAN BUKA',
        className: 'status-open'
      };
    } else {
      return {
        status: 'TUTUP',
        keterangan: 'DI LUAR JAM OPERASIONAL',
        className: 'status-closed'
      };
    }
  }
}

// Update jam dan tanggal real-time
function updateDateTime() {
  const now = new Date();
  
  // Array nama hari dan bulan dalam Bahasa Indonesia
  const days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
  const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
                  'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
  
  const dayName = days[now.getDay()];
  const date = now.getDate();
  const monthName = months[now.getMonth()];
  const year = now.getFullYear();
  
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  
  const dateDisplay = document.querySelector('.date-display');
  const timeDisplay = document.querySelector('.time-display');
  const statusDisplay = document.querySelector('.status-display');
  
  if (dateDisplay && timeDisplay) {
    dateDisplay.textContent = `${dayName}, ${date} ${monthName} ${year}`;
    timeDisplay.textContent = `${hours}:${minutes}:${seconds} WIB`;
  }
  
  // Update status operasional
  if (statusDisplay) {
    const statusInfo = getStatusOperasional();
    statusDisplay.textContent = statusInfo.keterangan;
    statusDisplay.className = 'status-display ' + statusInfo.className;
  }
}

// Update setiap detik
document.addEventListener('DOMContentLoaded', function() {
  updateDateTime();
  setInterval(updateDateTime, 1000);
});
