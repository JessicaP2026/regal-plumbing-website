<?php
/**
 * Regal Plumbing Child Theme Functions
 */

// Enqueue parent and child theme stylesheets + Google Fonts
add_action( 'wp_enqueue_scripts', 'regal_enqueue_styles' );
function regal_enqueue_styles() {
    wp_enqueue_style(
        'regal-child-style',
        get_stylesheet_directory_uri() . '/style.css',
        [ 'hello-elementor' ],
        wp_get_theme()->get( 'Version' )
    );
    wp_enqueue_style(
        'regal-custom-style',
        get_stylesheet_directory_uri() . '/assets/css/custom.css',
        [ 'regal-child-style' ]
    );
    wp_enqueue_style(
        'google-fonts-oswald-opensans',
        'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Oswald:wght@400;500;700&display=swap',
        [],
        null
    );
    wp_enqueue_script(
        'regal-custom-js',
        get_stylesheet_directory_uri() . '/assets/js/custom.js',
        [],
        wp_get_theme()->get( 'Version' ),
        true  // load in footer
    );
}
