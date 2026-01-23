# Naming Conventions

Standards for naming tokens, components, files, and CSS classes in design systems.

## Token Naming

### Pattern
```
{category}-{property}-{variant}-{state}
```

### Examples

**Colors**:
- `color-brand-primary`
- `color-semantic-success`
- `color-text-secondary`
- `color-background-primary`

**Typography**:
- `font-family-sans`
- `font-size-heading-lg`
- `font-weight-bold`
- `font-lineHeight-normal`

**Spacing**:
- `spacing-component-sm`
- `spacing-layout-md`
- `spacing-inline-lg`

**Shadows**:
- `shadow-elevation-low`
- `shadow-elevation-high`

### Rules

1. **Use kebab-case**: `color-primary` not `colorPrimary`
2. **Be descriptive**: Full words, not abbreviations
3. **Semantic names**: Purpose, not appearance
4. **Consistent order**: category → property → variant → state

## Component Naming

### BEM Convention

```
.block__element--modifier
```

**Examples**:
```css
.button { }                    /* Block */
.button__icon { }              /* Element */
.button--primary { }           /* Modifier */
.button--large { }             /* Modifier */
.card__header { }              /* Element */
.card__header--highlighted { } /* Element + Modifier */
```

### State Classes

Use `is-` or `has-` prefix:

```css
.button.is-loading { }
.button.is-disabled { }
.card.has-image { }
.modal.is-open { }
```

## File Naming

### Token Files
```
colors.json
typography.json
spacing.json
shadows.json
borders.json
```

### Component Files
```
button.css
button.md
input.css
input.md
```

### Resource Files
```
design-token-standards.md
css-architecture-guide.md
component-patterns.md
naming-conventions.md
```

### Use kebab-case for all files

## CSS Class Naming

### Utility Classes

Prefix with `u-`:

```css
.u-text-center { text-align: center; }
.u-hidden { display: none; }
.u-mt-4 { margin-top: var(--spacing-4); }
```

### Layout Classes

Prefix with `l-`:

```css
.l-container { }
.l-grid { }
.l-flex { }
```

### JavaScript Hooks

Prefix with `js-`:

```html
<button class="button js-toggle">Toggle</button>
```

**Never style `js-` classes**:
```css
/* Good */
.button { }

/* Bad */
.js-toggle { }
```

## Variable Naming

### CSS Custom Properties

```css
--color-primary: #3B82F6;
--spacing-md: 1rem;
--font-size-base: 1rem;
```

### JavaScript Variables

```javascript
const colorPrimary = '#3B82F6';
const spacingMd = '1rem';
const fontSizeBase = '1rem';
```

## Best Practices

1. **Be consistent**: Follow patterns across all naming
2. **Be descriptive**: Clear, self-documenting names
3. **Avoid abbreviations**: Write full words
4. **Use semantic names**: Purpose over appearance
5. **Follow conventions**: BEM for CSS, kebab-case for files
6. **Document exceptions**: Explain any deviations
