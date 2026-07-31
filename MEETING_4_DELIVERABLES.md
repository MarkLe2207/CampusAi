# CampusAI Meeting 4 Deliverables & Instructions

**Meeting 4 Date**: August 2, 2026  
**Status**: In Progress  
**Theme**: Core AI integration goes live — CampusAI should actually answer questions by the end of this sprint.

---

## 📊 Deliverable Overview

| Team Member | Role | Deliverable | Priority |
|---|---|---|---|
| **Abrar** | Project Lead | LangChain + ChromaDB + Ollama RAG pipeline, `/api/chat` returns real answers | CRITICAL |
| **Mathew** | AI Research Lead | Finalize knowledge base accuracy, source metadata, retrieval QA | CRITICAL |
| **Syed** | UI/UX Lead | Real chat frontend connected to `/api/chat` | HIGH |
| **Mark** | Documentation Lead | Finalize PRD/SRS, create API.md, update board, start Final Report | HIGH |
| **Nairobi** | QA & Presentation Lead | Finalize Charter, 80% slides, Test Plan, demo script, start integration testing | HIGH |

**Dependency chain**: Mathew's knowledge base quality → Abrar's RAG pipeline → Syed's frontend demo → Nairobi's integration testing/demo. Mark's docs run in parallel but must reflect what's actually built by the end.

---

## 🧑‍💻 ABRAR — PROJECT LEAD / BACKEND INTEGRATION (YOU)

### Goal: Make CampusAI actually answer questions.

---

### Task 1: Integrate LangChain into the Backend

**What to Do**:
1. Wire `LangChain` into `backend/app/services/rag_service.py` (scaffold already exists from Meeting 3).
2. Replace placeholder logic with real LangChain components:
   - `RecursiveCharacterTextSplitter` for chunking (reuse Mathew's already-chunked files where possible)
   - `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`) for embeddings
   - `Chroma` vectorstore wrapper pointing at `backend/chromadb_data/`
   - `RetrievalQA` or `ConversationalRetrievalChain` for the actual Q&A chain
3. Keep prompt templates in a dedicated file (e.g. `backend/app/services/prompts.py`) rather than inline strings — easier for Mathew to tune later.

**Deliverable**: LangChain fully wired into `rag_service.py`, no more placeholder responses.

---

### Task 2: Load the Knowledge Base into ChromaDB

**What to Do**:
1. Implement `backend/app/services/knowledge_loader.py` (scaffold referenced since Meeting 3, not yet built):
   - Walk `knowledge/` directory (all `.md` files across `departments/`, `programs/`, `facilities/`, `policies/`, plus the main knowledge base file)
   - Chunk each doc, generate embeddings, upsert into Mathew's `centennial_knowledge_base` collection via `backend/init_chroma.py`'s client config
   - Attach metadata to each chunk (source file, section title) — this is what Mathew's "source metadata" work feeds into
2. Add a one-off script or CLI entry point to (re)run indexing on demand, e.g. `python -m app.services.knowledge_loader`
3. Confirm collection persists correctly in `backend/chromadb_data/` (already gitignored).

**Deliverable**: Running the loader populates ChromaDB with the full knowledge base, ready for retrieval.

---

### Task 3: Connect Ollama to the RAG Pipeline

**What to Do**:
1. Implement real Ollama calls in `backend/app/services/llm_service.py` (currently placeholder text).
2. Use the OpenAI-compatible endpoint at `OLLAMA_BASE_URL` (`config.py`, default `http://localhost:11434`) with model `OLLAMA_MODEL` (default `mistral`).
3. Keep the existing `is_available()` health check meaningful — return `False` gracefully if Ollama isn't running, so the API degrades instead of crashing.
4. No OpenAI fallback (per earlier decision — Ollama only).

**Deliverable**: `LLMService.generate_response()` returns real model output instead of the placeholder string.

---

### Task 4: `/api/chat` Returns Real AI Responses

**What to Do**:
1. Update `ChatService.process_chat_message()` to actually pass a real `RAGService` instance instead of `rag_service=None` (currently hardcoded in `routes.py`).
2. Instantiate `RAGService` + `LLMService` once (module-level or FastAPI dependency) and inject into `ChatService` calls in `app/api/routes.py`.
3. Verify multi-turn conversation history still works end-to-end with real responses.

**Deliverable**: A POST to `/api/chat` with a real student question returns a real, grounded answer.

---

### Task 5: Return Source Citations with Each Response

**What to Do**:
1. Use the metadata attached during indexing (Task 2) to populate the `sources` field in `ChatResponse` / `QueryResponse`.
2. Each source should include at least `title` and `excerpt` (matches existing `Source` schema in `app/schemas/chat.py`) — add `url`/section reference if Mathew provides it.
3. Confirm this lines up with Syed's "Verified Seal" citation UI concept from the Meeting 3 design system.

**Deliverable**: Every chat/query response includes real, traceable source citations — not placeholder text.

---

### Task 6: Basic Integration Tests

**What to Do**:
1. Extend `backend/tests/test_api.py` (or add `backend/tests/test_rag_pipeline.py`) with tests that exercise the real pipeline:
   - Knowledge base loads without errors
   - A known question returns a non-empty answer with at least one source
   - Ollama-unavailable case degrades gracefully (mock or skip if Ollama isn't running in CI)
2. Keep existing unit tests passing — they used `rag_service=None`, so confirm behavior didn't silently change for that path.

**Deliverable**: Test suite covers the real RAG path, not just the API contract.

---

### Success Criteria for Abrar:

- ✅ Backend answers real questions using the knowledge base (not placeholders)
- ✅ Swagger UI (`/docs`) demo works live — can type a question into `/api/chat` and get a grounded answer with sources
- ✅ Integration tests passing
- ✅ Code pushed to GitHub

### Files to Create/Modify:
- `backend/app/services/rag_service.py` (replace placeholders with real LangChain)
- `backend/app/services/llm_service.py` (real Ollama calls)
- `backend/app/services/knowledge_loader.py` (NEW — indexing pipeline)
- `backend/app/services/prompts.py` (NEW — prompt templates)
- `backend/app/api/routes.py` (wire real `RAGService`/`LLMService` into `ChatService` calls)
- `backend/tests/test_rag_pipeline.py` (NEW — integration tests)

---

## 📚 MATHEW — AI RESEARCH LEAD

### Goal: Ensure the knowledge base produces accurate answers.

---

### Task 1: Finish All Official Centennial Knowledge Files

**What to Do**:
1. Complete the department/program/facility/policy files started in the Meeting 3 restructure (PR #4).
2. Make sure every major student-facing topic has a file: admissions, tuition/financial aid, programs by school, campus locations/hours, key student services, important dates.
3. Cross-check facts against official Centennial College sources; flag anything time-sensitive (tuition, deadlines) as "verify before stating."

**Deliverable**: Knowledge base is complete enough to answer the majority of common student questions.

---

### Task 2: Add Source Metadata (Title/URL if Applicable)

**What to Do**:
1. For each knowledge file, add a small metadata header (or accompanying frontmatter) with at least: `title`, and `source_url` if the info came from a specific official page.
2. This metadata is what Abrar's `knowledge_loader.py` (Task 2 above) will attach to each indexed chunk — coordinate on the exact format (simple YAML frontmatter at the top of each `.md` file is easiest):
   ```markdown
   ---
   title: Admissions Requirements
   source_url: https://www.centennialcollege.ca/admissions/
   ---
   ```
3. Where no single official URL exists, use `source_url: internal` or omit it — don't fabricate a link.

**Deliverable**: Every knowledge file has clear title/source metadata ready for citation display.

---

### Task 3: Test at Least 20 Sample Questions

**What to Do**:
1. Once Abrar's indexing pipeline is up, run at least 20 realistic student questions through the system (via Swagger `/api/query` or `/api/chat`), e.g.:
   - "What are the admissions requirements for the Business program?"
   - "How much does tuition cost per semester?"
   - "Where is the Progress Campus located?"
   - "What support services are available for international students?"
2. Record each question + the answer + whether it was accurate/relevant in a simple table.

**Deliverable**: A documented test log of 20+ Q&A pairs with pass/fail notes.

**Suggested File**: `knowledge/RETRIEVAL_TEST_LOG.md`

---

### Task 4: Fix Missing or Inaccurate Knowledge

**What to Do**:
1. From the Task 3 test log, identify gaps (questions with no good answer) or inaccuracies (wrong info retrieved).
2. Add/correct the relevant knowledge files.
3. Re-run the failing questions to confirm the fix worked (may require Abrar to re-run the indexing loader).

**Deliverable**: Known gaps from testing are closed; knowledge base measurably improved.

---

### Task 5: Improve Chunking if Retrieval Quality is Poor

**What to Do**:
1. If Task 3 shows retrieval pulling irrelevant chunks, work with Abrar on chunk size/overlap tuning in the loader (`RecursiveCharacterTextSplitter` params), or restructure files so each section is more self-contained (avoid huge multi-topic sections).
2. Prefer smaller, focused files/sections over long documents — easier for the vector search to isolate relevant content.

**Deliverable**: Retrieval returns relevant chunks for the majority of test questions.

---

### Success Criteria for Mathew:

- ✅ Most common student questions return relevant, accurate information
- ✅ Every knowledge file has source metadata
- ✅ 20+ test questions logged with results
- ✅ Files pushed to GitHub

### Files to Create/Modify:
- `knowledge/**/*.md` (complete + add frontmatter metadata to all files)
- `knowledge/RETRIEVAL_TEST_LOG.md` (NEW — 20+ test Q&A results)

---

## 🎨 SYED — UI/UX LEAD

### Goal: Build the real frontend.

---

### Task 1: Chat Interface, Message Bubbles, Input Box, Loading Indicator

**What to Do**:
1. Implement the components specified in the Meeting 3 design doc (`frontend/Next.js Frontend Layout Components.md`, from PR #3) as real React/TypeScript components:
   - `ChatMessage.tsx` — message bubble (user vs. assistant styling, using the Ink Navy / Parchment / Paper White palette already defined)
   - `ChatInput.tsx` — input box + send button
   - A loading/typing indicator shown while waiting for the backend response
2. Assemble these into a chat page (e.g. `frontend/app/chat/page.tsx`).

**Deliverable**: A working, styled chat UI running locally via `npm run dev`.

---

### Task 2: Connect to `/api/chat`

**What to Do**:
1. Implement `frontend/lib/api.ts` with a function to call Abrar's live `/api/chat` endpoint (base URL from `NEXT_PUBLIC_API_URL`, already configured in `next.config.js`).
2. Send `{ message, conversation_id }`, handle the `ResponseModel` wrapper (`success`, `data`, `message`, `error`) already used by the backend.
3. Handle loading and error states (e.g. Ollama not running, network error) gracefully in the UI.

**Deliverable**: Typing a question in the browser and hitting send returns a real backend response.

---

### Task 3: Display Citations

**What to Do**:
1. Implement `SourceCitation.tsx` per the "Verified Seal" concept from the design doc — render the `sources` array returned in the chat response (title + excerpt at minimum).
2. Keep it visually distinct but not distracting from the main answer.

**Deliverable**: Each AI response visibly shows where its information came from.

---

### Task 4: Responsive Layout

**What to Do**:
1. Confirm the chat page works cleanly on mobile, tablet, and desktop breakpoints using Tailwind (already configured).
2. Test scroll behavior in the message list, and that the input box stays usable on small screens.

**Deliverable**: Chat UI is usable across device sizes.

---

### Success Criteria for Syed:

- ✅ User can ask a question from the browser and receive a real AI response with citations
- ✅ UI is responsive
- ✅ Code pushed to GitHub

### Files to Create/Modify:
- `frontend/components/ChatMessage.tsx`
- `frontend/components/ChatInput.tsx`
- `frontend/components/SourceCitation.tsx`
- `frontend/components/ConversationList.tsx` (if time permits — history view)
- `frontend/app/chat/page.tsx`
- `frontend/lib/api.ts`
- `frontend/types/chat.ts`

---

## 📄 MARK — DOCUMENTATION LEAD

### Goal: Finalize project documentation.

---

### Task 1: Finish PRD

**What to Do**:
1. Take the Meeting 3 draft (`docs/PRD.md`) and finalize it against what's actually being built this sprint: real RAG answers, citations, chat UI.
2. Make sure MVP feature list matches reality — no features listed that were descoped, no missing ones that got added.

**Deliverable**: Finalized `docs/PRD.md`.

---

### Task 2: Finish SRS

**What to Do**:
1. Finalize `docs/SRS.md` with confirmed functional + non-functional requirements.
2. Cross-check functional requirements against the actual `/api/chat`, `/api/query`, `/api/feedback` behavior once Abrar's integration lands.

**Deliverable**: Finalized `docs/SRS.md`.

---

### Task 3: Create API.md

**What to Do**:
1. Document all live endpoints in `docs/API.md`:
   - `POST /api/chat`, `POST /api/query`, `POST /api/feedback`, `GET /api/conversations/{id}`
   - Request/response examples (reuse the schema examples already in `backend/app/schemas/chat.py`)
   - Note the standard response envelope: `{ success, data, message, error }`
2. Link to the live Swagger docs at `/docs` for interactive testing.

**Deliverable**: `docs/API.md` accurately reflects the real, integrated API (not the stub version from Meeting 3).

---

### Task 4: Update GitHub Project Board

**What to Do**:
1. Move Meeting 3 items to Done, add Meeting 4 tasks (this doc) with owners and due date (Aug 2).
2. Keep board status in sync as tasks complete during the sprint.

**Deliverable**: Board reflects current sprint reality at all times.

---

### Task 5: Start Final Report

**What to Do**:
1. Create `docs/FINAL_REPORT.md` (or a shared doc) with a skeleton structure now, even if mostly empty:
   - Project summary, objectives, what was built, tech stack, team contributions, challenges, results, future work
2. Fill in sections as they become true (e.g. tech stack, team contributions can be written now).

**Deliverable**: Final Report skeleton exists and is partially filled in — ready to complete for Meeting 5.

---

### Success Criteria for Mark:

- ✅ Documentation matches the implemented project
- ✅ Board is current
- ✅ Final Report started
- ✅ Files pushed to GitHub

### Files to Create/Modify:
- `docs/PRD.md` (finalize)
- `docs/SRS.md` (finalize)
- `docs/API.md` (NEW)
- `docs/FINAL_REPORT.md` (NEW — skeleton)
- GitHub Projects board

---

## 🎤 NAIROBI — QA & PRESENTATION LEAD

### Goal: Prepare for demo day.

---

### Task 1: Project Charter Finalized

**What to Do**:
1. Finalize `docs/PROJECT_CHARTER.md` (started Meeting 3) — confirm scope, objectives, constraints, stakeholders all still match reality.
2. Get sign-off from all team members.

**Deliverable**: Signed-off, final Project Charter.

---

### Task 2: Presentation Slides (80% Complete)

**What to Do**:
1. Continue building the deck outlined in Meeting 3 instructions (problem, solution, features, stack, architecture, demo, challenges, roadmap).
2. Target 80% completion by Aug 2 — content mostly locked, demo section can stay flexible until closer to Meeting 5.
3. Coordinate with Abrar/Syed on what the live demo will actually show, so the slides match reality.

**Deliverable**: Slide deck ~80% complete, structurally done.

---

### Task 3: Test Plan

**What to Do**:
1. Create/finalize `docs/TEST_PLAN.md`: unit tests (Abrar's), integration tests (RAG pipeline + frontend), E2E workflow tests, edge cases (empty input, very long queries, Ollama down).
2. Include a manual QA checklist for demo readiness.

**Deliverable**: `docs/TEST_PLAN.md` complete and actionable.

---

### Task 4: Demo Script

**What to Do**:
1. Write a concrete demo script/`docs/DEMO_SCRIPT.md`: sample questions to ask live, expected answers, what to highlight (citations, responsiveness, etc.), fallback plan if something breaks live.

**Deliverable**: Demo script ready to rehearse against the real system.

---

### Task 5: Begin Integration Testing

**What to Do**:
1. Once Abrar's backend + Syed's frontend are connected, actually run through the full flow as a QA pass: ask real questions in the browser, verify answers + citations look right, log any bugs.
2. Feed findings back to Abrar/Mathew/Syed as needed.

**Deliverable**: A first round of integration test results, bugs filed/flagged.

### Success Criteria for Nairobi:

- ✅ Team can rehearse the presentation
- ✅ Test plan and demo script exist and are usable
- ✅ Integration testing underway with findings shared
- ✅ Files pushed to GitHub

### Files to Create/Modify:
- `docs/PROJECT_CHARTER.md` (finalize)
- `docs/PRESENTATION_SLIDES` (80% complete)
- `docs/TEST_PLAN.md`
- `docs/DEMO_SCRIPT.md`

---

## 📌 COORDINATION NOTES

**Critical Path**: Mathew's knowledge base metadata format (Task 2) must be agreed with Abrar early — it determines how citations get built. Talk to each other before either of you goes too far down your own path.

**Blockers to Watch**:
- Abrar's RAG pipeline needs Mathew's knowledge base to be reasonably complete to test against meaningfully — can start with what exists now and iterate.
- Syed's frontend needs Abrar's `/api/chat` returning real (not placeholder) responses to do meaningful integration testing — can build UI against the existing contract in the meantime.
- Nairobi's integration testing needs both Abrar and Syed's pieces connected — plan this for the second half of the sprint.
- Mark's API.md and Final Report should be written last, once behavior is confirmed, to avoid rework.

**GitHub**: All work on feature branches → PR → review → merge to master, same as Meeting 3. Clear commit messages required.

---

## 🎯 FINAL CHECKLIST (August 2)

### Abrar (Project Lead)
- [ ] LangChain integrated into backend
- [ ] Knowledge base loaded into ChromaDB
- [ ] Ollama connected to RAG pipeline
- [ ] `/api/chat` returns real AI responses
- [ ] Source citations returned with each response
- [ ] Basic integration tests passing

### Mathew (AI Research)
- [ ] All official Centennial knowledge files finished
- [ ] Source metadata added to knowledge files
- [ ] 20+ sample questions tested and logged
- [ ] Missing/inaccurate knowledge fixed
- [ ] Chunking improved if retrieval quality was poor

### Syed (UI/UX)
- [ ] Chat interface, message bubbles, input box, loading indicator built
- [ ] Connected to `/api/chat`
- [ ] Citations displayed
- [ ] Responsive layout confirmed

### Mark (Documentation)
- [ ] PRD finished
- [ ] SRS finished
- [ ] API.md created
- [ ] GitHub Project Board updated
- [ ] Final Report started

### Nairobi (QA & Presentation)
- [ ] Project Charter finalized
- [ ] Presentation slides ~80% complete
- [ ] Test Plan written
- [ ] Demo script written
- [ ] Integration testing begun

---

## 💡 Key Success Factors

1. **Talk before you build** — Mathew's metadata format and Abrar's loader need to match.
2. **Build against the real thing as soon as it exists** — Syed and Nairobi should switch from placeholders to real endpoints/answers as soon as Abrar's pipeline is live, not wait until the last day.
3. **Log everything you test** — Mathew's Q&A log and Nairobi's integration findings are what make Meeting 5 easy.
4. **Docs follow reality, not the plan** — Mark should write API.md and the Final Report against what's actually built.

**Let's make CampusAI actually talk.** 🚀
