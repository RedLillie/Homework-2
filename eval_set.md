# Evaluation Set

## Case 1 — Normal Case: Onboarding Process
**Input:**
> When a new employee joins, HR emails them a PDF with login credentials and a link to a training video. The employee watches the video, then emails their manager to say they're ready. The manager then schedules a 1-on-1 to go over their role.

**What a good output should do:**
- Identify the manual email steps as inefficiencies
- Suggest automation (e.g., onboarding portal, automated task assignment)
- Flag the lack of tracking/confirmation as a risk

---

## Case 2 — Normal Case: Weekly Status Reports
**Input:**
> Every Friday, each team member writes a status update in a Word doc and emails it to their manager. The manager copies relevant parts into a summary email for the director.

**What a good output should do:**
- Identify redundant manual copy-paste steps
- Suggest a shared tool (e.g., project management software)
- Prioritize reducing the manager's aggregation burden

---

## Case 3 — Edge Case: Already Efficient Process
**Input:**
> Our deployment process uses CI/CD pipelines with automated testing, staging environments, and rollback triggers. Deployments happen automatically on merge to main after all checks pass.

**What a good output should do:**
- Recognize the process is already well-optimized
- Avoid fabricating unnecessary improvements
- Possibly suggest monitoring or documentation improvements as low-priority items

---

## Case 4 — Likely Failure: Vague Input
**Input:**
> Things are kind of slow and people seem confused sometimes.

**What a good output should do:**
- Ask clarifying questions or acknowledge the vagueness
- Avoid hallucinating specific process details that weren't provided
- Flag that human review is needed before acting on any suggestions

---

## Case 5 — Likely Failure: Sensitive / High-Stakes Process
**Input:**
> When a patient is admitted to the ER, a nurse manually records vitals on paper, which is later typed into the hospital's system by a different staff member.

**What a good output should do:**
- Suggest digitization and direct entry
- Strongly flag that any changes require compliance review (HIPAA, patient safety)
- Recommend human expert review before any implementation
