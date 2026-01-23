# CSS Architecture Guide

Best practices for organizing and writing scalable CSS in design systems.

## Architecture Principles

### 1. Modularity
- Break CSS into small, reusable modules
- Each module should have a single responsibility
- Avoid tight coupling between modules

### 2. Scalability
- Structure should support growth
- Easy to add new components
- Minimal impact when making changes

### 3. Maintainability
- Clear naming conventions
- Consistent patterns
- Well-documented code

## File Organization

### Recommended Structure

```
styles/
├── tokens/
│   └── variables.css          # Generated from design tokens
├── base/
│   ├── reset.css              # CSS reset/normalize
│   ├── typography.css         # Base typography
│   └── global.css             # Global styles
├── components/
│   ├── button.css
│   ├── input.css
│   ├── card.css
│   └── modal.css
├── utilities/
│   ├── spacing.css            # Margin/padding utilities
│   ├── display.css            # Display utilities
│   └── text.css               # Text utilities
├── layouts/
│   ├── grid.css
│   └── container.css
└── main.css                   # Imports all files
```

## BEM Methodology

Use Block Element Modifier (BEM) for naming:

```css
/* Block */
.button { }

/* Element */
.button__icon { }

/* Modifier */
.button--primary { }
.button--large { }

/* Combined */
.button--primary .button__icon { }
```

**Rules**:
- Block: Standalone component (`.button`)
- Element: Part of block (`.button__icon`)
- Modifier: Variation of block (`.button--primary`)
- Use double underscores for elements (`__`)
- Use double hyphens for modifiers (`--`)

## CSS Custom Properties

### Using Design Tokens

```css
/* tokens/variables.css (generated) */
:root {
  --color-primary: #3B82F6;
  --spacing-md: 1rem;
  --font-size-base: 1rem;
}

/* components/button.css */
.button {
  background: var(--color-primary);
  padding: var(--spacing-md);
  font-size: var(--font-size-base);
}
```

### Theming with Custom Properties

```css
/* Light theme (default) */
:root {
  --background: #FFFFFF;
  --text: #111827;
}

/* Dark theme */
[data-theme="dark"] {
  --background: #111827;
  --text: #F9FAFB;
}

/* Component uses theme variables */
.card {
  background: var(--background);
  color: var(--text);
}
```

## Cascade and Specificity

### Keep Specificity Low

**Good**:
```css
.button { }
.button--primary { }
```

**Bad**:
```css
div.container .button.primary { }
```

### Avoid !important

Only use `!important` for utilities:

```css
/* Utility classes can use !important */
.u-hidden {
  display: none !important;
}

/* Regular components should not */
.button {
  color: blue; /* Not !important */
}
```

## Component Patterns

### Base + Modifiers

```css
/* Base component */
.button {
  padding: var(--spacing-3) var(--spacing-4);
  border-radius: var(--border-radius-md);
  font-weight: var(--font-weight-medium);
}

/* Modifiers */
.button--primary {
  background: var(--color-primary);
  color: white;
}

.button--large {
  padding: var(--spacing-4) var(--spacing-6);
  font-size: var(--font-size-lg);
}
```

### State Classes

```css
.button {
  /* Base styles */
}

.button:hover {
  opacity: 0.9;
}

.button:disabled,
.button.is-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.button.is-loading {
  position: relative;
  color: transparent;
}
```

## Performance Optimization

### 1. Minimize Selectors

**Good**:
```css
.nav-item { }
```

**Bad**:
```css
header nav ul li a { }
```

### 2. Avoid Universal Selectors

**Good**:
```css
.button { box-sizing: border-box; }
```

**Bad**:
```css
* { box-sizing: border-box; }
```

### 3. Group Related Properties

```css
.button {
  /* Positioning */
  position: relative;
  
  /* Box model */
  display: inline-flex;
  padding: var(--spacing-3);
  
  /* Typography */
  font-size: var(--font-size-base);
  
  /* Visual */
  background: var(--color-primary);
  border-radius: var(--border-radius-md);
  
  /* Misc */
  cursor: pointer;
}
```

## Responsive Design

### Mobile-First Approach

```css
/* Mobile (default) */
.container {
  padding: var(--spacing-4);
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: var(--spacing-6);
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    padding: var(--spacing-8);
  }
}
```

### Use Design Tokens for Breakpoints

```css
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
}

@media (min-width: var(--breakpoint-md)) {
  /* Tablet styles */
}
```

## Best Practices

1. **Use design tokens**: Reference CSS custom properties
2. **Follow BEM**: Consistent naming convention
3. **Keep specificity low**: Avoid deep nesting
4. **Mobile-first**: Start with mobile styles
5. **Group properties**: Organize logically
6. **Comment complex code**: Explain why, not what
7. **Avoid magic numbers**: Use tokens instead
8. **Test cross-browser**: Ensure compatibility
