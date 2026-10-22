# Lean4Agent project website

Static project website for **Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards** and **Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory**, following the MA-LoT academic page layout.

`index.html` remains the default Lean4AgenticRL homepage; `lean4agent.html` presents Lean4Agent. A shared top navigation bar links between the two pages. Navigation uses ordinary links, with no JavaScript persistence or redirects.

## Preview and publish

From this directory, run:

```sh
python3 -m http.server 8000
```

Open [localhost:8000](http://localhost:8000) or [the Lean4Agent page](http://localhost:8000/lean4agent.html). No installation or build step is required. For GitHub Pages, publish the repository root from the desired branch; `.nojekyll` keeps the files served as a static site. Canonical and social-preview URLs assume `https://lean4agent.github.io/`.

## Files and editing

| File | Purpose |
| --- | --- |
| `index.html` | Default Lean4AgenticRL page: metadata, authors, teaser video, main results chart, achievements, methodology, and citation |
| `lean4agent.html` | Lean4Agent page: metadata, authors, narrative, main results, and citation |
| `static/css/index.css` | Shared page styling, project navigation, and mobile layouts |
| `static/css/bulma.min.css` | Local Bulma 0.9.1 base styles |
| `static/js/index.js` | Shared Copy BibTeX button with a selection fallback |
| `static/videos/Lean4AgenticRL-video.mp4` | Lean4AgenticRL teaser video, shown below the resource links with native playback controls |
| `static/images/ResultPlot.png` | Lean4AgenticRL main results chart and social preview |
| `static/images/MainPlot.png` | Lean4AgenticRL framework diagram from the research repository |
| `static/pdfs/paper.pdf` | Locally served Lean4AgenticRL paper |
| `static/images/lean4agent/MainPlot.png` | Lean4Agent framework diagram from its source repository |
| `static/images/lean4agent/MainResults.svg`, `MainResults.png` | Lean4Agent verification-results charts derived from paper Table 1 |
| `scripts/build_lean4agent_results.py` | Regenerates the Lean4Agent results charts with Python and Matplotlib |
| `static/pdfs/lean4agent.pdf` | Locally served Lean4Agent paper |
| `outputs/lean4agenticrl-teaser/` | Existing results workbook; retained separately from the page |

Edit the HTML and CSS directly, preview locally, then inspect desktop and mobile layouts before publishing. When results change, update the relevant table, result images, headline claims, and metadata together. Keep the existing workbook and result assets unless intentionally revising them. Python and Matplotlib are needed only to regenerate the Lean4Agent charts with `python3 scripts/build_lean4agent_results.py`, not to view the site.

## Structure and narrative

MA-LoT uses a hand-edited HTML/CSS workflow with `.nojekyll`, rather than a build pipeline. The pages retain the centered title and resource buttons, result figures, gray abstract band, illustrated methodology, and citation. A Goedel-Prover-style **Key Achievements** panel follows the abstract, with three metrics arranged horizontally on desktop and stacked on mobile. Unused template carousels and video dependencies are omitted. Lean4AgenticRL shows a responsive teaser video with native controls and inline mobile playback, followed by its main results chart. The video preloads only metadata and starts when the visitor presses play. Lean4AgenticRL includes Key Achievements without a separate Experimental Results section. Lean4Agent retains its **Main Results** table.

The narrative is: problem-specific workflows establish a plan; Lean4-based workflow formalization supports outcome, workflow-stage, and tool-call rewards; workflow-stage-normalized GRPO turns these signals into training for LAR-9B/27B. The abstract is approximately 127 words versus MA-LoT’s 178; methodology paragraphs are 57–64 words versus 57–159, keeping the text compact.

Lean4Agent uses the same concise page structure. Its narrative introduces FormalAgentLib's structural, static semantic, and trajectory verification, then LeanEvolve's workflow refinement from verification feedback. Its experiment section also contains main results only.

## Sources and interpretation

### Lean4AgenticRL

- The [research repository README](https://github.com/RickySkywalker/Lean4AgenticRL/blob/main/README.md) supplies the main-results table, evaluation settings, and citation. The [paper](static/pdfs/paper.pdf), especially Sections 2–3 and Appendix F, supplies methodology, authors, and the formal-verification boundary. Source assets are in the sibling `../Lean4AgenticRL/assets/` directory.
- Scores are reported research results. SWE-Bench-Verified uses **mean@3 with Claude-code**; TerminalBench-2.0/2.1 use **mean@5 with Terminus-2**. Best/second-best styling refers to the compared models of similar size. Missing scores remain unreported, not zero.
- The highlighted 77.3% versus 69.6% difference is **7.7 percentage points**, or **11.1% relative improvement**. Achievement rankings refer to the 27–31B models in the main-results comparison; the framework-first claim is qualified as “to our knowledge.” The source’s aggregate gains of 9.89% and 5.07% are omitted: simple averages of the rounded table entries give approximately 9.92 and 5.10 percentage points, respectively.
- Lean checks apply after workflow formalization, trajectory segmentation, and semantic annotation; those LLM-based steps are outside the formal guarantee.
- The homepage’s arXiv-labeled button currently links to the bundled paper PDF; Code links to the research repository; the Hugging Face button links to the user-provided [amazon/LAR-27B model repository](https://huggingface.co/amazon/LAR-27B). No arXiv identifier is provided for Lean4AgenticRL, so its citation remains a preprint entry.

### Lean4Agent

- Content and framework assets come from [the research repository snapshot](https://github.com/RickySkywalker/Lean4Agent/tree/e6a78cbe2c8b49e6784a4adcb4f682ed36de0f9a) (`e6a78cbe2c8b49e6784a4adcb4f682ed36de0f9a`) and [arXiv:2606.06523v2](https://arxiv.org/abs/2606.06523v2). The bundled paper supplies author names and affiliations: Ruida Wang, Jerry Huang, Pengcheng Wang, and Tong Zhang are at UIUC; Xuanqing Liu and Luyang Kong are independent researchers.
- Verification scores use a **50-problem hard subset of SWE-Bench-Verified** and a **100-question ELAIP-Bench subset**, averaged over three workflows in each verification group. The charts reproduce Table 1's model scores. The main-results table reports per-model scores; it omits the paper's inconsistent ELAIP difference entry and conflicting aggregate means.
- SWE LeanEvolve results reproduce Table 2's cumulative solved rates and include the pure-LLM evolution add-on. The headline gains of **14.80** (verification-passing versus failing SWE workflows) and **7.47** (additional SWE success with LeanEvolve) are paper-reported absolute **percentage-point** improvements, not relative percentages. Static semantic verification is conditional on the specified predicates and the `LLMExec` assumption.

## Attribution and license

Adapted from [MA-LoT](https://ma-lot.github.io/), [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template), [Nerfies](https://nerfies.github.io/), and [Goedel-Prover](https://goedel-lm.github.io/). Website content follows the reference page’s [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license; retain attribution when reusing it. The bundled Bulma stylesheet retains its MIT license notice. This website license does not change the licensing of the research paper, models, or research code.
