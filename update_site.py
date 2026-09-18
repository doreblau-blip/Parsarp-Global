import re

html_content = '''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-i18n="pageTitle">Parsarp Global — Temizlik & Kişisel Bakım İhracatı</title>
  <meta name="description" content="Parsarp Global — Türkiye'den Dubai'ye premium temizlik ve kişisel bakım ürünleri ihracatı.">
  <style>
/* ═══════════════════════════════════════════════
   PARSARP GLOBAL — Design System
   Swiss + Apple aesthetic · Premium · Warm
   ═══════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');

/* ── Tokens ── */
:root {
  --c-slate: #193A4E;
  --c-steel: #507B8F;
  --c-ice: #C3D4D7;
  --c-sand: #E4E2DE;
  --c-white: #FFFFFF;
  --c-bg: #FAFAF9;
  --c-bg-warm: #F6F4F1;
  --c-text: #193A4E;
  --c-text-soft: #507B8F;
  --c-border: rgba(195, 212, 215, 0.4);

  --ff-sans: 'Plus Jakarta Sans', -apple-system, sans-serif;
  --ff-mono: 'Space Mono', monospace;

  --radius: 20px;
  --radius-sm: 12px;
  --radius-xs: 8px;

  --shadow-sm: 0 1px 3px rgba(25, 58, 78, 0.04);
  --shadow-md: 0 4px 20px rgba(25, 58, 78, 0.06);
  --shadow-lg: 0 8px 40px rgba(25, 58, 78, 0.08);
  --shadow-card: 0 2px 16px rgba(25, 58, 78, 0.05);

  --ease: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html {
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: var(--ff-sans);
  color: var(--c-text);
  background: linear-gradient(180deg, var(--c-white) 0%, var(--c-bg) 30%, var(--c-bg-warm) 100%);
  min-height: 100vh;
  line-height: 1.6;
  overflow-x: hidden;
}

/* ── Typography ── */
h1, h2, h3, h4 { line-height: 1.15; letter-spacing: -0.02em; }
h1 { font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; }
h2 { font-size: clamp(2.0rem, 4vw, 3rem); font-weight: 800; }
h3 { font-size: 1.25rem; font-weight: 700; }
p  { font-size: 1.05rem; line-height: 1.7; color: var(--c-text-soft); }

.label {
  font-family: var(--ff-mono);
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--c-steel);
  font-weight: 700;
}

.light { font-weight: 300; color: var(--c-steel); }

/* ── Layout ── */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 clamp(1.5rem, 4vw, 3rem);
}

section {
  padding: clamp(4rem, 10vw, 8rem) 0;
}

/* ── Nav ── */
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 1.25rem 0;
  transition: all 0.4s var(--ease);
  background: rgba(255, 255, 255, 0);
  backdrop-filter: blur(0);
}

nav.scrolled {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px) saturate(1.2);
  border-bottom: 1px solid var(--c-border);
  padding: 0.75rem 0;
}

nav .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.logo-main {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--c-slate);
  letter-spacing: -0.02em;
  line-height: 1;
}

.logo-sub {
  font-size: 0.7rem;
  font-weight: 300;
  color: var(--c-steel);
  letter-spacing: 0.2em;
  line-height: 1;
  margin-top: 2px;
}

.nav-right-group {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2.5rem;
  list-style: none;
}

.nav-links a {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--c-steel);
  text-decoration: none;
  transition: color 0.3s var(--ease);
  position: relative;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 1.5px;
  background: var(--c-slate);
  transition: width 0.3s var(--ease);
}

.nav-links a:hover { color: var(--c-slate); }
.nav-links a:hover::after { width: 100%; }

.nav-cta {
  padding: 0.55rem 1.5rem;
  background: var(--c-slate);
  color: var(--c-white) !important;
  border-radius: var(--radius-sm);
  font-weight: 600 !important;
  font-size: 0.82rem !important;
  transition: all 0.3s var(--ease) !important;
  box-shadow: var(--shadow-sm);
}

.nav-cta::after { display: none !important; }
.nav-cta:hover {
  background: var(--c-steel) !important;
  transform: translateY(-1px);
  box-shadow: var(--shadow-md) !important;
}

/* ── Language Switcher (Apple/Swiss Style) ── */
.lang-switch {
  display: inline-flex;
  align-items: center;
  background: rgba(25, 58, 78, 0.05);
  border: 1px solid rgba(195, 212, 215, 0.5);
  border-radius: 20px;
  padding: 3px;
  gap: 2px;
  backdrop-filter: blur(8px);
  transition: border-color 0.3s var(--ease), background 0.3s var(--ease);
}

.lang-switch:hover {
  border-color: rgba(80, 123, 143, 0.6);
  background: rgba(25, 58, 78, 0.08);
}

.lang-btn {
  padding: 4px 10px;
  border-radius: 14px;
  font-family: var(--ff-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--c-steel);
  background: transparent;
  border: none;
  cursor: pointer;
  transition: all 0.25s var(--ease);
  line-height: 1;
}

.lang-btn:hover:not(.active) {
  color: var(--c-slate);
}

.lang-btn.active {
  background: var(--c-slate);
  color: var(--c-white);
  box-shadow: 0 2px 6px rgba(25, 58, 78, 0.18);
}

/* ── Hero ── */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding-top: 6rem;
  position: relative;
}

.hero .container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1rem;
  background: rgba(195, 212, 215, 0.25);
  border: 1px solid var(--c-border);
  border-radius: 100px;
  margin-bottom: 1.5rem;
  backdrop-filter: blur(10px);
}

.hero-badge .dot {
  width: 7px;
  height: 7px;
  background: #22C55E;
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(34, 197, 94, 0.5);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(0.85); }
}

.hero h1 {
  margin-bottom: 1.5rem;
  color: var(--c-slate);
}

.hero h1 .accent {
  background: linear-gradient(135deg, var(--c-slate) 0%, var(--c-steel) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero p {
  font-size: 1.15rem;
  margin-bottom: 2.5rem;
  max-width: 480px;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.9rem 2rem;
  border-radius: var(--radius-sm);
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.3s var(--ease);
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: var(--c-slate);
  color: var(--c-white);
  box-shadow: var(--shadow-md);
}

.btn-primary:hover {
  background: #122B3B;
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.btn-secondary {
  background: transparent;
  color: var(--c-slate);
  border: 1.5px solid var(--c-ice);
}

.btn-secondary:hover {
  border-color: var(--c-steel);
  background: rgba(25, 58, 78, 0.03);
  transform: translateY(-2px);
}

/* ── Hero Visual Card ── */
.hero-visual {
  position: relative;
  display: flex;
  justify-content: center;
}

.hero-card {
  width: 380px;
  height: 480px;
  background: var(--c-slate);
  border-radius: var(--radius);
  padding: 2.5rem;
  color: var(--c-white);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: var(--shadow-lg);
  position: relative;
  overflow: hidden;
}

.hero-card::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(195, 212, 215, 0.12) 0%, transparent 60%);
  pointer-events: none;
}

.hero-card .card-logo {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.hero-card .card-logo span {
  display: block;
  font-size: 0.7rem;
  font-weight: 300;
  letter-spacing: 0.2em;
  color: var(--c-ice);
}

.hero-card .card-tagline {
  font-size: 1.35rem;
  font-weight: 300;
  line-height: 1.4;
  color: var(--c-ice);
}

.hero-card .card-batch {
  font-family: var(--ff-mono);
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  color: rgba(195, 212, 215, 0.6);
}

.hero-card-shadow {
  position: absolute;
  width: 340px;
  height: 440px;
  background: var(--c-ice);
  border-radius: var(--radius);
  top: 20px;
  right: 20px;
  z-index: -1;
  opacity: 0.3;
  filter: blur(20px);
}

/* ── Showcase (Text Left, Image Right) ── */
.showcase {
  background: var(--c-white);
  border-top: 1px solid var(--c-border);
  border-bottom: 1px solid var(--c-border);
}

.showcase .container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: center;
}

.showcase-image {
  position: relative;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  aspect-ratio: 4 / 3;
}

.showcase-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.8s var(--ease);
}

.showcase-image:hover img {
  transform: scale(1.03);
}

.showcase-text h2 {
  color: var(--c-slate);
  margin: 0.75rem 0 1.5rem;
}

.showcase-text p {
  margin-bottom: 1.25rem;
}

/* ── About ── */
.about .container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

.about-text h2 {
  margin-top: 0.75rem;
  margin-bottom: 1.5rem;
  color: var(--c-slate);
}

.about-features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.feature-card {
  background: var(--c-white);
  padding: 1.75rem;
  border-radius: var(--radius);
  border: 1px solid var(--c-border);
  transition: all 0.3s var(--ease);
  box-shadow: var(--shadow-card);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--c-steel);
}

.feature-icon {
  width: 44px;
  height: 44px;
  background: rgba(195, 212, 215, 0.25);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  color: var(--c-slate);
}

.feature-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.5rem;
  color: var(--c-slate);
}

.feature-card p {
  font-size: 0.88rem;
  line-height: 1.5;
}

/* ── Products ── */
.products {
  background: var(--c-white);
  border-top: 1px solid var(--c-border);
  border-bottom: 1px solid var(--c-border);
}

.section-header {
  text-align: center;
  max-width: 600px;
  margin: 0 auto 4rem;
}

.section-header h2 {
  margin-top: 0.75rem;
  margin-bottom: 0.75rem;
  color: var(--c-slate);
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.product-card {
  background: var(--c-bg);
  padding: 2rem 1.5rem;
  border-radius: var(--radius);
  border: 1px solid var(--c-border);
  text-align: center;
  transition: all 0.3s var(--ease);
  position: relative;
  overflow: hidden;
}

.product-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--c-slate);
  opacity: 0;
  transition: opacity 0.3s var(--ease);
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  background: var(--c-white);
  border-color: transparent;
}

.product-card:hover::before { opacity: 1; }

.product-icon {
  width: 56px;
  height: 56px;
  background: var(--c-white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.25rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--c-border);
}

.product-icon svg {
  width: 26px;
  height: 26px;
  stroke: var(--c-slate);
  stroke-width: 1.8;
  fill: none;
}

.product-icon svg.filled {
  stroke: none;
  fill: var(--c-slate);
}

.product-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.4rem;
  color: var(--c-slate);
}

.product-card p {
  font-size: 0.85rem;
}

/* ── Stats Bar ── */
.stats {
  background: var(--c-slate);
  color: var(--c-white);
  padding: 4rem 0;
}

.stats .container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  text-align: center;
}

.stat-item h3 {
  font-size: clamp(2.2rem, 4vw, 3.2rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--c-white);
  margin-bottom: 0.25rem;
}

.stat-item p {
  color: var(--c-ice);
  font-size: 0.9rem;
  font-family: var(--ff-mono);
  letter-spacing: 0.05em;
}

/* ── Route & Logistics ── */
.route .container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.route-visual {
  background: var(--c-white);
  padding: 3rem 2.5rem;
  border-radius: var(--radius);
  border: 1px solid var(--c-border);
  box-shadow: var(--shadow-card);
}

.route-line {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  margin-bottom: 2.5rem;
}

.route-point {
  text-align: center;
  z-index: 2;
}

.route-point .city {
  font-weight: 800;
  font-size: 1.3rem;
  color: var(--c-slate);
}

.route-point .country {
  font-size: 0.75rem;
  font-family: var(--ff-mono);
  color: var(--c-steel);
  letter-spacing: 0.1em;
}

.route-connector {
  flex: 1;
  height: 2px;
  background: repeating-linear-gradient(90deg, var(--c-steel) 0 6px, transparent 6px 12px);
  margin: 0 1.5rem;
  position: relative;
}

.route-connector::after {
  content: '✈';
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1rem;
  color: var(--c-slate);
}

.route-methods {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.route-method {
  padding: 0.5rem 1rem;
  background: var(--c-bg);
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--c-slate);
}

.route-specs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
  margin-top: 2rem;
}

.spec-row {
  background: var(--c-white);
  padding: 1rem 1.25rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--c-border);
}

.spec-label {
  display: block;
  font-size: 0.72rem;
  font-family: var(--ff-mono);
  color: var(--c-steel);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.spec-value {
  font-weight: 700;
  font-size: 1rem;
  color: var(--c-slate);
}

/* ── CTA ── */
.cta {
  background: linear-gradient(180deg, var(--c-white) 0%, var(--c-bg-warm) 100%);
  border-top: 1px solid var(--c-border);
  text-align: center;
}

.cta .container {
  max-width: 700px;
}

.cta p {
  margin: 1rem 0 2.5rem;
  font-size: 1.15rem;
}

.cta-actions {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

/* ── Footer ── */
footer {
  background: var(--c-slate);
  color: var(--c-ice);
  padding: 4rem 0 2rem;
  border-top: 1px solid rgba(195, 212, 215, 0.1);
}

footer .container {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 4rem;
}

.footer-brand .logo-main { color: var(--c-white); }
.footer-brand .logo-sub { color: var(--c-ice); }

.footer-brand p {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: rgba(195, 212, 215, 0.7);
  max-width: 320px;
}

.footer-links h4 {
  color: var(--c-white);
  font-size: 0.9rem;
  font-family: var(--ff-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}

.footer-links ul {
  list-style: none;
}

.footer-links li {
  margin-bottom: 0.6rem;
}

.footer-links a {
  color: rgba(195, 212, 215, 0.7);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s var(--ease);
}

.footer-links a:hover {
  color: var(--c-white);
}

/* ── Animations ── */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s var(--ease), transform 0.8s var(--ease);
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
.reveal-delay-4 { transition-delay: 0.4s; }
.reveal-delay-5 { transition-delay: 0.5s; }
.reveal-delay-6 { transition-delay: 0.6s; }
.reveal-delay-7 { transition-delay: 0.7s; }
.reveal-delay-8 { transition-delay: 0.8s; }

/* ── Responsive ── */
@media (max-width: 1024px) {
  .hero .container { grid-template-columns: 1fr; text-align: center; }
  .hero-content { max-width: 100%; }
  .hero p { margin: 0 auto 2.5rem; }
  .hero-actions { justify-content: center; }
  .hero-visual { margin-top: 3rem; }
  .showcase .container { grid-template-columns: 1fr; }
  .about .container { grid-template-columns: 1fr; }
  .about-features { grid-template-columns: 1fr 1fr; }
  .product-grid { grid-template-columns: repeat(2, 1fr); }
  .stats .container { grid-template-columns: repeat(2, 1fr); }
  .route .container { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .nav-links { display: none; }
  .about-features { grid-template-columns: 1fr; }
  .product-grid { grid-template-columns: 1fr; }
  .stats .container { grid-template-columns: 1fr; }
  .footer .container { flex-direction: column; gap: 2rem; grid-template-columns: 1fr; }
  .hero-card { width: 300px; height: 380px; }
  .cta-actions { flex-direction: column; align-items: center; }
}

</style>
</head>
<body>

  <!-- ═══ NAV ═══ -->
  <nav id="navbar">
    <div class="container">
      <div class="logo">
        <span class="logo-main">PARSARP</span>
        <span class="logo-sub">GLOBAL</span>
      </div>
      <div class="nav-right-group">
        <ul class="nav-links">
          <li><a href="#about" data-i18n="nav.about">Hakkımızda</a></li>
          <li><a href="#products" data-i18n="nav.products">Ürünler</a></li>
          <li><a href="#route" data-i18n="nav.logistics">Lojistik</a></li>
          <li><a href="#contact" class="nav-cta" data-i18n="nav.contact">İletişim</a></li>
        </ul>
        <div class="lang-switch" id="langToggle">
          <button class="lang-btn active" data-lang="tr">TR</button>
          <button class="lang-btn" data-lang="en">EN</button>
        </div>
      </div>
    </div>
  </nav>

  <!-- ═══ HERO ═══ -->
  <section class="hero" id="hero">
    <div class="container">
      <div class="hero-content">
        <div class="hero-badge reveal">
          <span class="dot"></span>
          <span class="label" style="margin:0; font-size: 0.65rem;" data-i18n="hero.badge">İstanbul → Dubai</span>
        </div>

        <h1 class="reveal reveal-delay-1" data-i18n="hero.headline">Güzelliğin <span class="accent">Güvenilir Adresi.</span></h1>
        <p class="reveal reveal-delay-2" data-i18n="hero.text">
          Dubai merkezli temizlik ve bakım odaklı, seçkin markaları bir araya getiriyoruz. Cilt, saç ve vücut bakımında yüksek kalite standartlarına uygun, güvenilir ve etkili ürünler sunuyoruz.
        </p>

        <div class="hero-actions reveal reveal-delay-3">
          <a href="#contact" class="btn btn-primary" data-i18n="hero.ctaPrimary">Teklif Alın →</a>
          <a href="#products" class="btn btn-secondary" data-i18n="hero.ctaSecondary">Ürünleri İnceleyin</a>
        </div>
      </div>
      <div class="hero-visual reveal reveal-delay-4">
        <div class="hero-card-shadow"></div>
        <div class="hero-card">
          <div>
            <div class="card-logo">
              PARSARP
              <span>GLOBAL</span>
            </div>
          </div>
          <div>
            <div class="card-tagline" data-i18n="hero.cardTagline">
              Premium temizlik ve kişisel bakım ürünleri. İhtiyaçlarınıza uygun, özenle hazırlanmış bir alışveriş deneyimi.
            </div>
          </div>
          <div>
            <div class="card-batch">PARSARPGLOBAL.COM — DUBAI, UAE</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ SHOWCASE — Premium Güzellik (Text Left, Image Right) ═══ -->
  <section class="showcase" id="showcase">
    <div class="container">
      <div class="showcase-text">
        <span class="label reveal" data-i18n="showcase.label">Parsarp Global</span>
        <h2 class="reveal reveal-delay-1" data-i18n="showcase.headline">Premium Güzellik <br><span class="light">ve Bakım.</span></h2>
        <p class="reveal reveal-delay-2" data-i18n="showcase.p1">
          Dubai'de temizlik ve bakım konusunda uzmanlığımızla seçilmiş güzellik ürünleri sunuyoruz. Cilt, saç ve kişisel bakım rutininizi destekleyen kaliteli ve güvenilir markaları tek bir çatı altında topluyoruz.
        </p>
        <p class="reveal reveal-delay-3" data-i18n="showcase.p2">
          İhtiyaçlarınıza uygun ürünleri kolayca bulabilmeniz için özenle hazırlanmış bir alışveriş deneyimi sağlıyoruz.
        </p>
      </div>
      <div class="showcase-image reveal reveal-delay-2">
        <img src="bubbles.jpg" alt="Premium güzellik ve bakım ürünleri">
      </div>
    </div>
  </section>

  <!-- ═══ ABOUT ═══ -->
  <section class="about" id="about">
    <div class="container">
      <div class="about-text">
        <span class="label about-label reveal" data-i18n="about.label">Hakkımızda</span>
        <h2 class="reveal reveal-delay-1" data-i18n="about.headline">İki Kıtayı <br><span class="light">Birleştiren Temizlik.</span></h2>
        <p class="reveal reveal-delay-2" data-i18n="about.p1">
          Parsarp Global, Türkiye'nin üretim gücünü Dubai'nin dinamik pazarıyla buluşturur. Temizlik ve kişisel bakım ürünlerimiz, ev ile profesyonel kullanım için formüle edilmiştir.
        </p>
        <p class="reveal reveal-delay-3" data-i18n="about.p2">
          Her ürünümüz uluslararası kalite standartlarında üretilir ve güvenilir lojistik ağımızla zamanında teslim edilir.
        </p>
      </div>
      <div class="about-features">
        <div class="feature-card reveal reveal-delay-1">
          <div class="feature-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h3 data-i18n="about.f1Title">Kalite Güvencesi</h3>
          <p data-i18n="about.f1Desc">Tüm ürünler uluslararası standartlarda üretilir ve test edilir.</p>
        </div>
        <div class="feature-card reveal reveal-delay-2">
          <div class="feature-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
          </div>
          <h3 data-i18n="about.f2Title">Global Standart</h3>
          <p data-i18n="about.f2Desc">İstanbul'dan Dubai'ye, her noktada aynı kalite ve güvenilirlik.</p>
        </div>
        <div class="feature-card reveal reveal-delay-3">
          <div class="feature-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></svg>
          </div>
          <h3 data-i18n="about.f3Title">Hızlı Teslimat</h3>
          <p data-i18n="about.f3Desc">Deniz, hava ve kara yoluyla 7–12 iş gününde güvenli teslimat.</p>
        </div>
        <div class="feature-card reveal reveal-delay-4">
          <div class="feature-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>
          </div>
          <h3 data-i18n="about.f4Title">Doğal Formüller</h3>
          <p data-i18n="about.f4Desc">Çevre dostu, sürdürülebilir ve güvenli içeriklerle üretim.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ PRODUCTS ═══ -->
  <section class="products" id="products">
    <div class="container">
      <div class="section-header">
        <span class="label reveal" data-i18n="products.label">Ürün Yelpazesi</span>
        <h2 class="reveal reveal-delay-1" data-i18n="products.headline">Temizlik & <span class="light">Kişisel Bakım</span></h2>
        <p class="reveal reveal-delay-2" data-i18n="products.subtitle">Ev ve profesyonel kullanım için geniş ürün gamı.</p>
      </div>
      <div class="product-grid">

        <!-- 1. Spray Bottle -->
        <div class="product-card reveal reveal-delay-1">
          <div class="product-icon">
            <svg class="filled" viewBox="0 0 256 256"><path d="M200,84a12,12,0,0,0,12-12,60.07,60.07,0,0,0-60-60H80A20,20,0,0,0,60,32V80a20,20,0,0,1-20,20,12,12,0,0,0,0,24A44.06,44.06,0,0,0,83.82,84H108v20.62a19.92,19.92,0,0,1-7.51,15.62L84.51,133A43.8,43.8,0,0,0,68,167.38V224a20,20,0,0,0,20,20H192a20,20,0,0,0,20-20V211.47A274.77,274.77,0,0,0,180.68,84ZM84,36h68a36,36,0,0,1,33.94,24H84ZM188,211.47V220H92V167.38a19.92,19.92,0,0,1,7.51-15.62l16-12.78A43.8,43.8,0,0,0,132,104.62V84h21.24A250.93,250.93,0,0,1,188,211.47Z"/></svg>
          </div>
          <h3 data-i18n="products.p1Title">Sprey Temizleyici</h3>
          <p data-i18n="products.p1Desc">Çok amaçlı yüzey temizleme</p>
        </div>

        <!-- 2. Hand Soap -->
        <div class="product-card reveal reveal-delay-2">
          <div class="product-icon">
            <svg class="filled" viewBox="0 0 256 256"><path d="M188,97.68V92a36,36,0,0,0-36-36H140V36h28a4,4,0,0,1,4,4,12,12,0,0,0,24,0,28,28,0,0,0-28-28H104a12,12,0,0,0,0,24h12V56H104A36,36,0,0,0,68,92v5.68A44.06,44.06,0,0,0,36,140v76a20,20,0,0,0,20,20H200a20,20,0,0,0,20-20V140A44.06,44.06,0,0,0,188,97.68ZM104,80h48a12,12,0,0,1,12,12v4H92V92A12,12,0,0,1,104,80Zm92,132H60V140a20,20,0,0,1,20-20h96a20,20,0,0,1,20,20Z"/></svg>
          </div>
          <h3 data-i18n="products.p2Title">Sıvı Sabun</h3>
          <p data-i18n="products.p2Desc">Nazik formül, etkili temizlik</p>
        </div>

        <!-- 3. Shampoo -->
        <div class="product-card reveal reveal-delay-3">
          <div class="product-icon">
            <svg viewBox="0 0 24 24"><path d="m12 9-8.414 8.414A2 2 0 0 0 3 18.828v1.344a2 2 0 0 1-.586 1.414A2 2 0 0 1 3.828 21h1.344a2 2 0 0 0 1.414-.586L15 12"/><path d="m18 9 .4.4a1 1 0 1 1-3 3l-3.8-3.8a1 1 0 1 1 3-3l.4.4 3.4-3.4a1 1 0 1 1 3 3z"/><path d="m2 22 .414-.414"/></svg>
          </div>
          <h3 data-i18n="products.p3Title">Saç Serumu</h3>
          <p data-i18n="products.p3Desc">Besleyici bakım formülü</p>
        </div>

        <!-- 4. Baby Shampoo -->
        <div class="product-card reveal reveal-delay-4">
          <div class="product-icon">
            <svg viewBox="0 0 24 24"><path d="M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M15 12h.01"/><path d="M19.38 6.813A9 9 0 0 1 20.8 10.2a2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1"/><path d="M9 12h.01"/></svg>
          </div>
          <h3 data-i18n="products.p4Title">Bebek Şampuanı</h3>
          <p data-i18n="products.p4Desc">Göz yakmayan hassas formül</p>
        </div>

        <!-- 5. Hair Mask -->
        <div class="product-card reveal reveal-delay-5">
          <div class="product-icon">
            <svg viewBox="0 0 24 24"><path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"/><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"/></svg>
          </div>
          <h3 data-i18n="products.p5Title">Saç Maskesi</h3>
          <p data-i18n="products.p5Desc">Yoğun nemlendirme ve onarım</p>
        </div>

        <!-- 6. Cleaning Wipes -->
        <div class="product-card reveal reveal-delay-6">
          <div class="product-icon">
            <svg viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/></svg>
          </div>
          <h3 data-i18n="products.p6Title">Islak Mendil</h3>
          <p data-i18n="products.p6Desc">Hijyenik temizlik ve tazelik</p>
        </div>

        <!-- 7. Face Mask -->
        <div class="product-card reveal reveal-delay-7">
          <div class="product-icon">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
          </div>
          <h3 data-i18n="products.p7Title">Yüz Maskesi</h3>
          <p data-i18n="products.p7Desc">Cilt bakımı ve yenilenme</p>
        </div>

        <!-- 8. Shower Gel -->
        <div class="product-card reveal reveal-delay-8">
          <div class="product-icon">
            <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3 data-i18n="products.p8Title">Duş Jeli</h3>
          <p data-i18n="products.p8Desc">Ferahlatıcı vücut temizliği</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ═══ STATS ═══ -->
  <div class="stats" id="stats">
    <div class="container">
      <div class="stat-item reveal">
        <h3>4,200</h3>
        <p data-i18n="stats.s1">Kilometre Güzergah</p>
      </div>
      <div class="stat-item reveal reveal-delay-1">
        <h3>150+</h3>
        <p data-i18n="stats.s2">Ürün Çeşidi</p>
      </div>
      <div class="stat-item reveal reveal-delay-2">
        <h3>24s</h3>
        <p data-i18n="stats.s3">Yanıt Süresi</p>
      </div>
      <div class="stat-item reveal reveal-delay-3">
        <h3>%98</h3>
        <p data-i18n="stats.s4">Memnuniyet</p>
      </div>
    </div>
  </div>

  <!-- ═══ ROUTE ═══ -->
  <section class="route" id="route">
    <div class="container">
      <div class="route-visual reveal">
        <div class="route-line">
          <div class="route-point">
            <div class="city">İstanbul</div>
            <div class="country">Türkiye</div>
          </div>
          <div class="route-connector"></div>
          <div class="route-point">
            <div class="city">Dubai</div>
            <div class="country">BAE</div>
          </div>
        </div>
        <div class="route-methods">
          <span class="route-method" data-i18n="route.methodSea">🚢 Deniz</span>
          <span class="route-method" data-i18n="route.methodAir">✈️ Hava</span>
          <span class="route-method" data-i18n="route.methodLand">🚛 Kara</span>
        </div>
      </div>
      <div>
        <span class="label reveal" data-i18n="route.label">Lojistik</span>
        <h2 class="reveal reveal-delay-1" style="margin-top:0.75rem" data-i18n="route.headline">Güvenilir <br><span class="light">Tedarik Zinciri.</span></h2>
        <p class="reveal reveal-delay-2" data-i18n="route.desc">
          İstanbul'dan Dubai'ye — deniz, hava ve kara yoluyla kesintisiz lojistik. Her gönderimde takip ve güvenlik.
        </p>
        <div class="route-specs reveal reveal-delay-3">
          <div class="spec-row">
            <span class="spec-label" data-i18n="route.spec1Label">Teslimat Süresi</span>
            <span class="spec-value" data-i18n="route.spec1Value">7–12 İş Günü</span>
          </div>
          <div class="spec-row">
            <span class="spec-label" data-i18n="route.spec2Label">Teslim Şekli</span>
            <span class="spec-value" data-i18n="route.spec2Value">CIF Dubai</span>
          </div>
          <div class="spec-row">
            <span class="spec-label" data-i18n="route.spec3Label">Üretim</span>
            <span class="spec-value" data-i18n="route.spec3Value">Made in Turkey</span>
          </div>
          <div class="spec-row">
            <span class="spec-label" data-i18n="route.spec4Label">Sertifika</span>
            <span class="spec-value" data-i18n="route.spec4Value">ISO 9001</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══ CTA ═══ -->
  <section class="cta" id="contact">
    <div class="container">
      <span class="label reveal" data-i18n="cta.label">İletişim</span>
      <h2 class="reveal reveal-delay-1" style="margin-top:0.75rem" data-i18n="cta.headline">Birlikte <span class="light">Büyüyelim.</span></h2>
      <p class="reveal reveal-delay-2" data-i18n="cta.desc">
        Ürün kataloğumuzu inceleyin, özel fiyat teklifi alın. Parsarp ailesine hoş geldiniz.
      </p>
      <div class="cta-actions reveal reveal-delay-3">
        <a href="mailto:info@parsarpglobal.com" class="btn btn-primary" data-i18n="cta.btnPrimary">Teklif İsteyin →</a>
        <a href="#" class="btn btn-secondary" data-i18n="cta.btnSecondary">Katalog İndirin</a>
      </div>
    </div>
  </section>

  <!-- ═══ FOOTER ═══ -->
  <footer>
    <div class="container">
      <div class="footer-brand">
        <div class="logo">
          <span class="logo-main">PARSARP</span>
          <span class="logo-sub">GLOBAL</span>
        </div>
        <p data-i18n="footer.brandDesc">Türkiye'den Dubai'ye premium temizlik ve kişisel bakım ürünleri ihracatı.</p>
      </div>
      <div class="footer-links">
        <h4 data-i18n="footer.col1Title">Şirket</h4>
        <ul>
          <li><a href="#about" data-i18n="nav.about">Hakkımızda</a></li>
          <li><a href="#products" data-i18n="nav.products">Ürünler</a></li>
          <li><a href="#route" data-i18n="nav.logistics">Lojistik</a></li>
          <li><a href="#contact" data-i18n="nav.contact">İletişim</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4 data-i18n="footer.col2Title">İletişim</h4>
        <ul>
          <li><a href="#" data-i18n="footer.locationTR">İstanbul, Türkiye</a></li>
          <li><a href="#" data-i18n="footer.locationUAE">Dubai, BAE</a></li>
          <li><a href="mailto:info@parsarpglobal.com">info@parsarpglobal.com</a></li>
        </ul>
      </div>
    </div>
    <div style="border-top:1px solid rgba(195,212,215,0.4); margin-top:2rem; padding-top:1.5rem; text-align:center;">
      <p style="font-size:0.75rem; color:#C3D4D7;" data-i18n="footer.copyright">© 2026 PARSARP GLOBAL® — Tüm hakları saklıdır.</p>
    </div>
  </footer>

  <!-- ═══ JAVASCRIPT & I18N ═══ -->
  <script>
    // ── Translations Object ──
    const translations = {
      tr: {
        pageTitle: "Parsarp Global — Temizlik & Kişisel Bakım İhracatı",
        nav: {
          about: "Hakkımızda",
          products: "Ürünler",
          logistics: "Lojistik",
          contact: "İletişim"
        },
        hero: {
          badge: "İstanbul → Dubai",
          headline: 'Güzelliğin <span class="accent">Güvenilir Adresi.</span>',
          text: "Dubai merkezli temizlik ve bakım odaklı, seçkin markaları bir araya getiriyoruz. Cilt, saç ve vücut bakımında yüksek kalite standartlarına uygun, güvenilir ve etkili ürünler sunuyoruz.",
          ctaPrimary: "Teklif Alın →",
          ctaSecondary: "Ürünleri İnceleyin",
          cardTagline: "Premium temizlik ve kişisel bakım ürünleri. İhtiyaçlarınıza uygun, özenle hazırlanmış bir alışveriş deneyimi."
        },
        showcase: {
          label: "Parsarp Global",
          headline: 'Premium Güzellik <br><span class="light">ve Bakım.</span>',
          p1: "Dubai'de temizlik ve bakım konusunda uzmanlığımızla seçilmiş güzellik ürünleri sunuyoruz. Cilt, saç ve kişisel bakım rutininizi destekleyen kaliteli ve güvenilir markaları tek bir çatı altında topluyoruz.",
          p2: "İhtiyaçlarınıza uygun ürünleri kolayca bulabilmeniz için özenle hazırlanmış bir alışveriş deneyimi sağlıyoruz."
        },
        about: {
          label: "Hakkımızda",
          headline: 'İki Kıtayı <br><span class="light">Birleştiren Temizlik.</span>',
          p1: "Parsarp Global, Türkiye'nin üretim gücünü Dubai'nin dinamik pazarıyla buluşturur. Temizlik ve kişisel bakım ürünlerimiz, ev ile profesyonel kullanım için formüle edilmiştir.",
          p2: "Her ürünümüz uluslararası kalite standartlarında üretilir ve güvenilir lojistik ağımızla zamanında teslim edilir.",
          f1Title: "Kalite Güvencesi",
          f1Desc: "Tüm ürünler uluslararası standartlarda üretilir ve test edilir.",
          f2Title: "Global Standart",
          f2Desc: "İstanbul'dan Dubai'ye, her noktada aynı kalite ve güvenilirlik.",
          f3Title: "Hızlı Teslimat",
          f3Desc: "Deniz, hava ve kara yoluyla 7–12 iş gününde güvenli teslimat.",
          f4Title: "Doğal Formüller",
          f4Desc: "Çevre dostu, sürdürülebilir ve güvenli içeriklerle üretim."
        },
        products: {
          label: "Ürün Yelpazesi",
          headline: 'Temizlik & <span class="light">Kişisel Bakım</span>',
          subtitle: "Ev ve profesyonel kullanım için geniş ürün gamı.",
          p1Title: "Sprey Temizleyici", p1Desc: "Çok amaçlı yüzey temizleme",
          p2Title: "Sıvı Sabun", p2Desc: "Nazik formül, etkili temizlik",
          p3Title: "Saç Serumu", p3Desc: "Besleyici bakım formülü",
          p4Title: "Bebek Şampuanı", p4Desc: "Göz yakmayan hassas formül",
          p5Title: "Saç Maskesi", p5Desc: "Yoğun nemlendirme ve onarım",
          p6Title: "Islak Mendil", p6Desc: "Hijyenik temizlik ve tazelik",
          p7Title: "Yüz Maskesi", p7Desc: "Cilt bakımı ve yenilenme",
          p8Title: "Duş Jeli", p8Desc: "Ferahlatıcı vücut temizliği"
        },
        stats: {
          s1: "Kilometre Güzergah",
          s2: "Ürün Çeşidi",
          s3: "Yanıt Süresi",
          s4: "Memnuniyet"
        },
        route: {
          label: "Lojistik",
          headline: 'Güvenilir <br><span class="light">Tedarik Zinciri.</span>',
          desc: "İstanbul'dan Dubai'ye — deniz, hava ve kara yoluyla kesintisiz lojistik. Her gönderimde takip ve güvenlik.",
          methodSea: "🚢 Deniz",
          methodAir: "✈️ Hava",
          methodLand: "🚛 Kara",
          spec1Label: "Teslimat Süresi", spec1Value: "7–12 İş Günü",
          spec2Label: "Teslim Şekli", spec2Value: "CIF Dubai",
          spec3Label: "Üretim", spec3Value: "Made in Turkey",
          spec4Label: "Sertifika", spec4Value: "ISO 9001"
        },
        cta: {
          label: "İletişim",
          headline: 'Birlikte <span class="light">Büyüyelim.</span>',
          desc: "Ürün kataloğumuzu inceleyin, özel fiyat teklifi alın. Parsarp ailesine hoş geldiniz.",
          btnPrimary: "Teklif İsteyin →",
          btnSecondary: "Katalog İndirin"
        },
        footer: {
          brandDesc: "Türkiye'den Dubai'ye premium temizlik ve kişisel bakım ürünleri ihracatı.",
          col1Title: "Şirket",
          col2Title: "İletişim",
          locationTR: "İstanbul, Türkiye",
          locationUAE: "Dubai, BAE",
          copyright: "© 2026 PARSARP GLOBAL® — Tüm hakları saklıdır."
        }
      },
      en: {
        pageTitle: "Parsarp Global — Cleaning & Personal Care Export",
        nav: {
          about: "About Us",
          products: "Products",
          logistics: "Logistics",
          contact: "Contact"
        },
        hero: {
          badge: "Istanbul → Dubai",
          headline: 'The Trusted Name <span class="accent">in Beauty.</span>',
          text: "Based in Dubai, we bring together select cleaning and personal care brands. We offer reliable and effective products for skin, hair, and body care that meet high quality standards.",
          ctaPrimary: "Get Quote →",
          ctaSecondary: "Explore Products",
          cardTagline: "Premium cleaning & personal care products. A curated shopping experience tailored to your needs."
        },
        showcase: {
          label: "Parsarp Global",
          headline: 'Premium Beauty <br><span class="light">& Care.</span>',
          p1: "In Dubai, we offer curated beauty products backed by our expertise in hygiene and care. We gather high-quality, reliable brands under one roof to support your skin, hair, and personal care routine.",
          p2: "We provide a thoughtfully designed shopping experience so you can easily find products that fit your needs."
        },
        about: {
          label: "About Us",
          headline: 'Hygiene Bridging <br><span class="light">Two Continents.</span>',
          p1: "Parsarp Global connects Turkey's manufacturing power with Dubai's dynamic market. Our cleaning and personal care products are formulated for home and professional use.",
          p2: "Every product is manufactured to international quality standards and delivered on time through our reliable logistics network.",
          f1Title: "Quality Assurance",
          f1Desc: "All products are manufactured and tested to international standards.",
          f2Title: "Global Standard",
          f2Desc: "From Istanbul to Dubai, consistent quality and reliability at every point.",
          f3Title: "Fast Delivery",
          f3Desc: "Safe delivery in 7–12 business days via sea, air, and land.",
          f4Title: "Natural Formulas",
          f4Desc: "Formulated with eco-friendly, sustainable, and safe ingredients."
        },
        products: {
          label: "Product Range",
          headline: 'Cleaning & <span class="light">Personal Care</span>',
          subtitle: "Wide product lineup for residential and professional use.",
          p1Title: "Spray Cleaner", p1Desc: "Multi-purpose surface cleaning",
          p2Title: "Liquid Soap", p2Desc: "Gentle formula, effective cleansing",
          p3Title: "Hair Serum", p3Desc: "Nourishing care formula",
          p4Title: "Baby Shampoo", p4Desc: "Tear-free gentle formula",
          p5Title: "Hair Mask", p5Desc: "Intense hydration & repair",
          p6Title: "Wet Wipes", p6Desc: "Hygienic cleaning & freshness",
          p7Title: "Face Mask", p7Desc: "Skincare & rejuvenation",
          p8Title: "Shower Gel", p8Desc: "Refreshing body wash"
        },
        stats: {
          s1: "Kilometers Route",
          s2: "Product Varieties",
          s3: "Response Time",
          s4: "Satisfaction"
        },
        route: {
          label: "Logistics",
          headline: 'Reliable <br><span class="light">Supply Chain.</span>',
          desc: "From Istanbul to Dubai — seamless logistics via sea, air, and land. Tracking and security with every shipment.",
          methodSea: "🚢 Sea",
          methodAir: "✈️ Air",
          methodLand: "🚛 Land",
          spec1Label: "Delivery Time", spec1Value: "7–12 Business Days",
          spec2Label: "Delivery Term", spec2Value: "CIF Dubai",
          spec3Label: "Origin", spec3Value: "Made in Turkey",
          spec4Label: "Certification", spec4Value: "ISO 9001"
        },
        cta: {
          label: "Contact",
          headline: 'Let\'s Grow <span class="light">Together.</span>',
          desc: "Explore our product catalog, get a custom quote. Welcome to the Parsarp family.",
          btnPrimary: "Request Quote →",
          btnSecondary: "Download Catalog"
        },
        footer: {
          brandDesc: "Exporting premium cleaning and personal care products from Turkey to Dubai.",
          col1Title: "Company",
          col2Title: "Contact",
          locationTR: "Istanbul, Turkey",
          locationUAE: "Dubai, UAE",
          copyright: "© 2026 PARSARP GLOBAL® — All rights reserved."
        }
      }
    };

    function getNestedValue(obj, path) {
      return path.split('.').reduce((prev, curr) => prev && prev[curr], obj);
    }

    function setLanguage(lang) {
      document.documentElement.lang = lang;
      
      // Update data-i18n elements
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const val = getNestedValue(translations[lang], key);
        if (val !== undefined) {
          if (el.tagName.toLowerCase() === 'title') {
            document.title = val;
          } else {
            el.innerHTML = val;
          }
        }
      });

      // Update switcher active state
      document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
      });

      try { localStorage.setItem('parsarp_lang', lang); } catch(e){}
    }

    // Language toggle click event
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        setLanguage(lang);
      });
    });

    // ── Nav scroll ──
    const nav = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    });

    // ── Reveal on scroll ──
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    reveals.forEach(el => observer.observe(el));

    // ── Smooth scroll ──
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', e => {
        e.preventDefault();
        const t = document.querySelector(a.getAttribute('href'));
        if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });

    // Load saved language if available
    const savedLang = (function() {
      try { return localStorage.getItem('parsarp_lang'); } catch(e) { return null; }
    })();
    if (savedLang === 'en') {
      setLanguage('en');
    }
  </script>

</body>
</html>
'''

with open('/Users/nisaalkan/.gemini/antigravity/scratch/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML successfully updated with text left, image right.")
