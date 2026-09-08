# Independent audit: k=17 v7 typed socket cascade and buffered compression

Date: 2026-08-01  
Verdict: **PASS in the theorem's stated finite and conditional scopes.**

Audited theorem:
`MATH_THEOREM_HA_K17_V7_TYPED_SOCKET_CASCADE_AND_BUFFERED_COMPRESSION_20260801.md`,
SHA-256
`99eff00fdf7d38f2b2fcd4084365ab9385609dd088d9d0a071ca9184b30ea402`.

## 1. Literal finite replay

The independent audit script
`scratch/audit_ha_k17_v7_typed_socket_cascade_20260801.py`, SHA-256
`6f729cf09d313336b346c7ede223fd49a7c22f3dd5f054819aced8fae028dd3e`,
replays the source TSV/JSON artifacts rather than reading theorem constants.
Its payload is
`scratch/ha_k17_v7_typed_socket_cascade_20260801.audit.json`, SHA-256
`9c3f4250a5406d4bf44c41e53a87dcd7a7cb9070988e1252342e20babfc26539`.

It verifies:

* 38 sockets, 6258 pieces and 24310 distinct owners;
* rank-ten raw/extendable zero counts 0/100;
* exactly 100 L3 rows, individual extra-cut sum 213, and the 99/1 child
  split with sole dependency 75749 -> 14309;
* all four published parent/child L3/L4 shared-facet pairings contain the
  same bounded coordinate-1024 run of length two;
* the canonical joined owner word has upper deck
  `75749,75749,14309,14309`, four distinct lower colours, and trace
  `0,1,1,0,1`;
* the fixed38 plus compatible-L5-child prepared selector has 200 candidate
  rows, 17 locally viable rows, 183 locally dead rows and 88 targets with no
  viable choice;
* an independent parser and unit propagator derives contradiction in the
  9094-variable, 41823-clause CNF.  The H100 Kissat transcript independently
  reports UNSAT with zero decisions and zero conflicts.

The prepared CNF SHA-256 is
`ec727c1df31765489f22fd959c9950e6e1e32e28c19428a45350dcd89a0951b8`;
the diagnostic TSV SHA-256 is
`4c121092176b4850b60c9a5336e9a367787397bcba5af1981238f6b6dbac7bfe`;
and the Kissat transcript SHA-256 is
`e38aed38f1e31ef76efb7d0e0d5f44078e311fb5dedc15587418cb5a5f68294c`.
The builder/solver ran only on H100 CPU under
`/home/amodo/or15/work/laneL_k17_v7_socket_selector_20260801`; the local
audit is a lightweight literal replay.

## 2. Mathematical audit

The following implications were checked independently.

1. Minimal casualty covers give exactly the provider-preservation clauses:
   any joint provider loss contains a minimal cover, while any selected
   minimal cover with no new provider creates a hole.
2. The head-partition/graphic common basis has full size exactly when it is
   a rooted dependency arborescence.  This validates the formal depth-two
   colour cascade but makes no physical claim.
3. At a shared facet, deduplicating the common owner gives junction run
   length `(h-p)+(g-q)-1`.  Thus only double omissions can introduce a new
   bounded run at one two-socket junction.  Pairwise omission-bank
   disjointness is not hereditary: three L3 blocks can place two zeros at
   global positions 1 and 5, creating a run of length3 across the middle
   block.  The corrected exact selector carries the full clipped suffix-age
   state and applies a position-specific Hall test at every reachable state.
4. The amalgamated extraction identity subtracts old internal edges once;
   for a two-regular equal-h chain it gives `2(h-1)T+2` cuts under the
   displayed retained-edge hypotheses.
5. Counting killed old colours against genuinely new target-coloured edges
   proves the sharpened cascade row

   \[
   |\Gamma_{\rm out}|\ge
   (m_{\mathcal T}-\mu-\rho-\tau_{\mathcal T}-\kappa)_+.
   \]

   Retained child-provider edges therefore save cuts but are not incorrectly
   counted as new repeated target edges.
6. Rado's theorem applies only after one common component/guard state has
   been fixed; the quantifier order `exists common state, for every target
   cut` is correct.  Marginal facet and guard Hall tests fail by the stated
   two-list XOR example.
7. Buffered compression is valid only with the theorem's corrected
   hypotheses: the bridge is itself internally resident, its full clipped
   relation composes, it has size O(d), and the compound cut union passes
   every provider-cover row with no undeclared typed child.
8. The hereditary theorem defines a positive-weight potential.  For
   beta=0, geometric summation gives the stated footprint.  For beta>0, the
   theorem explicitly assumes a terminal atlas below Phi_star and includes
   the finite stopping time L and its L beta cost.  The affine recurrence
   alone is not claimed to have finite cumulative cost.

## 3. Required scope qualifications

The finite UNSAT result is append-only for the frozen v7 bank and the
published two-choice target menu.  It does not exclude reselecting the old
38 sockets, new nonnested sockets, joint parent/child macros, or a nonflat
replay.

The pivot-rich geodesic packet is proved and available.  Its explicit
collar uses the sufficient ground-set condition `k>=r+3h`, which is false
for `(k,r,h)=(17,9,3)`, and its two outer boundary flags are clipped.
Therefore it supports the sufficiently-large regenerative template but is
not a finite k=17 bridge certificate.  It supplies one local candidate;
resource-disjoint availability of an entire bridge bank remains a separate
planting hypothesis.

The four rank-eleven extendable-seam zeros are not promoted to socket
obstructions: ranks eleven and above require accumulated-union replay.
Lower exactness, final topology, endpoint-fibre balance and one common
compiler cap remain open.
