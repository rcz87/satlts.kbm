document.addEventListener('DOMContentLoaded', function() {
  const btnFeedback = document.getElementById('btn-feedback');
  const modal = document.getElementById('feedback-modal');
  const btnClose = document.getElementById('close-modal');
  const form = document.getElementById('feedback-form');
  const formMessage = document.getElementById('feedback-message');
  
  if (!btnFeedback || !modal) return;
  
  // Open modal
  btnFeedback.addEventListener('click', function() {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden'; // Prevent scrolling
  });
  
  // Close modal
  btnClose.addEventListener('click', function() {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  });
  
  // Close modal when clicking outside
  modal.addEventListener('click', function(e) {
    if (e.target === modal) {
      modal.style.display = 'none';
      document.body.style.overflow = 'auto';
    }
  });
  
  // Handle form submission
  form.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const nama = form.querySelector('[name="nama"]').value.trim();
    const email = form.querySelector('[name="email"]').value.trim();
    const kategori = form.querySelector('[name="kategori"]').value;
    const pesan = form.querySelector('[name="pesan"]').value.trim();
    
    // Validasi
    if (!kategori) {
      showMessage('Mohon pilih kategori feedback', 'error');
      return;
    }
    
    if (!pesan || pesan.length < 10) {
      showMessage('Pesan minimal 10 karakter', 'error');
      return;
    }
    
    const submitButton = form.querySelector('button[type="submit"]');
    submitButton.disabled = true;
    submitButton.textContent = 'Mengirim...';
    
    // Get CSRF token
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    
    try {
      const response = await fetch('/feedback/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
          nama: nama || 'Anonim',
          email: email,
          kategori: kategori,
          pesan: pesan
        })
      });
      
      const data = await response.json();
      
      if (data.success) {
        showMessage(data.message, 'success');
        form.reset();
        
        setTimeout(() => {
          modal.style.display = 'none';
          document.body.style.overflow = 'auto';
        }, 2000);
      } else {
        showMessage(data.message, 'error');
      }
    } catch (error) {
      showMessage('Terjadi kesalahan saat mengirim feedback. Silakan coba lagi.', 'error');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = '📤 Kirim Feedback';
    }
  });
  
  function showMessage(message, type) {
    formMessage.textContent = message;
    formMessage.className = 'feedback-form-message ' + (type === 'success' ? 'success' : 'error');
    formMessage.style.display = 'block';
    
    setTimeout(() => {
      formMessage.style.display = 'none';
    }, 5000);
  }
});
