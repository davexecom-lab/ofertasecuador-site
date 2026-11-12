"""Genera el sitio estático de Ofertas Ecuador. Uso: python3 build.py"""
from pathlib import Path

WA = "https://wa.me/593983582688"
def wa(msg): return WA + "?text=" + msg.replace(" ", "%20")

# Iconos SVG de línea (sin emojis)
I = {
 "truck": '<path d="M3 6h11v9H3z"/><path d="M14 9h4l3 3v3h-7z"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
 "cash": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M6 10v4M18 10v4"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "pan": '<circle cx="10" cy="13" r="6"/><path d="M16 13h6"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
 "plug": '<path d="M9 3v5M15 3v5"/><path d="M6 8h12v4a6 6 0 01-12 0z"/><path d="M12 18v3"/>',
 "paw": '<circle cx="7" cy="9" r="2"/><circle cx="12" cy="6" r="2"/><circle cx="17" cy="9" r="2"/><path d="M8 16c0-3 2-5 4-5s4 2 4 5-2 3-4 3-4 0-4-3z"/>',
 "car": '<path d="M4 15l2-6h12l2 6"/><rect x="3" y="15" width="18" height="4" rx="1"/><circle cx="7.5" cy="19" r="1.5"/><circle cx="16.5" cy="19" r="1.5"/>',
 "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
 "pin": '<path d="M12 21s7-6.5 7-12a7 7 0 00-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "wa": '<path d="M4 20l1.3-4A8 8 0 1112 20a8 8 0 01-3.8-1z"/><path d="M9 9c0 3 3 6 6 6l1-1.5-2-1-1 .8c-1-.5-2-1.5-2.4-2.4l.8-1-1-2z"/>',
}
def ico(n, s=28): return f'<svg class="ico" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'

CATS = [("home","Hogar","Organización, limpieza y decoración"),("pan","Cocina","Utensilios prácticos para el día a día"),
        ("spark","Cuidado personal","Belleza y bienestar"),("plug","Tecnología","Accesorios y gadgets útiles"),
        ("paw","Mascotas","Cuidado y accesorios"),("car","Auto","Accesorios para tu carro")]

def head(title, desc, verify=False):
    meta = '<meta name="facebook-domain-verification" content="g6vfticiif0der3hz5231vrbm8hq7d" />\n' if verify else ""
    return f'''<!DOCTYPE html>
<html lang="es-EC">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{meta}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<div class="ticker" aria-label="Beneficios"><div class="ticker-track">{"".join(f"<span>{t}</span>" for t in ["Envío gratis a todo Ecuador","Pagas al recibir tu pedido","Garantía de 30 días","Atención por WhatsApp"]*4)}</div></div>
<header class="header">
  <div class="wrap header-in">
    <a class="hdr-wa" href="{WA}" target="_blank" rel="noopener">{ico("wa",22)}<span>+593 98 358 2688</span></a>
    <a href="/" class="logo" aria-label="Ofertas Ecuador, inicio"><img src="/logo.png" alt="Ofertas Ecuador" width="76" height="76"></a>
    <a class="btn btn-wa sm" href="{wa("Hola, quiero hacer un pedido")}" target="_blank" rel="noopener">Comprar</a>
  </div>
  <nav class="catnav"><div class="wrap">{"".join(f'<a href="/#categorias">{c[1]}</a>' for c in CATS)}<a href="/envios.html">Envíos</a><a href="/contacto.html">Contacto</a></div></nav>
</header>
'''

FOOT = f'''<section class="trustbar">
  <div class="wrap trust-grid">
    <div>{ico("truck",34)}<b>Envío gratis</b><small>A todo Ecuador</small></div>
    <div>{ico("cash",34)}<b>Pago contra entrega</b><small>Pagas al recibir</small></div>
    <div>{ico("shield",34)}<b>Garantía de 30 días</b><small>Por defectos de fábrica</small></div>
    <div>{ico("chat",34)}<b>Atención por WhatsApp</b><small>Lunes a sábado</small></div>
  </div>
</section>
<footer class="footer">
  <div class="wrap foot-in">
    <div>
      <img src="/logo.png" alt="Ofertas Ecuador" width="88" height="88" class="foot-logo">
      <p>Tienda online con envío gratis a todo Ecuador y pago contra entrega.</p>
    </div>
    <div>
      <h4>Información</h4>
      <a href="/envios.html">Envíos y entregas</a>
      <a href="/devoluciones.html">Cambios, devoluciones y garantía</a>
      <a href="/terminos.html">Términos y condiciones</a>
      <a href="/privacidad.html">Política de privacidad</a>
    </div>
    <div>
      <h4>Contacto</h4>
      <a href="{WA}" target="_blank" rel="noopener">WhatsApp: +593 98 358 2688</a>
      <span>Lunes a viernes 8:00 a 20:00</span>
      <span>Sábados 9:00 a 14:00</span>
      <span>Ecuador</span>
    </div>
  </div>
  <p class="copy">© 2026 Ofertas Ecuador. Todos los derechos reservados.</p>
</footer>
<a class="float-wa" href="{wa("Hola, tengo una consulta")}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{ico("wa",30)}</a>
</body>
</html>
'''

INDEX = head("Ofertas Ecuador | Envío gratis y pago contra entrega",
             "Ofertas Ecuador: productos para el hogar, cocina, cuidado personal, tecnología, mascotas y auto con envío gratis a todo Ecuador y pago contra entrega.", verify=True) + f'''
<main>
<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-copy">
      <p class="eyebrow">Tienda online en Ecuador</p>
      <h1>Productos útiles para tu casa, <span>con envío gratis</span> y pago al recibir</h1>
      <p class="lead">Escríbenos por WhatsApp, te asesoramos y te enviamos tu pedido a cualquier ciudad del país. No necesitas tarjeta: pagas en efectivo cuando lo recibes.</p>
      <div class="cta">
        <a class="btn btn-main" href="#categorias">Ver catálogo</a>
        <a class="btn btn-wa" href="{wa("Hola, quiero hacer un pedido")}" target="_blank" rel="noopener">{ico("wa",20)} Pedir por WhatsApp</a>
      </div>
    </div>
    <div class="hero-card">
      <img src="/logo.png" alt="Ofertas Ecuador" width="300" height="300">
      <ul>
        <li>{ico("truck",22)} Entrega en 2 a 4 días hábiles</li>
        <li>{ico("cash",22)} Pagas en efectivo al recibir</li>
        <li>{ico("shield",22)} 30 días de garantía</li>
      </ul>
    </div>
  </div>
</section>

<section id="categorias" class="section">
  <div class="wrap">
    <h2 class="center">Categorías</h2>
    <p class="sub center">Elige una categoría y te mostramos por WhatsApp los productos disponibles esta semana.</p>
    <div class="cats">
      {"".join(f'<a class="cat c{i}" href="{wa("Hola, quiero ver productos de " + n.lower())}" target="_blank" rel="noopener"><div class="cat-ic">{ico(k,44)}</div><b>{n}</b><small>{d}</small><span class="cat-go">Ver productos</span></a>' for i,(k,n,d) in enumerate(CATS))}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <h2 class="center">Así de fácil compras</h2>
    <ol class="steps">
      <li><span class="num">1</span><b>Escríbenos</b><p>Envíanos un mensaje al +593 98 358 2688 con el producto que te interesa.</p></li>
      <li><span class="num">2</span><b>Confirma tus datos</b><p>Nombre, ciudad, dirección y un punto de referencia. Te enviamos el resumen para confirmar.</p></li>
      <li><span class="num">3</span><b>Despachamos</b><p>Enviamos con Servientrega, Laar Courier o Gintracom y te compartimos tu número de guía.</p></li>
      <li><span class="num">4</span><b>Pagas al recibir</b><p>Recibes en 2 a 4 días hábiles y pagas en efectivo al transportista.</p></li>
    </ol>
  </div>
</section>

<section id="preguntas" class="section">
  <div class="wrap narrow">
    <h2 class="center">Preguntas frecuentes</h2>
    <details><summary>¿Cuánto cuesta el envío?</summary><p>El envío es gratis a todas las ciudades de Ecuador con cobertura de nuestras transportadoras.</p></details>
    <details><summary>¿Cuánto tarda en llegar?</summary><p>Entre 2 y 4 días hábiles desde que confirmas tu pedido. Las entregas son de lunes a viernes de 9:00 a 18:00 y sábados de 9:00 a 14:00.</p></details>
    <details><summary>¿Cómo pago?</summary><p>En efectivo al recibir tu pedido. No necesitas tarjeta ni pagar por adelantado.</p></details>
    <details><summary>¿Qué pasa si mi producto llega con un defecto?</summary><p>Tienes 30 días de garantía por defectos de fábrica. Escríbenos con una foto o video y lo solucionamos. Revisa la <a href="/devoluciones.html">política de cambios y devoluciones</a>.</p></details>
    <details><summary>¿Puedo cambiar mi dirección después de pedir?</summary><p>Sí, mientras el pedido no haya sido despachado. Escríbenos por WhatsApp y la actualizamos.</p></details>
  </div>
</section>
</main>
''' + FOOT

PAGES = {
"envios.html": ("Envíos y entregas", """
<p>En Ofertas Ecuador enviamos a todas las ciudades del país que tengan cobertura de nuestras transportadoras aliadas.</p>
<h2>Costo de envío</h2><p>El envío es gratis. El precio que te confirmamos por WhatsApp es el valor total que pagas al recibir.</p>
<h2>Tiempos de entrega</h2><p>Entregamos en 2 a 4 días hábiles desde que confirmas tu pedido. En zonas alejadas el tiempo puede ser mayor; te avisamos antes de despachar.</p>
<h2>Horarios</h2><p>Las transportadoras entregan de lunes a viernes de 9:00 a 18:00 y sábados de 9:00 a 14:00. No hay entregas los domingos ni feriados.</p>
<h2>Transportadoras</h2><p>Trabajamos con Servientrega, Laar Courier y Gintracom. Al despachar te enviamos el número de guía por WhatsApp para que sigas tu pedido.</p>
<h2>Pago contra entrega</h2><p>Pagas en efectivo al transportista cuando recibes el paquete. Ten el valor exacto listo para agilizar la entrega.</p>
<h2>Si no estás en casa</h2><p>Si la transportadora no te encuentra, te contactaremos por WhatsApp para coordinar una nueva fecha o el retiro en la oficina más cercana.</p>
"""),
"devoluciones.html": ("Cambios, devoluciones y garantía", """
<h2>Garantía</h2><p>Todos nuestros productos tienen 30 días de garantía por defectos de fábrica, contados desde la fecha de entrega.</p>
<h2>Cómo solicitarla</h2><ol><li>Escríbenos por WhatsApp al +593 98 358 2688 con tu nombre y número de guía.</li><li>Envíanos una foto o video que muestre el defecto.</li><li>Revisamos tu caso en un máximo de 2 días hábiles y te indicamos si procede el cambio del producto o la devolución del dinero.</li></ol>
<h2>Producto equivocado o incompleto</h2><p>Si recibiste un producto diferente al que pediste o te falta una parte, avísanos dentro de las 48 horas siguientes a la entrega y te enviamos lo correcto sin costo.</p>
<h2>Qué no cubre la garantía</h2><ul><li>Daños por mal uso, golpes, caídas o contacto con líquidos no indicados.</li><li>Desgaste normal por el uso.</li><li>Productos modificados o reparados por terceros.</li></ul>
<h2>Devoluciones de dinero</h2><p>Cuando corresponde una devolución, te reembolsamos el valor pagado por transferencia bancaria a la cuenta que nos indiques, dentro de los 10 días hábiles posteriores a recibir el producto de vuelta.</p>
<h2>Derecho de devolución</h2><p>Conforme a la Ley Orgánica de Defensa del Consumidor del Ecuador, puedes devolver un producto comprado a distancia dentro de los 3 días hábiles siguientes a la entrega, siempre que esté sin uso y en su empaque original.</p>
"""),
"terminos.html": ("Términos y condiciones", """
<p>Al comprar en Ofertas Ecuador aceptas estos términos. Si tienes dudas, escríbenos antes de confirmar tu pedido.</p>
<h2>Pedidos</h2><p>Los pedidos se realizan por WhatsApp. El pedido queda confirmado cuando aceptas el resumen con el producto, el precio total y tus datos de entrega.</p>
<h2>Precios</h2><p>Los precios están en dólares de los Estados Unidos (USD) e incluyen el envío. El precio válido es el que te confirmamos por WhatsApp al momento del pedido.</p>
<h2>Disponibilidad</h2><p>Los productos están sujetos a disponibilidad. Si un producto se agota después de tu pedido, te avisamos y puedes elegir otro o cancelar sin costo.</p>
<h2>Pago</h2><p>El pago es contra entrega, en efectivo, al recibir el pedido.</p>
<h2>Cancelaciones</h2><p>Puedes cancelar tu pedido sin costo antes de que sea despachado escribiéndonos por WhatsApp.</p>
<h2>Datos de entrega</h2><p>Eres responsable de darnos una dirección completa y un número de contacto correcto. Si la entrega falla por datos incorrectos, coordinaremos contigo un nuevo intento.</p>
<h2>Garantía</h2><p>Aplican las condiciones de nuestra <a href="/devoluciones.html">política de cambios, devoluciones y garantía</a>.</p>
<h2>Legislación</h2><p>Estos términos se rigen por las leyes de la República del Ecuador, incluida la Ley Orgánica de Defensa del Consumidor.</p>
"""),
"privacidad.html": ("Política de privacidad", """
<p>En Ofertas Ecuador cuidamos tus datos personales conforme a la Ley Orgánica de Protección de Datos Personales del Ecuador.</p>
<h2>Qué datos recopilamos</h2><p>Nombre, número de teléfono, ciudad, provincia, dirección de entrega y punto de referencia, además de los mensajes que nos envías por WhatsApp.</p>
<h2>Para qué los usamos</h2><ul><li>Procesar, despachar y dar seguimiento a tus pedidos.</li><li>Enviarte avisos sobre el estado de tu pedido por WhatsApp.</li><li>Atender garantías y consultas.</li><li>Medir el rendimiento de nuestros anuncios con herramientas de Meta, sin compartir el contenido de tus conversaciones.</li></ul>
<h2>Con quién los compartimos</h2><p>Solo con las transportadoras que entregan tu pedido y con los proveedores tecnológicos que usamos para gestionar pedidos y mensajes. No vendemos tus datos.</p>
<h2>Tus derechos</h2><p>Puedes pedir acceder, corregir o eliminar tus datos, o dejar de recibir mensajes, escribiéndonos por WhatsApp al +593 98 358 2688. Respondemos en un máximo de 15 días.</p>
<h2>Conservación</h2><p>Guardamos tus datos mientras sean necesarios para atender tu pedido, la garantía y nuestras obligaciones legales.</p>
"""),
"contacto.html": ("Contacto", f"""
<p>Estamos para ayudarte antes, durante y después de tu compra.</p>
<h2>WhatsApp</h2><p><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{ico("wa",20)} +593 98 358 2688</a></p>
<h2>Horario de atención</h2><p>Lunes a viernes de 8:00 a 20:00 y sábados de 9:00 a 14:00, hora de Ecuador.</p>
<h2>Cobertura</h2><p>Ofertas Ecuador es una tienda online y despacha a todo el Ecuador.</p>
"""),
}

out = Path(__file__).parent
(out / "index.html").write_text(INDEX)
for f, (t, body) in PAGES.items():
    html = head(f"{t} | Ofertas Ecuador", f"{t} de Ofertas Ecuador.") + \
        f'<main class="page"><div class="wrap narrow"><h1>{t}</h1><p class="updated">Última actualización: 12 de noviembre de 2026</p>{body}</div></main>\n' + FOOT
    (out / f).write_text(html)
print("ok")
