// Consentimiento de cookies y eventos de clic para las páginas de servicio y guías.
// La lógica de analítica vive en /assets/js/analytics.js (misma que el home).
(() => {
  'use strict';
  const banner = document.getElementById('cookie-banner');
  const accept = document.getElementById('cookie-accept');
  const reject = document.getElementById('cookie-reject');
  const settings = document.getElementById('cookie-settings');
  const analytics = window.CMAnalytics;
  if (!analytics || !banner) return;

  if (!analytics.consent()) banner.hidden = false;
  accept.addEventListener('click', () => { analytics.accept(); banner.hidden = true; });
  reject.addEventListener('click', () => { analytics.reject(); banner.hidden = true; });
  settings.addEventListener('click', () => { banner.hidden = false; accept.focus({ preventScroll: true }); });

  document.addEventListener('click', event => {
    const trigger = event.target.closest('[data-analytics-event]');
    if (!trigger) return;
    analytics.track(trigger.dataset.analyticsEvent, {
      ubicacion: trigger.dataset.analyticsLocation || 'pagina'
    });
  });
})();
