# Daher Clínica Premium - Tema WordPress Otimizado

**Desenvolvido por:** [Hadel Rachid Daher Junior](https://github.com/hadelrachid)  
**Versão:** 2.4.0  
**Arquitetura:** Vanilla JS/CSS (Zero Plugins Dependencies)

Este é um tema WordPress customizado, projetado do zero com um foco implacável em **Alta Performance (PageSpeed Insights)**, **Segurança**, e **Acessibilidade (WCAG)** para clínicas médicas.

---

## 🚀 Destaques de Performance (PageSpeed: 99 Desktop / 93 Mobile)

Diferente de temas comerciais inchados, este projeto adota a filosofia *"Zero Plugins"*, onde toda a inteligência de otimização está embutida no núcleo do tema (functions/PHP).

- **Google Maps Facade Pattern:** Substituição inteligente do Iframe pesado do Maps por um placeholder estático, poupando quase 500KB de JavaScript inútil no carregamento inicial da página de Contato. O mapa real só é injetado sob demanda (interação do usuário).
- **Fontes 100% Locais & Preload:** Google Fonts eliminadas como dependência externa de renderização. Fontes convertidas em `.woff2`, chamadas nativamente via `@font-face (swap)` com `<link rel="preload">` inserido no Head, mitigando o Flash of Unstyled Content (FOUC) sem travar a thread principal.
- **Cache Busting Dinâmico:** Versionamento de arquivos CSS e JS usando `filemtime()`. Elimina problemas de cache do lado do cliente, forçando a renovação automática de assets.
- **Scripts em Defer Seguro:** Filtro nativo que adia o carregamento de JavaScript e CSS auxiliares.
- **Imagens WebP & Tamanhos Responsivos Dinâmicos:** As tags nativas de imagem agora utilizam o motor `wp_get_attachment_image()` do WordPress para gerar automaticamente os tamanhos corretos via `srcset` na Viewport, além da exigência estrita de atributos `width` e `height` para zerar o Cumulative Layout Shift (CLS). Imagens pesadas de fundo passaram por processamento em script Python (LANCZOS resampling) limitando a dimensão máxima (2x Viewport).

## 🛡️ Segurança e Privacidade

- **Desativação de XML-RPC:** Bloqueio nativo contra ataques de força bruta.
- **Content-Security-Policy (CSP):** Cabeçalhos de segurança estritos para evitar injeção de scripts maliciosos.
- **Ocultação da Versão do WP:** Remove assinaturas do WordPress dos cabeçalhos HTTP.

## ♿ Acessibilidade (WCAG 100/100)

- Contraste de cores perfeitamente mapeado para daltonismo e deficiência visual em crachás, botões e tipografia.
- Hierarquia semântica rigorosa (H1 > H2 > H3) na construção das seções.
- Animações CSS limpas de reflow (foco em `transform` e `opacity` para evitar engasgos no celular).

## ⚙️ Painel de Controle Customizado (Settings API)

O tema dispõe de um painel exclusivo (`Daher Clínica`) integrado nativamente ao Dashboard do WordPress.

O painel permite a edição completa de:
- Textos institucionais e informações de contato.
- Configurações do WhatsApp com mensagem padronizada.
- Link das Redes Sociais.
- Gerenciamento de Médicos e Especialidades.
- Aba de **Instruções (Leia-me)** embutida para treinamento do usuário final.

---

## 🛠️ Instalação e Requisitos

1. Faça o upload da pasta `daherclinica-premium` para o diretório `/wp-content/themes/` do seu WordPress.
2. Ative o tema pelo painel de controle.
3. Se estiver migrando de outro tema, rode o plugin **Regenerate Thumbnails** 1 (uma) vez para que o WordPress recorte suas imagens nas novas métricas de performance. Após rodar, o plugin pode ser deletado.

## 🔗 Sobre o Autor

Apaixonado por performance web e código limpo. Para ver mais projetos ou entrar em contato, visite meu perfil no [GitHub](https://github.com/hadelrachid).
