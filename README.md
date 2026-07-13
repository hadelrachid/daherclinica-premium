# Daher Clínica Premium - Tema WordPress Otimizado

**Desenvolvido por:** [Hadel Rachid Daher Junior](https://github.com/hadelrachid)  
**Versão:** 2.4.0  
**Arquitetura:** Vanilla JS/CSS (Zero Plugins Dependencies)

Este é um tema WordPress customizado, projetado do zero com um foco implacável em **Alta Performance (PageSpeed Insights)**, **Segurança**, e **Acessibilidade (WCAG)** para clínicas médicas.

---

## 🚀 Destaques de Performance (PageSpeed: 98 Desktop / 85+ Mobile)

Diferente de temas comerciais inchados, este projeto adota a filosofia *"Zero Plugins"*, onde toda a inteligência de otimização está embutida no núcleo do tema (functions/PHP).

- **Cache Busting Dinâmico:** Versionamento de arquivos CSS e JS usando `filemtime()`. Elimina problemas de cache do lado do cliente, forçando a renovação automática de assets.
- **Resource Hints Avançados:** Deduplicação inteligente de `<link rel="preconnect">` no cabeçalho.
- **Fontes Assíncronas:** Carregamento otimizado de ícones pesados (Font Awesome) utilizando o truque `media="print"` para evitar bloqueio de renderização (Render-Blocking).
- **Scripts em Defer Seguro:** Filtro nativo no `script_loader_tag` que adia o carregamento de JavaScript não-crítico.
- **Imagens WebP & Tamanhos Responsivos:** Régua de cortes personalizadas para o uploader do WordPress, forçando compressão nativa e servindo imagens precisas (reduzindo absurdamente o LCP).

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
