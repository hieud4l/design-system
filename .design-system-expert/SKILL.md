---
name: design-system-expert
description: Comprehensive Design System Expert skill for creating, managing, and scaling design systems. Includes design token workflows, Style Dictionary integration, CSS architecture, component generation, and design system documentation. Use when the user mentions design tokens, Style Dictionary, CSS custom properties, design system creation, token conversion, or needs help building scalable design systems.
---

# Design System Expert Skill

## When to use this skill

Use this skill when the user needs to:
- Create or manage design tokens
- Convert CSS custom properties to JSON format
- Set up Style Dictionary for token transformation
- Build a complete design system from scratch
- Generate component specifications and code
- Validate design token structure and naming
- Create design system documentation
- Migrate from CSS to token-based systems
- Scale and maintain design systems
- Generate Style Dictionary configurations

## Workflow Checklist

Copy this checklist to track your progress:

```markdown
## Design System Workflow
- [ ] 1. Define design system goals and scope
- [ ] 2. Create or audit design tokens
- [ ] 3. Set up token structure and naming conventions
- [ ] 4. Convert CSS to JSON tokens (if migrating)
- [ ] 5. Configure Style Dictionary
- [ ] 6. Generate component specifications
- [ ] 7. Create design system documentation
- [ ] 8. Validate tokens and build outputs
- [ ] 9. Set up version control and distribution
```

## Core Instructions

### 1. Design Tokens Fundamentals

Design tokens are the atomic design decisions that make up your design system. They are platform-agnostic values that can be transformed into platform-specific formats.

#### Token Categories

**Color Tokens**:
```json
{
  "color": {
    "brand": {
      "primary": { "value": "#3B82F6", "type": "color" },
      "secondary": { "value": "#8B5CF6", "type": "color" }
    },
    "semantic": {
      "success": { "value": "#10B981", "type": "color" },
      "warning": { "value": "#F59E0B", "type": "color" },
      "error": { "value": "#EF4444", "type": "color" }
    },
    "neutral": {
      "50": { "value": "#F9FAFB", "type": "color" },
      "900": { "value": "#111827", "type": "color" }
    }
  }
}
```

**Typography Tokens**:
```json
{
  "font": {
    "family": {
      "sans": { "value": "Inter, system-ui, sans-serif", "type": "fontFamily" },
      "mono": { "value": "Fira Code, monospace", "type": "fontFamily" }
    },
    "size": {
      "xs": { "value": "0.75rem", "type": "dimension" },
      "sm": { "value": "0.875rem", "type": "dimension" },
      "base": { "value": "1rem", "type": "dimension" },
      "lg": { "value": "1.125rem", "type": "dimension" }
    },
    "weight": {
      "normal": { "value": "400", "type": "fontWeight" },
      "medium": { "value": "500", "type": "fontWeight" },
      "bold": { "value": "700", "type": "fontWeight" }
    }
  }
}
```

**Spacing Tokens**:
```json
{
  "spacing": {
    "0": { "value": "0", "type": "dimension" },
    "1": { "value": "0.25rem", "type": "dimension" },
    "2": { "value": "0.5rem", "type": "dimension" },
    "4": { "value": "1rem", "type": "dimension" },
    "8": { "value": "2rem", "type": "dimension" }
  }
}
```

#### Token Hierarchy

Organize tokens in three levels:

1. **Global Tokens**: Base values (colors, sizes)
2. **Alias Tokens**: Semantic references to global tokens
3. **Component Tokens**: Component-specific values

Example:
```json
{
  "color": {
    "blue": {
      "500": { "value": "#3B82F6", "type": "color" }
    }
  },
  "semantic": {
    "primary": { "value": "{color.blue.500}", "type": "color" }
  },
  "button": {
    "background": { "value": "{semantic.primary}", "type": "color" }
  }
}
```

### 2. CSS to JSON Token Conversion

Convert CSS custom properties to Style Dictionary JSON format.

#### Using the Token Converter

```bash
python scripts/token_converter.py \
  --input path/to/tokens.css \
  --output tokens.json \
  --validate
```

**Input (CSS)**:
```css
:root {
  --color-primary: #3B82F6;
  --color-secondary: #8B5CF6;
  --font-size-base: 1rem;
  --spacing-md: 1rem;
}
```

**Output (JSON)**:
```json
{
  "color": {
    "primary": { "value": "#3B82F6", "type": "color" },
    "secondary": { "value": "#8B5CF6", "type": "color" }
  },
  "font": {
    "size": {
      "base": { "value": "1rem", "type": "dimension" }
    }
  },
  "spacing": {
    "md": { "value": "1rem", "type": "dimension" }
  }
}
```

#### Handling Light/Dark Mode

For mode-specific tokens:

```json
{
  "color": {
    "background": {
      "primary": {
        "value": "#FFFFFF",
        "type": "color",
        "$extensions": {
          "mode": {
            "light": "#FFFFFF",
            "dark": "#1F2937"
          }
        }
      }
    }
  }
}
```

### 3. Style Dictionary Setup

Style Dictionary transforms design tokens into platform-specific formats.

#### Generating Style Dictionary Config

```bash
python scripts/style_dictionary_config_generator.py \
  --platforms web,ios,android \
  --output config.json
```

#### Example Configuration

```json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "web": {
      "transformGroup": "css",
      "buildPath": "build/css/",
      "files": [{
        "destination": "variables.css",
        "format": "css/variables"
      }]
    },
    "scss": {
      "transformGroup": "scss",
      "buildPath": "build/scss/",
      "files": [{
        "destination": "_variables.scss",
        "format": "scss/variables"
      }]
    }
  }
}
```

#### Building Tokens

```bash
# Install Style Dictionary
npm install -g style-dictionary

# Build tokens
style-dictionary build --config config.json
```

### 4. Token Validation

Validate tokens before building to catch errors early.

#### Using the Token Validator

```bash
python scripts/token_validator.py \
  --input tokens.json \
  --check-naming \
  --check-values \
  --check-references \
  --output validation_report.md
```

**Validation Checks**:
- ✅ Naming conventions (kebab-case, semantic names)
- ✅ Valid color values (hex, rgb, hsl)
- ✅ Valid dimension units (rem, px, em)
- ✅ Token references resolve correctly
- ✅ No circular references
- ✅ Required tokens exist

### 5. Design System Builder

Generate a complete design system structure.

#### Creating a New Design System

```bash
python scripts/design_system_builder.py \
  --name "My Design System" \
  --brand-color "#3B82F6" \
  --output design-system/
```

**Generated Structure**:
```
design-system/
├── tokens/
│   ├── colors.json
│   ├── typography.json
│   ├── spacing.json
│   └── shadows.json
├── config.json (Style Dictionary config)
├── package.json
├── README.md
└── docs/
    ├── getting-started.md
    └── token-reference.md
```

### 6. Component Generation

Generate component specifications and code.

#### Generating Components

```bash
python scripts/component_generator.py \
  --components button,input,card \
  --tokens tokens.json \
  --output components/
```

**Generated for Each Component**:
- Component documentation (purpose, variants, states)
- CSS/SCSS implementation using tokens
- Accessibility guidelines
- Usage examples
- Props/attributes documentation

#### Example: Button Component

**Documentation** (`components/button.md`):
```markdown
# Button Component

## Purpose
Trigger actions and events with clear visual hierarchy.

## Variants
- Primary: Main call-to-action
- Secondary: Less prominent actions
- Tertiary: Minimal emphasis
- Danger: Destructive actions

## States
- Default
- Hover
- Active
- Disabled
- Loading

## Accessibility
- Minimum 44x44px touch target
- ARIA labels for icon-only buttons
- Keyboard accessible (Enter/Space)
- Focus visible indicator
```

**CSS Implementation** (`components/button.css`):
```css
.button {
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  border-radius: var(--border-radius-md);
  transition: all 0.2s ease;
}

.button--primary {
  background: var(--color-primary);
  color: var(--color-white);
}

.button--primary:hover {
  background: var(--color-primary-dark);
}

.button--primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### 7. Token Naming Conventions

Follow consistent naming patterns for maintainability.

#### Recommended Patterns

**Category-Based Naming**:
```
{category}-{property}-{variant}-{state}
```

Examples:
- `color-background-primary`
- `color-text-secondary`
- `font-size-heading-lg`
- `spacing-component-md`
- `shadow-elevation-high`

**Semantic Naming**:
```json
{
  "color": {
    "action": {
      "primary": { "value": "#3B82F6" },
      "secondary": { "value": "#8B5CF6" }
    },
    "feedback": {
      "success": { "value": "#10B981" },
      "error": { "value": "#EF4444" }
    }
  }
}
```

**Component-Specific Naming**:
```json
{
  "button": {
    "background": {
      "primary": { "value": "{color.action.primary}" },
      "secondary": { "value": "{color.action.secondary}" }
    },
    "padding": {
      "sm": { "value": "{spacing.2} {spacing.3}" },
      "md": { "value": "{spacing.3} {spacing.4}" }
    }
  }
}
```

See `resources/naming_conventions.md` for complete guidelines.

### 8. CSS Architecture

Organize CSS for scalability and maintainability.

#### Recommended Structure

```
styles/
├── tokens/
│   └── variables.css (generated from tokens)
├── base/
│   ├── reset.css
│   └── typography.css
├── components/
│   ├── button.css
│   ├── input.css
│   └── card.css
├── utilities/
│   └── spacing.css
└── main.css (imports all)
```

#### Using CSS Custom Properties

```css
/* tokens/variables.css (generated) */
:root {
  --color-primary: #3B82F6;
  --spacing-md: 1rem;
  --font-size-base: 1rem;
}

/* components/button.css */
.button {
  padding: var(--spacing-md);
  font-size: var(--font-size-base);
  background: var(--color-primary);
}
```

See `resources/css_architecture_guide.md` for best practices.

## Scripts and Tools

### Helper Scripts Location

All scripts are in the `scripts/` directory:

- `token_converter.py`: Convert CSS to JSON tokens
- `token_validator.py`: Validate token structure and values
- `design_system_builder.py`: Generate complete design system
- `component_generator.py`: Create component specs and code
- `style_dictionary_config_generator.py`: Generate Style Dictionary config

### Running Scripts

Always check help documentation first:

```bash
python scripts/[script_name].py --help
```

### Common Script Options

**Token Converter**:
```bash
python scripts/token_converter.py \
  --input tokens.css \
  --output tokens.json \
  --validate \
  --format pretty
```

**Token Validator**:
```bash
python scripts/token_validator.py \
  --input tokens.json \
  --check-naming \
  --check-values \
  --check-references \
  --strict \
  --output report.md
```

**Design System Builder**:
```bash
python scripts/design_system_builder.py \
  --name "Design System" \
  --brand-color "#3B82F6" \
  --include-examples \
  --output design-system/
```

## Common Workflows

### Workflow 1: New Design System from Scratch

```bash
# 1. Create design system structure
python scripts/design_system_builder.py \
  --name "My Design System" \
  --brand-color "#3B82F6" \
  --output my-design-system/

# 2. Navigate to design system
cd my-design-system/

# 3. Install dependencies
npm install

# 4. Build tokens
npm run build

# 5. Generate components
python ../scripts/component_generator.py \
  --components button,input,card,modal \
  --tokens tokens/colors.json \
  --output components/
```

### Workflow 2: Migrate from CSS to Tokens

```bash
# 1. Convert existing CSS variables to JSON
python scripts/token_converter.py \
  --input styles/variables.css \
  --output tokens/converted.json \
  --validate

# 2. Validate converted tokens
python scripts/token_validator.py \
  --input tokens/converted.json \
  --check-all \
  --output validation_report.md

# 3. Generate Style Dictionary config
python scripts/style_dictionary_config_generator.py \
  --platforms web,scss \
  --output config.json

# 4. Build tokens
style-dictionary build --config config.json
```

### Workflow 3: Add New Components

```bash
# 1. Generate component specifications
python scripts/component_generator.py \
  --components dropdown,tooltip,badge \
  --tokens tokens/all.json \
  --include-docs \
  --include-css \
  --output components/

# 2. Review generated files
ls components/
# dropdown.md, dropdown.css
# tooltip.md, tooltip.css
# badge.md, badge.css
```

### Workflow 4: Token Validation and Quality Check

```bash
# Run comprehensive validation
python scripts/token_validator.py \
  --input tokens/ \
  --check-naming \
  --check-values \
  --check-references \
  --check-duplicates \
  --strict \
  --output validation_report.md

# Review report
cat validation_report.md
```

## Best Practices

### Design Tokens

- **Use semantic names**: `color-primary` not `color-blue`
- **Organize hierarchically**: Global → Alias → Component
- **Keep it DRY**: Use references to avoid duplication
- **Version your tokens**: Track changes in version control
- **Document decisions**: Explain why tokens exist

### Token Organization

- **Separate by category**: colors.json, typography.json, spacing.json
- **Use consistent structure**: Same format across all token files
- **Group related tokens**: Keep semantic tokens together
- **Avoid deep nesting**: Max 3-4 levels deep

### Naming Conventions

- **Use kebab-case**: `color-background-primary`
- **Be descriptive**: `button-padding-large` not `btn-pd-lg`
- **Follow patterns**: Consistent naming across all tokens
- **Avoid abbreviations**: Write full words for clarity

### Style Dictionary

- **Use transformGroups**: Leverage built-in transforms
- **Create custom transforms**: For specific needs
- **Organize platforms**: Separate configs for web, mobile, etc.
- **Test builds**: Validate output before deployment

### Component Generation

- **Start with basics**: Button, Input, Card first
- **Document thoroughly**: Include usage examples
- **Use tokens consistently**: Reference design tokens
- **Consider accessibility**: WCAG 2.1 AA compliance
- **Include variants**: Cover all use cases

### CSS Architecture

- **Use BEM methodology**: Block__Element--Modifier
- **Leverage custom properties**: For dynamic theming
- **Keep specificity low**: Avoid deep selectors
- **Mobile-first**: Start with mobile styles
- **Optimize performance**: Minimize CSS size

## Error Handling

Common issues and solutions:

### Token Conversion Errors

**Issue**: Invalid CSS variable format
```
Error: Cannot parse CSS variable: --color primary: #3B82F6
```
**Solution**: Ensure proper CSS syntax with colon
```css
--color-primary: #3B82F6;
```

### Validation Errors

**Issue**: Invalid color value
```
Error: Invalid color value "blue" for token color.primary
```
**Solution**: Use valid hex, rgb, or hsl values
```json
{ "value": "#3B82F6", "type": "color" }
```

**Issue**: Circular reference
```
Error: Circular reference detected: color.primary → color.secondary → color.primary
```
**Solution**: Break the circular dependency

### Style Dictionary Build Errors

**Issue**: Token reference not found
```
Error: Cannot resolve reference {color.nonexistent}
```
**Solution**: Ensure referenced token exists

**Issue**: Invalid transform
```
Error: Unknown transform: custom/invalid
```
**Solution**: Check transform name or register custom transform

## Resources

- [Design Token Standards](./resources/design_token_standards.md)
- [CSS Architecture Guide](./resources/css_architecture_guide.md)
- [Component Patterns](./resources/component_patterns.md)
- [Naming Conventions](./resources/naming_conventions.md)
- [Sample Tokens](./examples/sample_tokens.json)
- [Sample Component](./examples/sample_component.md)
- [Sample Style Dictionary Config](./examples/sample_style_dictionary_config.json)
- [Sample Design System](./examples/sample_design_system.md)

## External Resources

- [Style Dictionary Documentation](https://amzn.github.io/style-dictionary/)
- [Design Tokens W3C Community Group](https://www.w3.org/community/design-tokens/)
- [CSS Custom Properties MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)
