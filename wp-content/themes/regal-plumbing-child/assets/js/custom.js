// Mobile sticky CTA bar — inject into DOM (guard against duplicate injection)
document.addEventListener('DOMContentLoaded', function () {
  if (document.querySelector('.mobile-sticky-cta')) return;
  var bar = document.createElement('div');
  bar.className = 'mobile-sticky-cta';
  bar.innerHTML = '<a href="tel:9096004561" aria-label="Call Regal Plumbing now: (909) 600-4561">Call Now: (909) 600-4561</a>';
  document.body.appendChild(bar);
});
