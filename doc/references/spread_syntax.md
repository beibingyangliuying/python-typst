# Typst Spread Syntax: `..list`

## 1. Core idea

In Typst, the `..` syntax is commonly called the **spread operator**. Its basic purpose is to take a container-like value and expand it into a place where Typst expects a sequence of items or arguments.

A concise rule of thumb is:

> Use `..value` when you already have a collection, but the current context expects its elements as separate items.

For example, if a function expects several positional arguments, an array can be spread into those arguments:

```typst
#let values = (2, 3, 5)

#calc.min(..values)
```

This is equivalent to:

```typst
#calc.min(2, 3, 5)
```

The `..` operator is therefore not a normal displayable expression. It only makes sense in specific syntactic contexts such as function calls, array or dictionary construction, and destructuring patterns.

---

## 2. Spreading arrays in function calls

When an array is spread in a function call, each array item becomes a separate **positional argument**.

```typst
#let cells = ([A], [B], [C], [D])

#table(
  columns: 2,
  ..cells,
)
```

This is conceptually similar to writing:

```typst
#table(
  columns: 2,
  [A], [B], [C], [D],
)
```

This pattern is especially useful when generating table cells, grid children, list items, or other repeated content programmatically.

Example:

```typst
#let items = (
  [First item],
  [Second item],
  [Third item],
)

#list(..items)
```

Here, `items` is an array, and `..items` passes each array element as a separate child argument to `list`.

---

## 3. Spreading dictionaries as named arguments

When a dictionary is spread in a function call, each key-value pair becomes a separate **named argument**.

```typst
#let style = (
  fill: blue,
  size: 12pt,
)

#text(..style)[Hello]
```

This is equivalent to:

```typst
#text(fill: blue, size: 12pt)[Hello]
```

This pattern is useful when you want to define a reusable style configuration:

```typst
#let heading-style = (
  weight: "bold",
  size: 16pt,
  fill: navy,
)

#text(..heading-style)[Section Title]
```

General rule:

```typst
..array       // expands into positional arguments
..dictionary  // expands into named arguments
```

---

## 4. Spreading `arguments`

Typst also has an `arguments` type. It can contain both positional and named arguments.

A common way to obtain an `arguments` value is by using an **argument sink** in a function definition:

```typst
#let wrapper(..args) = {
  box(..args)
}
```

Here:

- `..args` in the function definition collects all supplied arguments.
- `..args` in the `box(..args)` call spreads them back into another function call.

This is useful for wrapper functions:

```typst
#let framed(..args) = {
  rect(
    stroke: 0.5pt,
    inset: 8pt,
    ..args,
  )
}

#framed(fill: luma(240))[Important content]
```

The wrapper adds default behavior while still allowing the caller to pass additional arguments.

The collected `arguments` object can also be inspected:

```typst
#let inspect(..args) = {
  args.pos()
  args.named()
}
```

Typical methods include:

```typst
args.pos()      // positional arguments
args.named()    // named arguments
args.at(0)      // argument by position
args.at("key")  // argument by name
```

---

## 5. Spreading into dictionaries

The spread operator can also be used inside dictionary construction.

```typst
#let base-style = (
  fill: blue,
  size: 10pt,
)

#let final-style = (
  ..base-style,
  size: 12pt,
)
```

If the same key appears multiple times, the later value overrides the earlier value.

In this example:

```typst
#let final-style = (
  ..base-style,
  size: 12pt,
)
```

the final value of `size` is `12pt`, not `10pt`.

This makes dictionary spreading useful for defining defaults and then overriding selected fields:

```typst
#let default-style = (
  fill: black,
  size: 10pt,
  weight: "regular",
)

#let title-style = (
  ..default-style,
  size: 18pt,
  weight: "bold",
)
```

### Special case: dictionary consisting only of spreads

If a dictionary consists only of spread items, Typst requires a special syntax:

```typst
#let copied = (:..base-style)
```

This is different from:

```typst
#let copied = (..base-style)
```

The latter can be interpreted as an array context rather than a dictionary context. The leading colon in `(:..base-style)` disambiguates the expression as a dictionary.

---

## 6. Spreading and destructuring

The same `..` symbol is also used in destructuring patterns, but the direction is different.

In a function call, `..` expands a collection outward. In destructuring, `..` collects the remaining items.

Example:

```typst
#let (first, ..middle, last) = (1, 2, 3, 4)
```

The result is conceptually:

```typst
first  = 1
middle = (2, 3)
last   = 4
```

You can also ignore the middle part:

```typst
#let (first, .., last) = (1, 2, 3, 4)
```

This keeps only the first and last values.

A destructuring pattern can contain at most one `..`, because only one part of the pattern can collect the remaining items.

---

## 7. Important limitation: `..` is not a general-purpose concatenation operator

The spread syntax is context-dependent. It cannot be used as an ordinary expression.

Valid examples:

```typst
#calc.min(..values)

#table(
  columns: 2,
  ..cells,
)

#text(..style)[Hello]
```

Invalid idea:

```typst
#{..values}
```

The problem is that there is no function argument list, array construction, dictionary construction, or destructuring pattern that can receive the spread result.

So the practical rule is:

> `..value` must appear in a context that knows how to consume expanded items.

---

## 8. Single-element array pitfall

In Typst, a one-element array needs a trailing comma.

Correct:

```typst
#let xs = (1,)
#calc.min(..xs)
```

Incorrect if you intended an array:

```typst
#let xs = (1)
```

`(1)` is just the value `1` in parentheses, not a one-element array.

Therefore, if you want to spread a one-element array, write:

```typst
#func(..(x,))
```

not:

```typst
#func(..(x))
```

---

## 9. Practical patterns

### 9.1 Reusable table cells

```typst
#let row = ([A], [B], [C])

#table(
  columns: 3,
  ..row,
)
```

### 9.2 Reusable style dictionaries

```typst
#let emphasis = (
  fill: red,
  weight: "bold",
)

#text(..emphasis)[Warning]
```

### 9.3 Defaults plus overrides

```typst
#let base = (
  size: 10pt,
  fill: black,
)

#let highlighted = (
  ..base,
  fill: orange,
)
```

### 9.4 Function wrapper

```typst
#let my-box(..args) = {
  box(
    inset: 6pt,
    stroke: 0.5pt,
    ..args,
  )
}

#my-box(fill: luma(240))[Content]
```

---

## 10. Checklist

When using `..list` or `..value`, ask the following questions:

1. **What type is being spread?**
   - Array: expands into positional arguments or items.
   - Dictionary: expands into named arguments or key-value fields.
   - Arguments: can expand into both positional and named arguments.

2. **Is the surrounding context able to receive expanded items?**
   - Function call: yes.
   - Dictionary construction: yes.
   - Array construction: yes, depending on the intended structure.
   - Destructuring pattern: yes, but it collects rather than expands.
   - Plain content expression: usually no.

3. **Are duplicate dictionary keys possible?**
   - Later values override earlier values.

4. **Is this a one-element array?**
   - Use `(x,)`, not `(x)`.

5. **Is the dictionary made only from spreads?**
   - Use `(:..dict)` to force dictionary interpretation.

---

## 11. Summary

The Typst spread syntax `..value` is a compact mechanism for converting a container into separate arguments or items. Arrays spread into positional arguments, dictionaries spread into named arguments, and `arguments` values can carry both. The same symbol is also used in destructuring, where it collects remaining values instead of expanding them.

The key principle is simple:

> Use `..` only where Typst expects a sequence of arguments, items, fields, or destructured values. It is not a standalone expression.
