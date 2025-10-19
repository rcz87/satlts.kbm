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
  
  if (dateDisplay && timeDisplay) {
    dateDisplay.textContent = `${dayName}, ${date} ${monthName} ${year}`;
    timeDisplay.textContent = `${hours}:${minutes}:${seconds} WIB`;
  }
}

// Update setiap detik
document.addEventListener('DOMContentLoaded', function() {
  updateDateTime();
  setInterval(updateDateTime, 1000);
});
