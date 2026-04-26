# OmniGuard Pitch Deck

**Slide 1: Problem**
- **Headline:** Creators lose ownership the moment content goes online.
- **Context:** Sports highlights, fan footage, and local tournament media are instantly copied, cropped, and monetized by aggregator pages without authorization.
- **Impact:** Small creators, student journalists, and grassroots leagues lose crucial revenue, visibility, and attribution.

**Slide 2: Why Current Systems Fail**
- **Too Slow:** DMCA takedowns take weeks.
- **Manual & Expensive:** Requires legal teams and manual searching.
- **Easy to Bypass:** Aggregators just crop, mirror, or filter the video to avoid standard hash detection.

**Slide 3: The OmniGuard Solution**
- **Real-time Media Authenticity:** AI-powered ownership protection.
- **How it Works:** 
  1. Extract structural data via AI Fingerprinting.
  2. Anchor proof of ownership to a lightweight Trust Registry.
  3. Instantly detect unauthorized, edited copies anywhere online.

**Slide 4: Live Demo**
- *Transition to Live App*
- Scenario: "I'm a student journalist." 
- Action: Upload `official_clip.mp4` -> Register Asset.
- Scenario: "An aggregator reposted my cropped clip."
- Action: Upload `stolen_edited_copy.mp4` -> Detect Misuse -> Show 98% Match and Original Owner!
- Share public verification link.

**Slide 5: Technical Architecture**
- **Frontend:** Next.js 14, Framer Motion, Tailwind (Glassmorphism UI).
- **Backend/AI:** FastAPI, `imagehash` (pHash) for structural robustness against compression/filters, OpenCV.
- **Persistence Layer:** Fast Local State & Trust Registry (Solidity Smart Contract).
- **Cloud Readiness:** Architected for Google Cloud Run and Vertex AI.

**Slide 6: Social Impact & Market Potential**
- **Democratizing Rights:** Protecting student journalists, women-led local tournaments, and independent videographers.
- **Scale:** High volume capability; local organizers can batch register full match media instantly.

**Slide 7: Vision**
- Today: Protecting grassroots sports media.
- Tomorrow: The global standard for decentralized media authenticity and automated revenue routing for small creators.
- **"OmniGuard: Keep what's yours."**
