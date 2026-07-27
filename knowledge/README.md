# Knowledge Base

This directory contains the official Centennial College information that will be used for the RAG (Retrieval-Augmented Generation) pipeline.

## Structure

```
knowledge/
├── README.md              # This file
├── college_info.json      # College general information
├── departments/           # Department information
├── programs/              # Program information
├── facilities/            # Campus facilities
└── policies/              # College policies
```

## File Formats

- **JSON**: For structured data (programs, departments, contacts)
- **Markdown**: For policy documents and guides
- **PDF**: Original source documents (will be converted to markdown)

## Knowledge Sources

Information will be collected from official Centennial College sources:
- Official website
- Student handbook
- Program guides
- Department websites
- College policies

## Adding Information

When adding new information:
1. Create appropriate directory if needed
2. Use clear, descriptive filenames
3. Format consistently (JSON or Markdown)
4. Include source attribution
5. Update this README

## RAG Integration

This knowledge base will be indexed by ChromaDB for semantic search during the RAG pipeline development phase.
