document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('btn-aduan-toggle');
  var panel = document.getElementById('panel-aduan');
  if (btn && panel) {
    btn.addEventListener('click', function() {
      panel.style.display = panel.style.display === 'none' ? 'block' : 'none';
    });
  }

  var links = document.querySelectorAll('.unit-segera');
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener('click', function(e) {
      e.preventDefault();
      var unit = this.getAttribute('data-unit');
      alert('Nomor WhatsApp unit ' + unit + ' belum tersedia. Silakan hubungi nomor darurat Satlantas: 0287-385514');
    });
  }
});
