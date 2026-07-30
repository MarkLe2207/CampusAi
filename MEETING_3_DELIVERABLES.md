# CampusAI Meeting 3 Deliverables & Instructions

**Meeting 3 Date**: July 30, 2026 at 8:30 PM  
**Status**: Core deliverables defined, assignments clear

---

## 📊 Deliverable Overview

| Team Member | Role | Deliverable | Status | Priority |
|---|---|---|---|---|
| **Abrar** | Project Lead | FastAPI Backend + optional TTS/Avatar | ✅ DONE | - |
| **Mathew** | AI Research Lead | Knowledge Base + ChromaDB Setup | 🔄 IN PROGRESS | CRITICAL |
| **Syed** | UI/UX Lead | Next.js Frontend + Components | 🔄 IN PROGRESS | HIGH |
| **Mark** | Documentation Lead | Project Board + Finalize Docs | 🔄 IN PROGRESS | HIGH |
| **Nairobi** | QA & Presentation Lead | Project Charter + Slides | 🔄 IN PROGRESS | HIGH |

---

## ✅ ABRAR - PROJECT LEAD (COMPLETED)

### Deliverable: FastAPI Backend Implementation

**Status**: ✅ **COMPLETE** - Ready for integration

**What's Done**:
- ✅ 4 API endpoints fully implemented and tested
  - `POST /api/chat` - Chat interactions
  - `POST /api/query` - Knowledge base queries
  - `POST /api/feedback` - User feedback
  - `GET /api/conversations/{id}` - History
- ✅ ChatService with conversation tracking
- ✅ Error handling middleware
- ✅ Structured JSON logging
- ✅ 20+ unit tests created
- ✅ LLMService & RAGService scaffolds ready
- ✅ All code pushed to GitHub

**Commits Made**:
1. `feat(backend): implement FastAPI endpoints and chat service`
2. `feat(backend): add LLM and RAG service layers with tests`
3. `docs: update work log with completed backend implementation`

**Next Step**: Integrate with Mathew's ChromaDB + knowledge base

**Code Location**: `backend/app/api/routes.py`, `backend/app/services/`

---

## 🔄 MATHEW - AI RESEARCH LEAD (DUE JULY 30)

### Deliverable: Knowledge Base + ChromaDB Setup

**Priority**: 🔴 **CRITICAL** - Blocks Abrar's RAG integration

---

### Task 1: Finalize Official Sources Research

**What to Do**:
1. Review collected institutional information
2. Research official sources for:
   - Admissions requirements & process
   - Academic programs & majors
   - Tuition & financial aid information
   - Campus facilities & services
   - Student support services
   - Important dates & deadlines
   - Contact information for departments
3. Document all sources with URLs/citations
4. Ensure information is current (2026)

**Deliverable**: 
- Updated `knowledge/Centennial_College_Knowledge_Base.md` with comprehensive, sourced information
- Cross-reference all facts with official sources

**File Location**: `knowledge/Centennial_College_Knowledge_Base.md` (already has 82KB placeholder)

---

### Task 2: Build Knowledge Base

**What to Do**:
1. Structure knowledge base with clear sections:
   ```
   knowledge/
   ├── Centennial_College_Knowledge_Base.md (main)
   ├── departments/
   │   ├── engineering.md
   │   ├── business.md
   │   └── ...
   ├── programs/
   │   ├── full_time.md
   │   └── part_time.md
   ├── facilities/
   │   ├── campus_locations.md
   │   └── resources.md
   └── policies/
       ├── academic_policies.md
       └── student_conduct.md
   ```

2. Each file should have:
   - Clear headings and structure
   - Specific, factual information
   - Source attribution
   - Contact information where relevant

3. Make content **searchable** and **chunking-friendly** (max 500 words per section)

**Deliverable**:
- Well-organized knowledge base in Markdown format
- At least 3-5 department files
- At least 2-3 program descriptions
- Facilities and policies documentation

**File Location**: `knowledge/` directory

---

### Task 3: Set up ChromaDB Database

**What to Do**:
1. Install ChromaDB (already in requirements.txt)
2. Initialize ChromaDB instance with collection name: `college_knowledge`
3. Create script to:
   - Load knowledge base files
   - Generate embeddings using `sentence-transformers` (all-MiniLM-L6-v2 model)
   - Index documents into ChromaDB
4. Test retrieval with sample queries

**Expected Code Structure**:
```python
# backend/app/services/knowledge_loader.py (Abrar has scaffold ready)

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def load_and_index_knowledge_base():
    # 1. Load from knowledge/ directory
    # 2. Split into chunks
    # 3. Generate embeddings
    # 4. Store in ChromaDB at backend/chromadb_data/
```

**Deliverable**:
- Working ChromaDB instance with college knowledge indexed
- Test queries returning relevant documents (>80% accuracy)
- Ready for Abrar to wire into RAGService

**Database Location**: `backend/chromadb_data/`

---

### Task 4: Verify Retrieval Quality

**What to Do**:
1. Test ChromaDB with sample queries:
   - "What are the admissions requirements?"
   - "Tell me about engineering programs"
   - "What are the tuition costs?"
   - "How do I apply?"
2. Ensure top results are relevant (>80% accuracy)
3. Adjust chunking strategy if needed

**Deliverable**:
- Confirmation that retrieval works correctly
- Document any adjustments made

---

### Success Criteria for Mathew:

- ✅ Knowledge base files complete and organized
- ✅ ChromaDB initialized and indexed
- ✅ Retrieval tests passing (>80% relevant results)
- ✅ Files pushed to GitHub by July 30

### Files to Create/Modify:
- `knowledge/Centennial_College_Knowledge_Base.md` (expand/refine)
- `knowledge/departments/*.md` (create 3-5 files)
- `knowledge/programs/*.md` (create 2-3 files)
- `knowledge/facilities/*.md` (create at least 1)
- `knowledge/policies/*.md` (create at least 1)
- `backend/app/services/knowledge_loader.py` (Abrar scaffold ready - you implement)

---

## 🎨 SYED - UI/UX LEAD (DUE JULY 30)

### Deliverable: Next.js Frontend Implementation

**Priority**: 🟡 **HIGH** - Needed for E2E testing

---

### Task 1: Develop Frontend Layout & Components

**What to Do**:
1. **Create Chat Interface Component**:
   - Message display area (scrollable)
   - Input field for user messages
   - Send button
   - Loading indicator while waiting for response

2. **Create Response Display Component**:
   - Show AI response text
   - Display source citations (with links/titles)
   - Show confidence score (optional)

3. **Create Conversation History Component**:
   - List of past conversations
   - Ability to load previous conversations
   - Clear conversation option

4. **Create Layout Structure**:
   - Header with logo/title
   - Sidebar or navigation
   - Main chat area
   - Responsive design (mobile, tablet, desktop)

**File Structure to Create**:
```
frontend/
├── app/
│   └── chat/
│       └── page.tsx          # Chat page
├── components/
│   ├── ChatInput.tsx         # Message input component
│   ├── ChatMessage.tsx       # Single message display
│   ├── SourceCitation.tsx    # Citation display
│   ├── ConversationList.tsx  # Past conversations
│   ├── ResponseDisplay.tsx   # Response with sources
│   └── Layout.tsx            # Main layout wrapper
├── types/
│   └── chat.ts               # TypeScript interfaces
└── lib/
    └── api.ts                # Backend API calls
```

**Deliverable**:
- Functional chat UI (not connected to backend yet)
- Responsive layout
- TypeScript types defined
- Basic styling with Tailwind CSS

---

### Task 2: Create User Stories

**What to Do**:
1. Write user stories for core features:
   - "As a student, I want to ask questions and get instant answers"
   - "As a student, I want to see where information comes from"
   - "As a student, I want to continue previous conversations"
   - "As a student, I want to give feedback on responses"

2. Format:
   ```
   As a [user type], I want to [action], so that [benefit]
   
   Acceptance Criteria:
   - [ ] Criterion 1
   - [ ] Criterion 2
   - [ ] Criterion 3
   ```

3. Save in `docs/USER_STORIES.md`

**Deliverable**:
- 8-10 user stories covering MVP features
- Each with clear acceptance criteria
- Linked to frontend components

---

### Task 3: Test API Integration (Prep Work)

**What to Do**:
1. Create API utility file: `frontend/lib/api.ts`
2. Implement functions to call backend:
   ```typescript
   async function sendChatMessage(message: string)
   async function sendQuery(query: string)
   async function submitFeedback(responseId: string, rating: number)
   async function getConversationHistory(conversationId: string)
   ```
3. Handle loading states
4. Handle errors gracefully
5. Display responses from Abrar's API

**Deliverable**:
- API integration working (call /api/chat, /api/query, etc.)
- Error handling implemented
- Loading states functional

---

### Success Criteria for Syed:

- ✅ Chat UI components created
- ✅ Responsive layout implemented
- ✅ User stories documented
- ✅ API integration wired up
- ✅ Frontend pushed to GitHub by July 30

### Files to Create:
- `frontend/components/ChatInput.tsx`
- `frontend/components/ChatMessage.tsx`
- `frontend/components/SourceCitation.tsx`
- `frontend/components/ConversationList.tsx`
- `frontend/types/chat.ts`
- `frontend/lib/api.ts`
- `docs/USER_STORIES.md`

### Design Notes:
- Use Tailwind CSS for styling (already configured)
- Keep components reusable
- Follow TypeScript best practices
- Make it mobile-responsive

---

## 📚 MARK - DOCUMENTATION LEAD (DUE JULY 30)

### Deliverable: Project Documentation & Board Setup

**Priority**: 🟡 **HIGH** - Needed for organization

---

### Task 1: Set Up Project Board

**What to Do**:
1. **Choose Platform**: GitHub Projects (recommended) or Trello
2. **Create Columns**:
   - Backlog
   - In Progress
   - Review
   - Done
3. **Add All Tasks**:
   - Move completed items to Done (from Meeting 2 & now)
   - Add remaining Meeting 3 & Meeting 4 tasks
   - Assign owners to each task
   - Set due dates
4. **Create Milestones**:
   - Meeting 2 (July 27) ✅
   - Meeting 3 (July 30)
   - Meeting 4 (Early August)
   - Meeting 5 (Mid August)

**Deliverable**:
- GitHub Projects board (or Trello) fully set up
- All Meeting 2-3 tasks listed with status
- Team can see progress at a glance

**Platform**: Use GitHub Projects (integrated with repo)

---

### Task 2: Finalize PRD (Product Requirements Document)

**What to Do**:
1. Review current PRD (`docs/PRD.md`)
2. Expand with:
   - **User Personas**: Student, Staff, etc.
   - **User Journey Map**: From question to answer
   - **Feature Prioritization**: Must-have vs. nice-to-have
   - **Success Metrics**: How to measure success
   - **Constraints**: What's out of scope
   - **Timeline**: Milestones and deadlines
3. Ensure alignment with actual development
4. Get team sign-off

**Deliverable**:
- Complete, detailed PRD (3-5 pages)
- All features defined
- Success criteria clear

---

### Task 3: Finalize SRS (Software Requirements Specification)

**What to Do**:
1. Review current SRS (`docs/SRS.md`)
2. Add:
   - **Functional Requirements** (detailed):
     - API endpoints with parameters and responses
     - UI components and interactions
     - Data persistence
   - **Non-Functional Requirements**:
     - Performance (query <2s)
     - Scalability (support 100+ concurrent users)
     - Security (secure API calls)
     - Reliability (99% uptime during course)
   - **Technical Stack** (confirm):
     - Frontend: Next.js 14, TypeScript, Tailwind
     - Backend: FastAPI, Python
     - AI: Ollama, LangChain, ChromaDB
   - **API Specifications**: Full endpoint documentation
3. Link to actual API implementation

**Deliverable**:
- Complete SRS (5-8 pages)
- Technical requirements clear
- Testing strategy defined

---

### Task 4: Create API Documentation

**What to Do**:
1. Create `docs/API.md` with:
   - Base URL: `http://localhost:8000`
   - Authentication: None for MVP
   - Response format (standard)
   - All endpoints documented:
     - Request examples
     - Response examples
     - Error codes
2. Include cURL examples for testing
3. Link to Swagger docs: `/docs`

**Example Format**:
```markdown
## POST /api/chat

Send a chat message to the AI assistant.

### Request
```json
{
  "message": "What are admissions requirements?",
  "conversation_id": "optional-id"
}
```

### Response
```json
{
  "success": true,
  "data": {
    "response": "...",
    "sources": [...],
    "conversation_id": "..."
  }
}
```
```

**Deliverable**:
- Comprehensive API documentation
- Examples for all endpoints
- Error handling documented

---

### Success Criteria for Mark:

- ✅ Project Board (GitHub Projects) set up and populated
- ✅ PRD finalized and reviewed
- ✅ SRS finalized and reviewed
- ✅ API documentation complete
- ✅ All pushed to GitHub by July 30

### Files to Create/Modify:
- `docs/PRD.md` (expand existing)
- `docs/SRS.md` (expand existing)
- `docs/API.md` (create new)
- GitHub Projects board (link in README)

---

## 🎤 NAIROBI - QA & PRESENTATION LEAD (DUE JULY 30)

### Deliverable: Project Charter & Presentation Slides

**Priority**: 🟡 **HIGH** - Needed for final presentation

---

### Task 1: Finalize Project Charter

**What to Do**:
1. **Define Project Charter** with sections:
   - Project Title
   - Project Sponsor/Owner
   - Project Manager (Abrar)
   - Start Date & End Date (July 27 - August 10)
   - Objectives (from PROJECT_SOURCE_OF_TRUTH.md)
   - Success Criteria (MVP features delivered & working)
   - Scope (what's in/out)
   - Constraints (8-week course, team of 5)
   - Assumptions (Ollama available, internet access)
   - Risks & Mitigation
   - Budget/Resources (course project, no budget)
   - Stakeholders (Centennial College, instructors)

2. **Get Sign-Off**: Each team member reviews & approves

**Deliverable**:
- Formal Project Charter document (2-3 pages)
- Signed off by all team members
- Clear project boundaries

**File Location**: `docs/PROJECT_CHARTER.md`

---

### Task 2: Build Presentation Slides

**What to Do**:
1. **Create presentation** covering:
   - Slide 1-2: Title slide + team members
   - Slide 3-4: Problem statement & solution
   - Slide 5-6: Features & MVP scope
   - Slide 7-8: Technology stack with justification
   - Slide 9-10: Architecture diagram
   - Slide 11-12: Demo (live or video) of working app
   - Slide 13-14: Challenges & solutions
   - Slide 15: Accomplishments (what team achieved)
   - Slide 16: Future roadmap (post-course plans)
   - Slide 17: Q&A

2. **Design Guidelines**:
   - Use consistent branding (CampusAI)
   - Clean, professional design
   - Large readable fonts
   - Minimal text per slide
   - Include screenshots/diagrams

3. **Delivery**:
   - Time limit: 10-12 minutes + 3 min Q&A
   - Speaker notes for each slide
   - Practice timing

**Deliverable**:
- Presentation slides (PowerPoint, Google Slides, or PDF)
- Speaker notes for each slide
- Ready for final presentation (August 10)

**File Location**: `docs/PRESENTATION_SLIDES` (PowerPoint/PDF)

---

### Task 3: Prepare for Demo Day (July 30 Meeting)

**What to Do**:
1. Coordinate with team on **what to demo**:
   - Backend API endpoints (use Swagger or Postman)
   - Frontend chat interface
   - Integration with knowledge base
2. Create **demo script** (5-10 minutes):
   - "Here's a student asking about admissions"
   - Show AI response with sources
   - Show feedback submission
   - Show conversation history
3. Test demo thoroughly before meeting
4. Have **backup plan** if something fails

**Deliverable**:
- Working demo or demo video
- Clear demo script
- All team members know their part

---

### Task 4: QA Testing Plan (Start Now)

**What to Do**:
1. Create `docs/TEST_PLAN.md` with:
   - **Unit Tests**: API endpoints (Abrar's tests)
   - **Integration Tests**: Frontend + Backend
   - **E2E Tests**: Full user workflow
   - **Test Cases**:
     - Valid inputs → Expected outputs
     - Invalid inputs → Proper error messages
     - Edge cases (empty messages, very long queries)
2. **Testing Checklist**:
   - [ ] Backend starts without errors
   - [ ] All API endpoints respond correctly
   - [ ] Frontend loads and connects to backend
   - [ ] Chat workflow works end-to-end
   - [ ] Sources display correctly
   - [ ] Error handling works
   - [ ] Responsive design works on mobile/tablet/desktop

**Deliverable**:
- Test plan document
- Test cases documented
- QA checklist ready for final testing

**File Location**: `docs/TEST_PLAN.md`

---

### Success Criteria for Nairobi:

- ✅ Project Charter finalized & signed off
- ✅ Presentation slides completed (15-17 slides)
- ✅ Demo script written & tested
- ✅ Test plan documented
- ✅ All files pushed to GitHub by July 30

### Files to Create:
- `docs/PROJECT_CHARTER.md`
- `docs/PRESENTATION_SLIDES` (PowerPoint/PDF)
- `docs/TEST_PLAN.md`
- `docs/DEMO_SCRIPT.md` (optional)

### Presentation Tips:
- Tell a story (problem → solution → results)
- Show enthusiasm for the project
- Be ready to answer technical questions
- Practice beforehand

---

## 📅 TIMELINE - NEXT 3 DAYS (July 28-30)

### Day 1 (July 28) - NOW
- Abrar: ✅ Backend complete
- Mathew: Start knowledge base research
- Syed: Create component structure
- Mark: Refine PRD/SRS
- Nairobi: Draft slides & charter

### Day 2 (July 29)
- Mathew: Set up ChromaDB, index knowledge base
- Syed: Implement components, wire API
- Mark: Set up project board, finalize docs
- Nairobi: Finalize slides, prepare demo script
- Abrar: Integration testing, prepare for live demo

### Day 3 (July 30) - MEETING DAY
- **Morning**: Final testing by everyone
- **8:30 PM**: Live Meeting - Demo + Progress Update

---

## 📌 COORDINATION NOTES

**Blockers**:
- Mathew's work blocks Abrar's RAG integration
- Syed needs Abrar's API working (✅ DONE)
- All need each other for final integration testing

**GitHub**:
- All work must be pushed to master branch
- Clear commit messages required
- Link back to relevant tasks

**Communication**:
- Daily standup recommended (async via Slack)
- Flag blockers immediately
- Help each other when needed

---

## 🎯 FINAL CHECKLIST (July 30 Evening)

### Abrar (Project Lead)
- ✅ FastAPI Backend (COMPLETE)
- ✅ API endpoints tested
- ✅ Code pushed to GitHub
- ⏳ RAG integration ready (waiting for Mathew)

### Mathew (AI Research)
- ⏳ Knowledge base finalized & organized
- ⏳ ChromaDB initialized & indexed
- ⏳ Retrieval quality tested >80%
- ⏳ Code pushed to GitHub

### Syed (UI/UX)
- ⏳ Frontend components implemented
- ⏳ API integration working
- ⏳ User stories documented
- ⏳ Code pushed to GitHub

### Mark (Documentation)
- ⏳ Project board set up (GitHub Projects)
- ⏳ PRD finalized (3-5 pages)
- ⏳ SRS finalized (5-8 pages)
- ⏳ API documentation complete
- ⏳ All pushed to GitHub

### Nairobi (QA & Presentation)
- ⏳ Project Charter signed off
- ⏳ Presentation slides complete (15-17 slides)
- ⏳ Demo script tested
- ⏳ Test plan documented
- ⏳ All pushed to GitHub

---

## 💡 Key Success Factors

1. **Mathew's work is critical** - Start immediately if not done
2. **Integration testing** - Everything must work together
3. **Clear communication** - Flag blockers early
4. **Git discipline** - Commit frequently, clear messages
5. **Team support** - Help each other succeed

**Good luck! You've got this.** 🚀
