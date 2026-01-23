import StyleDictionary from 'style-dictionary';

// Custom format cho TailwindCSS preset
StyleDictionary.registerFormat({
    name: 'tailwind/preset',
    format: function ({ dictionary }) {
        const colors = {};
        const fontSize = {};
        const fontFamily = {};
        const lineHeight = {};
        const letterSpacing = {};
        const borderRadius = {};
        const boxShadow = {};
        const animation = {};
        const screens = {};
        const spacing = {};

        dictionary.allTokens.forEach(token => {
            const path = token.path;
            const value = token.value;

            // Colors
            if (token.type === 'color' && path[0] === 'color') {
                let current = colors;
                for (let i = 1; i < path.length; i++) {
                    if (i === path.length - 1) {
                        current[path[i]] = value;
                    } else {
                        current[path[i]] = current[path[i]] || {};
                        current = current[path[i]];
                    }
                }
            }

            // Font Family
            if (token.type === 'fontFamily') {
                fontFamily[path[path.length - 1]] = value;
            }

            // Font Size
            if (token.type === 'fontSize') {
                const name = path.slice(1).join('-');
                fontSize[name] = value;
            }

            // Line Height
            if (token.type === 'lineHeight') {
                const name = path.slice(1, -1).join('-');
                lineHeight[name] = value;
            }

            // Letter Spacing
            if (token.type === 'letterSpacing') {
                const name = path.slice(1, -1).join('-');
                letterSpacing[name] = value;
            }

            // Border Radius
            if (token.type === 'borderRadius') {
                borderRadius[path[path.length - 1]] = value;
            }

            // Box Shadow
            if (token.type === 'boxShadow' && path[0] === 'shadow') {
                const name = path.slice(1).join('-');
                boxShadow[name] = value;
            }

            // Animation
            if (token.type === 'animation') {
                const name = path.slice(1).join('-');
                animation[name] = value;
            }

            // Breakpoints/Screens
            if (path[0] === 'breakpoint') {
                screens[path[1]] = value;
            }

            // Max Width
            if (path[0] === 'max' && path[1] === 'width') {
                spacing[`max-${path[2]}`] = value;
            }
        });

        const preset = {
            theme: {
                extend: {
                    colors,
                    fontFamily,
                    fontSize,
                    lineHeight,
                    letterSpacing,
                    borderRadius,
                    boxShadow,
                    animation,
                    screens,
                    spacing
                }
            }
        };

        return `/** @type {import('tailwindcss').Config} */
module.exports = ${JSON.stringify(preset, null, 2)};`;
    }
});

// Custom format cho CSS variables
StyleDictionary.registerFormat({
    name: 'css/tailwind-variables',
    format: function ({ dictionary }) {
        let css = ':root {\n';

        dictionary.allTokens.forEach(token => {
            const name = token.path.join('-');
            css += `  --${name}: ${token.value};\n`;
        });

        css += '}\n';
        return css;
    }
});

export default {
    source: ['tokens/**/*.json'],
    platforms: {
        css: {
            transformGroup: 'css',
            buildPath: 'build/css/',
            files: [{
                destination: 'tokens.css',
                format: 'css/tailwind-variables'
            }]
        },
        tailwind: {
            transformGroup: 'js',
            buildPath: 'build/',
            files: [{
                destination: 'tailwind.preset.js',
                format: 'tailwind/preset'
            }]
        }
    }
};
