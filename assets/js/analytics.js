(() => {
  const CONSENT_KEY = 'cm_consent_v1';
  const IS_PRODUCTION = ['certimotors.com', 'www.certimotors.com'].includes(location.hostname);
  let enabled = false;
  let loaded = false;

  const readConsent = () => {
    try { return localStorage.getItem(CONSENT_KEY); } catch (_) { return null; }
  };
  const writeConsent = value => {
    try { localStorage.setItem(CONSENT_KEY, value); } catch (_) { /* storage can be unavailable */ }
  };
  const loadScript = src => {
    const script = document.createElement('script');
    script.async = true;
    script.src = src;
    document.head.appendChild(script);
  };
  const enable = () => {
    if (enabled) return;
    enabled = true;
    if (!IS_PRODUCTION) return;
    if (loaded) {
      if (window.gtag) window.gtag('consent', 'update', { analytics_storage: 'granted', ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted' });
      if (window.fbq) window.fbq('consent', 'grant');
      if (window.ttq) window.ttq.grantConsent();
      return;
    }
    loaded = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', 'G-17RQ4B76BR');
    window.gtag('config', 'G-53TM6JHBXW');
    loadScript('https://www.googletagmanager.com/gtag/js?id=G-17RQ4B76BR');

    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', '26679746048367896');
    window.fbq('track', 'PageView');

    !function (w, d, t) {
      w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];
      ttq.methods=['page','track','identify','instances','debug','on','off','once','ready','alias','group','enableCookie','disableCookie','holdConsent','revokeConsent','grantConsent'];
      ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};
      for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);
      ttq.instance=function(e){var n=ttq._i[e]||[];for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(n,ttq.methods[i]);return n};
      ttq.load=function(e,n){var r='https://analytics.tiktok.com/i18n/pixel/events.js';ttq._i=ttq._i||{};ttq._i[e]=[];ttq._i[e]._u=r;ttq._t=ttq._t||{};ttq._t[e]=+new Date;ttq._o=ttq._o||{};ttq._o[e]=n||{};n=d.createElement('script');n.async=true;n.src=r+'?sdkid='+e+'&lib='+t;d.head.appendChild(n)};
      ttq.load('D9GISS3C77U6Q0JCP34G');
      ttq.page();
    }(window, document, 'ttq');
  };

  window.CMAnalytics = {
    consent: readConsent,
    accept() { writeConsent('accepted'); enable(); },
    reject() {
      writeConsent('rejected');
      enabled = false;
      if (!IS_PRODUCTION || !loaded) return;
      if (window.gtag) window.gtag('consent', 'update', { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
      if (window.fbq) window.fbq('consent', 'revoke');
      if (window.ttq) window.ttq.revokeConsent();
    },
    enable,
    track(name, params = {}) {
      if (!enabled || !IS_PRODUCTION) return;
      if (window.gtag) window.gtag('event', name, params);
      if (window.fbq) window.fbq('trackCustom', name, params);
      if (window.ttq) window.ttq.track(name, params);
    },
    purchase(params) {
      if (!enabled || !IS_PRODUCTION) return;
      if (window.gtag) window.gtag('event', 'purchase', params);
      if (window.fbq) window.fbq('track', 'Purchase', params);
      if (window.ttq) window.ttq.track('Purchase', params);
    }
  };
  if (readConsent() === 'accepted') enable();
})();
