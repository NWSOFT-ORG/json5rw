# `json5rw` - A JSON5 parsing tool

This tool supports loading and dumping JSON 5 content

## Supported syntax

Currently, the following are supported:

- Comments
    - `//`
    - `/**/`
- Different numerals
    - Hex (`0xABC`)
    - Int (`100`)
    - Float (`12.34`)
    - NaN (`NaN`, `nan`)
    - Infinity (`Infinity`, `-Infinity`)
- Trailing commas

*Note: Unquoted keys are not supported*