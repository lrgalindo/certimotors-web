# CERTIMOTORS — Logo & Design System · Context para Claude Code

## Logo seleccionado: Variante C (Tipográfico)

### Anatomía del logo
```
CERTI  |  MOTORS
       ^
   separador dorado vertical (1.5px)

Tagline debajo: "Inspección certificada · Guatemala"
```

### Tokens de marca (fuente única de verdad)
```
Navy   #1c1e54  → wordmark sobre fondo claro, headers, dark surfaces
Gold   #C8973A  → separador, tagline, CTAs, acento único de la marca
White  #ffffff  → wordmark sobre fondo navy
CERTI en navy oscuro: rgba(255,255,255,0.68) sobre fondo navy
```

### Tipografía del logo
```
Fuente:   DM Sans (Google Fonts)
Import:   https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,700&display=swap

CERTI    → font-weight: 400, color: #1c1e54 (light) / rgba(255,255,255,0.68) (dark)
MOTORS   → font-weight: 700, color: #1c1e54 (light) / #ffffff (dark)
tracking → letter-spacing: -0.01em en ambas palabras
Tagline  → font-weight: 400, font-size: ~29% del logo, letter-spacing: 0.18em, uppercase
```

### Fórmulas de escala (relativas al font-size base `s`)
```
Separador alto:    s × 0.85
Separador margen:  s × 0.33 (a cada lado)
Gap wordmark↔tagline: s × 0.33
Tagline size:      max(7px, s × 0.29)
```

### Componente React — Logo.jsx
```jsx
/**
 * Props:
 *   variant  "light" | "dark"   (default: "light")
 *   size     number px          (default: 24)
 *   tagline  boolean            (default: true)
 */
export function LogoCertimotors({ variant = 'light', size = 24, tagline = true, className = '', style = {} }) {
  const isDark      = variant === 'dark';
  const certiColor  = isDark ? 'rgba(255,255,255,0.68)' : '#1c1e54';
  const motorsColor = isDark ? '#ffffff' : '#1c1e54';
  const sepH        = Math.round(size * 0.85);
  const sepM        = Math.round(size * 0.33);
  const tagSize     = Math.max(7, Math.round(size * 0.29));

  return (
    <div className={className} style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'flex-start', gap: Math.round(size * 0.33), ...style }}>
      <div style={{ display: 'flex', alignItems: 'center', lineHeight: 1 }}>
        <span style={{ fontFamily: "'DM Sans', sans-serif", fontSize: size, fontWeight: 400, color: certiColor, letterSpacing: '-0.01em', lineHeight: 1 }}>CERTI</span>
        <div aria-hidden="true" style={{ width: 1.5, height: sepH, background: '#C8973A', margin: `0 ${sepM}px`, flexShrink: 0, alignSelf: 'center' }} />
        <span style={{ fontFamily: "'DM Sans', sans-serif", fontSize: size, fontWeight: 700, color: motorsColor, letterSpacing: '-0.01em', lineHeight: 1 }}>MOTORS</span>
      </div>
      {tagline && (
        <span style={{ fontFamily: "'DM Sans', sans-serif", fontSize: tagSize, fontWeight: 400, color: '#C8973A', letterSpacing: '0.18em', textTransform: 'uppercase', lineHeight: 1, whiteSpace: 'nowrap' }}>
          Inspección certificada · Guatemala
        </span>
      )}
    </div>
  );
}
```

### Uso del componente
```jsx
// Header web (fondo blanco)
<LogoCertimotors size={24} />

// Hero / slide (fondo navy #1c1e54)
<LogoCertimotors variant="dark" size={32} />

// Solo wordmark sin tagline
<LogoCertimotors size={20} tagline={false} />

// Tamaño grande para landing hero
<LogoCertimotors size={48} />
```

### SVG standalone (para contextos sin React: emails, PDFs, Telegram)
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 52" width="260" height="52" role="img" aria-label="CERTIMOTORS">
  <defs>
    <style>
      .certi   { font-family: 'DM Sans', sans-serif; font-size: 32px; font-weight: 400; fill: #1c1e54; letter-spacing: -0.01em; }
      .motors  { font-family: 'DM Sans', sans-serif; font-size: 32px; font-weight: 700; fill: #1c1e54; letter-spacing: -0.01em; }
      .tagline { font-family: 'DM Sans', sans-serif; font-size: 9px;  font-weight: 400; fill: #C8973A; letter-spacing: 0.18em; }
    </style>
  </defs>
  <text class="certi"  x="0"   y="33">CERTI</text>
  <rect x="94" y="6" width="1.5" height="27" fill="#C8973A"/>
  <text class="motors" x="106" y="33">MOTORS</text>
  <text class="tagline" x="0"   y="48">INSPECCIÓN CERTIFICADA · GUATEMALA</text>
</svg>
```

### Reglas de uso (DO / DON'T)
```
✅ DO
  - Logo sobre #ffffff (fondo claro)   → variant="light"
  - Logo sobre #1c1e54 (fondo navy)    → variant="dark"
  - Un solo logo visible por pantalla (header o hero, no ambos)
  - Mantener proportions — escalar solo con la prop `size`
  - Usar .cm-btn-primary (gold pill) para CTAs en la misma página

❌ DON'T
  - No colocar el logo sobre fondos de color fuera de blanco o navy
  - No separar CERTI y MOTORS — son una sola unidad tipográfica
  - No cambiar el color del separador (#C8973A es el único dorado de marca)
  - No usar font-weight > 400 en CERTI ni < 700 en MOTORS
  - No añadir sombras, gradientes ni efectos al logo
  - No escalar CERTI y MOTORS a tamaños diferentes entre sí
```

### Design tokens CSS (importar en globals.css o index.css)
```css
:root {
  --cm-navy:          #1c1e54;
  --cm-gold:          #C8973A;
  --cm-gold-deep:     #a37828;
  --cm-gold-press:    #7a5a1e;
  --cm-gold-bg:       #f5e9d4;
  --cm-ink:           #0d253d;
  --cm-ink-secondary: #273951;
  --cm-ink-mute:      #64748d;
  --cm-canvas:        #ffffff;
  --cm-canvas-soft:   #f6f9fc;
  --cm-hairline:      #e3e8ee;
  --cm-font:          'DM Sans', 'Inter', system-ui, sans-serif;
  --cm-radius-pill:   9999px;
  --cm-radius-lg:     12px;
  --cm-radius-md:     8px;
  --cm-shadow-card:   rgba(0,55,112,0.08) 0 1px 3px;
  --cm-shadow-float:  rgba(0,55,112,0.08) 0 8px 24px, rgba(0,55,112,0.04) 0 2px 6px;
}
```

### Archivos entregados
- `Logo.jsx`    → Componente React con todas las props
- `tokens.css`  → Variables CSS + clases de utilidad (btn, card, badge, price)
- `logo.svg`    → SVG standalone para emails, Telegram, pdfkit
