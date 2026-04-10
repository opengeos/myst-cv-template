---
title: Services
abstract: ""
exports:
  - format: typst
    template: lapreprint-typst
    output: _build/exports/typst/
---

# Services

This chapter covers my services.

## Overview

Provide an overview of the topic here.

## Sample Dropdown

:::{dropdown} 2025
:open:

- Item 1
- Item 2
- Item 3

:::

:::{dropdown} 2024

- Item 1
- Item 2
- Item 3

:::

## Running the Example

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.set_title("A Simple Plot")
plt.show()
```

## Summary

This example demonstrated the basic workflow.
