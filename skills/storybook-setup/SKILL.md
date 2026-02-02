---
name: storybook-setup
description: Set up and configure Storybook for component library documentation and isolated development
---

# Storybook Setup Skill

## When to Use This Skill

- Setting up Storybook for React component library
- Documenting components with stories
- Creating interactive component documentation
- Building design systems with Storybook
- Setting up component previews for designers
- Configuring Storybook add-ons and plugins
- Integrating Storybook with CI/CD pipelines
- Creating visual regression testing with Storybook

## Quick Start

```
/storybook-setup <project_type_and_requirements>
```

**Example**:
```
/storybook-setup React component library with TypeScript, Tailwind CSS, and accessibility testing
```

## How It Works

The skill sets up complete Storybook configuration:

### 1. Storybook Installation
- **Initialize**: npx sb init command
- **Framework Setup**: React, Vue, Angular, Svelte configurations
- **Webpack/Vite**: Modern bundler configuration
- **TypeScript**: Full TypeScript support

### 2. Story Structure
- **Component Story Format (CSF)**: Modern story format
- **Argon Control**: Interactive prop manipulation
- **Decorators**: Global and story-level decorators
- **Subcomponents**: Document related components

### 3. Add-ons
- **Essentials**: Docs, Controls, Actions, Viewport
- **Custom Add-ons**: Accessibility, Visual regression, Interaction
- **Third-party**: Figma, Chromatic, Percy integration

### 4. Documentation
- **MDX**: Write stories with markdown
- **DocsPage**: Auto-generated documentation
- **Description**: Component and prop descriptions
- **Stories in Docs**: Embed live stories in documentation

## Configuration

**Storybook Setup (main.ts)**:
```typescript
import type { StorybookConfig } from "@storybook/react-webpack5";

const config: StorybookConfig = {
  stories: ["../src/**/*.stories.{js,jsx,ts,tsx}"],
  addons: [
    "@storybook/addon-essentials",
    "@storybook/addon-interactions",
    "@storybook/addon-a11y",
  ],
  framework: "@storybook/react-webpack5",
  docs: {
    autodocs: "tag",
  },
};

export default config;
```

## Examples

### Example 1: Basic Button Story

```typescript
// Button.stories.tsx
import type { Meta, StoryObj } from "@storybook/react";
import { Button } from "./Button";

const meta = {
  title: "Components/Button",
  component: Button,
  tags: ["autodocs"],
  parameters: {
    layout: "centered",
  },
  argTypes: {
    variant: {
      control: "select",
      options: ["primary", "secondary", "danger"],
    },
    size: {
      control: "select",
      options: ["small", "medium", "large"],
    },
    disabled: {
      control: "boolean",
    },
  },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: {
    variant: "primary",
    size: "medium",
    children: "Click me",
  },
};

export const Secondary: Story = {
  args: {
    variant: "secondary",
    size: "medium",
    children: "Click me",
  },
};

export const Disabled: Story = {
  args: {
    variant: "primary",
    size: "medium",
    disabled: true,
    children: "Disabled",
  },
};

export const AllSizes: Story = {
  render: (args) => (
    <div style={{ display: "flex", gap: "1rem" }}>
      <Button {...args} size="small">
        Small
      </Button>
      <Button {...args} size="medium">
        Medium
      </Button>
      <Button {...args} size="large">
        Large
      </Button>
    </div>
  ),
};
```

### Example 2: Form Component Story

```typescript
// Form.stories.tsx
import type { Meta, StoryObj } from "@storybook/react";
import { useState } from "react";
import { Form } from "./Form";

const meta = {
  title: "Components/Form",
  component: Form,
  tags: ["autodocs"],
  parameters: {
    layout: "centered",
  },
} satisfies Meta<typeof Form>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  render: () => {
    const [formData, setFormData] = useState({ email: "", password: "" });

    return (
      <Form
        onSubmit={(data) => {
          alert(JSON.stringify(data));
          setFormData(data);
        }}
      >
        {/* Form fields */}
      </Form>
    );
  },
};

export const WithValidation: Story = {
  render: () => {
    const [errors, setErrors] = useState<Record<string, string>>({});

    const validate = (data: Record<string, string>) => {
      const newErrors: Record<string, string> = {};
      if (!data.email.includes("@")) {
        newErrors.email = "Invalid email";
      }
      if (data.password.length < 8) {
        newErrors.password = "Min 8 characters";
      }
      setErrors(newErrors);
      return Object.keys(newErrors).length === 0;
    };

    return <Form onSubmit={validate ? undefined : () => {}} />;
  },
};

export const Loading: Story = {
  args: {
    isSubmitting: true,
  },
};
```

### Example 3: MDX Documentation

```mdx
// Button.mdx
import { Meta, Controls, Stories } from "@storybook/blocks";
import * as ButtonStories from "./Button.stories";

<Meta of={ButtonStories} />

# Button Component

A versatile button component that supports multiple variants and sizes.

## Usage

```tsx
import { Button } from "@/components/Button";

export const MyComponent = () => (
  <Button variant="primary" size="large">
    Click me
  </Button>
);
```

## Props

<Controls of={ButtonStories.Primary} />

## Stories

<Stories of={ButtonStories} />
```

### Example 4: Accessibility Testing

```typescript
// Button.stories.tsx
import { Meta, StoryObj } from "@storybook/react";
import { Button } from "./Button";

const meta = {
  title: "Components/Button",
  component: Button,
  tags: ["autodocs"],
  parameters: {
    a11y: {
      config: {
        rules: [
          {
            id: "color-contrast",
            enabled: true,
          },
        ],
      },
    },
  },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Accessible: Story = {
  args: {
    children: "Click me",
    "aria-label": "Submit form",
  },
  parameters: {
    a11y: {
      // Custom accessibility checks
      disable: ["button-name"], // Disable specific rules if needed
    },
  },
};

export const WithIcon: Story = {
  args: {
    children: (
      <>
        <Icon /> Download
      </>
    ),
    "aria-label": "Download document",
  },
};
```

### Example 5: Interaction Testing

```typescript
// Modal.stories.tsx
import { Meta, StoryObj } from "@storybook/react";
import { userEvent, within, expect } from "@storybook/test";
import { Modal } from "./Modal";

const meta = {
  title: "Components/Modal",
  component: Modal,
  tags: ["autodocs"],
} satisfies Meta<typeof Modal>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    isOpen: true,
    title: "Confirm Action",
    onClose: () => {},
  },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);

    // Test that title is visible
    const title = canvas.getByText("Confirm Action");
    await expect(title).toBeInTheDocument();

    // Test button interaction
    const closeButton = canvas.getByRole("button", { name: /close/i });
    await userEvent.click(closeButton);
  },
};

export const ConfirmationFlow: Story = {
  args: {
    isOpen: true,
    title: "Delete Item?",
    onConfirm: () => alert("Deleted"),
    onCancel: () => alert("Cancelled"),
  },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);

    // Click confirm button
    const confirmBtn = canvas.getByRole("button", { name: /confirm/i });
    await userEvent.click(confirmBtn);

    // Verify callback was called
    await expect(confirmBtn).not.toBeInTheDocument();
  },
};
```

## Best Practices

### 1. Story Organization
```
src/
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   └── Button.stories.tsx
│   ├── Form/
│   │   ├── Form.tsx
│   │   └── Form.stories.tsx
```

### 2. Naming Convention
- Title: `Components/ComponentName`
- Exported names: `Primary`, `Secondary`, `Disabled`, etc.
- Stories reflect prop variations

### 3. Controls Documentation
```typescript
argTypes: {
  size: {
    control: "select",
    options: ["small", "medium", "large"],
    description: "Button size",
  },
  onClick: {
    action: "clicked", // Shows in Actions panel
  },
}
```

### 4. Default Props
```typescript
const meta = {
  component: Button,
  args: {
    size: "medium",
    variant: "primary",
  },
} satisfies Meta<typeof Button>;
```

## Add-ons Configuration

**Essential Add-ons** (automatic):
- Docs: Component documentation
- Controls: Interactive prop editor
- Actions: Event logging
- Viewport: Responsive testing

**Recommended Add-ons**:
```typescript
addons: [
  "@storybook/addon-essentials",
  "@storybook/addon-interactions",      // Interaction testing
  "@storybook/addon-a11y",             // Accessibility testing
  "storybook-addon-performance",        // Performance metrics
  "@chromatic-com/storybook",          // Visual regression
]
```

## Integration with Other Skills

- **`react-component-patterns`**: Document component patterns
- **`react-testing-strategy`**: Interaction testing in stories
- **`frontend-performance`**: Performance monitoring in Storybook
- **`javascript-documentation`**: Auto-generate component docs

## Storybook Deployment

- **Chromatic**: Visual regression and review
- **GitHub Pages**: Static hosting
- **Vercel/Netlify**: Automatic deployment on push
- **AWS S3**: CDN-hosted component library

## Storybook Checklist

- [ ] Storybook installed and configured
- [ ] Stories created for all components
- [ ] Controls configured for all props
- [ ] Accessibility add-on configured
- [ ] Interaction tests written
- [ ] MDX documentation added
- [ ] Deployed to hosting service
- [ ] Team using Storybook for design review
- [ ] Visual regression testing enabled
- [ ] API documentation auto-generated
