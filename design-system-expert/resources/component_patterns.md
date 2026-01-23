# Component Patterns

Common patterns for building design system components.

## Atomic Design Principles

### Atoms
Smallest building blocks (buttons, inputs, labels)

### Molecules
Groups of atoms (form field = label + input + error)

### Organisms
Groups of molecules (header = logo + navigation + search)

### Templates
Page-level layouts

### Pages
Specific instances of templates

## Component Composition

### Base Component Pattern

```css
/* Base component with common styles */
.card {
  padding: var(--spacing-4);
  border-radius: var(--border-radius-md);
  background: var(--color-background-primary);
}

/* Compose with other components */
.card .button {
  margin-top: var(--spacing-4);
}
```

### Variant Pattern

```css
/* Base */
.button {
  padding: var(--spacing-3) var(--spacing-4);
}

/* Variants */
.button--primary { background: var(--color-primary); }
.button--secondary { background: var(--color-secondary); }
.button--tertiary { background: transparent; }
```

### Size Pattern

```css
.button--sm { padding: var(--spacing-2) var(--spacing-3); }
.button--md { padding: var(--spacing-3) var(--spacing-4); }
.button--lg { padding: var(--spacing-4) var(--spacing-6); }
```

## State Management

### Interactive States

```css
.button {
  /* Default */
  background: var(--color-primary);
  transition: all 0.2s ease;
}

.button:hover {
  /* Hover */
  background: var(--color-primary-dark);
}

.button:active {
  /* Active/Pressed */
  transform: translateY(1px);
}

.button:focus {
  /* Focus */
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.button:disabled {
  /* Disabled */
  opacity: 0.5;
  cursor: not-allowed;
}
```

### Loading State

```css
.button.is-loading {
  position: relative;
  color: transparent;
  pointer-events: none;
}

.button.is-loading::after {
  content: "";
  position: absolute;
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 0.6s linear infinite;
}
```

## Responsive Patterns

### Container Pattern

```css
.container {
  width: 100%;
  max-width: var(--max-width-container);
  margin: 0 auto;
  padding: 0 var(--spacing-4);
}

@media (min-width: 768px) {
  .container {
    padding: 0 var(--spacing-6);
  }
}
```

### Grid Pattern

```css
.grid {
  display: grid;
  gap: var(--spacing-4);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

## Accessibility Patterns

### Focus Visible

```css
.button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

### Screen Reader Only

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

## Best Practices

1. **Single Responsibility**: Each component does one thing well
2. **Composable**: Components can be combined
3. **Predictable**: Consistent behavior across variants
4. **Accessible**: WCAG 2.1 AA compliant
5. **Documented**: Clear usage guidelines
