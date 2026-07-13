<?php
/**
 * Assets Module
 * Enfileiramento de scripts e estilos do tema
 * 
 * @package DaherClinica
 * @version 1.0.0
 */

if (!defined('ABSPATH')) {
    exit;
}

class DaherClinica_Assets {
    
    public function __construct() {
        add_action('wp_enqueue_scripts', [$this, 'enqueue_styles']);
        add_action('wp_enqueue_scripts', [$this, 'enqueue_scripts']);
    }
    
    public function enqueue_styles() {
        // 1. Recursos Externos
        wp_enqueue_style('daherclinica-fonts', 'https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&family=Playfair+Display:wght@400;500;600;700;800&display=swap', [], null);
        
        // Font Awesome Assíncrono (Carrega como 'print' e muda para 'all' no client-side)
        wp_enqueue_style('daherclinica-fontawesome', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css', [], '6.5.1', 'print');

        // 2. CSS Principal (sempre carrega)
        wp_enqueue_style(
            'daherclinica-main',
            get_template_directory_uri() . '/assets/css/main.min.css',
            [],
            defined('DAHER_THEME_VERSION') ? DAHER_THEME_VERSION : '1.0.0'
        );
        
        // 3. CSS do Blog (apenas nas páginas de blog) - SEM DUPLICAÇÃO
        if (is_page('blog') || is_home() || is_single() || is_archive() || is_category() || is_tag()) {
            wp_enqueue_style(
                'daherclinica-blog',
                get_template_directory_uri() . '/assets/css/blog.min.css',
                ['daherclinica-main'],
                defined('DAHER_THEME_VERSION') ? DAHER_THEME_VERSION : '1.0.0'
            );
        }
    }
    
    public function enqueue_scripts() {
        // 1. JS Principal (sempre carrega) — Vanilla JS puro, sem dependência de jQuery
        wp_enqueue_script(
            'daherclinica-main',
            get_template_directory_uri() . '/assets/js/main.min.js',
            [], // Sem dependências: o main.js usa Vanilla JS puro
            defined('DAHER_THEME_VERSION') ? DAHER_THEME_VERSION : '1.0.0',
            true
        );

        // 2. JS do Blog (apenas nas páginas de blog)
        if (is_page('blog') || is_home() || is_single() || is_archive() || is_category() || is_tag()) {
            wp_enqueue_script(
                'daherclinica-blog',
                get_template_directory_uri() . '/assets/js/blog.min.js',
                ['daherclinica-main'],
                defined('DAHER_THEME_VERSION') ? DAHER_THEME_VERSION : '1.0.0',
                true
            );
        }
        
        // Dados globais para JavaScript
        wp_localize_script('daherclinica-main', 'daherData', [
            'ajaxUrl'        => admin_url('admin-ajax.php'),
            'siteUrl'        => get_site_url(),
            'whatsappNumber' => $this->get_whatsapp_number(),
        ]);
    }
    
    private function get_whatsapp_number() {
        $options = get_option('daher_whatsapp_options', []);
        $number = !empty($options['whatsapp_number']) ? $options['whatsapp_number'] : get_theme_mod('whatsapp_number', '5521977667676');
        return preg_replace('/[^0-9]/', '', $number);
    }
}

// Inicializa a classe
new DaherClinica_Assets();

/**
 * Script inline para ativar o FontAwesome após o carregamento da página
 * Isso remove o bloqueio de renderização (FCP) causado pelo all.min.css
 */
add_action('wp_head', function() {
    echo "<script>
        document.addEventListener('DOMContentLoaded', function() {
            var fa = document.getElementById('daherclinica-fontawesome-css');
            if(fa) fa.media = 'all';
        });
    </script>\n";
}, 99);