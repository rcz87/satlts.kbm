document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ikm-survey-form');
    if (!form) return;
    
    const starRatings = document.querySelectorAll('.star-rating');
    const formMessage = document.getElementById('form-message');
    
    starRatings.forEach(ratingContainer => {
        const stars = ratingContainer.querySelectorAll('.star');
        const ratingName = ratingContainer.getAttribute('data-name');
        
        stars.forEach(star => {
            star.addEventListener('click', function() {
                const value = parseInt(this.getAttribute('data-value'));
                ratingContainer.setAttribute('data-rating', value);
                
                stars.forEach((s, index) => {
                    if (index < value) {
                        s.classList.add('active');
                    } else {
                        s.classList.remove('active');
                    }
                });
            });
            
            star.addEventListener('mouseenter', function() {
                const value = parseInt(this.getAttribute('data-value'));
                stars.forEach((s, index) => {
                    if (index < value) {
                        s.classList.add('hover');
                    } else {
                        s.classList.remove('hover');
                    }
                });
            });
        });
        
        ratingContainer.addEventListener('mouseleave', function() {
            stars.forEach(s => s.classList.remove('hover'));
        });
    });
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const jenis_layanan = form.querySelector('select[name="jenis_layanan"]').value;
        if (!jenis_layanan) {
            showMessage('Mohon pilih jenis layanan terlebih dahulu', 'error');
            return;
        }
        
        const ratings = {};
        let allRated = true;
        
        starRatings.forEach(ratingContainer => {
            const name = ratingContainer.getAttribute('data-name');
            const rating = parseInt(ratingContainer.getAttribute('data-rating'));
            if (rating === 0) {
                allRated = false;
            }
            ratings[name] = rating;
        });
        
        if (!allRated) {
            showMessage('Mohon berikan penilaian untuk semua aspek', 'error');
            return;
        }
        
        const komentar = form.querySelector('textarea[name="komentar"]').value;
        
        const submitButton = form.querySelector('button[type="submit"]');
        submitButton.disabled = true;
        submitButton.textContent = 'Mengirim...';
        
        try {
            const response = await fetch('/ikm/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    ...ratings,
                    komentar: komentar,
                    jenis_layanan: jenis_layanan
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showMessage(data.message, 'success');
                form.reset();
                starRatings.forEach(ratingContainer => {
                    ratingContainer.setAttribute('data-rating', '0');
                    ratingContainer.querySelectorAll('.star').forEach(s => s.classList.remove('active'));
                });
                
                setTimeout(() => {
                    window.location.href = '/ikm/hasil';
                }, 2000);
            } else {
                showMessage(data.message, 'error');
            }
        } catch (error) {
            showMessage('Terjadi kesalahan saat mengirim data. Silakan coba lagi.', 'error');
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = '✅ Kirim Penilaian';
        }
    });
    
    function showMessage(message, type) {
        formMessage.textContent = message;
        formMessage.className = 'form-message ' + (type === 'success' ? 'success' : 'error');
        formMessage.style.display = 'block';
        
        setTimeout(() => {
            formMessage.style.display = 'none';
        }, 5000);
    }
});
