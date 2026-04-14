document.addEventListener('submit', function (e) {
  var form = e.target;
  if (form.tagName !== 'FORM') return;
  var msg = form.getAttribute('data-confirm');
  if (msg && !window.confirm(msg)) {
    e.preventDefault();
  }
});
