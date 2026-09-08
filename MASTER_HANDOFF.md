# Universal contiguous-subarray OR arrays: authoritative handoff

**Mathematical state and research record:** 2026-09-09. This document preserves
the self-contained finite and conditional proofs and records the September 8
coefficient improvements and proposed PBBS proof in Section 9. The active
research objective is the exact equality
\[
 \nu(k)=B(k)\qquad\text{for every }k\ge0.
\]
The September 8 manuscript concerns the separate asymptotic claim
\[
 \nu(k)=(1+o(1))W(k),\qquad W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]
That proposed asymptotic proof does not settle exact equality. The later
height-adaptive construction and period estimates in Sections 9.13–9.23
give stronger quantitative rates. The strongest internally reviewed
record, Section 9.23, has explicit relative error
\(\exp[-(93/100)(k(\log k)^2)^{1/5}]\) for
\(k\ge2^{131073}+1\), and three directly checked finite error certificates.
Section 9.24 now gives exact periods with nonprimitive rows and an
independently reproduced construction census through dimension101.
It also proves exponential additive overhead for the unchanged native
word and a complete obstruction to fusing its unchanged states at17.
Section 9.25 supplies uniform guarantees of 1%, 0.1%, 0.01% and 0.001%
from dimensions 29, 327, 1483 and 6849, respectively.
**Exact equality is now established through dimension20:** Sections9.26–9.27
record the optimal17/18 words, and Section9.31 records the supplied,
independently verified optimal19/20 words of lengths92,381 and184,759.
The19 cyclic minimum is also exactly92,378. The first unsettled case
is21, with endpoint target352,719. Section 9.28 records a valid forward-prefix bound method, while
its newly claimed 713-case numerical band awaits the actual certificates.
Section 9.29 reviews the stronger height-moment prefix method and records
an independently generated and completely replayed ten-parts-per-million
certificate at 137/138. The claimed 3,356-case band needed for the uniform
starting dimension137 has not been supplied or independently checked.
Section 9.30 records the optimal17 carrier's retained canonical matching,
the exact18 trace's complete insertion obstruction, and a stronger general
paired-endpoint theorem requiring4,859 exits and entrances per coordinate
at the exact19 target. These are constructive interfaces and necessary
conditions; they do not establish the all-dimensional equality objective.
The current
investigation is tracked in
[the exact-goal checkpoint](/Users/amir.nuriyev/Documents/problem/scratch/EXACT_B_GOAL_CHECKPOINT_20260909.md).

Tags mean **[I]** proved here, **[C]** proved here from the displayed
hypotheses, **[O]** open, and **[W]** an external finite word body whose
length, hash, encoding, verifier and matching internal lower bound are here.
No other file, checker, hash, conjecture, or archived branch is a premise of
an [I] or [C] claim. Skipped appendix numbers are deliberate.

The new record tags are **[R]**, a result checked through linked proof and
verification records, and **[P]**, a proposed proof with internal AI-agent
reviews. Neither tag promotes linked dependencies to [I]/[C] premises.
The coefficient-one [P] manuscript has not been externally reviewed or
formally verified; internal PASS labels are not human certification.

Current status:

- **[P], earlier proof route:** the PBBS manuscript claims
  \(\nu(k)=(1+o(1))W(k)\) for all ranks and every sufficiently large
  dimension. Its full consolidated argument is recorded in 9.2, with
  supporting lemmas and the internal review history. No gap was found
  in those reviews; it remains a proposed resolution. The later
  height-adaptive construction below does not use this proof chain.
- **[R]** The user's separate selective-truncation construction gives
  \(\nu(k)\le(1.177987+o(1))W(k)\). Geometry, padding, literal-word and
  analytic arguments passed internal review; the mask and exact rational
  certificate were reproduced on `h100`. See 9.1.
- **Comparison:** \(1.177987\), the earlier proposed \(1\), and the later
  height-adaptive coefficient \(1\) refer to the **same full-cube leading
  coefficient**. Sections 9.13–9.23 give internally reviewed finite
  routes to coefficient one with explicit quantitative errors. This still does
  not establish exact attainment of \(B(k)\).
- **[I]+[W]** \(\nu(k)=B(k)\) for \(0\le k\le20\); 2.1 records each decisive
  breakthrough.
- **[I]+[W], exact finite breakthrough:** \(\nu(17)=B(17)=24313\).
  The supplied optimal word passes complete suffix-OR enumeration,
  independent direct forward enumeration and all 131,071 range-OR witness
  checks. Its actual two-cycle opening and five join targets also pass.
  Section 9.26 and Appendix B record the word, hash and proof. This closes
  the previous 345-position gap independently of all PBBS asymptotics.
- **[I]+[W], exact finite breakthrough at 18:**
  \(\nu(18)=B(18)=48623\). The actual supplied word passes complete
  suffix enumeration, all 262,143 separate range-OR witness queries,
  and an independent first-occurrence census of 607,684 OR-change events.
  The analytic endpoint lower bound matches. Section 9.27 records the
  certificate and the exact initialized-state extension law.
- **[I]+[W], exact dimensions19–20:**
  \(\mu(19)=92378\), \(\nu(19)=B(19)=92381\), and
  \(\nu(20)=B(20)=184759\). Both additive gaps are zero.
  Independent forward and suffix enumerations cover all524,287 and
  1,048,575 targets; a separate range tree checks every saved witness.
  The19 cycle and its three-letter opening pass, and the20 word
  regenerates byte for byte by the periodic-core lift. Section9.31 and
  [the full exact record](K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md) supersede
  [the numerical comparison and certificates](FINITE_BOUNDS_K18_K19_K20_20260908.md).
- **[R], strongest current construction rate:** reciprocal-period charging
  and the sharp reverse-depth product give
  \(\nu(k)/W(k)\le1+\exp[-(93/100)(k(\log k)^2)^{1/5}]\)
  for every \(k\ge2^{131073}+1\). Section 9.23 records the finite
  inequality, full internal proof audits, and exact numerical certificates.
  Direct evaluation of that finite inequality also gives errors below
  \(10^{-330},10^{-950},10^{-2600}\) at the dimension pairs
  \(2\cdot10^{12}+1,+2\), \(2\cdot10^{14}+1,+2\), and
  \(2\cdot10^{16}+1,+2\), respectively. These pairs are not claimed
  to be thresholds for all larger dimensions.
- **[R], other new routes:** the depth-product coefficient \(3/5\)
  is in 9.21; the stopped-LCM alternative gives every fixed \(c<1/3\)
  on the same scale in 9.22. The fresh-prime route in 9.20 gives error
  \(e^{-k^{1/5}/128}\) already for every \(k\ge2^{2048}+1\).
  That weaker scale has a smaller certified starting dimension.
- **[R], exact finite construction evaluation:** Section9.24 gives
  \(\nu(101)\le199805614710856411551021117606<1.000006W(101)\),
  also the same relative bound at102. Exact integer checks give
  \(\nu(k)<1.01W(k)\) on29–102, \(<1.001W(k)\) on57–102,
  and \(<1.0001W(k)\) on87–102. These are individually checked
  finite ranges, not thresholds for every larger dimension. They
  use the retained finite support proof; no astronomical literal
  output was generated. At101 the construction is about5.9422parts
  per million above W, but still more than10^24positions above B.
- **[R], uniform finite thresholds:** Section 9.25 now proves
  \(\nu(k)<1.01W(k)\) for every \(k\ge29\),
  \(<1.001W(k)\) for every \(k\ge327\),
  \(<1.0001W(k)\) for every \(k\ge1483\), and
  \(<1.00001W(k)\) for every \(k\ge6849\). An exact 31-case finite
  band is joined to a proved decreasing analytic envelope. These are
  sufficient uniform thresholds, with the finite support premises retained.
- **[R], exact-construction limit:** the unchanged native height-adaptive
  word has collar cost \(C_n\ge\exp(n\log2-O(\sqrt n\log n))\).
  Sharper analysis of that same word cannot attain B(n). At17 the
  complete relevant graph of its native recency states has only17
  extra edges, all one-way from a153-cycle to an85-cycle. Its minimum
  cyclic routing count remains146. These statements concern the
  fixed construction/inventory, not unrestricted \(\nu(k)\).
- **[R], other reviewed routes:** the one-seventh profile sieve (9.15),
  multilevel joint-profile estimate (9.16), and fractional-LCM
  squared-logarithm estimate (9.18) also pass internal review. The last
  submission improves the joint-profile route, but is asymptotically
  weaker than the one-seventh and one-fifth bounds. Section 9.17 records
  the preceding first-moment one-fifth rate; 9.19 gains a further factor
  \(\log k\) in its exponent. Submission order
  must not be mistaken for strength order.
- **[R], earlier explicit period rates:** the same height-adaptive construction
  gives error \(\exp[-2^{-32}(\log k)^{6/5}]\) for
  \(k\ge\lceil e^{e^{256}}\rceil\). A separate fully explicit one-row
  bound gives relative error \(2\sqrt{2\pi}\,k^{-3/2}+O(k^{-2})\)
  and factors 1.01 for every \(k\ge5643\), 1.001 for every
  \(k\ge6255\). Section 9.14 records the proofs and exact arithmetic.
  The first estimate is asymptotically stronger; the second has useful
  finite thresholds. These use the finite corridor/pruning inputs, not
  the proposed clock/renewal coefficient-one proof.
- **Finite provenance:** the intermediate 24,660-word was not supplied.
  The later actual 24,658-word was supplied and independently passed
  complete verification; it supersedes both that claim and the verified
  24,668-word without requiring the intermediate search history.
- **[P]** The inverse-logarithmic argument has completed internal review:
  \(\nu(k)/W(k)\le1+2^{400000}(\log\log k)^{3/2}/\log k\)
  for \(k\ge\lceil\exp(\exp(4194304))\rceil\). Section 9.10 gives
  the explicit proof records and retains the finite PBBS dependency.
- **[I]** A.7 gives the full-cube bound
  \(\nu(k)\le(c_9+o(1))W(k)\), with the exact constant
  \(1.1807038038<c_9<1.1807038039<1.18071\).
  Nine balanced accumulators and an overlapping eight-axis staircase cover
  improve substantially on A.5B. This is the strongest upper bound with its
  complete proof embedded in the [I] core; the later [R]/[P] records are above.
- **[I]** the deterministic word of 3.5 gives
  \(\nu_h(2b)=(1+O((h+1)/\sqrt b))W(2b)\) for \(h=o(\sqrt b)\).
- **[I]** \(W(k)\le\mu(k)\le\nu(k)\le\mu(k)+(k-2)_+\).
- **[I]** \(\mu(5)=12\) by exhaustive enumeration, \(\mu(7)=35=W(7)\),
  and a width-length \(k=9\) cycle has exactly 12 holes.
- **[I]/[C]** 3.9 reduces coefficient one to near-width words with
  \(o(2^k)\) holes; I.7 correspondingly weakens the selector deficit.
  The user's sharper finite completion bound, with no dimension-only error
  floor for a linear base, is recorded in 9.3 [R].
- **[I]/[C]** 3.10 gives same-dimension facet-forest repair and an exact
  lower-compiler deficiency; 3.11 proves a prescribed Catalan matching
  extension and packet-owner avoidance; degree-two acyclicity remains open.
- **[I]** 3.12 quantifies the symmetry breaking required at \(k=17\).
- **[I]/[O]** C.5a replaces maximum-degree caps by an average-conflict cap;
  its bounded fourth-moment-scale adaptive test remains open.
- **[P]** full-cube coefficient one: proposed proof in 9.2, not promoted
  to a settled [I] theorem by the internal reviews.
- **[O]** Exact equality in every dimension; the first unsettled case is
  now \(k=21\), with target \(B(21)=352719\).
- **[R], exact construction audit:** every one of the 65,535 lower targets
  has an individual short cap host in the fixed capped PBBS bank. However,
  preserving every native H3 pair while freezing H1/H2 is impossible for
  a full cover: the exact low-target assignment maximum is 8,245 of 9,401.
  A 1,768-target Hall family has only 612 usable slots. The
  [host census](scratch/K17_CAPPED_PBBS_ALL_LOWER_TARGETS_INDIVIDUAL_HOST_CERTIFICATE_20260908.md)
  and [independently replayed Hall certificate](scratch/K17_CAPPED_LOW_TARGET_FLOW_HALL_OBSTRUCTION_20260908.md)
  show that the next construction must change this constraint. They do
  not rule out general short-interval caps or unrestricted exact equality.
- **[R], capped-bank follow-up:** allowing internal pairs to change
  while keeping full anchors at0,3,6,... gives individual hosts for
  every rank1–7target, but the exact simultaneous menu is impossible:
  4,441forced rank7placements and eight further implications leave
  target2103 without a host. The [replayed finite certificate](scratch/K17_CANONICAL_W3_ANCHOR_EIGHT_STEP_PROPAGATION_OBSTRUCTION_20260908.md)
  excludes this one anchor frame. A separate [directed-context port census](scratch/K17_CAPPED_RANK6_CONTEXT_PORT_CENSUS_20260908.md)
  found no cyclic fusion among74,562prescribed one-coordinate caps.
  Neither result excludes more general changes of states or sources.
- **[R]** Exact-construction progress is recorded in 9.4: a new 306-owner
  Johnson prefix preserves the complete proper upper support together
  with the remaining cycles. It is a component of a possible construction;
  these components do not themselves close the all-dimensional exact
  question. The later height-adaptive construction and period records in
  9.13–9.23 give the improved finite upper bounds and general rates.

The following three older conditional coefficient-one compiler branches
retain their own open gates; they are separate from the proposed PBBS route:
punctured \(A\to B\to4.4\); independent
\(C_{\rm F}\) or \(C_{\rm Q}\to3.4\); and DCC\(\to3.3\).
Their implications and bounded top-bit extensions are [C], but all four
named gates and a DCC construction itself are [O]. Section 3.4 eliminates
the old product-lift gate. The full Baranyai--Katona wreath conjecture is
not a premise; Appendix I's coherent-tour and packet routes bypass A and B.
Section 3.8 makes an unrestricted cyclic construction equivalent to the
linear problem up to \(O(k)\). Section 3.9 adds an architecture-free
almost-cover route using \(o(k)\) new coordinates. None supplies the open
near-width covering family or adaptive persistence theorem.

## 1. Problem and exact state model

Identify a bit mask with a subset of `[k]`. All witnessing intervals are
nonempty: `1<=i<=j<=n`. For a word

\[
A=(A_1,\ldots,A_n),\qquad
U(i,j)=\bigcup_{p=i}^j A_p,
\]

let `N(k)` be the least `n` for which every subset of `[k]`, including the
empty set, occurs as an interval union `U(i,j)`; its letters may be empty.
Let `nu(k)` be the analogous minimum when every letter and every required
target is nonempty. We set `nu(0)=0`, witnessed by the empty word.
Let \(\mu(k)\) be the least period of a nonzero cyclic set-word realizing
every nonempty subset by an interval of length at most one period.

### 1.1 Zero theorem

\[
                         N(k)=\nu(k)+1.
\]

If a nonempty target is witnessed by an interval, deleting every zero letter
inside the word compresses the surviving positions of that interval to a
contiguous interval with the same union.  Thus deleting all zero letters
preserves all nonempty targets. Any nonempty interval with empty union
contains an empty letter, so a full word has at least one zero position;
deleting all such positions leaves at most `N(k)-1` letters and proves
`N(k)>=nu(k)+1`. Conversely, prepending one zero to a shortest nonzero word
realizes the empty target without changing any old witness, proving the
reverse inequality. This also gives `N(0)=1`.

### 1.2 Move-to-front theorem

At a right endpoint `j`, group the coordinates already seen by equal
last-occurrence time, most recent first:

\[
P_j=(B_1,\ldots,B_t).
\]

The distinct suffix unions ending at `j` are exactly the prefix unions of
this ordered partition: extending a suffix leftward crosses the last-occurrence
classes in recency order, and every nonempty prefix is reached. Appending a
nonempty letter `X` makes the exact
transition

\[
(B_1,\ldots,B_t)\longmapsto
(X,B_1\setminus X,\ldots,B_t\setminus X),
\]

after empty blocks are deleted.  Indeed every coordinate of `X` acquires the
new common last-occurrence time, while the other coordinates keep their old
relative recency; this proves both the update and its converse.  Hence `nu(k)`
is the shortest walk starting at the empty ordered partition, using one
nonempty move-to-front update per letter, whose prefix unions cover the
nonempty Boolean lattice.

For a set sequence `X`, define

\[
(DX)_i=X_i\cup X_{i+1},\qquad
(D^qX)_i=\bigcup_{p=i}^{i+q}X_p.
\]

Every interval union is an entry of the derivative triangle
`A,DA,D^2A,...`.

Throughout,

\[
W(k)=\binom{k}{\lfloor k/2\rfloor},\qquad
[x]_+=\max(x,0),\qquad
\operatorname{Cat}_r={1\over r+1}\binom{2r}{r}.
\]

For an integer \(m\ge0\), the falling factorial is
\[
 (z)_m=z(z-1)\cdots(z-m+1),\qquad (z)_0=1.
\]

## 2. Sharp lower bound, finite theorem, and unconditional upper bounds

For `1<=s<=k`, put

\[
M_s=\binom ks,\qquad
\Lambda_s=\sum_{j=1}^{s-1}\binom kj,
\]

and let

\[
\tau_s=\min\left\{t\in\mathbb Z_{\ge0}:
\Lambda_s\le tM_s+\binom{t+1}{2}\right\}.
\]

Then

\[
\boxed{\nu(k)\ge B(k):=\max_{1\le s\le k}(M_s+\tau_s).}
\]

Set `B(0)=0`.

For `k>=1`, the maximum is attained at `s=ceil(k/2)`. Writing
`W=binom(k,ceil(k/2))` and

\[
d(k)=\min\left\{d\in\mathbb Z_{\ge0}:dW+\binom{d+1}{2}\ge
\sum_{j=1}^{\lceil k/2\rceil-1}\binom kj\right\},
\]

one has

\[
B(k)=W+d(k),\qquad d(k)=\sqrt{\pi k/8}+O(1).
\]

Here is the complete proof.  Choose one witness interval for every rank-`s`
target and order the resulting `M_s` intervals by left endpoint.  Two
distinct equal-rank witnesses cannot contain one another: containment of
intervals implies containment of their unions, and equal finite cardinality
would then force equality.  Their right endpoints therefore occur in the
same strict order.  If the word has length `M_s+t`, the `i`-th interval has
endpoints

\[
 [i+\alpha_i,i+\beta_i],\qquad
 0\le\alpha_i\le\beta_i\le t;
\]

the upper bounds follow because `M_s-i` later distinct endpoints must still
fit to its right.  Any interval of length at least `t+1`, starting at `a`,
contains the `a`-th chosen interval (necessarily `a<=M_s`).  A witness for a
target of rank below `s` cannot contain a rank-`s` witness, so it has length
at most `t`.  The number of such intervals is exactly

\[
 \sum_{j=1}^t(M_s+t-j+1)=tM_s+\binom{t+1}{2}.
\]

This proves the displayed lower bound.

It remains to justify the asserted maximizing rank.  Put

\[
 F_s=M_s(M_s+1)+2\Lambda_s.
\]

Since `\Lambda_{s+1}=\Lambda_s+M_s`, direct subtraction gives

\[
 F_{s+1}-F_s=(M_s+M_{s+1})(M_{s+1}-M_s+1).
\]

The adjacent ratio
`M_{s+1}/M_s=(k-s)/(s+1)` proves binomial unimodality. Therefore `F_s` is
maximal at
`s=ceil(k/2)` (for `k=2` there is an irrelevant tie).  If `N=W+d`, the
central defining inequality is exactly `N(N+1)>=F_{ceil(k/2)}`.  For any
other `s`, put `t=N-M_s`; then

\[
 tM_s+\binom{t+1}{2}
 ={N(N+1)-M_s(M_s+1)\over2}\ge\Lambda_s.
\]

Thus `M_s+\tau_s<=N`, proving the maximizer claim.  Finally, for
`m=ceil(k/2)`, symmetry gives

\[
 {\Lambda_m\over W}=
 \begin{cases}
 2^{k-1}/W-1/2+O(W^{-1}),&k\text{ even},\\
 2^{k-1}/W+O(W^{-1}),&k\text{ odd}.
 \end{cases}
\]

The internally proved estimate (A.2),
`W=2^k\sqrt{2/(\pi k)}(1+O(1/k))`, makes this
`\sqrt{\pi k/8}+O(1)`.  The quadratic term
is controlled noncircularly as follows: `d=ceil(\Lambda_m/W)` is admissible,
so the least `d` is `O(sqrt(k))`. Hence
`\binom{d+1}{2}=O(k)=o(W)` and it changes the least admissible integer by only
`O(1)`, proving `d(k)=\sqrt{\pi k/8}+O(1)`.

### 2.1 Exact finite values [I]+[W]

The lower bound is attained for every `0<=k<=20`:

| `k` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nu(k)` | 0 | 1 | 2 | 4 | 7 | 12 | 21 | 37 | 72 |

| `k` | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nu(k)` | 128 | 254 | 465 | 926 | 1719 | 3434 | 6438 | 12873 | 24313 |

At `k=18,19,20`, the exact values are respectively `48623,92381,184759`.
The cyclic value at19 is `mu(19)=92378`.

The historically decisive breakthrough for each closed dimension was:

| `k` | `nu(k)` | breakthrough that first closed the case |
|---:|---:|---|
| 0 | 0 | the empty word |
| 1 | 1 | the singleton word and the one-target bound |
| 2 | 2 | a direct two-letter construction and endpoint count |
| 3 | 4 | three singleton positions cannot realize all three two-sets |
| 4 | 7 | Sperner-equality rigidity forces one position beyond width |
| 5 | 12 | the odd two-middle-layer obstruction forces `W+2` |
| 6 | 21 | general Sperner-equality rigidity plus an attaining word |
| 7 | 37 | the odd two-middle-layer obstruction plus a graded word |
| 8 | 72 | the rank-count bound plus a graded fixed-window construction inspired by the `k=7` pattern |
| 9 | 128 | short-cell saturation forces `D^2A` to enumerate rank five; a compatible middle-level factor exists |
| 10 | 254 | a Johnson chronology with complete two-sided shadows and exact delay-two factor labeling |
| 11 | 465 | quotient SAT found a resident all-shadow voltage-two carrier; a safe cut and exact compiler completed it |
| 12 | 926 | one-hole recovery completed the 924-state central path and its natural factor |
| 13 | 1719 | two perfect carrier cycles were cut and joined by one Johnson seam; the compiler absorbed the lost boundary colour |
| 14 | 3434 | a six-piece odd-to-even `A/B` braid supplied exact depth-two residence and compilation |
| 15 | 6438 | resident cycles of lengths `6390+45`, an upper-safe nonrecycling seam, two boundary colours, and the generalized compiler |
| 16 | 12873 | after one singleton was pre-pinned, one common-cap SAT model assigned the remaining 26,331 lower targets injectively to short cells while enforcing a shared nonempty source letter at every position |
| 17 | 24313 | a changed middle-layer chronology supports two exact-width cycles of lengths 24,225 and 85; a joint opening uses three copied letters and the join supplies five otherwise missing targets; the literal word is independently verified |
| 18 | 48623 | the supplied literal shares initialization with an optimal17 seed; complete independent coverage checks and the endpoint lower bound establish exact attainment |
| 19 | 92381 | one width-length universal cycle; a triple-preserving compiler lets adjacent pairs supply smaller targets; a safe three-letter opening and independent full coverage checks attain the endpoint bound |
| 20 | 184759 | the verified19 periodic core supplies an initialized continuation; the general lift regenerates the supplied optimal20 word byte for byte, with complete independent target checks |

This table is historical provenance, not an extra lemma. Appendix B's [W]
words and the analytic lower bound uniformly verify its positive rows (the
empty word handles \(k=0\)); 2.3 independently removes [W] reliance at
\(k=7,8\). Historically, `k=12` closed before `k=11`.

Appendix B identifies the literal external word bodies by hash and contains
their exact recurrence verifier together with its proof. The words themselves
are the sole permitted self-containment exception [W]; all lower bounds and
all reasoning about them are internal.

For `k=17`,

\[
\boxed{\nu(17)=B(17)=24313.}
\]

The supplied optimal [W] word is identified in Appendix B and Section 9.26.
All 131,071 targets have independently checked ordinary interval witnesses.
The matching analytic lower bound is internal; no PBBS theorem is needed
for this equality. The previous upper words remain historical artifacts.

At `k=18`, the separately checked 48,623-letter word also attains the
internal endpoint lower bound. All 262,143 targets have ordinary interval
witnesses; see Section 9.27 and Appendix B. At19 and20 the supplied words
attain92381 and184759, with all524287 and1048575 ordinary witnesses
checked independently. Section9.31 records the cyclic core and lift.
Equality through20 does not establish an induction to every dimension.

### 2.2 Architecture-free constraints and upper bounds

For every coordinate set `Q`, deleting all letters meeting `Q` leaves a
universal word on `[k]\Q`. Indeed, a witness for a target disjoint from
`Q` contains no letter meeting `Q`; after all other letters are deleted, its
surviving positions remain consecutive and have the same union. Thus

\[
\#\{i:A_i\cap Q=\varnothing\}\ge\nu(k-|Q|),
\]

Summing over all `t`-sets `Q` counts position `i` exactly
`binom(k-|A_i|,t)` times and gives

\[
\sum_i\binom{k-|A_i|}{t}\ge\binom kt\nu(k-t).
\]

There is an overlap-sensitive top-bit splice. Let
\(A=(A_1,\ldots,A_n)\) be universal and suppose
\[
 A_i=A_{n-d+i}\quad(1\le i\le d),\qquad0\le d\le n/2.               \tag{2.1}
\]
For a new coordinate \(z\), the word
\[
 A_1,\ldots,A_n,\{z\},
 A_{d+1}\cup\{z\},\ldots,A_{n-1}\cup\{z\}                           \tag{2.2}
\]
is universal and has length \(2n-d\). Old targets remain. For
\(T\cup\{z\}\), choose an old witness \([i,j]\). If \(j=n\), use its suffix
and the bridge; if \(j<n,i>d\), use its lifted copy. If
\(i\le d<j<n\), use the equal terminal copy of \(A_i,\ldots,A_d\), the
bridge, and the lifted \(A_{d+1},\ldots,A_j\). If \(j=d\), use the equal
terminal suffix and bridge. If \(j<d\), shift the witness to
\([n-d+i,n-d+j]\subseteq[d+1,n-1]\) and use its lifted copy; the containment
uses \(n\ge2d\). The bridge realizes \(\{z\}\). This exhausts the cases.
Taking \(d=0\) proves, for \(k\ge2\), \(\nu(k)\le2\nu(k-1)\).

Every border satisfies
\[
                              d\le n-W(k).              \tag{2.3}
\]
Indeed (2.1) makes \(A\) a prefix of the period
\(C=(A_1,\ldots,A_{n-d})\), whose union is \([k]\). A proper target cannot
use more than one period, so every witness maps to a cyclic interval of
\(C\); hence \(C\) is cyclic universal and its \(n-d\) endpoints must
supply the \(W(k)\) middle targets. The literal \(k=16\) certificate has
no nonzero border, as the audit checks directly, so (2.2) gives only
\(25746\). Appendix B saves one position without a literal border.

The strongest unconditional full-cube asymptotic construction whose complete
proof is retained in the self-contained [I] core is

\[
\boxed{\nu(k)\le(c_9+o(1))W(k),\qquad c_9<1.18071.}
\]

Appendix A.7 contains the finite all-rank template, actual staircase chains,
balanced-accumulator analysis, all-dimension construction, and exact constant
evaluation. Every overlap, padding multiplicity, and closing cost is charged.
The older four-block construction and its strict switch improvement remain
proved in A.5 and A.5B, with coefficient \(c_4-\Delta_8<1.26946080564\).
The older \(\sqrt2\) construction in A.3 remains valid and supplies A.4's
far-rank repair. These constructions alone give no new finite optimum or
coefficient-one claim. Section 9 records the later user-supplied coefficient
\(1.177987\) [R] and the separate PBBS coefficient-one manuscript [P].

### 2.3 Cyclic finite certificates and safe erasure [I]

For \(k=7\), let
\[
 \rho(x)=((x\ll1)\mathbin{\&}127)\mathbin{|}(x\gg6),\qquad
 S=(3,5,64,20,36),
\]
and concatenate \(S,\rho(S),\ldots,\rho^6(S)\) as whole blocks. This
35-letter cycle is universal. Put
\(c(T)=\min_{0\le j<7}\rho^j(T)\). Here is a human-checkable orbit certificate;
starts are zero-based in \(S\), and each listed interval has a union in the
orbit of the corresponding canonical representative:

| rank | representatives | orbit witnesses \((\text{start},\text{length})\) |
|---:|---|---|
| 1 | \(1\) | \((2,1)\) |
| 2 | \(3,5,9\) | \((0,1),(1,1),(4,1)\) |
| 3 | \(7,11,13,19,21\) | \((0,2),(1,2),(3,2),(4,2),(2,2)\) |
| 4 | \(15,23,27,29,43\) | \((0,3),(4,3),(3,3),(2,3),(1,3)\) |
| 5 | \(31,47,55\) | \((3,4),(0,4),(2,4)\) |
| 6 | \(63\) | \((0,5)\) |
| 7 | \(127\) | \((1,6)\) |

Every nonempty proper subset has orbit seven, since seven is prime, and the
rank-orbit counts are \(1,3,5,5,3,1\). The table exhausts them; shifting a
witness five positions applies \(\rho\). Thus all 127 targets occur, while
the rank-three endpoint bound gives
\[
                              \boxed{\mu(7)=35=W(7).}                \tag{2.4}
\]

The construction illustrates a general safe-erasure rule. In a cyclic word,
choose pairwise nonadjacent positions \(i\) and delete
\[
 D_i\subseteq E_{i-1}\cap E_i\cap E_{i+1}
\]
from \(E_i\), leaving it nonempty. Every interval of length at least two
containing \(i\) contains an unmodified neighbor that still contains
\(D_i\); hence every such interval union is unchanged. The developed parent
seed \((3,5,68,20,36)\) covers all ranks at least two: the table's
rank-at-least-three witnesses have length at least two and are preserved
backward, while its rank-two orbits occur at unmodified seed positions
\(0,1,4\). At zero-based positions \(i\equiv2\pmod5\), delete the developed
copies of mask \(4\), changing \(68\) to \(64\).
The removed pair orbit remains at the unmodified copies of \(36\), since
\(\rho^4(36)=68\), while the new \(64\)-orbit supplies all singletons.

All table witnesses wrap by at most two positions. Appending \(3,5\) gives
a universal linear word of length 37 with border \((3,5)\); (2.2) then gives
a 72-letter word for \(k=8\). Thus this one internal certificate also
recovers \(\nu(7)=37,\nu(8)=72\).

There is also a computer-assisted exact result
\[
                              \boxed{\mu(5)=12}.                      \tag{2.5}
\]
The upper word is
\((1,4,17,24,18,1,2,4,16,12,10,8)\). For the lower bound, suppose a
length-11 cycle exists. Let \(p,q,b\) count letters of sizes \(2,1,\ge3\).
Every coordinate occurs as a singleton, so \(q\ge5\). Unless all letters
are singletons, let \(t\ge1\) count maximal singleton runs. Every rank-two
target is a pair letter or is witnessed by an adjacent change within one
singleton run, so there are at most
\[
 p+q-t=11-b-t
\]
of them. Covering all ten pairs forces \(b=0,t=1\) and equality throughout:
the singleton block is an edge-simple trail in \(K_5\), and the pair block
orders exactly its missing edges. Hence \(1\le p\le6\). Canonical
first-appearance renaming leaves respectively
\[
\begin{array}{c|rrrrrr}
p&1&2&3&4&5&6\\ \hline
\text{trails}&22&22&23&16&6&1\\
\text{mixed words}&22&44&138&384&720&720
\end{array}
\]
and none is universal. In the all-singleton case there are
246730 canonical surjections; 242 cover every pair and none is
universal. The complete exhaustive verifier is reproduced below. Repeating
a letter adjacently preserves every old cyclic interval union, so exclusion
at length 11 excludes every shorter length.

```python
from itertools import combinations, permutations
def U(w):
    out=set(); n=len(w)
    for i in range(n):
        x=0
        for j in range(n): x|=w[(i+j)%n]; out.add(x)
    return out
def rgs(n,p=(0,),m=0):
    if len(p)==n:
        if m==4: yield p
        return
    for x in range(min(m+1,4)+1):
        yield from rgs(n,p+(x,),max(m,x))
def edges(v,cyc=False):
    I=range(len(v)) if cyc else range(len(v)-1)
    return [tuple(sorted((v[i],v[(i+1)%len(v)]))) for i in I
            if v[i]!=v[(i+1)%len(v)]]
def rot(x,k): return ((x<<1)&((1<<k)-1))|(x>>(k-1))
def dev(s,k):
    out=[]
    for _ in range(k): out+=s; s=[rot(x,k) for x in s]
    return out
ALL=set(range(1,32)); E=set(combinations(range(5),2))
assert U((1,4,17,24,18,1,2,4,16,12,10,8))==ALL
tc=[]; cc=[]
for p in range(1,7):
    ts=[v for v in rgs(11-p)
        if len(edges(v))==10-p and len(set(edges(v)))==10-p]
    c=0
    for v in ts:
        for z in permutations(E-set(edges(v))):
            c+=1
            w=tuple((1<<a)|(1<<b) for a,b in z)+tuple(1<<a for a in v)
            assert U(w)!=ALL
    tc.append(len(ts)); cc.append(c)
assert tc==[22,22,23,16,6,1]
assert cc==[22,44,138,384,720,720]
n=q=0
for v in rgs(11):
    n+=1
    if set(edges(v,True))==E:
        q+=1
        assert U(tuple(1<<a for a in v))!=ALL
assert (n,q)==(246730,242)
A7=dev([3,5,64,20,36],7); assert U(A7)==set(range(1,128))
A9=dev([1,130,136,12,36,48,80,272,18,17,9,65,96,68],9)
assert sorted(set(range(1,512))-U(A9)) == [
  59,118,199,219,236,285,355,365,398,433,438,472]
```

The final assertion is a separate near-certificate. The displayed
14-letter seed developed as nine whole rotated blocks has length
\(126=W(9)\), realizes 499 of 511 targets, and has rank census
\[
                 9,36,84,126,117,81,36,9,1.             \tag{2.6}
\]
Its missing family is exactly the disjoint union of the size-nine orbit of
59 and size-three orbit of 219. It is not universal and does not improve
\(\nu(9)=128\). No optimizer, successor-switch, or SMT nonexistence claim is
a premise of these finite statements.

## 3. Exact compiler facts and the asymptotic reduction

### 3.1 Unrestricted interval normal form

Choose one interval `I_S=[ell_S,r_S]` for every nonempty target. The sets
with common left endpoint and those with common right endpoint form two
ordered inclusion-chain partitions. They are orthogonal and triangular.
Indeed, intervals with a common left endpoint are nested, so their unions
form an inclusion chain; the same holds at a common right endpoint. Two
distinct targets cannot have both endpoints equal, because one interval has
only one union, proving orthogonality. Along a left chain, larger targets have
larger right endpoints; along a right chain they have smaller left endpoints;
and every occupied pair satisfies `ell_S<=r_S`, proving the order and
triangularity assertions.

Conversely, index the two chain partitions by positions `p,q`, and give a
target belonging to their unique intersection the interval `[p,q]`.
Orthogonality makes these intervals distinct and triangularity makes them
nonempty. This prescribes witnesses, but realization has one additional exact
condition.  Put

\[
Z_x=[n]\setminus\bigcup_{S:x\notin S}I_S.
\]

The assignment is realized exactly when

\[
                 I_S\cap Z_x\ne\varnothing
                 \quad(S\ne\varnothing,\ x\in S).       \tag{3.1}
\]

Necessity is immediate: every occurrence of `x` must avoid every interval
whose target omits `x`, hence lies in `Z_x`, while a positive interval must
contain such an occurrence. For sufficiency set
`A_j={x:j\in Z_x}`. An interval whose target omits `x` contains no legal
position for it, while (3.1) supplies `x` to every interval requiring it.
Thus `\bigcup_{j\in I_S}A_j=S` for every target. Finally
`\bigcup_xZ_x=[n]` is exactly the condition that every letter be nonempty;
otherwise empty positions may be deleted without changing nonempty unions.

### 3.2 Flat central compiler

Fix a rank-`s` chronology `T=(T_1,...,T_W)` and depth `d`. A possibly empty
letter factor `A` with `D^dA=T` exists exactly when every internal run of
ones in every coordinate-incidence word of `T` has length at least `d+1`.
The maximal factor is

\[
A_j^{\max}=\bigcap_{\max(1,j-d)\le i\le\min(W,j)}T_i.
\]

To prove the criterion, work one coordinate at a time. Any occurrence at
position `j` lies in every `d+1` window whose union is one, so every factor
satisfies `A_j\subseteq A_j^{max}`. Conversely, a one in `T_i` is recovered
from the maximal factor precisely when some `j\in[i,i+d]` is contained in no
zero window. For an internal one-run `[p,q]` this requires and is implied by
`p+d<=q`, i.e. length at least `d+1`; prefix and suffix runs use the truncated
intersections and impose no length condition. Thus the maximal factor works
exactly under the stated run condition. Under that run condition, a factor
with no empty letters and the same length exists exactly when every
`A_j^{max}` is nonempty.

The exact lower-target compiler can also be stated without shorthand. Give
each desired lower target `S` a short interval `J_S\subseteq[W+d]`, and for
each coordinate `x` put

\[
E_x=[W+d]\setminus\bigcup_{i:x\notin T_i}[i,i+d],\qquad
Q_x=E_x\setminus\bigcup_{S:x\notin S}J_S.             \tag{3.2}
\]

The owner windows and assigned lower intervals are simultaneously realized
by a nonzero factor if and only if

\[
\begin{aligned}
J_S\cap Q_x&\ne\varnothing &&(x\in S),\\
[i,i+d]\cap Q_x&\ne\varnothing &&(x\in T_i),\\
\bigcup_xQ_x&=[W+d].
\end{aligned}                                        \tag{3.3}
\]

Necessity follows because a negative window or interval forbids `x`, whereas
each positive one must contain it. For sufficiency take
`A_j={x:j\in Q_x}`; (3.2) forbids every unwanted coordinate and (3.3)
supplies every required one. This is why an SDR ignoring the legal-position
sets `Q_x` is insufficient.

Upper targets have the following equally exact oracle. For a starting owner
`T_i`, define the first-arrival time

\[
\delta_i(x)=\min\{0\le q\le W-i:x\in T_{i+q}\},
\]

with value infinity when the set is empty. For a nonempty `S`, a consecutive
owner union is exactly `S` for some endpoint if and only if, for some `i`,

\[
       \max_{x\in S}\delta_i(x)
       <\min_{y\notin S}\delta_i(y).                 \tag{3.4}
\]

The minimum over an empty outside set is infinity.

Indeed, stop at the last first arrival among coordinates of `S`; (3.4) says
that every coordinate of `S` and no outside coordinate has appeared. The
converse is immediate from any witnessing run.

### 3.3 Defective central covering

Let `n=2m+1`, `W=binom(n,m)`, and

\[
H=\lceil\sqrt{n\log n}\rceil.
\]

A `DCC(n,H,delta)`, where `delta>=0`, is a cyclic singleton word of length at most
`(1+delta)W` such that

1. equal letters have cyclic distance at least `m+H+2`; and
2. the total number of rank-band targets not cleanly realized over ranks
   `m-H,...,m+1+H` is at most `delta W`.

A cyclic distance is the smaller number of index steps in the two directions
around the cycle between two occurrences.
A rank-`ell` target is *cleanly realized* when it is the union of a cyclic
window of exactly `ell` singleton positions whose labels are pairwise
distinct.

Linearize the cycle by writing one period followed by its first `m+H`
letters. This costs `O(n)` and retains every cyclic window of band length.
The gap condition makes each such window clean. Append one letter equal to
each missing band target (at most `delta W` letters), and then one letter per
nonempty far-rank target. Their exact number is one less than, and hence at
most,

\[
2\sum_{j=0}^{m-H-1}\binom nj
 \le 2^{n+1}e^{-2(H+1)^2/n}=o(W).
\]

For completeness, the tail inequality is elementary. If
`X~Bin(n,1/2)`, then

\[
\mathbb E e^{\lambda(X-n/2)}=
\bigl(\cosh(\lambda/2)\bigr)^n\le e^{n\lambda^2/8}.
\]

The last inequality follows because
`d(log cosh u)/du=tanh u<=u` for `u>=0` and both functions are even.

For `lambda<0`, on the event `X-n/2<=-a` one has
`exp(lambda(X-n/2))>=exp(-lambda a)`. Markov's inequality and
`lambda=-4a/n` therefore give
`Pr(X<=n/2-a)<=e^{-2a^2/n}`; take `a=H+1`. Also
`W>=2^n/(n+1)` because the largest of the `n+1` binomial coefficients is
at least their average. With `H=ceil(sqrt(n log n))`, the displayed tail
is therefore `o(W)`, and `O(n)=o(W)` as well. The final length is
`(1+2delta)W+o(W)`.

Therefore, if such a `DCC(n,H_n,delta_n)` exists for every sufficiently
large odd `n`, with `H_n=ceil(sqrt(n log n))` and `delta_n->0`, then

\[
\boxed{\nu(k)=(1+o(1))W(k).}
\]

Even dimensions follow from the internally proved top-bit splice and the
identity

\[
\binom{2m+2}{m+1}=2\binom{2m+1}{m};
\]

the lower bound gives the matching coefficient-one lower estimate. This
proves the boxed implication without any prime-gap input.

### 3.4 High OR-derivative compiler [I]/[C]

Let \(1\le\ell\le u\). Suppose a singleton source, read through
\(w_{L+u-2}\), has \(L\) consecutive designated starts
\(a=0,\ldots,L-1\), and every length-\(s\) window there is clean for
\(\ell\le s\le u\). Define the nonempty set-valued word
\[
 B_j=\{w_j,\ldots,w_{j+\ell-1}\},
 \qquad0\le j<L+u-\ell.
\]
Then, for every designated \(a,s\),
\[
 \boxed{\displaystyle
 \bigcup_{j=a}^{a+s-\ell}B_j
   =\{w_a,\ldots,w_{a+s-1}\}.}                         \tag{3.5}
\]
The blocks overlap consecutively and have first and last source indices
\(a\) and \(a+s-1\), proving the identity; the last word index is at most
\(L+u-\ell-1\). Thus one fragment compiles to exactly \(L+u-\ell\)
letters, with overhead \(u-\ell\).

For fragments with total designated-start count \(M\), number \(t\), and
\(h_s\) distinct rank-\(s\) targets missing from their designated windows,
concatenate the compiled blocks and append one set-valued letter per missing
or nonempty far-rank target. No witness crosses a join, so
\[
\boxed{\nu(n)\le M+(u-\ell)t+\sum_{s=\ell}^u h_s+
 \sum_{\substack{1\le s\le n\\s\notin[\ell,u]}}\binom ns.} \tag{3.6}
\]
The last sum may instead be replaced by the length of any word covering all
far-rank targets. This is the compiler used below.

### 3.5 Deterministic truncated-bridge band compiler [I]

Let \(\nu_h(2b)\) be the least length of a nonzero set-valued word covering
ranks \(b-h,\ldots,b+h\). For \(b\ge2\) and \(0\le h\le b-1\),
\[
\boxed{W(2b)\le\nu_h(2b)\le W(2b)+(2h+3)W(b-1)W(b)
      +2^{b-1}+W(b-1).}                                \tag{3.7}
\]
Consequently, uniformly for \(h=o(\sqrt b)\),
\[
 \nu_h(2b)=\left(1+O\!\left({h+1\over\sqrt b}\right)\right)W(2b).    \tag{3.8}
\]
Thus \(h=\lfloor\sqrt b/\log b\rfloor\) gives relative error
\(O(1/\log b)\). The word below is deterministic.

For a saturated chain \(E_0\subset\cdots\subset E_{m-1}\) in \(2^U\), let
\[
 \beta_U(E)=(E_0,E_1\setminus E_0,\ldots,
 E_{m-1}\setminus E_{m-2},U\setminus E_{m-1}),          \tag{3.9}
\]
omitting empty letters. Every \(E_i\) is a prefix union, every
\(U\setminus E_i\) a suffix union, and the bridge has at most \(m+1\)
letters. An empty prefix or suffix means that the interval starts or ends
at the adjacent bridge.

Split \([2b]=P_0\dot\cup\{z\}\dot\cup Q\), with
\(|P_0|=b-1,|Q|=b\), and put \(P=P_0\cup\{z\}\). Take SCDs
\(\mathcal C\) of \(2^{P_0}\) and \(\mathcal D\) of \(2^Q\); A.2 proves
their existence. Put \(A=|\mathcal C|=W(b-1)\), \(B=|\mathcal D|=W(b)\).
For chains \(C,D\) of lengths \(a,c\), define their rank-centered subchains
by
\[
 |C^D|=\min(a,c+2h+1),\qquad |D^C|=\min(c,a+2h+1).       \tag{3.10}
\]
Here \(a\equiv b\pmod2\) and \(c\equiv b+1\pmod2\), so the requested
lengths have the original parities and the centered subchains exist.

Every band target has unique owner chains. If \(z\notin S\), take
\(X=S\cap P\in C,\ Y=Q\setminus S\in D\); if \(z\in S\), take
\(X=P\setminus S\in C,\ Y=S\cap Q\in D\). Thus
\[
 S=X\cup(Q\setminus Y)\quad\hbox{or}\quad S=(P\setminus X)\cup Y.     \tag{3.11}
\]
Writing \(x=|X|-(b-1)/2,\ y=|Y|-b/2\), the two ranks are
\(b-\tfrac12+x-y\) and \(b+\tfrac12-x+y\). The band condition gives
\(|x-y|\le h+\tfrac12\). Since \(|y|\le(c-1)/2\),
\(|x|\le(c+2h)/2\), exactly the radius of a centered segment of length
\(c+2h+1\); symmetrically \(|y|\le(a+2h)/2\). Hence
\(X\in C^D,\ Y\in D^C\).

Order \(D_1,\ldots,D_B\) by nondecreasing length. For fixed \(C\), put
\(C_i=C^{D_i},E_i=D_i^C\). Then \(C_1\subseteq\cdots\subseteq C_B\).
Output
\[
 R_C=\beta_P(C_1),\beta_Q(E_1),\ldots,
      \beta_P(C_B),\beta_Q(E_B),\beta_P(C_B),           \tag{3.12}
\]
then concatenate the \(R_C\). In the second representation in (3.11), use
the suffix \(P\setminus X\) of \(\beta_P(C_i)\) followed by the prefix
\(Y\) of \(\beta_Q(E_i)\). In the first, use the suffix \(Q\setminus Y\)
of \(\beta_Q(E_i)\) followed by the prefix \(X\) of
\(\beta_P(C_{i+1})\); nesting permits this, and the final repeated bridge
handles \(i=B\). At least one piece is nonempty because \(|S|\ge1\).
Deleting empty bridge letters preserves contiguity, and no witness crosses
a row join.

Let \(L_h\) be this word's length. The longest right chain has length
\(b+1\), so \(C_B=C\). The bridge bound gives
\[
 L_h\le\sum_{C,D}\{\min(a,c+d)+\min(c,a+d)+2\}
          +\sum_C(a+1),\qquad d=2h+1.                  \tag{3.13}
\]
Now \(\sum_Ca=2^{b-1}\), and
\[
 \min(a,c+d)+\min(c,a+d)=2\min(a,c)+\min(|a-c|,d),
 \quad 2\sum_{C,D}\min(a,c)=W(2b).                    \tag{3.14}
\]
For the second identity, the rectangles \(C\times D\) partition
\(2^{P_0\cup Q}\); their rank-\((b-1)\) diagonal has \(\min(a,c)\)
members, so the sum is \(\binom{2b-1}{b-1}=W(2b)/2\). Therefore
\[
 L_h\le W(2b)+\sum_{C,D}\min(|a-c|,2h+1)
             +2AB+2^{b-1}+A.                          \tag{3.15}
\]
Capping by \(2h+1\) proves the upper bound in (3.7). The middle layer gives
the lower bound: unions of intervals ending at one position form a chain,
so one endpoint witnesses at most one \(b\)-target. Finally A.1 gives
\[
 {AB\over W(2b)}={1+O(b^{-1})\over\sqrt{\pi b}},\qquad
 {2^{b-1}+A\over W(2b)}=O(\sqrt b\,2^{-b}),            \tag{3.16}
\]
proving (3.8).

Choose chains uniformly from \(\mathcal C,\mathcal D\), with lengths
\(\mathsf A_b,\mathsf C_b\). The number of SCD chains of bottom rank \(i\)
is \(\binom ni-\binom n{i-1}\), so telescoping and adjacent-binomial products
give, with Gaussian-uniform tails,
\[
 \Pr(L_n\ge u)={\binom n{\lfloor(n+1-u)/2\rfloor}\over W(n)},\qquad
 {\mathsf A_b\over\sqrt b},{\mathsf C_b\over\sqrt b}
 \Longrightarrow X,Y,\quad \Pr(X>x)=e^{-x^2/2}.        \tag{3.17}
\]
Thus the limits are independent Rayleigh variables and uniformly integrable.
As \(|\beta_U(E)|=|E|+O(1)\), exact accounting in (3.13)--(3.15) gives
\[
 L_h=W(2b)+AB\,\mathbb E\min(|\mathsf A_b-\mathsf C_b|,2h+1)
       +O(AB+2^b).
\]
Together with (3.16) and integration of
\(\Pr(|X-Y|>u)=2\int_0^\infty ye^{-[y^2+(y+u)^2]/2}\,dy\), give
\[
 {L_h\over W(2b)}\longrightarrow
 F(c)=\sqrt2\,\operatorname {erf}(\sqrt2c)+e^{-c^2}\operatorname {erfc}(c)
 \quad(h/\sqrt b\to c).                               \tag{3.18}
\]
Here \(\operatorname {erf}(x)=2\pi^{-1/2}\int_0^xe^{-u^2}\,du\) and
\(\operatorname {erfc}=1-\operatorname {erf}\). Hence \(F(0)=1\),
\(F(c)>1\) for \(c>0\), and \(F(\infty)=\sqrt2\): this word's
coefficient-one range and A.4's cheap-repair range do not overlap.

### 3.5A Exact coverage and fixed-split completion barriers [I]

Let \(C_{b,h}(s)\) count rank-\(s\) targets realized by any interval of
(3.12). If \(h/\sqrt b\to c<\infty\) and
\(s=b+\lfloor t\sqrt b\rfloor\), then
\[
 {C_{b,h}(s)\over W(2b)}\to G_c(t):=
 \begin{cases}
 e^{-t^2},&|t|\le c,\\
 \operatorname {erf}(c)e^{-t^2}+e^{-c^2}\operatorname {erfc}(|t|),&|t|>c.
 \end{cases}                                           \tag{3.19}
\]
To census every interval, first discard the at most \(4\,2^b\) targets
empty or full in one half. Every remaining witness crosses exactly one
\(P\)-\(Q\) bridge boundary: staying in one bridge misses a half, crossing
two contains a complete intervening bridge, and containing any complete
bridge fills a half. A proper \(P\)-prefix omits \(z\), whereas every
nonempty \(P\)-suffix contains it; thus \(z\) fixes the orientation and
the two components fix their unique SCD owners. The \(P\)-to-\(Q\) boundary
gives one orientation of \(C_i\times E_i\); the reverse boundary gives the
other plus \((C_{i+1}\setminus C_i)\times E_i\). Per left chain there are \(O(b)\)
strict right-length jumps, each adding at most two left members, hence only
\(O(bW(b-1))=o(W(2b))\) extras at a fixed rank.

Under (3.17), set \(X_c=\min(X,Y+2c)\), \(Y_c=\min(Y,X+2c)\),
\(m=\min(X,Y)\), and \(d_c=\min(|X-Y|/2,c)\). Outside the band the two
rank diagonals have scaled length \(2(m+d_c-|t|)_+\), while
\(W(b-1)W(b)\sqrt b/W(2b)\to1/\sqrt\pi\). Thus
\[
 G_c(t)={2\over\sqrt\pi}\mathbb E(m+d_c-|t|)_+,\qquad
 \Pr(m+d_c>u)=e^{-u^2}\{e^{-c^2}+\sqrt\pi\,u\operatorname {erf}(c)\}
 \quad(u>c).
\]
Tail integration proves (3.19) outside the band; inside, exact coverage and
\(\binom{2b}{b+\lfloor t\sqrt b\rfloor}/W(2b)\to e^{-t^2}\) do. Moreover
the intended cells number \(2\sum_{C,D}|C^D||D^C|\); uniform Rayleigh tails
make all other cells negligible. Integrating
\(\min(x,y+2c)\min(y,x+2c)xy e^{-(x^2+y^2)/2}\) over \(x,y>0\) gives
\[
 P(c)={2\over\pi}\mathbb E(X_cY_c)
 =1-\operatorname {erfc}(c)^2+{2\over\pi}e^{-2c^2}
 -{2c\over\sqrt\pi}e^{-c^2}\operatorname {erfc}(c).    \tag{3.19a}
\]
Thus for \(h=o(\sqrt b)\), (3.12) covers \((2/\pi+o(1))4^b\) targets but
misses
\(\{e^{-t^2}-\operatorname {erfc}(|t|)+o(1)\}W(2b)\)
at Gaussian offset \(t\).

If a word misses \(m_s\) rank-\(s\) targets, any universal \(r\)-letter
append satisfies \(r\ge m_s\): each old miss newly witnessed has a new
right endpoint, whose nested suffix unions contain at most one rank-\(s\)
set. Consequently every append-only completion of (3.12) with
\(h=o(\sqrt b)\) has length at least
\[
 \{1+\eta_0-o(1)\}W(2b),\qquad
 \eta_0=e^{-1/\pi}-\operatorname {erfc}(1/\sqrt\pi)
       =0.3024398656\ldots,                            \tag{3.19b}
\]
because its derivative is \(2e^{-t^2}(1/\sqrt\pi-t)\). For general \(c\), put
\[
 D_c(t)=\operatorname {erfc}(c)e^{-t^2}-e^{-c^2}\operatorname {erfc}(t),
 \quad u(c)={e^{-c^2}\over\sqrt\pi\operatorname {erfc}(c)}>c.
\]
The derivative changes sign at \(u(c)\), and
\(2c\int_c^\infty e^{-v^2}dv<2\int_c^\infty ve^{-v^2}dv=e^{-c^2}\)
proves \(u(c)>c\). Thus it maximizes \(D_c\), so the
completion coefficient is at least \(F(c)+D_c(u(c))\). It increases since
\[
 {d\over dc}\{F(c)+D_c(u(c))\}
 ={4e^{-c^2}\over\sqrt\pi}\int_c^{u(c)}(v-c)e^{-v^2}\,dv>0.       \tag{3.19c}
\]

A wider barrier needs no SCD. Split \([2b]=P\dot\cup Q\), \(|P|=|Q|=b\),
and decompose a universal word into maximal alternating half-supported
blocks. If each block union is its whole half, then
\[
 N\ge W(b)(2^b-2)=(\sqrt2-o(1))W(2b).                 \tag{3.19d}
\]
Weight each target proper and nonempty in both halves by the number of
half-intersections of size \(\lfloor b/2\rfloor\); total required weight is
\(2W(b)(2^b-2)\). Its witness crosses exactly one boundary. At a boundary
between blocks of lengths \(a,c\), nested suffix/prefix unions supply weight
at most \(a+c\); every position meets at most two boundaries, proving
(3.19d). If instead every maximal block union has size at least
\(u>\lfloor b/2\rfloor\), restrict both half-intersections to
\(1,\ldots,u-1\); identically,
\[
 N\ge W(b)\sum_{j=1}^{u-1}\binom bj.                  \tag{3.19e}
\]
For \(u=\lfloor b/2\rfloor+H\), \(H/\sqrt b\to\infty\), this is
\((\sqrt2-o(1))W(2b)\). These results constrain only appends to (3.12) and
fixed-split blocks, not unrestricted \(\nu(2b)\) or mixed-support
fragments, tours, packets, or DCC.

Two earlier selector no-go results remain distinct. Equal use of \(L\)
targets at every band rank forces
\(Lt\le\binom{2b}{b-h}\le W(2b)e^{-h^2/(b+h)}\), so it covers \(o(W)\)
middle targets when \(h/\sqrt b\to\infty\). Rank-balanced quotas do not
validate independent half-retention: if also \(h/L\to0\) and
\(h+L\le b+1\), the ranks \(|s-b|\le\sqrt b/4\) require at least \(7L/8\)
of \(L\) independent retained targets. One fragment succeeds with
probability \(e^{-\Omega(L\sqrt b)}\), whereas there are at most
\(W(2b)b^{2(h+L-1)}=e^{o(L\sqrt b)}\) supports. A union bound leaves none
with high probability. This excludes only that independent-residual model.

### 3.6 Architecture-free adjacent shadows and a GK-block obstruction [I]/[C]

Let \(b\ge2\), \(W=\binom{2b}b\),
\(M=\binom{2b}{b-1}=\binom{2b}{b+1}\), and
\(\Delta=W-M=W/(b+1)\). Suppose a word of length \(N=W+t\) realizes ranks
\(b-1,b,b+1\). Choose one interval \(I_i=[\ell_i,r_i]\) for each middle
target \(T_i=U(I_i)\), ordered by left endpoint. Equal-rank witness intervals
cannot contain one another, so both endpoints are distinct and
\(r_1<\cdots<r_W\). Close the order cyclically and let

\[
 \mathcal S_-=\{T_i\cap T_{i+1}:|T_i\cap T_{i+1}|=b-1\},\quad
 \mathcal S_+=\{T_i\cup T_{i+1}:|T_i\cup T_{i+1}|=b+1\},             \tag{3.20}
\]
where supports, not occurrences, are counted, and put
\(h_\pm=M-|\mathcal S_\pm|\). Then
\[
                         \boxed{h_-\le2t,\qquad h_+\le2t.}             \tag{3.21}
\]

Indeed the \(W\) central left endpoints and the \(W\) central right
endpoints each omit exactly \(t\) word positions. Choose witnesses for all
lower targets. Their left endpoints are distinct, as are their right
endpoints, so all but at most \(2t\) have the form
\(J=[\ell_j,r_i]\). Necessarily \(j>i\), since otherwise \(J\supseteq I_i\);
hence \(J\subseteq I_i\cap I_{i+1}\) and its union is exactly
\(T_i\cap T_{i+1}\). For an upper target the same argument gives \(j<i\):
\(J\) contains \(I_j,I_{j+1}\), so its union is
\(T_j\cup T_{j+1}\). These are linear adjacent pairs; adding the cyclic pair
can only enlarge the supports, proving (3.21).

If \(J_1\) is the number of cyclic Johnson-distance-one transitions, then
\[
 (W-J_1)+(J_1-|\mathcal S_\pm|)
   =\Delta+h_\pm\le\Delta+2t.                         \tag{3.22}
\]
Thus every coefficient-one word forces \(o(W)\) non-Johnson transitions,
missing adjacent targets, and excess repeated shadow occurrences in every
chosen middle-witness chronology.

Conversely, take any cyclic middle ordering and put
\(A_i=T_i\cap T_{i+1}\). Use the finite word
\(A_1,\ldots,A_W,A_1,A_2\), deleting empty letters. Define
\[
 B=|\{i:T_i\not\subseteq T_{i-1}\cup T_{i+1}\}|.                     \tag{3.23}
\]
The letters realize \(\mathcal S_-\). At every other owner,
\(A_{i-1}\cup A_i=T_i\). If consecutive owners are both good, their three
letters unite to \(T_i\cup T_{i+1}\); hence at most \(2B\) distinct upper
shadow colors can fail. Deleting empty letters preserves every nonempty
interval union. Appending the missing lower, middle, and upper targets gives
\[
 \nu_1(2b)\le W+2+h_-+h_++3B.                         \tag{3.24}
\]
Put \(q=W-J_1\). At most \(2q\) owners touch a non-Johnson transition. At
every remaining bad owner the two adjacent \((b-1)\)-shadows are equal,
since two distinct \((b-1)\)-subsets of \(T_i\) unite to \(T_i\). Along the
Johnson runs, equal-color adjacencies number at most
\(J_1-|\mathcal S_-|+1\); the \(+1\) covers the single cyclic run. Therefore
\[
 B\le2q+J_1-|\mathcal S_-|+1
   \le2(\Delta+h_-)+1,                                \tag{3.25}
\]
and
\[
 \boxed{\nu_1(2b)\le W+7h_-+h_++6\Delta+5.}           \tag{3.26}
\]
Consequently three-rank coefficient one is equivalent to the existence of
a cyclic middle ordering with \(h_-+h_+=o(W)\).

One natural recursive symmetric-chain chronology fails this criterion.
Take an SCD on \(2b-2\) coordinates. A nontrivial parent has fixed-one set
\(F\), \(|F|=b-1-a\), and free coordinates \(v_1,\ldots,v_{2a}\), \(a\ge1\).
After adjoining \(\alpha,\beta\), suppose its four middle descendants occur
consecutively, in the displayed order or its reversal:
\[
\begin{aligned}
T_0&=F\cup\{\alpha,v_1,\ldots,v_a\},&
T_1&=F\cup\{v_1,\ldots,v_{a+1}\},\\
T_2&=F\cup\{v_1,\ldots,v_a,\beta\},&
T_3&=F\cup\{\alpha,v_1,\ldots,v_{a-1},\beta\}.
\end{aligned}                                                       \tag{3.27}
\]
Then
\[
 T_0\cap T_1=T_1\cap T_2=F\cup\{v_1,\ldots,v_a\}.                  \tag{3.28}
\]
There are \(P=\binom{2b-2}{b-2}\) nontrivial parents, since each meets rank
\(b-2\) exactly once. Their forced equal-color transition pairs are
position-disjoint, so \(J_1-|\mathcal S_-|\ge P\), whence
\[
 h_-\ge P-\Delta,\qquad
 N\ge W+\tfrac12[P-\Delta]_+.                         \tag{3.29}
\]
As
\[
 {P\over W}={b-1\over2(2b-1)}\to{1\over4},\qquad
 {\Delta\over W}\to0,
\]
every word whose selected middle chronology has these consecutive blocks
satisfies \(N\ge(9/8-o(1))W\). Replacing \(m\) cyclic adjacencies can enlarge
either distinct shadow support by at most \(m\), so \(o(W)\) changes do not
remove the obstruction. The known recursive Hamilton extension of the
Greene--Kleitman SCD uses these blocks, but the internal result is only about
this chronology class, not arbitrary SCD-containing Hamilton cycles or
unrestricted \(\nu(2b)\).

### 3.7 Union recoding and cumulative difference cycles [I]

For a word \(A\), let \(\mathcal U_s(A)\) be its distinct rank-\(s\)
interval unions. Replace pairwise disjoint old intervals by nonzero words
of lengths \(m_1,\ldots,m_t\), each having the same union as the old block,
and call the result \(B\). Then
\[
 |\mathcal U_s(B)\setminus\mathcal U_s(A)|
 \le2J,\qquad J=\sum_i(m_i-1).                         \tag{3.30}
\]
Indeed call a cut of \(B\) inherited unless it is strictly internal to a
replacement. An interval bounded by inherited cuts maps order-preservingly
to an old interval with the same union. Every new target therefore starts
or ends at one of the \(J\) new cuts. Unions with a fixed left or right
endpoint are nested, so each endpoint supplies at most one rank-\(s\) set.
Thus disjoint union-preserving two-letter recodings create at most \(2t\)
new targets per rank. If each old letter is instead refined into a block
whose union is that letter and \(R=\sum(m_i-1)\), then at most \(2R\) new
rank-\(s\) targets arise. In particular the rank deficit (3.19b) requires
\[
                         R\ge\tfrac12\eta_0W(2b)-o(W(2b)).           \tag{3.31}
\]
This is a letterwise-refinement bound, not a bound on global reorderings or
on arbitrary block recoding measured only by net length change.

A different obstruction comes from difference universal cycles. Put
\(M=2r+1\), \(L=\binom{2r}r\), and let \(\mathcal E\) contain all positive
\(r\)-tuples of sum at most \(2r\). Such tuples are the edges, from prefix
to suffix, of the directed overlap graph on positive \((r-1)\)-tuples of
sum at most \(2r-1\). A vertex of sum \(q\) has indegree and outdegree
\(2r-q\). Appending ones reaches the all-one vertex; conversely, appending
the entries of any target vertex reaches it from all ones, and every
intermediate edge has sum at most \(2r\). Thus the graph is strongly
connected, and the Euler argument in A.3 supplies a cyclic word
\(\delta_0,\ldots,\delta_{L-1}\) containing every member of \(\mathcal E\)
once as an \(r\)-window. Partial sums biject \(\mathcal E\) with
\(\binom{[2r]}r\), so \(|\mathcal E|=L\).

Define \(a_0=0\) and \(a_{i+1}=a_i+\delta_i\pmod M\). Each symbol occurs in
\(r\) tuple windows, while a tuple's sum is the maximum of its associated
\(r\)-subset of \([2r]\). Hence
\[
 r\sum_i\delta_i
 =\sum_{m=r}^{2r}m\binom{m-1}{r-1}
 =r\binom{2r+1}{r+1},\qquad
 \sum_i\delta_i=M\operatorname {Cat}_r.                \tag{3.32}
\]
The cumulative singleton word therefore closes cyclically. Any forward sum
of at most \(r\) consecutive differences lies in \([1,M-1]\), so every
\(r+1\) consecutive labels are distinct.

There is an exact cycle-independent inventory. For an \(s\)-set
\(S\subseteq\mathbb Z_M\), \(1\le s\le r+1\), let
\(g_1,\ldots,g_s\) be its positive cyclic gaps and
\(h(S)=|\{z:S+z=S\}|\). Then
\[
 \boxed{\#\{i:\{a_i,\ldots,a_{i+s-1}\}\in\{S+z:z\in\mathbb Z_M\}\}
 ={1\over h(S)}\sum_{j=1}^s\binom{g_j-1}{r-s+1}.}       \tag{3.33}
\]
Root \(S\) at the point preceded by a gap \(g_j\). Its first \(s-1\)
differences are fixed and sum to \(M-g_j\); the remaining
\(r-s+1\) positive entries may sum to at most \(g_j-1\), giving the displayed
binomial. Every completed tuple occurs once, and the \(s\) roots count each
distinct rooted representation exactly \(h(S)\) times. For \(s=r,r+1\),
\(\gcd(M,s)=1\), so \(h(S)=1\), and (3.33) equals \(r+1\) for every
translation orbit. This regularity counts occurrences, not distinct phases,
and does not produce two complementary central supports. Exactly,
\[
                        2L=(1+1/M)W(M),                \tag{3.34}
\]
and retaining cyclic central windows after linearization costs only \(O(r)\);
this is a capacity observation, not a construction.

For \(s=r-d\), (3.33) is nonzero only if some \(g_j\ge d+2\), i.e. \(S\)
has \(d+1\) consecutive absent coordinates. This governs every rank-\(s\)
interval, not only designated windows: an interval longer than \(s\) contains
\(s+1\le r+1\) distinct labels, while a shorter one cannot have rank \(s\).
The eligible fraction is therefore at most
\[
 M{\binom{M-d-1}s\over\binom Ms}
 \le M\left({M-s\over M}\right)^{d+1}
 =M2^{-(d+1)}e^{O(d^2/r)}.                             \tag{3.35}
\]
Taking \(d=\lceil3\log_2M\rceil\) makes this \(o(1)\), whereas
\(\binom M{r-d}=(1-o(1))W(M)\) by multiplying the \(d\) adjacent-rank
ratios. At a join, a crossing rank-\(s\) interval
must end among the first \(r\) positions of the next cumulative block;
otherwise it contains \(r+1\) clean labels. Endpoint nesting adds at most
\(r\) targets per join. Consequently any fixed number of these blocks,
even with different cycles, phases, or coordinate orders, still misses
\((1-o(1))W(M)\) targets at this \(O(\log M)\)-deep rank. In fact (3.35)
is \(O(M^{-2})\), so these blocks alone require \(\Omega(M^2)\) copies.

Finally, a \(W(k)\)-event geometric or wiring object is not automatically an
OR compiler. From singleton recency state \((1,2,3,4)\), no one-letter update
has both \(\{1,4\}\) and \(\{1,3,4\}\) as prefixes: the first target forces
the new letter to be \(\{4\}\) or \(\{1,4\}\), after which the next old
coordinate is \(2\), not \(3\). Thus any Venn/wiring route still needs a
proved \(1+o(1)\)-cost move-to-front compilation.

### 3.8 Cyclic normalization and exact-width rigidity [I]

Recall the cyclic minimum \(\mu(k)\) from Section 1.
For every cyclic word \(A=(A_1,\ldots,A_m)\), with
\(U=\bigcup_iA_i\), there is a linear word preserving all its cyclic unions
and having length at most
\[
 m+\max\{0,\ |U|-\max_i|A_i|-1\}.                     \tag{3.36}
\]
Rotate so a largest letter \(Z=A_m\) precedes the cut. Scan
\(A_1,\ldots,A_m\), recording each nonempty set of coordinates outside
\(Z\) not recorded earlier; call the resulting disjoint blocks
\(C_1,\ldots,C_q\). Their union is \(U\setminus Z\), so
\(q\le|U|-|Z|\). Use
\[
                         A_1,\ldots,A_m,C_1,\ldots,C_{q-1},          \tag{3.37}
\]
with no append when \(q\le1\). Nonwrapping intervals remain, and the full
period realizes \(U\). A proper wrapping union is a suffix through \(A_m\)
followed by a prefix. The suffix contains \(Z\); deleting \(Z\) from the
prefix gives \(C_1\cup\cdots\cup C_j\). If \(j=q\), the target is \(U\);
otherwise the corresponding suffix of (3.37) followed by
\(C_1,\ldots,C_j\) realizes it. This proves (3.36), including \(q=0,1\).

At one cyclic start, growing intervals have nested unions, so it supplies
at most one distinct target of any fixed rank. Consequently
\[
 W(k)\le\mu(k)\le\nu(k)\le\mu(k)+(k-2)_+\quad(k\ge1),               \tag{3.38}
\]
where \(\mu(1)=\nu(1)=1\); the last bound uses \(U=[k]\) and
\(\max_i|A_i|\ge1\). Hence
\[
 \boxed{\nu(k)=(1+o(1))W(k)\iff\mu(k)=(1+o(1))W(k).}                \tag{3.39}
\]
Thus cyclicity removes cut, initial-state, cleanliness, and witness-length
conditions from an unrestricted cyclic construction; it does not create
targets missing from a proposed cycle.

Exact cyclic width is rigid. Suppose \(k\ge2\), \(m=W(k)\), and
\(\binom kr=m\). Then some \(\ell\) satisfies
\[
 1+\left\lceil{\sum_{j=1}^{r-1}\binom kj\over W(k)}\right\rceil
 \le\ell\le r,                                         \tag{3.40}
\]
and the \(m\) cyclic length-\(\ell\) windows enumerate the rank-\(r\)
targets once. Indeed the \(m\) targets must use every start and every end
once. Lift the chosen witness from start \(i\in\mathbb Z\) to the inclusive
interval \([i,e_i]\), with
\[
 i\le e_i\le i+m-2,\qquad e_{i+m}=e_i+m.
\]
If \(e_{i+1}\le e_i\), one equal-rank witness contains the next, forcing
two distinct targets to be equal. Thus the \(m\) positive integer increments
\(e_{i+1}-e_i\) sum to \(m\), so all equal one and every witness has one
length \(\ell\). Any target below rank \(r\) has length below \(\ell\):
a longer interval contains a length-\(\ell\) rank-\(r\) window. There are
\(m(\ell-1)\) shorter cyclic intervals, proving the lower bound in (3.40).

Let \(T_i\) be the length-\(\ell\) window from \(i\). Since
\(T_i\ne T_{i+1}\), choose
\[
 x_i\in A_i\setminus\bigcup_{j=i+1}^{i+\ell}A_j.
\]
The \(\ell\) corresponding \(x_i\)'s in any \(\ell\)-position window are
distinct and lie in its rank-\(r\) union, proving \(\ell\le r\). If
\(\ell=r\), these coordinates exhaust each window; in the window ending at
\(i\), every earlier chosen coordinate is absent from \(A_i\), so
\(A_i=\{x_i\}\). If coordinate \(x\) occurs \(f_x\) times, incidence with
the rank-\(r\) windows gives
\[
 rf_x=\binom{k-1}{r-1}={rW(k)\over k},\qquad
 \ell=r\Longrightarrow k\mid W(k).                    \tag{3.41}
\]

For \(k=17,r=9\), \(W(17)=24310\) and
\(\sum_{j=1}^8\binom{17}j=65535\), so exact cyclic width would force
\(\ell\in\{4,\ldots,9\}\) and, by (3.38),
\[
                         \mu(17)=24310\Longrightarrow\nu(17)\le24325. \tag{3.42}
\]
This is conditional. For \(k=4\), (3.40) forces \(\ell=2=r\), contradicting
\(4\nmid W(4)=6\). The word \((1,2,4,1,8,10,12)\) realizes masks
\(1,\ldots,15\) on intervals
\((1),(2),(1{:}2),(3),(3{:}4),(2{:}3),(1{:}3),(5),(4{:}5),(6),
(4{:}6),(7),(3{:}5),(5{:}7),(3{:}7)\), respectively. Hence
\(\mu(4)=7\), so exact cyclic width is not automatic.

### 3.9 Sublinear-dimension cylinder completion [I]/[C]

**September 8 refinement:** the inequalities and proof below remain valid,
but the \(k^{-1/2}\) term in (3.45) is not necessary. Section 9.3 records
the user's sharper finite theorem and its checked supporting proof [R].

If a nonzero cyclic word on \([k]\), \(k\ge1\), has period \(m\ge1\)
and \(h\) nonempty holes, then for every integer \(t\ge0\),
\[
 \boxed{\nu(k+t)\le2^t\{m+(k-2)_+\}+h\{\nu(t)+1\}.}       \tag{3.43}
\]
For a nonempty linear base of length \(n\), replace the braces by \(n\)
and count its linear holes. Nonemptiness matters: an empty base at
\(k=1,t=2\) would falsely give \(\nu(3)\le3\).

Normalize the cycle by 3.8. For any nonempty linear word
\(A=(A_1,\ldots,A_n)\), the partial lift
\[
 A_1,\ldots,A_n,\{z\},A_1\cup\{z\},\ldots,A_{n-1}\cup\{z\}
                                                               \tag{3.44}
\]
has length \(2n\). Every old witness \([i,j]\) persists, and its union
with \(z\) uses its lifted copy if \(j<n\), or the old suffix and bridge
if \(j=n\). The bridge supplies \(\{z\}\). Thus \(t\) lifts cover
every old realized target times every subset of the new \(t\)-set \(Q\),
and every nonempty subset of \(Q\), without assuming old universality.
For each old hole \(T\), append
\((T,T\cup B_1,\ldots,T\cup B_{\nu(t)})\), where \(B\) is universal
on \(Q\). Its interval unions include every \(T\cup Z\), since
\(\bigcup_{p=i}^j(T\cup B_p)=T\cup\bigcup_{p=i}^jB_p\). The first
letter handles \(Z=\varnothing\); at \(t=0\) this is the whole block.
No witness crosses a join, proving (3.43). Projection onto \(Q\) and 1.1
show \(\nu(t)+1\) is optimal for one isolated full fiber, not for shared
repairs of several fibers.

Write \(m\le(1+\varepsilon)W(k)\), \(h=\eta2^k\), with
\(0\le\varepsilon\le1\). A.1 and A.3 give, for \(t\to\infty,t=o(k)\),
\[
 {\nu(k+t)\over W(k+t)}
 \le1+O\left(\varepsilon+{t\over k}
                  +\eta\sqrt{k/t}+k^{-1}\right).
\]
Indeed \(2^tW(k)/W(k+t)=\sqrt{1+t/k}(1+O(k^{-1}))\), normalization
costs only \(O(k^{3/2}2^{-k})\), and
\(\nu(t)+1=O(2^t/\sqrt t)\). Consequently
\[
 \boxed{t=\lceil k\eta^{2/3}+\sqrt k\rceil
 \quad\Longrightarrow\quad
 {\nu(k+t)\over W(k+t)}
 \le1+O(\varepsilon+\eta^{2/3}+k^{-1/2})}
 \quad(\eta=o(1)).                                      \tag{3.45}
\]
Thus near-width words with \(o(2^k)\) holes suffice. For a family in every
large dimension, put \(d_K=\sup_{j\ge\lfloor K/2\rfloor}\eta_j\), choose
\(t=\lceil Kd_K^{2/3}+\sqrt K\rceil\), and use the base \(k=K-t\);
eventually \(k\ge K/2\), proving the result at every \(K\). It also
suffices on increasing base dimensions \(k_i\) with
\(k_{i+1}/k_i\to1\): completed dimensions \(n_i=k_i+o(k_i)\) have the
same ratio limit. Choose the largest index with \(n_i\le K\); then
\(n_i\le K<n_{i+1}\), and further lifts cost
\(2^{K-n_i}W(n_i)/W(K)=\sqrt{K/n_i}(1+o(1))=1+o(1)\).
The converse uses universal words, so this is an equivalent existence
criterion, not an almost-cover construction. In particular
\(h=O(k^aW(k))\), \(0\le a<1/2\), permits
\(t=\Theta(k^{(2a+2)/3})\) and error
\(O(\varepsilon+k^{(2a-1)/3})\); \(h=O(W(k))\) permits error
\(O(\varepsilon+k^{-1/3})\).

For calibration, if \(m/W(k)\to c>0\), \(h/2^k\to\eta>0\), and
\(t/k\to\lambda>0\), using A.5 for the fiber word makes (3.43) give
the upper coefficient \(\sqrt{1+\lambda}(c+c_4\eta/\sqrt\lambda)\).
Differentiation minimizes this ledger at \(\lambda=(c_4\eta/c)^{2/3}\),
with value \((c^{2/3}+(c_4\eta)^{2/3})^{3/2}\); no global optimality is
claimed. The older A.3 input gives the same formulas with \(\sqrt2\) in
place of \(c_4\).

Conversely, endpoint nesting gives for any linear or cyclic word of length
\(m\) and hole count \(h\),
\[
 h\ge\sum_{s=1}^k[\tbinom ks-m]_+,\qquad
 {m\over W(k)}\ge1-O\left((h/2^k)^{2/3}+k^{-1}\right).   \tag{3.46}
\]
For the second bound set \(m=(1-e)W(k)\), \(0<e\le1\). Adjacent-rank
products give \(\binom{k}{\lfloor k/2\rfloor-j}/W(k)
\ge1-2j(j+1)/k\). If \(ek\ge16\), the
\(\lfloor\sqrt{ek}/4\rfloor+1\) ranks nearest the middle on one side
each miss at least \(3eW(k)/4\); A.1 gives
\(h/2^k\ge3e^{3/2}/32\) for large \(k\). Otherwise \(e<16/k\).
For fixed \(0<c<1\), the same products give the uniform Gaussian
profile \(e^{-2u^2}\) at offset \(u\sqrt k\); its Riemann sum sharpens
the first bound to
\[
 \liminf {h\over2^k}\ge
 \operatorname{erf}\sqrt{\log(1/c)}
 -{2c\over\sqrt\pi}\sqrt{\log(1/c)}
 \quad(m/W(k)\to c).                                    \tag{3.47}
\]
The integral is \(\sqrt{2/\pi}\int(e^{-2u^2}-c)_+du\); as \(c\uparrow1\)
it equals \(4(1-c)^{3/2}/(3\sqrt\pi)+O((1-c)^{5/2})\).

Dimension extension is essential to this argument. An entire middle layer
has \(o(2^k)\) targets but needs \(W(k)\) endpoints. Listing every
nonmiddle proper nonempty target separated by full-set letters misses
exactly that layer and needs at least \(W(k)\) appended positions.
This is not a near-width counterexample. In the near-width regime
\(h=o(\sqrt b)\), the word of 3.5 misses fraction \(1-2/\pi+o(1)\),
so it fails the almost-cover antecedent; its wider versions instead lose
the width coefficient. Fixed finite cyclic seeds also give no such family.

### 3.10 Facet-forest repair and exact envelope deficiency [I]/[C]

Let \(\mathcal H\) be any family of nonempty subsets of \([k]\), with
\(\mathcal H_r=\mathcal H\cap\binom{[k]}r\), \(h_r=|\mathcal H_r|\).
For \(X\subseteq\mathcal H_{r+1}\), let
\(N_r(X)=\{S\in\mathcal H_r:S\subset U\text{ for some }U\in X\}\), and put
\[
 b_r=\max_{X\subseteq\mathcal H_{r+1}}(2|X|-|N_r(X)|),\qquad
 \boxed{F(\mathcal H)=\sum_{r=1}^kh_r-
                \sum_{r=1}^{k-1}[h_{r+1}-b_r]_+.}       \tag{3.48}
\]
There is a nonzero word of length at most \(F(\mathcal H)\) realizing
every member of \(\mathcal H\). Thus a word of length \(n\) with hole
family \(\mathcal H\) can be completed in the same dimension at cost
\(n+F(\mathcal H)\), rather than \(n+|\mathcal H|\).

Here is a complete matching and occurrence proof. In a finite bipartite
graph, the minimum number of unmatched left vertices is
\(\max_X(|X|-|N(X)|)\). The lower bound is immediate. For equality take
a maximum matching and its alternating reachability sets \(X,Y\) from
the unmatched left vertices. No unmatched right vertex is reachable;
\(Y=N(X)\), and the matching bijects \(Y\) with the matched part of
\(X\), proving equality. Replace each upper target by two identical
left slots. Completing a slot family to whole pairs preserves its
neighborhood, so this graph's deficiency is exactly \(b_r\). At least
\([h_{r+1}-b_r]_+\) upper targets receive two distinct lower facets.
Discard assignments to incompletely served upper targets. The two facets
union to their parent, and no lower target is used twice.

Do this at every adjacent rank. Each target has at most one parent and
each internal target has two children. Ranks decrease towards children,
so the result is a forest. Recursively concatenate its leaf labels in
depth-first order. The descendants of every vertex occupy one contiguous
block and union to that vertex. With \(I\) internal vertices the forest
has \(|\mathcal H|-I\) leaves, proving (3.48). In particular, nested
repairs coexist in one literal word; no independent witnesses are composed.

For \(k=17\), define the covered-facet incidence count
\[
 g_{12}=\sum_{U\in\mathcal H_{12}}
              \left(12-|\mathcal H_{11}\cap\tbinom U{11}|\right).
\]
Every eleven-set has six twelve-supersets. For any
\(X\subseteq\mathcal H_{12}\), double counting gives
\(12|X|-g_{12}\le6|N_{11}(X)|\). Therefore
\[
 b_{11}\le\lfloor g_{12}/6\rfloor,\qquad
 \boxed{\operatorname{repair}(\mathcal H_{11}\cup\mathcal H_{12})
 \le h_{11}+\min\{h_{12},\lfloor g_{12}/6\rfloor\}.}     \tag{3.49}
\]
If every eleven-facet of a twelve-hole is a hole, all twelve-holes cost
no extra letters after paying for the eleven-holes. This is the critical
incidence ratio \(12/6=2\), not a generic positive-degree argument.
No bound on \(g_{12}\) is asserted for an arbitrary carrier.

There is also an exact lower-compiler reduction. On a collection of
\(c\ge1\) cycles with total period \(24310\), suppose
\[
 |E_i|=6,\quad C_i\subseteq E_i,\quad DC=DE,\quad |(DE)_i|=7.
                                                               \tag{3.50}
\]
Derivatives use the separate cyclic adjacencies. Pool all positions, and
join each nonempty target \(S\), \(|S|\le6\), to position \(i\) when
\(C_i\subseteq S\subseteq E_i\). For each present six-set \(R\), put
\(P_R=\{i:E_i=R\}\), \(m_R=|P_R|>0\), and
\(h_6=12376-|\{E_i\}|\). For a family \(X\) of targets of ranks
one through five, write \(n_R(X)=|N(X)\cap P_R|\). Its exact Hall
deficiency is
\[
 \boxed{\Delta_C=h_6+\beta_C,\qquad
 \beta_C=\max_X\left\{|X|-\sum_{R\text{ present}}
                      \min(n_R(X),m_R-1)\right\}.}      \tag{3.51}
\]
Indeed every absent six-set is isolated. For fixed smaller-target family
\(X\), adding a present six-set \(R\) changes the Hall deficit by
\(1-m_R+n_R(X)\). The fibers are disjoint, so optimize these choices
independently and use
\(n-[1-m+n]_+=\min(n,m-1)\), proving (3.51).

A maximum matching can cover every present six-set: if \(R\) is
unmatched, every position of \(P_R\) is matched to a smaller target,
and replacing one such assignment by \(R\) preserves cardinality and
all previously matched six-sets. Give matched positions their targets
and unmatched positions their envelopes. Then
\(C\subseteq A\subseteq E\), so \(DA=DE\), and all letters are
nonempty. Every interval of length at least two is fixed by these pair
unions and has rank at least seven. The cyclic collection thus has
exactly \(h_6+\beta_C\) lower holes, all present six-sets being covered.
This is also optimal within the fixed core box: distinct realized lower
targets require distinct single-letter positions and hence a matching.
The remaining capacities sum to \(11934+h_6\) for \(9401\) smaller
targets; their surplus does not bound \(\beta_C\). For example,
\(C=E\) makes every smaller target isolated.

Let \(\mathcal H\) now be the cyclic hole family of this compiled
collection, and let \(g\) count components without a six-letter.
There is at least one component with a six-letter, so \(g\le c-1\).
In each other component replace one letter by its envelope. The pair
unions remain fixed, and at most one smaller target per replacement is
lost. Apply (3.36) after cutting after a six-letter in each component;
the opening costs at most ten letters per cycle. Append the forest word
for the original holes and the at most \(g\) newly lost targets. Hence
\[
 \boxed{\nu(17)\le24310+10c+g+F(\mathcal H),\qquad g\le c-1.}    \tag{3.52}
\]
Opening can cover additional targets, so the original hole family is
only an upper ledger afterward. Using only the eleven/twelve saving,
write \(h_{\rm other}=\sum_{7\le r\le17,\ r\ne11,12}h_r\) to obtain
\[
 \nu(17)\le24310+10c+g+h_6+\beta_C+h_{\rm other}+h_{11}
                   +\min\{h_{12},\lfloor g_{12}/6\rfloor\}.       \tag{3.53}
\]
An overhead at most \(1434\) would improve the retained bound to
\(25744\); none is proved here for an actual envelope collection.
The smaller-target Hall and hole-incidence hypotheses remain separate
from residence. Uniform opening charges cannot themselves attain \(W+3\).

### 3.11 Prescribed Catalan matching extension [I]/[C]

The width discrepancy is structural:
\[
 \binom{16}8-\binom{16}7=1430=\operatorname{Cat}_8,\qquad
 W(17)=\binom{16}8+\binom{16}7.                         \tag{3.54}
\]
The following prescribed matching problem can be solved without search.
Let \(\Omega=\mathbb Z_{15}\cup\{x\}\), with \(g(i)=i+1\) and
\(g(x)=x\). Plus signs between sets or coordinates mean union; complements
in this section are in \(\Omega\). Put
\(B_i=\{i,i+5,i+10\}\), \(i\in\mathbb Z_5\),
\(Z=B_0\cup B_1\), \(Y=B_2\cup B_4\),
\(P=Z\cup\{3\}\), and \(Q=Y\cup\{8\}\).
There exists a \(g\)-invariant matching in the bipartite disjointness
graph on two copies of \(\binom\Omega7\), of size \(11430\), containing
all thirty prescribed edges
\[
 (g^tP,g^tQ),\ (g^tQ,g^tP),\qquad0\le t<15.            \tag{3.55}
\]
It leaves exactly \(\mathcal E=\{\{x\}\cup B_i\cup B_j:i<j\}\)
unmatched on each shore. Every such matching admits a perfect completion
by deleting ten edges and adding twenty, and ten deletions are necessary.

Here is the extension proof. If a seven-set has stabilizer of order
\(d\mid15\), its finite part has size divisible by \(d\). Without
\(x\) the size is seven, so it is free. With \(x\) it is six, so the
only nontrivial stabilizer has order three. Thus \(\mathcal E\) is
exactly the nonfree part, consisting of two size-five orbits; all other
orbits have size fifteen. The disjointness matrix \(K\) has inverse
\[
 (K^{-1})_{S,T}=c_{|S\cap T|},\qquad
 c_j={(-1)^j(j+1)\over36\binom7j}.                     \tag{3.56}
\]
To verify it directly put \(d=7-|S\cap T|\). A neighbor of \(S\)
omits two elements of its nine-element complement, so the product entry is
\[
 \binom{9-d}{2}c_d+d(9-d)c_{d-1}+\binom d2c_{d-2}.
\]
Terms with negative subscripts are absent. The expression is \(36c_0=1\)
for \(d=0\); otherwise the ratios
\(c_d/c_{d-1}=-(d+1)/(8-d)\) and
\(c_{d-2}/c_{d-1}=-(9-d)/d\), the latter for \(d\ge2\), make it zero.

Both matrices preserve orbit-constant functions. In the orbit-indicator
basis, the inverse principal block on the orbits of
\(x+Z,x+Y,P,Q\), of sizes \(5,5,15,15\), is
\[
 H=\begin{pmatrix}
 -29/126&1/126&1/60&37/420\\
 1/126&-29/126&37/420&1/60\\
 1/180&37/1260&-17/105&2/21\\
 37/1260&1/180&2/21&-17/105
 \end{pmatrix},\qquad \det H={41\over61740}\ne0.        \tag{3.57}
\]
For a completely internal evaluation, the six independent entries are
\(c_7+2c_4+2c_1\), \(4c_4+c_1\),
\(3c_6+6c_3+6c_1\), \(3c_0+6c_3+6c_4\),
\(c_7+2c_6+6c_3+6c_2\), \(c_1+2c_0+12c_4\), respectively
\(H_{11},H_{12},H_{13},H_{14},H_{33},H_{34}\).
The permutation \(s\mapsto2s+2\pmod{15}\) exchanges the two pairs
of representatives. Symmetry and the orbit sizes give the transposed
entries. Pair sums and differences split the determinant into two
two-by-two determinants \(41/3675\) and \(5/84\).

If an invertible matrix \(A\) has an invertible inverse block
\((A^{-1})_{II}\), its complementary principal block \(A_{JJ}\)
is invertible: \(A_{JJ}v=0\) implies \(A(0,v)=(w,0)\), then
\(0=(A^{-1})_{II}w\), so \(w=v=0\). Apply this on the invariant
space. Removing the four orbits leaves a nonsingular \(760\)-by-\(760\)
disjointness matrix. A nonzero determinant term gives a matching of its
orbit vertices. Choose an actual edge for each positive entry and develop
it; the free endpoint actions give a literal matching of size \(11400\).
The disjoint \(P,Q\) orbits are distinct, so adjoining (3.55) proves
the prescribed extension. Ordinary regularity alone would not prove it.

For \(0\le t<5\), set \(E_t=x+g^tZ\), \(F_t=x+g^tY\),
\(P_t=g^tP\), \(Q_t=g^tQ\). The ten paths
\[
 E_t^{\rm L}-Q_t^{\rm R}-P_t^{\rm L}-F_t^{\rm R},\qquad
 F_t^{\rm L}-P_t^{\rm R}-Q_t^{\rm L}-E_t^{\rm R}        \tag{3.58}
\]
are vertex-disjoint alternating paths, with prescribed middle edges.
Their outer disjointness follows from the four disjoint full triples
and the distinct coordinates 3 and 8 in the remaining triple. Flipping
them gives \(11440\) matching edges. Every exceptional vertex contains
\(x\), so no exceptional left vertex meets an exceptional right vertex.
In any completion the ten exceptional left vertices consume ten distinct
previously matched right vertices, forcing at least ten old deletions.
This also shows \(11430\) is the maximum invariant matching size: the
unique partner of an exceptional vertex in an invariant matching would
have to be exceptional.

The relevant middle structure is not supplied by this matching theorem.
An edge \((S,T)\) represents the flag \(S\subset\Omega\setminus T\);
if the difference is \(\{a,b\}\), lift it to the Johnson edge
\(S+a\)--\(S+b\) on the \(12870\) eight-sets. Its intersection and
union are its two flag colours, so distinct flags give distinct edges.
For \(C=g^tZ\) use \((a,b,c)=(t+3,t+8,t+13)\); for \(C=g^tY\)
use \((a,b,c)=(t+8,t+3,t+13)\), all modulo fifteen. Put
\(X_s=C+\{x,s\}\), \(Y_s=C+(\{a,b,c\}\setminus\{s\})\).
The forty surviving or new prescribed edges lift exactly to
\[
                 X_a-X_c-Y_a,\qquad X_b-Y_c-Y_b         \tag{3.59}
\]
for the ten cores \(C\). These are twenty disjoint three-vertex paths
on sixty owners, forming four full \(g\)-orbits. Each orbit contains
internal vertices of degree two. Consequently, for any extension above,
its repaired lift is a spanning linear forest exactly when its invariant
\(11400\)-edge bulk is acyclic, has maximum degree two, and avoids all
sixty packet owners. Necessity of avoidance follows because bulk degree
is constant on each owner orbit; sufficiency follows by disjoint union.
Under this additional condition its component count is
\[
             (12870-60-11400)+20=1430=15\cdot94+20.      \tag{3.60}
\]
The choice of actual edge phases remains part of this condition. The
following refinement proves its avoidance part. Joint degree-two acyclicity
is still [O], as are a compatible seventeen-bit chronology, residence or
a nonflat schedule, and the common-word compiler.

**Owner-avoiding extension [I].** The bulk can be chosen to avoid all
sixty packet owners \(\mathcal W\). This is an additional existence
theorem, not a property of every matching supplied above.

Index triples by \(\mathbb F_5\). The ten cores are
\(C_{r,d}=B_{r-d}\cup B_{r+d}\), \(d=1,2\), with gap \(B_r\).
The forbidden owners are \(C_{r,d}+\{x,s\}\) and
\(C_{r,d}+(B_r\setminus\{s\})\), \(s\in B_r\).
They are complement-closed: complementation exchanges these forms and
replaces \(d\) by \(3-d\). Their four orbit representatives are
\[
 V=(x+P,x+Q,(x+P)^c,(x+Q)^c),\qquad
 \Gamma=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}.       \tag{3.60a}
\]
Every pair of adjacent forbidden owners has its seven-set intersection
in the removed palette. For the same core the intersection is \(C+x\)
or \(C+s\). Different cores share at most one full triple, so intersections
involving an owner containing \(x\) have size at most six. Two owners
omitting \(x\) could intersect in seven only with core indices
\(\{i,j\},\{i,k\}\) and gap indices \(k,j\), respectively.
The midpoint rule would give \(2k=i+j\), \(2j=i+k\), forcing
\(i=j=k\) in \(\mathbb F_5\), a contradiction. Thus no remaining
flag has both middle owners forbidden.

Let \(\widehat K\) be the full \(764\)-state orbit matrix, with
\(R=\widehat K^{-1}\), removed orbit indices \(I\) and remaining
indices \(J\). Write \(A=\widehat K_{JJ}\), so \(A\) is invertible
by (3.57). Define the \(764\)-by-four incidence matrix
\(F_{\alpha j}=|\{V'\in[V_j]:S_\alpha\subset V'\}|\),
and \(U=F_J\). All retained palette and owner orbits have size fifteen.
Consequently the actual allowed-flag matrix is
\[
 A_{\mathcal W}=A-U\Gamma U^T.                         \tag{3.60b}
\]
The subtracted entry counts forbidden middle owners of a flag, which
is zero or one by the preceding geometry. There is no double-deletion
correction. In fact each remaining seven-set belongs to at most one
forbidden owner, and each forbidden owner has six remaining facets;
thus \(U^TU=6I_4\). Only twenty-four retained palette orbits are affected.

The two exceptional palette orbits have size five. Their relative weights
are \(w=\operatorname{diag}(1/3,1/3,1,1)\), and the full weight matrix
is \(D=\operatorname{diag}(w,I_{760})\). Orbit double counting gives
\(DR=R^TD\). Put \(G=(RF)_I\), \(T=F^TDRF\). The complementary
inverse identity, verified by block multiplication, is
\(R-R_{\bullet I}H^{-1}R_{I\bullet}=\operatorname{diag}(0,A^{-1})\).
It implies
\[
 S:=U^TA^{-1}U=T-G^TwH^{-1}G,\qquad
 {\det A_{\mathcal W}\over\det A}=\det(I_4-\Gamma S).   \tag{3.60c}
\]
For the determinant identity, eliminate either diagonal block of
\(\begin{pmatrix}I_4&\Gamma U^T\\U&A\end{pmatrix}\).
The position of \(w\) in the first identity is essential.

All entries can be evaluated without the bulk catalogue. Define
\[
 d_m={2(-1)^m\over9\binom8m},\quad
 e_m=2\mathbf1_{m=0}-d_m\quad(0\le m\le8).
\]
For \(m\le7\), summing (3.56) over the seven-facets of one eight-set
gives \((8-m)c_m+mc_{m-1}=d_m\). A second facet sum gives
\((8-m)d_m+md_{m-1}=e_m\) for \(0\le m\le8\). Negative-index
terms are omitted; \(d_8=2/9\) is defined by the closed formula, not the
first recurrence. For \(S_i=(x+Z,x+Y,P,Q)_i\), therefore,
\[
 G_{ij}=\sum_{V'\in[V_j]}d_{|S_i\cap V'|},\qquad
 T_{ij}=\sum_{V'\in[V_j]}e_{|V_i\cap V'|}.              \tag{3.60d}
\]
The same pair-sum/difference decomposition used in (3.57) gives
\[
 S_+=\begin{pmatrix}2452/615&138/41\\138/41&243/205\end{pmatrix},
 \qquad S_-={1\over25}\begin{pmatrix}14&36\\36&9\end{pmatrix}.
\]
On each sector \(\Gamma\) exchanges the two coordinates. Thus the
two determinants of \(I-\Gamma S\) are \(893/1025\) and \(-1/125\),
and
\[
 \boxed{\det A_{\mathcal W}/\det A=-893/128125\ne0.}    \tag{3.60e}
\]
The nonnegative integer matrix \(A_{\mathcal W}\) therefore has a
perfect matching in its support. Choose an actual allowed edge for each
matched orbit pair and develop it. Invariance of \(\mathcal W\) preserves
avoidance. Adding the prescribed edges and repairing the exceptions gives
the claimed owner-disjoint extension. Degree and acyclicity do not follow
from this determinant.

There is a useful conditional cycle-removal step. Suppose an allowed bulk
already has maximum owner degree two, and orient one cycle component of
its owner quotient. Retain loops and parallel edges in that quotient.
For consecutive lifted edges \(u\to v\to w\), replace the flag
\((u\cap v,u\cup v)\) by \((u\cap v,v\cup w)\). Its owners are
\(v\) and \(y=(u\cap v)\cup(w\setminus v)\); lower colours stay
fixed and upper colours are cyclically permuted. If every new \(y\)
lies off the old cycle and \(\mathcal W\), and each other owner orbit
receives at most its degree slack \(2-\deg\), this move preserves both
palettes and the degree cap while deleting exactly that cycle. Every old
cycle vertex becomes a leaf, so no new edge can lie on a cycle. The
existence of such a move, and of a cap-two bulk in the first place, remains
open. Merely changing voltages of a fixed quotient cycle cannot remove it:
traversing the quotient cycle repeatedly eventually closes upstairs.

The following check verifies only the small inverse blocks and orbit
histograms; no matching search is a premise of either existence proof.

```python
from fractions import Fraction as F
from math import comb
rot=lambda A,t: frozenset((i+t)%15 if i<15 else 15 for i in A)
B=[{i,i+5,i+10} for i in range(5)]
Z,Y=B[0]|B[1],B[2]|B[4]
R=[Z|{15},Y|{15},Z|{3},Y|{8}]
O=[{rot(A,t) for t in range(15)} for A in R]
assert list(map(len,O))==[5,5,15,15]
c=[F((-1)**j*(j+1),36*comb(7,j)) for j in range(8)]
H=[[sum((c[len(A&T)] for T in orbit),F(0)) for orbit in O] for A in R]
assert H==[list(map(F,row.split())) for row in [
    "-29/126 1/126 1/60 37/420", "1/126 -29/126 37/420 1/60",
    "1/180 37/1260 -17/105 2/21", "37/1260 1/180 2/21 -17/105"]]
dets=[]
for s in (1,-1):
    dets.append((H[0][0]+s*H[0][1])*(H[2][2]+s*H[2][3])
                -(H[0][2]+s*H[0][3])*(H[2][0]+s*H[2][1]))
assert dets==[F(41,3675),F(5,84)] and dets[0]*dets[1]==F(41,61740)
Omega=set(range(16))
V=[R[2]|{15},R[3]|{15}]
V+= [Omega-A for A in V]
VO=[{rot(A,t) for t in range(15)} for A in V]
d=[F(2*(-1)**m,9*comb(8,m)) for m in range(9)]
e=[2*(m==0)-d[m] for m in range(9)]
G=[[sum((d[len(A&T)] for T in orbit),F(0)) for orbit in VO] for A in R]
T=[[sum((e[len(A&B)] for B in orbit),F(0)) for orbit in VO] for A in V]
ratios=[]
for index,s in enumerate((1,-1)):
    h=[[H[i][j]+s*H[i][j+1] for j in (0,2)] for i in (0,2)]
    g=[[G[i][j]+s*G[i][j+1] for j in (0,2)] for i in (0,2)]
    t=[[T[i][j]+s*T[i][j+1] for j in (0,2)] for i in (0,2)]
    inv=[[h[1][1]/dets[index],-h[0][1]/dets[index]],
         [-h[1][0]/dets[index],h[0][0]/dets[index]]]
    w=[F(1,3),F(1)]
    S=[[t[i][j]-sum(g[a][i]*w[a]*inv[a][b]*g[b][j]
                    for a in range(2) for b in range(2))
        for j in range(2)] for i in range(2)]
    expected=([['2452/615','138/41'],['138/41','243/205']] if s==1
              else [['14/25','36/25'],['36/25','9/25']])
    assert S==[list(map(F,row)) for row in expected]
    ratios.append((1-S[1][0])*(1-S[0][1])-S[0][0]*S[1][1])
assert ratios==[F(893,1025),F(-1,125)]
assert ratios[0]*ratios[1]==F(-893,128125)
```

### 3.12 Quantitative inherited-symmetry breaking [I]

Now work on \(\mathbb Z_{15}\cup\{x,y\}\), with \(h=g^5\), fixing
\(x,y\). Suppose a nonempty set-valued linear word of length \(W+t\),
\(W=24310\), covers ranks eight and nine. Choose one witness for every
nine-set and close their endpoint-ordered chronology to a simple cycle
\(F\). Let \(\eta\) be the number of eight-sets absent from adjacent
intersections and \(q\) its number of non-Johnson edges. Then
\[
 \eta\le2t,\quad q\le\eta,\quad
 |E(F)\mathbin\triangle E(hF)|\ge
 \begin{cases}60-4\eta,&q=0,\\64-4\eta-2q,&q>0.\end{cases}        \tag{3.61}
\]
In particular, length \(24313\) forces a symmetric difference of at
least \(28\); an exactly rainbow lower palette forces at least \(60\).
These are adjacency bounds, not extra-letter costs.

For completeness, the endpoint argument works for arbitrary set-valued
letters. The selected intervals \([\ell_i,r_i]\) have both endpoint
sequences strictly increasing. Rank-eight witnesses also have distinct
endpoints; at most \(t\) left endpoints and \(t\) right endpoints
fall outside the central endpoint sets. Any other lower witness is
\([\ell_j,r_i]\), with \(j>i\), and lies inside both central
intervals \(i,i+1\). Its union equals \(T_i\cap T_{i+1}\).
Thus \(\eta\le2t\). There are \(W-q\) Johnson edges but
\(W-\eta\) distinct lower colours, so their total excess multiplicity
is \(e=\eta-q\ge0\).

The ten fixed nine-sets are unions of three triples \(B_i\). No two
are Johnson-adjacent. The ten fixed eight-colours are \(x+y+B_i+B_j\).
An unordered edge fixed by the order-three action has both endpoints
fixed. Every other edge orbit has size three; selecting one or two of
its edges contributes exactly two to the symmetric difference. Call
such an orbit partial. Write \(b\) for the number of fixed nine-sets
whose two neighbors are fixed, and \(z\) for those having no incident
Johnson edge. There are at least \(10-b\) partial orbits incident to
fixed vertices, since any other two-element neighbor set is not invariant.

For a fixed nine-set \(v\), its nine eight-subsets form a colour family
\(\mathcal C_v\). These ten families are disjoint, since distinct
fixed nine-sets intersect in at most six coordinates; they also avoid
the ten fixed colours. If \(v\) has an incident Johnson edge and every
colour in \(\mathcal C_v\) occurs once, its family contains at least
two partial edge orbits. Indeed an incident edge orbit is partial
because \(v\) has degree two. Its three-colour orbit has exactly three
selected edges in total, which cannot be supplied by just one partial
orbit and any number of complete orbits. This supplies one additional
partial orbit beyond the one counted at \(v\).

Each fixed colour occurring once or twice also supplies a partial orbit.
These edges have \(x,y\) at both endpoints and meet no fixed nine-set.
Failure of an additional \(\mathcal C_v\) contribution consumes at
least one absent colour or excess occurrence; failure at a fixed colour
means it is absent or occurs at least three times. The families are
disjoint, so at most \(\eta+e\) of these contributions are lost. Hence
\[
             \tfrac12|E(F)\mathbin\triangle E(hF)|
                         \ge30-b-z-\eta-e.             \tag{3.62}
\]
Here \(b\le z\). If \(q=0\), both vanish. If \(q>0\), then
\(z\le q-1\): for \(z>0\) the fixed vertices with no Johnson
incidence induce a path forest inside the spanning cycle, so at least
\(2z-(z-1)=z+1\) non-Johnson edges meet them; \(z=0\) is immediate.
Substitution proves (3.61), including its \(28\) and \(60\)
specializations. This quantifies a necessary departure from the inherited
fifteen-coordinate symmetry; it supplies neither the departure nor an
optimal word.

## 4. Live coefficient-one architecture

For the punctured two-rank problem put

\[
b=2r+1,\qquad
\mathcal M=\binom{[b]}r,\qquad
\mathcal L=\binom{[b]}{r-1},\qquad
A=|\mathcal M|,\qquad A/b=\operatorname{Cat}_r.
\]

For the independent \(2b\)-coordinate selectors, \(b\) is odd,
\(|\Omega|=2b\), and \(W=\binom{2b}b\). Context determines which notation is
in force.

### 4.1 The punctured two-rank hypergraph [I]

For a permutation \(w=(w_0,\ldots,w_{b-1})\), with subscripts modulo \(b\),
write

\[
I_k^w(s)=\{w_s,\ldots,w_{s+k-1}\}
\]

and define

\[
E(w)=\{(\mathcal M,I_r^w(s)):s\ne0\}
\;\dot\cup\;
\{(\mathcal L,I_{r-1}^w(s)):s\ne0\}.
\]

It has \(4r\) vertices, \(2r\) on each shore. Its containment graph is a
canonically oriented alternating path, so \(w\mapsto E(w)\) is injective
and there are \(b!\) configurations. Every middle and lower target has
degree

\[
D_M=2r\,r!(r+1)!,\qquad D_L={r+2\over r}D_M.
\]

Weight \(1/D_L\) on every configuration is an optimal fractional matching:
it saturates the lower shore, loads each middle target by \(r/(r+2)\), and
has mass \(|\mathcal L|/(2r)\).

For fixed \(e\), let \(q(T)\) be the number of distinct cyclic boundary cuts
used by \(T\subseteq e\). The boundary graph is
\(\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\})\) with two edges deleted;
every subgraph with \(m\) edges and \(v\) nonisolated vertices has
\(m\le2(v-1)\). Consequently, for an absolute \(C\) and \(|T|\ge2\),

\[
{\deg(T)\over D_M}\le C^{|T|}r^{\,2-q(T)}.             \tag{4.1}
\]

The exact pair inventory also gives

\[
{1\over D_M}\sum_F\binom{|e\cap F|}{2}
=12+{32\over r}+{99\over2r^2}+O(r^{-3}).              \tag{4.2}
\]

Thus the local enumeration, fractional optimum, and all-order boundary
codegrees are closed. They do not constitute a matching theorem.

### 4.2 Product-law control and stopped descent [I]/[C]

Independently retain lower targets with density \(x\) and middle targets
with density

\[
y={rx+2\over r+2}.
\]

Put \(d_x=D_Mx^{2r}y^{2r-1}\). Conditional on a fixed configuration \(e\)
surviving, let

\[
\mathcal E_x(e)=
\mathbb E\!\left[\sum_{F\ {\rm surviving}}(|e\cap F|-1)_+
\,\middle|\,e\ {\rm survives}\right].
\]

Then

\[
{\mathcal E_x(e)\over r d_x}
=O\!\left({1\over rx^3}\right),                         \tag{4.3}
\]

uniformly for \(x\ge r^{-\alpha}\), every fixed \(\alpha<1/3\). For a fixed
retained target \(v\), the rooted estimate gives

\[
{\operatorname {Var}X_v\over(\mathbb EX_v)^2}
\le {1\over\mathbb EX_v}+O\!\left({1\over rx^3}\right). \tag{4.4}
\]

For each fixed integer \(s\ge1\) and \(\alpha<1/(6s)\),

\[
{\mathbb E(X_v-\mathbb EX_v)^{2s}\over(\mathbb EX_v)^{2s}}
=O_s((rx^3)^{-s}).                                      \tag{4.5}
\]

The moment estimates remain valid after conditioning on both exact shore
sizes, with exponentially small comparison error. They are annealed or
fixed-slice results, not estimates for the adaptive residual law.

For the actual isolated-edge process, after round \(j\) let \(H_j\) be the
residual hypergraph, \(Z_j=|E(H_j)|\), and \(M_j,L_j\) its shores. Put

\[
x_j={|L_j|\over|L_0|},\qquad
\bar d_j^M={2rZ_j\over|M_j|},\qquad
\bar d_j^L={2rZ_j\over|L_j|}.
\]

Fix \(K\ge1\), set \(\gamma=1/(96K)\), and take
\(0<\alpha\le1/(256K)\). In every good round, mark each residual
configuration with probability

\[
p_j={\gamma\over r\bar d_j^M}.                         \tag{4.6}
\]

Assume, until \(x_j\le r^{-\alpha}\), only

\[
\max_{v\in M_j}d_j(v)\le K\bar d_j^M,\qquad
\max_{v\in L_j}d_j(v)\le K\bar d_j^L.                  \tag{4.7}
\]

The internal covariance and drift proof gives

\[
\Pr\!\left(
\begin{array}{c}
\text{the cap persists to the threshold, but a bite estimate}\\
\text{or the resulting two-shore descent fails}
\end{array}\right)
\le e^{-\Omega(r)}.                                    \tag{4.8}
\]

On success, the accepted configurations form a matching leaving
\(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and \(o(1)\) of the middle
shore. The cap also preserves an \(\exp(r\log r)\) average-degree floor
through the required \(O_K(r\log r)\) rounds. Equation (4.8) is a
stopped-event statement; it is not a conditional probability given the
future event that the cap persists.

### 4.3 The all-depth capacity boundary [I]/[C]

For a matching \(\mathcal P\) of punctured configurations, retain its starts
\((w,s)\) with \(s\ne0\), and for \(1\le q\le H\) define

\[
h_q^-(\mathcal P)=\binom b{r-q}
-\left|\{I_{r-q}^w(s):(w,s)\text{ is retained}\}\right|,
\]

\[
h_q^+(\mathcal P)=\binom b{r+1+q}
-\left|\{I_{r+1+q}^w(s):(w,s)\text{ is retained}\}\right|. \tag{4.9}
\]

If the unmatched lower-shore density is \(x\), then whenever
\(H\ge\lfloor\sqrt{rx}/4\rfloor\) and \(rx\ge64\),

\[
\sum_{q\le H}(h_q^-+h_q^+)
\ge {7\over32}|\mathcal L|\sqrt r\,x^{3/2}.            \tag{4.10}
\]

Therefore aggregate \(o(A)\) Gaussian-band holes require

\[
x=o(r^{-1/3}).                                         \tag{4.11}
\]

The stopped descent in Section 4.2 ends earlier, so Gate A alone cannot give
all-depth coverage. There are two exact continuations:

1. continue the same literal bank below (4.11) and prove distinct coverage
   at every depth \(q\le H\); or
2. prove a positive fractional cover of mass
   \(O(x\operatorname{Cat}_r)\); C.10 then rounds it to
   \(O(x\log r\,\operatorname{Cat}_r)\) compatible rows while leaving only
   \(o(A)\) holes.

For the second route, the logarithmic rounding overhead is harmless because
\(x\log r=o(1)\) in the live fixed-power range. The missing input is the
fractional cover itself, equivalently a capacity-sized hole-aligned
external-window degree tail. Uniform use of the complete survivor catalogue
does not supply it. Appendices H.11, H.14, H.15, H.15A, and H.16 prove,
respectively, the local affine identity, a uniform \(r^{-29}\) inverse for
the sixteen-atom bank, the remote shore-difference bound, a positive
\(j=2\) rooted-core determinant, and Venn-gap localization. These remain
local or rooted statements: rootless dressing can cancel the leading
determinant coefficient, and no compatible positive cover on the stopped
residual at every depth has been constructed.

### 4.4 Gates A and B already imply coefficient one [C]

Keep \(b=2r+1\), \(A=\binom br\), and put
\[
 L_-=\binom b{r-1}={r\over r+2}A,\qquad
 H=\lceil\sqrt{b\log b}\rceil.
\]
Assume the common Gates A--B output contains a matching of \(p\) punctured
configurations with unmatched lower density \(x=o(1)\), so
\(2rp=(1-x)L_-\). Restore the omitted start in every selected row. Assume
Gate B, using those same literal rows
and \(o(A/b)\) additional full cyclic rows, leaves aggregate \(o(A)\) holes
at ranks \(r-q,r+1+q\), \(1\le q\le H\). Its fractional-cover alternative
has the required row count because
\(O(x\log r\,A/b)=o(A/b)\) at Gate A's fixed-power residual.

For the resulting \(t\) full rows,
\[
 p={(1-x)A\over2(r+2)}={(1-x)A\over b+3},\qquad
 t=p+o(A/b),\qquad bt\le A+o(A).                       \tag{4.12}
\]
The matching already supplies \((1-x)L_-\) distinct rank-\(r\) targets, so
\[
 h_r\le A-(1-x)L_-={2+rx\over r+2}A=o(A).             \tag{4.12a}
\]
In a full cyclic permutation row, complements of its rank-\(r\) windows
are exactly its rank-\(r+1\) windows after a cyclic shift. For the identical
full-row family, therefore, \(h_{r+1}=h_r\). Gate B now gives
\[
 \sum_{s=r-H}^{r+1+H}h_s=o(A).                        \tag{4.12b}
\]

Periodically extend each row and apply 3.4 with \(L=b\),
\(\ell=r-H\), \(u=r+1+H<b\). The cyclic permutation windows are clean,
its compiled block has \(b+2H+1\) letters, and
\[
 (b+2H+1)t=bt+O(Ht)\le A+o(A).                       \tag{4.12c}
\]
The nonempty targets outside the band number at most
\[
 2^{b+1}e^{-2H^2/b}=o(A),                             \tag{4.12d}
\]
by the exponential-moment argument in 3.3 and
\(A\ge2^b/(b+1)\). Append those targets and the holes from (4.12b).
This constructs a nonzero word of length \(A+o(A)\), proving
\(\nu(2r+1)=(1+o(1))W(2r+1)\). One top-bit splice and
\(W(2r+2)=2W(2r+1)\) prove the same in every even dimension. Thus Gates
A and B alone imply coefficient one; no product lift is required.

### 4.5 Coherent-tour banks [I]

Appendix I proves the all-band catalogue scale
\(\Theta(2^b/b^{3/2})\) up to a slow factor and constructs
\(2^b/Q^2\ge2^b/(4b^2)\)-sized, internally three-rank-disjoint,
\(H\)-wise balanced coset banks. Cross-pairing completed-start selection
remains open.

## 5. Exact remaining gates

### Gate A [O]: quenched cap preservation

For one fixed \(K>1\), and \(0<\alpha\le1/(256K)\), run the actual
isolated-edge process of Section 4.2 and stop at the first round when either
\(x_j\le r^{-\alpha}\) or one inequality in (4.7) fails. Prove

\[
\Pr(\text{the degree cap fails before the density threshold})=o(1). \tag{5.1}
\]

Together with (4.8), this yields the punctured two-rank near-factor. The
boundary codegrees, annealed and exact-slice moments, bite concentration,
empirical degree floor, and stopped descent are already proved. A maximum
degree cap does not generically propagate itself; the proof must exploit the
punctured interval geometry. The shortest current product-law target is the
tail-relative signed connected-carrier hierarchy under the appropriate Palm
law: its first unresolved member is the connected two-star, and the signed
higher-star remainder must be controlled with it. Stopped slice, center,
erosion, and purge transfer are then still required on this twelfth-moment
route.

Independently, Appendices C.12--C.12a retain the older sixth-moment route.
Its product/exact-slice signed collision forcing and deterministic
post-purge transfer are proved. Its only open probabilistic inputs are the
stopped pre-purge scalar sum (C.12a.24) and removed-edge sum (C.12a.25);
a common comparison loss \(r^{\kappa+o(1)}\) is sufficient under
(C.12a.28).

An alternative sufficient stop, not a proof of (5.1), is
\(\chi=\bar C/[2r(z_M+z_L)]\le K\) from C.5a. Its descent and exact-slice
bounded-test estimate are proved. The remaining input is the actual
arrival-law estimate (C.5a.7), allowing loss
\(r^{\kappa+o(1)}\), \(\kappa<1-6\alpha\). It must include the first
violating child state; conditioning that state to be good is invalid.

### Gate B [O]: critical all-depth cover-down

On the same literal bank produced after Gate A, prove one of:

- continuation to \(x=o(r^{-1/3})\) together with
  \(\sum_{q\le H}(h_q^-+h_q^+)=o(A)\); or
- a compatible positive fractional cover of the holes of mass
  \(O(x\operatorname{Cat}_r)\), followed by the proved rounding theorem,
  which uses \(O(x\log r\,\operatorname{Cat}_r)\) physical rows.

The rows must cover all depths \(q\le H=\lceil\sqrt{b\log b}\rceil\) in one
common occurrence state. Raw capacity, conservation, complete-catalogue
averaging, or a two-rank matching does not prove this gate. The
zero-avoidance lemmas in Appendix H, including the uniform local inverse
and the \(j=2\) rooted-core determinant, are only partial estimates: the
missing output is still a compatible positive cover, on this stopped bank,
at all displayed depths simultaneously.

These are the retained same-dimension routes. Alternatively, 3.9 permits
aggregate \(o(2^b)\) holes in a restored-row word of length \(A+o(A)\),
followed by \(o(b)\)-dimensional extension. C.9.15 bounds the raw
occurrence deficit by \(O(Ax(1+\sqrt{rx}))\), which is \(o(2^b)\) for
any \(x=o(1)\); thus raw capacity no longer forces \(x=o(r^{-1/3})\)
for this weaker interface. Actual distinct-window coverage is still open.

### Independent selector gates [O]

The punctured route ends at Gate B by 4.4. Two independent \(2b\)-coordinate
selectors remain:

- **Gate \(C_{\rm F}\).** Independently select completed coherent tours
  from the balanced coset banks of Section 4.5 so that their internal middle
  supports are disjoint and the off-middle deficit in (I.41) is \(o(W)\).
  Cleanliness and serialization are proved; this open selector is independent
  of Gates A and B.
- **Gate \(C_{\rm Q}\).** Select phase packets with disjoint internal middle
  supports and aggregate off-middle deficit \(o(W)\), as in (I.Q.17).
  Section 3.4 serializes every packet separately; ordered queues and
  cross-join cleanliness are not premises.

Either output is a literal compiler antecedent; no common symmetric-chain
factor or odd DCC is assumed.

I.7 weakens either selector's aggregate off-middle requirement to
\(o(4^b)\) if one allows sublinear dimension extension. For tours it also
removes the balanced-coset restriction. Both weaker selections remain [O].

Appendix I.3A proves exact regularity, the full middle pair-codegree profile,
exact fractional middle/adjacent loads, and the completed-tour compiler for
the all-pairing orbit; its maximum normalized pair codegree is
\((b^2-5)/(2b^2(b-1))\). The growing-rank correlated selector controlling all
nonzero band offsets is not proved.

### Gate D [I]+[W]: finite \(k=17,18,19,20\) closed

The supplied optimal word and independent complete replay establish
\(\nu(17)=24313\); see 9.26. Its two-block join retains all internal
witnesses and supplies exactly five missing targets across the boundary.
The newly supplied optimal18 word also passes complete independent
verification and attains48623; see9.27. The supplied19/20 words now also
pass independent complete verification and attain92381/184759; see9.31.
The next unresolved finite case is21, with endpoint target352719.
Section 3.10 supplies an intermediate-bound repair criterion; 3.11 closes
prescribed colour extension and packet-owner avoidance, but leaves
degree-two acyclicity open. Section 3.12 is only a necessary
symmetry-breaking bound.

## 6. Completion implications

Within the self-contained [I] core, A.7 gives the full-cube upper coefficient
\(c_9<1.18071\). The later records in Section 9 give the user's checked
explicit coefficient \(1.177987\) [R] and a proposed coefficient-one proof
[P], both for this same full-cube problem. A.6 proves a \(2/\sqrt e\) floor
for the designated
terminal-rectangle ledger of centered product-SCD refinements, including
vanishing-volume omissions; it is not a lower bound on unrestricted \(\nu\).
A.7 escapes that partition ledger by a fully charged overlapping terminal
cover, not by omitting its excess volume or its closing positions.
Gates A and B on one literal restored row family imply
\(\nu(k)=(1+o(1))W(k)\) by 4.4; the result is constructive or a
finite-sample probabilistic existence proof according to the gates. It does
not imply \(\nu(k)=W(k)\), since \(B(k)=W(k)+\Theta(\sqrt k)\).
Independently, either \(C_{\rm F}\) or \(C_{\rm Q}\) followed by 3.4, or a
DCC cycle followed by 3.3, proves coefficient one; bounded top-bit splices
cover the other dimensions. Section 3.5 unconditionally treats only
\(\nu_h\) for \(h=o(\sqrt b)\), and 3.5A proves that completing that
particular word by appending cannot settle the full cube. Section 3.7
separately excludes sublinear union-preserving refinement and any fixed
number of cumulative difference-cycle blocks.
Equivalently, 3.8 says any cyclic all-rank word of length \(W+o(W)\)
already yields the full linear theorem with only \(O(k)\) overhead.
The finite cycles in 2.3 supply new exact certificates and a reusable
safe-erasure operation, but no asymptotic family.
The further equivalent target in 3.9 is a near-width linear or cyclic
word missing only \(o(2^k)\) targets; I.7 applies it to tours and packets.
C.5a is an alternative punctured matching antecedent, not adaptive
persistence or all-depth coverage.

## 7. Scope walls

1. Baranyai--Katona is not required.
2. Two-rank matching says nothing about deeper windows.
3. Annealed or exact-slice estimates do not imply adaptive quenched ones.
4. Product degrees are not tangent-invariant under isolated-edge bites;
   stopped descent uses empirical shore averages.
5. Independently built factors, banks, retirements, and compilers compose
   only in one literal occurrence state.
6. A fixed-pairing coset resolution is not a cross-pairing near-factor;
   low-order balance does not control every residual obstruction.
7. High-derivative blocks make joins harmless, but their actual lengths and
   holes still matter.
8. For the word of 3.5, \(F(c)>1\) at \(h/\sqrt b\to c>0\), whereas A.4
   needs \(h/\sqrt b\to\infty\); 3.5A also rules out cheap append-only repair.
9. The \(\sqrt2\) barrier in 3.5A concerns maximal fixed-split blocks, not
   mixed-support fragments, tours, packets, DCC, or unrestricted \(\nu\).
10. The \(2J\) recoding bound counts new internal cuts; net length change
    does not control arbitrary block recoding.
11. Difference-cycle orbit regularity counts occurrences, not complementary
    phases. Its deep-rank barrier is for a fixed number of cumulative blocks.
12. Cyclic normalization removes boundary handling, not the need to cover
    every rank inside the cycle; exact cyclic width is itself restrictive.
13. The bordered splice (2.2) needs a literal prefix--suffix border; the
    \(k=16\) certificate has none. Appendix B's different boundary splice
    saves one position using explicit source identities.
14. The \(k=9\) cycle in 2.3 has 12 proved holes; failed searches within
    particular templates are not nonexistence results.
15. The weaker hole condition in 3.9 is aggregate on one word, and its
    all-dimension conclusion needs relatively dense base dimensions. Do not
    append the holes before lifting, or confuse it with same-dimension repair.
16. An average-conflict cap suffices for descent, not its own preservation;
    the bounded slice test in C.5a does not imply its adaptive arrival test.
17. A.5, A.5B, and A.7 give asymptotic coefficients, not bounds with those exact
    coefficients at every finite \(k\). A.6 constrains centered terminal-rectangle
    accounting, not new cross-boundary coverage or arbitrary OR words.
18. Facet repair needs its actual incidence geometry; envelope capacity
    surplus is not Hall. A prescribed colour matching need not have a
    degree-two acyclic middle lift, and symmetry-breaking counts are not
    letter savings.
19. A.7's Brownian law averages the cost of complete deterministic SCD
    refinements; no sampled branch is substituted for coverage. Padding
    repeats existing sets, and its image chains retain their multiplicities.
    Neither the nine-accumulator bound nor a fractional template proves
    the coefficient-one conjecture.
20. Section 9's coefficient-one claim is a proposed proof with internal
    AI-agent reviews, not an externally or formally verified theorem.
    Do not read [P] or [R] as [I]/[C], silently replace linked hypotheses,
    or confuse coefficient one asymptotically with \(\nu(k)=W(k)\) at
    finite \(k\); Section 2 already gives the stronger finite lower bound.

### Archived GK/Dyck branch (status only; not a premise)

Section 3.6 excludes the recursive GK four-block chronology at coefficient
one. Other Hall--GK--Dyck banks still lack all-depth shadow control; 3.4
removes only serialization. No live implication uses them.

## 8. Completion ledger and audit contract

| item | status | boundary |
|---|---|---|
| rank lower bound/central maximizer | [I] | closed |
| \(\nu(k)=B(k),0\le k\le17\) | [I]+[W] | only word bodies external |
| \(k=17\) | [I]+[W] | exact optimum 24,313, Section 9.26 |
| \(k=18\) | [I]+[W] | exact optimum48,623, Section9.27 |
| four-block full-cube upper bound | [I] | A.5: \(\nu(k)\le(c_4+o(1))W(k)\), certified \(c_4<1.27\) |
| length-dependent full-cube improvement | [I] | A.5B: coefficient \(c_4-\Delta_8<1.26946080564\); not coefficient one |
| balanced-accumulator staircase cover | [I] | A.7: exact \(c_9<1.18071\), all-rank coverage and all positions charged |
| user selective-truncation improvement | [R] | 9.1: same full-cube coefficient \(1.177987\); proof reviews and exact `h100` certificate recorded |
| grouped cylinders/three-block precursor | [I] | exact paired-family compiler; closed-form \(c_3\) in A.5 |
| centered terminal-rectangle floor | [I] | A.6: \(2/\sqrt e\), also with vanishing designated-volume omissions |
| DCC compiler | [C] | DCC open |
| retained-SCD far repair | [I] | \(o(W)\) for \(H/\sqrt b\to\infty\) |
| punctured profile/codegrees/polymers/fractional optimum | [I] | closed |
| product/slice moments and stopped descent | [I]/[C] | succeeds unless cap fails |
| average-conflict descent/bounded test | [I]/[C] | C.5a; adaptive arrival estimate (C.5a.7) open |
| sixth-moment/purge route | [I]/[O] | (C.12a.24)--(C.12a.25) open |
| Gate A | [O] | quenched cap preservation |
| capacity/rounding/zero-avoidance | [I]/[C] | positive all-depth cover open |
| Gate B | [O] | all-depth cover-down on the same bank |
| high OR derivative | [I]/[C] | exact block and holes inequality |
| deterministic central band | [I] | \(h=o(\sqrt b)\); exact \(F,G,P\) |
| append/fixed-split barriers | [I] | only (3.12) appends and fixed-split blocks |
| union-preserving recoding | [I] | at most two new rank-\(s\) targets per new cut |
| cumulative difference cycles | [I] | exact orbit inventory; fixed-block deep-rank no-go |
| cyclic normalization/rigidity | [I] | \(\nu\le\mu+(k-2)_+\); exact width forces (3.40)--(3.41) |
| cylinder completion/almost-cover equivalence | [I]/[C] | \(o(2^k)\) holes suffice after \(o(k)\) extension; almost-cover family open |
| finite completion without a dimension-only floor | [R] | 9.3: user refinement; checked constant \(13\), including \(t=0\) and \(h=0\) |
| facet-forest repair/envelope deficiency | [I]/[C] | 3.10: exact fixed-core deficit; useful hole geometry remains required |
| prescribed Catalan extension | [I]/[C] | 3.11: prescribed matching, owner avoidance, and optimal ten-deletion repair proved; middle forest open |
| inherited-symmetry breaking | [I] | 3.12: at least 28 changed adjacencies at \(W+3\); not a length gap |
| cyclic finite certificates/safe erasure | [I] | \(\mu(5)=12\) computer-assisted; \(\mu(7)=35\); \(k=9\) has 12 holes |
| bordered top-bit splice | [I]+[W] | length \(2n-d\); current \(k=16\) border is zero |
| adjacent shadows/GK chronology | [I]/[C] | converse closed; recursive block order costs \(9/8-o(1)\) |
| A+B compiler | [C] | same rows and all-depth holes |
| pairing catalogues/coset banks | [I] | balance and local disjointness, not selection |
| coherent-tour orbit | [I]/[C] | local facts closed; selector open |
| phase-packet banks | [I]/[C] | local facts/blocks closed; selector open |
| Gates \(C_{\rm F},C_{\rm Q}\) | [O] | internally disjoint selection with \(o(W)\) off-middle deficit |
| density-hole selectors | [C]/[O] | I.7 weakens deficit to \(o(4^b)\); selections still open |
| full coefficient one | [P] | 9.2: proposed PBBS proof for the same full-cube asymptotic coefficient; AI-agent internal reviews passed; external/formal verification not obtained |

Every refresh must preserve all [I]/[C] proofs, the \(k\le16\) breakthrough
table, recomputed [W] hashes and verification, word bodies as the sole
external data for [I]/[C] claims, conditional hypotheses, stopped-event
formulations, rank-depth scope, and the status of each unresolved gate.
The linked [R]/[P] research records must remain explicitly outside [I]/[C]
premises until their required proofs and verification are incorporated.

## 9. September 8 result records and proposed coefficient-one proof

This section records the new work without changing the self-contained
premises of the earlier [I]/[C] proofs. **[R]** means a result checked
through the identified proof and verification records. **[P]** means a
proposed proof reviewed internally by AI agents. Neither label means
external mathematical review or formal verification.

The coefficients below multiply the **same** width in the **same** problem:
\[
 \nu(k)\le(c+o(1))W(k),\qquad W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

| coefficient | scope | record status |
|---|---|---|
| \(c_9=1.180703803847\ldots\) | all ranks, every sufficiently large dimension | [I], complete proof in A.7 |
| \(1.177987\) | the same full-cube asymptotic bound | [R], user's selective-truncation construction and checked certificate |
| \(1\) | the same full-cube asymptotic bound, matching the leading lower bound | [P], proposed PBBS proof reproduced in 9.2 |
| \(1\), with relative error \(\sqrt{2\pi/k}+O(k^{-1})\) | all ranks and both parities, with an explicit finite length formula | [R], later height-adaptive construction in 9.13 |
| \(1\), with error \(2\sqrt{2\pi}k^{-3/2}+O(k^{-2})\) | all ranks and both parities; finite factors 1.01 above 5643, 1.001 above 6255 | [R], one-row period bound in 9.14 |
| \(1\), with error \(e^{-2^{-32}(\log k)^{6/5}}\) | every \(k\ge\lceil e^{e^{256}}\rceil\) | [R], many-row period bound in 9.14 |
| \(1\), with error \(e^{-2^{-50}k^{1/7}(\log\log k/\log k)^{6/7}}\) | every \(k\ge\lceil e^{e^{2^{21}}}\rceil\) | [R], profile sieve in 9.15 |
| \(1\), with error \(e^{-c\log k\log\log k}\) | every fixed \(c<1/(2\log2)\), eventually | [R], alternative multilevel bound in 9.16 |
| \(1\), with error \(e^{-2^{-330}k^{1/5}/(\log k)^{3/5}}\) | every \(k\ge\lceil e^{e^{2^{21}}}\rceil\) | [R], first-moment sieve in 9.17 |
| \(1\), with error \(e^{-c(\log k)^2}\) | every fixed \(c<1/(6144e^2)\), eventually; \(c=1/65536\) works | [R], alternative fractional-LCM bound in 9.18 |
| \(1\), with error \(e^{-(k(\log k)^2)^{1/5}/128}\) | every \(k\ge\lceil e^{e^{2^{21}}}\rceil\); also error \(\le e^{-k^{1/5}}\) there | [R], earlier logarithmic-gcd route, 9.19 |
| \(1\), with error \(e^{-k^{1/5}/128}\) | every \(k\ge2^{2048}+1\); eventual constants \(c<9/512\) also available | [R], fresh primes, 9.20 |
| \(1\), with error \(e^{-(3/5)(k(\log k)^2)^{1/5}}\) | every \(k\ge2^{131073}+1\) | [R], depth product, 9.21 |
| \(1\), with error \(e^{-c(k(\log k)^2)^{1/5}}\) | every fixed \(c<1/3\), eventually | [R], alternative stopped LCM, 9.22 |
| \(1\), with error \(e^{-(93/100)(k(\log k)^2)^{1/5}}\) | every \(k\ge2^{131073}+1\); additional specific finite pairs in 9.23 | [R], strongest recorded rate, 9.23 |

Thus coefficient one, if the proposed proof withstands further scrutiny,
would strengthen the \(1.177987\) result. It does not concern a different
normalization or only a central band. It also does not assert
\(\nu(k)=W(k)\) at finite \(k\): Section 2 already proves
\(B(k)=W(k)+\Theta(\sqrt{k})\). No new finite optimum is claimed.

**Construction and finite meaning.** The PBBS argument specifies a finite
word recipe; the new proposed theorem concerns its asymptotic length.
Trying all admissible integer depths and taking the shortest output avoids
needing an explicit slow-diagonal threshold. An executable implementation
of that recipe has not been delivered in this continuation. The
[construction companion](/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_CONSTRUCTION_20260908.md)
records the finite steps. The current verified actual word at \(k=17\) is
[the optimal 24,313-letter word](/Users/amir.nuriyev/Documents/problem/answers/k17_optimal24313.word),
with exact equality \(\nu(17)=B(17)=24,313\). Its complete
literal verification is recorded in 9.26; the independently implemented
height-adaptive recipe is in 9.13. Both are separate from the earlier
logarithmic compiler.
The [remote finite-ledger check](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md)
shows that the earlier fixed-aperture PBBS ledger could not certify an improvement
at that dimension; it does not rule out better words.

**Later user submission, awaiting audit.** The user subsequently supplied
an endpoint-optimized chain-partition argument claiming
\(\nu(k)\le(1.15325+o(1))W(k)\), with numerical upper enclosure
\(1.153248597553791677\ldots\). This new proof and its stated verifier have
not been independently checked in this continuation, so it is not promoted
to [R] here. It concerns the same full-cube leading coefficient. If the
coefficient-one proof is correct, its asymptotic conclusion is stronger.
Neither statement gives an explicit comparison of their vanishing error
terms or a finite crossover dimension.

### 9.1 User's selective-truncation improvement [R]

**Attribution:** the construction and energy argument were supplied by
the user. Their checked conclusion is
\[
 \boxed{\nu(k)\le(1.177987+o(1))W(k).}                 \tag{9.R.1}
\]
The proof retains A.7's fourteen-row eight-axis template and selectively
truncates twelve rows after absorbing the ninth chain. Each selected shore
permits removal only inside its empty, first-one and first-two threshold
masks; the simultaneous finite certificate leaves all 256 masks covered.

For eight length-\(2s\) chains and a ninth chain of length \(r\le2s\),
the principal terminal charge becomes
\[
 P_{\rm new}\le140rs^7-
       12s^6\left\lfloor\frac{[r-s]_+^2}{4}\right\rfloor. \tag{9.R.2}
\]
For actual lengths \(r\le a_1\le\cdots\le a_8\), put
\(A=2\lceil a_8/2\rceil=2s\), \(D=\sum_i(A-a_i)\) and
\(\alpha=35/32\). The padding-stable bound is
\[
 P_{\rm new}\le r\alpha A^7-
       12s^6\left\lfloor\frac{[r-s-D]_+^2}{4}\right\rfloor. \tag{9.R.3}
\]
The geometry audit retains the actual ninth-coordinate coverage,
contracted chains of possibly unequal lengths, nonempty truncated
families, and A.24's degree-seven endpoint and closing overhead.

Let \(S_9\) be the sum of nine independent three-dimensional unit-ball
Brownian exit times as in A.7, and \(M_p=\mathbb E S_9^{-p}\).
The exact expected-energy identity supplies the saving
\[
 C_*=
 c_9-\sqrt{\frac{\pi}{8}}\,
 \frac{(3-\frac{33}{4}M_1)^2}{48M_{5/2}}<1.177987.       \tag{9.R.4}
\]
It does not assume convergence of the shortest ninth radius. The
continuity and moment argument uses A.7's existing reciprocal domination.

**Verification record.** Geometry, padding, literal compilation, energy,
moment formulas, and the all-dimension passage passed internal
mathematical reviews. An independent small verifier ran only on `h100`, at
`/home/amodo/selective-truncation-audit-20260908.VGqood/verify.py`.
It confirmed retained multiplicity 314 with minimum one over all
256 masks; 1,000 upward-rounded rational terms, the full analytic tail,
and Machin intervals gave
\[
 M_1<0.348224,\quad M_{5/2}<0.077681,\quad
 \sqrt{\pi/8}>0.62665,\quad c_9<1.1807038039,
\]
and the exact coefficient enclosure
\[
 C_*<
 \frac{915071803984367}{776810000000000}<1.177987.       \tag{9.R.5}
\]
The source was copied back without local mathematical execution.
The user's displayed attachment labels contained no usable path or URL;
their external full verifier and reported sample fine-grid runs were not
read or rerun. The general geometry was checked by proof.

Detailed records:

- [Received proof and complete audit record](/Users/amir.nuriyev/Documents/problem/scratch/USER_SELECTIVE_TRUNCATION_PROPOSED_1_177987_20260908.md).
- [Geometry, padding and literal-word audit](/Users/amir.nuriyev/Documents/problem/scratch/USER_SELECTIVE_TRUNCATION_GEOMETRY_PADDING_COMPILER_AUDIT_20260908.md).
- [Independent exact mask and numerical verifier; run only on h100](/Users/amir.nuriyev/Documents/problem/scratch/USER_SELECTIVE_TRUNCATION_EXACT_AUDIT_20260908.py).

### 9.2 Proposed PBBS coefficient-one proof [P]

The equation numbers (1)–(15) in this reproduced manuscript are local to 9.2.
The separate editable source is
[COEFFICIENT_ONE_PROOF_20260908.md](/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_PROOF_20260908.md).

**Status: proposed proof with AI-agent internal reviews. It has not been
externally reviewed or formally verified. No gap was found in the current
reviews; their PASS labels must not be read as independent human certification.**

2026-09-08. Consolidated proof with supporting finite lemmas linked below.
The two new main lemmas and the passage through the existing literal word
compiler have passed root, direct-route and appendix mathematical audits.
This is a proof manuscript, not a formal proof-assistant certificate.
No mathematical computation was used in this PBBS proof. The manuscript
was recorded in MASTER_HANDOFF.md, Section 9.2, on 2026-09-08 as a proposed
proof [P], retaining the review status above.

#### Claimed theorem

Let nu(n) be the minimum length of a word of nonempty subsets of [n]
whose nonempty contiguous interval unions include every nonempty subset
of [n]. With W(n)=binom(n,floor(n/2)),

$$
\boxed{\displaystyle \nu(n)=(1+o(1))\binom{n}{\lfloor n/2\rfloor}.}
\tag{1}
$$

This holds in every sufficiently large dimension and covers every rank.
No explicit convergence rate is asserted.

The new argument proves abundant overlap for ALL Gaussian-short PBBS
repair intervals. It combines growing-depth stationary flux with an
exact renewal law for ACTUAL shifted triangles. The earlier raw-cone
renewal alone did not provide this physical interface.

#### 9.2.1 The physical reduction and exact base fibre

Work in dimension 2r+1; write R=sqrt(r) and
W_r=binom(2r+1,r)=(2r+1)Cat_r. The full PBBS factor has W_r edges.
A newborn lifetime T includes the consuming update, its native physical
same-label return has length 2T+1, and its repair trace has T+2 edges.

For fixed 0<c<C put H_c=floor(cR), H_C=floor(CR) and

    F_c={GOOD,Z_(0,0)=0,T<=H_c}, F_C={GOOD,Z_(0,0)=0,T<=H_C}.

GOOD is the established invariant profile condition. Actual base
incidence weights a uniform Dyck root by(T+2)1_(F_c)/mu_c, then samples
offset j uniformly in{0,...,T+1}. The accepted bounds are
mu_c=Theta_c(1) and mu_C=O_C(1). Let K_C count the ACTUAL F_C traces
containing the sampled edge. It will suffice to prove K_C tends to
infinity under this law.

Let D_s be the original depth-s pruned core, r_s its semilength,
p_s=2r_(s+1)+1 and ell_s=r_s-2r_(s+1)+r_(s+2). The exact inverse-pruning
rows Z_s are independent uniform weak compositions conditional on the
complete profile. On the safe base zero triangle through depth S, expose

    E_S=(complete original profile, all original rows at depths>=S, j).

Conditional on this environment, row s<S is uniform on P_s=p_s-s-1
free slots, and its slots0,-1,...,-s are fixed zero. The short-base
condition introduces no further weight on these free entries.

The physical clocks C_s and T_s select the next predecessor and next
same label. They commute, C preserves parity, and T reverses parity.
A zero gap gives the exact short-horizon rules C->C and T->CT under
pruning, including reverse grouping. Profiles and height are invariant.

#### 9.2.2 Growing-depth flux supplies eligible boundaries

Here and below all quoted finite identities are proved in the linked
supporting notes, with their original source dependencies recorded.
Set L=floor(r^(2/5)). The accepted sampled-base triangle and safety
bounds retain depth L with probability1-o(1): triangle failure costs
O_c(L^2/r), and the safe-profile exception is exponentially small in
r/L^2. This does not require simultaneous zero triangles for all partners.

Sum all upper completions to obtain the EXACT unnormalized stationary
core measure q_(r,L), divided by Cat_r, retaining GOOD and safety. Define

    M_L=sum_E q_(r,L)(E) pk(E).

The new profile calculation proves, for every fixed eta>0,

    M_L<=C_eta r/L^(3-eta)+superpolynomially small error.          (2)

Briefly, uniform original-depth concentration through2L gives
r_u=(1+o(1))r/(u+1), and convexity gives
d_u=r_u-r_(u+1)<=O(r/u^2). The exact zero-triangle probability is
product_(u<L)(p_u-1)_(u+1)/(ell_u+p_u-1)_(u+1). Its negative logarithm
is at least sum_(u<L)(u+1)ell_u/(p_u+ell_u). The exact Abel identity for
sum(u+1)(u+2)ell_u supplies2r log L-O(r). Thus the zero probability is
at most C_eta L^(-1+eta). Multiplication by d_L proves(2), including
the negligible exceptional-profile contribution. With eta=1/8,
M_L=O(r^(-3/20)).

On the base core let b_0 be the endpoint of Q_L=C_L^L T_L. For fixed K,
t_K=C_L^K(0) and Delta_K=C_L^K(b_0)-b_0. The exact stationary C index
is the peak count. The Q_L endpoint permutation preserves q_(r,L), even
when switching parity. Consequently

    sum q_(r,L)t_K=2K M_L, sum q_(r,L)Delta_K=2K M_L.     (3)

In the actual Palm sum the base weight is at most H_c+2. Markov and
offset counting give

    P_inc,c(t_K>=L)=O(r^(-1/20))+o(1),
    Delta_K=o(R), P_inc,c(2j<t_K)=o(1).                  (4)

Fix S>=K. Base zeros identify the first K common C boundaries at depths
S and L by reverse grouping inside the already short base endpoint
b_0<=2H_c+1; this supplies a finite safe horizon for that identification.
Require K extra zeros immediately after each base prefix in
rows S,...,L-1. Their exact composition-product probability tends to

    product_(u=S)^infinity(1-1/(u+2)^2)^K
                         =[(S+1)/(S+2)]^K.             (5)

The tail is uniform because the finite Abel bound
sum_(u=m)^(L-1)ell_u/r_(u+1)<=O(1/m) controls all remaining extra slots.
No growing-depth geometric approximation is used.

On this collar, C_S^(S+k)T_S reverse-groups from the FINITE endpoint
C_L^k(b_0). By(4) it passes the fixed larger cutoff C with probability
1-o(1). Grouping is used only after that safe endpoint test. If A_S
is the set of common boundaries passing the deep cutoff and the
sampled-edge overlap test, then

    liminf_r P_inc,c({0,...,K} subset A_S)
                              >=[(S+1)/(S+2)]^K.        (6)

#### 9.2.3 The exact actual multipoint law

Equation(4), together with h>=2L on the retained safe base, prevents
any repeated selected label before t_K at every upper depth. For fixed
S it is enough to restrict to the E_S-MEASURABLE event

    t_K<2(h-S)+1, n_S=2r_S+1>=2S+1.                    (7)

This has probability1-o(1) and guarantees no repeats for EVERY upper
completion, so the exact row law remains unchanged. The depth-S sites
0,-1,...,-K are original zero bits: they are first selected at even times.

Let I_s be the ORIGINAL initial insertion map, with

    I_s(0)=0, I_s(a)-I_s(a-1)=1+epsilon_(s,a)+2Z_(s,a),
    I_s(a+p_s)=I_s(a)+n_s.

Here epsilon records whether adjacent child bits differ. The physical
position cocycle is I_s plus a previous-visit count. That count vanishes
on(7), so the actual shifted labels are the nested static images

    xi_S(k)=-k, xi_s(k)=I_s(xi_(s+1)(k)).                (8)

Define Y_k by the FULL shifted zero triangle

    Z_(s,xi_(s+1)(k)-u)=0 for0<=s<S, 0<=u<=s.           (9)

Two exact geometric facts determine its joint law. First, insertion
maps expand integer distances and are periodic; thus
n_v+xi_v(k)>=n_S-k. Every query block lies in the same fundamental
arc(-p_s,0], for every fibre configuration. There are no cyclic collisions.
Second, for successive requested successes i<j and g=j-i, their row-s
blocks add exactly min(g,s+1) new positions. If g<=s+1, the earlier
HIGHER-row zero tests preserve a consecutive zero block through each
insertion, so the centers are exactly g apart. If g>=s+1, increasing
maps separate the centers by at least g, making the blocks disjoint.

Therefore, for0=k_0<...<k_m<=K, g_a=k_a-k_(a-1), and
M_s=sum_a min(g_a,s+1), revealing whole rows downward gives EXACTLY

    P(Y_(k_1)=...=Y_(k_m)=1 | E_S)
       =product_(s=0)^(S-1)
            (P_s-1)_(M_s)/(ell_s+P_s-1)_(M_s).          (10)

The locations depend on deeper rows, but the probability of M_s new
zeros depends only on the profile. No independence of survival events
or freshness after failed chronological tests is assumed. These events
need not equal original-index cones pointwise.

For fixed S,K, actual-incidence profile concentration gives
ell_s/(ell_s+P_s)->1/(s+2)^2. The limiting multipoint probabilities are

    product_a u_(g_a,S),
    u_(g,S)=1/(g+1)*[(S+2)/(S+1)]^g, 1<=g<=S.           (11)

For fixed K let S tend to infinity. Finite inclusion-exclusion identifies
the full indicator vector with the renewal process of masses u_n=1/(n+1).
It is proper: U(z)=-log(1-z)/z and

    F(z)=1-1/U(z)=1-integral_0^1(1-z)^t dt

has nonnegative coefficients
-integral_0^1(-1)^n binom(t,n)dt for n>=1, constant coefficient0 and
F(1-)=1. Its gaps are finite positive integers almost surely. Hence its
number R_K of renewals through K tends to infinity almost surely.

#### 9.2.4 Native partners, occupied support, and packing

If k is deep-eligible and Y_k=1, the tested finite C_S^S T_S word
reverse-groups through all rows to the native T_0 clock. It is H_C-short
and its trace contains the sampled edge. Row zero supplies its actual
top gap0, and invariant GOOD is preserved. Distinct k give distinct
physical births. Therefore K_C>=sum_(k=0)^K Y_k on{0,...,K} subset A_S.

For each fixed M, use this bound and a union bound. First send r to
infinity at fixed S,K, then S to infinity at fixed K, using(6),(11).
The resulting limsup of P_inc,c(K_C<=M) is at most P(R_K<=M).
Sending K to infinity proves

    K_C -> infinity under actual base-c incidence
                         for every fixed0<c<C.         (12)

The cutoff remains fixed; C=2c suffices. Equivalently choose finite K,
then finite S, then all r beyond a threshold. No independence between
eligibility and survival or interchange of growing parameters is needed.

The established deterministic cross-cutoff inequality is

    |U_c|/W_r<=mu_c P_inc,c(K_C<M)+mu_C/M.               (13)

Equations(12),(13) give |U_c|=o_c(W_r). The accepted negligible
top-gap/BAD incidence extends this to ALL births with T<=H_c.
For fixed epsilon>0 the low-height birth count and edge-capacity split
bound their maximum edge-disjoint packing P_c(r) by

    R P_c(r)/W_r<=C_c exp(-b_c/epsilon^2)
                              +|U_all,c|/(epsilon W_r).

Let r tend to infinity and then epsilon decrease to zero. Thus

    P_c(r)=o_c(W_r/sqrt(r)) for every fixed c>0.         (14)

#### 9.2.5 Literal word, all ranks, and every dimension

The audited PBBS owner-corridor theorem supplies every required central
target. Erosion, actual dominance-staircase cut charts, and the existing
product-SCD exterior word give the finite all-target ledger

    nu(2r+1)<=W_r+2H Cat_r
               +2(5H-1)P({T<=H-1})+2L_r(r-H),           (15)
    2L_r(r-H)/W_r<=C exp(-(H-1)^2/(8r)),

for2H<=r+1. All witnesses are ordinary contiguous interval unions;
the exact exterior boundary and every seam are charged in(15).

For each fixed integer j use H=floor(jR)+1 and(14). Choose successive
finite thresholds after which both normalized central excesses are
at most1/j. A sufficiently slow diagonal j(r)->infinity keeps H=o(r)
and2H<=r+1. Both central excesses and the exterior term then vanish,
giving nu(2r+1)<=(1+o(1))W_r. The exact trimmed one-coordinate lift
doubles the word length, while W(2r+2)=2W_r, proving the even case.
At a fixed right endpoint the interval unions are nested, so at most
one middle-rank target is realized there. Hence nu(n)>=W(n), proving(1).

#### Supporting proofs and contribution record

* [Exact stationary core law and flux](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md).
* [Full growing-depth eligibility and insertion-interface proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md).
* [Exact actual multipoint renewal and native-partner proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md).
* [Complete previously audited literal compiler, tail and parity chain](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md).

This consolidated manuscript also passed complete independent reads by
both direct-route and appendix, with no mathematical correction required.
The eligibility and renewal files have root, direct-route and appendix
full-file audits marked PASS. Both independent auditors also reread the
complete cross-cutoff and literal compiler chain. This manuscript
consolidates those checked arguments and retains their exact quantifiers.

The user's separate selective-truncation construction proves the explicit
coefficient 1.177987. Its geometry, padding, literal compilation, energy
identity and moment certification also pass independent checks; the
small exact numerical check ran only on h100. That construction and
the earlier finite-completion refinement are credited to the user.
Neither is used in the PBBS proof above.

The zero-budget renewal/packing theorem rederived during this continuation
already appeared in a September7 note. The new result here concerns the
FULL Gaussian-short family, including positive-budget runs.

### 9.3 User's finite completion refinement [R]

The original finite inequality (3.43) remains the starting point.
For a nonempty linear or cyclic base on \([k]\), \(k\ge1\), of length
or period \(m\le(1+\varepsilon)W(k)\), with \(0\le\varepsilon\le1\)
and at most \(h\) nonempty holes, put
\[
 \eta=h/2^k,\qquad t=\lfloor k\eta^{2/3}\rfloor,\qquad
 \delta_k=
 \begin{cases}
 0,&\text{linear base},\\
 (k-2)_+/W(k),&\text{cyclic base}.
 \end{cases}
\]
The user's finite improvement, with constant 16, passed review.
The audit sharpened that constant to 13:
\[
 \boxed{\frac{\nu(k+t)}{W(k+t)}
 \le1+\varepsilon+\delta_k+
       13\min\{\eta\sqrt{k},\eta^{2/3}\}.}              \tag{9.R.6}
\]
The cases \(t=0\) and \(h=0\) are included. There is no independent
dimension-only error for a linear base; a cyclic base retains only its
exponentially small cutting cost. The key finite estimates are
\[
 \nu(t)+1\le\frac{4\,2^t}{\sqrt{t+1}},\qquad
 \frac{2^tW(k)}{W(k+t)}\le1+\frac{t}{k+1}.
\]
This strengthens (3.45); its earlier displayed bound remains valid but
nonsharp. It is a completion theorem conditional on the specified base,
not itself a near-width almost-cover construction.

The full proof, boundary cases, every-target-dimension passage and
attribution are in
[the finite completion audit](/Users/amir.nuriyev/Documents/problem/scratch/USER_FINITE_CYLINDER_COMPLETION_WITHOUT_DIMENSION_FLOOR_20260908.md).

### 9.4 Exact-equality construction checkpoint [R]/[O]

The active objective is \(\nu(k)=B(k)\) in every dimension. No proof of
that statement, and no new optimal word beyond dimension 16, is asserted.
The detailed state and executable records are linked from
[the exact-goal checkpoint](/Users/amir.nuriyev/Documents/problem/scratch/EXACT_B_GOAL_CHECKPOINT_20260908.md).

**Current finite source component.** The six canonical PBBS components
containing every positive run of length three have 306 owners altogether.
Using all 51 cuts in each component yields the following Johnson path,
with all orientations forward:
\[
 116/33,\quad118/32,\quad122/31,\quad129/30,\quad138/29,\quad115/0.
\]
The notation is canonical cycle ID/cut position. Its 305 rank-eight
adjacency labels are distinct. Its 308-letter maximal depth-two source
is nonempty, has minimum letter rank seven, and replays all 306 owners.
With the other 140 components intact, it retains all 41,225 proper upper
targets. These are exact finite checks on `h100`, with a complete
612-option decision certificate in
[the Johnson-prefix record](/Users/amir.nuriyev/Documents/problem/scratch/K17_PBBS_ALLPORTS_JOHNSON_306_OWNER_PREFIX_20260908.md).

This prefix also has an explicit algebraic generalization. In dimension
\(2r+1\), for every \(r\ge3\), it joins all \(r-2\) canonical
components containing positive three-runs into a Johnson path with
\(3(2r+1)(r-2)\) owners and minimum internal positive residence three.
Its nonempty depth-two source has two more letters. The full seam proof
is in [the all-dimensional short-run-sector construction](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ALL_R_SHORT_RUN_SECTOR_JOHNSON_PATH_20260908.md).
Full upper-support preservation now has an all-dimensional proof. Every
target at least three ranks above the lower-owner rank has an untouched
maximum-height corridor; the next rank has a height-three witness, and
the immediate-upper cut colors have explicit recaptures. Thus the path
together with the untouched components covers all upper ranks for every
\(r\ge3\). See
[the full upper-preservation proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_GLOBAL_CORRIDOR_HEIGHT_AND_SHORT_SECTOR_FULL_UPPER_PRESERVATION_20260908.md)
and [its independent internal audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_SHORT_SECTOR_FULL_UPPER_PRESERVATION_INDEPENDENT_AUDIT_20260908.md).
All-dimensional facet injectivity and subsequent cycle joins are separate
requirements; this theorem alone supplies no optimal word.

The current global adjacent rank-eight palette misses only 43857 and
46420. Neither can be supplied by the initial or pivot exceptional cell,
or by the prefix/remainder adjacency. At most one can use the final
suffix, so at least one must be recreated inside the remaining path.
Moreover, 59 globally private rank-ten colors must be recovered on new
adjacencies in that remaining path; the prefix and exceptional cells
cannot supply them. Both requirements concern the same chronology.
See [the exact endpoint interface](/Users/amir.nuriyev/Documents/problem/scratch/K17_PBBS_ALLPORTS_JOHNSON_PREFIX_ENDPOINT_INTERFACE_20260908.md).

The earlier prefix obtained from 17 individually safe cuts per component
had three non-Johnson seams and is **ruled out for the proposed one-pivot
schedule**. The exact facet budget permits at most two non-Johnson steps
and repeated facet labels combined. The new prefix supersedes it;
[the obstruction proof](/Users/amir.nuriyev/Documents/problem/scratch/K17_PBBS_PREFIX_ONE_PIVOT_NOGO_AND_CONSECUTIVE_START_BUDGET_20260908.md)
does not rule out unrestricted exact words.

**Current compatible cycle mergers.** After the mountain C6, four genuine
three-to-one mergers produce cycles of lengths 475, 849, 1223 and 1513.
The final cycle combines original components 0 through 8, reducing the
remaining component count from 140 to 132. The actual source retains all
41,225 proper upper targets, its rank-eight adjacency counter, and minimum
positive residence six. The final two moves also preserve the exact local
rank-seven pair and rank-six letter counters. With the unchanged 102
protected prefix targets, all 19,448 rank-seven targets remain covered;
all 12,376 rank-six targets occur as letters. These are properties of a
bank of cyclic sources and one prefix, not a complete linear word.
See [the 1513-cycle construction and finite certificates](/Users/amir.nuriyev/Documents/problem/scratch/K17_NINE_COMPONENT_1513_FUSION_AND_PARENT_FAMILY_SATURATION_20260908.md)
and [the final lower-bank audit](/Users/amir.nuriyev/Documents/problem/scratch/K17_LOWER_BANK_FINAL_1513_INCREMENTAL_AUDIT_20260908.md).
Every endpoint of the tested 221-parent connector family lies inside this
1513-owner sector, so that entire family cannot join it to an outside
component, even through temporary splits. New connectors are needed.
The two missing rank-eight colors also persist; moves preserving their
counter cannot by themselves finish the proposed one-pivot construction.

**Arbitrary-endpoint rigidity, supplied by the user.** At equality length,
write the selected middle witnesses as
\(I_i=[i+\alpha_i,i+\beta_i]\). Their exact endpoint deficit is
\[
 D=\sum_i(d+\alpha_i-\beta_i)
   +\sum_i(\alpha_i-\alpha_{i-1})(d-\beta_i)\le\sigma(k).
\]
This is the endpoint form of the earlier deadline-particle loss identity.
It yields the explicit new equality-case consequences: at dimension 17,
at least 16,909 consecutive four-letter windows have distinct nine-set
unions, and selected witness lengths follow a subsequence of
\(1,2,3,4,3,2,1\). Each fixed upper rank has at most six targets absent
from consecutive unions of the selected middle chronology. These are
necessary conditions, not an existence proof. The proof and precise scope
are in [the arbitrary-endpoint audit](/Users/amir.nuriyev/Documents/problem/scratch/ARBITRARY_ENDPOINT_DEFICIT_AND_FULL_WIDTH_BLOCK_INDEPENDENT_AUDIT_20260908.md).

**Scope of the separate tagged-module route.** Exact fixed-hub incidence
equations obstruct the tested fixed-width architecture at dimension 19.
At dimension 17, a complete mixed-sector bank would force at least 1,287
repeated permitted rank-eight endpoint labels. Keeping its flat owner
chronology cannot achieve length \(B(17)\), even by shrinking letters:
shrinking can remove a facet occurrence but cannot let its protected
endpoint serve a different facet. The precise hypotheses and conservative
opening bounds are in
[the tagged-module analysis](/Users/amir.nuriyev/Documents/problem/scratch/EXACT_B_TAGGED_MODULE_SECTOR_MOMENTS_AND_LOWER_CAP_BURDEN_20260908.md).
This excludes that frozen chronology, not general tagged sources or
\(\nu(k)=B(k)\).

The current positive prefix still needs a compatible chronology for the
remaining 24,004 owners, complete upper coverage after all joins, and one
simultaneous lower-target compiler. Separate solutions of these conditions
do not automatically combine into a word of length 24,313.


### 9.5 Explicit quantitative coefficient-one bound [P]

The user's quantitative refinement of the PBBS argument now has explicit
numerical constants. Put
\[
 \gamma=2^{-2097160},\qquad
 k_0=\left\lceil\exp\!\left(\exp(2^{2097165})\right)\right\rceil.
\]
On the same finite PBBS inputs as Section 9.2,
\[
 \boxed{\nu(k)\le W(k)\bigl(1+(\log k)^{-\gamma}\bigr)
                 \quad(k\ge k_0).}
\]
The error multiplier here is **C=1**. A completely numerical version
valid for every integer \(k\ge2\) is
\[
 \boxed{0\le\nu(k)-B(k)
       \le\frac{2^{60}W(k)}{(\log k)^{\,2^{-2097160}}}.}
\]
All logarithms are natural. These are deliberately conservative constants,
not optimized numerical estimates. They provide no useful improvement at
dimension 17. The later finite height-adaptive improvement is in 9.13.

The explicit intermediate estimate uses \(A=2^{2097152}\). Uniformly for
\(r\ge2^{1000000}\) and \(1\le c\le\sqrt{\log\log r}\),
\[
 \frac{\nu(2r+1)}{W_r}\le
  1+\frac{c+2}{\sqrt r}
  +e^{A(c+2)^2}\frac{(\log\log r)^{3/2}}{\log r}
  +1024e^{-c^2/8}.
\]
The proof replaces the old iterated-limit step by a finite complete-vector
coupling, makes the cutoff dependence uniform using two query depths, and
averages the cutoff in the unnormalized incidence measure. The explicit
raw exponent is \(A_0=2^{80}e^{2^{20}}\), the low-height exponent is
\(2^{-53}\), and the stationary peak-flux constant is 11,000,000.
Every aperture is an actual finite compiler candidate, covering all ranks;
the exact one-coordinate lift supplies the other parity.

[The full numerical derivation and source audits](/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_EXPLICIT_RATE_20260908.md)
record all constants, thresholds and construction costs. This extension
has passed internal mathematical reviews; the inherited finite PBBS
lemmas retain the manuscript's proposed-proof status. It is not an external
or formal certification, and it does not establish exact equality.
The stronger, subsequently checked terminal-incidence refinement is
recorded in Section 9.7. It is not a premise of the bound above.

### 9.6 Recency-state fusion: valid theorem and embedding boundary [R]/[O]

The user's six-way interface is valid. For blocks \(H,C,D,G\) of sizes
4,4,3,6, the states
\[
 P_Y=(Y\mid C\mid D\mid H\setminus Y\mid G),\qquad
 Q_z=(H\cup\{z\}\mid C\mid D\mid G\setminus\{z\})
\]
obey \(T_{H\cup\{z\}}P_Y=Q_z\) for every two-subset \(Y\subset H\)
and \(z\in G\). Their twelve rank-nine prefixes are distinct.
More generally the construction provides
\(\lfloor k/2\rfloor-O(\log k)\) compatible ports with
\(O(\log k)\)-size joining letters.

For **one path starting at the empty state and some cycles**, partition
the nonterminal sources into coherent classes: every source in a class
can precede every destination currently assigned to that class. The
minimum number of routing components after classwise rewiring is exactly
the number of connected components of the routing-plus-class auxiliary
graph. Reusable anchors attain it in exactly one two-edge switch per
component reduction. This preserves all recency states, their complete
prefix-target inventory and the letter multiset. If the auxiliary graph
is connected, the result is one ordinary word with no added letters.
See [the full gadget and fusion proof](/Users/amir.nuriyev/Documents/problem/scratch/RECENCY_BICLIQUE_AND_COHERENT_CLASS_FUSION_INDEPENDENT_AUDIT_20260908.md).

The specified ports cannot simply be installed in the current k17 bank.
Their prefix-rank menus are \(2,6,9,11,17\) and \(5,9,12,17\), omitting
the rank-seven suffixes preserved by the present pair-union compiler.
More strongly, an interior endpoint of distinct rank-nine four-windows
must reach its rank-nine prefix in exactly four recency blocks; neither
port does. This rules out that direct embedding while keeping the current
flat owner schedule, including arbitrary caps preserving those windows.
Boundary or schedule changes require a fresh target-coverage audit.
[The precise local obstruction](/Users/amir.nuriyev/Documents/problem/scratch/K17_SIXWAY_RECENCY_PORT_OBSTRUCTION_IN_CURRENT_FLAT_BANK_20260908.md)
does not rule out the fusion theorem or unrestricted exact constructions.

### 9.7 Stronger numerical rate by terminal charging [P]

The user's terminal-incidence/profile-capping refinement passes internal
review on the same finite PBBS inputs. At every fixed \(c>0\), it proves
\[
 P_{\lfloor c\sqrt r\rfloor}(r)
       =O_c\!\left(\frac{W_r}{\sqrt r\log r}\right).
\]
The cutoff is prescribed, and both earlier iterated-logarithm losses are
removed. Charge each occupied edge to its latest-starting covering trace,
use invariant weight \(1+\sqrt r/(h+2)\), and cap each profile's occupied
fraction at one before averaging. The fractional moment then incurs
\(e^{Ap^2(c+2)^2}\), with a quadratic dependence on \(p\).

Using the same explicit \(A=2^{2097152}\), the boundary exponent is
\(\gamma_*=1/(4\sqrt{2A})\), with the stated
\(e^{C\sqrt{\log\log k}}\) correction. A fully numerical corollary is
\[
 \boxed{\nu(k)\le W(k)\left(1+(\log k)^{-2^{-1048580}}\right)
       \quad\text{for }k\ge
       \left\lceil\exp\!\left(\exp(2^{1048616})\right)\right\rceil.}
\]
Thus **C=1**, with an improved exponent and an explicit threshold. These
very conservative numbers still give no useful improvement at dimension
17 and do not prove exact equality.

[The complete numerical proof and independent audits](/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_TERMINAL_RATE_20260908.md)
retain the finite error term, the corrected exterior constant 2048 for
the floored cutoff, all profile-conditioning requirements, and the exact
parity lift. The inherited manuscript remains a proposed proof with
internal reviews, not external or formal certification. The subsequent
sharper-tail/shrinking-window improvement is now checked in Section 9.8.

### 9.8 Sharp exterior and the earlier numerical rate [R]/[P]

The user's sharper finite exterior theorem is proved for every
\(r\ge1\), \(1\le H\le r\):
\[
 \boxed{\frac{2L_r(r-H)}{W_r}
  \le\Theta_{r,H}\frac{\binom{2r}{r-H}}{\binom{2r}{r}}
  \le32\left(1+\frac{H^2}{r}\right)e^{-H^2/(r+1/2)},}
\]
\[
 \Theta_{r,H}=
 \frac{8(r+1)(r+H)(H^2-H+r)}{(2r+1)(r+2)^2}
                   \left(1+\frac1H\right)^3.
\]
This is an unconditional estimate of the existing literal product-SCD
tail word. Its proof retains the combined deficit and telescopes the
exact cubic binomial sum. At the actual aperture
\(H=\lfloor c\sqrt r\rfloor+1\), it gives
\(48(1+c^2)e^{-c^2}\) for \(r\ge16\), \(c^2\le\log\log r\).
Exact rational arithmetic on `h100` certifies that the bound at
\(r=1000,H=120\) is below \(0.000037923376246<1/25000\).

Combining this with the user's cutoff-shift removal and shrinking-window
argument gave the strongest recorded full-cube rate at that stage. The
later period results in 9.14–9.18 supersede it. Set
\[
 A=2^{2097152},\qquad
 k_*=\left\lceil\exp\!\left(\exp(2^{1048616})\right)\right\rceil.
\]
For every \(k\ge k_*\),
\[
 \boxed{\frac{\nu(k)}{W(k)}\le1+
 2^{76}\frac{(\log\log k)^{\,3/2+2^{-1048577}}}
                 {(\log k)^{\,2^{-1048577}}}.}
\]
At the same threshold the simpler **C=1** consequence is
\[
 \boxed{\nu(k)\le W(k)\left(1+(\log k)^{-2^{-1048578}}\right).}
\]
All logarithms are natural. These explicitly improve the earlier
numerical rates, but their conservative constants do not themselves give
a useful dimension-17 comparison; the later finite improvement is in 9.13.

[The complete numerical proof and audits](/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_SHARP_TAIL_RATE_20260908.md)
record the exact finite tail, shift-free conditional clock estimate,
shrinking-window floors, profilewise cap, fixed-parameter moment constants,
logarithmic balance and both parity conversions. The general logarithmic
exponent is \(1/(2\sqrt A)\), with iterated-logarithm power
\((3+A^{-1/2})/2\). This full-cube deduction retains the finite PBBS
manuscript's proposed-proof status and has internal reviews; the exterior
inequality itself does not depend on those PBBS inputs.

### 9.9 Genuine periodic fusion and exact partial-family optima [R]

The user's explicit 35-letter period and its eight rotations have now
been independently replayed on `h100`. Their alternating eight-edge
reassignment produces one 280-letter cycle, preserving exactly the union
of all 1,811 cyclic targets, with 280 distinct rank-eight triple unions
and 280 distinct rank-nine four-window unions. Every component refreshes
all 17 coordinates; these are actual periodic recency states.

The specified linear openings give exact partial-family optima:

| Target family | Number of targets | Required rank-nine targets | Required targets below nine | Optimal linear length |
|---|---:|---:|---:|---:|
| One component | 251 | 35 | 105 | 38 |
| Eight-component union | 1,811 | 280 | 807 | 283 |
| Fully rooted construction | 1,876 | 288 | 836 | 291 |

For each row the endpoint lower bound excludes delay two, and the
materialized word attains delay three. Thus joining the eight individually
optimal component covers saves exactly \(8\cdot38-283=21\) positions.
The rooted word's additional optimality follows from its independently
verified census, not just from the user's claim.

The exact rank potential also passes proof review. Starting from the
empty state, if \(b_s(P)\) counts prefixes below rank \(s\), then
\[
 N-D_s=L_s+b_s(P_N)+E_s,
\]
where \(L_s\) is total downward variation and \(E_s\) counts non-new-rank
steps that do not increase \(b_s\). An upward step is at most one and
cannot introduce a new rank-\(s\) target. For the rooted word,
\(291-288=0+3+0\) at rank nine. Conversely, the earlier six-way gadget
has six downward steps and therefore cannot occur in a 24,313-letter
universal word; its abstract transition theorem remains valid.

[The independent finite proof and all word artifacts](/Users/amir.nuriyev/Documents/problem/scratch/USER_NATIVE35_GRAFT280_AND_ROOTED291_INDEPENDENT_CERTIFICATE_20260908.md)
include a witness interval for every counted target, both requested
openings, the full recency-state replay and the rank-potential ledger.
The user's separately mentioned 24,313-state static inventory was not
supplied and has not been verified here. These partial-family optima
do not prove \(\nu(17)=24313\), and the existing 1513-sector PBBS bank
has not been changed by this verification.

### 9.10 Inverse-logarithmic rate with numerical constants [P]

The user's linear-budget geometric-clock theorem and its transfer to
the original finite composition rows pass complete internal proof review.
An explicit conservative result is
\[
 \boxed{\nu(k)\le W(k)\left(1+2^{400000}
              \frac{(\log\log k)^{3/2}}{\log k}\right),\qquad
 k\ge\left\lceil\exp\!\left(\exp(4194304)\right)\right\rceil.}
\]
All logarithms are natural. The logarithmic exponent is one, independent
of the old Gaussian-envelope constant. The geometric theorem has
\(C_{\rm pgf}=20e^{54}C_Z\), \(C_{\rm budget}=64e^{54}C_Z\), with
\(C_Z=2e^{2^{18}}\). Query depth
\(d=\lfloor2^{-40}\sqrt r/((b+1)Q)\rfloor\) gives the global original-row
bound \(\mu_H(\Pi)\le2^{74}e^{2^{18}+55}(b+1)^3Q^2\).
Latest-start charging followed by dyadic division by actual trace length
then gives the inverse logarithm. The full inherited finite PBBS chain
retains its proposed-proof status; internal audits are not external or
formal certification.

[The complete numerical proof and separate audits](/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_INVERSE_LOG_RATE_20260908.md)
include the prefix restart, exact row likelihood comparison, every finite
guard, error absorption and both parity conversions. The newer
height-adaptive construction in 9.13 supersedes this rate and has completed
its separate finite structural proof review.

### 9.11 A verified optimal 20-letter singleton extension [R]

The rooted 291-letter partial word from 9.9 has an explicit 20-letter
continuation supplying all fourteen previously missing singleton targets.
Every appended endpoint has a globally new rank-eight triple and
rank-nine four-window. The resulting 311-letter word covers 1,979 targets,
including all 17 singletons and 308 targets at each middle rank, while
retaining every one of the original 1,876 targets.

Twenty is minimal among continuations preserving rank-eight triple
windows: fourteen required singleton letters need at least six
nonsingleton separators, since three consecutive singleton letters cannot
have an eight-element union. The resulting target family itself has exact
minimum 311, because its 308 required nine-sets and 893 required lower
targets exclude delay two by the endpoint bound.

[The literal word, complete interval census and proof](/Users/amir.nuriyev/Documents/problem/scratch/NATIVE291_TO311_OPTIMAL_SINGLETON_EXTENSION_20260908.md)
also record 37 repeated below-eight incidences. Any optimal full-cube
completion retaining this prefix must continue its initial four-window
block for at least another 16,638 positions. This is an extension
requirement, not a proof of eventual completion.

### 9.12 Verified 25,374-letter full-cube word [W]

The user supplied the actual word, and an independent bounded `h100`
run verifies
\[
 \boxed{24313\le\nu(17)\le25374.}
\]
It has exactly 25,374 nonzero 17-bit letters, covers all 131,071 nonempty
targets by ordinary intervals, and every recorded witness passes an
independent segment-tree range-OR check. It saves 371 positions against
the previous 25,745-letter word and leaves an exact-bound gap of 1,061.

[The verified word, certificate, all witnesses and proof](/Users/amir.nuriyev/Documents/problem/K17_UPPER25374_VERIFIED_20260908.md)
identify the byte body by SHA-256
`16951cef9e2efff841c6bbf9cc72f2061f35650dda850714fcceee7a7bb43208`.
The checker has a separate code audit. This upper bound requires no
asymptotic theorem or trust in the user's optimization search. The
intermediate matching, Hall and deletion certificates were not supplied
and have not been independently reproduced; the literal word alone
suffices for this finite result.

### 9.13 Height-adaptive polynomial rate and a 24,957-letter word [R]/[W]

The user's strict-height refinement and height-adaptive construction pass
complete internal proof review. For every odd \(n=2r+1\ge3\),
the explicit finite construction bound is
\[
 \boxed{\nu(n)\le W_r+
           \left\lfloor\frac{2^{n+1}-3W_r}{n}\right\rfloor,\qquad
 W_r=\binom{2r+1}{r}.}
\]
The exact even lift gives \(\nu(2r+2)\le
2W_r+2\lfloor(2^{2r+2}-3W_r)/(2r+1)\rfloor\). Consequently
\[
 \nu(k)\le W(k)\left(1+\sqrt{\frac{2\pi}{k}}+O(k^{-1})\right),
\]
with verified exact thresholds \(\nu(k)<1.1W(k)\) for \(k\ge569\)
and \(\nu(k)<1.01W(k)\) for \(k\ge62233\). The error also implies
\(0\le\nu(k)-B(k)=O(W(k)/\sqrt k)\).

The construction chooses each PBBS owner's own invariant height as its
aperture. The strict-height refinement of the finite global-maximum
corridor lemma supplies each nonempty rank-\((r-q)\) target in a cycle
of height at least \(q+1\). The interleaved cycle has exactly the same
height, so every rank is covered without
an exterior word or residence repair. The cycle-period residue and finite
reflection count bound the whole opening charge. This route uses the
finite corridor and cycle identities, not the clock/renewal proof chain.

For each cycle, the nonzero erosion letters are
\(D_i=\bigcap_{j=0}^{h}X_{i+j}\). Emitting one period followed by its
first \(2h-1\) letters covers all required windows. The equality-edge
residue proves that each period is divisible by \(n\), and reflection
counting gives \(\sum_{|A|=r}(M(A)-m(A))=2^n-W_r\). These yield the
displayed finite bound with every opening and join included.

At \(k=17\), a single fixed canonical construction on `h100` confirms
146 cycles and total height 519. The full theorem word has length 25,202
and is universal. Trimming each collar to \(h\) gives 24,829 letters with
128 holes (65 at rank ten, 49 at eleven, 14 at twelve). Appending those
128 masks gives the stronger verified result
\[
 \boxed{24313\le\nu(17)\le24957.}
\]
Both the construction checker and a separate root-owned literal replay
verify all 131,071 targets and independently recheck their nonwrapping
witnesses. The word's SHA-256 is
`dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db`.
It improves 25,374 by 417 letters and 25,745 by 788; the remaining gap
to \(B(17)\) is 644.

The user's reported 24,969-word used an unspecified cut/order and was not
supplied. Our fixed convention gave 128 rather than 140 holes, with no
cut or ordering search; boundary witnesses can depend on those choices.
[The complete construction proof, internal audits, exact threshold checks,
generator, word and all witnesses](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md)
record the distinction. The general theorem uses the retained finite
global-maximum corridor and matching identities, not the much larger
proposed clock/renewal chain. Internal review is not external or formal
certification. Exact equality with \(B(k)\) remains open.

### 9.14 Period improvements, explicit thresholds and verified 24,668 [R]/[W]

The invariant incoming-gap row has least cyclic period \(d\), and the
physical owner cycle has period \(v\). Persistent particle labels give
\(nd\mid v\). If the first \(L\) rows are primitive, their fixed-label
returns descend at the same time, proving
\[
 \operatorname{lcm}_{0\le s<L}(n_sn_{s+1})\mid v,
 \qquad n_s=2r_s+1.
\]
No product or coprimality assumption is made. The unchanged all-rank word
has exact normalized overhead
\[
 \frac{N_n-W(n)}{W(n)}=\mathbb E_A\frac{2h(A)-1}{v(A)}.
\]
Uniformity is over original middle states, not over cycles.

For odd \(n\ge5\), define the entirely rational quantity
\[
 \beta_n=4n(n+1)(242/243)^n+n(99/100)^n.
\]
The first-row composition count, profile concentration, reflection
moments and cyclic-edge moments give the explicit finite bound
\[
 \boxed{\nu(n)\le W(n)+\left\lfloor
 \frac{2^{n+2}+2W(n)}{n^2}+W(n)\beta_n\right\rfloor.}
\]
The floor applies to the whole displayed sum. The even lift doubles both
the word length and width. Thus the relative error is
\(2\sqrt{2\pi}\,k^{-3/2}+O(k^{-2})\).
The normalized expression decreases along odd \(n\ge485\). Exact
rational comparisons on `h100` prove
\[
 \nu(k)<1.01W(k)\quad(k\ge5643),\qquad
 \nu(k)<1.001W(k)\quad(k\ge6255).
\]

A stronger asymptotic estimate follows from many primitive rows. For
\(L=\lfloor r^{1/6}/\log r\rfloor\), the original-profile concentration
and exact repetition counts give failure probability at most
\(e^{-2^{-26}(\log r)^6}\) when \(\log r\ge2^{20}\). On the good event,
\(v\) has more than \(\tfrac12 n^{1/6}/\log n\) distinct divisors at
most \(n\). A finite elementary prime/divisor estimate gives
\(\log v\ge2^{-24}(\log n)^{6/5}\). Inserting this in the exact
state-average charge proves
\[
 \boxed{\nu(k)\le W(k)\{1+e^{-2^{-32}(\log k)^{6/5}}\},
 \qquad k\ge\lceil e^{e^{256}}\rceil.}
\]
Both parities and every numerical guard are checked in
[the consolidated period proof](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PERIOD_BOUNDS_20260908.md).
This implies \(0\le\nu(k)-B(k)=O_m(W(k)/k^m)\) for every fixed
\(m>0\). It is asymptotically stronger than the one-row estimate, whose
finite thresholds remain useful. The latest profile-sieve and joint-profile
submissions are separate deductions; their current audit status must be
read in their own records.

Separately, the supplied 24,715-word passed complete verification, and
the subsequently supplied **24,668-word** passed the same independent
`h100` checks. Thus
\[
                 \boxed{24313\le\nu(17)\le24668.}
\]
All 131,071 nonempty targets have ordinary nonwrapping witnesses, each
independently rechecked by segment-tree OR. All letters are nonzero. The
current SHA-256 is
`22af061610f9c6cb4708ccca77c8d8008f251a1cc40f92858ca79bf7ad2ffff6`.
The [actual word and complete certificate](/Users/amir.nuriyev/Documents/problem/K17_UPPER24668_VERIFIED_20260908.md)
prove the finite upper bound independently of all PBBS premises. This
saves 47 letters against 24,715 and leaves 355 to \(B(17)\). The user's
rewrite search was not supplied or reproduced; it is not a premise of
the literal check. Earlier words and their checks remain retained.

All general deductions above passed internal proof review on the linked
finite inputs. They are not external reviews or proof-assistant
formalizations. Exact equality \(\nu(k)=B(k)\) remains open.

### 9.15 Exact profile sieve and the explicit one-seventh rate [R]

The exact original profile weight is
\(\prod_j\binom{a_j+a_{j+2}}{2a_{j+1}}\), with terminal zeros.
After exposing all but every third size in
\([\lceil L/2\rceil,L-2]\), the free sizes have independent full
conditional laws. A free \(x=a_s\) has weight
\(\binom{A+x}{2b}\binom{b+c}{2x}\binom{x+D}{2c}\) on its full
convexity interval. Under exposed-neighbor regularity, the law is unimodal
and has maximal atom at most \(1024\sqrt{(L+1)^3/r}\).

A missing-prime second-moment sieve excludes each prescribed short period
with a uniform probability at each free depth. Independence is used only
under the full conditional law. Free-coordinate regularity is dropped
before multiplying probabilities; primitivity is used only to make the
divisibility tests necessary. With
\(L=\lfloor(r\log r/\log\log r)^{1/7}\rfloor\), the original-state
period tail and exact collar charge yield
\[
 \boxed{\frac{\nu(k)}{W(k)}\le1+
 e^{-2^{-50}k^{1/7}(\log\log k/\log k)^{6/7}},\qquad
 k\ge\lceil e^{e^{2^{21}}}\rceil.}
\]
The [complete proof and explicit constants](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PROFILE_SIEVE_RATE_20260908.md)
include the elementary prime-sum error \(32/\log Y\), original-law
bookkeeping, numerical domain and both parities. This is a valid
intermediate rate; 9.17 is stronger asymptotically.

### 9.16 Joint-profile atoms and a complementary exact period formula [R]

Under the auxiliary measure \(\Pr_*(D)=4^{-|D|}/2\), inverse pruning
gives exact negative-binomial parent kernels. A Narayana/binomial
calculation bounds the depth-\(L\) core mass. Multiplying conditional
atom bounds, then dividing by the actual original-size probability,
proves
\[
 \Pr_r(r_1=a_1,\ldots,r_L=a_L)
 \le16(L+1)((L+1)!)^{3/2}r^{-L/2}
\]
when \(a_j\ge r/[2(j+1)]\). The user's weaker factorial-square form
also follows. For odd \(n\ge4096(L+3)^6\), the exact good-profile error is
\[
 \delta_{n,L}=2(L+1)n(n+1)e^{-n/[2048(L+3)^6]}
                         +Ln\,2^{-n/[6(L+3)^3]}.
\]
Writing \(A_L=16(L+1)3^L((L+1)!)^2\) and \(d(n)\) for the divisor
count, a finite divisor-tuple injection proves
\[
 \frac{N_n-W(n)}{W(n)}\le\delta_{n,L}+n^{-L}
 +A_Ln^{-L/2}d(n)^L(1+L\log n)^{2^L}.
\]
Taking \(L=\lfloor\log_2\log n-2\log_2\log\log n\rfloor\) gives
relative error \(e^{-c\log k\log\log k}\) for every fixed
\(c<1/(2\log2)\), eventually. This is an alternative proof with an
explicit finite expression, not an improvement over 9.15.

There is also a new exact physical period statement. For a full profile
ending at \(n_h=1\), let \(M=\operatorname{lcm}_{s<h}(n_sn_{s+1})\).
Then \(f^M(A)=A\) always. The equality-edge update forces uniform site
selection counts at every child return, allowing the return to be lifted
upward at the same time. Hence all physical periods are odd and the
\(f\)- and \(f^2\)-periods coincide. If every gap row is primitive,
the period equals \(M\). The one-site case is checked separately.
[The full joint-profile, divisor and period record](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_MULTILEVEL_PROFILE_BOUND_20260908.md)
links the independent finite proofs.

### 9.17 Reverse-profile concentration and the first one-fifth rate [R]

The same auxiliary measure gives an exact law for the original second
difference conditional on the entire deeper profile:
\[
 \ell_s\sim\operatorname{NB}(2a_{s+1}+1,q_s),\quad
 q_s=(s+2)^{-2},\quad
 \mu_s=\frac{2a_{s+1}+1}{(s+1)(s+3)}.
\]
Its two-sided tail outside \([\mu_s/2,2\mu_s]\) is at most
\(2e^{-\mu_s/32}\). This law is applied before fixed-size conditioning;
the inverse original-size probability is then explicitly charged, at
most \(12r^2\).

Set \(\Gamma(r)=r^{1/5}/(\log r)^{3/5}\) and
\(L=\lfloor\Gamma(r)\log r\rfloor\). On
\(\log\log r\ge2^{20}\), coarse relative-profile control, the reverse
tails and exact composition repetition counts give total bad probability
at most \(e^{-2^{-26}\Gamma(r)^2}\). Exposed data admitting even one
good completion suffice to bound the entire free conditional law by
maximal atom \(2^{20}/\Gamma(r)\). The law is not conditioned on
the good completion.

Choose absent primes between \(2^{-296}\Gamma(r)\) and
\(2^{-40}\Gamma(r)\). At most six of them can divide any integer in
the entire conditional support. This pointwise cap permits a first-moment
sieve with error proportional to the number of primes, improving the
second-moment argument in 9.15. Candidates \(v\le e^{2^{-320}\Gamma(r)}\)
are rejected at enough independent conditional depths to give a short-
period probability at most \(e^{-\Gamma(r)/512}\). The exact state-average
collar charge consequently yields
\[
 \boxed{\nu(k)\le W(k)\left\{1+
 \exp\left[-2^{-330}\frac{k^{1/5}}{(\log k)^{3/5}}\right]\right\},
 \qquad k\ge\lceil\exp(\exp(2^{21}))\rceil.}
\]
All constants, finite guards, full-law conditioning and both parities are
proved in [the complete reverse-profile record](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_REVERSE_PROFILE_RATE_20260908.md).
The relative error is eventually at most \(e^{-c_\theta k^\theta}\)
for every fixed \(0<\theta<1/5\), including \(1/6\). The additive
gap is at most the displayed relative error times \(W(k)\), and need
not vanish. The subsequent logarithmic-gcd argument in 9.19 improves
this exponent by a full factor of \(\log k\).

### 9.18 Fractional LCM moments: an alternative squared-logarithm rate [R]

For \(L\ge2^{16}\), \(1/3\le\beta\le1/2\), \(0<\eta\le1/6\),
and \(\alpha=1+\eta-\beta\), a uniform finite Euler-product argument proves
\[
 \sum_{1\le u_1,\ldots,u_L\le M}
       \operatorname{lcm}(u_1,\ldots,u_L)^{-\alpha}
 \le M^{\beta L}(1+\eta^{-1})^L
 \exp\left[96\left(\frac{2L}{\log L}\right)^{1/\beta}\right].
\]
The proof retains the maximum-exponent factor on large-prime supports;
all common factors and prime powers are counted. Applying the original
joint-profile atom bound of 9.16 gives the finite word estimate
\[
 \frac{N_n-W(n)}{W(n)}\le\delta_{n,L}+
 nA_Ln^{-(1/2-\beta)L}(1+\eta^{-1})^L
 \exp\left[96\left(\frac{2L}{\log L}\right)^{1/\beta}\right]
\]
on the stated parameter ranges and \(n\ge4096(L+3)^6\).
Taking \(\beta=1/2-1/(2\log\log n)\), \(\eta=1/\log n\), and
\(L=\lfloor\lambda\log n\log\log n\rfloor\), then optimizing
\(\lambda\), proves
\[
 \boxed{\nu(k)/W(k)\le1+e^{-c(\log k)^2}
 \quad\text{for every fixed }0<c<1/(6144e^2),}
\]
eventually. In particular \(c=1/65536\) works. No numerical starting
dimension is certified for this particular form. This improves 9.16,
but is asymptotically weaker than both 9.15 and 9.17.
[The fractional-LCM proof and audits](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_FRACTIONAL_LCM_BOUND_20260908.md)
record the finite constants, optimization and original-law scope.

The accompanying 24,660-word claim has only a sandbox link here; the
expected local file was absent. Its claimed eight-letter saving is
awaiting the actual word body and a complete independent replay. The
current verified finite bound remains \(24313\le\nu(17)\le24668\).
None of these general rates proves exact equality with \(B(k)\).

### 9.19 Logarithmic-gcd reverse tests and the endpoint one-fifth rate [R]

The reverse negative-binomial sum law and uniform composition fibre
combine into an exact full-row product under the auxiliary critical-size
measure: conditional on the entire deeper profile, row coordinates are
independent geometric variables with parameter \(q_s=(s+2)^{-2}\).
For odd row length \(p\), summing all masses gives nonprimitivity
probability at most \(p e^{-2pq_s/3}\). This removes the separate
second-difference concentration event from 9.17.

The arithmetic replacement is also explicit. For a unimodal integer
law \(U\) of maximal atom \(\rho\), with \(2U+1\ge Y_0>1\),
\[
 \Pr(2U+1\mid v)\le
 \frac{\log(2+\log v)+20+2\rho\log v}{\log Y_0}.
\]
It follows by expanding \(\mathbb E\log\gcd(2U+1,v)\) over prime
powers and using the full-law residue discrepancy \(2\rho\).
The bound allows infinite support and requires no missing-prime band or
local-profile smoothing estimate.

Set \(X=\log r\), \(J_r=(rX^2)^{1/5}\), and \(L=\lfloor J_r\rfloor\).
Under one-percent coarse ranges for the two child sizes, the entire
reverse parent law has maximal atom at most \(\sqrt{(L+2)^3/r}\) and
\(2a_s+1\ge r/(L+2)\). On \(\log\log r\ge2^{20}\), every candidate
\(v\le e^{L/16}\) passes each reverse divisibility test with probability
at most one half. A tower of successive conditional expectations gives
an auxiliary probability at most \(2^{-L}\) for all tests and coarse
ranges. This is not independence of pruning sizes. Fixed-size conditioning
is then paid once, at cost at most \(Q_r=2(r+1)(2r+1)\).

The coarse-profile and geometric-row bounds make the bad event at most
\(e^{-L}\). Primitivity is used only to make the divisibility tests
necessary. A union over candidates yields short-period probability at
most \(e^{-L/3}\), and the exact state-average collar charge is at most
\(e^{-L/32}\). All of these comparisons hold on the explicit domain
above, not merely with an unspecified eventual qualification.

For both parities, the exact lift and finite comparison between \(r\)
and \(k\) consequently give
\[
 \boxed{\nu(k)\le W(k)\left\{1+
 \exp\left[-\frac{(k(\log k)^2)^{1/5}}{128}\right]\right\},
 \qquad k\ge\lceil\exp(\exp(2^{21}))\rceil.}
\]
The same threshold also gives
\[
                         \boxed{\nu(k)\le W(k)(1+e^{-k^{1/5}}).}
\]
The [complete logarithmic-gcd proof and finite audits](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_LOG_GCD_RATE_20260908.md)
record the row normalization, constant20, reverse tower, exceptional
probabilities and parity conversion. The threshold is conservative and
not optimized. These are internally reviewed deductions on the retained
finite inputs, not external or formal certification.

This was the strongest recorded general rate at that stage. Sections
9.21 and 9.23 sharpen its coefficient and starting dimension. The word
construction itself is unchanged, and exact equality remains open.
The then-verified finite upper bound was 24,668; the later supplied
24,658-word in 9.20 supersedes it.

### 9.20 Fresh primes, explicit onset and the verified 24,658 word [R]/[W]

The [complete fresh-prime proof](HEIGHT_ADAPTIVE_FRESH_PRIME_RATE_20260908.md)
and its independent audit retain the exact reverse geometric-row law,
but select one new prime per successful upward step. A killed auxiliary
trajectory exceeding the required original size cannot contribute after
fixed-size conditioning. The selected primes are distinct and divide the
physical period on primitive rows; no coprimality of pruning sizes is used.

For odd n, let B=n/[2(L+1)], mu=(L+1)/sqrt(B), and

    kappa=[log Y+16+2mu Y log n]/log B+L(1/Y+2mu).

For integer L>=2, Y>=2, B>1 and kappa<=5/8, the exact constructed
relative overhead is at most

    2n(n+1)e^[-n/(8(L+1)^2)]
    +L n^2(n+1)e^[-n/(3(L+1)^3)]
    +n(n+1)e^[-9(L-1)/64]+nY^[-(L-1)/16].

Taking L=floor(n^(1/5)/8), Y=n^(1/5) gives every eventual constant
c<9/512 in the exponent -c k^(1/5). The explicit choice c=1/128
holds for every k>=2^2048+1. This is weaker asymptotically than the
logarithmic-gcd scale but has a smaller certified starting dimension.
The audit retains every conditioning factor and proves the onset;
user-reported verifier suites were not treated as independently executed.

Separately, the actual supplied [24,658-letter word and certificate](K17_UPPER24658_VERIFIED_20260908.md)
pass all131071 nonempty-target checks and independent range-OR replay:

    24313 <= nu(17) <= 24658, gap345.
    SHA256 24f7f831b7446e942cc0927472296b2d20069f694b8bbad6374e65cc07b6f7fb.

Its literal doubled lift has49316 letters and passes all262143 targets
at18, giving gap693 aboveB(18)=48623. These finite certificates have
no PBBS or asymptotic premise. Search regeneration was not supplied.

### 9.21 Sharp residues and a depth product with coefficient 3/5 [R]

The [full depth-product proof and finite audits](HEIGHT_ADAPTIVE_DEPTH_PRODUCT_RATE_20260908.md)
give, for every k>=2^131073+1,

    nu(k)/W(k) <=1+exp[-(3/5)(k(log k)^2)^(1/5)].

For a unimodal integer law of maximal atom rho, layer-cake intervals
prove the sharp residue discrepancy (1-1/d)rho. Finite Stirling bounds
give NB maximal atom<=1.001/sqrt(2pi pq) whenever pq>=1000,q<=1/4.
With T=(r(log r)^2)^(1/5), L=floor2T and candidate log-period<=.7T,
the reverse-step factors are bounded by

    b_s=.251+.25((s+2)/T)^(3/2).

Independent exact rational arithmetic gives the integral lower bound
1.411587409289687... . A finite shifted-sum debit below4 gives product
<=exp(-1.41T), rather than merely a limiting Riemann assertion.
Successive conditioning, the original-size factor, period union and
collar charge give error<=exp(-.69T). The explicit local domain
log r>=65536 and a finite parity comparison give the displayed onset
and coefficient3/5. No external or formal certification is asserted.

### 9.22 A stopped logarithmic-LCM alternative [R]

The [complete stopped-LCM proof](HEIGHT_ADAPTIVE_STOPPED_LCM_RATE_20260908.md)
uses the exact increment log N-log gcd(Q,N) while the running LCM
satisfies log Q<H. The gcd expectation is bounded by log H+18+2mu H.
The conditional killed/stopped-process argument gives a fully specified
four-term finite error bound without independent-trial assumptions.

For w=(n(log n)^2)^(1/5), L=floor(w/2), H=w/3,
alpha=1/1024 and theta=log log n, the failure constant tends to
2624/5115<5131/10000. Exact rational logarithm enclosures verify
-log(5131/10000)>2/3. This proves every fixed coefficient c<1/3
on the same w scale, eventually in both parities. It is a valid
alternative but weaker than9.21 and9.23; no new finite word is implied.

### 9.23 Reciprocal-period charging, coefficient 0.93 and finite certificates [R]

The [harmonic-period proof and exact numerical certificates](HEIGHT_ADAPTIVE_HARMONIC_PERIOD_RATE_20260908.md)
retain the reciprocal period in the actual overhead. Since periods are
multiples of n, a uniform candidate point-probability bound B costs
only B times a harmonic sum, at most B(1+M) up to periods exp M.
The exponential candidate-count debit in9.21 disappears.

Use integers L>=1,z>=2 and real M>=0,0<delta<=1/6 satisfying
delta sqrt(r)/(L+2)>=4 and2(1-delta)r/(L+2)^3>=1000. Put

    Q_r=4(r+1)sqrt(r),
    A_z(M)=sum_(prime p<=z) log(p)/(p-1)+M/z,
    rho_s=1.001(s+2)^(3/2)/[2sqrt(pi(1-delta)r)],
    y_s=4(1-delta)r/(s+2)-2(1+delta)r/(s+3)+1,
    b_s=min(1,[A_z(M)+M rho_s]/log y_s),
    E_A=2(L+1)exp[-(delta sqrt(r)/(L+2)-4)^2/6],
    E_P=Q_r L(3r+1)exp[-4(1-delta)r/(3(L+2)^3)].

Then the finite construction satisfies, with no unspecified constants,

    (N_r-W_r)/W_r
      <=4sqrt(r)e^(-M)+Q_r(1+M)product_s b_s+E_A+E_P.

The integer restriction on z makes p>z imply p-1>=z. Every submitted
application already satisfies it. Full auxiliary-kernel conditioning,
primitive-row scope, height prefactor and all numerical guards pass
internal proof review.

The choices delta=.01, L=floor(25T/16), M=1.07T,z=floor M give
b_s<=.251+.38((s+2)/T)^(3/2). The independently reproduced downward
integral sum is exactly1.074181933864880728>1.073. The finite shifted
product, harmonic debit, and collar charge give error<=exp(-1.069T).
The root and independent audits supply the explicit sufficient domain
log r>=65536 and the finite parity comparison, proving

    nu(k)/W(k)<=1+exp[-.93(k(log k)^2)^(1/5)]
    for every integer k>=2^131073+1.

Direct evaluation of the finite inequality, with delta=.1 and z=M,
gives additional certificates independently of that onset:

| r | L | M | Dimension pairs | Relative excess |
|---:|---:|---:|---|---|
| 10^12 | 1100 | 790 | 2,000,000,000,001 and2,000,000,000,002 | <10^-330 |
| 10^14 | 3500 | 2250 | 200,000,000,000,001 and200,000,000,000,002 | <10^-950 |
| 10^16 | 10200 | 6150 | 20,000,000,000,000,001 and20,000,000,000,000,002 | <10^-2600 |

The exact h100 calculation bounds all four terms by one quarter of
the indicated target, with outward rational logarithms, Machin pi
enclosures and integer-square-root bounds. No exponentially long word
at those dimensions was generated. These specific pairs are not
asserted to be starting thresholds for every larger k.

This is the strongest currently recorded general error bound. It
retains the finite PBBS premises and does not prove exact equality.
The word at17 remains the independently verified24658certificate.

### 9.24 Exact translated periods, the finite census through101, and the native overhead barrier

**[R].** The [full result record](HEIGHT_ADAPTIVE_EXACT_ROTATION_PERIOD_AND_FINITE_CENSUS_20260908.md)
links the independent symbolic audits, new arithmetic implementation,
exact finite census, and complete native recency graph certificate.
These retain the finite support, particle-reduction and rooted-fibre
premises. Internal reviews are not external or formal certification.

For circumferences n_0=n>...>n_h=1 and incoming-row least periods d_s,
put e_s=n_(s+1)/d_s and sigma_j=sum_(s<j)1/(n_s*n_(s+1)). The exact
physical return criterion is

    f^T(A)=rho^K(A)
    iff e_(j-1)*(K/n_0-T*sigma_j) is integral for every1<=j<=h.

The one-level identity T=nm+pK determines the child's translation -m.
The child bits plus invariant row gaps also prove the converse, so this
is an equivalence. In particular,

    v(A)=lcm_(1<=j<=h) den(e_(j-1)*sigma_j).

Every denominator is odd and f/f²periods agree. For the firstLrows,
M_L/gcd(M_L,E_L)|v, where M_L=lcm(n_s*n_(s+1)) and E_L=lcm(e_s).
Nonprimitive rows are included exactly, not discarded as exceptional.

Peak counts form a partition ofr. Exact divisor subtraction counts each
row's least-period classes; their product counts rooted profiles. A
signature witha roots givesn*a physical states andn*a/v cycles. The
new h100 census processed1,295,970partitions and1,702,866signatures in
26.83seconds, checking every signature's integral cycle quotient and
every dimension's Catalan/state total. It reproduces all submitted rows:

| n | W(n) | Native overhead C_n |
|---:|---:|---:|
|17|24,310|892|
|31|300,540,195|1,355,845|
|41|269,128,937,220|327,229,518|
|61|232,714,176,627,630,544|33,239,463,842,328|
|101|199,804,427,433,372,226,016,001,220,056|1,187,277,484,185,535,019,897,550|

Thus N101=199805614710856411551021117606<1.000006W101. Here
B101=W101+7, so N101−B101=1187277484185535019897543. Everycase in
the claimed1%,0.1%,0.01%ranges29–102,57–102,87–102 passed exact
integer comparison, with the literal doubling lift in even dimensions.
These are finite ranges, and these enormous words were not materialized.

For the structural barrier, divide the peak partition intoq constant
blocks with boundary circumferencesx_0=n,...,x_q=1. The exact period
divideslcm(x_(j-1)*x_j), which dividesproductx_j, so v<=n^q. Since
q(q+1)/2<=r, defineQ_n=floor((sqrt(4n−3)−1)/2). Then

    C_n>=ceil((2Q_n−1)*W(n)/n^Q_n)
       >=exp(n*log2−O(sqrt(n)*log(n))).

This lower bound is for the unchanged word's collar cost, notnu−W.
SinceB−W=O(sqrt(n)), that unchanged construction cannot attainB for
large dimensions. A real modification of its word/states is necessary.

At17, the separate native-D^h recency reconstruction checked every
same-height predecessor using the nine-subset containment criterion.
All86,972neutral candidates were tested. The legal graph has24,310native
edges,24,310self-loops,and17extra edges, allcanonical83→103 atheight3,
periods153→85. The component quotient is acyclic. Cross-height edges
cannot occur on a cycle becauseb9=h cannot increase to a different
rank9label. Within each originalcomponent only the native edges and
self-loops remain. Therefore every cyclic permutation either retains
that component or splits it entirely into loops: minimum146components,
unique loop-free routing. Other submitted small-dimension graph checks
and the reported rewrite search were not rerun.

The finite17bound remains24313<=nu17<=24658. The exact all-k goal
remains open. The capped-state investigations above genuinely change
the inventory and are not automatically excluded by this native result.

### 9.25 Uniform finite guarantees from dimension 29 [R]

The [complete uniform-threshold record](HEIGHT_ADAPTIVE_UNIFORM_FINITE_THRESHOLDS_20260908.md)
contains the exact signature recursion, two independent analytic audits
and a new exact numerical certificate. These retain the finite construction,
corridor, particle-reduction and original rooted-fibre premises. They do
not require the older concentration or divisor-probability arguments.

For n=2r+1 define

    J_r=(3r+49)/(3r(r+2)(r+3))+43/(72 Cat_r),
    E_r=2sqrt(2J_r/(2r+1))+86(r+1)sqrt(r)(25/36)^r.

The unchanged construction satisfies (N_r-W_r)/W_r<=E_r for every r>=1.
The Narayana particle law gives E(p^-2)<=J_r by two exact Vandermonde
sums. Reflection gives E(h^2)<=2n. An original-root generating-function
bound counts every nonprimitive top row: b_r<=43(25/9)^r, hence its
probability is at most the second term of E_r. On primitive rows v>=np;
Cauchy–Schwarz bounds their contribution by the first term. No independence
of height and particle count is assumed.

Every positive summand of J_r decreases. For the other term, the squared
successive ratio is at most125/144 for r>=4. Therefore E_r strictly
decreases from r=4. Upward rational square-root certificates prove

    E45<.009272<.01,
    E163<.000992<.001,
    E741<.00009987<.0001,
    E3424<.000009999<.00001.

The already reproduced census, with its hash checked, also passes all
31 inequalities125C_r<W_r for14<=r<=44. The unique maximum is at r=16,
with ratio4479616/583401555<1/125. This finite band covers odd29–89;
the envelope covers every odd dimension from91 onward. The exact doubling
lift supplies all even dimensions. Consequently, for every integer in
the stated range,

| k | Guaranteed upper factor |
|---:|---:|
| k>=29 | nu(k)<1.01W(k) |
| k>=327 | nu(k)<1.001W(k) |
| k>=1483 | nu(k)<1.0001W(k) |
| k>=6849 | nu(k)<1.00001W(k) |

These are sufficient uniform thresholds. The native finite ratios are
not assumed monotone. No large literal word or new partition census was
generated in this audit. The new numeric check ran on h100 in0.084seconds
under30CPU/45wall/512MiB limits. Its full certificate has SHA
acd7d2c2cfc8c067198c3e227c4011de09d32a28df79c41289c0da6fb337ebb4.

The alternative exact period signature is Gamma={(jQ,jU+kn)} with full
periodQn/gcd(n,U). For childp,(Q,U) and rowleastd, set

    K=lcm(p/gcd(p,Q+nU), d/gcd(d,U)), m=(-KU) modp,
    Q'=KQ, U'=((KQ-nm)/p) modn.

The one-level return equivalence proves this is minimal and exact. It
agrees with9.24's denominator formula, including nonprimitive rows.
The principal new guarantee here is the finite-to-infinite envelope;
the strongest eventual rate in9.23 is unchanged.

### 9.26 Exact attainment at dimension 17, and its historical first lift [I]+[W]

The [supplied optimal word](answers/k17_optimal24313.word) has exactly
24,313 nonempty17-bit masks and SHA-256

    7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9.

The [full optimality record](K17_OPTIMAL24313_VERIFIED_20260908.md) links
the actual file, standalone verifiers, every target witness, independent
forward scan and the self-contained analytic lower-bound audit.

The endpoint proof uses W=binom(17,9)=24310 and Lambda=65535 lower-rank
targets. For a length W+t word, ordered distinct nine-set witnesses
have i<=ell_i<=r_i<=i+t. Every valid(t+1)-window contains I_i at its
corresponding start, so lower ranks require intervals of length<=t.
There are only tW+t(t+1)/2 of these; at t<=2 this is at most48623<65535.
Distinct left endpoints first exclude lengths belowW. Hence every
universal word has length>=24313, including the t=0 endpoint case.

The root verifier enumerated every ending-suffix OR and found all131071
targets. A separately built segment tree rechecked all131071 ordinary
nonwrapping intervals. A second implementation used direct forward scans
from every start, stopping only at the full ground set or the word end;
it checked552396intervals and independently found every target. Thus

    nu(17)=B(17)=24313.

This is a finite [I]+[W] result, independent of the PBBS support and
asymptotic premises. It closes the previous345-position gap and extends
the known equality range through17. Internal review qualifications on
the separate asymptotic manuscript remain unchanged.

The literal also verifies the claimed joint opening. Recover Q from
the first85positions and R from zero-based positions86through24310.
They have lengths85and24225. The final word is exactly

    Q || Q_0 || R || R_0 || R_1.

The cyclic target families have sizes664and130748 and together cover
all131071targets. The two separate opened blocks have lengths86and24227,
cover639and130747targets, and together miss exactly five. The six-letter
boundary is

    (19076,19106,8834 | 25249,689,12849).

Its local one-based intervals supply the missing targets:

| Target | Rank | Local interval |
|---:|---:|---|
|27299|8|[2,4]|
|27303|9|[1,4]|
|27315|9|[2,5]|
|27319|10|[1,5]|
|29363|9|[3,6]|

All other witnesses lie inside a block and survive concatenation. All
24,310 four-letter windows are distinct nine-sets. All one-, two-, three-,
four- and five-letter window unions have the reported ranks and complete
corresponding target counts. Higher-rank coverage was checked independently.
The unprovided quotient-search certificate and generator were not replayed;
the final literal and its reconstructed opening suffice for optimality.

The [verified exact lift to18](scratch/K18_VERIFIED_48626_TRIMMED_LIFT_FROM_OPTIMAL_K17_20260908.md)
emits A_1,...,A_m,{z},A_1|z,...,A_(m-1)|z for m=24313. Its length48626
word passed all262143target and independent range-OR witness checks:

    48623=B(18)<=nu(18)<=48626.

That first lift left a gap of three, subsequently closed by Section9.27.
Bounds at19and20 remain94161and188322.
No statement here proves exact equality for every dimension. All mathematical
execution in these checks occurred only onh100 under explicit resource caps.

### 9.27 Exact attainment at dimension18 and initialized-state lifting [I]+[W]

The [supplied optimal18 word](answers/k18_optimal48623.word) has length
48623 and SHA-256

    6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5.

The [complete record](K18_OPTIMAL48623_VERIFIED_20260908.md) links two
independent coverage implementations and all ordinary interval witnesses.
The suffix recurrence finds all262143nonempty targets, and a separately
built segment tree rechecks every saved interval. The first-coordinate
occurrence algorithm independently visits607684OR-change events and
finds the same complete cube. Both actual runs occurred only onh100.

For the internal lower bound, W=binom(18,9)=48620 and Lambda=106761.
The endpoint proof of9.26 gives Lambda<=tW+t(t+1)/2 for a lengthW+t
universal word. At t<=2, this is at most97243<106761. Hence

    nu(18)=B(18)=48623.

This finite result needs neither the PBBS support premises nor the
construction's generation history. Equality is now known through18.
The previously verified48626lift remains historical, and19is the first
unsettled dimension.

The [initialized extension audit](scratch/INITIALIZED_RECENCY_EXTENSION_INTERLEAVING_AND_K18_LOWER_BOUND_AUDIT_20260908.md)
also proves a general exact identity. Let lambda_k(P) be the least
number of nonempty recency updates such that their prefix families,
including that of initialP, cover the nonemptyk-cube. Then
lambda_k(P)>=W(k)-1. If universalA ends atP, its minimum appended suffix
whose every letter contains a newz has length

    Ext_z(A)=1+lambda_k(P).

For the upper direction append{z}, followed by marked initialized
updates. For the lower direction stripz from any all-marked extension
and remove empty updates. At least one empty update is necessary for
the target{z}; the remaining sequence, together withP, covers every
base target. The initial-state interpretation gives actual suffix
witnesses, including those crossing the original boundary.

The supplied mechanism independently passes
[complete structural reconstruction](scratch/K18_OPTIMAL_INITIALIZED_TWO_CYCLE_STRUCTURE_AND_BYTE_REGENERATION_20260908.md).
It uses the pair-preserving adjustment689to8881 at the optimal17seed's
final position, producing terminal profile(6,1^11). From its actual
two cyclesQ85/R24225, a rotated reverseR traversal omits one initial
endpoint and then appends reverseQ. All24310initialized states cover
the base cube; rank8andrank9are each bijections, and allsevenjoinholes
have literal witnesses. Thuslambda17(P)=24309=W17-1 exactly.
The word regenerates byteforbyte from the supplied17literal and the
given permutation. All131071marked witnesses pass separate rangeOR;
the full18word has a distinctnine-set at every endpoint except0,1,2.
This does not claim regeneration from the unprovided quotient generator.

The general interleaving inequality also passes independent proof:
ifm_z counts markedletters andR_z marked-to-unmarked transitions, then
D_(z,s)<=m_z+(s-1)R_z. Deleting markedletters gives a universal base
word, so m_z<=N-nu(k). At exact19 this forces at least541exits and,
by reversing the word,541entrances per coordinate. This number already
followed fromB(18) in the earlier entrance/exit note; exact18reconfirms
it rather than first proving it. Section9.30 subsequently strengthens
the general requirement to4859 in both directions. A single-switch19lift costs at least
97243>B(19)=92381. The all-k equality objective remains open.

### 9.28 Forward pruning-prefix upper certificates [R method; finite band pending]

The [new method record](HEIGHT_ADAPTIVE_FORWARD_PREFIX_CERTIFICATE_METHOD_20260908.md)
and [independent proof audit](scratch/PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md)
establish a valid finite upper bound at every complete prefix-tree
stopping point, retaining the stated PBBS construction and fibre inputs.

With beta_0=0 and beta_(s+1)=(1+n_(s+1)*beta_s)/n_s, the exact period is
lcm_s den(beta_(s+1)/d_s). The originaln together with the processed
denominators gives a divisorP of every completion's period. A prefix
ending in sizesa,b has exact massM=w*binom(a,b)*binom(a,b+1)/a and
height capH=s+b+1. Splitting every legal nextsize and ordered-row period
class preserves exact mass. Therefore

    U=sum_leaves ceil(M*(2H-1)/P), N_r<=W_r+(2r+1)*U.

No unfinished leaf may be omitted. The unrounded total decreases under
refinement; the rounded total need not. The final one-slot denominator
must be included before a terminal period is called exact.

The user reports713integer certificates, namely1000U<Cat_r forr28–42
and10000U<Cat_r forr43–740. With9.25's verified envelope fromr741,
those certificates would prove uniform0.1%from57 and0.01%from87.
The full band's actualUvalues and transcripts were not supplied with the
text and have not been independently checked. A new independent bounded
implementation passes fullcensusr1–8comparisons and a singlecase at r163:
U/Cat163<0.000099417180896906105456651839. All395splits and13947final
leaves are replayed without the priority rule, retaining every unfinished
branch. This certifies0.01%at327and328only, not the whole713-case band.
The currently verified uniform
thresholds remain29/327/1483/6849 until that finite band is certified.
The smaller finite ranges57–102 and87–102 remain separately verified
by9.24. This distinction does not affect the exact18literal certificate.

### 9.29 Height-moment prefix charges [R method and first pair; uniform band pending]

The [height-moment method record](HEIGHT_ADAPTIVE_MOMENT_PREFIX_CERTIFICATE_METHOD_20260909.md)
reviews the user's latest proof and distinguishes its valid mathematical
interfaces from its unprovided finite computation. For the exact core count
K(a,b)=binom(a,b)binom(a,b+1)/a, the total remaining height satisfies

    H(a,0)=1,
    H(a,b)=K(a,b)+sum_c binom(a+c,2b)H(b,c).

The sum has max(0,2b-a)<=c<b. A prefix at depth s, with multiplicity w
and common period divisor P, can therefore be charged by

    w[(2s-1)K(a,b)+2H(a,b)]/P.

This sums correlated heights exactly after using the common period bound;
it does not factor an expectation. Integrating the next row gives the
additional nonnegative proper-period correction

    sum_d A_d/P_d = (sum_d A_d)/P_p
                       +sum_(d<p) A_d(1/P_d-1/P_p),

where P|P_d|P_p. Symmetric rows remain included. The reflection substitute
for large-core heights, sparse exact-mass reserves, terminal final-row
denominator, and upward integer normalization all pass separate proof
reviews. A predecessor lower certificate must use exact or downward
arithmetic, not these upper ceilings.

One independent h100 implementation and complete priority-free replay
now certify r=68, hence137and138:

    Cat_68=86218923998960285726185640663701108500,
    U=860872256709126171307785011672491,
    Cat_68-100000U=131698328047668595407139496452008500>0.

Thus nu137<=11812110527356728294772901937473650995767 and the relative
excess is below0.000009984725125072396316850761. All162refinements and
2409finalleaves, including2388unfinishedleaves, were replayed. This run
uses exact heights and exact symmetry classes throughout, no sparse
reserves. Its5050height cells,23713directDyck roots,125475middlebridges,
2575orderedrows and288smallprefixstates also pass the stated structural
checks. [Complete numerical evidence](scratch/MOMENT_PREFIX_R68_INDEPENDENT_NUMERICAL_CERTIFICATE_20260909.md)
and [report](scratch/moment_prefix_structural_and_r68_20260909/moment_prefix_complete_certificate.json)
are retained.

The user reports100000U_r<Cat_r for all3356integers68<=r<=3423,
plus a lower certificate excluding the nativeconstructor tolerance at
135/136. Those transcripts and programs were not attached to the proof
and log. They have not been independently verified here. If the entire
band passes, the previously proved decreasing envelope fromr3424 and
the even lift establish the claimed uniform threshold137. Until then,
the independently verified uniform ten-parts-per-million threshold
remains6849, alongside this new isolatedpair137/138. This does not
change the exact17/18 results or prove exact equality in any new dimension.

### 9.30 Exact frontier: fixed matching and paired-endpoint runs [R]/[O]

The [consolidated exact-frontier record](EXACT_EQUALITY_FIXED_MATCHING_AND_RUN_CONSTRAINTS_20260909.md)
separates the following completed results from the still-open all-rank
constructor. At the time of this earlier record, equality was known
through18. Section9.31 below subsequently closes both19/20 gaps.

From the optimal17 literal's actual85/24225cyclic pieces, a full
comparison recovers all1430rotation-quotient rows and proves that its
rank8-to-rank9 outgoing matching is exactly the canonicalPBBSmatching
on all24310labels. The incoming matching changes17578incidences.
Its alternating differences include a single16167-cycle; this must
not be described as a known safe small-flip factorization. The optimal
carrier passes the two-step residence test with zero violations,
whereas the native carrier has119. No all-dimensional matching with
all required residence, all-rank and opening properties is constructed.

A new pure finite counting theorem applies to ANY partially covering
word. Let a_s count represented rank-s targets avoidingz and b_s count
represented rank-(s+1) targets containingz. If R_out,R_in count exits
and entrances ofz, then

    a_s+b_s <= N+R_out,    a_s+b_s <= N+R_in.

Choose distinct witness endpoints in each family. Shared endpoints
pair D with D union{z}, and the whole unmarked-run prefix at such an
endpoint equalsD. Its fixed rank allows only one distinct suchD per
noninitial run. Thus shared endpoints inject into exit runs; reversal
gives entrances. This strengthens the earlier marked-target-only bound
without a PBBS premise. AtN=B(2r+1)=W(2r+1)+d it gives

    R_out,R_in >= max(0,Cat_r-d),

namely1427at17 and4859at19. The deficits and endpoint-overlap argument
have earlier occurrences; the run injection is the strengthening here.
One reviewed h100 diagnostic passes all137256nonemptythree-coordinate
words through length six in both orientations, with1647072family checks
and454260literalshared-witness replays. Hash-pinned17/18run statistics
also satisfy the inequalities; full-cube coverage was not rerun.

Combining with the old-target endpoint loss at run starts gives
H_s>=max(0,3binom(k,s)-N-M), whereM is the unmarked length. At exact19
andM48623, at least4856unmarked runs must begin with a literalnine-set,
and the same holds for ends. A trace with no such literal requires
M>=53479. The actual optimal18 trace has maximum letterrank7.

Its complete shortest-nine-set-witness check further proves that all
48622internal gaps are fatal to old coverage if a marked letter is
inserted. Any superword retaining that exact unmarked subsequence leaves
it contiguous. It then has at most one entrance/exit, and the new
paired bound forcesN>=97239. This excludes that fixed-trace architecture,
not unrestrictednu19. The occupied-cut idea has earlier fixed16instances.

An exact multi-run recency cursor and protected-witness tagging compiler
are proved in the linked record. A separate proper-pair reservation
lemma has an integral flow formulation for a prescribed independent
frame and retained middle palette. Neither closes the coupled residual
lower-target allocation or supplies an optimum-length source. In
particular locally proper pair targets must not be credited twice if
they also remain literal elsewhere. No pair-flow or new word search ran.

### 9.31 Exact19/20 words, cyclic19 optimum, and periodic lift [I]+[W]/[R]

The user supplied complete words of lengths92381 and184759. Two new
independent implementations, run only onh100, establish their complete
ordinary interval coverage. A forward first-occurrence enumeration finds
all524287/1048575 targets; a separate suffix recurrence finds the same
families and saves a witness for every target. Every saved interval is
then recomputed with a separate range-OR segment tree. There are no empty
letters, missing targets, or wrapping witnesses. These finite checks
need no PBBS or asymptotic premise.

At rank10 the endpoint theorem has W=92378/184756, smaller-target
counts262143/431909, and t=2 capacities184759/369515. Thus t>=3.
The supplied words attain the resulting bounds:

\[
\boxed{\nu(19)=B(19)=92381,\qquad\nu(20)=B(20)=184759.}
\]

Let C be the first92378 letters of the19 word A. The checker verifies
A=C followed by its firstthree letters. Every checked ordinary witness
has length at most29, so reducing its start modulo92378 gives an
admissible cyclic witness in C. Consequently C is universal. A cyclic
endpoint supplies at most one ten-set, proving

\[
\boxed{\mu(19)=92378.}
\]

The periodic-core lift has a direct recency proof. If C has period M,
0<=d<M, and A=C+C[:d] is ordinary universal, A ends at the periodic state after
phase d-1. That state and the next M-1 updates supply every cyclic
suffix family. Append {z} and those M-1 letters with z added; every
marked target is supplied by an ordinary suffix, and old targets remain
inside A. Length is2M+d. For M=W the initialized traversal is optimal
from every periodic phase. This is also the retained border-sensitive
splice at border lengthd; existence of the required cores and safe cuts
in every odd dimension remains unproved.

At M92378,d3,z524288 this lift regenerates the supplied20 file byte
for byte. Its full coverage is additionally checked from the raw file.
Both ordinary words have onlythree rank10-free initial endpoints; every
later endpoint supplies a fresh ten-set. The cycle's triple/four windows
enumerate all nine-/ten-sets once, respectively.

A separate complete literal reconstruction finds that the19 carrier,
like the optimal17 carrier, retains every canonical outgoing PBBS
matching edge. It changes70452 incoming incidences and joins the native
360components into one physical cycle. Actual caps preserve all triples
while changing12654pairs. Literal/pair unions give exactly all169765
targets of ranks1 through8;11324targets of ranks at most7 are pair-only.
The full4862rotation-quotient rows and phases are recovered. This is
structural reconstruction from the supplied word, not a replay of the
unprovided compact generator or search.

The general short-window cap criterion is exact: intersect each envelope
with every target assigned through that position; these maximal caps
must be nonempty and retain the required unions. Necessity follows from
containment, and sufficiency by taking the maximal caps themselves.
Their simultaneous allocation in every dimension remains open.

The user also gives the valid set-turnover consequence
tR_Q>=nu(k-|Q|)-binom(k-|Q|,s)-t, where t=N-binom(k,s).
Every rank-s witness has length at mostt+1 by the endpoint theorem;
only the firstt endpoints after each Q-exit can witness a target meetingQ.
For singletonQ, Section9.30's paired-endpoint law is stronger: an exact21
word requires16793 exits and16793 entrances per coordinate, compared
with5599 from this turnover consequence. Neither excludes exact21.

The current finite frontier is therefore B(21)=352719 and B(22)=705435,
with no attaining words claimed here. The all-dimensional goal remains
active. [Full proof, hashes, checks and artifacts](K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md)
and [complete numerical report](witnesses/k19_k20_optimal/complete_suffix_range_cyclic_lift_certificate.json)
record the exact scope. Internal reviews are not external or formal
certification, and the user's constructions are not claimed as new
discoveries of this verification turn.

### 9.32 Stronger bounded-height native-constructor barrier [R]

The unchanged native word is still distinct from the optimum. The exact
return criterion gives F_s dividing n_s F_(s+1), hence v<=n^h. Height-two
roots with profile(r,b,0) number binom(r,2b) and have period at most
n(2b+1). Their three-letter collars and the height-one cycle yield

\[
N_r-W_r\ge1+3\left\lceil\frac{2^r}{r+1}-1\right\rceil\quad(r\ge1).
\]

For height at mostH, the path-graph eigenvectors give at least
4 sin^2(pi/(H+2))/(H+2) times [4cos^2(pi/(H+2))]^r roots.
Combining with v<=n^H and choosing
H near(2pi^2r/log n)^(1/3) proves

\[
\frac{N_r-W_r}{W_r}\ge
\exp\!\left[-\left(\frac32\pi^{2/3}+o(1)\right)
(n(\log n)^2)^{1/3}\right].
\]

Thus N_r-B(n)=2^(n-o(n)) for this native constructor. Section9.24
already established the same leading exponential conclusion; this
refines its subexponential penalty and supplies the explicit height-two
bound. It is not a lower bound on unrestrictednu(n), and does not
contradict any of the optimal17–20 words. [Independent pure-proof audit](scratch/PBBS_BOUNDED_HEIGHT_SPECTRAL_CONSTRUCTOR_BARRIER_INDEPENDENT_AUDIT_20260909.md)
checks the exact scope and constants; no new enumeration was run.

## Appendix A.1: Central-binomial estimate

The central-binomial estimate used throughout is proved here. Put

\[
I_n=\int_0^{\pi/2}\sin^n x\,dx.
\]

Integration by parts gives `I_n=(n-1)I_{n-2}/n`, whence

\[
I_{2m}={\pi\over2}{\binom{2m}m\over4^m},\qquad
I_{2m+1}={4^m\over(2m+1)\binom{2m}m}.
\]

Since `I_{2m}>=I_{2m+1}>=I_{2m+2}` and
`I_{2m}/I_{2m+2}=(2m+2)/(2m+1)`, the ratio
`I_{2m}/I_{2m+1}` lies between `1` and `1+1/(2m+1)`. Substituting the two
product formulas therefore gives

\[
\binom{2m}m={4^m\over\sqrt{\pi m}}(1+O(1/m)).       \tag{A.1}
\]

The same formula and the adjacent-binomial ratio imply, uniformly as
`t->infinity`,

\[
W(t)=\binom t{\lfloor t/2\rfloor}
     =2^t\sqrt{2\over\pi t}\,(1+O(1/t)).             \tag{A.2}
\]

## Appendix A.2: Symmetric chains and bridge words

The Boolean lattice on a `t`-set partitions into saturated chains whose
bottom and top ranks sum to `t`. This follows by induction: from a chain
`C_0 subset ... subset C_s`, after adjoining a new element `x`, use the long
chain

\[
C_0\subset\cdots\subset C_s\subset C_s\cup\{x\}
\]

and, when nonempty, the short chain

\[
C_0\cup\{x\}\subset\cdots\subset C_{s-1}\cup\{x\}.
\]

These chains are disjoint, cover both copies of the old lattice, and remain
symmetric. Every symmetric chain meets rank `floor(t/2)` exactly once, so
every such decomposition has `W(t)` chains.

For a saturated chain `C=(C_0 subset ... subset C_s)` in universe `U`, define
its bridge word

\[
\beta_U(C)=(C_0,C_1\setminus C_0,\ldots,
            C_s\setminus C_{s-1},U\setminus C_s),
\]

omitting empty blocks. Its blocks are nonempty and disjoint. Prefix unions,
including the empty prefix, contain every `C_i`; suffix unions, including the
empty suffix, contain every `U\setminus C_i`.

## Appendix A.3: The construction

Split `[k]=P dotcup Q`, where `|P|=p`, `|Q|=q`, `p,q>=1`, and distinguish
`z in P`. Take a symmetric-chain decomposition of `2^{P\setminus\{z\}}`.
Replace each chain by its long lifted chain ending with the old top together
with `z`; call the resulting family `mathcal C`. It has
`a=W(p-1)` chains, and every subset of `P\setminus\{z\}` occurs in exactly
one member. Take a symmetric-chain decomposition `mathcal D` of `2^Q`, of
size `b=W(q)`.

Form the directed complete bipartite graph on
`mathcal C dotcup mathcal D`, with both directed arcs between every left and
right vertex. It is strongly connected and every indegree equals the
corresponding outdegree, so the following elementary Euler argument applies:
follow unused outgoing arcs until stuck. A nonstarting endpoint would have
used one more incoming than outgoing arc, impossible because its total
indegree equals its total outdegree, so the trail closes at its start. If an
arc remains, strong connectivity supplies a visited vertex with an unused
outgoing arc; form another closed trail there and splice it into the first.
Iteration terminates in a circuit using every arc once.

Start the Euler circuit at a right vertex, concatenate the bridges of the
tails of its `2ab` directed arcs in traversal order, and then append one more
copy of the starting right bridge. Let a nonempty target be `S=X\cup Y`, with `X subseteq P` and
`Y subseteq Q`. If `z in X`, then `P\setminus X` lies on a unique lifted
chain `C`, while `Y` lies on a unique `D`; across the occurrence of the arc
`C->D`, take the suffix of `beta_P(C)` with union `X` and the following prefix
of `beta_Q(D)` with union `Y`. If `z notin X`, use the unique chains containing
`Q\setminus Y` and `X` across the reverse arc `D->C`. One part may be empty,
but not both, so this is a nonempty interval with union exactly `S`.

In an SCD of `2^t`, the sum of bridge lengths is `2^t+W(t)-2`: the unique
chain containing the empty set contributes one less than its membership,
and every other chain one more. The lifted left chains have total membership
`2^{p-1}+a`, hence total bridge length `2^{p-1}+2a-2`; the right total is
`2^q+b-2`. In the first `2ab` visits of the circuit each left vertex occurs
as a tail `b` times and each right vertex `a` times. Cutting at a right vertex
adds at most `q+2` symbols. Thus

\[
L\le b(2^{p-1}+2a-2)+a(2^q+b-2)+q+2.              \tag{A.3}
\]

Choose `p=ceil(k/2)` and `q=floor(k/2)`. Formula (A.2) gives

\[
b2^{p-1}+a2^q=(\sqrt2+o(1))W(k),
\]

whereas `ab=O(2^k/k)=o(W(k))` and `q=o(W(k))`. Therefore

\[
                     \nu(k)\le(\sqrt2+o(1))W(k),
\]

with no external construction theorem.


## Appendix A.4: A short far-rank repair [I]

For sufficiently large \(b\) and \(\sqrt b\le H\le b-2\), all nonempty
\(S\subseteq[2b]\) with \(||S|-b|\ge H\) have a common nonzero covering
word of length
\[
\boxed{O\!\left(\left(1+{H\over\sqrt b}\right)
 e^{-H^2/(16b)}W(2b)\right)+O(b).}                    \tag{A.4}
\]
Use A.3 with \(|P|=|Q|=b\), but retain both directed arcs between a long
lifted left chain of bottom rank \(i\) and a right chain of bottom rank
\(j\) only when \(i+j\le b-H\). A target assigned to this pair has rank
between \(i+j\) and \(2b-i-j\); hence every stated far target is retained.
Every nonisolated chain meets the unique opposite bottom-rank-zero chain,
so the nonisolated directed graph is strongly connected. Both orientations
make every indegree equal its outdegree, and the Euler concatenation in A.3
therefore applies.

Put \(R=\lfloor(b-H)/2\rfloor\), \(A_0=W(b-1)\), \(B_0=W(b)\), and
\[
\Lambda_L=2^{b-1}+2A_0-2,\qquad\Lambda_R=2^b+B_0-2.
\]
Every retained pair has \(i\le R\) or \(j\le R\). In an SCD on a \(t\)-set,
the number of chains with bottom \(i\) is
\(c_t(i)=\binom ti-\binom t{i-1}\): subtract the rank-\(i-1\) chains,
each of which continues through rank \(i\), from all rank-\(i\) sets. Its
bridge has at most \(b-2i+2\) letters. Thus, with
\[
S_t(R)=\sum_{i=0}^Rc_t(i)(b-2i+2),
\]
the Euler word length is at most
\[
B_0S_{b-1}(R)+A_0S_b(R)+\binom bR\Lambda_L+
 \binom{b-1}R\Lambda_R+b.                              \tag{A.5}
\]
The last two cross terms account for the opposite bridge at every pair
selected through only one low-bottom endpoint.

Summation by parts and a geometric comparison below the middle rank give
\[
\begin{aligned}
S_t(R)&=(b-2R+2)\binom tR+2\sum_{i<R}\binom ti\\
&\le\left(H+3+{b\over H}\right)\binom tR,
\qquad t\in\{b-1,b\}.                                  \tag{A.6}
\end{aligned}
\]
Indeed successive backward ratios are at most
\(R/(t-R+1)\), so
\(\sum_{i<R}\binom ti\le R\binom tR/(t-2R+1)\le
b\binom tR/(2H)\).

Let \(m=\lfloor t/2\rfloor\), \(d=m-R\). For large \(b\), \(d\ge H/4\),
and \(\log(1-y)\le-y\) applied to
\[
{\binom tR\over W(t)}
=\prod_{a=1}^d{m-a+1\over t-m+a}
\]
gives
\[
{\binom tR\over W(t)}\le e^{-d^2/t}
\le e^{-H^2/(16b)}.                                    \tag{A.7}
\]
Equations (A.2), (A.5)--(A.7), and \(H\ge\sqrt b\) bound (A.5) by
\[
O\!\left((H+\sqrt b)A_0B_0e^{-H^2/(16b)}\right)+O(b).
\]
Finally
\[
{W(b-1)W(b)\over W(2b)}
={1+O(1/b)\over\sqrt{\pi b}},                          \tag{A.8}
\]
which proves (A.4). In particular the repair is \(o(W(2b))\) whenever
\(H/\sqrt b\to\infty\). \(\square\)

## Appendix A.5: Four-block cross-split full-cube bound [I]

Let \(A\le B\le C\le D\) be the order statistics of four independent
Rayleigh variables, each with density \(xe^{-x^2/2}\), \(x>0\). Then
\[
 \boxed{\nu(k)\le(c_4+o(1))W(k),\qquad
 c_4=\left({2\over\pi}\right)^{3/2}
 \mathbb E\left[AB(C+D)-{D\over4}(A+B-C)_+^2\right]<1.27.} \tag{A.9}
\]
The word construction is deterministic. Only the constant evaluation is
computer-assisted; its complete rational verifier and error proof are below.

### Paired-family compiler and product chains

On nonempty disjoint supports \(U,V\), let \(D\subseteq2^V\) be a
saturated chain of length \(d\), and partition \(\mathcal F\subseteq2^U\)
into saturated chains \(E_1,\ldots,E_r\), with \(v=\sum_j|E_j|\).
Write \(D^c\)
for its complements in ascending order. Using A.2's bridges, output
\[
 \beta_V(D^c),\beta_U(E_1),\beta_V(D^c),\ldots,
 \beta_U(E_r),\beta_V(D^c).                              \tag{A.10}
\]
For \(X\in E_j,Y\in D\), the first boundary supplies suffix \(Y\) and
prefix \(X\), while the second supplies suffix \(U\setminus X\) and
prefix \(V\setminus Y\). Thus both \(X\cup Y\) and its full complement
are realized whenever nonempty. Empty parts may be omitted, and every
asserted witness stays in this block. The actual length is at most
\(v+r+(r+1)(d+1)=v+(d+2)r+d+1\), including the last fixed bridge.

For chains of lengths \(a\le b\), the grid chains
\[
 (0,i),(1,i),\ldots,(a-1-i,i),(a-1-i,i+1),\ldots,(a-1-i,b-1),
 \qquad0\le i<a,
\]
partition their product, are saturated, and have endpoint-rank sum
\(a+b-2\). Recursing gives an SCD of any product; union on disjoint
supports preserves covers and distinctness. For three lengths \(a\le b\le c\),
its number of chains is
\[
 w_3(a,b,c)=ab-\left\lfloor{(a+b-c)_+^2\over4}\right\rfloor. \tag{A.11}
\]
Indeed the middle coefficient counts \((i,j)\in[0,a-1]\times[0,b-1]\)
with \(s-c+1\le i+j\le s\), \(s=\lfloor(a+b+c-3)/2\rfloor\).
If \(a+b-c\le1\), none are excluded. For \(a+b-c=2q\), the two
excluded corners have sizes \(q(q-1)/2,q(q+1)/2\); for \(2q+1\), both
have size \(q(q+1)/2\). They fit since \(c\ge b\), proving (A.11).

### Full-cube word and its coefficient

Split \([4h]\), \(h\ge2\), into four \(h\)-sets \(U_i\), choose pivots
\(z_i\), and take SCDs of \(2^{U_i\setminus\{z_i\}}\), each containing
\(L_h=W(h-1)\) chains. For each chain tuple \((C_1,\ldots,C_4)\) and
each of the eight signs \(\varepsilon\in\{0,1\}^4\), \(\varepsilon_1=0\),
put \(F_i=C_i\) if \(\varepsilon_i=0\), and \(F_i=C_i^c\) otherwise,
with blockwise complements ordered increasingly. Pair the product family
\(\{X_1\cup\cdots\cup X_4:X_i\in F_i\}\) with its full complement.
These pairs partition the cube: first complement a target if necessary to
omit \(z_1\); its other pivot bits fix the signs and its SCD owners fix
the tuple. The empty target is counted but requires no witness.

Sort the lengths as \(a\le b\le c\le d\), isolate a longest block
(smallest block index in a tie), and product-SCD the other three signed
chains on the merged support. Its membership is \(abc\) and chain count
is \(w_3\). Applying (A.10) and concatenating all signed tuples proves
the exact finite upper bound
\[
 \boxed{\nu(4h)\le8\sum_{(C_1,\ldots,C_4)}
       \{abc+(d+2)w_3(a,b,c)+d+1\}.}                     \tag{A.12}
\]
The support split changes with the tuple. The moving bridges have genuine
mixed-support letters; no fixed two-half full-block restriction is imposed.
Each such letter costs one position under Section 1, not its cardinality.

The SCD length law (3.17) follows by telescoping the bottom-rank counts.
Adjacent-binomial products also give
\(\Pr(L_n\ge u)\le e^{-(u-2)_+^2/(4n)}\). Thus independent uniform chain
lengths divided by \(\sqrt h\) converge to the Rayleigh variables above,
with all fixed polynomial moments. For
\(f=ab(c+d)-d(a+b-c)_+^2/4\), the summand in (A.12) satisfies
\[
 0\le abc+(d+2)w_3+d+1-f\le2ab+2d+1.
\]
Its expected error is \(O(h)\), versus the cubic main scale \(h^{3/2}\).
By A.1,
\[
 L_h\sim{2^h\over\sqrt{2\pi h}},\qquad
 {8L_h^4h^{3/2}\over W(4h)}\longrightarrow(2/\pi)^{3/2}.
\]
This proves the coefficient in (A.9). Bridge and floor errors contribute
\(O(W(4h)/\sqrt h)\); expectation convergence contributes \(o(W(4h))\),
with no explicit rate asserted. At most three top-bit splices extend from
\(4h\) to every \(k\), since \(2^{k-4h}W(4h)/W(k)=1+O(h^{-1})\).
This proves an asymptotic bound, not \(\nu(k)\le1.27W(k)\) at every \(k\).

### Exact integral and rational certificate

On \([0,1]^2\), define
\[
 q=1+v^2(1+x^2),\quad p=xv^2,\quad s=\tfrac14[v(x+1)-1]_+^2,
 \quad G(q)={105\over(q+1)^{9/2}},
\]
\[
 J(q)={48-(105q^3+210q^2+168q+48)/(q+1)^{7/2}\over q^4},
 \quad \Psi(x,v)=xv^3\{(2p-s)G(q)+(p-s)J(q)\}.
\]
Then
\[
                         c_4={48\over\pi}\int_0^1\int_0^1\Psi(x,v)\,dx\,dv.
                                                               \tag{A.13}
\]
To verify the reduction, the ordered density is
\(24abcd\exp(-(a^2+b^2+c^2+d^2)/2)\). Integrate \(d\) using
\(\int_r^\infty te^{-t^2/2}dt=e^{-r^2/2}\) and
\(\int_r^\infty t^2e^{-t^2/2}dt=re^{-r^2/2}
+\sqrt{\pi/2}\operatorname{erfc}(r/\sqrt2)\). Substitute
\((a,b,c)=(ru,rv,r)\), then \(u=xv\). The radial integrals are
\(\int_0^\infty r^8e^{-(q+1)r^2/2}dr=\sqrt{\pi/2}G(q)\) and
\(\int_0^\infty r^7e^{-qr^2/2}\operatorname{erfc}(r/\sqrt2)dr=J(q)\).
The second follows by parts from the antiderivative
\(-e^{-qr^2/2}(r^6/q+6r^4/q^2+24r^2/q^3+48/q^4)\).
The Jacobians give the displayed \(xv^3\), establishing (A.13).

Here \(1\le q\le3\) and \(0\le s\le p/4\). The inequality
\(\operatorname{erfc}(z)\le e^{-z^2}\), \(z\ge0\), follows by
differentiating their difference, which increases to \(z=1/\sqrt\pi\)
and then decreases to zero. Differentiating the integral for \(J\) gives
\(0\le J\le3, |J'|\le6, |J''|\le15\); directly,
\(0<G<5, |G'|<11, |G''|<29\). Put
\(A=xv^3(2p-s),B=xv^3(p-s)\). Product rules give these uniform bounds:

| quantity | absolute value | \(x\) derivative | \(v\) derivative | \(xx\) derivative | \(vv\) derivative |
|---|---:|---:|---:|---:|---:|
| \(A\) | 2 | \(9/2\) | 11 | \(11/2\) | 48 |
| \(B\) | 1 | \(5/2\) | 6 | \(7/2\) | 28 |
| \(q\) | 3 | 2 | 4 | 2 | 4 |

For example \(s\le1/4,|s_x|\le1/2,|s_v|\le1,
|s_{xx}|\le1/2,|s_{vv}|\le2\). Substitution in
\(\Psi=AG(q)+BJ(q)\) yields \(|\Psi_{xx}|\le644\) and
\(|\Psi_{vv}|\le2860\) almost everywhere. The function is \(C^1\)
across \(v(x+1)=1\), with absolutely continuous first derivatives on
coordinate lines. Taylor's integral remainder on an interval of width
\(1/N\) bounds midpoint error by \(\|f''\|_\infty/(24N^3)\).
Applying it successively in both variables proves
\[
 \left|\int\Psi-{1\over N^2}\sum_{i,j=0}^{N-1}
 \Psi\left({2i+1\over2N},{2j+1\over2N}\right)\right|
 \le{146\over N^2}.                                      \tag{A.14}
\]

The following complete verifier uses only rational and integer arithmetic.
For rational \(z>0\), \(j=\operatorname{isqrt}(\lfloor zS^2\rfloor)\)
gives \(j/S\le\sqrt z<(j+1)/S\). At fixed rational \(q\), \(G\)
decreases and the formula for \(J\) increases with the bounded square
root; \(2p-s,p-s\ge0\) preserve the upper bounds. Each value is rounded
up to denominator \(10^{16}\). Alternating-series bounds and
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), verified by the tangent
addition formula and angle range, give a rational lower bound for \(\pi\).

```python
from fractions import Fraction as F
from math import isqrt

def atan_bounds(x):
    a = sum(((-1)**j * x**(2*j+1) / (2*j+1)
             for j in range(40)), F(0))
    return a, a + x**81 / 81

al, au = atan_bounds(F(1, 5))
bl, bu = atan_bounds(F(1, 239))
pi_lower = 16*al - 4*bu
assert pi_lower > 3
N, S, Q = 1024, 10**20, 10**16
upper_sum = 0
for i in range(N):
    x = F(2*i+1, 2*N)
    for j in range(N):
        v = F(2*j+1, 2*N)
        q = 1 + v*v*(1+x*x)
        z = q + 1
        root = isqrt(z.numerator*S*S // z.denominator)
        lo, hi = F(root, S), F(root+1, S)
        G = 105 / (z**4 * lo)
        J = (48 - (105*q**3 + 210*q*q + 168*q + 48)
             / (z**3 * hi)) / q**4
        p = x*v*v
        s = max(F(0), v*(x+1)-1)**2 / 4
        value = x*v**3*((2*p-s)*G + (p-s)*J)
        assert 0 <= s <= p/4 and value >= 0
        upper_sum += -((-value.numerator*Q) // value.denominator)
c4_upper = 48*(F(upper_sum, Q*N*N) + F(146, N*N)) / pi_lower
assert c4_upper < F(126947180564, 10**11) < F(127, 100)
```

Thus \(c_4<1.26947180564<1.27\), with integration and arithmetic error
both charged. The finer decimal \(c_4\approx1.2673446\) is diagnostic
only and is not used in the theorem.

### Grouped cylinders and the three-block precursor

For two chains of lengths \(a,c\) on disjoint supports, pair their
product with its full complement and adjoin a fresh \(t\)-set. Put
\(m=\min(a,c),M=\max(a,c)\). The entire pair times the new cube has a
nonzero covering word of length at most
\[
 \boxed{2^tm+(M+2)w_m(t)+M+1,\qquad
 w_m(t)=\sum_{j=0}^{m-1}\binom t{\lfloor(t+m-1)/2\rfloor-j}.} \tag{A.15}
\]
Product-SCD the shorter chain with the new cube: its membership is
\(m2^t\), and its central coefficient, hence chain count, is \(w_m(t)\).
Apply (A.10). Complementing the new subset is a bijection of its full
cube, so both cylinders are covered. This groups whole rectangles rather
than separately paying for every fiber as in 3.9.

Alternatively use three equal pivoted blocks and four signs. For sorted
lengths \(a\le b\le c\), merge the two shorter chains and apply
(A.10); its principal cost is \(ab+ca=a(b+c)\). The same normalization
gives \(\nu(k)\le(c_3+o(1))W(k)\), where
\[
 c_3={\sqrt3\over\pi}\mathbb E[A(B+C)]
 ={\sqrt3\over\pi}\left({1\over3}
             +{3\over\sqrt2}\arctan\sqrt2\right)
 \approx1.3010623.                                       \tag{A.16}
\]
Here \(A\le B\le C\) are three ordered Rayleigh variables. Their
expectation is
\(6\int_0^\infty x^2e^{-x^2}
[xe^{-x^2/2}+\sqrt{\pi/2}\operatorname{erfc}(x/\sqrt2)]dx\).
The first contribution is \(4/3\); for the second differentiate
\(\int_0^\infty e^{-qx^2}\operatorname{erfc}(\alpha x)dx
=\arctan(\sqrt q/\alpha)/\sqrt{\pi q}\) in \(q\).
That identity follows by differentiating in \(\alpha\) and taking its
zero limit at infinity. This proves (A.16). The four-block improvement
uses the full three-chain product and its triangular saving (A.11).

## Appendix A.5B: A length-dependent switch below \(c_4\) [I]

The following strict improvement uses no new numerical quadrature:
\[
 \boxed{\nu(k)\le(c_4-\Delta_8+o(1))W(k),\qquad
 \Delta_8={181781e^{-4}\over28800000\pi^2}>{11\over10^6}.} \tag{A.16a}
\]
Together with A.5's rational certificate this gives
\(c_4-\Delta_8<1.26946080564\), not coefficient one.

### Finite construction and its literal cost

Split \(8h\) coordinates into five blocks of sizes \(2h,2h,2h,h,h\),
each with one pivot, and take SCDs on their nonpivot coordinates. For each
chain tuple, use the sixteen signed complementary product pairs of A.5.
They partition the cube by exactly the same pivot-and-owner argument.
Write the five lengths as \(a,b,c,d,e\), without sorting, and put
\(s=\sqrt h\). Fix the hook product SCD from A.5 at every merge.

The baseline first merges the last two factors. Its child lengths are
\(r=|d-e|+1,|d-e|+3,\ldots,d+e-1\), with \(\sum_r r=de\).
For each resulting four-factor tuple, isolate a longest factor and
product-SCD the other three, leaving paired terminal rectangles. For
sorted lengths \(v_1\le v_2\le v_3\le v_4\), the sum of terminal side
lengths for this four-factor step is exactly
\[
 P_4(\mathbf v)=v_1v_2v_3+v_4w_3(v_1,v_2,v_3),
\]
by (A.11). Thus the baseline charge of one five-factor tuple is
\(P_0=\sum_rP_4(a,b,c,r)\).

Change this rule only when
\[
                 a,b,c\le s,\qquad d,e\ge2s.           \tag{A.16b}
\]
There, isolate the fifth factor and product-SCD the other four. If
\(w_4\) is their central coefficient, its charge is
\(P_1=abcd+ew_4\le abc(d+e)\): for every choice in the first three
chains, at most one element of the fourth has the required rank, so
\(w_4\le abc\). Outside (A.16b), leave the baseline unchanged.

Here is why these charges give actual words, not just rank inventories.
For every terminal pair \((C,D)\) on complementary supports \(U,V\),
put both directed arcs between bridge vertices \((U,C)\) and \((V,D^c)\).
The two arc directions realize the rectangle and its complement by the
suffix-prefix proof of (A.10). In every component follow the Euler
circuit of A.3, outputting its bridge occurrences and one closing bridge.
If \(M\) is the total side-length charge, \(E\) the number of terminal
pairs, and \(V_{\rm cat}\) the number of possible bridge vertices, then
\[
                    N\le M+2E+(8h+1)V_{\rm cat}.         \tag{A.16c}
\]
All required nonempty witnesses stay at the asserted boundaries, including
each component's closing boundary. Empty bridge letters are deleted.

Uniformly for these two policies,
\(E=O(2^{8h}/h)\) and \(V_{\rm cat}=O(2^{7h})\). For the first bound,
there are three merges per tuple and at most \((a+b+c+d+e)^3\) leaves.
The five initial chain counts total \(O(2^{8h}/h^{5/2})\), and (3.17)
with its moment bounds gives an expected cubed length sum \(O(h^{3/2})\).
For the second, any bridge chain belongs to a hook-SCD binary tree on a
proper subset of the five original blocks, or is the ascending complement
of such a chain. Include both in the catalogue, at a factor of at most two.
Only finitely many trees, supports, and signs occur, independently of \(h\).
For each, the signed leaf chains
and subsequent merges give a chain partition of the corresponding
fixed-pivot slice, hence at most \(2^{|U|}\) chains. Every proper support
omits a block of size at least \(h\). External length choices merely
select from this catalogue. Consequently both errors in (A.16c) are
\(o(W(8h))\).

### An exact finite saving on the switching event

Let \(\rho(x,y,z)\) be the density at zero of the sum of centered uniforms
of lengths \(x,y,z\). For \(x\le y\le z\), (A.11)'s continuous formula is
\[
 \rho(x,y,z)={1\over z}-{(x+y-z)_+^2\over4xyz}.
\]
For sorted positive \(x_1\le\cdots\le x_4\), put
\(F_4(\mathbf x)=1/x_4+\rho(x_1,x_2,x_3)\). The integer floor in (A.11)
implies
\(sP_4(\mathbf v)/\prod_i v_i\ge F_4(\mathbf v/s)\).

The density \(\rho\) is nonincreasing in each length. Indeed a convolution
of centered uniform densities is symmetric and unimodal: adjoining a
uniform averages the previous density over a centered interval, and its
derivative away from zero has the sign of
\(f(x+u/2)-f(x-u/2)\le0\) for \(x>0\). At zero the average of a symmetric
unimodal density over an expanding interval is nonincreasing.
It follows that, when \(x,y,z\le1\),
\[
 F_4(x,y,z,u)\ge g(u):=
 \begin{cases}2-u/4,&0<u\le1,\\3/4+1/u,&u\ge1.\end{cases}
\]
For \(u\ge1\), isolate \(u\) and use \(\rho(x,y,z)\ge\rho(1,1,1)=3/4\).
For \(u\le1\), isolating one of the other factors gives at least
\(1+\rho(1,1,u)=2-u/4\); if \(u\) is isolated, use
\(1/u+3/4\ge2-u/4\). No optimality assertion about all merge policies
is needed.

Set \(\delta=d/s,\epsilon=e/s\), and define the nonnegative convex function
\[
 \psi(u)=\begin{cases}1-5u/4+u^2/4,&0\le u\le1,\\0,&u\ge1.\end{cases}
 \qquad \int_0^\infty\psi(u)\,du={11\over24}.
\]
The radii \(r/s\) are midpoint nodes of mesh \(2/s\) on
\([|\delta-\epsilon|,\delta+\epsilon]\). Convexity bounds their midpoint
sum by the integral. Since
\(g(u)=3/4+1/u-\psi(u)/u\) and the weights \(r/(de)\) sum to one,
\[
 {sP_0\over abcde}
 \ge\sum_r{r\over de}g(r/s)
 \ge {3\over4}+{1\over\max(\delta,\epsilon)}
                         -{11\over48\delta\epsilon}.
\]
Meanwhile \(sP_1/(abcde)\le1/\delta+1/\epsilon\). On (A.16b), therefore,
\[
 \boxed{P_0-P_1\ge{abcde\over s}
  \left({3\over4}-{1\over\min(\delta,\epsilon)}
                       -{11\over48\delta\epsilon}\right)
            \ge{37\over192s}abcde.}                    \tag{A.16d}
\]
This is a finite inequality, not a continuous-kernel approximation.

### Averaging and the certified coefficient

Let \(\mathcal L_n\) be an SCD chain length sampled with probability
proportional to its number of members. By (3.17), size bias, and
\(2^n/W(n)\sim\sqrt{\pi n/2}\),
\(\mathcal L_n/\sqrt n\) converges to \(Z\) of density
\(\sqrt{2/\pi}\,z^2e^{-z^2/2}\), \(z>0\). The moment bounds in A.5
justify the size bias. Weighting a five-factor tuple by \(abcde\) gives
independent laws \(\mathcal L_{2h-1}\) in the first three factors and
\(\mathcal L_{h-1}\) in the last two. The sixteen signed products have
total such volume \(2^{8h-1}\). Thus, writing
\[
 p_h=\Pr(\mathcal L_{2h-1}\le\sqrt h),\qquad
 q_h=\Pr(\mathcal L_{h-1}\ge2\sqrt h),
\]
and summing (A.16d), the total baseline and switched charges satisfy
\[
       M_0-M_1\ge{2^{8h-1}\over\sqrt h}{37\over192}p_h^3q_h^2.
                                                               \tag{A.16e}
\]

The baseline still has \(M_0/W(8h)\to c_4\). Across all last-two chain
pairs, their product SCD has the chain-length inventory of the
\((2h-2)\)-cube. The first three inventories are those of the
\((2h-1)\)-cube. The proof of A.5 applies with this one-coordinate change:
the four scaled uniform-chain laws have the same Rayleigh limit, and
\(16W(2h-1)^3W(2h-2)/(8W(2h-1)^4)\to1\). The same polynomial
charge bound and moment domination control the error.

Now \(p_h\to p=\Pr(\sqrt2Z\le1)\) and \(q_h\to q=\Pr(Z\ge2)\), with
\[
 p={1\over2\sqrt\pi}\int_0^1x^2e^{-x^2/4}\,dx
       \ge{17\over120\sqrt\pi},\qquad
 q\ge{12\over5}\sqrt{2/\pi}\,e^{-2}.
\]
The first bound uses \(e^{-x^2/4}\ge1-x^2/4\). For the second, integrate
by parts and use
\(\int_x^\infty e^{-u^2/2}du\ge xe^{-x^2/2}/(x^2+1)\).
Finally \(2^{8h-1}/(\sqrt h W(8h))\to\sqrt\pi\), so (A.16c)--(A.16e)
save at least
\[
 \sqrt\pi\,{37\over192}p^3q^2
 \ge{181781e^{-4}\over28800000\pi^2}=\Delta_8
\]
in the asymptotic coefficient.

The numerical comparison is also elementary and exact. Summing the
exponential series through \(1/5!\) and bounding its tail by \(7/4320\)
gives \(e<87/32\), whose fourth power is below \(55\). Polynomial division
in \(\int_0^1x^4(1-x)^4/(1+x^2)\,dx=22/7-\pi>0\) gives
\(\pi<22/7\), whose square is below \(10\). Hence
\(\Delta_8>181781/15840000000>11/10^6\).
For every dimension use \(h=\lfloor k/8\rfloor\) and at most seven top-bit
splices; \(2^{k-8h}W(8h)/W(k)=1+O(h^{-1})\). This proves (A.16a) in
all dimensions. It supplies neither a near-width almost-cover family nor
any of the open adaptive or common-family covering estimates.

## Appendix A.6: Centered terminal-rectangle ledger barrier [I]

This is a restriction on the preceding method, not on unrestricted OR
words. Split \(k=dh\), \(d,h\ge2\), into pivoted blocks as in A.5, and
put \(n=d(h-1)=k-d\). Refine every signed paired product by complete
centered product SCDs until two chains remain. Choices may depend on the
current child tuple. Retain whole paired terminal rectangles with side
lengths \(a,b\), and define their charged main length and omitted volume by
\[
 M_{\rm ret}=\sum_{\rm ret}(a+b),\qquad
 \delta=1-{2\sum_{\rm ret}ab\over2^k}.
\]
Uniformly over these refinements and selections, as \(n\to\infty\),
\[
 \boxed{{M_{\rm ret}\over W(k)}\ge\sqrt{k/n}
 \left({2\over\sqrt e}-O(\delta^{2/3})-\epsilon_n\right),
 \qquad\epsilon_n\to0.}                                 \tag{A.17}
\]
In particular vanishing designated-volume omissions still force the
coefficient \(2/\sqrt e>1\) in this terminal-rectangle ledger.

The ledger is literal: collect bidirected edges between bridge vertices
\((U,C)\), \((U^c,D^c)\) for all retained terminal pairs. The Euler
argument of A.3 gives both complementary families, with one extra bridge
per component. Every chain retains a fixed pivot, so cannot contain both
\(\varnothing\) and its full support. Since
\(|\beta(C)|=|C|+1-\mathbf1_{C_{\min}=\varnothing}
-\mathbf1_{C_{\max}=U}\ge|C|\), the resulting word length is at least
\(M_{\rm ret}\). No negative bridge correction is being ignored.

Complete each terminal rectangle by one final product SCD. Its lengths
are \(r=|a-b|+1,|a-b|+3,\ldots,a+b-1\). A centered SCD's length
inventory is determined by consecutive rank-count differences. The
unsigned initial products partition the \(n\)-cube, and signs preserve
lengths; therefore the full completed inventory, under every adaptive
refinement, is \(2^{d-1}\) copies of
\[
 c_n(r)=\binom n{(n-r+1)/2}-\binom n{(n-r-1)/2}
 ={2r\over n+r+1}\binom n{(n-r+1)/2},
 \quad r>0,\ r\equiv n+1\pmod2.
\]
For each rectangle put \(L=(a-b)^2/n,U=(a+b)^2/n\), and give its
interval the measure weight \(n/2^{k+1}\). The child intervals
\(((r-1)^2/n,(r+1)^2/n)\) partition \((L,U)\) up to endpoints. Thus
the full mixture density is exactly, almost everywhere,
\[
 g_n(s)={n\over4\,2^n}\sum_rc_n(r)
       \mathbf1_{\{(r-1)^2/n<s<(r+1)^2/n\}},\qquad\int g_n=1.
\]
If \(\eta_{\rm ret}\) is the retained interval measure and
\(g_{\rm ret}(s)=\int\mathbf1_{\{L<s<U\}}d\eta_{\rm ret}\), then
\[
 0\le g_{\rm ret}\le g_n,\quad \int(g_n-g_{\rm ret})=\delta,
 \quad {M_{\rm ret}\over W(k)}
 ={2^{k+1}\over W(k)\sqrt n}\int\sqrt U\,d\eta_{\rm ret}. \tag{A.18}
\]
Adjacent-binomial logarithms at displacement \(j=O(\sqrt n)\) give
\(-2j^2/n+O(j/n+j^3/n^2)\). Together with A.1 and the formula for
\(c_n(r)\), they imply essential uniform convergence on compact subsets
of \((0,\infty)\) to
\(g(s)=\sqrt{s}e^{-s/2}/\sqrt{2\pi}\). Above a threshold \(S\), a
weighted tail with factor \(s^{-1/2}\) is at most \(S^{-1/2}\), so
the weighted tail integrals also converge uniformly near threshold one.

For every interval and \(t>0\), splitting at \(t\) proves the identity
\[
 \sqrt U=\sqrt t\,\mathbf1_{\{L<t<U\}}
 +\tfrac12\int_t^\infty{\mathbf1_{\{L<s<U\}}\over\sqrt s}\,ds
 +\sqrt U\,\mathbf1_{\{U\le t\}}
 +\sqrt L\,\mathbf1_{\{L\ge t\}}.
\]
Drop the last two nonnegative terms and integrate. For the limiting full
density, the bound times \(\sqrt{2\pi}\) is
\((t+1)e^{-t/2}\), maximized at \(t=1\) with value \(2/\sqrt e\).
For retained intervals average \(t\) over \([1-e,1+e]\), \(0<e<1/2\).
Missing density mass \(\delta\) loses at most
\(\sqrt{1+e}\,\delta/(2e)+\delta/(2\sqrt{1-e})\); the full averaged
bound loses \(O(e^2)\). The preceding uniform convergence adds an error
depending only on \(n\). Choose \(e=\delta^{1/3}\) for small positive
\(\delta\), or let \(e\downarrow0\) for \(\delta=0\), and use
\(2^{k+1}/(W(k)\sqrt n)=\sqrt{2\pi k/n}(1+O(k^{-1}))\).
This proves (A.17), without convergence assumptions on the chosen policies.

The bound concerns designated paired rectangles and their bridge cost.
It neither charges additional targets from intervals crossing several
terminal boundaries nor excludes moving-center refinements or a new
leading-order sharing mechanism. It supplies no lower bound
\(\nu(k)\ge(2/\sqrt e-o(1))W(k)\). This ledger barrier does not settle
coefficient one; the separate proposed PBBS proof is recorded in 9.2 [P].

## Appendix A.7: Nine balanced accumulators and an overlapping staircase cover [I]

There is a deterministic all-dimension construction with
\[
 \boxed{\nu(k)\le(c_9+o(1))W(k),\qquad
 c_9={564480\pi^2-1105440\pi^4+723296\pi^6-62475\pi^8\over393216}
       <1.18071.}                                             \tag{A.19}
\]
The constant lies strictly between \(1.1807038038\) and \(1.1807038039\).
This proof uses an overlapping cover, not the terminal partitions of A.6.
All initial SCD children are retained. Probability is used only to evaluate
their total deterministic charge. No adaptive matching gate is assumed.

### A.7.1 A complete eight-bit template

For disjoint ordered quadruples \(I,J\) partitioning \(\{0,\ldots,7\}\),
take the family of unions of a prefix of \(I\) and a prefix of \(J\),
including empty prefixes. The following fourteen families cover every
eight-bit pattern. The displayed exact verifier includes the entire finite
template and checks all ranks, rather than inferring them from middle coverage.

```python
rows = [
    ("0461", "5723"), ("0473", "2651"), ("0674", "3152"),
    ("0726", "1435"), ("1507", "4263"), ("1605", "7432"),
    ("2104", "6375"), ("2150", "7463"), ("3206", "7154"),
    ("3210", "4567"), ("3617", "5204"), ("4302", "6157"),
    ("5034", "6721"), ("5426", "7301"),
]

def prefixes(order):
    out = [0]
    for label in order:
        out.append(out[-1] | (1 << int(label)))
    return out

loads = [0] * 256
for left, right in rows:
    assert sorted(left + right) == list("01234567")
    for x in prefixes(left):
        for y in prefixes(right):
            loads[x | y] += 1
assert all(loads)
assert sum(loads) == 350
assert [sum(loads[x] for x in range(256) if x.bit_count() == r)
        for r in range(9)] == [14, 28, 42, 56, 70, 56, 42, 28, 14]
assert all(loads[x] == 1 for x in range(256)
           if 3 <= x.bit_count() <= 5)
```

The loops enumerate exactly the two-prefix family of each row, so positivity
of every load proves coverage. Each row has five middle targets; hence
\(70/5=14\) is also the minimum number of such families. There are 94
excess occurrences. These are not removed from the subsequent charge.

Equivalently, for any bits \(b_0,\ldots,b_7\), some row has nonincreasing
bits along both of its orders. We apply this to threshold bits of chain
indices, which establishes coverage of actual sets and not merely ranks.

### A.7.2 Actual staircase chains

On \(\ell\) coordinate chains of length \(2s\), consider
\[
 \mathcal S_{\ell,s}=
 \{\mathbf x\in\{0,\ldots,2s-1\}^{\ell}:
   \mathbf1_{x_1\ge s}\ge\cdots\ge\mathbf1_{x_\ell\ge s}\}.
\]
It has an explicit partition into \(s^{\ell-1}\) increasing chains, with
total membership \((\ell+1)s^\ell\). To prove this, start with the first
coordinate chain. Inductively, every current chain \(E_0<\cdots<E_{L-1}\)
has exactly \(s\) terminal members above its last coordinate's cut.
Adjoining a coordinate permits precisely the hook
\(i\ge L-s\) or \(y<s\) in \(E\times\{0,\ldots,2s-1\}\).
Its chains are, for \(0\le j<s\),
\[
 (E_0,j),\ldots,(E_{L-1-j},j),
 (E_{L-1-j},j+1),\ldots,(E_{L-1-j},2s-1).              \tag{A.20}
\]
A point \((E_i,y)\) belongs to the unique chain
\(j=\min(y,L-1-i)\); the hook condition is exactly \(j<s\).
Every resulting chain again has exactly \(s\) terminal members above the
new cut, proving the induction. All chains are saturated in index rank.
The chain indexed by \(j_2,\ldots,j_\ell\) has length
\(2\ell s-(\ell-1)-2\sum_{i=2}^{\ell}j_i\), and its endpoint ranks
sum to \(\ell(2s-1)\). Thus the chains are symmetric and certify the width.
The membership count also follows by splitting the staircase into its
\(\ell+1\) disjoint low/high subboxes, each of volume \(s^\ell\).

For \(\ell=4\), the chain count is \(R=s^3\) and membership is \(V=5s^4\).
Apply the fourteen rows of A.7.1 to eight equal coordinate chains, using
the same half cut on each axis. They cover the whole product. Decomposing
both staircases in every row gives paired rectangles with total side-length
charge
\[
              14(VR+RV)=140s^7=\alpha(2s)^7,
              \qquad\alpha={35\over32}.               \tag{A.21}
\]
Their excess volume is \(94s^8\), and remains included in this cost.
Union on disjoint physical supports sends each increasing index chain to
an increasing set chain, even when the input set chains are nonsaturated.

### A.7.3 Nine-factor compiler, padding, and all joins

Given nine strict ascending set chains on disjoint supports, set aside a
shortest chain of length \(r\). Sort the other lengths as
\(a_1\le\cdots\le a_8\), and put \(A=2\lceil a_8/2\rceil\).
Pad each of these eight chains to \(A\) formal positions by repeating its
last member. The index product maps surjectively onto the actual product.
Apply A.7.2 in formal indices, then remove consecutive repetitions inside
each image chain. Keep the image chains as an indexed family: different
chains may coincide or overlap, and membership is counted with multiplicity.
This creates no new physical coordinates and cannot increase any chain length.

In each row adjoin the set-aside chain to the first staircase shore.
For an image chain \(E\), a complete product SCD of \(E\times[r]\) has
membership \(r|E|\) and \(\min(r,|E|)\le r\) chains. It is taken only
after repetitions have been removed. Both factors then are strict chains
on disjoint supports, so the index-product construction is valid.
Consequently the terminal paired-rectangle charge is at most
\(r\alpha A^7\). Every child and every target remains covered.

There is a second complete construction with charge
\(r(a_8+a_7)\prod_{i=1}^6a_i\). Isolate a longest factor, partition the
other seven factors into lines along the second longest, and adjoin
the shortest chain to the isolated factor by a product SCD. Since
\(r\le a_8\), this multiplies the original charge by exactly \(r\).
Choose the smaller of these two numerical upper charges:
\[
 P_9\le r\min\left\{\alpha A^7,
                        (a_8+a_7)\prod_{i=1}^6a_i\right\}.       \tag{A.22}
\]
Normalization is always by the actual volume \(r\prod_i a_i\), never
by the padded volume. The continuum upper function is therefore
\[
 \Phi(\mathbf a)=\min\left\{
       {\alpha a_8^7\over\prod_i a_i},\ {1\over a_8}+{1\over a_7}
                         \right\},
 \qquad \Phi(a,\ldots,a)={\alpha\over a},\quad
                0\le\Phi(\mathbf a)\le {2\over a_1}.             \tag{A.23}
\]
It is continuous and homogeneous of degree minus one. The second
construction supplies the domination even for very unequal lengths.

Here a local row compiler is enough; no global bridge-catalogue assertion
is needed. If the left indexed chain family has \(R\) chains and membership
\(V\), and the right has \(S\) chains and membership \(Z\), sum (A.10)
over the right chains. Its literal word length is at most
\[
                        SV+RZ+2RS+Z+S.                \tag{A.24}
\]
The prefix/suffix proof of (A.10) needs only strict chains, not saturation:
a larger set difference still costs one permitted letter. Every right
chain's closing bridge is included. All nonempty targets of the product
and its full complement have ordinary interval witnesses inside their row.

Let \(L\) be the sum of the nine input lengths. In a padded row after
absorption, \(R=O((L+1)^4)\), \(S=O((L+1)^3)\), and
\(Z=O((L+1)^4)\). For the line construction, take the absorbed longest
factor on the left: \(R\le L\), \(S\le L^6\), \(Z\le L^7\).
Thus all fourteen rows, or the line alternative, compile with overhead
\(O((L+1)^7)\) beyond (A.22), and main charge \(O((L+1)^8)\).
Padding, overlap, every endpoint letter, and every closing are paid.

### A.7.4 Complete deterministic refinements and their weighted law

Fix an integer \(m\ge9\) first, and split \(mh\) coordinates into \(m\)
blocks of size \(h\). Take SCDs on each block minus a pivot. As in A.5,
the \(2^{m-1}\) signed complementary product pairs partition the cube:
the pivots fix the signs and global complement, and the SCDs fix ownership.

Keep the first nine chains in labeled accumulator slots. Read the remaining
chains in fixed order. Merge the next chain into a currently shortest
accumulator, using a complete product SCD. Retain every child and continue
the same rule at each child. Break ties by slot label. Crucially, the slot
is chosen before inspecting the unread chain's length. When no chain
remains unread, apply A.7.3 to the terminal nine-tuple. Concatenate its
row words, then concatenate the words of all branches and signed tuples.
This is a finite deterministic universal word, not a sampled construction.

Let \(L\) be the sum of the initial \(m\) lengths. The sum of the nine
accumulator lengths and all unread lengths never increases: a merge
replaces \(a+b\) by a child length at most \(a+b-1\). It stays at most
\(L\), so every merge has at most \(L\) children.
There are \(m-9\) initial merges. The preceding terminal bounds therefore
give main charge \(O_m((L+1)^{m-1})\) and total nonprincipal charge
\(O_m((L+1)^{m-2})\) per initial tuple. The number of initial tuples is
\(O_m(2^{mh}/h^{m/2})\); the SCD moment estimates of A.5 give
\(\mathbb E(L+1)^j=O_m(h^{j/2})\) for each fixed \(j\). Hence all
nonprincipal positions total
\(O_m(2^{mh}/h)=o(W(mh))\).

Let \(P\) be the sum of the smaller upper charges in (A.22) over all
branches of an initial tuple. Its total signed charge is exactly
\[
       2^{mh-1}\mathbb E_{\rm vol}{P(a_1,\ldots,a_m)\over\prod_i a_i}.
                                                               \tag{A.25}
\]
Here each initial chain is independently selected with probability
proportional to its length. The normalization uses
\(\sum_C|C|=2^{h-1}\). This bias is applied before the overlapping cover,
not to its repeated target occurrences.

By (3.17) and size bias, such a length divided by \(\sqrt h\) tends to
\(Z\) of density \(\sqrt{2/\pi}\,z^2e^{-z^2/2}\), \(z>0\), with
the requisite polynomial moment bounds. This is the \(\chi_3\) law.
A product SCD of lengths \(a,b\) has child lengths
\(|a-b|+1,|a-b|+3,\ldots,a+b-1\), whose sum is \(ab\).
The volume-biased child probabilities are \(r/(ab)\); their mesh-two
continuum kernel is
\[
             K(a,b;dr)={r\over2ab}\mathbf1_{|a-b|<r<a+b}\,dr.
\]

For fixed \(m\), the discrete charges converge to their continuum
integrals. One can see this without a singular domination assumption:
the unweighted terminal upper function is
\(r\min\{\alpha a_8^7,(a_8+a_7)\prod_{i=1}^6a_i\}\), continuous even
at zero lengths and of degree eight. Even rounding of \(A\) contributes
only degree seven. Each further mesh-two merge becomes a half integral,
increasing the degree by one. At a minimum-slot tie, the two choices
produce the same numerical length multiset. Ordinary Riemann convergence
on compact sets and the polynomial SCD moment bounds justify the induction
and the initial expectation. No estimate uniform in \(m\) is asserted.

Run the same nine-slot kernel process with \(m\) independent inputs
\(Z/\sqrt m\), and let \(Y_{1,m}\le\cdots\le Y_{8,m}\) be its eight
largest terminal radii. Since
\(2^{mh-1}/(\sqrt h W(mh))\to\sqrt{\pi m/8}\), homogeneity and (A.25)
give the fixed-\(m\) upper coefficient
\[
       Q_m=\sqrt{\pi/8}\,\mathbb E\Phi(Y_{1,m},\ldots,Y_{8,m}),
       \qquad \limsup_{h\to\infty}{\nu(mh)\over W(mh)}\le Q_m.   \tag{A.26}
\]

### A.7.5 Nine independent clocks and reciprocal convergence

Take nine independent standard three-dimensional Brownian motions \(B_i\),
started at zero, with separate mesh clocks. At each of \(m\) updates advance
the clock of a currently shortest-radius path by \(1/m\). Reveal only that
path's next increment. The first nine steps seed different slots almost
surely. Each later unrevealed increment remains an independent
\(N(0,I_3/m)\) vector: the chosen slot depends only on already revealed
increments. Its norm is \(Z/\sqrt m\); conditional on that norm, its cosine
with the current vector is uniform on \([-1,1]\). The radius of their sum
therefore has exactly kernel \(K\). This couples the law in (A.26).

Let \(\omega_m\) be the largest vector oscillation from a left mesh endpoint
within any mesh interval of the nine paths on \([0,1]\). Let \(A_m\) be the
largest current radius, \(B_m\) the second smallest, and \(H_i\) each path's
largest sampled radius up to its allocated time. Minimum updates imply
\[
 A_m=\max_iH_i,\qquad A_m-B_m\le\omega_m,\qquad
                         A_m-\omega_m\le H_i\le A_m.             \tag{A.27}
\]
Indeed updating a minimum preserves a maximum. The eight untouched radii
already have spread at most \(\omega_m\); a new value entering that group
is at most the old minimum plus \(\omega_m\). At the update attaining the
eventual maximum, all old radii were at least \(A_m-\omega_m\), proving
the historical bound. The second smallest current radius never decreases.

Put \(\tau_i(a)=\inf\{t:|B_i(t)|=a\}\),
\(\sigma(a)=\sum_{i=1}^9\tau_i(a)\), and
\(A=\sup\{a:\sigma(a)\le1\}\). First-hit times of a continuous path are
strictly increasing and left-continuous in the level: increasing levels
converging to \(a\) have limiting hit time that itself hits \(a\).
Every path has reached \((A_m-\omega_m)_+\) by its allocated clock time,
and its continuous past has not reached \(A_m+2\omega_m\). The allocated
times sum to one, so
\[
 \sigma((A_m-\omega_m)_+)\le1<\sigma(A_m+2\omega_m),\qquad
                 A_m-\omega_m\le A\le A_m+2\omega_m.
\]
Uniform continuity gives \(\omega_m\to0\) almost surely. All eight charged
radii consequently tend to \(A\); no assertion is needed about the ninth,
currently smallest radius.

Let \(\tau\) be the unit-ball exit time of a standard three-dimensional
Brownian motion started at zero, and \(S_9\) a sum of nine independent
copies. The exact inverse event is \(A<a\) if and only if \(\sigma(a)>1\).
Brownian scaling at fixed \(a\) gives \(A^{-2}\overset d=S_9\).
Stopping \(|B_t|^2-3t\) at exit first truncated at a fixed time shows
integrability, then yields the exit-time mean \((1-|x|^2)/3\) from \(x\)
in the unit ball. In particular \(\mathbb E S_9=3\), and \(A>0\) almost
surely. A fixed-level hitting time has no time atoms, because hitting at
exactly \(t>0\) places a Gaussian vector on a sphere; this also removes
any ambiguity between strict distributional endpoints.

The mean bound and the Markov property in time blocks \(2/3\), and then
the reflection bound for the 27 coordinate paths, give
\[
 \Pr(\tau\ge t)\le2^{-\lfloor3t/2\rfloor},\qquad
 \Pr(A\le r)\le9\,2^{-\lfloor1/(6r^2)\rfloor},\qquad
 \Pr(\omega_m>\epsilon)\le108m e^{-m\epsilon^2/6}.
\]
After the nine seeding steps the radii are independent \(\chi_3/\sqrt m\).
Since \(\mathbb E\chi_3^{-2}=1\) and \(B_m\) never decreases,
\(\mathbb E B_m^{-2}\le9m\).

Set \(\epsilon=m^{-1/4}\) and
\(G_m=\{\omega_m\le\epsilon,\ A>6\epsilon\}\).
On this event, \(B_m\ge A-3\epsilon>A/2\), so (A.23) gives
\(\Phi(Y_m)\le4/A\). On its complement, Cauchy--Schwarz gives
\[
 \mathbb E[\Phi(Y_m)\mathbf1_{G_m^c}]
 \le2\sqrt{9m\Pr(G_m^c)},\qquad
 \Pr(G_m^c)\le108m e^{-m\epsilon^2/6}
                   +9\,2^{-\lfloor1/(216\epsilon^2)\rfloor}.
\]
This expectation tends to zero. The modulus failure bound is summable,
so \(G_m\) holds eventually almost surely. Since \(\mathbb E A^{-1}<\infty\),
dominated convergence on \(G_m\) proves
\[
       Q_m\longrightarrow \alpha\sqrt{\pi/8}\,\mathbb E\sqrt{S_9}.
                                                               \tag{A.28}
\]
Thus reciprocal expectations, not merely radii in distribution, converge.

### A.7.6 Exact evaluation and all dimensions

The regular radial solution of
\(u''/2+u'/r=su\), \(u(1)=1\), is
\(u(r)=\sinh(r\sqrt{2s})/(r\sinh\sqrt{2s})\).
The stopped bounded-solution martingale, or Ito's formula, gives
\(\mathbb E e^{-s\tau}=\sqrt{2s}/\sinh\sqrt{2s}\), its value at zero.
Tonelli and one integration by parts give
\(\mathbb E\sqrt X=(2\sqrt\pi)^{-1}
\int_0^\infty(1-\mathbb E e^{-sX})s^{-3/2}\,ds\).
Substituting the ninth power of the exit transform and \(x=\sqrt{2s}\)
turns (A.28) into
\[
 c_9={35\over64}I_9,\qquad
 I_9=\int_0^\infty\left({1\over x^2}-{x^7\over\sinh^9x}\right)dx.
                                                               \tag{A.29}
\]

For completeness set \(f=\operatorname{csch}x\), \(D=d/dx\).
The identity
\((\operatorname{csch}^p x)''=p^2\operatorname{csch}^p x+
p(p+1)\operatorname{csch}^{p+2}x\) gives
\[
 \operatorname{csch}^9x=
 {D^8-84D^6+1974D^4-12916D^2+11025\over40320}f.
\]
Integrating against \(x^7\) on \([\varepsilon,\infty)\) by parts, the
eighth derivative contributes \(1/\varepsilon+O(\varepsilon)\); all
other boundary terms vanish. The odd Laurent expansion
\(f=x^{-1}+O(x)\) shows there is no finite boundary constant. With
\(J_q=\int_0^\infty x^q/\sinh x\,dx\), the remaining terms are
\[
 I_9={21\over2}J_1-{329\over8}J_3+{3229\over240}J_5-{35\over128}J_7.
\]
Expanding \(\operatorname{csch}x=2\sum_{j\ge0}e^{-(2j+1)x}\) and using
nonnegative termwise integration gives
\(J_1=\pi^2/4,J_3=\pi^4/8,J_5=\pi^6/4,J_7=17\pi^8/16\).
These even-zeta evaluations can be checked by Parseval successively for
\(x,x^2,x^3,x^4\) on \([-\pi,\pi]\): their nonconstant coefficients are
\(2(-1)^{n+1}/n\), \(4(-1)^n/n^2\),
\(2(-1)^n(-\pi^2/n+6/n^3)\), and
\(8(-1)^n(\pi^2/n^2-6/n^4)\), respectively, with constant coefficients
\(2\pi^2/3\) for \(x^2\) and \(2\pi^4/5\) for \(x^4\).
Substitution proves the polynomial in (A.19).

Here is a short exact rational certificate for its numerical endpoints.
Machin's identity and the alternating-series remainder are justified in A.5.
No floating-point quadrature enters this calculation.

```python
from fractions import Fraction as F

def atan_interval(q):
    lo = sum((F((-1)**j, (2*j+1)*q**(2*j+1))
              for j in range(40)), F(0))
    return lo, lo + F(1, 81*q**81)

al, au = atan_interval(5)
bl, bu = atan_interval(239)
pl, pu = 16*al - 4*bu, 16*au - 4*bl
cl = (564480*pl**2 - 1105440*pu**4
      + 723296*pl**6 - 62475*pu**8) / 393216
cu = (564480*pu**2 - 1105440*pl**4
      + 723296*pu**6 - 62475*pl**8) / 393216
assert F(11807038038, 10**10) < cl <= cu < F(11807038039, 10**10)
assert cu < F(118071, 100000)
```

Finally, for each fixed \(m\), Section 2.2's top-bit splice extends the
constructed \(mh\)-dimensional word to \(k=mh+t\), \(0\le t<m\), at
length at most \(2^tN\). Its width correction
\(2^tW(mh)/W(k)\) tends to one. For each \(k\), construct candidates for
every \(9\le m\le\lfloor\sqrt k\rfloor\) and take a shortest one,
using the all-subsets word if that range is empty. This is a finite
deterministic construction. Every fixed \(m\) eventually is a candidate,
so (A.26)--(A.28) imply
\[
 \limsup_{k\to\infty}{\nu(k)\over W(k)}
                         \le\inf_{m\ge9}Q_m\le c_9.
\]
No compiler estimate uniform in a growing number of blocks is required.
This completes the full-cube constant improvement (A.19), not the
coefficient-one conjecture. The overlapping terminal cover is essential;
the partition restriction in A.6 therefore does not apply to this word.

# Appendix B: The sole self-containment exception—finite word bodies

The only mathematical data not printed in this handoff are the literal
whitespace-separated mask words answers/k01.word through
answers/k16.word and the later words answers/k17_upper25374.word,
answers/k17_upper24957.word, answers/k17_upper24715.word and
answers/k17_upper24668.word, answers/k17_upper24658.word,
answers/k17_optimal24313.word, answers/k18_optimal48623.word,
answers/k18_upper48626.word,
answers/k18_upper49316.word, answers/k19_upper94161.word and
answers/k20_upper188322.word.
This exception is
denoted **[W]**. The currently stored
byte bodies have the following SHA-256 integrity digests. These hashes are
provenance only; mathematical validity comes from applying the displayed
recurrence verifier to the supplied word bodies.

The lower-bound arithmetic from Section 2 is entirely internal:

| `k` | central `r` | `W` | `Lambda_r` | `d` | `B(k)` |
|---:|---:|---:|---:|---:|---:|
| 0 | - | - | - | - | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 1 | 2 | 0 | 0 | 2 |
| 3 | 2 | 3 | 3 | 1 | 4 |
| 4 | 2 | 6 | 4 | 1 | 7 |
| 5 | 3 | 10 | 15 | 2 | 12 |
| 6 | 3 | 20 | 21 | 1 | 21 |
| 7 | 4 | 35 | 63 | 2 | 37 |
| 8 | 4 | 70 | 92 | 2 | 72 |
| 9 | 5 | 126 | 255 | 2 | 128 |
| 10 | 5 | 252 | 385 | 2 | 254 |
| 11 | 6 | 462 | 1023 | 3 | 465 |
| 12 | 6 | 924 | 1585 | 2 | 926 |
| 13 | 7 | 1716 | 4095 | 3 | 1719 |
| 14 | 7 | 3432 | 6475 | 2 | 3434 |
| 15 | 8 | 6435 | 16383 | 3 | 6438 |
| 16 | 8 | 12870 | 26332 | 3 | 12873 |
| 17 | 9 | 24310 | 65535 | 3 | 24313 |
| 18 | 9 | 48620 | 106761 | 3 | 48623 |
| 19 | 10 | 92378 | 262143 | 3 | 92381 |
| 20 | 10 | 184756 | 431909 | 3 | 184759 |

For every `d>0`, the two integer inequalities

\[
(d-1)W+\binom d2<\Lambda_r\le dW+\binom{d+1}2
\]

are immediate from the displayed entries; when `d=0`, `Lambda_r=0`.

| \(k\) | length | SHA-256 |
|---:|---:|---|
| 1 | 1 | 4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865 |
| 2 | 2 | f251ddc12234e0da8d3b778bd0f7463fb477f16f47757f5617dc8b4ff4d4f14a |
| 3 | 4 | aafa934d13be209cc39a9b5cb0b140af652fc0eebd127c42c6c982422964a790 |
| 4 | 7 | efe145ebc697686a2e3bf53a36362b5025835f2eb0ba16a1a0e64e2abd4ec1ca |
| 5 | 12 | 72195450d0361b37fbf58442203014eff475b3f59222c907fab99743106eee06 |
| 6 | 21 | 7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d |
| 7 | 37 | dda4b06c2e35bda3ea8a876a90807172adee166567d84b587ef5ae68cae9bec7 |
| 8 | 72 | df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb |
| 9 | 128 | c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221 |
| 10 | 254 | 24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd |
| 11 | 465 | 746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850 |
| 12 | 926 | 6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851 |
| 13 | 1719 | 8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0 |
| 14 | 3434 | 7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17 |
| 15 | 6438 | f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b |
| 16 | 12873 | 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe |
| 17 (exact optimum) | 24313 | 7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9 |
| 17 (previous upper bound) | 24658 | 24f7f831b7446e942cc0927472296b2d20069f694b8bbad6374e65cc07b6f7fb |
| 17 (previous upper bound) | 24668 | 22af061610f9c6cb4708ccca77c8d8008f251a1cc40f92858ca79bf7ad2ffff6 |
| 17 (previous upper bound) | 24715 | 3e7da8c69f8d32ca73750e12b8746fc483f9d56a441ad94f1d3a2e9b4c11b2fe |
| 17 (earlier constructed bound) | 24957 | dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db |
| 17 (previous upper bound) | 25374 | 16951cef9e2efff841c6bbf9cc72f2061f35650dda850714fcceee7a7bb43208 |
| 18 (exact optimum) | 48623 | 6b191b447231c665bb1288cdc7ebdea5c73fd79502ef47015ee3d98fcf685be5 |
| 18 (previous upper bound) | 48626 | 52a68ff6bb2757c00b4be03edbb53eaf821d5dca0985d0a680941502d0c2315b |
| 18 (previous upper bound) | 49316 | abf5fd9f3ee7cd5e66afa777a271077e981ef14a62678b80c0bd52995ed7d37c |
| 19 (exact optimum) | 92381 | 1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414 |
| 19 (exact cyclic optimum) | 92378 | ff7e753ecd579283e519c14df10d3123bde562ca682c667af04543a5576192dc |
| 19 (previous upper bound) | 94161 | 1c039f3225afa9fa32306c26d44cd7d79a05a83077dd928889b2d43286f86224 |
| 20 (exact optimum) | 184759 | 047b990b9e9f7a4585ba5d8fadf9c3d191cd218c989c3ffacf6e351d91b88d02 |
| 20 (previous upper bound) | 188322 | 0d42106351f630eda5693e91a246ceb738f0704004a38b803eba8456aeec3874 |

Everything needed to interpret and verify those words is internal. Each file
is a whitespace-separated list of ordinary decimal integers. The following
recurrence is the complete verifier:

~~~python
def check(k, expected_length, masks):
    a = [int(x) for x in masks.split()]
    assert len(a) == expected_length
    assert all(0 < x < (1 << k) for x in a)
    ending, seen = set(), set()
    for x in a:
        ending = {x} | {y | x for y in ending}
        seen |= ending
    assert seen == set(range(1, 1 << k))
~~~

After processing position \(j\), induction shows that ending is exactly the
set of unions of nonempty intervals ending at \(j\): an interval is either
the singleton last letter or a previous ending interval extended by that
letter. Thus acceptance proves universality. Section 2 proves the matching
lower bounds analytically for dimensions1 through20. The optimal words
at17–20 match those lower bounds exactly. The cyclic19 row uses the
cyclic endpoint lower bound and cyclic interpretation specified in9.31;
it is not claimed ordinary universal without its three-letter opening.

**Optimal word at 17 [I]+[W].** The actual file
`answers/k17_optimal24313.word`, with the SHA above, passed the complete
recurrence and all 131,071 independent range-OR witness queries using
`scripts/verify_k17_optimal24313.py`. Reports and witnesses are in
`witnesses/k17_optimal24313/`. A separately implemented direct forward
scan checked 552,396 intervals and independently found every target;
its two-block opening and all five join identities also passed. See
Section 9.26 and `K17_OPTIMAL24313_VERIFIED_20260908.md`.
The former lifted word at18 has length48,626 and remains a verified
historical upper certificate.

**Optimal word at18 [I]+[W].** The actual file
`answers/k18_optimal48623.word`, with the SHA above, passes
`scripts/verify_k18_optimal48623.py`: all262143targets and every separate
range-OR witness check. Reports and witnesses are in
`witnesses/k18_optimal48623/`. The independently implemented first-coordinate
occurrence scan visits607684events and separately finds every target.
The matching internal endpoint proof gives48623, so this word is optimal.
SeeSection9.27 and `K18_OPTIMAL48623_VERIFIED_20260908.md`.

**Optimal words at19 and20 [I]+[W].** The actual files
`answers/k19_optimal92381.word` and `answers/k20_optimal184759.word`
pass complete independent forward and suffix enumerations and every
separate range-OR witness query. The complete reports and gzipped
ordinary witnesses are in `witnesses/k19_k20_optimal/`; the independent
forward bundle is `scratch/k19_k20_optimal_forward_20260909/`.
`scripts/verify_k19_k20_optimal_suffix_and_lift.py` additionally verifies
the width-length19 cycle, its safe opening, and byte-identical20 lift.
See9.31 and `K19_K20_OPTIMAL_AND_CYCLIC19_VERIFIED_20260909.md`.
The ordinary optimum claims depend only on these literal words and the
internal endpoint bound, not on a PBBS or search premise.

**Previous direct word at 17 [W].** Applying the displayed recurrence to
`answers/k17_upper24658.word` returned all 131,071 nonempty targets in an
independent `h100` run. Its SHA-256 is the row above. The standalone
`scripts/verify_k17_upper24658.py` additionally records one interval per
target and independently verifies every interval by a segment tree.
Both endpoints lie in the ordinary word; no wrapping is used. The report
and full target witnesses are in `witnesses/k17_upper24658/`. The earlier
24,668-, 24,715-, 24,957- and 25,374-words retain their own complete certificates.
This establishes the new upper bound without assuming anything about
the construction search. The following earlier boundary-splice proof is
retained unchanged as provenance for the prior 25,745 upper bound.

**Reversed boundary splice [I]+[W].** Let `X` be the listed `k=16` word,
`n=12873`, with zero-based half-open slices; write `U` for interval OR,
`z=65536`, and `mark(A)=[z|x for x in A]`. Set
`(a,b,c,d)=X[:4]=(50120,49994,33610,33640)`,
`u=a|b=50122`, `v=c|d=33642`. Then `c|u=u`, and

\[
 Y=\operatorname{reverse}(X[1:])+[z,u,v]+\operatorname{mark}(X[3:])
 \quad\hbox{has length }2n-1=25745.
\]

The source-only ledger is

| target | source interval |
|---:|---|
| 50120 | `X[1715:1717]` |
| 33610 | `X[4489:4490]` |
| 58346 | `X[165:170]` |
| 58347 | `X[5931:5937]` |
| 58351 | `X[6389:6397]` |
| 62447 | `X[6389:6399]` |
| 63471 | `X[1:10]` |

For unmarked targets, only source intervals starting at zero need repair.
The nine prefix ORs are
`50120,50122,50122,50154,58346,58347,58351,62447,63471`.
The ledger or `[u]`, `[u,v]` supplies each. Since
`a|U(X[1:10])=U(X[1:10])=63471`, every later prefix also occurs in
`X[1:]`; reversal preserves interval ORs.

For a marked target choose a source witness `X[i:j]`. If `i>=3`, use its
marked copy. If `i=1`, use the reversed left suffix followed by `z`.
If `i=2,j=3`, use the ledger's marked copy of `c`; if `i=2,j>=4`, use
`[v]+mark(X[3:j])`. If `i=0,j=1`, use the ledger's marked copy of `a`;
if `i=0,j=2` or `3`, use `[z,u]`; otherwise use
`[z,u,v]+mark(X[3:j])`. The repetitions of `d` are OR-idempotent.
The singleton `z` is present. This proves universality with no new [W] body.

The following finite ledger check and the preceding recurrence independently
replay the claim from the sole input `X`; `X` has the hash listed above.

```python
from functools import reduce
from operator import or_
U=lambda A: reduce(or_,A,0)
assert X[:4]==[50120,49994,33610,33640]
ledger={50120:(1715,1717),33610:(4489,4490),58346:(165,170),
        58347:(5931,5937),58351:(6389,6397),62447:(6389,6399),63471:(1,10)}
assert all(U(X[i:j])==t for t,(i,j) in ledger.items())
assert [U(X[:j]) for j in range(1,10)]==[
    50120,50122,50122,50154,58346,58347,58351,62447,63471]
assert X[0]|U(X[1:10])==U(X[1:10])==63471
Y=X[1:][::-1]+[65536,50122,33642]+[x|65536 for x in X[3:]]
check(17,25745," ".join(map(str,Y)))
```

Its single-space decimal body with one final newline has SHA-256
`ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38`.
Neither the boundary identities nor a complete resident central factor
alone supplies the missing length-24313 word: lower assignment, all upper
targets, and the final nonwrapping cut remain separate requirements.

# Appendix C: Complete proofs for the direct punctured route

This appendix contains the retained proofs for the direct punctured route. No computation or external file is a premise of an argument below.

## Appendix C.1: Boundary-polymer estimate

Let \(B_r\) be the punctured boundary graph whose vertices are the \(b\)
boundary cuts and whose \(4r\) edges are the tagged targets of one
configuration:
\[
 B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})
       \setminus\{\{0,1\},\{0,3\}\}.
\]
For an edge set \(T\subseteq E(B_r)\), let
\(q(T)=|V(T)|\) be its number of incident boundary cuts.  Define

\[
 \mathcal P_2(z)=
 \sum_{\substack{T\subseteq E(B_r)\\|T|\ge2}}
 |T|^2z^{|T|}r^{-q(T)}.
\]

There are absolute constants \(c_0,c_1>0\) such that, uniformly for
\(0\le z\le c_0\sqrt r\),

\[
 \boxed{\mathcal P_2(z)\le
 c_1\left({z^2\over r^2}+{z^4\over r^2}\right).}
\]

### Proof of the polymer estimate

Write a nonempty edge subgraph of \(B_r\) as the disjoint union of its
connected components.  In a graph of maximum degree four, an exploration
from a prescribed root vertex encodes every connected \(m\)-edge subgraph
by one of at most \(A_0^m\) bounded-choice exploration words, for an absolute
constant \(A_0\).  Thus the total activity \(z^m r^{-v}\) of connected
\(m\)-edge subgraphs is at most
\[
        bA_0^m z^m r^{-v}.
\]
For \(m=1,2,3\), simplicity and triangle-freeness give
\(v\ge2,3,4\), respectively.  The graph is triangle-free for \(b\ge11\):
three signed steps from \(\{1,3\}\) have odd integer sum of absolute value
at most nine and hence cannot vanish modulo \(b\).  The finitely many
smaller \(b\) are absorbed into the constants.  For \(m\ge4\), the density
bound \(m\le2(v-1)\) gives \(v\ge m/2+1\).  Consequently, if \(\eta_j\)
denotes the sum of \(m^j\) times the activities of connected polymers, and
\(\eta_2^{\ge2}\) omits the one-edge polymers, then for
\(z\le c_0\sqrt r\), after decreasing \(c_0\),
\[
\eta_0=O(z/r+z^4/r^2),\quad
\eta_1=O(z/r+z^4/r^2),\quad
\eta_2^{\ge2}=O(z^2/r^2+z^4/r^2).
\]
Dropping mutual vertex-disjointness between components only enlarges the
sum.  For \(|T|\ge2\),
\(|T|^2\le2|T|(|T|-1)\).  Marking the ordered pair of distinguished
edges either inside one nontrivial component or in two components, and
then applying the exponential formula, gives
\[
\mathcal P_2(z)
 \le2e^{\eta_0}\bigl(\eta_2^{\ge2}+\eta_1^2\bigr)
 =O(z^2/r^2+z^4/r^2).
\]
This proves the asserted estimate.

## Appendix C.2: Annealed regeneration


### Proof of annealed regeneration

Let \(t_F=|e\cap F|\) and put \(a=x^{-1}-1\).  If \(F\) overlaps \(e\) in
\(\ell\) lower and \(m\) middle targets, then, conditional on retaining
all targets of \(e\), its additional retention probability is
\(x^{2r-\ell}y^{2r-m}\).  Because \(y\ge x\), after division by
\(d_x=D_Mx^{2r}y^{2r-1}\) this is at most
\(yx^{-t_F}/D_M\).  Also
\((t-1)_+\le\binom t2\), and
\[
\binom t2x^{-t}
=x^{-2}\sum_{s=2}^t\binom ts\binom s2a^{s-2}.
\]
Double-counting pairs \((F,T)\) with
\(T\in\binom{e\cap F}{s}\) therefore gives
\[
\frac{\mathcal E_x(e)}{rd_x}
\le {y\over rD_Mx^2}
\sum_{s=2}^{4r}\binom s2a^{s-2}
\sum_{T\in\binom es}\deg(T).
\]
Apply the boundary-codegree theorem, set \(z=Ca\), and use
\(\binom s2\le s^2/2\).  For \(a>0\), the last double sum divided by
\(D_M\) is at most
\[
 {r^2\over2a^2}\mathcal P_2(Ca)=O_C(1+a^2).
\]
For \(a=0\) the same statement is the continuous limit, or follows
directly from the \(s=2\) term.  Since
\(\alpha<1/3\) gives \(Ca=o(\sqrt r)\), and
\(y/x=1+O(1/(rx))\), it follows that
\[
\frac{\mathcal E_x(e)}{rd_x}
=O_C\!\left({1+a^2\over rx}\right)
=O_C\!\left({1\over rx^3}\right)=o(1)
\]
uniformly for \(x\ge r^{-\alpha}\).

## Appendix C.3: Fixed-target residual variance

### Proof of the fixed-target variance bound

Condition on retaining \(v\), and write
\[
 X_v=\sum_{F\ni v}I_F,
\]
where \(I_F\) says that every target of \(F-\{v\}\) is retained.
All \(I_F\) have the same mean \(w_v\), so
\(\mu_v=\mathbb EX_v=d(v)w_v\).  If
\(t=|F\cap G|\), every common target other than \(v\) has retention
probability at least \(x\), whence
\[
 {\mathbb E(I_FI_G)\over\mathbb EI_F\,\mathbb EI_G}
 \le x^{-(t-1)}.
\]
With \(a=x^{-1}-1\),
\[
x^{-(t-1)}-1
=\sum_{\varnothing\ne S\subseteq(F\cap G)-\{v\}}a^{|S|}.
\]
Summing over ordered `F,G`, separating diagonal variances, and
double-counting `G` containing `\{v\}\cup S` gives
 \[
 {\operatorname{Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}+
 {1\over d(v)^2}\sum_{F\ni v}
 \sum_{\varnothing\ne S\subseteq F-\{v\}}
 a^{|S|}\deg(\{v\}\cup S)
 \le {1\over\mu_v}+{1\over d(v)}
 \max_{F\ni v}\sum_{\varnothing\ne S\subseteq F-\{v\}}
 a^{|S|}\deg(\{v\}\cup S).
\]

Here `d(v)` is the degree in the full punctured-configuration hypergraph, so
it is `D_M` or `D_L`. Choose a maximizing `F`, identify the canonical
boundary graph of the targets of `F` with `B_r`, and let \(R\) be the
boundary edge representing \(v\). Set
\(z=Ca\).  The boundary-codegree theorem and \(d(v)\ge D_M\) bound the last
term, up to one absolute factor, by
\[
\sum_{\varnothing\ne S\subseteq E(B_r)-\{R\}}
 z^{|S|}r^{2-|V(R\cup S)|}.
\]
To estimate this rooted sum, decompose \(R\cup S\) into its component
containing \(R\) and its other components.  The unrooted component
activity from the preceding polymer proof is
\(\eta_0=O(z/r+z^4/r^2)\).  A root component with one added edge costs
\(O(z/r)\); with two added edges it costs \(O(z^2/r^2)\), by
triangle-freeness; and with at least three added edges the density bound
gives the geometric tail
\[
\sum_{m\ge4}A_0^m z^{m-1}r^{1-m/2}=O(z^3/r).
\]
Dropping disjointness of the other components multiplies this by at most
\(e^{\eta_0}\), while the possibility of no added root edge and at least
one remote component contributes \(e^{\eta_0}-1\).  Hence the rooted sum
is
\[
O(z/r+z^3/r+z^4/r^2).
\]
For \(x\ge r^{-\alpha}\), \(\alpha<1/3\), one has
\(z=O_C(x^{-1})=o(\sqrt r)\); substitution yields
 \[
 {\operatorname{Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}+
O_C(a/r+a^3/r+a^4/r^2)
\le {1\over\mu_v}+O_C(1/(rx^3)).
\]
The mean \(\mu_v\) is exponential in this range, proving the final
\(o(1)\): indeed `D_M=exp((2+o(1))r log r)`, while each indicator `I_F`
requires exactly `4r-1` further targets, each retained with probability at
least `x`, so
`mu_v>=D_M x^{4r-1}=exp((2-4alpha+o(1))r log r)`.

## Appendix C.3bis: Rooted overlap kernels

Use the directed punctured-configuration hypergraph with parameter `r`.
Fix one target `v` and condition on retaining it.  Every other lower target
is retained independently with probability `x`, every other middle target
with probability `y>=x`, and

\[
                         x\ge r^{-\alpha}.           \tag{C.3bis.1}
\]

Let `mathcal F_v` be the `D=d(v)` configurations containing `v`.  Put

\[
 X_v=\sum_{F\in\mathcal F_v}I_F,
 \qquad \mu=\mathbb EX_v=Dw,                       \tag{C.3bis.2}
\]

where `I_F` says that all targets of `F-{v}` survive.  The mean `w` is the
same for every `F in mathcal F_v`, since every configuration has the same
two shore sizes.  For distinct `F,G in mathcal F_v`, write

\[
                   t(F,G)=|(F\cap G)-\{v\}|.        \tag{C.3bis.3}
\]

For each fixed real `c>=1`, define

\[
 R_c=\max_F {1\over D}\sum_{G\ne F}
                 (x^{-c t(F,G)}-1),                 \tag{C.3bis.4}
\]

and

\[
 Q_c=\max_F {1\over D}\sum_{\substack{G\ne F\\t(F,G)>0}}
                 x^{-c t(F,G)}.                     \tag{C.3bis.5}
\]

### Lemma C.3bis.1 (rooted kernel bounds)

For every fixed `c`, uniformly under (C.3bis.1), provided `c alpha<1/2`,

\[
 R_c=O_c\left({1\over r x^{3c}}+{1\over r^2x^{4c}}\right),
 \qquad
 Q_c=O_c\left({1\over r x^{3c}}+{1\over r^2x^{4c}}\right).   \tag{C.3bis.6}
\]

In particular

\[
                         R_1=O((rx^3)^{-1}).         \tag{C.3bis.7}
\]

#### Proof

The rooted-polymer proof for the variance applies with retention floor
`x^c`.  With

\[
                         a_c=x^{-c}-1,
\]

its nonnegative overlap expansion gives

\[
 R_c=O_c\left({a_c\over r}+{a_c^3\over r}
                         +{a_c^4\over r^2}\right)
       +e^{-\Omega_c(r\log r)}.                     \tag{C.3bis.8}
\]

The exponentially small term is the excluded diagonal `G=F`; it is
negligible because `c alpha<1/2`.  The activity condition in the polymer
estimate is also valid, since `a_c=O(r^(c alpha))=o(sqrt r)`.

To pass from `R_c` to `Q_c`, first note

\[
 {1\over D}\sum_{G\ne F}\mathbf1_{t(F,G)>0}
 \le {1\over D}\sum_{G\ne F}t(F,G)=O(1/r).         \tag{C.3bis.9}
\]

The last estimate is the coefficient of the linear activity in the same
rooted overlap polynomial: divide its bound
`O(a/r+a^3/r+a^4/r^2)` by `a` and let `a` decrease to zero.  All
coefficients are nonnegative, so the passage to the limit is valid.
Finally

\[
 \mathbf1_{t>0}x^{-ct}
 \le \mathbf1_{t>0}+(x^{-ct}-1),                   \tag{C.3bis.10}
\]

and (C.3bis.8)--(C.3bis.10), together with `a_c<=x^{-c}`, prove (C.3bis.6).
\(\square\)

### Lemma C.3bis.2 (unrooted surviving-row moments)

Let \(\mathcal N=b!\) be the number of configurations, let
\(\mathsf Z=\sum_FI_F\) count those surviving the independent product
retention, and put \(w_0=x^{2r}y^{2r}\). For every fixed \(s\ge1\), if
\(0<\alpha<1/(6s)\), \(x\ge r^{-\alpha}\), and \(y\ge x\), then
\[
 \boxed{{\mathbb E(\mathsf Z-\mathbb E\mathsf Z)^{2s}
       \over(\mathbb E\mathsf Z)^{2s}}
       =O_s((rx)^{-s}).}                                  \tag{C.3bis.11}
\]

#### Proof

For configurations \(F,G\), put \(t_0(F,G)=|F\cap G|\), and define
\[
\begin{aligned}
 \widehat R_c&={1\over\mathcal N}\max_F\sum_{G\ne F}
                    (x^{-ct_0(F,G)}-1),\\
 \widehat Q_c&={1\over\mathcal N}\max_F
        \sum_{\substack{G\ne F\\t_0(F,G)>0}}x^{-ct_0(F,G)}.
\end{aligned}                                             \tag{C.3bis.12}
\]
For every \(1\le c\le s\),
\(a_c=O(r^{c\alpha})=o(\sqrt r)\), so the polymer estimate applies. Let
\(A=\binom br\) and
\(\vartheta=D_M/\mathcal N=2r/A=e^{-\Theta(r)}\). With
\(a_c=x^{-c}-1\), expand \((1+a_c)^t-1\) and double-count
\(T\subseteq F\cap G\). Singleton \(T\)'s contribute
\(O(\vartheta r a_c)\), since \(F\) has \(4r\) targets and both target
degrees are \(\Theta(D_M)\). For \(|T|\ge2\), C.7 and C.1 give
\[
 {1\over\mathcal N}\sum_{\substack{T\subseteq F\\|T|\ge2}}
 a_c^{|T|}\deg(T)
 \le C\vartheta r^2\mathcal P_2(Ca_c)
 =O_c(\vartheta(a_c^2+a_c^4)).                            \tag{C.3bis.13}
\]
Also
\[
 {1\over\mathcal N}\sum_{G\ne F}\mathbf1_{t_0(F,G)>0}
 \le {1\over\mathcal N}\sum_{G\ne F}t_0(F,G)
 =O(\vartheta r).                                         \tag{C.3bis.14}
\]
Consequently
\[
\begin{aligned}
 \widehat R_c&=O_c(\vartheta(ra_c+a_c^2+a_c^4)),\\
 \widehat Q_c&=O_c(\vartheta(r+ra_c+a_c^2+a_c^4)).
\end{aligned}                                             \tag{C.3bis.15}
\]

Expand the \(2s\)-th centered moment. For distinct rows, join two indices
when their configurations overlap. A singleton dependency component has
zero expectation. After summation, a two-row component costs
\((\mathcal Nw_0)^2\widehat R_1\). For a component of \(j\ge3\) rows,
put \(t_{ab}=t_0(F_a,F_b)\). A uniformly random spanning tree of the
complete graph on \([j]\) contains each pair with probability \(2/j\).
Thus a maximum-weight spanning tree \(T\) satisfies
\[
 \sum_{a<b}t_{ab}\le {j\over2}\sum_{ab\in T}t_{ab}.
\]
The positive-overlap graph is connected, so \(T\) may use only positive
edges. Since \(0<x\le1\),
\[
 x^{-\sum_{a<b}t_{ab}}
 \le\prod_{ab\in T}\mathbf1_{\{t_{ab}>0\}}
                         x^{-(j/2)t_{ab}}.
\]
There are \(j^{j-2}\) labelled trees. Root one and sum its leaves
successively with \(\widehat Q_{j/2}\). The component sum is at most
\[
 O_j((\mathcal Nw_0)^j\widehat Q_{j/2}^{\,j-1}).
\]
Because \(\vartheta=e^{-\Theta(r)}\) while
\(a_c\le r^{c\alpha}\), (C.3bis.15) is smaller than every required fixed
power of \((rx)^{-1}\). Thus a \(j\)-row component costs
\(O_s((\mathcal Nw_0)^j(rx)^{-j/2})\); multiplying components gives the
right side of (C.3bis.11).

For repeated rows use
\((I-w_0)^h=A_h(I-w_0)+B_h\), where
\(|A_h|\le1\) and \(|B_h|\le w_0\), and group equal indicators.
The resulting terms have fewer distinct rows and an extra \(w_0\) for
each constant group. They are negligible because
\(\mathcal Nw_0\ge\exp((2-4\alpha+o(1))r\log r)\).
\(\square\)

## Appendix C.3ter: Fixed slices and the stopped Palm reduction

We first remove exact shore cardinalities as a possible obstruction.  Let
`R` be a uniformly random `m`-subset of an `N`-set and put `p=m/N`.  For a
fixed `a`-set `U`,

\[
 \Pr(U\subseteq R)={(m)_a\over(N)_a}.              \tag{C.3t.1}
\]

If `a<=q<=m/2`, then

\[
 \left|\log{{(m)_a/(N)_a}\over p^a}\right|
 \le {2q^2\over m}.                                \tag{C.3t.2}
\]

Indeed, the logarithm is

\[
 \sum_{i=0}^{a-1}\{\log(1-i/m)-\log(1-i/N)\},
\]

and the derivative of `log(1-z)` has absolute value at most two on
`[0,1/2]`.  Thus two independent uniform shore slices, of densities at
least `x` and minimum population `N_*`, reproduce every query using at most
`q` coordinates on either shore with relative error

\[
                              O(q^2/(xN_*)).         \tag{C.3t.3}
\]

The error remains relative to the rare survival scale after centering.
Fix a root target \(v\) and distinct configurations `F_1,...,F_j` containing \(v\). Let `I_F` be its survival
indicator, let `w` and `tilde w` be its product and slice means, and write

\[
                         t(F,G)=|(F\cap G)-\{v\}|.
\]

For each shore \(\sigma\), let \(p_\sigma\) be its product retention probability, let \(a_\sigma\) be the number of nonroot shore-\(\sigma\) targets in one \(F_i\), and for \(S\subseteq[j]\) put
\[
 u_\sigma(S)=\left|\bigcup_{i\in S}((F_i\cap V_\sigma)-\{v\})\right|.
\]
Thus \(w=\prod_\sigma p_\sigma^{a_\sigma}\). When the union queries at most `q` coordinates per shore, expansion over
subsets of `[j]` and (C.3t.3) give

\[
 \left|
 \mathbb E_{\rm sl}\prod_i(I_{F_i}-\widetilde w)
 -\mathbb E_{\rm prod}\prod_i(I_{F_i}-w)
 \right|
 \le C_j{q^2\over xN_*}
 w^j x^{-\sum_{a<b}t(F_a,F_b)}.                   \tag{C.3t.4}
\]

To verify the scale explicitly, for every subset `S` in the centered
expansion the product probability divided by `w^|S|` is

\[
 \prod_\sigma p_\sigma^{-(|S|a_\sigma-u_\sigma(S))}
 \le x^{-\sum_{a<b\in S}t(F_a,F_b)},              \tag{C.3t.5}
\]

because a coordinate of multiplicity `c` satisfies
`c-1<=binom(c,2)`.  Also `tilde w/w=1+O_j(q^2/(xN_*))`.
Equations (C.3t.3)--(C.3t.5), term by term over the `2^j` subsets, prove
(C.3t.4).

Now condition on a fixed root target and let `X_v` be its residual degree.
For a fixed `2s`th moment, a tuple queries `q=O_s(r)` coordinates per shore.
The punctured target populations satisfy `N_*=exp(Omega(r))`, so the error
in (C.3t.4) is exponentially small.  It remains to sum its overlap weight.
If `R_c` is the rooted kernel from C.3bis, insertion of `F_i` after
`F_1,...,F_(i-1)` uses

\[
 x^{-\sum_{a<i}t(F_a,F_i)}
 \le {1\over i-1}\sum_{a<i}x^{-(i-1)t(F_a,F_i)}   \tag{C.3t.6}
\]

by arithmetic--geometric mean.  Successive row sums therefore give

\[
 \sum_{F_1,\ldots,F_j\ {\rm distinct}}
 x^{-\sum_{a<b}t(F_a,F_b)}
 \le D^j\prod_{i=2}^j(1+R_{i-1})=O_s(D^j).        \tag{C.3t.7}
\]

Repeated configurations cause no larger error.  Group equal indicators
and use, for every fixed power,

\[
 (I-u)^a=A_a(I-u)+B_a,\qquad |A_a|\le1,\quad |B_a|\le u.       \tag{C.3t.8}
\]

Every resulting constant group removes at least one distinct configuration
and contributes a factor at most `w`; after summation these terms are
`O_s(mu^(2s-1))`, exponentially smaller than the main scale.  Combining (C.3t.4)--(C.3t.8) with the product dependency-component estimate (G.21)--(G.22) gives, uniformly on every exact two-shore slice, where \(\widetilde\mu=\mathbb E_{\rm sl}X_v\),

\[
 \boxed{
 {\mathbb E_{\rm sl}(X_v-\widetilde\mu)^{2s}
       \over\widetilde\mu^{2s}}
 =O_s((rx^3)^{-s})+O_s(r^2/(xN_*))}               \tag{C.3t.9}
\]

for `alpha<1/(6s)`.  The identical slice comparison applied to Lemma C.3bis.2 gives

\[
 {\mathbb E_{\rm sl}(\mathsf Z-\mathbb E_{\rm sl}\mathsf Z)^{2s}
       \over(\mathbb E_{\rm sl}\mathsf Z)^{2s}}
 =O_s((rx)^{-s})+O_s(r^2/(xN_*)).                 \tag{C.3t.10}
\]

## Appendix C.5: Isolated-count covariance and one-cap descent

Use the process and averages of Section 4.2.  Fix \(K\ge1\), put
\(\gamma=1/(96K)\), \(p_j=\gamma/(r\bar d_j^M)\), and assume the two
maximum-degree caps (4.7) while \(x_j\ge r^{-\alpha}\), where
\(0<\alpha\le1/(256K)\).  Then

\[
 \Pr(\text{the caps persist to the threshold but a bite estimate or
 the descent fails})\le e^{-\Omega(r)}.
\]

On the complementary stopped event the accepted configurations form a
matching leaving \(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and
\(o(1)\) of the middle shore, and the average-degree floor remains at
least \(\exp(r\log r)\).

### Proof

Let \(G_j\) be the conflict graph on the \(Z_j\) surviving
configurations, let \(g_e\) be its degrees, and let
\(\Delta=\max_e g_e\).  For a general graph with \(Z\) vertices, mark
vertices independently with probability \(p\), and let \(A\) count marked
vertices having no marked neighbour.  Put
\[
q_e=p(1-p)^{g_e},\qquad \mu=\mathbb EA.
\]
Adjacent vertices have nonpositive covariance.  If \(e,f\) are
nonadjacent and \(c_{ef}=|N(e)\cap N(f)|\), then exactly
\[
\operatorname{Cov}(I_e,I_f)
=q_eq_f\{(1-p)^{-c_{ef}}-1\}.
\]
When \(p\le1/2\) and \(p\Delta\le B\), the braces are at most
\(2e^{2B}pc_{ef}\): indeed
`-log(1-p)<=2p`, so the braces are at most
`exp(2p c_(ef))-1`, and `exp(u)-1<=u exp(u)` for `u>=0`.
Finally,
\[
\sum_{e,f}c_{ef}=\sum_h|N(h)|^2\le Z\Delta^2,
\qquad
\mu\ge Zp(1-p)^\Delta\ge Zpe^{-2B}.
\]
Consequently
\[
{\operatorname{Var}A\over\mu^2}
\le C_B\left({1\over Zp}+{p\Delta^2\over Z}\right).
\tag{*}
\]

Each accepted configuration removes exactly `2r` targets from both shores.
Consequently
`|M_j|-|L_j|=|M_0|-|L_0|=2|L_0|/r`. Since
`|L_j|=x_j|L_0|`, under the displayed maximum-degree cap and while
\(x_j\ge r^{-\alpha}\), the exact shore relation is
\[
{ |M_j|\over|L_j|}
={\bar d_j^L\over\bar d_j^M}
=1+{2\over rx_j}\le2
\]
for all sufficiently large \(r\).  Hence
\[
\Delta(G_j)\le
2rK\bar d_j^M+2rK\bar d_j^L
\le6Kr\bar d_j^M.
\]
Also
\[
{1\over Z_j}\sum_e g_e
\le{1\over Z_j}\sum_vd_j(v)(d_j(v)-1)
\le2Kr(\bar d_j^M+\bar d_j^L)
\le6Kr\bar d_j^M.
\]
Since \(u\mapsto(1-p_j)^u\) has nonnegative second derivative, the finite
chord-induction proof of Jensen gives
\[
{\mathbb E(A_j\mid H_j)\over Z_jp_j}
\ge(1-p_j)^{6Kr\bar d_j^M}.
\]

Now take \(\gamma=1/(96K)\).  Once
\(\bar d_j^M\ge e^{r\log r}\), the last display is at least
\(e^{-12K\gamma}=e^{-1/8}\); here
`log(1-p)>=-2p` for `0<=p<=1/2`, as follows by differentiating the two
sides. In (*) one has
\(p_j\Delta\le1/16\), and the exact identity
\[
Z_jp_j={\gamma|M_j|\over2r^2}
\]
shows that the relative variance is
\(O_K(r^2/|M_j|)=e^{-\Omega(r)}\): indeed
`|M_j|>=|L_j|=x_j|L_0|>=r^(-alpha)|L_0|=e^(Omega(r))`;
the last fact follows from the binomial-average lower bound on `|M_0|` and
`|L_0|=r|M_0|/(r+2)`. Moreover `e^(-1/8)>=1-1/8=7/8`, so
`E(A_j|H_j)>=7Z_jp_j/8`; the event `A_j<Z_jp_j/2` has a fixed positive
relative deviation from this mean. Chebyshev's inequality in the form
`Pr(|A-EA|>=t)<=Var(A)/t^2` now gives the required lower bound below.
For the upper bound, if `Y` is the total number marked, then
`E(2^Y)=(1+p_j)^(Z_j)<=exp(Z_jp_j)`; the elementary Markov inequality
`E(2^Y)>=2^(2Z_jp_j)Pr(Y>=2Z_jp_j)` makes the failure probability at most
`exp(-(2 log 2-1)Z_jp_j)`. Since `A_j<=Y`, these two estimates give
\[
{1\over2}Z_jp_j\le A_j\le2Z_jp_j
\tag{**}
\]
with conditional failure \(e^{-\Omega(r)}\).

It remains only to justify the degree floor used in this argument.  Start
from
\[
Z_0={|M_0|D_M\over2r}=(2r+1)!,
\qquad \log Z_0=(2+o(1))r\log r.
\]
Every accepted configuration has \(2r\) targets on each shore, so its
closed conflict neighbourhood has size at most
\[
2rK\bar d_j^M+2rK\bar d_j^L\le6Kr\bar d_j^M.
\]
By the upper bound in (**),
\[
Z_j-Z_{j+1}
\le A_j\,6Kr\bar d_j^M
\le12K\gamma Z_j=Z_j/8.
\]
The lower bound in (**) removes at least \(\gamma/(2r)\) of each
residual shore per round.  Thus the lower density reaches
\(r^{-\alpha}\) within
\[
J_*=\left\lceil{2\alpha r\log r\over\gamma}\right\rceil
\]
rounds.  For \(\alpha\le1/(256K)\),
\[
\log Z_j\ge\log Z_0+j\log(7/8)
\ge(2-o(1))r\log r-{J_*\over7},
\qquad
{J_*\over7}\le{3\over28}r\log r+O(1).
\]
Since \(|M_j|\le\binom{2r+1}r=e^{O(r)}\), this implies
\(\bar d_j^M\ge e^{r\log r}\), closing the induction.  The conditional
failure probabilities union-bound over the
\(O_K(r\log r)\) stopped rounds.  Accepted configurations are disjoint
within a round, and deletion of their targets makes different rounds
disjoint.  The one-round overshoot is \(1+O_K(1/r)\), and
\[
{|M_j|\over|M_0|}={rx_j+2\over r+2}=o(1).
\]
Therefore
\[
\Pr(\text{the cap persists to the threshold but a bite estimate or the
descent fails})\le e^{-\Omega(r)}.
\]
Equivalently, outside an event of that probability, either the cap fails
first or the union of accepted configurations is a matching leaving
\(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and \(o(1)\) of the middle
shore. If a separate theorem makes cap failure `o(1)`, the two bad events
combine by a union bound.

## Appendix C.5a: Average-conflict descent and bounded arrival test [I]/[C]

For a finite simple graph on \(Z>0\) vertices, let \(g_e\) be its degrees,
\(C_e=g_e+1\), \(\bar C=Z^{-1}\sum C_e\), and independently mark vertices
with probability \(0<p<1\). If \(I_e\) indicates an isolated mark, put
\(A=\sum I_e\), \(S=\sum C_eI_e\). Without a maximum-degree assumption,
\[
 \boxed{\begin{aligned}
 \mathbb EA&\ge Zp(1-p)^{\bar C-1},&\mathbb ES&\le pZ\bar C,\\
 \operatorname{Var}A&\le Zp+p^3\sum g_e^2,&
 \operatorname{Var}S&\le Z\bar C+p\sum g_e^2.
 \end{aligned}}                                           \tag{C.5a.1}
\]
Indeed \(\mathbb EI_e=p(1-p)^{g_e}\), so Jensen proves the expectations.
Adjacent covariances are nonpositive. For nonadjacent \(e,f\), write
\(a=1-p\), \(c=|N(e)\cap N(f)|\); their covariance is
\(p^2a^{g_e+g_f-c}(1-a^c)\le p^3c\). AM--GM gives
\(pCa^{(C-1)/2}\le p\sum_{i=0}^{C-1}a^i=1-a^C\le1\).
Since \(c\le\min(g_e,g_f)\), the weighted covariance is at most
\(pc[pC_ea^{g_e/2}][pC_fa^{g_f/2}]\le pc\), and the weighted diagonal
variance is at most \(C_e^2pa^{g_e}\le C_e\). Sum using
\(\sum_{e,f}|N(e)\cap N(f)|=\sum g_e^2\), proving (C.5a.1).

If this is the conflict graph of a hypergraph of nonempty edges of size at
most \(q\), then, with \(\Delta_C=\max C_e\),
\[
 \boxed{\Delta_C^2\le qZ\bar C,\qquad
                 \sum g_e^2\le\Delta_C Z\bar C.}          \tag{C.5a.2}
\]
Partition a largest closed neighborhood by one chosen witness vertex in
its edge. The at most \(q\) classes are cliques, so their sizes \(s_i\)
satisfy \(\sum s_i=\Delta_C\) and \(\sum s_i^2\le Z\bar C\);
Cauchy proves the first bound, and \(g_e^2\le\Delta_C g_e\) the second.

For the punctured process use closed conflict sizes, counting each edge
itself, and retained shore sizes including isolated targets. Define
\[
 z_\sigma={2rZ\over n_\sigma},\qquad
 \chi(H)={\bar C\over2r(z_M+z_L)},\qquad \chi(H)=\infty\ (Z=0).
                                                               \tag{C.5a.3}
\]
Keep C.5's \(K\ge1,\gamma=1/(96K),\alpha\le1/(256K)\), marking rule
\(p=\gamma/(rz_M)\), and threshold \(x_*=r^{-\alpha}\), but stop at
\(x\le x_*\) or \(\chi>K\), giving the density threshold priority.
No purge or other target deletion is made. The initial \(\chi\le1\),
and (4.7) implies \(\chi\le K\); no converse is used.

At a live state, C.5's exact shore identity gives \(z_L/z_M\le2\), hence
\(p\bar C\le1/16\). As \(\bar C\ge1\), this already proves
\(p\le1/16\) without a degree-floor assumption. With \(n=n_M\),
\[
 Zp={\gamma n\over2r^2},\quad {\bar C\over Z}\le{12Kr^2\over n},
 \quad {\Delta_C\over Z}\le\delta:=\sqrt{48Kr^3/n},
\]
\[
 {\operatorname{Var}A\over(Zp)^2}\le{2r^2\over\gamma n}+{\delta\over16},
 \qquad {\operatorname{Var}S\over Z^2}\le{12Kr^2\over n}+{\delta\over16}.
\]
Also \(\mathbb EA\ge e^{-1/8}Zp\ge7Zp/8\), \(\mathbb ES\le Z/16\).
Chebyshev and the total-mark bound from C.5 therefore give, conditionally
on every live history, except with probability \(e^{-\Omega(r)}\),
\[
 \tfrac12Zp\le A\le2Zp,\qquad S\le Z/8,\qquad Z'\ge7Z/8. \tag{C.5a.4}
\]
Here \(n\ge x_*|L_0|=e^{\Omega(r)}\), and the last inequality follows
because deleted edges lie in the union of the accepted closed neighborhoods.
Thus \((1-4\gamma/r)x\le x'\le(1-\gamma/(2r))x\).
Union-bound the conditional errors over
\(J_*=\lceil2\alpha r\log r/\gamma\rceil\) rounds. Outside probability
\(e^{-\Omega(r)}\), the stop occurs by \(J_*\), all reached states have
\(z_M\ge e^{r\log r}\) by C.5's \(Z_0(7/8)^j\) calculation, and either
\(\chi>K\) occurs first or the accepted matching leaves lower density
\(x_*(1+O_K(r^{-1}))\) and middle density \((rx+2)/(r+2)=o(1)\).
This is a proved stopped alternative, not persistence.

For \(K>1,Z>0\), put
\(U_{m,\sigma}=n_\sigma^{-1}\sum_v|d(v)/z_\sigma-1|^m\) and
\[
 T_K(H)=\min\{1,[(\chi-1)_+/(K-1)]^2\},\qquad T_K(H)=1\ (Z=0).
\]
Then \(\mathbf1_{\{\chi>K\}}\le T_K\le1\), and on nonempty states
\[
 T_K\le{U_{4,M}+U_{4,L}\over(K-1)^2}.                      \tag{C.5a.5}
\]
Indeed \(\bar C\le Z^{-1}\sum_vd(v)^2
=2r\sum_\sigma z_\sigma(1+U_{2,\sigma})\). Squaring the weighted
average gives the sharper numerator
\(\sum_\sigma z_\sigma U_{4,\sigma}/(z_M+z_L)\), since
\(U_{2,\sigma}^2\le U_{4,\sigma}\).

On a uniform exact two-shore slice of densities
\(y\ge x\ge r^{-\alpha}\), \(\alpha<1/12\), let \(m=\mathbb EZ>0\) and
\(\mu_\sigma=2rm/n_\sigma\), the exact retained-root mean. C.3ter with
\(s=2\) bounds the rooted normalized fourth moment by
\(O((rx^3)^{-2})+e^{-\Omega(r)}\), and the unrooted one by
\(O((rx)^{-2})+e^{-\Omega(r)}\). If
\(V_\sigma=n_\sigma^{-1}\sum_v|d(v)/\mu_\sigma-1|^4\), root summation
gives the former bound for \(\mathbb EV_\sigma\). On \(Z\ge m/2\),
Jensen and \(|u+v|^4\le8(|u|^4+|v|^4)\) give
\(U_{4,\sigma}\le256V_\sigma\). The complementary event, including
\(Z=0\), has probability at most \(16\mathbb E|Z/m-1|^4\). Hence
\[
 \boxed{\mathbb E_{\rm sl}T_K=O_K((rx^3)^{-2})+e^{-\Omega(r)}.}
                                                               \tag{C.5a.6}
\]
This also holds for subprobability mixtures of such slices. No untruncated
inverse-\(Z\) moment or adaptive comparison is asserted.

Let \(\tau\) be the actual alternative stop and \(\mathcal F_j\) the
history before round \(j\). The precise sufficient remaining input is [O],
uniformly for \(j<J_*\):
\[
 \boxed{\mathbb E\left[\mathbf1_{\{j<\tau\}}
 \mathbf1_{\{x_{j+1}>x_*\}}T_K(H_{j+1})\right]
 \le r^{\kappa+o(1)}(rx_*^3)^{-2}+e^{-\Omega(r)},
 \qquad\kappa<1-6\alpha.}                                \tag{C.5a.7}
\]
The child is evaluated before discarding it for a new cap violation.
At the first violation before threshold its test equals one and its
parent is live. Summing (C.5a.7) gives
\(O(r\log r)r^{\kappa-2+6\alpha+o(1)}=o(1)\); (C.5a.4) handles
late stopping and bite failures. Restricting to histories with successful
earlier bites is also sufficient. Conditioning the child to satisfy its
cap removes precisely the event that must be bounded. The actual shapes
inside the slice mixture need not be uniform, so (C.5a.6) does not prove
(C.5a.7). Even its proof would supply only a two-rank bank for subsequent
all-depth work, not original Gate A or Gate B.

One exact drift diagnostic explains why no automatic sign was used. Let
\(B\) be the closed conflict matrix, \(T=\mathbf1^TB\mathbf1\).
Accepting one uniformly chosen edge and deleting its neighborhood gives
\[
 \mathbb E(T'-T\mid H)
 ={\operatorname{tr}(B^3)-2\sum_eC_e^2\over Z}.           \tag{C.5a.8}
\]
For its column \(b_e\), expand
\((\mathbf1-b_e)^TB(\mathbf1-b_e)\) and average. Thus normalized
conflict drift still involves triangles and degree variation. For example,
in \(N\) disjoint ordinary triangles, after accepting \(j\) disjoint edges,
\(n=3N-2j,Z=3(N-j),\bar C=3\); the rank-two normalization
\(\bar C/(2z)=(3N-2j)/(4(N-j))\), \(z=2Z/n\), diverges while a third
of the vertices remain. This is only a generic warning, not a punctured
counterexample or a refutation of (C.5a.7).

## Appendix C.7: Global boundary-codegree theorem

For targets \(T\) inside one fixed directed punctured configuration, let
\(q(T)\) be the number of distinct boundary cuts used by those targets.
For every \(|T|\ge2\), an absolute constant \(C\) satisfies

\[
 \boxed{{\deg(T)\over D_M}\le C^{|T|}r^{2-q(T)}.}
\]

The boundary graph is
\(\operatorname {Cay}(\mathbb Z_{2r+1},\{\pm1,\pm3\})\) with the two
start-zero edges deleted, and every subgraph with \(m\) edges and \(v\)
nonisolated vertices satisfies \(m\le2(v-1)\).

### Proof of the punctured-circulant density bound

Before the linear relabelling, a retained middle window starting at \(i\)
has boundary edge \(\{i,i+r\}\), and a retained lower window has boundary
edge \(\{i,i+r-1\}\).  Multiplication by \(-2\) modulo
\(b=2r+1\) sends these differences to \(1\) and \(3\), respectively.
The two dirty starts remove \(\{0,1\}\) and \(\{0,3\}\).

For a proper nonempty \(U\subset\mathbb Z_b\), let
\(\partial_d(U)\) be the number of step-\(d\) edges crossing its cut in
the full circulant.  The number of full-circulant edges induced by \(U\)
is
\[
2|U|-{\partial_1(U)+\partial_3(U)\over2}.
\]
The step-one cycle is connected, so \(\partial_1(U)\ge2\).  If
\(\partial_3(U)>0\), parity gives \(\partial_3(U)\ge2\).  If it is zero,
then \(3\mid b\) and \(U\) is a nontrivial union of complete step-three
cycles; its step-one cut has at least \(2b/3\) edges.  Thus every proper
\(U\) induces at most \(2(|U|-1)\) edges.  Deleting the two dirty edges
cannot increase this number, while the full punctured graph has
\(2b-2=2(b-1)\) edges.  Therefore every subgraph with \(m\) edges and
\(v\) nonisolated vertices satisfies \(m\le2(v-1)\).

### Proof of the boundary-codegree inequality

Fix \(T\subseteq e\), put \(t=|T|\), and list its \(q\) distinct boundary
cuts cyclically.  For target lengths \(k,h\in\{r,r-1\}\), fixing one
cyclic start and the intersection size leaves at most four possible
relative starts: the exact numbers are \(b-k-h+1\) in the disjoint case,
two in a proper overlap, and \(|k-h|+1\) in a containment.  Hence, after
choosing an anchor target, the number \(P(T)\) of retained positional
tuples having the prescribed labelled Venn signature satisfies
\[
                         P(T)\le(b-1)4^{t-1}.          \tag{B1}
\]

Let \(n_\sigma\) be the sizes of the labelled Venn cells and set
\[
V(T)=\prod_\sigma n_\sigma!.
\]
For a fixed positional tuple, labels may be assigned independently inside
corresponding cells in exactly \(V(T)\) ways.  Conversely, a proper
nonempty target has a unique cyclic start in a fixed word, so no word is
counted twice.  Thus
\[
                         \deg(T)=P(T)V(T).             \tag{B2}
\]

The \(q\) cuts divide the circle into positive elementary gaps
\(g_1,\ldots,g_q\), with sum \(b\); put \(G(T)=\prod_i g_i!\).
We claim
\[
                         V(T)\le8^{t-1}G(T).           \tag{B3}
\]
For one target, its arc and complement are exactly the two elementary gaps,
so `V=G` and the initial ratio `R=V/G` is one. Expose the remaining target
arcs one at a time. Splitting an
old Venn cell of size \(n\) into sizes \(p,n-p\) multiplies \(V\) by
\(\binom np^{-1}\), while splitting an elementary gap of size \(g\) into
\(a,g-a\) multiplies \(G\) by \(\binom ga^{-1}\).
If the two new cuts lie in distinct old gaps, independently selecting the
prescribed labels from those split gaps injects into the prescribed
subset of the containing Venn cell.  Therefore the product of the gap
binomials is at most the corresponding cell binomial, even when the two
gaps belong to the same cell, and \(R\) does not increase.  With one new
cut the same injection applies.  With two old cuts, \(G\) is unchanged
and every Venn-cell factorial can only decrease, so again \(R\) does not
increase.

If both new cuts lie in one old gap of size \(g\), write the three pieces
as \(x,y,z\), where \(y\) lies between the new cuts.  The gap refinement
factor is
\[
\binom gy\binom{g-y}x.
\]
The middle segment is either the new arc or its complement, so
\(y\in\{k,b-k\}\).  Fix the selected labels outside the old gap.
Adjoining a \(y\)-subset of the gap injects into the prescribed selected
subsets of the old Venn cell; if the middle segment is the complement,
apply the same injection to unselected labels and use binomial symmetry.
Thus the Venn-cell split cancels the first binomial.
After the first target has been exposed, every old gap has size at most
\(r+2\); hence \(g-y\le3\) if \(y=k\), and \(g-y\le1\) if
\(y=b-k\).  The uncancelled factor is at most
\(2^{g-y}\le8\).  This proves (B3) by induction.

Every gap is at most \(r+2\).  Factorial log-convexity says that moving one
unit from a smaller positive gap to a larger nonsaturated gap cannot
decrease the product of factorials.  Repeating this transfer yields
\[
G(T)\le
\begin{cases}
(r+2)!(r-q+1)!,&2\le q\le r,\\
(2r-q+2)!,&r+1\le q\le2r+1.
\end{cases}                                            \tag{B4}
\]
For completeness, for `1<=m<=n` the falling-factorial estimate used next is
internal:
\[
 \binom nm=\prod_{i=0}^{m-1}{n-i\over m-i}\ge(n/m)^m,
 \qquad
 \log(m!)\ge\int_1^m\log x\,dx\ge m\log m-m.
\]
Multiplication gives \((n)_m=m!\binom nm\ge(n/e)^m\). Using this, the
case `m=0` is immediate. The first case gives
\[
{G(T)\over r!(r+1)!}
\le {r+2\over(r)_{q-1}}
\le3e^{q-1}r^{2-q},
\]
and the second gives
\[
{G(T)\over r!(r+1)!}
\le e^{q-1}r^{1-q}\le e^q r^{2-q}.
\]
Thus, uniformly,
\[
{G(T)\over r!(r+1)!}\le(3e)^q r^{2-q}.                \tag{B5}
\]

Finally \(D_M=(b-1)r!(r+1)!\), and \(q\le2t\).
Combining (B1)--(B5) gives
\[
{\deg(T)\over D_M}
\le4^{t-1}8^{t-1}(3e)^q r^{2-q}
\le\{32(3e)^2\}^{t}r^{2-q}.
\]
This proves the displayed theorem with the explicit absolute constant
\(C=32(3e)^2\).

## Appendix C.8: Directed punctured-configuration profile

### Deck reconstruction, degrees, and the fractional optimum

In the unpunctured deck, containment between its \((r-1)\)- and
\(r\)-windows is the alternating cycle.  A cyclic \((r-1)\)-interval is
contained in exactly its two one-point end extensions, so there are no
other containment edges.  Deleting \(L_0,M_0\) leaves the path
\[
L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r}.
\]
Its endpoint layers orient it canonically.  The recovered same-start
pairs satisfy
\[
M_i\setminus L_i=\{w_{i+r-1}\},\qquad1\le i\le2r.
\]
These give every word position except \(r-1\); the unique unused label
gives that final position.  Hence \(w\mapsto E(w)\) is injective and there
are \(b!\) configurations.

For a fixed \(k\)-set, prescribing any of its \(b-1\) retained starts
gives \(k!(b-k)!\) words, with no overcount because a proper cyclic
interval has a unique start.  Therefore
\[
D_M=(b-1)r!(r+1)!=2r\,r!(r+1)!,
\]
\[
D_L=(b-1)(r-1)!(r+2)!={r+2\over r}D_M.
\]
Weighting every configuration by \(1/D_L\) loads each lower target by
one and each middle target by \(D_M/D_L=r/(r+2)\).  Its total mass is
\[
{b!\over D_L}={|\mathcal L|\over2r},
\]
using the lower incidence identity
\(b!\,2r=|\mathcal L|D_L\).  No fractional matching can have larger mass:
each edge consumes \(2r\) units of the total lower capacity
\(|\mathcal L|\).  This proves optimality.

### Complete pair calculation

For target sizes \(k,h\in\{r,r-1\}\) and intersection \(a\), set
\[
\Phi_{k,h}(a)=a!(k-a)!(h-a)!(b-k-h+a)!
\]
and
\[
m_{k,h}(a)=
\begin{cases}
b-k-h+1,&a=0,\\
2,&0<a<\min(k,h),\\
|k-h|+1,&a=\min(k,h).
\end{cases}
\]
For distinct layer-tagged targets \(A,B\),
\[
d(A,B)=
\bigl((b-2)m_{k,h}(a)+\mathbf1_{a=\min(k,h)}\bigr)
\Phi_{k,h}(a).                                        \tag{P1}
\]
Indeed, after fixing the first cyclic start, the three cases have exactly
the displayed numbers of relative starts.  A positional pair has
\(\Phi_{k,h}(a)\) labelings of its four Venn cells.  Of the
\(bm_{k,h}(a)\) ordered start pairs, \(2m_{k,h}(a)\) have a dirty start;
\((0,0)\) was removed twice and is restored exactly in the same-start
containment case.  This proves (P1).

Inside one fixed configuration, the complete unordered inventory is
\[
\begin{array}{c|c|c|c}
XY&a&N&d\\ \hline
MM&0\le a\le r-1&2r-1&
(4r-2)a!(r-a)!^2(a+1)!\\
LL&0&4r-2&(8r-4)(r-1)!^2\,3!\\
LL&1\le a\le r-2&2r-1&
(4r-2)a!(r-1-a)!^2(a+3)!\\
ML&0&6r-3&(6r-3)r!(r-1)!\,2!\\
ML&1\le a\le r-2&4r-2&
(4r-2)a!(r-a)!(r-1-a)!(a+2)!\\
ML&r-1&4r-1&(4r-1)(r-1)!(r+1)!.
\end{array}                                            \tag{P2}
\]
The \(N\)-column is the retained ordered-start count from (P1), divided
by two only for equal-layer pairs.  Thus (P2) is an analytic inventory,
not a finite census.

Let \(S_{XY}\) be the pair-codegree mass from the indicated layer pair.
Multiplying the last two columns of (P2) and using factorial cancellation
gives the exact sums
\[
{S_{MM}\over D_M}
={(2r-1)^2\over r}
\sum_{a=0}^{r-1}
{1\over\binom ra\binom{r+1}{a+1}},                    \tag{P3}
\]
\[
{S_{ML}\over D_M}
={1\over2r}\sum_{a=0}^{r-1}
{n_{ML}(a)^2\over\binom ra\binom{r+1}{a+2}},           \tag{P4}
\]
\[
{S_{LL}\over D_M}
={r+2\over4r^2}\sum_{a=0}^{r-2}
{n_{LL}(a)^2\over\binom{r-1}a\binom{r+2}{a+3}},        \tag{P5}
\]
where
\[
n_{ML}(a)=
\begin{cases}
3(2r-1),&a=0,\\
2(2r-1),&1\le a\le r-2,\\
4r-1,&a=r-1,
\end{cases}
\quad
n_{LL}(a)=
\begin{cases}
4(2r-1),&a=0,\\
2(2r-1),&1\le a\le r-2.
\end{cases}
\]
For example, the cancellation behind (P3) is
\[
{a!(r-a)!^2(a+1)!\over r!(r+1)!}
={1\over\binom ra\binom{r+1}{a+1}},
\]
and the other two are identical.

Isolating the endpoint terms in these reciprocal-binomial sums gives
\[
\sum_{a=0}^{r-1}
{1\over\binom ra\binom{r+1}{a+1}}
={1\over r}+{2\over r^3}+O(r^{-4}).
\]
In (P4), the containment, disjoint, and \(a=r-2\) terms are respectively
\[
8-{4\over r}+{1\over2r^2},\qquad
{36\over r}-{72\over r^2}+O(r^{-3}),\qquad
{16\over r^2}+O(r^{-3});
\]
all other terms total \(O(r^{-3})\).  In (P5), the \(a=r-2\) and
\(a=0\) terms are
\[
{4\over r}+O(r^{-3}),\qquad
{96\over r^2}+O(r^{-3}),
\]
and the rest total \(O(r^{-3})\).  Here are uniform remainder bounds.
In (P3), the omitted \(a=2\) and \(a=r-2\) terms are respectively
\(O(r^{-5})\) and \(O(r^{-4})\); for
\(3\le a\le r-3\), both binomial factors are \(\Omega(r^3)\), so all
middle terms total \(O(r^{-5})\).  In (P4), the common proper-overlap
prefactor is \(O(r)\): the \(a=1\) term is \(O(r^{-3})\), and after it
is removed the two binomial factors have product \(\Omega(r^5)\), apart
from the already displayed right endpoint layers, so the remaining
\(O(r)\) terms total \(O(r^{-3})\).  The same argument applies to (P5):
its prefactor is \(O(r)\), its \(a=r-3\) term is \(O(r^{-3})\), and all
other undisplayed terms have binomial product \(\Omega(r^5)\).  The
finitely many small \(r\) are absorbed by the constants.  This proves the
stated remainder bounds.
Substitution proves
\[
{S_{MM}\over D_M}=4-{4\over r}+{9\over r^2}+O(r^{-3}),
\]
\[
{S_{ML}\over D_M}=8+{32\over r}-{111\over2r^2}
+O(r^{-3}),
\qquad
{S_{LL}\over D_M}={4\over r}+{96\over r^2}+O(r^{-3}),
\]
and hence the displayed expansion for \(S(e)\).

### Path localization, maximum codegree, and the first bite

The containment pairs in (P2) form the reconstructed alternating path and
number \(4r-1\).  In the full middle cyclic deck, disjointness joins
successive windows in the odd-graph cyclic order; deleting \(M_0\) leaves
a path of \(2r-1\) edges.  The two skeleton masses, obtained from the
\(ML,a=r-1\) and \(MM,a=0\) rows of (P2), sum to
\[
{(2r-1)^2\over r(r+1)}
+{(4r-1)^2\over2r^2}
=12-{12\over r}+{19\over2r^2}+O(r^{-3}).
\]
Subtracting from (P3)--(P5) leaves
\[
{44\over r}+{40\over r^2}+O(r^{-3})
\]
of normalized off-skeleton mass.  The successive factorial ratios in the
MM, LL, and proper-ML rows are, respectively,
\[
{(a+1)(a+2)\over(r-a)^2},\qquad
{(a+1)(a+4)\over(r-1-a)^2},\qquad
{(a+1)(a+3)\over(r-a)(r-1-a)}.
\]
Each is increasing in \(a\), so every row maximum occurs at an endpoint.
Substitution shows that every off-skeleton pair has codegree
\(O(D_M/r^2)\).  For \(r\ge3\), the largest pair codegree is the
containment value
\[
\Delta_2=(4r-1)(r-1)!(r+1)!,
\qquad
{\Delta_2\over D_L}={4r-1\over2r(r+2)},
\]
so \(4r\Delta_2/D_L\to8\).
For \(r=2\), the disjoint LL pair is the finite exceptional maximum; it
does not affect the asymptotic statement.

For the bite calculation, let \(C(e)\) be the number of other
configurations meeting \(e\), and put
\[
A(e)=\sum_{v\in e}(d(v)-1)=2r(D_M+D_L)-4r.
\]
For \(F\ne e\), \(t_F-1\le\binom{t_F}2\), so
\[
A(e)-\left(S(e)-\binom{4r}2\right)
\le C(e)\le A(e).
\]
Thus
\[
C(e)=4(r+1)D_M(1+O(1/r)).
\]
If configurations are marked independently with
\(p=\gamma/(rD_M)\), a fixed marked configuration is isolated with
probability
\[
(1-p)^{C(e)}=\exp(-4\gamma+o(1)).
\]
Isolated marked configurations form a matching.  Multiplying their
retention probability by \(D_M\) or \(D_L\) gives expected covered
fractions
\[
{\gamma e^{-4\gamma}+o(1)\over r},
\qquad
{r+2\over r}{\gamma e^{-4\gamma}+o(1)\over r},
\]
which proves the claimed calibrated first bite.

## Appendix C.9: Exact all-depth occurrence-capacity threshold

Put `b=2r+1`,

\[
 \mathcal M={ [b]\choose r},\qquad
 \mathcal L={ [b]\choose {r-1}},\qquad
 A=|\mathcal M|,\qquad B=A/b=\operatorname{Cat}_r,\qquad
 L=|\mathcal L|={r\over r+2}A.                    \tag{C.9.1}
\]

Let `P` be any matching of directed punctured configurations and write
`p=|P|`.  Since each configuration contains exactly `2r` lower targets,
there is a unique `x in [0,1]` such that

\[
                         2rp=(1-x)L.               \tag{C.9.2}
\]

For `1<=q<=r-1`, retain the same `2r` nonzero starts and form the indexed
occurrence multisets

\[
 \mathcal S_q^-(P)=\{I_{r-q}^w(s):E(w)\in P, s\ne0\},
\]
\[
 \mathcal S_q^+(P)=\{I_{r+1+q}^w(s):E(w)\in P, s\ne0\}.       \tag{C.9.3}
\]

Let \(\mathcal H_q^-\) and \(\mathcal H_q^+\) be the complements of those two supports in their full layers, put \(h_q^\pm=|\mathcal H_q^\pm|\), and set

\[
 B_q={b\choose {r-q}}={b\choose {r+1+q}}.          \tag{C.9.4}
\]

Every multiset in (C.9.3) has exactly `2rp=(1-x)L` indexed occurrences.
Its support can only be smaller.  Therefore, without any probabilistic or
order hypothesis,

\[
 \boxed{h_q^-,h_q^+\ge[B_q-(1-x)L]_+},             \tag{C.9.5}
\]

and hence

\[
 \boxed{
 \sum_{q=1}^H(h_q^-+h_q^+)
 \ge2\sum_{q=1}^H[B_q-(1-x)L]_+.}                 \tag{C.9.6}
\]

We now locate the exact scale of this rank-volume obstruction.  The ratio
has the product form

\[
 {B_q\over L}=\prod_{j=1}^{q-1}{r-j\over r+j+2}. \tag{C.9.7}
\]

Since

\[
 {r-j\over r+j+2}
 =1-{2j+2\over r+j+2}\ge1-{2j+2\over r},
\]

and `prod_j(1-u_j)>=1-sum_j u_j` for `0<=u_j<=1`,

\[
 \boxed{{B_q\over L}\ge1-{(q-1)(q+2)\over r}.}    \tag{C.9.8}
\]

Indeed, if the right side is nonpositive this is trivial; otherwise the
sum of the displayed `u_j` is below one, so every `u_j` lies in `[0,1]`
and the product inequality applies.

Assume `rx>=64` and set

\[
 Q=\min\left\{H,\left\lfloor{\sqrt{rx}\over4}\right\rfloor\right\}.
\]

For `q<=Q`,

\[
 {(q-1)(q+2)\over r}
 \le{x\over16}+{1\over2}\sqrt{x\over r}
 \le{x\over8},                                    \tag{C.9.9}
\]

where the last inequality uses `sqrt(x/r)=x/sqrt(rx)<=x/8`.
Equations (C.9.6)--(C.9.9) give

\[
 \sum_{q=1}^H(h_q^-+h_q^+)\ge {7\over4}xLQ.       \tag{C.9.10}
\]

If `H>=floor(sqrt(rx)/4)`, then `floor(sqrt(rx)/4)>=sqrt(rx)/8`, so

\[
 \boxed{
 \sum_{q=1}^H(h_q^-+h_q^+)
 \ge {7\over32}L\sqrt r\,x^{3/2}.}               \tag{C.9.11}
\]

Because `L/A=1-o(1)`, Gaussian-band aggregate holes can be `o(A)` only if

\[
                              \boxed{x=o(r^{-1/3}).} \tag{C.9.12}
\]

In particular, `x=r^{-alpha}(1+o(1))` with any fixed
`alpha<=1/3` fails (C.9.12) for
`H=ceil(sqrt(b log b))`.  For `alpha<1/3`, the lower bound divided by `A`
grows as `Omega(r^((1-3alpha)/2))`; at `alpha=1/3` it stays bounded below.

The exponent is sharp for raw occurrence capacity.  From
`1-u<=e^{-u}` and `r+j+2<=2(r+1)`, (C.9.7) also gives

\[
 {B_q\over L}
 \le\exp\left\{-{(q-1)(q+2)\over2(r+1)}\right\}. \tag{C.9.13}
\]

If `x<=1/2` and `B_q>(1-x)L`, then
`-log(1-x)<=2x` implies

\[
                         (q-1)(q+2)<4(r+1)x.       \tag{C.9.14}
\]

Thus only `O(1+sqrt(rx))` summands in (C.9.6) are positive, and each is at
most `xL`.  Consequently its rank-volume right side is

\[
 O\bigl(Ax(1+\sqrt{rx})\bigr)=o(A)                \tag{C.9.15}
\]

when `x=o(r^{-1/3})`.  This removes only the numerical obstruction; it does
not make repeated windows distinct.

Restoring the omitted start in every selected row does not change the
threshold.  The full rows have

\[
 bp=\left(1+{1\over2r}\right)(1-x)L              \tag{C.9.16}
\]

occurrences at every rank.  Their effective deficit from `L` is

\[
 x-{1-x\over2r}\ge {3x\over4}                    \tag{C.9.17}
\]

when `x>=2/r`.  If `x<2/r`, then already `x=o(r^{-1/3})`; otherwise, on
any subsequence contradicting (C.9.12), the effective deficit times `r`
tends to infinity and the proof of (C.9.11) applies with changed constants.

Finally, when `x>>r^{-1/3}`, repairing even this occurrence deficit by
adjoining full rows needs

\[
 \Omega(xL/b)=\Omega(x\operatorname{Cat}_r)       \tag{C.9.18}
\]

additional rows, because each adds only `b` occurrences at a depth and
`L/b=(1-o(1))Cat_r`.  The same order supplies enough *counts*, but it says
nothing about distinct targets, common depths, or legality.  Thus the
current direct route requires either descent below (C.9.12) or a separate
integral cover-down of the order (C.9.18).

## Appendix C.10: Exact positive cover-down and cheap rounding

Continue with Appendix C.9, put \(B=A/b=\operatorname{Cat}_r\), and let `Q` be its shallow cutoff.  Restoring the
one omitted start in every selected configuration changes the aggregate
hole count by at most `2Hp<=2HB=o(A)` when `H=o(b)`.  For the enrichment
estimate retain the punctured hole sets of Appendix C.9.  For a row `C`,
define its shallow score against those sets by

\[
 S_Q(C)=\sum_{q=1}^Q\sum_{s\in\mathbb Z_b}
 \left({\bf1}_{I_{r-q}^C(s)\in\mathcal H_q^-}
       +{\bf1}_{I_{r+1+q}^C(s)\in\mathcal H_q^+}\right).       \tag{C.10.1}
\]

If `s` added rows leave at most `epsilon A` aggregate shallow holes, every
repaired target is counted at least once on the right, so (C.9.10) gives

\[
 \boxed{\sum_CS_Q(C)\ge {7\over4}xLQ-\epsilon A.}              \tag{C.10.2}
\]

For `x=r^{-alpha}(1+o(1))`, `alpha<1/3`,
`Q=floor(sqrt(rx)/4)`, `epsilon=o(1)`, and `s<=KxB`, division by `s`, using
`xQ->infinity`, yields average score at least
`(7/(4K)+o(1))bQ`.  A uniform random row instead has exact mean

\[
 b\sum_{q\le Q}\left({h_q^-\over\binom b{r-q}}+
 {h_q^+\over\binom b{r+1+q}}\right)=O(xbQ)          \tag{C.10.3}
\]

when every displayed hole count is `O(xA)`.  Thus a minimal cover-down
requires a genuine `Omega(1/x)` enrichment in the joint nested hole flag;
a one-rank packing alone does not certify it.

For the positive-cover question, now let `mathcal H` be the restored,
shore-tagged hole universe and exclude base rows from the set `Omega` of
candidate cyclic rows.  For `T in mathcal H,C in Omega`, let `M_(T,C)` be
the tagged window incidence.  The exact fractional physical-row cover number is

\[
 \tau^*(\mathcal H)=\min\left\{\sum_Cy_C:y_C\ge0,
                  \ \sum_CM_{T,C}y_C\ge1\ (T\in\mathcal H)\right\}. \tag{C.10.4}
\]

Finite covering duality gives

\[
 \boxed{\tau^*(\mathcal H)=\max\left\{\sum_Tz_T:z_T\ge0,
                \ \sum_TM_{T,C}z_T\le1\ (C\in\Omega)\right\}.} \tag{C.10.5}
\]

For self-containment, weak duality follows by reversing the two finite
sums.  If a number below the primal optimum were larger than every dual
value, separate the vector `(1,t)` from the closed nonnegative cone
generated by the columns `(M_C,1)`, `(-e_T,0)`, and `(0,1)`.  The separating
vector can be written `(-z,lambda)` with `z>=0`, `lambda>=0`,
`M^Tz<=lambda 1`, and `sum z>lambda t`.  Every target lies in a row, so
`lambda=0` is impossible; division by `lambda` gives a dual value above
`t`, a contradiction.  This proves (C.10.5).

The positive fractional gate has a cheap integral rounding.  More generally,
let `mathcal H' subseteq mathcal H` omit at most `o(A)` exceptional holes,
and suppose (C.10.4) on `mathcal H'` has a feasible vector of mass `t`.
Select each distinct row independently with probability
`min(1,lambda y_C)`.  The expected selected count is at most `lambda t`.
For every `T in mathcal H'`, either an incident row is certain or

\[
 \Pr(T\hbox{ uncovered})\le
 \exp\{-\lambda\sum_CM_{T,C}y_C\}\le e^{-\lambda}.             \tag{C.10.6}
\]

Two applications of Markov give one outcome with at most `4lambda t` rows
and at most `4|mathcal H'|e^{-lambda}` uncovered members.  Consequently,

\[
 \boxed{\tau^*(\mathcal H')=O(xB)}                              \tag{C.10.7}
\]

is sufficient: with `lambda=3 log r` it produces
`O(x log r B)=o(B)` physical rows, adds `O(x log r A)=o(A)` occurrences at
each rank, and leaves only `o(A)` aggregate holes, including the exceptional
set.  Hence no Baranyai--Katona factor or disjoint integral rounding theorem
is needed after (C.10.7).

Equivalently, (C.10.7) asks for a distribution on rows which contains every
nonexceptional hole with probability `Omega(1/(xB))`.  A concrete sufficient
condition is a (possibly labelled) candidate family `mathcal C` with

\[
 d_{\mathcal C}(T):=|\{C\in\mathcal C:M_{T,C}=1\}|\ge D_0,
 \qquad {|\mathcal C|\over D_0}=O(xB),              \tag{C.10.8}
\]

outside `o(A)` holes: weight every candidate by `1/D_0` and apply the
preceding rounding to that nonexceptional universe.  Labelled duplicate
copies may be sampled independently and then coalesced; coverage is
unchanged and the number of physical rows can only decrease.  For the stopped
catalogue this is an all-depth external-window degree floor; Gate A's
maximum-degree cap does not imply it.

There is also a weaker long-arc interface.  For a cyclic interval `J` of
`L_0` starts, charge all tagged depth-`H` windows of a row `C` beginning in
`J`.  If `M=O(xA/L_0)` such arcs cover all but `o(A)` holes and their
underlying rows are distinct, promoting the arcs to their full rows leaves
the same holes and costs `Mb` occurrences per rank.  Thus

\[
 xb\ll L_0\le b                                      \tag{C.10.9}
\]

makes the promotion cost `o(A)`.  In particular `L_0=ceil(b sqrt x)` needs
only `O(sqrt x B)=o(B)` rows.  Gate B may therefore be closed either by the
positive fractional bound (C.10.7), by the external degree floor (C.10.8),
or by a covering long-flag-arc theorem; none is currently proved for the
actual stopped residual.

## Appendix C.11: Shallow external regularity and the survivor-catalogue no-go

Continue with \(b=2r+1\), \(A={b\choose r}\), \(B=A/b\), and \(L={b\choose r-1}\) from C.9. Put `k_q=r-q`, `B_q=binom(b,k_q)`, and, for a tagged lower `k_q`-set `T`
or complementary upper target, let `Omega_q(T)` be the directed punctured
configurations whose full cyclic row contains `T`.  A proper target has one
start in a fixed row, so

\[
 D_q=|\Omega_q(T)|=b\,k_q!(b-k_q)!={b\,b!\over B_q}.           \tag{C.11.1}
\]

Independently retain lower and middle targets with probabilities `x` and
`y>=x`.  If `C` is the surviving labelled catalogue, set
`Z=|C|`, `X_(q,T)=|C cap Omega_q(T)|`, and
`rho=x^(2r)y^(2r)`.  Exact counting gives

\[
 \mathbb EZ=b!\rho,\quad \mu_q:=\mathbb EX_{q,T}=D_q\rho,\quad
 {\mathbb EZ\over\mu_q}={B_q\over b},\quad
 \sum_TX_{q,T}=bZ.                                      \tag{C.11.2}
\]

### Mixed external-root codegree lemma

Fix \(F=E(w)\), and suppose that \(T=I_{k_q}^w(s)\) is a full cyclic
window of the row \(w\).
Put a cut between consecutive positions of \(w\), and multiply cut labels
by \(-2\) modulo \(b\).  The boundary pairs of the \(r\)- and
\((r-1)\)-targets of \(F\) become the edges of a subgraph

\[
 \mathcal B_F\subseteq
 \operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})             \tag{C.11.3a}
\]

obtained by deleting two edges.  The boundary pair \(R_q\) of \(T\) has
cyclic length \(2q+1\).  For
\(\varnothing\ne S\subseteq F\), let \(\partial S\) be the set of
boundary edges representing its tagged targets, and define

\[
 v_q(S)=|V(R_q\cup\partial S)|,                             \tag{C.11.3b}
\]

\[
 d_q(T,S)=|\{u\in\mathfrak S_b:T\text{ is a full window of }u,
                    \ S\subseteq E(u)\}|,                  \tag{C.11.3c}
\]

where \(\mathfrak S_b\) is the set of permutations of the \(b\) ground
labels and \(E(u)\) is the punctured configuration defined by the row
\(u\).

There is an absolute constant \(C\) such that, uniformly for

\[
 2\le q\le\sqrt r/4,
\]

\[
 \boxed{\frac{d_q(T,S)}{D_q}
       \le C^{|S|}r^{\,2-v_q(S)}.}                         \tag{C.11.3}
\]

The same statement holds for the complementary upper target.

#### Proof

Anchor the start of \(T\).  Its two root cells have sizes

\[
                         r-q,\qquad r+1+q.                 \tag{C.11.3d}
\]

Fix the labelled Venn signature of \(T\cup S\).  If
\(n_\sigma\) are its cell sizes and \(V=\prod_\sigma n_\sigma!\), then
\(V\) is the number of label assignments for any one compatible positional
tuple.  Let \(P_q(S)\) be the number of relative positional tuples with
the anchored start and this signature.  It is enough to prove

\[
 P_q(S)V\le
 C^{|S|}(r-q)!(r+1+q)!r^{\,2-v_q(S)}.                     \tag{C.11.3e}
\]

Indeed, there are \(b\) choices for the start of \(T\), so the left side
times \(b\) bounds \(d_q(T,S)\), whereas
\(D_q=b(r-q)!(r+1+q)!\).  The puncture can only reduce the count.

We now prove (C.11.3e), including the positional multiplicity.  Order
\(S=\{S_1,\ldots,S_t\}\).  The exposure tree at level \(i\) has one node
for every relative start tuple of
\(T,S_1,\ldots,S_i\) having the prescribed labelled Venn signature; the
start of \(T\) is fixed.  A node \(\eta\) is weighted by the product
\(V_i(\eta)\) of the factorials of its current Venn cells.  Thus the sum
of the terminal node weights is exactly \(P_q(S)V\).

At any node list the positive elementary cut gaps as
\(g_1,\ldots,g_v\), and put \(G=\prod_hg_h!\).  They satisfy

\[
                  \sum_hg_h=b,\qquad g_h\le r+1+q.         \tag{C.11.3f}
\]

If an old Venn cell \(C\) is the disjoint union of elementary gaps
\(H\), and a child interval takes \(p_H\) labels from gap \(H\), with
\(p_C=\sum_{H\subset C}p_H\), then

\[
 \prod_{H\subset C}\binom{|H|}{p_H}\le\binom{|C|}{p_C},
 \qquad
 \sum_{\sum p_H=p_C}\prod_H\binom{|H|}{p_H}
       =\binom{|C|}{p_C}.                                  \tag{C.11.4}
\]

The first map sends independently chosen gap subsets to their disjoint
union in \(C\); intersection with the old gaps recovers them.  Summing
over allocations gives the second identity.  Consequently all branches
whose two new cuts lie in distinct old gaps are paid for by the Venn-cell
refinement and do not increase the ratio of total node weight to the gap
factorial product.

If both new cuts lie in one ordinary gap of size \(g\), write its three
pieces as \(u,m,v\).  The middle piece or its complement has size in
\(\{r-1,r,r+1,r+2\}\).  Since an ordinary gap has size at most \(r+2\),
one has \(u+v\le3\), so the information lost when the two outside pieces
are merged costs at most

\[
                         \binom{u+v}{u}\le8.                \tag{C.11.4a}
\]

The only additional case is a gap descended from one of the two root
cells and still having size \(g\ge r-1\).  Put
\(d=u+v=g-m\le q+2\).  There are at most \(d+1\) positional splits, the
Venn merge loses at most \(\binom du\), and the exact change of the gap
factorial is

\[
 \frac{u!m!v!}{g!}
 =\frac1{\binom gd\binom du}.                              \tag{C.11.5a}
\]

Thus the total, over every split of this type, is charged by

\[
 \frac{d+1}{\binom gd}\le
 \begin{cases}
  1,&d=0,\\
  4/r,&d=1,\\
  16/r^2,&2\le d\le q+2.
 \end{cases}                                               \tag{C.11.5}
\]

For the last line, the ratio of the expression at \(d+1\) to that at
\(d\) is \((d+2)/(g-d)\le1\), since
\(q+2\le\sqrt r/2\) for large \(r\); hence its maximum occurs at
\(d=2\), and \(3/\binom g2\le16/r^2\).  Enlarging the absolute constant
handles the finitely many smaller \(r\).

At the first exposure level, (C.11.5a)--(C.11.5) sum every possible
root-relative placement.  At later levels retain \(S_1\) as a positional
anchor.  A cyclic interval of either central length and prescribed
intersection with \(S_1\) has at most four starts: disjointness gives at
most \(b-k-h+1\le4\), a proper overlap gives two, and containment gives
at most \(|k-h|+1\le2\).  Therefore (C.11.4), with one absolute factor
per exposed interval, sums all children rather than following one branch.
Coincident old cuts cost no power of \(r\); one genuinely new reference
cut costs \(O(1/r)\), and two cost \(O(1/r^2)\), by
(C.11.4)--(C.11.5).  This remains true if another positional child
makes a reference cut coincident, because that child is already one of the
splits summed in (C.11.5).

For completeness, the terminal factorial envelope used in this induction
is

\[
 \frac{G}{(r-q)!(r+1+q)!}
 \le C^v r^{\,2-v}.                                      \tag{C.11.6}
\]

To prove it, factorial log-convexity moves mass from smaller positive gaps
to larger nonsaturated gaps.  If \(v\le r-q+1\), the maximizing product is
at most
\((r+1+q)!(r-q-v+2)!\), and division by the root product leaves
\(1/(r-q)_{v-2}\le(e/r)^{v-2}\), after changing the constant because
\(q\le\sqrt r/4\).  If \(v>r-q+1\), the transfers leave at most one gap
of size \(b-v+1\) and all other gaps of size one, which is smaller still.
The elementary inequality used here is
\((n)_a=a!\binom na\ge(n/e)^a\): compare ordered samples with samples
allowing repetition to obtain \(\binom na\ge(n/a)^a\), and integrate
\(\log x\) to obtain \(a!\ge(a/e)^a\).

Let \(v_i^*\) be the number of reference cuts of
\(T,S_1,\ldots,S_i\).  The preceding child calculation and
(C.11.6) give, by induction over the exposure tree, the following
bound.  Since \(v_i^*\le2i+2\), its factor \(C^{v_i^*}\) is absorbed by
enlarging the absolute base \(C\):

\[
 \sum_{\eta\text{ at level }i}V_i(\eta)
 \le C^i(r-q)!(r+1+q)!r^{\,2-v_i^*}.                      \tag{C.11.6a}
\]

At level zero this is equality.  The three child cases above prove the
induction step and exhaust all possibilities because an interval has two
boundary cuts.  At level \(t\), \(v_t^*=v_q(S)\), so
(C.11.6a) is (C.11.3e).  This proves (C.11.3).  Complementation keeps
the same boundary pair and proves the upper-target version. \(\square\)

### Two-root polymer lemma

For a sufficiently small absolute \(c_{\rm pol}>0\), uniformly in the
preceding range and for \(0\le z\le c_{\rm pol}\sqrt r\),

\[
 \boxed{
 \sum_{\varnothing\ne S\subseteq F}
 z^{|S|}r^{\,2-v_q(S)}
 =O\!\left(\frac z r+\frac{z^3}r+\frac{z^4}{r^2}\right).}  \tag{C.11.7}
\]

#### Proof

The graph \(\mathcal B_F\) has maximum degree four, is triangle-free for
all sufficiently large \(r\), and every \(m\)-edge subgraph with \(v\)
nonisolated vertices satisfies

\[
                              m\le2(v-1).                   \tag{C.11.7a}
\]

Indeed the full circulant is the union of its step-one and step-three
two-factors.  Every proper nonempty vertex set has at least two step-one
cut edges.  It either cuts a step-three cycle, giving two more, or is a
union of whole step-three cycles; in the latter case its step-one cut is
at least four.  Thus an induced proper subgraph has at most \(2v-2\)
edges.  On all \(b\) vertices, deleting the two punctured edges leaves
\(2b-2\) edges.  This proves (C.11.7a).  Triangle-freeness follows because
three signed steps from \(\{1,3\}\) have odd integer sum of absolute value
at most nine and cannot vanish modulo \(b\ge11\).

Adjoin the fixed chord \(R_q\).  It creates no triangle: a sum of two
signed elements of \(\{1,3\}\) belongs to
\(\{0,\pm2,\pm4,\pm6\}\), whereas the chord length is \(5\) for \(q=2\)
and at least \(7\) for \(q\ge3\), with no modular wrap in the stated
range.

Decompose \(S\) into its connected components in \(\mathcal B_F\).
A maximum-degree-four exploration from a prescribed vertex has at most
\(A_0^m\) connected \(m\)-edge shapes.  Components meeting neither chord
endpoint have total connected activity

\[
 \eta_0=O(z/r+z^4/r^2).                                   \tag{C.11.7b}
\]

The one-, two-, and three-edge cases use respectively at least two, three,
and four vertices; (C.11.7a) gives a geometric tail from four edges on.
A connected component meeting a prescribed chord endpoint has rooted
activity

\[
 O(z/r+z^2/r^2+z^3/r+z^4/r^2).                            \tag{C.11.7c}
\]

The first two terms again use triangle-freeness, while
(C.11.7a) and the bounded-choice exploration give the last two geometric
tails.  The same estimate covers a component meeting both endpoints; the
chord itself supplies the second fixed root, and the smallest such
component has three edges.  There are only two chord endpoints.

Dropping disjointness among all other components only enlarges the sum and
multiplies a rooted contribution by at most \(e^{\eta_0}\).  If no
component meets a chord endpoint, subtract the empty family.  Combining
these alternatives, absorbing \(z^2/r^2\) into \(z/r\), and taking
\(c_{\rm pol}\) small enough proves (C.11.7). \(\square\)

### Application: product external-degree variance

Let \(I_G\) indicate survival of a catalogue row \(G\in\Omega_q(T)\), so
\(X_{q,T}=\sum_GI_G\) and \(\mathbb EI_G=\rho\).  For distinct rows
\(F,G\), the quotient of their joint survival probability by
\(\rho^2\) is at most \(x^{-|F\cap G|}\).  With
\(a=x^{-1}-1\), expand

\[
 x^{-|F\cap G|}-1
 =\sum_{\varnothing\ne S\subseteq F\cap G}a^{|S|}.
                                                                    \tag{C.11.8a}
\]

Separate the diagonal variance, sum first over \(G\), and apply
the mixed external-root codegree lemma to each \(S\subseteq F\).
Maximizing over the anchored
row \(F\) gives

\[
 \frac{\operatorname {Var}X_{q,T}}{\mu_q^2}
 \le\frac1{\mu_q}+
 \sum_{\varnothing\ne S\subseteq F}
       (Ca)^{|S|}r^{\,2-v_q(S)}.                          \tag{C.11.8b}
\]

If \(x\ge r^{-\alpha}\) with \(\alpha<1/3\), then
\(Ca=o(\sqrt r)\).  The two-root polymer lemma and
\(a\le x^{-1}\) yield

\[
 \frac{\operatorname {Var}X_{q,T}}{\mu_q^2}
 \le\frac1{\mu_q}+O\!\left(
       \frac1{rx}+\frac1{rx^3}+\frac1{r^2x^4}\right)
 \le\frac1{\mu_q}+O\!\left(\frac1{rx^3}\right)=o(1).     \tag{C.11.8}
\]

The mean is exponential uniformly in this range:
\(D_q=\exp((2+o(1))r\log r)\), while
\(\rho\ge x^{4r}\), so
\(\mu_q\ge\exp((2-4\alpha+o(1))r\log r)\).  Hence the right side is
\(o(1)\).

If instead each shore is a uniform subset of its prescribed size, every
union of two configurations has at most `4r` variables per shore and
`(m)_u/(N)_u=(m/N)^u exp(O(u^2/m)+O(u^2/N))`.  Since the shore sizes are
exponential, the normalized variance in (C.11.8) changes by only
`e^-Omega(r)`.  Exact shore sizes therefore do not create positive external
bias.

This implies the promised no-go.  Assume `x=o(1)`, `x>=r^-alpha` for one fixed `alpha<1/6`, put
`Q=floor(sqrt(rx)/4)`, and let possibly residual-dependent tagged hole sets
satisfy

\[
 \sum_{q=2}^Q(|\mathcal H_q^-|+|\mathcal H_q^+|)\ge c_0xAQ.  \tag{C.11.9}
\]

With high probability there are no `D_0>0` and exceptional `o(A)` targets
for which all remaining holes have `X_(q,T)>=D_0` and

\[
                              {Z\over D_0}=O(xB).               \tag{C.11.10}
\]

To prove it, the product-law unrooted concentration (C.3bis.11) with \(s=1\) first gives
\(Z\ge\mathbb EZ/4\) with high probability.  Since
`B_q/L>=1-(q-1)(q+2)/r>=1-x/8`, (C.11.10) would make every
nonexceptional hole satisfy `X_(q,T)>=c mu_q/x`.  Chebyshev and (C.11.8)
show that a fixed target has this enrichment with probability
`O(1/(rx))`.  Among at most `2QA` tagged targets the expected enriched
count is `O(QA/(rx))`; because `rx^2->infinity`, Markov makes this
`o(xAQ)`.  Also `xQ->infinity`, so an `o(A)` exception removes only
`o(xAQ)` holes, contradicting (C.11.9).

Finally, ordinary external regularity is incompatible even with the actual
stopped descent.  At a good round `j`, let `Z_j` be the current catalogue,
`M_j` its middle shore, and mark with
`p_j=gamma|M_j|/(2r^2Z_j)`.  If for one depth `q`, throughout every good
trajectory,

\[
 X_{q,j}(T)\le K_E{bZ_j\over B_q},\quad B_q\ge c_BA,\quad
 p_j\le\tfrac12,\quad \sum_{j<\tau}{|M_j|\over A}\le C_0r,  \tag{C.11.11}
\]

then each tagged `T` has a constant probability of either seeing a declared
failure or remaining a full-bank hole at the threshold.  Indeed

\[
 \sum_{j<\tau}p_jX_{q,j}(T)\le{\gamma K_EC_0b\over2c_Br}=O(1). \tag{C.11.12}
\]

Conditionally, no member of the external star is marked with probability
`(1-p_j)^(X_(q,j)(T))>=exp(-2p_jX_(q,j)(T))`.  Formally, if `A_j` is the
event of no earlier external mark and
`Lambda_j=sum_(i<j)p_iX_(q,i)(T)`, then
`1_(A_j)exp(2Lambda_j)` stopped at `tau` is a nonnegative submartingale.
Equation (C.11.12) therefore gives `Pr(A_tau)>=exp(-O(1))` without
conditioning on future cap persistence.
On that event either failure occurs or no accepted row covers `T`.  Hence,
if failures are `o(1)`, an all-target cap (C.11.11) forces
`mathbb E(h_q^++h_q^-)=Omega(A)`, far above `O(xA)`.  The exact positive Gate-B
input is therefore a history-induced alignment of `Omega(xAQ)` holes with
an external high-degree tail of factor `1/x`, a hole-biased subcatalogue,
or the separate constant-density long-flag-arc tail.

## Appendix C.12: Signed sixth-moment collision forcing

This section is only a product/uniform-slice theorem; it does not assert a
stopped comparison. Retain the two shores with
\(p_M=y\ge p_L=x\ge r^{-\alpha}\), and put
\[
q_0=x^{2r}y^{2r},\qquad
\mu_\sigma={d_\sigma q_0\over p_\sigma},\qquad
d_M=D_M,\quad d_L=D_L.                                    \tag{C.12.1}
\]
Fix an original row \(G\), a shore-\(\sigma\) target \(v\notin G\), and
condition on retaining \(G\cup\{v\}\). Define
\[
A_{G,v}=|\{F\ni v:F\cap G\ne\varnothing,\ F\text{ survives}\}|, \tag{C.12.2}
\]
\[
K_c(G,v)={1\over d_\sigma}
\sum_{\substack{F\ni v\\F\cap G\ne\varnothing}}
\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}.          \tag{C.12.3}
\]
Then \(\mathbb EA_{G,v}=\mu_\sigma K_1(G,v)\). For every fixed \(c\)
with \(c\alpha<1/3\),
\[
\boxed{\sum_{v\notin G}K_c(G,v)=O_c(r^2x^{-c}).}             \tag{C.12.4}
\]
Indeed, with \(a_c=x^{-c}-1\), expand
\[
W_c(G)=\sum_{F:F\cap G\ne\varnothing}
\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-c}.
\]
Singleton subsets cost \(O(D_Mrx^{-c})\); C.7 and C.1 bound all larger
subsets by \(O_c(D_M(a_c^2+a_c^4))\). Since
\(a_c^4=O(rx^{-c})\), \(W_c(G)=O_c(D_Mrx^{-c})\). Interchanging \(v,F\),
using \(2r\) shore targets per row and \(d_\sigma\ge D_M\), proves
(C.12.4).

C.8 also gives the time-zero external-star cap
\[
\max_{G\not\ni v}|\{F\ni v:F\cap G\ne\varnothing\}|
\le {32D_M\over r}.                                      \tag{C.12.4a}
\]
Only disjoint-middle and lower-in-middle containment pairs have codegree
above \(6D_M/r^2\); each has codegree at most \(2D_M/r\), and \(v\) has at
most four such partners in \(G\). Cauchy and (C.12.4) therefore give
\[
K_1(G,v)^2\le {32\over r}K_2(G,v),\qquad
\sum_vK_1(G,v)^2=O(rx^{-2}).                              \tag{C.12.6}
\]
For distinct \(F,H\ni v\), their conditional joint-survival monomial is
\[
w_\sigma^2s_Fs_H
\prod_{u\in(F\cap H)-(G\cup\{v\})}p_{\operatorname{sh}(u)}^{-1},
\quad w_\sigma={\mu_\sigma\over d_\sigma},\quad
s_F=\prod_{u\in F\cap G}p_{\operatorname{sh}(u)}^{-1}.
\]
The constant part sums with (C.12.6). For the remainder use
\(s_Fs_H\le(s_F^2+s_H^2)/2\) and C.3bis.6 with \(c=1\), obtaining
\[
\boxed{\sum_{v\notin G}\mathbb E[(A_{G,v})_2\mid G,v]
=O(\mu_\sigma^2rx^{-5}).}                                \tag{C.12.5}
\]

For \(f_z(d)=(d-z)^6\), define
\[
\mathfrak d_z(d,a)=a\nabla f_z(d)-[f_z(d)-f_z(d-a)].        \tag{C.12.7}
\]
Falling-factorial expansion and telescoping give
\[
\mathfrak d_z(d,a)=\sum_{\ell=1}^6c_\ell(z)
\{\ell a(d-1)_{\ell-1}-[(d)_\ell-(d-a)_\ell]\}
=\sum_{h=0}^{a-2}(a-1-h)\nabla^2f_z(d-h).                  \tag{C.12.8}
\]
Since \(f_z\) is convex and
\(\nabla^2f_z(d)=30t^4-120t^3+210t^2-180t+62\), \(t=d-z\),
\[
\boxed{0\le\mathfrak d_z(d,a)
\le C(a)_2(1+|d-z|^4+a^4).}                               \tag{C.12.9}
\]
For a residual \(H\), set
\[
a_G(v)=|\{F\in E(H):v\in F,\ F\cap G\ne\varnothing\}|,
\quad
\mathfrak D_{z,\sigma}(H)=
\sum_v\sum_{G\not\ni v}\mathfrak d_z(d_H(v),a_G(v)).       \tag{C.12.10}
\]
It is nonnegative. The first expression in (C.12.8), after interchanging
\(G\) and ordered tuples through \(v\), is exactly the signed recombination
of the five factorial collision defects in the first-order evolution of
the centered sixth degree mass.

If \(\alpha<1/18\), uniformly in \(G\),
\[
\boxed{\sum_{v\notin G}\mathbb E[
(A_{G,v})_2\{1+|X_v-\mu_\sigma|^4+A_{G,v}^4\}\mid G,v]
=O(\mu_\sigma^6r^{-1}x^{-33}).}                           \tag{C.12.11}
\]
Here \(X_v\) is the full residual degree under the conditioning above.
Here is the full carrier estimate. Put
\[
\theta={32\over r},\qquad \lambda=\theta+Q_3=O(r^{-1}x^{-9}). \tag{C.12.12}
\]
For an ordered pair meeting \(G\) and four further distinct centered
carriers, their absolute conditional contribution is at most
\[
Cw_\sigma^6\prod_{i\in R}s_i\,
x^{-\sum_{i<j}|(F_i\cap F_j)-(G\cup\{v\})|}.               \tag{C.12.13}
\]
Join carriers with positive displayed overlap. A centered singleton
component vanishes, hence at most two components avoid \(R\). A
maximum-weight tree in every other component carries at least one third of
its overlap weight and sums with \(Q_3\). Since
\(\prod_{i\in R}s_i\le |R|^{-1}\sum_{j\in R}s_j^{|R|}\), at least three
\(\theta\)- or \(Q_3\)-costs remain. Thus (C.12.4) gives
\[
C\mu_\sigma^6\lambda^3\sum_{h=2}^6\sum_vK_h(G,v)
=O(\mu_\sigma^6r^{-1}x^{-33}).                            \tag{C.12.14}
\]
Repeated Bernoulli labels reduce affinely to fewer centered labels; a term
with at most five distinct carriers is
\(O_m(\mu_\sigma^m r^2x^{-m})\), exponentially smaller because
\(\mu_\sigma\) is exponential. Finally,
\[
(A)_2A^4=16(A)_2+65(A)_3+55(A)_4+14(A)_5+(A)_6.           \tag{C.12.15}
\]
The all-\(j\)-carriers-meet-\(G\) sum is at most
\(C_j\mu_\sigma^j\lambda^{j-1}\sum_vK_j\). At \(j=6\) this is
\(O(\mu_\sigma^6r^{-3}x^{-51})\), absorbed because
\(r^{-2}x^{-18}=o(1)\); lower orders are smaller. This proves (C.12.11).

For the provisional product residual \(H^*\), put \(Z^*=|E(H^*)|\). Then
\[
\boxed{\mathbb E\mathfrak D_{\mu_\sigma,\sigma}(H^*)
=O((\mathbb EZ^*)p_\sigma\mu_\sigma^6r^{-1}x^{-33}).}      \tag{C.12.16}
\]
This follows by summing (C.12.11) over \(G\), multiplying by \(q_0p_\sigma\),
and using (C.12.9). C.3ter transfers it to every uniform exact two-shore
slice, with that slice's exact mean: each term queries at most seven rows;
the positive carrier envelope is \(O(\mu_\sigma^6rx^{-15})\), so the
exponentially small slice/product error remains negligible.

At paired densities, \(\pi_0=\gamma/(r\mu_M)\); if \(N_\sigma\) is the
full shore population, then
\((N_\sigma p_\sigma)\mu_\sigma=2r\mathbb EZ^*\), so
\[
{\pi_0\mathbb E\mathfrak D_{\mu_\sigma,\sigma}(H^*)
\over(N_\sigma p_\sigma)\mu_\sigma^6}=O(r^{-3}x^{-32}).    \tag{C.12.17}
\]
On \(x_{j+1}=x_j(1-\Theta(1/r))\), \(x_J\ge r^{-\alpha}\),
\[
\sum_{j<J}O(r^{-3}x_j^{-32})=O(r^{-2}x_J^{-32})=o(1).     \tag{C.12.18}
\]

For every \(z,z'\),
\[
\boxed{\mathfrak D_{z',\sigma}(H)\le
C\mathfrak D_{z,\sigma}(H)+C|z'-z|^4\mathcal Q_{2,\sigma}(H),} \tag{C.12.19}
\]
where \(\mathcal Q_{2,\sigma}=\sum_v\sum_{G\not\ni v}(a_G(v))_2\).
Indeed \(P(t)=t^6-2(t-1)^6+(t-2)^6=30\mathbb E(t-U-V)^4\), so
\(P(t-u)\le C(P(t)+|u|^4)\); apply this in (C.12.8).
With \(\eta=r^{-1/8}\) and \(\bar d_\sigma=2rZ/n_\sigma\), C.3bis.11
and C.3t.10 give, over
\(O(r\log r)\) checkpoints,
\[
\Pr(\exists j,\sigma:|\bar d_{\sigma,j}/\mu_{\sigma,j}-1|>\eta)
=O(r^{-2+6/8+3\alpha}\log r)+e^{-\Omega(r)}=o(1).          \tag{C.12.20}
\]
Product shore sizes add only an exponential tail; slice sizes are fixed.
Summing (C.12.5) over \(G\) gives
\[
\mathbb E\mathcal Q_{2,\sigma}(H^*)
=O((\mathbb EZ^*)p_\sigma\mu_\sigma^2rx^{-5}).             \tag{C.12.20a}
\]
Thus the cumulative center-shift contribution is
\[
O(\eta^4x_J^{-4})=O(r^{-1/2+4\alpha})=o(1).                \tag{C.12.21}
\]
Therefore the pre-purge product and exact-slice forcing is summable for
\(\alpha<1/18\). No adaptive stopped conclusion is asserted.

## Appendix C.12a: Deterministic post-purge stability

Let \(H\) be finite, simple, shore-uniform, every edge using \(k_\sigma\)
vertices of shore \(\sigma\), and put
\[
q=\sum_\sigma k_\sigma,\quad Z=|E(H)|,\quad
n_\sigma=|V_\sigma|,\quad z_\sigma={k_\sigma Z\over n_\sigma}. \tag{C.12a.1}
\]
Use \(a_G^H,\mathfrak d_z,\mathfrak D_{z,\sigma}\) above and set
\[
Q_{2,v}(H)=\sum_{G\not\ni v}(a_G^H(v))_2.                  \tag{C.12a.3}
\]
If \(d'=d-\ell\), \(0\le a'\le d'\), \(a'\le a\le d\), then for every
\(\varepsilon>0\),
\[
\boxed{\mathfrak d_{z'}(d',a')\le(1+\varepsilon)^3\mathfrak d_z(d,a)
+15(1+\varepsilon^{-1})^3(a')_2|\ell-(z-z')|^4.}          \tag{C.12a.4}
\]
This follows from (C.12.8),
\[
\mathfrak d_z(d,a)=\sum_{h=0}^{a-2}(a-1-h)P(d-z-h),\quad
P(t)=30\mathbb E(t-U-V)^4,                               \tag{C.12a.5}
\]
and \(|X-Y|^4\le(1+\varepsilon)^3|X|^4+
(1+\varepsilon^{-1})^3|Y|^4\); the new weights sum to \((a')_2/2\).

If \(H'\) is vertex-induced and
\(\ell_v=d_H(v)-d_{H'}(v)\), then \(a_G^{H'}(v)\le a_G^H(v)\), so
\[
\boxed{\mathfrak D_{z',\sigma}(H')\le
(1+\varepsilon)^3\mathfrak D_{z,\sigma}(H)
+15(1+\varepsilon^{-1})^3\sum_{v\in V_\sigma(H')}
Q_{2,v}(H')|\ell_v-(z-z')|^4.}                           \tag{C.12a.8}
\]
Also
\[
Q_{2,v}(H')\le d_{H'}(v)\sum_{\substack{F\in E(H')\\v\in F}}
\sum_{u\in F-\{v\}}d_{H'}(u).                             \tag{C.12a.9}
\]

Fix \(K_0>1\), purge
\[
B_\sigma=\{v:d_H(v)>K_0z_\sigma\},\quad
H^\circ=H[V(H)-\bigcup_\sigma B_\sigma],\quad
Z^\circ=|E(H^\circ)|,                                    \tag{C.12a.10}
\]
and set
\[
L_\sigma=\sum_{v\in B_\sigma}d_H(v),\quad
\beta={\sum_\sigma L_\sigma\over Z},\quad
\rho={Z-Z^\circ\over Z}.                                  \tag{C.12a.11}
\]
Assume \(0\le\rho\le\rho_0<1\) and
\(\max_\tau z_\tau/\min_\tau z_\tau\le R_0\). Then
\[
\rho\le\beta\le q\rho,\qquad L_\sigma\le k_\sigma(Z-Z^\circ), \tag{C.12a.14}
\]
because each removed edge contains between one and \(q\) bad vertices and
at most \(k_\sigma\) on shore \(\sigma\).
\[
\tau_\sigma:={|B_\sigma|\over n_\sigma}\le{\rho\over K_0},
\qquad {z_\sigma^\circ\over z_\sigma}={1-\rho\over1-\tau_\sigma}, \tag{C.12a.16}
\]
\[
z_\sigma^\circ\ge(1-\rho)z_\sigma,\quad
n_\sigma^\circ\ge(1-\rho/K_0)n_\sigma,\quad
0\le z_\sigma-z_\sigma^\circ\le
{\rho z_\sigma\over1-\rho_0/K_0}.                         \tag{C.12a.17}
\]
For surviving \(v\), \(d_H(v),\ell_v\le K_0z_\sigma\) and
\(\sum_v\ell_v\le\rho n_\sigma z_\sigma\). Hence
\[
\sum_v|\ell_v-(z_\sigma-z_\sigma^\circ)|^4
\le C_{K_0,\rho_0}\rho n_\sigma z_\sigma^4,               \tag{C.12a.18}
\]
\[
Q_{2,v}(H^\circ)\le(q-1)K_0^3R_0z_\sigma^3.               \tag{C.12a.19}
\]
The first bound uses
\(\sum\ell_v^4\le(K_0z_\sigma)^3\sum\ell_v\) and the center bound;
the second is (C.12a.9) with the post-purge cap and the shore ratio.
Substitution in (C.12a.8) proves
\[
\boxed{\mathfrak D_{z_\sigma^\circ,\sigma}(H^\circ)\le
(1+\varepsilon)^3\mathfrak D_{z_\sigma,\sigma}(H)
+C_{\varepsilon,K_0,\rho_0,R_0}q\rho n_\sigma z_\sigma^7.} \tag{C.12a.20}
\]
Equivalently, its additive term is \(Cqk_\sigma\rho Zz_\sigma^6\).

For the punctured hypergraph \(k_M=k_L=2r\), \(q=4r\). If
\(\pi\le C_\pi/(rz_M^\circ)\), the paired shore ratio is bounded, and
(C.12a.20) normalizes to
\[
\boxed{{\pi\mathfrak D_{z_\sigma^\circ,\sigma}(H^\circ)
\over n_\sigma^\circ(z_\sigma^\circ)^6}\le
C{\pi\mathfrak D_{z_\sigma,\sigma}(H)\over n_\sigma z_\sigma^6}+C\rho.}
                                                                    \tag{C.12a.22}
\]
For provisional \(H_j^*\), purged \(H_j^\circ\), and active events
\(\mathcal G_j\) on which the displayed rate and ratio hypotheses hold,
the exact two remaining stopped inputs are
\[
\boxed{\sum_{j,\sigma}\mathbb E\!\left[
\mathbf1_{\mathcal G_j}{\pi_j\mathfrak D_{z_{j,\sigma}^*,\sigma}(H_j^*)
\over n_{j,\sigma}^*(z_{j,\sigma}^*)^6}\right]=o(1),}      \tag{C.12a.24}
\]
\[
\boxed{\sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]=o(1).} \tag{C.12a.25}
\]
Then (C.12a.22) gives the post-purge \(o(1)\) sum on
\(\mathcal G_j\cap\{\rho_j\le\rho_0\}\), and
\[
\Pr(\exists j:\mathcal G_j,\rho_j>\rho_0)
\le\rho_0^{-1}\sum_j\mathbb E[\mathbf1_{\mathcal G_j}\rho_j]=o(1). \tag{C.12a.26}
\]
If \(K>K_0\) and \(\rho_0\le1-K_0/K\), the post-purge cap is at most \(K\).
Since \(\rho_j\le\beta_j\), stopped summability of \(\beta_j\) is sufficient
but stronger.

At a product or exact-slice checkpoint, the fixed sixth moments, with
(C.12.20) replacing \(\mu_\sigma\) by the realized average, give
\[
\mathbb E\beta_j=O(r^{-2}x_j^{-9}),\qquad
\mathbb E{\pi_j\mathfrak D_j\over n_jz_j^6}
=O(r^{-3}x_j^{-32}).                                    \tag{C.12a.27}
\]
For the first estimate use
\(u\mathbf1_{\{u>K_0\}}\le C_{K_0}(u-1)^6\), sum the fixed-target sixth
moment over both shores, and use total incidence \(2rZ\). Along a geometric
schedule the sums are \(O(r^{-1}x_J^{-9})\) and
\(O(r^{-2}x_J^{-32})\). Thus a common stopped comparison loss
\(r^{\kappa+o(1)}\) suffices if
\[
\boxed{\kappa<\min\{1-9\alpha,\ 2-32\alpha\}.}             \tag{C.12a.28}
\]
No such stopped comparison is proved. There is no third post-purge
statistic: this branch is exactly (C.12a.24) plus (C.12a.25).

## Appendix C.13: Stopped external hits and relative protection

Let \(\mathcal C_j\) be the residual labelled configuration catalogue before
round \(j\), \(Z_j=|\mathcal C_j|\), and \(G_j\) its conflict graph.
Conditionally on \(\mathcal F_j\), mark each configuration with probability
\(p_j\), accept the isolated marks \(\mathcal A_j\), and delete their closed
conflict neighbourhoods.  All stopping times below are bounded by the deterministic round cap. Fix a positive terminal density scale \(x\), put \(Q=\lfloor\sqrt{rx}/4\rfloor\), and use this \(Q\) for the aggregate shallow-depth statements.

Fix a tagged shallow depth \(q\), put

\[
 b=2r+1,\quad A={b\choose r},\quad B=A/b,\quad
 k_q=r-q,\quad B_q={b\choose{k_q}},
\]

and use restored full rows.  For a target \(T\), define

\[
 \mathcal S_j(T)=\{F\in\mathcal C_j:T\hbox{ is a full-row window of }F\},
 \qquad X_j(T)=|\mathcal S_j(T)|.                  \tag{C.13.1}
\]

Every configuration has \(b\) such windows, so

\[
 \sum_TX_j(T)=bZ_j.                                \tag{C.13.2}
\]

Initially

\[
 Z_0=b!,\qquad X_0(T)=D_q=b\,k_q!(b-k_q)!,
 \qquad {X_0(T)\over Z_0}={b\over B_q}.            \tag{C.13.3}
\]

Let \(U_j(T)\) indicate that no earlier accepted full row contains \(T\), and put \(h_q(n)=\sum_TU_n(T)\) over the shore-tagged depth-\(q\) layer (rank \(r-q\) or \(r+1+q\)).
Thus \(U_\tau(T)=1\) precisely for a restored terminal hole.  Returning to
the punctured convention changes at most one occurrence per accepted row
and depth, hence \(O(QB)=o(A)\) aggregate targets when \(Q=o(b)\).

For one round put

\[
 K_j(T)=|\mathcal A_j\cap\mathcal S_j(T)|,\qquad
 a_j(T)=\Pr(K_j(T)>0\mid\mathcal F_j),\qquad
 u_j(T)=p_jX_j(T).                                 \tag{C.13.4}
\]

If \(p_j\le1/2\) and \(p_j\Delta(G_j)\le\beta\), then

\[
 \boxed{e^{-4\beta}{u_j(T)\over1+u_j(T)}
 \le a_j(T)\le\min\{1,u_j(T)\}.}                  \tag{C.13.5}
\]

Indeed, if \(I_F\) indicates that \(F\in\mathcal S_j(T)\) is an isolated
mark, then

\[
 \lambda=\mathbb E(K_j(T)\mid\mathcal F_j)
 =\sum_{F\in\mathcal S_j(T)}p_j(1-p_j)^{\deg_{G_j}(F)}
\]

lies between \(e^{-2\beta}u_j(T)\) and \(u_j(T)\).  Conflicting
configurations cannot both be isolated, while a nonconflicting pair is
simultaneously isolated with probability at most \(p_j^2\).  Hence
\(\mathbb EK_j(T)^2\le\lambda+u_j(T)^2\).  The second-moment inequality
gives the lower bound in (C.13.5), and the union bound gives the upper.

There are two exact stopped likelihoods.  For every fixed \(T\),

\[
 \boxed{U_n(T)+\sum_{j<n}U_j(T)a_j(T)}             \tag{C.13.6}
\]

is a martingale.  If \(p_j<1\) whenever \(Z_j>0\), then so is

\[
 \boxed{U_n(T)\exp\!\left\{\sum_{j<n}-\log(1-a_j(T))\right\}.} \tag{C.13.7}
\]

The condition ensures \(a_j(T)<1\): the event that nothing is marked has
positive probability.  On \(U_j(T)=1\), the next indicator is zero exactly
when \(K_j(T)>0\), which proves (C.13.6); multiplication by
\((1-a_j(T))^{-1}\) proves (C.13.7).  Optional stopping yields

\[
 \Pr\!\left(U_\tau(T)=1,\;
 \sum_{j<\tau}-\log(1-a_j(T))\ge s\right)\le e^{-s},            \tag{C.13.8}
\]

and, after summing (C.13.6) over \(T\),

\[
 \mathbb Eh_q(\tau)
 =B_q-\mathbb E\sum_{j<\tau}\sum_TU_j(T)a_j(T).    \tag{C.13.9}
\]

Thus (C.13.5) applies to targets unhit at the current time; replacing
\(U_j\) by the future event \(U_\tau\) would be invalid conditioning.

There is also an exact no-mark likelihood.  Let \(V_j(T)\) indicate that
no member of any successive external star of \(T\) has yet been marked, and
put

\[
 L_n(T)=\sum_{j<n}-X_j(T)\log(1-p_j).
\]

Then

\[
 \boxed{V_n(T)e^{L_n(T)}}                          \tag{C.13.10}
\]

is a nonnegative martingale: conditional on \(V_j(T)=1\), the next
no-mark probability is exactly \((1-p_j)^{X_j(T)}\).  Consequently

\[
 \Pr(V_\tau(T)=1,\ L_\tau(T)\ge s)\le e^{-s},\qquad
 V_\tau(T)\le U_\tau(T).                           \tag{C.13.11}
\]

In particular a pathwise bound \(L_\tau(T)\le\Lambda\) on all no-mark
paths implies \(\Pr(U_\tau(T)=1)\ge e^{-\Lambda}\).  An average bound
selected only after the final holes are known does not imply this.

Assume now that \(Z_j>0\) through \(\tau\), as on every good stopped
trajectory.  Define

\[
 d_j=1-{Z_{j+1}\over Z_j},\qquad
 d_j(T)=1-{X_{j+1}(T)\over X_j(T)}                 \tag{C.13.12}
\]

when \(X_j(T)>0\).  If a star becomes empty, assign all later protection
values \(-\infty\).  Otherwise put

\[
 \mathscr P_\tau(T)=\sum_{j<\tau}
 \log{1-d_j(T)\over1-d_j},\qquad
 \pi_j(T)={X_j(T)\over bZ_j}.                      \tag{C.13.13}
\]

Equation (C.13.2) makes \(\pi_j\) a probability law.  Direct substitution
and a second use of (C.13.2) give the exact replicator identities

\[
 \boxed{\pi_{j+1}(T)=\pi_j(T){1-d_j(T)\over1-d_j},\qquad
 \sum_T\pi_j(T)(d_j-d_j(T))=0.}                   \tag{C.13.14}
\]

The second equality is linear.  The logarithmic increment instead has
nonpositive Palm mean by Jensen:

\[
 \sum_T\pi_j(T)\log{1-d_j(T)\over1-d_j}\le0.       \tag{C.13.15}
\]

Telescoping (C.13.12)--(C.13.13) and using (C.13.3) proves

\[
 \boxed{{X_\tau(T)\over Z_\tau}
 ={b\over B_q}e^{\mathscr P_\tau(T)}}              \tag{C.13.16}
\]

for every nonempty terminal star.  Give each terminal survivor the common
weight \(KxB/Z_\tau\).  Its total mass is \(KxB\), and it covers \(T\) to
level one exactly when

\[
 \boxed{\mathscr P_\tau(T)\ge
 \log{B_q\over Kx\,bB}=\log{B_q\over KxA}.}        \tag{C.13.17}
\]

For \(q\le\sqrt{rx}/4\), (C.9.8) gives \(B_q/A=1-O(x)\), so the threshold
is \(\log(1/x)-O_K(1)\).

The full-catalogue Gate-B criterion is therefore pathwise:

\[
 \left|\left\{T\in\mathcal H:
 \mathscr P_\tau(T)<\log{B_{\operatorname{depth}(T)}\over KxA}\right\}\right|=o(A),
                                                               \tag{C.13.18}
\]

where \(\mathcal H\) is the restored tagged hole universe and \(\operatorname{depth}(T)\) is the unique \(q\) for which \(T\) belongs to its shore-tagged depth-\(q\) layer.  This is
equivalent to uniform terminal-survivor weight covering every other hole.
Moreover, iteration of (C.13.14) from
\(\pi_0(T)=1/B_q\) gives

\[
 \boxed{\sum_Te^{\mathscr P_\tau(T)}=B_q,\qquad
 |\{T:\mathscr P_\tau(T)\ge s\}|\le B_qe^{-s}.}    \tag{C.13.19}
\]

Empty stars contribute zero.  At the threshold (C.13.17), the upper tail
has size at most \(KxA\).  On the other hand, C.9.5 supplies
\(\Omega(xA)\) holes at every capacity-forcing shallow rank.  Thus a
successful theorem must align essentially the whole capacity-sized
protection tail with the holes; a marginal tail on arbitrary targets is
insufficient.

Finally, the protection has an exact first-blocker form.  In round \(j\),
order \(\mathcal A_j\) deterministically and assign every deleted
configuration to the first accepted configuration whose closed
neighbourhood deletes it.  Let \(\mathcal B_j(G)\) be the resulting cell.
The cells partition \(\mathcal C_j-\mathcal C_{j+1}\), so

\[
 Z_jd_j=\sum_{G\in\mathcal A_j}|\mathcal B_j(G)|,\qquad
 X_j(T)d_j(T)=\sum_{G\in\mathcal A_j}
 |\mathcal B_j(G)\cap\mathcal S_j(T)|.             \tag{C.13.20}
\]

For a terminal hole no accepted \(G\) belongs to \(\mathcal S_j(T)\).
Thus (C.13.18) is exactly the lower-tail assertion obtained by substituting
(C.13.20) into

\[
 \sum_{j<\tau}\log
 {1-\sum_G|\mathcal B_j(G)\cap\mathcal S_j(T)|/X_j(T)
  \over
  1-\sum_G|\mathcal B_j(G)|/Z_j}.                  \tag{C.13.21}
\]

On a good trajectory \(d_j\le1/8\).  Any target satisfying
(C.13.17) necessarily obeys the additive obstruction

\[
 \boxed{\sum_{j<\tau}(d_j-d_j(T))_+
 \ge {7\over8}\left(\log{B_q\over KxA}\right)_+.} \tag{C.13.22}
\]

Indeed, a round with \(d_j(T)\ge d_j\) contributes nonpositively, while
for \(d_j(T)<d_j\le1/8\),

\[
 \log{1-d_j(T)\over1-d_j}
 =\int_{d_j(T)}^{d_j}{du\over1-u}
 \le {8\over7}(d_j-d_j(T)).
\]

Equations (C.13.20)--(C.13.22) isolate the remaining positive theorem:
the actual terminal holes must cumulatively receive logarithmically less
outside-blocker loss than the whole catalogue while simultaneously avoiding
every accepted hit.  None of the identities above proves that alignment.

# Appendix G: Gate A—stopped tail transfer and connected carriers

Let a finite simple hypergraph have shores \(V_\sigma\), every edge meeting
shore \(\sigma\) in \(k_\sigma\) vertices.  Write

\[
 Z=|E|,\qquad n_\sigma=|V_\sigma|,\qquad
 z_\sigma={k_\sigma Z\over n_\sigma},\qquad d(v)=|\{F:v\in F\}|.
\]

For an edge \(F\), put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad C_F=|\Gamma(F)|.
\]

For \(v\notin G\), also put

\[
 a_G(v)=|\{F:v\in F,\ F\cap G\ne\varnothing\}|,\qquad
 E_v={1\over d(v)}\sum_{F\ni v}(C_F-d(v)),\qquad
 \bar C={1\over Z}\sum_FC_F.
\]

Swapping the two finite sums gives
\(\sum_{G\not\ni v}a_G(v)=d(v)E_v\).  In the punctured application
\(k_M=k_L=2r\).  All laws below are stopped before a displayed cap,
shore-comparability condition, or degree floor fails.  No assertion
conditions on a future persistence event.

## G.1 Exact Palm recursion, finite bites, and exact-slice mixtures

The purpose of this section is to connect the stopped target G.2 to the product-reference
objects in G.14, G.15, G.18, and G.19.  It contains no unproved mixing assertion.

Fix a shore `V` in a finite simple hypergraph state `H`, and fix an integer
`m>=2` (Gate A uses `m=12`).  A rooted ordered carrier is

\[
 \gamma=(v;F_1,\ldots,F_m),\qquad
 v\in V,\quad F_i\ne F_j,\quad v\in F_i.
\]

For a residual state `S`, write `d_S(v)` for the root degree and put

\[
 t(S)=\sum_{v\in V}(d_S(v))_m,
 \qquad F_c(S)=\sum_{v\in V}(d_S(v)-c)_+^m,
\]
\[
 \varphi_c(d)=
 \begin{cases}(d-c)_+^m/(d)_m,&d\ge m,\\0,&d<m,
 \end{cases}
 \qquad c\ge m-1.                                      \tag{G.1.1}
\]

For a nonzero finite measure `nu` on residual states with `nu(t)>0`, its
carrier Palm law is

\[
 \widehat\nu(S,\gamma)=
 {\nu(S){\bf1}_{\{\gamma\text{ alive in }S\}}\over\nu(t)}.
\]

Counting the `(d_S(v))_m` ordered carriers at each root gives the exact
identity

\[
 A_c(\nu):={\nu(F_c)\over\nu(t)}
           =\mathbb E_{\widehat\nu}\varphi_c(d_S(v)).       \tag{G.1.2}
\]

Let `P` be any deletion-only sub-Markov kernel, including a stopping
indicator.  For a current carrier state `x=(S,gamma)`, define

\[
 a(x)=\sum_{S'}P(S,S')\mathbf1_{\{\gamma\text{ alive in }S'\}},
\]
\[
 e_c(x)=\sum_{S'}P(S,S')\mathbf1_{\{\gamma\text{ alive in }S'\}}
       \{\varphi_c(d_S(v))-\varphi_c(d_{S'}(v))\}.          \tag{G.1.3}
\]

Whenever both carrier masses are positive,

\[
 \boxed{A_c(\nu P)=
 {\mathbb E_{\widehat\nu}[a\varphi_c-e_c]
       \over\mathbb E_{\widehat\nu}a}},                  \tag{G.1.4}
\]
and therefore

\[
 \boxed{A_c(\nu P)-A_c(\nu)=
 {\operatorname {Cov}_{\widehat\nu}(a,\varphi_c)
       -\mathbb E_{\widehat\nu}e_c
       \over\mathbb E_{\widehat\nu}a}.}                  \tag{G.1.5}
\]

Indeed, terminal alive carriers have unique labelled parents, so the
terminal carrier mass divided by the initial carrier mass is `E a`.
Summing the terminal test over those carriers gives
`E(a varphi_c-e_c)`, which proves (G.1.4); centering proves (G.1.5).

The erosion term is nonnegative.  For `d>c`,

\[
 {\varphi_c(d+1)\over\varphi_c(d)}
 =\left(1+{1\over d-c}\right)^m{d-m+1\over d+1}\ge1,       \tag{G.1.6}
\]

because Bernoulli's inequality and `c>=m-1` give
`(1+1/(d-c))^m >= 1+m/(d-m+1)=(d+1)/(d-m+1)`.
Deletion cannot increase `d`, hence `e_c>=0`.  Thus survival selection is
the only sign-indefinite term in (G.1.5).

For a reference pair `(lambda,U)`, define `Delta` and `Delta^0` to be the
right side of (G.1.5) for `(nu,P)` and `(lambda,U)`, respectively, before
adding `A_c` itself.  If the four adjacent scalars are positive, then

\[
 {A_c(\nu P)/A_c(\lambda U)\over A_c(\nu)/A_c(\lambda)}
 ={1+\Delta/A_c(\nu)\over1+\Delta^0/A_c(\lambda)}.          \tag{G.1.7}
\]

Consequently, for a fixed terminal cutoff `c`, put
\(A_{j,c}=A_c(\nu_j)\) and \(B_{j,c}=A_c(\lambda_j)\).  Iteration is
exact:

\[
 \log{A_c(\nu_J)\over A_c(\lambda_J)}
 =\log{A_c(\nu_0)\over A_c(\lambda_0)}
 +\sum_{j<J}\left[
  \log\!\left(1+{\Delta_{j,c}\over A_{j,c}}\right)
 -\log\!\left(1+{\Delta^0_{j,c}\over B_{j,c}}\right)
 \right].                                                  \tag{G.1.8}
\]

Zero reference tail is harmless: full support and nonnegativity make
`F_c` identically zero on that reference slice.  Formula (G.1.8), with one
fixed `c` while telescoping backward, is the exact stopped scalar
comparison; it neither assumes nor requires full-state likelihood
domination.

We next remove the infinitesimal-bite fiction.  In a deterministic state
put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 B(\gamma)=\bigcup_{i=1}^m\Gamma(F_i),\qquad
 h(\gamma)=|B(\gamma)|,
\]
\[
 \Delta_C=\max_F|\Gamma(F)|.
\]

Mark every row independently with probability `p` and accept exactly the
isolated marks.  If `a_p(gamma)` is the probability that the carrier
survives, then

\[
 \boxed{a_p(\gamma)=1-ph(\gamma)+r_p(\gamma),\qquad
 0\le r_p(\gamma)\le\left({m^2\over2}+m\right)
                         (p\Delta_C)^2.}                    \tag{G.1.9}
\]

If no member of `B(gamma)` is marked, the carrier survives, and
`0<=(1-p)^h-(1-ph)<=binom(h,2)p^2`.  Any additional survival has a marked
row in `B(gamma)` that is rejected by a distinct marked conflict
neighbour.  The ordered-pair union bound is at most
`p^2 h Delta_C`; since `h<=m Delta_C`, (G.1.9) follows.

Let `Delta` bound `Delta_C` on the support of the current law and assume
`p Delta` is a sufficiently small constant.  Substitution of (G.1.9) in
(G.1.5), use of `e_c>=0`, and
`|Cov(r_p,varphi_c)|<=2||r_p||_infty A_c` give

\[
 \boxed{
 \log{A_c(\nu P_p)\over A_c(\nu)}
 \le -p{\operatorname {Cov}_{\widehat\nu}(h,\varphi_c)
             \over A_c(\nu)}+C_m(p\Delta)^2.}              \tag{G.1.10}
\]

If \(p_j\Delta_j\le C\varepsilon\) for every microbite and their number is
at most \(C r\log r/\varepsilon\), then

\[
 \sum_j(p_j\Delta_j)^2=O(\varepsilon r\log r)
                        =o(r^{-1-\alpha}).                  \tag{G.1.11}
\]

The last equality holds under
\(\varepsilon=o(r^{-2-\alpha}/\log r)\).  More generally the exact
finite-bite budget is \(\sum_j(p_j\Delta_j)^2\); no constant-rate or
stopped-mixing assertion is hidden here.

The actual clock may choose its marking probability predictably from the
current state.  If the state is \(S\), write \(p=p(S)\), put

\[
 \theta=\sup_Sp(S)\Delta_C(S),\qquad
 s(S,\gamma)=p(S)h(S,\gamma),                              \tag{G.1.11a}
\]

and assume \(\theta\) is a sufficiently small constant depending only on
\(m\).  Applying (G.1.9) conditionally on \(S\) gives
\(a=1-s+r\), \(0\le r\le C_m\theta^2\).  Repeating the proof of
(G.1.10), without taking \(p\) outside the Palm expectation, yields

\[
 \boxed{
 \log{A_c(\nu P_{p(\cdot)})\over A_c(\nu)}
 \le-{\operatorname {Cov}_{\widehat\nu}(s,\varphi_c)
              \over A_c(\nu)}+C_m\theta^2.}                 \tag{G.1.11b}
\]

Thus the live regression variable is the weighted hazard \(p(S)h\), not
the unweighted hazard with \(p\) replaced by a constant.  In particular,
conditioning first on the root degree gives the literal profile
\(\zeta_s(d)=\mathbb E_{\widehat\nu}[p(S)h\mid d_S(v)=d]\).
Along a varying schedule, its remainder is the sum of the corresponding
\(\theta_j^2\).

Finally, exact shore sizes introduce no fibre-probability penalty.  Let
`N_j` be the vector of actual shore sizes with law `w_j`, let
`lambda_n` be uniform on the slice of size vector `n`, and put

\[
 \Lambda_j=\sum_nw_j(n)\lambda_n.
\]

If `kappa_j(n,n')` is the actual joint law of successive size vectors and
`K_j(n,n')=kappa_j(n,n')/w_j(n)`, define, for `S` in the `n`-slice,

\[
 U_j(S,S')=\sum_{n'\le n}K_j(n,n')
 {\mathbf1_{\{S'\subseteq S,\ |S'|=n'\}}
       \over\prod_\sigma {n_\sigma\choose n'_\sigma}}.     \tag{G.1.12}
\]

Double counting nested pairs proves

\[
                         \boxed{\Lambda_jU_j=\Lambda_{j+1}.} \tag{G.1.13}
\]

Moreover, for nonnegative observables `F,t`, with `F=0` on every
positive-mass zero-`t` fibre,

\[
 {\mathbb E_{\Lambda_j}F\over\mathbb E_{\Lambda_j}t}
 \le\sup_{n:w_j(n)\mathbb E_{\lambda_n}t>0}
 {\mathbb E_{\lambda_n}F\over\mathbb E_{\lambda_n}t}.     \tag{G.1.14}
\]

This is just a weighted average of the fibrewise ratios with weights
`w_j(n) E_(lambda_n)t`.  Hence every uniform exact-slice estimate in a
density bin passes to the random-size reference mixture without division
by a small size probability.

For completeness, let \(r_\sigma\in\{0,1\}\) indicate whether the carrier
root lies on shore \(\sigma\).  If a carrier footprint uses
\(b_{\gamma,\sigma}\) nonroot targets on that shore, then, conditional on
retaining the root target, the exact nested-slice survival factor is

\[
 \prod_\sigma{(n'_\sigma-r_\sigma)_{b_{\gamma,\sigma}}
                   \over(n_\sigma-r_\sigma)_{b_{\gamma,\sigma}}}.
                                                                  \tag{G.1.15}
\]

Without conditioning on the root, multiply (G.1.15) by the common factor
\(\prod_\sigma(n'_\sigma/n_\sigma)^{r_\sigma}\).  For a fixed root shore
this factor is independent of the carrier label and cancels from every
Palm ratio used here.

Put \(N_\sigma=n_\sigma-r_\sigma\) and
\(N'_\sigma=n'_\sigma-r_\sigma\).  When
\(\delta_\sigma=1-N'_\sigma/N_\sigma\le1/4\) and
\(b_{\gamma,\sigma}\le N_\sigma/2\), termwise expansion of
\(\log(1-z)\) gives

\[
 \log{(N'_\sigma)_{b_{\gamma,\sigma}}
             \over(N_\sigma)_{b_{\gamma,\sigma}}}
 =-b_{\gamma,\sigma}\delta_\sigma
 +O\!\left(b_{\gamma,\sigma}\delta_\sigma^2+
   {b_{\gamma,\sigma}^2\delta_\sigma\over N_\sigma}\right).
 \tag{G.1.16}
\]

The logarithm of (G.1.15) is the sum of (G.1.16) over the shores.

At the punctured scale \(b_{\gamma,\sigma}=O_m(r)\), shore sizes are
exponential, and \(\delta_\sigma=O(\varepsilon/r)\), so (G.1.16) is
\(O_m(\varepsilon)\), while its displayed remainder is
\(O_m(\varepsilon^2/r)+e^{-\Omega(r)}\). Accepted-count concentration is
the separate theorem in Appendix C.5.

Equations (G.1.2)--(G.1.16) are the exact finite-bite and slice bridge used by the stopped target G.2.  Under the
independent product reference, conditioning on a fixed labelled carrier
leaves independent target indicators.  Both its live conflict hazard `h`
and the degree-tail test are increasing, so Harris association makes the
within-carrier covariance favorable.  The only possible adverse reference
term is therefore the between-carrier covariance.  G.14 rewrites that
term as the tail tilt of the signed connected statistic
`q_0 Xi_gamma^circ`; G.15 decomposes it into carrier U-statistics; G.18
gives the exact two-shore cell determinant for `s=2`; and G.19 localizes
the factorial pair law.  What remains open is exactly:

1. cutoff-tail leakage and kernel-weighted uniform integrability outside
   the disjoint overlap cell;
2. the signed dominant-cell determinant and the signed `s=3,...,12`
   remainder;
3. the stopped twelfth-moment comparison (G.29), with
   \(\kappa<2-20\alpha\) for the present shore ledger; and
4. actual/reference survival-payoff and realized-center comparison, plus
   the purge/cemetery ledger, within the exponent budget of G.2.

## G.2 Product high moments and the exact stopped target

The following reference-law estimate is proved; its adaptive stopped
analogue is not.

For a fixed even \(m=2s\), the rooted component expansion from
C.3--C.3bis gives, at a product reference checkpoint,

\[
 {\mathbb E(X_v-\mu)^m\over\mu^m}
 \le C_m\!\!\sum_{\sum jn_j=m}R_1^{n_2}
       \prod_{j=3}^m Q_{j/2}^{(j-1)n_j}+e^{-\Omega(r)},       \tag{G.21}
\]

where
\(R_c,Q_c=O_c(r^{-1}x^{-3c}+r^{-2}x^{-4c})\).  To see (G.21), expand the
centered indicators of the incident configurations.  A dependency
component of size two costs \(R_1\); a component of size \(j\ge3\) is
controlled as follows. Give pair \(ab\) weight \(t_{ab}\). A uniform spanning tree contains each pair with probability \(2/j\), so a maximum-weight tree \(T\) satisfies \(\sum_{a<b}t_{ab}\le(j/2)\sum_{ab\in T}t_{ab}\). Connectedness lets \(T\) use only positive-overlap edges. Therefore \(x^{-\sum t_{ab}}\le\prod_{ab\in T}\mathbf1_{\{t_{ab}>0\}}x^{-(j/2)t_{ab}}\); rooting the tree and summing its leaves costs \(Q_{j/2}^{j-1}\).
Singleton components vanish.  Repeated Bernoulli powers reduce to fewer
distinct centered indicators.  There are only \(j^{j-2}\) labelled trees.

When \(\alpha<1/(3m)\), every component in (G.21) is at most its Gaussian
pairing scale.  Indeed, relative to
\(\varrho^{j/2}\), \(\varrho=r^{-1}x^{-3}\), the first kernel monomial is
\(r^{1-j/2}x^{-3j(j-2)/2}\le1\), and selecting its second monomial costs
at most \(r^{-1}x^{-j/2}\le1\).  Writing \(U_m^{\rm ref}\) for the normalized central moment on the left of (G.21), we obtain

\[
 U_m^{\rm ref}=O_m((rx^3)^{-m/2})+e^{-\Omega(r)}.     \tag{G.22}
\]

Appendix C.3ter transfers (G.22) to uniform two-shore slices.  For the
actual process, on shore \(\sigma\) define
\[
 U_{12,aw_j}(H_j)=
 {1\over n_{j,\sigma}z_{j,\sigma}^{12}}
 \sum_{v:d_j(v)>a w_{j,\sigma}}
       |d_j(v)-z_{j,\sigma}|^{12},
\]
where \(n_{j,\sigma}=|V_\sigma(H_j)|\), \(d_j(v)\) is the degree of
\(v\) in \(H_j\), \(z_{j,\sigma}=n_{j,\sigma}^{-1}
\sum_{v\in V_\sigma(H_j)}d_j(v)\),
\(w_{j,\sigma}\) is a predictable shadow center, and \(a>1\) is fixed.
Stop before any cap, shore-comparability, degree-floor, or fixed
shadow-ratio bound fails.  For a fixed-ratio density bin
\([\xi_\ell,2\xi_\ell)\), let \(\mathcal G_{j,\ell}\) be the event that
round \(j\) precedes every stop and lies in that bin.

The exact missing stopped-law input is [O]:
\[
 \boxed{\mathbb E[U_{12,aw_j}(H_j)\mid\mathcal G_{j,\ell}]
 \le r^{\kappa+o(1)}(r\xi_\ell^3)^{-6}+e^{-\Omega(r)},
 \qquad \kappa<2-20\alpha.}                              \tag{G.29}
\]
It must be accompanied by finite-bite, realized-center, purge, and
accepted-count errors whose total is \(o(r^{-\alpha}/r)\).  These are
premises of a possible Gate-A closure, not conclusions of this section.
The product and exact-slice estimates do not imply (G.29).

## G.14 The exact punctured connected-carrier correction


For the complete directed-punctured catalogue under independent target
retention, the one-carrier conditional mean hazard is exactly constant.
Consequently every between-carrier Simpson contribution comes from a
genuinely connected correction involving at least two carrier rows and one
further catalogue row.

In a retained target state let $E(H)$ be the surviving catalogue rows,
$d_v=|\{G\in E(H):v\in G\}|$, and
$\Gamma_H(F)=\{G\in E(H):G\cap F\ne\varnothing\}$. For an ordered
$m$-carrier $\gamma=(v;F_1,\ldots,F_m)$ put
$h_\gamma=|\bigcup_i\Gamma_H(F_i)|$ and define the signed connected
statistic $\Xi_\gamma$ in (G.14.3.3) below. If

\[
 H_\gamma=\mathbb E[h_\gamma\mid\gamma\text{ retained}],
 \qquad
 P_\gamma=\mathbb E[\psi(d_v/c)\mid\gamma\text{ retained}], \tag{G.14.0.1}
\]

where $c>0$ is deterministic and $\psi$ is increasing, then

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi(d_v/c))
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\psi(d_v/c)
                    \mid\gamma)
  +q_0\operatorname {Cov}_\pi(\Xi_\gamma,P_\gamma).}       \tag{G.14.0.2}
\]

The first term is nonnegative by Harris/FKG.  Thus, if
$d\tau/d\pi=P_\gamma/\mathbb E_\pi P_\gamma$,

\[
 \boxed{
 \frac{[-\operatorname {Cov}_{\rm Palm}(h_\gamma,\psi)]_+}
      {\mathbb E_{\rm Palm}\psi}
 \le q_0[\mathbb E_\pi\Xi_\gamma
             -\mathbb E_\tau\Xi_\gamma]_+.}                \tag{G.14.0.3}
\]

This is the exact product-reference object.  A deterministic normalization
of the hazard divides both sides by that deterministic row-count scale.
The realized random row count is a separate shadow-denominator transfer.

The statistic $\Xi_\gamma$ retains the cancellation lost by separate
absolute bounds on companion exposure and carrier duplicates.  Its activity
expansion has only three kinds of terms:

1. a negative empty-set duplicate term;
2. positive target sets spanning more than one carrier row; and
3. negative target sets shared by at least two carrier rows.

The remaining theorem is a tail-mass-relative estimate for this signed
connected statistic at $m=12$, not a pointwise bound on
$|\Xi_\gamma|$.

#### G.14.1 Product reference and carrier Palm law

Let $\mathcal C_r$ be the complete directed-punctured catalogue.  Every
row has $2r$ middle and $2r$ lower targets.  Retain a target $u$
independently with probability

\[
 p_u=p_{\operatorname{sh}(u)},\qquad p_M=y,\quad p_L=x,
 \qquad 0<x\le y\le1,                                    \tag{G.14.1.1}
\]

and put

\[
                         q_0=x^{2r}y^{2r}.                  \tag{G.14.1.2}
\]

Thus every catalogue row has unconditional survival probability $q_0$.
Fix a root $v$ in one chosen shore, and let
$\gamma=(v;F_1,\ldots,F_m)$ be an ordered tuple of distinct catalogue
rows through $v$.  Write

\[
 S_\gamma=\bigcup_{i=1}^mF_i,\qquad
 m_\gamma(u)=|\{i:u\in F_i\}|.                             \tag{G.14.1.3}
\]

The carrier survival probability is

\[
 q_\gamma=\prod_{u\in S_\gamma}p_u
 =q_0^m\prod_{u\in S_\gamma}p_u^{-(m_\gamma(u)-1)}.         \tag{G.14.1.4}
\]

Hence the carrier-label Palm law is

\[
                         \pi_\gamma
 =\frac{q_\gamma}{\sum_{\gamma'}q_{\gamma'}}.              \tag{G.14.1.5}
\]

Equation (G.14.1.4) shows that its departure from the uniform label law is itself
an intersection polymer supported only on targets repeated among carrier
rows.

The formulas may instead mix all root labels in the chosen shore: regard
$(v;F_1,\ldots,F_m)$ as the carrier label and use the same survival weight
$q_\gamma$.  Every identity below is labelwise.  More importantly, the
one-body constant in (G.14.2.2) depends on the row but not on the designated
root, and is in fact the same for every row.  It therefore remains a
constant after this shore/root Palm averaging.  Gate A applies the argument
one shore at a time, so no cross-shore mixture is required.

#### G.14.2 The one-body profile is constant

For one catalogue row $F$, define

\[
 L(F)=\mathbb E[|\Gamma(F)\cap E(H)|\mid F\text{ retained}]
 =q_0\sum_{G:G\cap F\ne\varnothing}
       \prod_{u\in G\cap F}p_u^{-1}.                       \tag{G.14.2.1}
\]

The symmetric group on the $2r+1$ ground labels acts transitively on the
catalogue rows: if $F=E(w)$ and $F'=E(w')$, the coordinate permutation
sending $w_i$ to $w'_i$ maps $F$ to $F'$, preserves the two shores,
and permutes the complete catalogue.  The product probabilities in (G.14.1.1)
depend only on the shore.  Therefore

\[
                         \boxed{L(F)=L_r(x,y)}              \tag{G.14.2.2}
\]

for every catalogue row $F$.

This is exactly the one-body cancellation absent from a generic
hypergraph.  A root target may occupy different positions in the oriented
punctured path, so its conditional degree-tail profile $P_\gamma$ need
not be one-body constant.  That causes no Simpson term because the hazard
profile paired with it in (G.14.2.2) is constant.

#### G.14.3 Exact connected correction

For a further catalogue row $G$, put

\[
 A_i(G)=G\cap F_i,qquad
 J_G(\gamma)=\{i:A_i(G)\ne\varnothing\},\qquad
 U_G(\gamma)=G\cap S_\gamma=\bigcup_iA_i(G),               \tag{G.14.3.1}
\]

and write

\[
                         w(A)=\prod_{u\in A}p_u^{-1}.       \tag{G.14.3.2}
\]

Define

\[
 \boxed{
 \Xi_\gamma=\sum_{G\in\mathcal C_r}
 \left\{
  \mathbf1_{\{J_G\ne\varnothing\}}w(U_G)
  -\sum_{i\in J_G}w(A_i(G))
 \right\}.}                                                \tag{G.14.3.3}
\]

##### Theorem G.14.3.1 (exact hazard decomposition)

For every labelled carrier,

\[
                         \boxed{H_\gamma=mL_r(x,y)+q_0\Xi_\gamma.} \tag{G.14.3.4}
\]

#### Proof

Conditioning the carrier to survive fixes every target in $S_\gamma$.
Thus a further row $G$ survives conditionally with probability

\[
             q_0w(G\cap S_\gamma)=q_0w(U_G).               \tag{G.14.3.5}
\]

It belongs to the carrier hazard exactly when $J_G\ne\varnothing$.
Summing (G.14.3.5) proves

\[
 H_\gamma=q_0\sum_G
       \mathbf1_{\{J_G\ne\varnothing\}}w(U_G).             \tag{G.14.3.6}
\]

On the other hand, summing the one-carrier formula (G.14.2.1) over the $m$
carrier rows gives

\[
 mL_r(x,y)=q_0\sum_G\sum_{i\in J_G}w(A_i(G)).              \tag{G.14.3.7}
\]

Subtract (G.14.3.7) from (G.14.3.6).  This is (G.14.3.4).  $\square$

If $G$ meets zero or one carrier row, its summand in (G.14.3.3) is zero.
Consequently

\[
 \boxed{\Xi_\gamma\text{ is supported on }G
                 \text{ meeting at least two carrier rows}.} \tag{G.14.3.8}
\]

This is a literal carrier--carrier--row connectedness condition.

##### G.14.3.2 Removing the constant root-only cluster

There is a sharper form adapted to the rooted boundary polymer.  Put
$p_v=p_{\operatorname{sh}(v)}$, let $D_v$ be the complete-catalogue degree
of $v$, and define the off-root intersections

\[
 B_i(G)=(G\cap F_i)-\{v\},\qquad
 K_G=\{i:B_i(G)\ne\varnothing\},\qquad
 B_G=\bigcup_iB_i(G).                                     \tag{G.14.3.9}
\]

For a catalogue row $G$, set

\[
 \chi_\gamma^\circ(G)=
 \begin{cases}
 p_v^{-1}\left\{w(B_G)-\displaystyle\sum_{i=1}^mw(B_i(G))
                         +(m-1)\right\},&v\in G,\\
 \mathbf1_{\{K_G\ne\varnothing\}}w(B_G)
       -\displaystyle\sum_{i\in K_G}w(B_i(G)),&v\notin G,
 \end{cases}                                               \tag{G.14.3.10}
\]

and

\[
                         \Xi_\gamma^\circ
 =\sum_{G\in\mathcal C_r}\chi_\gamma^\circ(G).             \tag{G.14.3.11}
\]

If $v\in G$, then every $A_i(G)=\{v\}\cup B_i(G)$ and
$U_G=\{v\}\cup B_G$.  Its summand in (G.14.3.3) is therefore

\[
 p_v^{-1}\left\{w(B_G)-\sum_{i=1}^mw(B_i(G))\right\}
 =(1-m)p_v^{-1}+\chi_\gamma^\circ(G).                       \tag{G.14.3.12}
\]

There are exactly $D_v$ such rows.  The external-row summands in (G.14.3.3)
already equal the second line of (G.14.3.10).  Hence

\[
 \boxed{\Xi_\gamma=(1-m)p_v^{-1}D_v+\Xi_\gamma^\circ.}      \tag{G.14.3.13}
\]

The first term is independent of the carrier label and disappears from
every covariance.  Moreover,

\[
 \boxed{\chi_\gamma^\circ(G)=0\quad\text{whenever }|K_G|\le1.} \tag{G.14.3.14}
\]

For $v\notin G$, this is the one-carrier cancellation already noted after
(G.14.3.7).  For $v\in G$, if no $B_i$ is nonempty then the braces in (G.14.3.10)
are $1-m+(m-1)=0$; if exactly one is nonempty, its weight cancels and the
same constants cancel.  Thus every nonconstant term has an off-root
two-star

\[
                         F_i\;-\;G\;-\;F_j,\qquad i\ne j,   \tag{G.14.3.15}
\]

whose two links are witnessed by off-root shared targets.  This is the
precise connected support to be classified by the punctured boundary
polymer.

#### G.14.4 Signed activity expansion

Put

\[
                         a_u=p_u^{-1}-1\ge0,qquad
 a(T)=\prod_{u\in T}a_u.                                  \tag{G.14.4.1}
\]

For $J_G\ne\varnothing$ and $T\subseteq U_G$, define

\[
 c_\gamma(T;G)=|\{i\in J_G:T\subseteq A_i(G)\}|.          \tag{G.14.4.2}
\]

For $T=\varnothing$, this is $|J_G|$.  Expanding
$w(A)=\prod_{u\in A}(1+a_u)=\sum_{T\subseteq A}a(T)$ in
(G.14.3.3) gives the exact identity

\[
 \boxed{
 w(U_G)-\sum_{i\in J_G}w(A_i(G))
 =\sum_{T\subseteq U_G}
          (1-c_\gamma(T;G))a(T).}                           \tag{G.14.4.3}
\]

The sign structure is now explicit.

* $T=\varnothing$ contributes $1-|J_G|<0$ when the cluster is
  nontrivial.  This is the multiplicity-one duplicate correction.
* If $T\ne\varnothing$ lies in exactly one carrier row, then
  $c_\gamma(T;G)=1$ and it cancels exactly.
* If no one carrier row contains all of $T$, then
  $c_\gamma(T;G)=0$, necessarily $|T|\ge2$, and the term is positive.
  These are cross-carrier conditioning clusters.
* If at least two carrier rows contain $T$, then the term is negative.
  These are shared-target carrier clusters.

In particular, the positive and negative pieces that appear separately as
companion exposure and duplicate load are coefficients of one connected
activity polynomial.  They should not be bounded independently.

For a root row $G\ni v$, the constant subtraction in (G.14.3.10) removes the
empty activity exactly.  With

\[
 c_\gamma^\circ(T;G)
   =|\{i:T\subseteq B_i(G)\}|\qquad
       (\varnothing\ne T\subseteq B_G),
\]

one has

\[
 \boxed{\chi_\gamma^\circ(G)
 =p_v^{-1}\sum_{\varnothing\ne T\subseteq B_G}
       (1-c_\gamma^\circ(T;G))a(T).}                        \tag{G.14.4.4}
\]

Every nonzero term in (G.14.4.4) therefore contains an off-root target
activity.  Together with (G.14.3.14), it is supported on the two-link connected
shape (G.14.3.15).

For orientation only, the cancellation-free envelope

\[
 |\Xi_\gamma|
 \le (m+1)\sum_{1\le i<j\le m}
 \sum_{\substack{G:G\cap F_i\ne\varnothing\\
                    G\cap F_j\ne\varnothing}}
          w(G\cap S_\gamma)                                \tag{G.14.4.5}
\]

follows from $w(A_i)\le w(U_G)$.  It is generally too lossy for the
coefficient-one ledger; (G.14.4.3)--(G.14.4.4), not (G.14.4.5), are the intended polymer
input.

#### G.14.5 Exact covariance reduction

Conditioned on a fixed labelled carrier, the remaining target indicators
are independent.  Both $h_\gamma$ and $\psi(d_v/c)$ are increasing, so
Harris's inequality gives

\[
 \operatorname {Cov}(h_\gamma,\psi(d_v/c)
             \mid\gamma\text{ retained})\ge0.              \tag{G.14.5.1}
\]

For completeness, Harris's inequality here follows by induction on the
independent Bernoulli coordinates: condition on the last coordinate and
use total covariance; the two conditional means are increasing in that
coordinate. The law of total covariance under the Palm mixture is

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\psi)
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\psi\mid\gamma)
  +\operatorname {Cov}_\pi(H_\gamma,P_\gamma).             \tag{G.14.5.2}
\]

Substitute (G.14.3.4); the constant $mL_r(x,y)$ disappears.  This proves
(G.14.0.2).  Dividing the second covariance by
$\mathbb E_\pi P_\gamma=\mathbb E_{\rm Palm}\psi$ gives

\[
 \frac{\operatorname {Cov}_\pi(\Xi_\gamma,P_\gamma)}
      {\mathbb E_\pi P_\gamma}
 =\mathbb E_\tau\Xi_\gamma-\mathbb E_\pi\Xi_\gamma,       \tag{G.14.5.3}
\]

which proves (G.14.0.3).

By (G.14.3.13), both covariances and both expectation differences are unchanged
when $\Xi_\gamma$ is replaced by $\Xi_\gamma^\circ$.  Thus the exact
adverse term is already supported on the off-root connected shapes in
(G.14.3.14)--(G.14.3.15).

#### G.14.6 The exact remaining product-reference theorem

For $m=12$, $x\ge r^{-\alpha}$, and the relevant deterministic-center
normalized tail tests, it is enough to prove a tail-mass-relative bound on

\[
                 q_0[\mathbb E_\pi\Xi_\gamma^\circ
                         -\mathbb E_\tau\Xi_\gamma^\circ]_+.
                                                                    \tag{G.14.6.1}
\]

The complete one-row boundary polymer already controls every fixed
one-body sum in (G.14.2.1).  It does not by itself control (G.14.6.1): the carrier
law (G.14.1.4), the signed multi-carrier activity (G.14.4.3), and the tail tilt
$P_\gamma$ must be expanded together.  The all-order Newton obstruction
for the normalized tail test prevents replacement of that expansion by a
fixed list of carrier moments.

Thus (G.14.6.1) is a precise tail-decorated connected-polymer target.  This note
does not claim its asymptotic bound, its exact-slice transfer, or the later
stopped-law/realized-center/purge transfer.

## G.15 The connected-carrier Möbius and U-statistic hierarchy

This section proves an exact refinement of G.14.  It decomposes the connected
correction by the number of carrier rows genuinely joined by one further row,
then sums every unused carrier label out of the Palm law.  Only the resulting
tail-relative estimate remains open.

Fix the root \(v\), an ordered \(m\)-carrier
\(\gamma=(F_1,\ldots,F_m)\), and a further catalogue row \(G\).  With the
notation of G.14 put

\[
 B_i(G)=(G\cap F_i)-\{v\},\qquad
 B_I(G)=\bigcup_{i\in I}B_i(G).                         \tag{G.15.1}
\]

Define the root-reduced set function

\[
 g_{G,\gamma}^{\circ}(I)=
 \begin{cases}
  p_v^{-1}\{w(B_I(G))-1\},&v\in G,\\[2pt]
  \mathbf1_{\{B_I(G)\ne\varnothing\}}w(B_I(G)),&v\notin G.
 \end{cases}                                             \tag{G.15.2}
\]

Thus \(g_{G,\gamma}^{\circ}(\varnothing)=0\), and direct substitution in
(G.14.3.10)--(G.14.3.11) gives

\[
 \Xi_\gamma^\circ=\sum_{G\in\mathcal C_r}
 \left(g_{G,\gamma}^{\circ}([m])-
       \sum_{i=1}^m g_{G,\gamma}^{\circ}(\{i\})\right). \tag{G.15.3}
\]

Put \(\mathcal S_v=\{F\in\mathcal C_r:v\in F\}\). For an ordered
\(s\)-subcarrier \(\alpha=(F_1,\ldots,F_s)\) from
\(\mathcal S_v\), define

\[
 \widehat g_{G,\alpha}^{\circ}([s])
 =\sum_{I\subseteq[s]}(-1)^{s-|I|}g_{G,\alpha}^{\circ}(I), \tag{G.15.4}
\]

and the symmetric kernel

\[
 K_s^\circ(\alpha)=
 \sum_{G\in\mathcal C_r}\widehat g_{G,\alpha}^{\circ}([s]). \tag{G.15.5}
\]

#### G.15.1 Exact connected hierarchy

For \(A\subseteq[m]\), let \(\gamma_A=(F_i)_{i\in A}\) in increasing index order. For every ordered \(m\)-carrier,

\[
 \boxed{\Xi_\gamma^\circ=
   \sum_{\substack{A\subseteq[m]\\|A|\ge2}}
        K_{|A|}^\circ(\gamma_A).}                       \tag{G.15.6}
\]

Moreover a row \(G\) contributes to the \(s\)-body coefficient only if

\[
 \boxed{(G\cap F_i)-\{v\}\ne\varnothing
        \quad(1\le i\le s).}                           \tag{G.15.7}
\]

Indeed, Boolean Möbius inversion gives

\[
 g_{G,\gamma}^{\circ}([m])=
 \sum_{\varnothing\ne A\subseteq[m]}
       \widehat g_{G,\gamma_A}^{\circ}(A).              \tag{G.15.8}
\]

The singleton coefficients are exactly the singleton terms subtracted in
(G.15.3), proving (G.15.6) after summing over \(G\).  If \(B_i(G)\) is
empty, then for every \(I\subseteq[s]-\{i\}\),

\[
 g_{G,\alpha}^{\circ}(I\cup\{i\})=g_{G,\alpha}^{\circ}(I). \tag{G.15.9}
\]

Pairing these two terms in (G.15.4), whose signs are opposite, proves
(G.15.7).

The first kernel retains the cancellation which an absolute polymer bound
would lose.  For \(s=2\), write

\[
 A=(G\cap F_1)-\{v\},\qquad B=(G\cap F_2)-\{v\}.         \tag{G.15.10}
\]

If either set is empty the coefficient is zero; otherwise it is

\[
 \widehat g_{G,(F_1,F_2)}^\circ([2])=
 \begin{cases}
 p_v^{-1}\{w(A\cup B)-w(A)-w(B)+1\},&v\in G,\\[2pt]
 w(A\cup B)-w(A)-w(B),&v\notin G.
 \end{cases}                                             \tag{G.15.11}
\]

This follows immediately by expanding the four subsets in (G.15.4).
In particular (G.15.11), rather than its termwise absolute value, is the
connected off-root two-star which the tail estimate must control.

#### G.15.2 Exact removal of unused carrier labels

Let \(X\) be the product target-retention state, let \(F\preceq X\) mean
that every target of \(F\) survives, and let
\(d=d_v(X)\) be the number of live root rows.  For \(2\le s\le m\), put

\[
 Y_s(X)=\sum_{\alpha\in\mathcal S_v^{\underline s}}
   \mathbf1_{\{\alpha\preceq X\}}K_s^\circ(\alpha),\qquad
 \overline K_s(X)=\begin{cases}Y_s(X)/(d)_s,&d\ge s,\\0,&d<s.
 \end{cases}                                             \tag{G.15.12}
\]

For an integer \(c\ge m-1\), with
\(\mathbb E(d-c)_+^m>0\), define two probability tilts of the product law:

\[
 f_c(d)=(d-c)_+^m,\qquad
 {d\lambda_m\over d\mathbb P}={(d)_m\over\mathbb E(d)_m},\qquad
 {d\lambda_c\over d\mathbb P}={f_c(d)\over\mathbb Ef_c(d)}. \tag{G.15.13}
\]

Also put

\[
 \varphi_c(d)=\begin{cases}f_c(d)/(d)_m,&d\ge m,\\0,&d<m,
 \end{cases}\quad
 P_\gamma=\mathbb E[\varphi_c(d)\mid\gamma\preceq X],\quad
 {d\tau_c\over d\pi}(\gamma)={P_\gamma\over\mathbb E_\pi P_\gamma}. \tag{G.15.14}
\]

Then every unused label sums out exactly:

\[
 \boxed{
 \mathbb E_\pi\Xi_\gamma^\circ
  =\sum_{s=2}^m{m\choose s}\mathbb E_{\lambda_m}\overline K_s,
 \qquad
 \mathbb E_{\tau_c}\Xi_\gamma^\circ
  =\sum_{s=2}^m{m\choose s}\mathbb E_{\lambda_c}\overline K_s.} \tag{G.15.15}
\]

To prove this, fix a state with \(d\) live root rows and a set of \(s\)
carrier positions.  After choosing their ordered subcarrier there are
\((d-s)_{m-s}\) ways to fill the other positions.  Hence (G.15.6) gives
the statewise identity

\[
 \sum_{\gamma\preceq X}\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}(d-s)_{m-s}Y_s(X)
 =(d)_m\sum_{s=2}^m{m\choose s}\overline K_s(X).         \tag{G.15.16}
\]

Because \(\sum_\gamma q_\gamma=\mathbb E(d)_m\), averaging and dividing
proves the first identity in (G.15.15).  Furthermore

\[
 q_\gamma P_\gamma=
 \mathbb E[\mathbf1_{\{\gamma\preceq X\}}\varphi_c(d)]. \tag{G.15.17}
\]

Multiplying (G.15.16) by \(\varphi_c(d)\) and averaging gives

\[
 \sum_\gamma q_\gamma P_\gamma\Xi_\gamma^\circ
 =\sum_{s=2}^m{m\choose s}
   \mathbb E[f_c(d)\overline K_s(X)],                    \tag{G.15.18}
\]

whereas the same carrier count without \(\Xi^\circ\) gives

\[
 \sum_\gamma q_\gamma P_\gamma=\mathbb Ef_c(d).         \tag{G.15.19}
\]

Dividing (G.15.18) by (G.15.19) proves the second identity.

#### G.15.3 Exact remaining product term

At the literal Gate-A order \(m=12\), the adverse product-reference term
in (G.14.6.1) is therefore exactly

\[
 \boxed{q_0\left[
  \sum_{s=2}^{12}{12\choose s}
  \left(\mathbb E_{\lambda_{12}}\overline K_s-
        \mathbb E_{\lambda_c}\overline K_s\right)
 \right]_+.}                                             \tag{G.15.20}
\]

Its first unresolved member is

\[
 q_0{12\choose2}
 \left(\mathbb E_{\lambda_{12}}\overline K_2-
       \mathbb E_{\lambda_c}\overline K_2\right),       \tag{G.15.21}
\]

with \(K_2^\circ\) given by (G.15.11).  Thus there is no remaining
carrier-extension or between-label normalization: the open product input
is a tail-mass-relative estimate for the full signed sum (G.15.20), starting
with its tail-decorated connected two-star.  Exact two-shore slicing,
stopped actual/reference erosion, the realized center, and unequal-purge
transfer are later gates and are not asserted here.

## G.18 The two-shore overlap-cell determinant

The two covariances in the carrier comparison recombine exactly.  Retain middle and lower
targets independently with probabilities \(y,x\in(0,1)\), respectively.  For distinct
root rows \(P=(F,H)\), let
\[
 q_P=\Pr(F,H\text{ live}),\qquad
 L_g(P)=\mathbb E[g(d_v)\mid F,H\text{ live}],           \tag{G.18.1}
\]
and at carrier order twelve put
\[
 g_{12}(d)=(d-2)_{10},\qquad
 g_c(d)={(d-c)_+^{12}\over(d)_2},\quad c\ge11,           \tag{G.18.2}
\]
with the second expression zero for \(d<2\).  Set
\[
\begin{gathered}
 Z_{12}=\sum_Pq_PL_{12}(P)=\mathbb E(d_v)_{12},\qquad
 Z_c=\sum_Pq_PL_c(P)=\mathbb E(d_v-c)_+^{12},\\
 \Pi_{12}(P)={q_PL_{12}(P)\over Z_{12}},\qquad
 S(P)={L_c(P)\over L_{12}(P)},\qquad
 \overline S={Z_c\over Z_{12}}.                         \tag{G.18.3}
\end{gathered}
\]
Assume the tail mass is positive.  The cutoff pair law is the
\(S\)-tilt of \(\Pi_{12}\).  Hence, writing \(K(P)=K_2^\circ(F,H)\) for \(P=(F,H)\), with \(K_2^\circ\) defined in (G.15.11),
\[
 \boxed{\Delta_{2,c}:=
 \mathbb E_{\lambda_{12}}\overline K_2-
 \mathbb E_{\lambda_c}\overline K_2
 =-{\operatorname {Cov}_{\Pi_{12}}(K,S)\over\overline S}.} \tag{G.18.4}
\]
Indeed, \((d)_2g_{12}(d)=(d)_{12}\) and
\((d)_2g_c(d)=(d-c)_+^{12}\), so the two state tilts followed by a uniform
ordered live-pair choice are exactly the two pair laws; expanding the
tilted expectation proves (G.18.4).

Partition ordered pairs by
\[
 \tau(P)=(t_M,t_L),                                      \tag{G.18.5}
\]
the numbers of common middle and lower targets after removing the common
root.  If \(\delta_M\) records that the root is middle and
\(\delta_L=1-\delta_M\), then every row has \(2r\) targets per shore and
\[
 q_P=q_\tau=y^{4r-t_M-\delta_M}x^{4r-t_L-\delta_L}.      \tag{G.18.6}
\]
Thus \(\tau\), unlike total overlap when \(x\ne y\), is sufficient for
the pair survival weight.

For the cell \(\mathcal P_\tau\), define
\[
\begin{aligned}
 A_{12,\tau}&=\sum_{P\in\mathcal P_\tau}L_{12}(P),&
 A_{c,\tau}&=\sum_{P\in\mathcal P_\tau}L_c(P),\\
 B_{12,\tau}&=\sum_{P\in\mathcal P_\tau}K(P)L_{12}(P),&
 B_{c,\tau}&=\sum_{P\in\mathcal P_\tau}K(P)L_c(P),
\end{aligned}                                            \tag{G.18.7}
\]
and put
\[
\begin{gathered}
 \rho_\tau={q_\tau A_{12,\tau}\over Z_{12}},\qquad
 \kappa_\tau={B_{12,\tau}\over A_{12,\tau}},\qquad
 s_\tau={A_{c,\tau}\over A_{12,\tau}},\\
 \mathfrak D_\tau=A_{12,\tau}B_{c,\tau}
                  -B_{12,\tau}A_{c,\tau},\qquad
 \eta_\tau={\mathfrak D_\tau\over A_{12,\tau}^2}.       \tag{G.18.8}
\end{gathered}
\]
Conditional on \(\tau\), the factorial pair law has mass
\(L_{12}(P)/A_{12,\tau}\).  Its means of \(K,S\) are
\(\kappa_\tau,s_\tau\), and its covariance is \(\eta_\tau\).
The law of total covariance therefore gives the exact live reduction
\[
 \boxed{\Delta_{2,c}=-{1\over\overline S}
 \left\{\operatorname {Cov}_\rho(\kappa_\tau,s_\tau)
       +\sum_\tau\rho_\tau
             {\mathfrak D_\tau\over A_{12,\tau}^2}\right\}.} \tag{G.18.9}
\]
Moreover
\[
 \mathfrak D_\tau={1\over2}\sum_{P,Q\in\mathcal P_\tau}
 L_{12}(P)L_{12}(Q)
 [K(P)-K(Q)][S(P)-S(Q)],                                \tag{G.18.10}
\]
by expanding the four products.  The within-cell part of (G.18.9) is
therefore
\[
                         -{1\over Z_c}\sum_\tau
 q_\tau{\mathfrak D_\tau\over A_{12,\tau}}.             \tag{G.18.11}
\]
This is already normalized by tail mass and preserves cancellation between
cells.  Write \(z=z_\sigma\) for the average degree on the root shore. Its first honest sufficient boundary target is
\[
 q_0\left[-{1\over Z_c}\sum_\tau
 q_\tau{\mathfrak D_\tau\over A_{12,\tau}}\right]_+=o(z), \tag{G.18.12}
\]
together with a favorable or \(o(z/q_0)\) between-cell term.

No cellwise sign is asserted. The open theorem is the aggregate punctured estimate in (G.18.9)--(G.18.12), followed by the kernels \(3\le s\le12\) and the slice, stopped, center, and purge transfers.

## G.19 Factorial pair-Palm mass is off-root disjoint

Assume \(x\ge r^{-\alpha}\) for a fixed \(\alpha>0\), condition on retaining a root \(v\), and let \(\mathcal F_v\) be its \(D\)
catalogue rows; each has the same conditional survival probability \(w\).
For distinct \(F,G\), put
\[
 t(F,G)=|(F\cap G)-\{v\}|.                               \tag{G.19.1}
\]
For fixed \(c\ge1\), define the rooted kernels
\[
 R_c=\max_F{1\over D}\sum_{G\ne F}(x^{-ct(F,G)}-1),\qquad
 Q_c=\max_F{1\over D}\sum_{\substack{G\ne F\\t(F,G)>0}}
                                      x^{-ct(F,G)}.       \tag{G.19.2}
\]
The rooted boundary-polymer estimate proved in C.3 and C.3bis gives, for
\(c\alpha<1/2\),
\[
 R_c,Q_c=O_c\!\left({1\over rx^{3c}}+
                         {1\over r^2x^{4c}}\right).       \tag{G.19.3}
\]

For an ordered distinct \(m\)-tuple
\(\gamma=(F_1,\ldots,F_m)\), let \(q_\gamma^*\) be its joint survival
probability conditional on \(v\).  If a nonroot target \(u\) occurs in
\(n_u\) carriers, then
\[
 {q_\gamma^*\over w^m}
 =\prod_{\substack{u\ne v\\n_u\ge2}}p_u^{1-n_u}
 \le x^{-\sum_{a<b}t(F_a,F_b)},                         \tag{G.19.4}
\]
because \(p_u\ge x\) and \(n_u-1\le{n_u\choose2}\); the ratio is also at
least one.  Normalize these weights to the carrier law \(\pi_m\).

Fix \(F_1,\ldots,F_{i-1}\).  With \(j=i-1\), apply AM--GM to
\(z_a=x^{-jt(F_a,F_i)}\).  Its geometric mean is the summand below, and
(G.19.2) gives
\[
 \sum_{F_i\notin\{F_1,\ldots,F_{i-1}\}}
 x^{-\sum_{a<i}t(F_a,F_i)}
 \le D(1+R_{i-1}).                                      \tag{G.19.5}
\]
If \(t(F_1,F_2)>0\), the corresponding second-carrier sum is at most
\(DQ_1\).  Summing (G.19.4) successively from \(F_m\) down to \(F_2\)
therefore yields
\[
 \sum_{\substack{\gamma\\t(F_1,F_2)>0}}q_\gamma^*
 \le w^mD^mQ_1\prod_{j=2}^{m-1}(1+R_j).                 \tag{G.19.6}
\]
On the other hand the lower half of (G.19.4) gives
\[
                         \sum_\gamma q_\gamma^*
                         \ge(D)_mw^m.                    \tag{G.19.7}
\]
If \(\alpha<1/[3(m-1)]\), (G.19.3) makes every displayed \(R_j=o(1)\);
also \(D^m/(D)_m=1+o(1)\).  Dividing (G.19.6) by (G.19.7) proves
\[
 \boxed{\Pr_{\pi_m}(t(F_a,F_b)>0)
 =O_m\!\left({1\over rx^3}+{1\over r^2x^4}\right)}       \tag{G.19.8}
\]
for every specified pair, and a union bound gives the same order for any
of the fixed number of pairs.

At \(m=12\), summing the last ten carrier labels gives exactly
\[
 \sum_{F_3,\ldots,F_{12}}q^*_{F,H,F_3,\ldots,F_{12}}
 =q^*_{FH}\,
 \mathbb E[(d_v-2)_{10}\mid F,H\text{ live}].            \tag{G.19.9}
\]
Thus the first-pair marginal is the factorial Palm law \(\Pi_{12}\) of
G.18.  With \(E=\{\tau\ne(0,0)\}\), (G.19.8) gives, for
\(\alpha<1/33\),
\[
                         \boxed{\Pi_{12}(E)
                         =O((rx^3)^{-1})=o(1).}          \tag{G.19.10}
\]

This is not a tail-relative conclusion.  The cutoff law obeys
\[
 \Pi_c(E)={\mathbb E_{\Pi_{12}}[S\mathbf1_E]
                  \over\mathbb E_{\Pi_{12}}S},           \tag{G.19.11}
\]
whose denominator can be a rare tail mass, and \(K\) is not bounded.  To
delete the exceptional cells from the signed comparison one still needs
\[
 \Pi_c(E)=o(1),\qquad
 {q_0\over z}\left\{
 \mathbb E_{\Pi_{12}}[|K|\mathbf1_E]
 +\mathbb E_{\Pi_c}[|K|\mathbf1_E]\right\}=o(1).         \tag{G.19.12}
\]
Even these estimates leave the arrangement-sensitive determinant
\[
 \mathfrak D_{(0,0)}
 ={1\over2}\sum_{P,Q\in\mathcal P_{(0,0)}}
 L_{12}(P)L_{12}(Q)[K(P)-K(Q)][S(P)-S(Q)]               \tag{G.19.13}
\]
on the dominant cell.  Its favorable or tail-relative small signed bound,
the higher carrier kernels, and all stopped transfers remain open.

# Appendix H: Gate B—certified zero-avoidance lemmas

Only independently reconstructible local, shore-current, and Venn-gap
lemmas are retained. Skipped labels correspond to omitted branches.

## H.1 Exact zero-avoidance setup

Put \(b=2r+1\), identify the label and position sets with
\(\Omega=\mathbb Z_b\), and define
\(I_s^w(u)=\{w_u,\ldots,w_{u+s-1}\}\), with cyclic subscripts. A
permutation \(w\) defines

\[
 E(w)=\{(M,I_r^w(u)):u\ne0\}\mathbin{\dot\cup}
      \{(L,I_{r-1}^w(u)):u\ne0\},\qquad
 D_M=2r\,r!(r+1)! .                                      \tag{H.1.1}
\]

Write \(I_s(u)=I_s^{\mathrm{id}}(u)\), and put
\[
 X=\{(M,I_r(u)),(L,I_{r-1}(u)):u\in\mathbb Z_b\},\quad
 A_0=(M,I_r(0)),\quad B_0=(L,I_{r-1}(0)),\quad
 E_0=X-\{A_0,B_0\}.                                      \tag{H.1.2}
\]
For a tagged target \(S=(\sigma,U)\), write \(\underline S=U\). If
\(J\) is a set of tagged targets, \(\deg(S,J)\) counts the permutations
whose configuration contains \(S\) and every member of \(J\). For
\(s\in\{r,r-1\}\), define
\[
\begin{aligned}
 d_s(S)&=|\{w:S\in E(w)\}|,\\
 W_{1,s}(S)&=\sum_{T\in E_0}\deg(S,\{T\}),\\
 e_s(S)&=\sum_{w:S\in E(w)}(|E(w)\cap E_0|-1)_+,\\
 Z_s(S)&=|\{w:S\in E(w),\ E(w)\cap E_0=\varnothing\}|.
\end{aligned}                                             \tag{H.1.3}
\]
The identity \((m-1)_+=m-1+\mathbf1_{\{m=0\}}\) and finite
inclusion--exclusion give
\[
 \boxed{e_s=W_{1,s}-d_s+Z_s,\qquad
 Z_s(S)=\sum_{J\subseteq E_0}(-1)^{|J|}\deg(S,J).}         \tag{H.1.4}
\]

Fix \(2\le j\le r-2\) disjoint ordered label pairs \((a_i,b_i)\), put
\(k=r-2\), \(\ell=r+3\), and, for every \(U\subseteq\Omega\), set
\[
 H_j(U)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in U\}}-\mathbf1_{\{b_i\in U\}}),
 \qquad H_{s,j}(S)=H_j(\underline S).                     \tag{H.1.5}
\]
For a permutation \(z\), let \(zU=\{z(u):u\in U\}\) and
\(z(\sigma,U)=(\sigma,zU)\). For \(K_t=I_k(t)\), let \(\mathcal B_t\)
be the injective placements of the distinguished labels in which pair one
occupies positions \((t-1,t)\), pair two occupies
\((t+k-1,t+k)\), and every remaining pair has one position in
\(K_t-\{t,t+k-1\}\) and one in its complement after the four boundary
positions are removed. Both orientations are allowed. Thus
\[
 |\mathcal B_t|=2^j(k-2)_{j-2}(\ell-2)_{j-2}.              \tag{H.1.6}
\]
Complete each placement arbitrarily to a permutation \(z\), and put
\(\varepsilon(z)=H_j(zK_t)\). For a coefficient function \(x\) on the
tagged shore-\(s\) targets, define
\[
 \omega_x(t)={1\over|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\varepsilon(z)
       \sum_{S:|\underline S|=s}x(S)H_j(z\underline S).    \tag{H.1.7}
\]
Only the positions of the distinguished labels occur, so the value is
independent of the completion of \(z\).

The zero-avoidance coefficient has exactly the same boundary profile as
the exposure coefficient. First, \(d_s(S)\) is constant in \(S\) by label
symmetry, and the sum of \(H_j\) over one rank is zero by swapping
\(a_1,b_1\); hence \(\omega_{d_s}=0\). Next fix \(T\in E_0\) and one
boundary placement \(z\). Let \(u_i,v_i\) be the two position coordinates
occupied by event pair \(i\). If \(T\) has equal membership at \(u_i,v_i\),
then \(\tau=(u_i\ v_i)\) fixes \(T\). Pair the inner-sum root set \(S\)
with \(\tau S\). Label equivariance gives
\(\deg(\tau S,\{T\})=\deg(S,\{T\})\), while \(\varepsilon(z)\) is fixed
and \(H_j(z\tau\underline S)=-H_j(z\underline S)\). Thus the two inner
terms cancel. If neither event edge permits this involution, both are
boundaries of \(T\); their intervening arcs have
lengths \(k,\ell\), whereas \(T\) has rank \(r\) or \(r-1\), a
contradiction. Thus the profile of \(S\mapsto\deg(S,\{T\})\) is zero.
Summing over \(T\in E_0\) and using (H.1.4) gives
\[
                         \boxed{\omega_{e_s}(t)=\omega_{Z_s}(t).}
                                                               \tag{H.1.7a}
\]

The blocker coordinates must move with the event. For
\(T=(\sigma,I_{s_\sigma}(u))\in X\), where
\(s_M=r\) and \(s_L=r-1\), define
\[
 \psi_t(T)=\{-2(u-t),-2(u+s_\sigma-t)\}\subseteq\mathbb Z_b.
 \tag{H.1.8}
\]
This bijects \(X\) with the edges of
\(\widetilde B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})\),
and sends the event cuts to the fixed roots \(0,5\). The two omitted
targets become
\[
 \mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\},\qquad
 B_r(t)=\widetilde B_r\setminus\mathcal P_t.               \tag{H.1.9}
\]
For an edge set \(J\), abbreviate
\(\deg_t(S,J)=\deg(S,\psi_t^{-1}(J))\).

For an edge set \(J\subseteq E(\widetilde B_r)\), define

\[
 \mathfrak I_{s,t}(J)=\frac1{|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\varepsilon(z)
 \sum_{\substack{S\text{ tagged}\\ |\underline S|=s}}
 H_j(z\underline S)\,\deg_t(S,J),
 \qquad s\in\{r,r-1\}.                                      \tag{H.1.10}
\]

Here a placement in \(\mathcal B_t\) is completed to a permutation only
to give meaning to \(zU=\{z(u):u\in U\}\).  The summand depends solely on
the placed distinguished labels, so (H.1.10) is independent of the chosen
completion.

Finite inclusion--exclusion in (H.1.4), followed by interchange of two
finite sums, gives the literal identity

\[
 \boxed{\omega_{Z_s}(t)=
 \sum_{J\subseteq E(B_r(t))}(-1)^{|J|}\mathfrak I_{s,t}(J).} \tag{H.1.11}
\]

This formula fixes all multiplicities: every blocker set is an ordinary
edge subset and occurs once, with its inclusion--exclusion sign.

There is a useful current interpretation.  For fixed \(t,z,J\), interchange
the root-target and configuration sums in the numerator of (H.1.10):

\[
 \sum_S H_j(z\underline S)\deg_t(S,J)
 =\sum_{w:E(w)\supseteq\psi_t^{-1}(J)}
   \sum_{a=1}^{b-1}H_j\!\left(zI_s^w(a)\right).             \tag{H.1.12}
\]

Thus the numerator is a shore current of exactly the form used in
Section H.15.1, after relabelling the distinguished pairs by \(z\), and then
multiplied by the sign \(\varepsilon(z)\), whose modulus is one.  It
follows directly from Theorem H.15.2.1 that

\[
 |\mathfrak I_{s,t}(J)|\le2r\deg_t(J),\qquad
 |\mathfrak I_{r,t}(J)-\mathfrak I_{r-1,t}(J)|
 \le2j\deg_t(J),                                         \tag{H.1.13}
\]

where \(\deg_t(J)=|\{w:E(w)\supseteq\psi_t^{-1}(J)\}|\).
The second inequality is valid because the same \(z,J,w\) are coupled on
the two shores before averaging.

The two displayed adjacent position pairs in the definition of
\(\mathcal B_t\) are the **event edges**.  After applying \(\psi_t\), their
two cut roots are

\[
                         p=0,\qquad q=5.                    \tag{H.1.14}
\]

If \(p\notin V(J)\), transpose the two positions of the first event edge.
This fixes every blocker target in \(J\), pairs the root targets, and
reverses exactly one factor in the harmonic product.  Hence
\(\mathfrak I_{s,t}(J)=0\).  The same argument at the second event edge
applies when \(q\notin V(J)\).  Therefore

\[
 \boxed{\mathfrak I_{s,t}(J)=0
       \quad\text{unless}\quad\{0,5\}\subseteq V(J).}      \tag{H.1.15}
\]

This is the precise version of “the boundary-event profile vanishes unless
the blocker set is incident with both roots.”


Appendices H.11, H.15, and H.16 prove a local affine identity, a remote
shore-difference estimate, and a Venn-gap bound. They do not prove Gate B:
the missing output remains the compatible all-depth positive cover stated
in Section 5 and C.10.
## H.11 Sixteen local atoms for zero avoidance [I]

Assume \(r\ge6\). In the nonwrapping integer neighbourhood of the event
roots \(0,5\), the four-vertex supports of blocker terms incident with both
roots are exactly
\[
\begin{array}{rrrr}
(-3,0,2,5),&(-3,0,4,5),&(-3,0,5,6),&(-3,0,5,8),\\
(-1,0,2,5),&(-1,0,4,5),&(-1,0,5,6),&(-1,0,5,8),\\
(0,1,2,5),&(0,1,4,5),&(0,1,5,6),&(0,1,5,8),\\
(0,2,3,5),&(0,3,4,5),&(0,3,5,6),&(0,3,5,8).
\end{array}                                                \tag{H.11.1}
\]
Call this list \(\mathscr V\). For \(V\in\mathscr V\), let \(M(V)\)
be the unique two-edge matching in \(\widetilde B_r[V]\) covering all
four vertices. For the six supports
\[
 \mathscr Q_V=\{(-1,0,2,5),(0,1,2,5),(0,1,4,5),
 (0,2,3,5),(0,3,4,5),(0,3,5,6)\},                         \tag{H.11.2}
\]
the induced graph has one additional connector; write
\(P(V)=E(\widetilde B_r[V])\) for the resulting three-edge path. The
other ten induced graphs equal \(M(V)\). This is exhaustive: choose one
of the four neighbours of each root, giving the sixteen supports in
(H.11.1); on a support in (H.11.2), an edge set incident with all four
vertices is either its endpoint matching or its full path.

Use the sixteen supports \(\mathscr V\) and the six path supports
\(\mathscr Q_V\) listed in (H.11.1)--(H.11.2).  Define the complete signed
local multiset

\[
 \mathscr A_{\rm loc}^{\circ}=
 \{(+1,M(V)):V\in\mathscr V\}
 \;\dot\cup\;
 \{(-1,P(V)):V\in\mathscr Q_V\}.                          \tag{H.11.3a}
\]

It has sixteen positive matching entries and six negative path entries.
The sign in (H.11.3a) is exactly \((-1)^{|J|}\), since a matching has two
edges and a path has three.  At puncture shift \(t\), retain only entries
whose edge set avoids \(\mathcal P_t\):

\[
 \mathscr A_{\rm loc}(t)=
 \{(\eta,J)\in\mathscr A_{\rm loc}^{\circ}:
                         J\cap\mathcal P_t=\varnothing\}.   \tag{H.11.3b}
\]

The local profile is now the explicit finite sum

\[
 \boxed{L_{s,j}(t)=
   \sum_{(\eta,J)\in\mathscr A_{\rm loc}(t)}
             \eta\,\mathfrak I_{s,t}(J).}                  \tag{H.11.3}
\]

This is exactly the signed sum of the ten matching entries and the six
matching-minus-path pairs, with every punctured entry removed.
The complete, unpunctured sum

\[
 \Omega_{s,j}=
   \sum_{(\eta,J)\in\mathscr A_{\rm loc}^{\circ}}
             \eta\,\mathfrak I^{\circ}_{s,t}(J)           \tag{H.11.3c}
\]

is independent of \(t\).  Here \(\mathfrak I^{\circ}\) is defined by
(H.1.10) using the full graph \(\widetilde B_r\), before requiring
\(J\cap\mathcal P_t=\varnothing\).  Translation of cut positions is a
bijection of placements, target tuples, and label assignments, proving the
independence.

We next make the supplier classification literal.  A tagged central target
\(T=(\sigma,I_{s_\sigma}(u))\), \(s_M=r,s_L=r-1\), has an oriented boundary
edge with

\[
 \operatorname{st}_t(T)=-2(u-t),\qquad
 \operatorname{en}_t(T)=-2(u+s_\sigma-t)\pmod b.           \tag{H.11.4a}
\]

For every entry \((\eta,J)\) in (H.11.3a), exactly one edge of \(J\) is
incident with each of the roots \(0,5\): this is immediate for a matching,
and in each of the six paths the roots are its endpoints.  That unique edge
is the **supplier** at the root.  Give it type \(S\) when the root is its
start endpoint in (H.11.4a), and type \(E\) when the root is its end endpoint.
For \(\alpha,\beta\in\{S,E\}\), define

\[
 F_{s,\alpha\beta}=
 \sum_{\substack{(\eta,J)\in\mathscr A_{\rm loc}^{\circ}\\
        \text{supplier types at }(0,5)=(\alpha,\beta)}}
       \eta\,\mathfrak I^{\circ}_{s,t}(J).                 \tag{H.11.4b}
\]

Equations (H.11.3c)--(H.11.4b) give

\[
 \Omega_{s,j}=F_{s,SS}+F_{s,SE}+F_{s,ES}+F_{s,EE}.          \tag{H.11.4c}
\]

For clarity about the sign under reflection, after multiplication by
\(\varepsilon(z)\) the harmonic factor is

\[
 \varepsilon(z)H_j(z\underline S)=
 \prod_{i=1}^j
 \bigl(\mathbf1_{\{u_i\in\underline S\}}-
       \mathbf1_{\{v_i\in\underline S\}}\bigr),           \tag{H.11.4d}
\]

where \(u_i\) and \(v_i\) are respectively the inside and outside
positions of event pair \(i\).  Thus it depends only on the oriented split,
not on the names of the two distinguished labels.  The reflection
\(a\mapsto5-a\) bijects the local entries and their placement sums,
preserves Venn-cell factorials and the sign \((-1)^{|J|}\), and reverses
the start/end role at both suppliers while exchanging the two roots.
Consequently

\[
                              F_{s,SS}=F_{s,EE}.             \tag{H.11.4e}
\]

At \(t=0\),
\(\mathcal P_0=\{\{0,1\},\{0,3\}\}\) consists precisely of the two
possible start suppliers at root \(0\).  Since a local entry has a unique
supplier there, no entry contains both punctured edges, and hence

\[
 \Omega_{s,j}-L_{s,j}(0)=F_{s,SS}+F_{s,SE}.                 \tag{H.11.5a}
\]

Since \(2\ell\equiv5\pmod b\), at \(t=\ell=r+3\) the two punctured edges
are \(\{5,6\},\{5,8\}\), the two possible start suppliers at root \(5\):

\[
 \Omega_{s,j}-L_{s,j}(\ell)=F_{s,SS}+F_{s,ES}.              \tag{H.11.5b}
\]

At \(t=3\), the punctured edges \(\{6,7\},\{6,9\}\) occur in no local
entry listed in (H.11.1), so

\[
                              L_{s,j}(3)=\Omega_{s,j}.       \tag{H.11.5c}
\]

Adding (H.11.5a)--(H.11.5b) and using (H.11.4c)--(H.11.4e) gives

\[
 \boxed{L_{s,j}(0)+L_{s,j}(\ell)=L_{s,j}(3).}               \tag{H.11.6}
\]


For arbitrary \(x,y\in\mathbb R\), put
\(p_t=xL_{r,j}(t)+yL_{r-1,j}(t)\) and \(e_t=1-p_t\).
Equation (H.11.6) gives \(e_0+e_\ell-e_3=1\), so
Cauchy--Schwarz yields
\[
 \boxed{{1\over b}\min_{x,y}\sum_{t\in\mathbb Z_b}
 (1-xL_{r,j}(t)-yL_{r-1,j}(t))^2\ge {1\over3b}.}           \tag{H.11.7}
\]

Appendix H.15.3 defines the complementary indexed remote family and proves
\[
 \omega_{Z_s}(t)=L_{s,j}(t)+R_{s,j}(t),\qquad
 |R_{s,j}(t)|=O(D_M/r^2),\qquad
 |R_{r,j}(t)-R_{r-1,j}(t)|=O(jD_M/r^3).                    \tag{H.11.8}
\]
Thus the local affine gap is rigorous, but these remote bounds do not
produce the compatible all-depth positive cover required by Gate B.

## H.14 Uniform all-depth conditioning of the sixteen-atom bank [I]

Put \(b=2r+1\),
\[
 K=r-4,\qquad \Lambda=r+1,\qquad m=j-2,
 \qquad D_M=2r\,r!(r+1)! .                              \tag{H.14.1}
\]
Use the two-pair harmonic projection and the sixteen signed local profiles
\(L_{s,j}(t)\), \(s\in\{r,r-1\}\), defined in H.1 and H.11. Thus the
blocker graph is
\(\Gamma_r=\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\})\), the event
roots are \(0,5\), the sixteen supports are
\(\{0,5,x,y\}\) with
\(x\in\{-3,-1,1,3\}\), \(y\in\{2,4,6,8\}\), and each support contributes
its endpoint matching, minus its full three-edge path when the connector is
present. The six connector pairs are
\[
 (-1,2),(1,2),(1,4),(3,2),(3,4),(3,6).                 \tag{H.14.2}
\]
Terms using either puncture edge
\(\{2t,2t+1\},\{2t,2t+3\}\) are omitted. If
\(\widehat L_{s,j}(t)\) denotes the corresponding unaveraged signed
injection sum, then the boundary average in H.1 is
\[
 L_{s,j}(t)={\widehat L_{s,j}(t)\over(K)_m(\Lambda)_m}.     \tag{H.14.3}
\]
Indeed the \(2^j\) orientations contribute equally after multiplication by
the two harmonic signs and cancel the \(2^j\) in \(|\mathcal B_t|\).
Define the \((2r+1)\)-by-two normalized profile matrix
\[
 (\mathsf A_{r,j})_{t,s}
 ={L_{s,j}(t)\over D_M}
 ={\widehat L_{s,j}(t)\over D_M(K)_m(\Lambda)_m},
 \quad t\in\mathbb Z_b, s\in\{r,r-1\}.                \tag{H.14.3a}
\]

### Theorem H.14.1

For every \(r\ge9\) and \(2\le j\le r-2\),
\[
                 \boxed{\sigma_{\min}(\mathsf A_{r,j})\ge r^{-29}.}
                                                                    \tag{H.14.4}
\]

### Proof

At \(t=3\) neither puncture meets a local atom. Take the two exact defects
\[
 C_{1,s,j}=L_{s,j}(3)-L_{s,j}(r+1),\qquad
 C_{2,s,j}=L_{s,j}(3)-L_{s,j}(r+2).                      \tag{H.14.5}
\]
Writing \((q,a)\) for the rank-\(q\) cyclic interval starting at \(a\),
comparison with the unpunctured bank leaves exactly these four deleted
three-blocker paths:
\[
\begin{array}{c|c|c}
 &\text{first}&\text{second}\\ \hline
C_1&\{(r-1,r),(r,0),(r,r+1)\}&
     \{(r-1,0),(r,r-1),(r,r+1)\}\\
C_2&\{(r-1,r+2),(r,0),(r,r)\}&
     \{(r-1,0),(r-1,r+2),(r,b-1)\}.
\end{array}                                               \tag{H.14.6}
\]
Hence no remote expansion enters these rows.

After the two marked boundary pairs are removed, the normalized signed
injection average of the remaining \(m\) event pairs, when a root has
\(a\) available inside and \(c\) available outside positions, is
\[
 e_m(a,c)=\sum_{h=0}^m(-1)^{m-h}{m\choose h}
 { (a)_h\over(K)_h}{(c)_{m-h}\over(\Lambda)_{m-h}},
 \qquad |e_m(a,c)|\le1.                                  \tag{H.14.7}
\]
The formula follows by choosing the \(h\) pairs whose selected endpoint is
inside and placing all constrained endpoints first. The bound follows
because this is an average of products from \(\{-1,0,1\}\).

Let \(P(a)=(K+1-a)(a+1)\). After division by \(D_M\), the coefficient of
\(e_m(a,s-2-a)\) in the four defect/shore combinations is
\[
\begin{array}{c|c}
G_{1,r}(a)&q_1P(a)+u_1\mathbf1_{a=K}\\
G_{2,r}(a)&q_2P(a)+u_2\mathbf1_{a=K}\\
G_{1,r-1}(a)&q_1P(a)+v_1\mathbf1_{a=K}\\
G_{2,r-1}(a)&q_2P(a)+w_2\mathbf1_{a=K-1}+v_2\mathbf1_{a=K},
\end{array}                                               \tag{H.14.8}
\]
where
\[
\begin{aligned}
q_1&={4(r+2)(2r-3)\over r^3(r-3)(r-2)(r-1)(r+1)},&
u_1&=-{2r-3\over r^3(r-1)(r+1)},\\
q_2&={2(4r^2+6r-15)\over r^3(r-3)(r-2)(r-1)(r+1)},&
u_2&=-{4r-5\over r^3(r-1)(r+1)},\\
v_1&=-{(r+4)(4r^2-13r+8)\over2r^3(r-2)(r-1)(r+1)},&
w_2&=-{(r-4)(4r-5)\over r^3(r-2)(r-1)(r+1)},\\
v_2&=-{4r^3+3r^2-36r+30\over2r^3(r-2)(r-1)(r+1)}.&&
\end{aligned}                                             \tag{H.14.9}
\]
This finite count uses no interpolation. For a blocker triple with Boolean
cell sizes \(c_\eta\) and root occupancies \(u_\eta\), compatible
bijections have weight
\(N_{s,J}(u)\prod_\eta u_\eta!(c_\eta-u_\eta)!\). Up to cell permutation,
the four triples in (H.14.6) have vectors
\[
 (0,1,r,0,2,r-2,0,0),\quad
 (0,r-1,2,0,2,0,r-2,0),\quad
 (3,0,r-2,0,0,r-1,1,0).                                 \tag{H.14.10}
\]
The first two types have \(2b-6\) retained positional tuples and the last
has \(2b-5\). Insert the four marks, sum the \(2r\) retained root starts,
and cancel factorials against \(D_M\). This gives the common quadratic for
\(a<K\); only \(a=K-1,K\) lose starts, giving exactly (H.14.9).

It remains to close the quadratic Hahn sums. Set
\[
 S_d=\sum_{a=0}^KP(a)e_m(a,K+d-a)\quad(d=1,2),             \tag{H.14.12}
\]
and
\[
 E_1=e_m(K,1)={\Lambda-m\over\Lambda},\quad
 E_2=e_m(K,2)={ (\Lambda-m)(\Lambda-m-1)\over\Lambda(\Lambda-1)},
                                                                  \tag{H.14.13}
\]
\[
 E_{12}=e_m(K-1,2)
 ={(\Lambda-m)(K\Lambda-Km-K-\Lambda m+m^2-m)
    \over K\Lambda(\Lambda-1)}.                         \tag{H.14.14}
\]
These sums have no hidden limiting step. Expand (H.14.7), write
\((a)_h(K+d-a)_q=h!q!{a\choose h}{K+d-a\choose q}\), and apply
Vandermonde after expanding the quadratic \(P(a)\) in falling factorials.
For \(d=1\) the omitted endpoint has weight zero; for \(d=2\) the two
omitted endpoints have weights zero and \(-(K+3)\). This finite identity
evaluates (H.14.12) as a rational function of \(r,m\) and yields the
matrix and factorization below by direct collection.

The normalized two-by-two defect matrix is therefore
\[
 \mathsf B_{r,j}=
 \begin{pmatrix}
 q_1S_2+u_1E_2&q_1S_1+v_1E_1\\
 q_2S_2+u_2E_2&q_2S_1+w_2E_{12}+v_2E_1
 \end{pmatrix}.                                          \tag{H.14.18}
\]
Let \(x=r-m-4\ge0\). Substitution gives
\[
 \det\mathsf B_{r,j}
 ={(r-m)(r-m+1)^2\Phi_m(x)\over\mathcal D(r,m)},          \tag{H.14.19}
\]
where
\[
\mathcal D=r^8(2r-m)(m+1)(m+2)(m+3)(r-2)(r-1)^2
(r+1)^4(2r-m-1)(2r-m+1).                                 \tag{H.14.20}
\]
The numerator has these four exhaustive forms:
\[
\begin{aligned}
\Phi_0(x)&=2(x+4)^2(2x+7)(2x+9)H_0(x),\\
H_0(x)&=40x^4+485x^3+1977x^2+3308x+1950,\\
\Phi_2(x)&=4(x+5)(2x+9)(2x+11)H_2(x),\\
H_2(x)&=40x^5+1245x^4+13508x^3+67422x^2+158710x+143316.
\end{aligned}                                             \tag{H.14.21}
\]
For odd \(m\),
\[
 \Phi_m(x)=-(m+1)(m+3)(m+2x+8)H_o(m,x),                  \tag{H.14.22}
\]
\[
\begin{aligned}
H_o={}&4m^8+(36x+119)m^7+(136x^2+912x+1467)m^6\\
&+(280x^3+2846x^2+9299x+9834)m^5\\
&+(340x^4+4628x^3+22901x^2+49207x+39053)m^4\\
&+(244x^5+4135x^4+27343x^3+88945x^2+143584x+92750)m^3\\
&+(96x^6+1924x^5+15810x^4+68904x^3+169743x^2
   +225672x+126443)m^2\\
&+(16x^7+364x^6+3544x^5+19526x^4+66867x^3
   +142873x^2+173845x+90190)m\\
&+8x^6+249x^5+2755x^4+14656x^3+40322x^2+54490x+27840.
\end{aligned}                                             \tag{H.14.23}
\]
For even \(m\ge4\), put \(y=m-4\); then
\[
 \Phi_m(x)=-(y+6)(2x+y+11)(2x+y+13)H_e(y,x),              \tag{H.14.24}
\]
\[
\begin{aligned}
H_e={}&(8y^2+48y+24)x^6
 +(44y^3+606y^2+2084y+651)x^5\\
&+(100y^4+2191y^3+15770y^2+38654y+10423)x^4\\
&+(120y^5+3632y^4+40713y^3+202416y^2+396813y+120432)x^3\\
&+(80y^6+3098y^5+47527y^4+362939y^3+1401929y^2
   +2359307y+852174)x^2\\
&+(28y^7+1322y^6+25825y^5+267951y^4+1569184y^3
   +5028592y^2+7582719y+3125836)x\\
&+4y^8+223y^7+5301y^6+69776y^5+551539y^4
   +2644354y^3+7324827y^2+10144976y+4525360.
\end{aligned}                                             \tag{H.14.25}
\]
Every coefficient in \(H_0,H_2,H_o,H_e\) is positive. Thus
\(\det\mathsf B_{r,j}\ne0\). Its numerator in (H.14.19) is a nonzero
integer, every denominator factor is positive, and for
\(r\ge9,0\le m\le r-4\),
\[
 \mathcal D(r,m)\le512r^{21},\qquad
 |\det\mathsf B_{r,j}|\ge r^{-24}.                        \tag{H.14.26}
\]
Indeed \(r^3\ge512\). Also (H.14.7)--(H.14.9) imply
\(|S_d|\le\sum_aP(a)\le r^3\), every entry of \(\mathsf B\) has
absolute value at most \(2r^3\), and
\[
 \|\mathsf B_{r,j}\|_F\le4r^3,\qquad
 \sigma_{\min}(\mathsf B_{r,j})\ge{1\over4r^{27}}.       \tag{H.14.27}
\]
Let \(T\) take the two row differences in (H.14.5). Then
\(TT^{\mathsf T}=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\),
so \(\|T\|=\sqrt3\), and \(\mathsf B=T\mathsf A\). Hence
\[
 \sigma_{\min}(\mathsf A_{r,j})
 \ge{1\over4\sqrt3\,r^{27}}\ge r^{-29},                 \tag{H.14.28}
\]
proving the theorem. \(\square\)

The theorem is local. Together with H.11 it removes the local
harmonic-depth and rank-two conditioning issue; it does not transfer the
inverse to the complete zero-avoidance exposure. In normalized units the
known absolute remote error \(O(r^{-2})\) can exceed the deliberately
crude \(r^{-29}\) inverse.


## H.15 A shore-difference current bound for the remote tail [I]

Assume \(r\ge6\) and \(2\le j\le r-2\), as in H.1 and H.11.
For this fixed \(j\), \(R_s(t)\) below abbreviates \(R_{s,j}(t)\), which is
defined explicitly in (H.15.3.2c).

**Status.**  This note proves a shore-adapted estimate for every blocker
set, before inclusion--exclusion is summed.  It improves the factor `2r` in
the usual rooted-current bound to `2j` after subtracting the middle and
lower shores.  Applied to the complete remote zero-avoidance tail outside the 22 signed
local terms of H.11, it gives

\[
 \boxed{|R_r(t)-R_{r-1}(t)|\le CjD_Mr^{-3},\qquad
        |R_s(t)|\le CD_Mr^{-2}.}                              \tag{H.15.0.1}
\]

Equivalently, the remote vector has ambient radius `O(D_M/r^2)` and
transverse distance `O(jD_M/r^3)` from the common-shore line. This is an
absolute directional statement; it does not assert a relative angle when
the common component vanishes, and it does not prove Gate B.

#### H.15.1 Configurations and currents

Put `b=2r+1`.  A word `w=(w_0,...,w_(b-1))` defines cyclic windows

\[
 I_s^w(a)=\{w_a,w_{a+1},\ldots,w_{a+s-1}\},
 \qquad a\in\mathbb Z_b,                                    \tag{H.15.1.1}
\]

with indices read modulo `b`.  Its directed punctured configuration is

\[
 E(w)=\{(M,I_r^w(a)):a\ne0\}\mathbin{\dot\cup}
      \{(L,I_{r-1}^w(a)):a\ne0\}.                            \tag{H.15.1.2}
\]

Fix `j` disjoint ordered label pairs `(a_i,b_i)`.  On an `s`-set put

\[
 H_{s,j}(S)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in S\}}-\mathbf1_{\{b_i\in S\}}),        \tag{H.15.1.3}
\]

and define the shore current of one configuration by

\[
 K_s(w)=\sum_{a=1}^{b-1}H_{s,j}(I_s^w(a)),
 \qquad s\in\{r,r-1\}.                                     \tag{H.15.1.4}
\]

For a set `J` of prescribed tagged targets, let

\[
 \deg(J)=|\{w:E(w)\supseteq J\}|,
 \qquad
 \Omega_s(J)=\sum_{w:E(w)\supseteq J}K_s(w).                \tag{H.15.1.5}
\]

The same definitions may be made after relabelling all targets and all
distinguished pairs, and may then be averaged with arbitrary coefficients
of absolute value at most one.  In particular they include the signed
boundary-event profiles used in the zero-avoidance quotient.

#### H.15.2 The pointwise shore coupling

##### Theorem H.15.2.1

For every word `w` and every choice of the `j` distinguished pairs,

\[
                         \boxed{|K_r(w)-K_{r-1}(w)|\le2j.}   \tag{H.15.2.1}
\]

Consequently, for every blocker set `J`,

\[
 \boxed{|\Omega_r(J)-\Omega_{r-1}(J)|\le2j\deg(J),\qquad
        |\Omega_s(J)|\le2r\deg(J).}                         \tag{H.15.2.2}
\]

#### Proof

Pair the two windows at the same retained start.  They are nested and
differ in exactly one label:

\[
 I_r^w(a)=I_{r-1}^w(a)\mathbin{\dot\cup}\{w_{a+r-1}\}.
                                                                    \tag{H.15.2.3}
\]

The product (H.15.1.3) depends only on membership of the `2j` distinguished
labels.  Therefore the two summands at start `a` agree unless
`w_(a+r-1)` is distinguished.  If it is distinguished, only one factor in
(H.15.1.3) changes, by one, while every other factor lies in `{-1,0,1}`; the
absolute change of the product is at most one.  As `a` runs through the
retained starts, each label occurs as `w_(a+r-1)` at most once.  At most
`2j` summands can therefore change, proving (H.15.2.1).

Sum (H.15.2.1) over the `deg(J)` words containing `J` to obtain the first
inequality in (H.15.2.2).  Each shore has `b-1=2r` retained starts and every
summand in (H.15.1.4) has absolute value at most one, which proves the second.
\(\square\)

##### Corollary H.15.2.2 (signed families and boundary averaging)

Let `A` be any finite family of blocker sets, let `|c_J|<=1`, and let

\[
 T_s=\sum_{J\in A}c_J\Omega_s(J),\qquad
 \mathcal M(A)=\sum_{J\in A}\deg(J).                        \tag{H.15.2.4}
\]

Then

\[
 |T_s|\le2r\mathcal M(A),\qquad
 |T_r-T_{r-1}|\le2j\mathcal M(A).                           \tag{H.15.2.5}
\]

The same inequalities hold if every current is first averaged over a
probability space and multiplied by a sign of modulus one.

#### Proof

Apply (H.15.2.2), the triangle inequality, and then Jensen's inequality for the
optional average. \(\square\)

#### H.15.3 The complete remote zero-avoidance tail

We record the application without suppressing its counting input.  After
the standard multiplication of cut labels by `-2 modulo b`, the blocker
graph is

\[
 \widetilde B_r=\operatorname {Cay}(\mathbb Z_b,\{\mathord\pm1,
                                      \mathord\pm3\}),\qquad
 \mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\},\qquad
 B_r(t)=\widetilde B_r\setminus\mathcal P_t.       \tag{H.15.3.1}
\]

Define the complete indexed blocker family surviving the puncture by

\[
 \mathscr A_{\rm all}(t)=
 \left\{\bigl((-1)^{|J|},J\bigr):
 J\subseteq E(B_r(t)),\ \{0,5\}\subseteq V(J)\right\}.     \tag{H.15.3.2a}
\]

Regard \(\mathscr A_{\rm loc}(t)\) from (H.11.3b) as the corresponding
submultiset of (H.15.3.2a), and put

\[
 \mathscr A_{\rm rem}(t)=
       \mathscr A_{\rm all}(t)\setminus
       \mathscr A_{\rm loc}(t),                           \tag{H.15.3.2b}
\]

\[
 \boxed{R_{s,j}(t)=
 \sum_{(\eta,J)\in\mathscr A_{\rm rem}(t)}
                  \eta\,\mathfrak I_{s,t}(J).}             \tag{H.15.3.2c}
\]

The subtraction in (H.15.3.2b) is literal: on each of the ten matching-only
supports it removes the matching; on each of the six path supports it
removes both the endpoint matching and the full path.  There are no other
four-vertex edge subsets incident with both roots.  Indeed the two roots
have disjoint neighbour sets; choosing one neighbour of each gives the
sixteen supports in (H.11.1).  On ten supports the two supplier edges are
the only induced edges.  On the remaining six the sole additional edge is
the connector, so the only edge subsets incident with all four vertices
are the matching and the full path.

By (H.1.11) and the root cancellation (H.1.15), every surviving
inclusion--exclusion term belongs to exactly one of (H.11.3b) and
(H.15.3.2b).
Therefore

\[
 \boxed{\omega_{Z_s}(t)=L_{s,j}(t)+R_{s,j}(t).}              \tag{H.15.3.2d}
\]

It remains to bound the unsigned remote mass

\[
 \mathcal M_{\rm rem}(t)=
       \sum_{(\eta,J)\in\mathscr A_{\rm rem}(t)}\deg_t(J).
                                                                    \tag{H.15.3.2e}
\]

For every such \(J\), the boundary-codegree theorem gives

\[
 \deg_t(J)\le D_M C_0^{|J|}r^{\,2-|V(J)|}.                \tag{H.15.3.2}
\]

Here is the complete summation.  Decompose \(J\) into connected
components.  Its rooted part is the union of the one or two components
meeting \(0\) or \(5\).  A maximum-degree-four exploration from a fixed
root has at most \(A_0^m\) connected \(m\)-edge shapes.  If one rooted
component contains both roots, then a four-vertex possibility is one of
the six local paths; every nonlocal possibility has at least five vertices.
If the roots lie in separate components, the only four-vertex possibility
is a pair of disjoint supplier edges, one of the ten local matchings;
otherwise the rooted part again has at least five vertices.  Together with
\(m\le2(v-1)\), this shows that the total weight in (H.15.3.2) of a nonlocal
rooted part is \(O(D_Mr^{-3})\): the finitely many small \(m\) have
\(v\ge5\), while the remaining terms are bounded by a geometric series in
\(A_0C_0/\sqrt r\).

A connected component meeting neither root, with \(m\) edges and \(v\)
vertices, has at most \(bA_0^m\) placements.  Its activity after removal of
the common factor \(D_Mr^2\) is
\(C_0^m r^{-v}\).  The one-edge total is \(O(1/r)\); the two- and
three-edge totals are smaller by triangle-freeness; and
\(m\le2(v-1)\) makes all \(m\ge4\) terms a convergent geometric tail.
Thus the total unrooted connected activity is \(O(1/r)\), and allowing any
unordered family of such components multiplies a rooted contribution by
at most \(\exp(O(1/r))\).  Finally, if the rooted part is one of the local
four-vertex entries but \(J\) is remote because it has an additional
component, the nonempty additional family contributes the extra factor
\(O(1/r)\).  Hence, uniformly in \(t\),

\[
 \boxed{\mathcal M_{\rm rem}(t)\le C D_Mr^{-3}.}             \tag{H.15.3.3}
\]

Apply (H.1.13) termwise to (H.15.3.2c) and then (H.15.3.3):

\[
 \boxed{|R_{s,j}(t)|\le C D_Mr^{-2},\qquad
 |R_{r,j}(t)-R_{r-1,j}(t)|\le CjD_Mr^{-3}.}                 \tag{H.15.3.4}
\]

In common/transverse coordinates

\[
 R_+(t)={R_r(t)+R_{r-1}(t)\over2},\qquad
 R_-(t)={R_r(t)-R_{r-1}(t)\over2},                          \tag{H.15.3.5}
\]

the conclusion is

\[
 |R_+(t)|=O(D_M/r^2),\qquad
 |R_-(t)|=O(jD_M/r^3).                                      \tag{H.15.3.6}
\]

Thus its transverse distance from the common-shore line is
`O(jD_M/r^3)` inside an ambient radius `O(D_M/r^2)`. For `j` comparable
with `r`, (H.15.3.6) gives no improvement over the absolute estimate.

#### H.15.4 Scope

The theorem is exact before blocker summation and is independent of the
number of blocker components. It controls the shore difference at every
fixed harmonic depth, but it neither controls cancellation along the
common-shore line nor proves the Gate-B cover.  These estimates do not construct the compatible all-depth positive cover
required by Gate B in Section 5 and C.10.

## H.15A Exact \(j=2\) six-vertex rooted-core determinant [I]

Put
\[
 b=2r+1,\qquad
 \Gamma_r=\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\}),
 \qquad p=0,\quad q=5,\quad D_M=2r\,r!(r+1)!.            \tag{H.15A.1}
\]
At event shift \(t\), puncture
\(\mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\}\). An edge set \(J\) is
**rooted** if \(\{p,q\}\subseteq V(J)\), \(|V(J)|\le6\), and every
connected component of \(J\) contains \(p\) or \(q\). Edges of cyclic
length one and three carry, respectively, the original rank-\(r\) and
rank-\((r-1)\) interval tags. Let
\(C_s^{(6)}(t)\) be the signed \(j=2\) harmonic contribution on shore
\(s\in\{r,r-1\}\) of rooted sets using at least one edge restored from
\(\mathcal P_t\), with inclusion--exclusion sign \((-1)^{|J|}\). The
complete rooted sum is translation invariant, so
its retained profile satisfies
\[
 L_s^{(6)}(u)-L_s^{(6)}(t)=C_s^{(6)}(t)-C_s^{(6)}(u).       \tag{H.15A.2}
\]
Define
\[
 X_s={C_s^{(6)}(r)-C_s^{(6)}(r+1)\over D_M},\qquad
 Y_s={C_s^{(6)}(r+2)-C_s^{(6)}(r+3)\over D_M},             \tag{H.15A.3}
\]
\[
 \mathsf M_r^{(6)}=\begin{pmatrix}X_r&X_{r-1}\\Y_r&Y_{r-1}\end{pmatrix}.
                                                                    \tag{H.15A.4}
\]

### Theorem H.15A.1

For every \(r\ge23\),
\[
 \boxed{\det\mathsf M_r^{(6)}={P(r)\over12Q(r)^2}>0,\qquad
 \det\mathsf M_r^{(6)}\ge2^{-187}r^{-6},}                \tag{H.15A.5}
\]
and
\[
 \det\mathsf M_r^{(6)}={4\over3}r^{-6}-6r^{-7}
 +{1169\over12}r^{-8}+O(r^{-9}).                          \tag{H.15A.6}
\]

### Proof

For an ordered blocker tuple, index Boolean cells by \(\eta\). Let
\(c_\eta\) be the cell size, \(m_\eta\) the number of the four event
labels in it, and \(u_\eta\) the root-interval occupancy of the
corresponding positional cell. If \(\sigma\) chooses one label from each
event pair, with product sign \(\operatorname{sgn}\sigma\), and
\(h_\eta(\sigma)\) selected labels lie in cell \(\eta\), then the exact
signed bijection weight is
\[
\begin{aligned}
&\sum_\sigma\operatorname{sgn}(\sigma)
 \prod_\eta {c_\eta-m_\eta\choose u_\eta-h_\eta(\sigma)}
 u_\eta!(c_\eta-u_\eta)!\\
&\quad=\prod_\eta(c_\eta-m_\eta)!
 \sum_\sigma\operatorname{sgn}(\sigma)
 \prod_\eta(u_\eta)_{h_\eta(\sigma)}
 (c_\eta-u_\eta)_{m_\eta-h_\eta(\sigma)}.
\end{aligned}
\tag{H.15A.7}
\]
Thus, after common factorials are removed, the marked-label factor has
degree four. Fix the first positional blocker at relative start zero. If
the other starts and root start are \(d_1,\ldots,d_a,u\), exactly
\[
 b-|\{0,-d_1,\ldots,-d_a,-u\}|                            \tag{H.15A.8}
\]
translates retain every displayed start.

For \(r\ge23\), five \(\{\pm1,\pm3\}\)-steps from \(\{0,5\}\) lift
without modular collision. Under the inverse cut relabelling
\[
 \phi_r(2h)=-h,\qquad \phi_r(2h+1)=r-h\pmod b,            \tag{H.15A.9}
\]
even and odd cuts form two bounded clusters. Every blocker joins opposite
parities, so its two complementary long gaps have different membership
vectors. Every Venn signature therefore has exactly two macroscopic cells,
of sizes \(r+a,r+c\), with all remaining cells bounded.

There are twenty macroscopic-factor types. For each, factor the two
macroscopic factorials and the bounded-cell factorials in (H.15A.7).
The remaining coefficient has degree at most six: four from
(H.15A.7), one from (H.15A.8), and at most one from summing the
piecewise-polynomial root start. Expanding these twenty explicitly gives
\[
 Q(r)=(r-7)(r-6)\prod_{h=1}^5(r-h)^2r^3(r+1),              \tag{H.15A.10}
\]
and, with \(x=r-23\),
\[
 P(r)=\sum_{i=0}^{26}a_ix^i,                              \tag{H.15A.11}
\]
where the coefficients in increasing order are
\[
\begin{aligned}
(a_0,\ldots,a_{26})={}&(
62981083599956614478115107174154240,
83731019301859283369193624773455872,\\
&53503167323082065050576460728060416,
21874508927965046394283771602943488,
6426381234586609560264944170832256,\\
&1444365103196196379308996566942592,
258170481804935360887224705464448,
37662599276106501292922749610480,\\
&4566280031383604538889761516544,
466127777416902336699609774388,
40438710544492245034672425456,\\
&3001278408729229165219406704,
191400833973788705746237666,
10515008159209256633718591,\\
&498043778207751522889761,
20322149467297451253335,
712577696918492023585,\\
&21377614697429068690,
545129461736876970,
11706023019295518,
208959527775844,\\
&3045080777091,35300366213,313170763,1997129,8152,16).
\end{aligned}                                             \tag{H.15A.12}
\]
Equations (H.15A.7)--(H.15A.9) are an exact finite evaluator for every
term; collecting its twenty types gives
\(\det\mathsf M_r^{(6)}=P(r)/(12Q(r)^2)\). Every coefficient in
(H.15A.12) and every denominator factor is positive for \(r\ge23\),
proving the sign. Exact division also gives (H.15A.6).

For the uniform bound, \(P(r)\ge16(x^{26}+1)\ge
2^{-21}(x+1)^{26}\), while \(x+1=r-22\ge r/23\),
\(23^{26}<2^{130}\), every one of the sixteen linear factors of \(Q\)
is at most \(2r\), and \(12<2^4\). Substitution in (H.15A.5) gives
\(\det\mathsf M_r^{(6)}\ge2^{-187}r^{-6}\). \(\square\)

The theorem controls only the explicitly rooted family and makes no
assertion about adjoining components meeting neither root.  That rootless
dressing remains part of Gate B.

## H.16 Venn-gap localization [I]

Let \(\varnothing\ne J\subseteq E_0\) be a finite set of canonical tagged central
targets, and let \(\deg(J)\) be the number of directed punctured
configurations containing them. Their standard interval presentations in
(H.1.2) give canonical boundary cuts. List the distinct cuts cyclically,
form their positive cyclic gaps, reorder that multiset as
\(g_1\ge g_2\ge\cdots\ge g_q\), and put
\(\delta=\sum_{i=3}^qg_i\). The proved estimate is

\[
 \boxed{{\deg(J)\over D_M}
 \le32^{|J|-1}{r+2\over
  (\delta+1){r\choose\delta+1}}}
 \qquad(0\le\delta\le r-2).                         \tag{H.16.1}
\]


### H.16.1 Venn-gap localization

Let `J subseteq E_0` contain `t>=1` canonical tagged central targets.  Write

\[
 \deg(J)=|\{w:E(w)\supseteq J\}|,
\]

where `E(w)` is the directed punctured configuration of the cyclic word
`w`; thus each of its middle and lower targets has nonzero start.  List the `q>=2` distinct original cut positions of `J` in cyclic order and
call the resulting positive gaps `d_1,...,d_q`. Reorder this gap multiset
nonincreasingly as

\[
                         g_1\ge g_2\ge\cdots\ge g_q,
 \qquad\sum_i g_i=b,                                       \tag{H.16.2}
\]

and define

\[
                         \delta=\sum_{i=3}^qg_i.             \tag{H.16.3}
\]

#### Theorem H.16.1

If `0<=delta<=r-2`, then (H.16.1) holds.

#### Proof

Fix an anchor target.  A second central interval with prescribed length and
intersection has at most four possible relative starts.  Hence the number
of retained positional target tuples with the labelled Venn signature of
`J` is at most

\[
                         (b-1)4^{t-1}.                       \tag{H.16.4}
\]

If the labelled Venn-cell sizes are `n_tau`, compatible labels contribute
`V(J)=prod_tau n_tau!`.  Put `G(J)=prod_i g_i!`.  Refining the cells one
interval at a time gives

\[
                         V(J)\le8^{t-1}\prod_{i=1}^qg_i!.    \tag{H.16.5}
\]

Here is the full refinement argument.  Expose the targets one at a time and
write `R=V/G`.  If an old Venn cell of size `n` receives `a` labels of the
new target, its factorial contribution is multiplied by
`a!(n-a)!/n!=1/binom(n,a)`.  If a new cut splits an old elementary gap of
size `g` into `u,g-u`, the gap-factorial contribution is multiplied by
`1/binom(g,u)`.  When the two new cuts lie in different old gaps, choosing
the required labels independently in the split gaps injects into the
choice of the required labels in their containing Venn cells.  Hence the
product of the gap binomials is at most the product of the Venn-cell
binomials, and `R` cannot increase.  The same argument covers one new cut;
two old cuts can only decrease `V`.

If both new cuts lie in one old gap of size `g`, write the three pieces as
`x,y,z`, with `y` between the new cuts.  The gap-refinement factor is

\[
 {g!\over x!y!z!}={g\choose y}{g-y\choose x}.              \tag{H.16.5a}
\]

The middle piece has length `r` or `r-1`, or the complementary length.
The containing Venn-cell binomial cancels `binom(g,y)`.  Every old gap lies
inside one of the two arcs of the first exposed central target, so
`g<=r+2`.  Therefore `g-y<=3` in the first case and `g-y<=1` in the
complementary case.  The uncancelled factor in (H.16.5a) is at most
`2^(g-y)<=8`.  Thus each added target multiplies `R` by at most eight,
which proves (H.16.5).

Write `G=prod_i g_i!`.  Merging the gaps after the two largest gives
`prod_(i>=3)g_i!<=delta!`.  Every elementary gap is at most `r+2`.
Since `g_1+g_2=2r+1-delta` and `delta<=r-2`, factorial log-convexity moves
mass toward the larger gap and yields

\[
 G\le(r+2)!(r-1-\delta)!\,\delta!.                          \tag{H.16.6}
\]

The exact Venn count is the positional count times `V(J)`.  Divide
(H.16.4)--(H.16.6) by `D_M=(b-1)r!(r+1)!` and use

\[
 { (r+2)!(r-1-\delta)!\delta!\over r!(r+1)!}
 ={r+2\over(\delta+1){r\choose\delta+1}}.                  \tag{H.16.7}
\]

This proves (H.16.1). \(\square\)

For fixed `delta`, (H.16.1) is `O_t(delta! r^-delta)`.  A consequence needed
below avoids any assertion about the number of positions at fixed
`delta`.  Fix `t_0>=2` and a family of `O_(t_0)(1)` rooted boundary-graph
shapes, each incident with both event roots `{0,5}` and having at most `t_0-1` blocker edges;
to each realization adjoin one central blocker edge.  There are at most
`2b=O(r)` choices for that edge.  For
`7<=delta<=r/2`, the right side of (H.16.1) is largest at `delta=7`; hence the
sum over *all* edge positions is at most

\[
 O_{t_0}\left({r(r+2)\over8{r\choose8}}\right)
 =O_{t_0}(r^{-6}).                                         \tag{H.16.8}
\]

For `delta>r/2`, use the unsimplified bound (H.16.4)--(H.16.5).  Since
`q<=2t_0`, one has

\[
 g_3\ge {\delta\over q-2}\ge {r\over2(2t_0-2)},
 \qquad g_1,g_2\ge g_3.                                   \tag{H.16.9}
\]

Also every `g_i<=r+2`.  With `p_i=g_i/b`, the vectors `(p_i)` therefore
belong, up to `O(1/r)`, to the compact set

\[
 \sum p_i=1,qquad \max p_i\le {1\over2},qquad
 p_3\ge {1\over6(2t_0-2)}.
\]

Put `H(p)=-sum_i p_i log p_i`. This continuous function has a minimum
on the displayed compact set. Under `max p_i<=1/2`, its value is at
least `log 2`, with equality only at a permutation of
`(1/2,1/2,0,...)`; the lower bound on the third-largest coordinate
excludes every equality point. Hence `H(p)>=log 2+c_(t_0)` for some
`c_(t_0)>0`.  The integral comparisons
\(\int_1^n\log t\,dt\le\log(n!)\le\int_1^n\log t\,dt+\log n\) give
\(\log(n!)=n\log n-n+O(\log(n+1))\). Hence
\[
 \log{\prod_i g_i!\over r!(r+1)!}
 =-b\{H(p)-\log2\}+O_{t_0}(\log r),
\]
and therefore, uniformly in this range,

\[
 {\prod_i g_i!\over r!(r+1)!}
 \le \exp(-c'_{t_0}r).                                    \tag{H.16.10}
\]

The positional factor (H.16.4), the at most `2b` edge choices, and the
bounded number of rooted core types are polynomial and are absorbed by
the exponential.  Combining (H.16.8)--(H.16.10) proves

\[
 \sum_{\substack{J:\text{from the fixed core family}\\
                         \text{plus one edge},\ \delta(J)\ge7}}
 \deg(J)=O_{t_0}(D_Mr^{-6}).                               \tag{H.16.11}
\]

Multiplying by the current bound \(2r\) from (H.15.2.2) makes their normalized profile
contribution `O(r^-5)`.


The conclusion proved here is exactly this: after fixing
an \(O(1)\)-sized family of blocker-edge patterns incident with both event
roots, adjoining one further blocker edge with Venn-gap defect at least
seven has total normalized profile contribution \(O(r^{-5})\), after the
\(2r\) current factor. It does not sum arbitrary root-incident patterns,
two or more components disjoint from both roots, or the full
inclusion--exclusion series. These retained lemmas do not prove Gate B; the
missing output is the compatible all-depth positive cover stated in
Section 5 and C.10.

# Appendix I: Independent packet and coherent-tour selectors

This appendix contains only the Gate-C statements used by the live direct
route.  All ground sets and all target sets are labelled.  Throughout,
\(b\) is sufficiently large and odd, so \(H\le b-2\),
\[
 \lvert\Omega\rvert=2b,\qquad
 W=\binom{2b}{b},\qquad
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil .
 \tag{I.1}
\]
Thus \(H=o(b/\log b)\).

The results below have four roles.

1. Section 3.4 compiles each physical fragment independently.
2. Phase packets give exact integral hypercube banks and a distinct
   all-band selector gate.
3. Coherent tours and their linear cosets give large integral banks which
   are already disjoint at ranks \(b-1,b,b+1\).
4. The cosets may simultaneously have dual distance greater than \(H\);
   hence every bank has exact \(H\)-wise state balance.

The two independent selection gates \(C_{\rm Q}\) and \(C_{\rm F}\) are open.

## I.1 The set-valued band compiler

For a singleton word \(w\), write
\[
 I_s^w(a)=\{w_a,\ldots,w_{a+s-1}\}                    \tag{I.2}
\]
when those letters are distinct, and call the window clean. A physical
\(H\)-fragment has \(L\) consecutive designated starts whose windows are
clean for \(b-H\le s\le b+H\). For \(t\) fragments put
\[
 M=\sum L,\qquad \mathcal I_s=\{\text{their designated rank-\(s\)
 targets}\},\qquad h_s=\binom{2b}s-|\mathcal I_s|.     \tag{I.3}
\]
Apply 3.4 separately with \(\ell=b-H,u=b+H\), and use the far-rank word
from A.4. Its length \(R_{\rm far}=o(W)\) for the value of \(H\) in (I.1).
Thus
\[
\boxed{\nu(2b)\le M+2Ht+\sum_{s=b-H}^{b+H}h_s+
 R_{\rm far}.}                                        \tag{I.4}
\]
Consequently
\[
 M\le W+o(W),\qquad Ht=o(W),\qquad
 \sum_{s=b-H}^{b+H}h_s=o(W)                           \tag{I.5}
\]
imply \(\nu(2b)=(1+o(1))W\). No disjointness assumption is needed for
(I.4); selector applications use it only to bound \(M\) or repetition
excess. The same implication holds for any \(H=o(b)\) with
\(H/\sqrt b\to\infty\).

## I.1A Phase-packet banks and the separate-block gate

This section is independent of the coherent-tour coset construction below.
Keep the notation of I.1, assume \(b\ge5\) is odd, and put \(m=b-1\).

A labelled phase packet consists of distinct \(u,v\in\Omega\) and ordered
disjoint \(m\)-tuples

\[
 X=(x_1,\ldots,x_m),\qquad Y=(y_1,\ldots,y_m)
\]

whose entries partition \(\Omega-\{u,v\}\).  In the cyclic singleton word

\[
 z=(u,x_1,\ldots,x_m,y_1,\ldots,y_m)                 \tag{I.Q.1}
\]

on \(\Omega-\{v\}\), its distinguished middle targets are the \(b+1\)
length-\(b\) arcs

\[
 C_0=\{u\}\cup X,\qquad
 C_i=\{x_i,\ldots,x_m\}\cup\{y_1,\ldots,y_i\} (1\le i\le m),
 \qquad C_b=\{u\}\cup Y.                              \tag{I.Q.2}
\]

They are distinct. Indeed they are proper arcs of one odd cycle with
distinct labels; equal arcs would have equal boundary edges and hence equal
starts or be complementary, but complementary arcs have sizes \(b\) and
\(b-1\). Every cyclic arc of length at most \(2b-2\) is clean. Applying 3.4
to the \(b+1\) starts with \(\ell=b-H,u=b+H\) therefore turns each packet
into a separate set-valued block of exactly
\[
                         b+1+2H                       \tag{I.Q.2a}
\]
letters preserving every designated band window. No ordered joining is
needed. There are

\[
                    (2b)(2b-1)(2b-2)!=(2b)!           \tag{I.Q.3}
\]

labelled packets.

### Theorem I.Q.1 (exact packet profile) [I]

Every middle target has labelled packet degree

\[
                         D_{\rm pkt}=(b+1)(b!)^2.       \tag{I.Q.4}
\]

If two middle targets are at Johnson distance \(d\), their labelled
codegree is

\[
 \lambda_d=
 \begin{cases}
 \displaystyle {2(b+1-d)(b!)^2\over\binom bd^2},&1\le d\le b-2,\\[6pt]
 \displaystyle {6(b!)^2\over b^2},&d=b-1,\\
 0,&d=b.
 \end{cases}                                           \tag{I.Q.5}
\]

Consequently

\[
                    \boxed{{\Delta_2\over D_{\rm pkt}}
                    ={2\over b(b+1)}.}                 \tag{I.Q.6}
\]

#### Proof

Fix a middle target \(C\) and its position \(i\in\{0,\ldots,b\}\).  At
an endpoint, choose \(u\in C\), order the other \(b-1\) members, choose
\(v\notin C\), and order the other \(b-1\) outside members.  This gives
\(b^2((b-1)!)^2=(b!)^2\) labels.  At an internal position, split and order
the \(i\) entered and \(b-i\) surviving members of \(C\), in
\(\binom bi i!(b-i)!=b!\) ways; the complementary labels fill their
\(b\) ordered roles in \(b!\) ways.  Summing over positions proves
(I.Q.4).

For two distinct positions at ordinary separation \(d\), their targets
have Johnson distance \(d\).  The only exception is the endpoint pair
\(0,b\), whose intersection is \(\{u\}\), so its distance is \(b-1\).
For a fixed ordered position pair and a fixed first target, its stabilizer
is transitive on the \(\binom bd^2\) targets at distance \(d\).  The
contribution to a fixed ordered target pair is therefore
\((b!)^2/\binom bd^2\).  There are \(2(b+1-d)\) ordered position pairs at
separation \(d\), while distance \(b-1\) receives four pairs at separation
\(b-1\) and two endpoint pairs.  This proves (I.Q.5).  Since
\(\binom bd\ge b\) for \(1\le d\le b-1\), the first line is maximized at
\(d=1\); the exceptional normalized value \(6/[b^2(b+1)]\) is no larger.
This proves (I.Q.6). \(\square\)

### Theorem I.Q.2 (integral hypercube bank and adjacent loads) [I]

Fix \(u,v\), and partition \(R=\Omega-\{u,v\}\) into ordered pairs

\[
 P_i=\{a_i^0,a_i^1\},\qquad1\le i\le m.
\]

For \(x\in\mathbb F_2^m\), let
\(V(x)=\{a_i^{x_i}:1\le i\le m\}\), and put
\(p_i=e_1+\cdots+e_i\), \(p_0=0\).  For every even-weight \(x\), take the
packet

\[
 X=(a_1^{x_1},\ldots,a_m^{x_m}),\qquad
 Y=(a_1^{1-x_1},\ldots,a_m^{1-x_m}).                  \tag{I.Q.7}
\]

Let \(\mathcal B(P)\) be the \((m+1)\)-sets in \(R\) which double one
pair and split all the others.  These \(2^{m-1}\) packets satisfy:

1. their internal middle targets \(C_1,\ldots,C_m\) partition
   \(\mathcal B(P)\), so \(|\mathcal B(P)|=m2^{m-1}\);
2. every transversal \(V(z)\) occurs exactly \(m/2\) times among the
   same-start rank-\(m=b-1\) targets;
3. every boundary \(\{u\}\cup V(z)\) with even \(z\) occurs twice; and
4. at rank \(m+2=b+1\), every internal target which doubles consecutive
   pairs \(P_i,P_{i+1}\) and splits the others occurs twice, while every
   final target containing \(u\), doubling \(P_m\), and splitting the
   others occurs once.

#### Proof

The internal target at step \(i\) is the union of the two transversals at
the ends of the direction-\(i\) cube edge

\[
                  \{x+p_{i-1},x+p_i\}.                  \tag{I.Q.8}
\]

For fixed \(i\), translation by \(p_{i-1}\) sends the even shore
bijectively to one endpoint of every direction-\(i\) edge.  Varying \(i\)
partitions \(\mathcal B(P)\), proving part 1.

The rank-\(m\) target at that start is \(V(x+p_{i-1})\).  A fixed
\(V(z)\) occurs precisely when \(x=z+p_{i-1}\) is even, equivalently
\(|z|\equiv i-1\pmod2\).  Exactly \(m/2\) indices have either parity,
proving part 2.  The packet boundaries are
\(\{u\}\cup V(x)\) and \(\{u\}\cup V(\bar x)\).  Since \(m\) is even,
both indices are even; each boundary is supplied by \(x=z\) and
\(x=\bar z\), proving part 3.

For \(i<m\), the upper target is

\[
 \{a_1^{1-x_1},\ldots,a_{i-1}^{1-x_{i-1}}\}
 \cup P_i\cup P_{i+1}
 \cup\{a_{i+2}^{x_{i+2}},\ldots,a_m^{x_m}\}.          \tag{I.Q.9}
\]

It fixes every bit except \(x_i,x_{i+1}\), of whose four completions
exactly two are even.  At \(i=m\), the upper target is
\(\{u\}\cup P_m\cup\{a_1^{1-x_1},\ldots,a_{m-1}^{1-x_{m-1}}\}\);
its split choices and parity determine \(x_m\) uniquely.  This proves
part 4. \(\square\)

The bank decomposition also recovers exact fractional loads.  A fixed
\(C\in\binom R{m+1}\) belongs to \(\mathcal B(P)\) for

\[
 \rho_m=\binom{m+1}2(m-1)!={(m+1)!\over2}              \tag{I.Q.10}
\]

pairings: choose its doubled pair and biject its other elements with
\(R-C\).  Weight \(1/\rho_m\) on every integral bank therefore gives
middle load one.  A fixed \(m\)-set is a transversal of \(m!\) pairings
and has multiplicity \(m/2\) in each, so its lower load is exactly

\[
                         {m!\,(m/2)\over(m+1)!/2}
                         ={m\over m+1}.                \tag{I.Q.11}
\]

### Defect-one packet census [I]

Pair all of \(\Omega\) as \(P_1,\ldots,P_b\).  For special pair \(P_j\),
take \(u=a_j^0,v=a_j^1\) and the bank on the other pairs.  The internal
targets of the \(b2^{b-2}\) packets partition the defect-one stratum

\[
                 |\mathcal S_1(P)|=b(b-1)2^{b-2}.       \tag{I.Q.12}
\]

Indeed a defect-one target has a unique empty pair; Theorem I.Q.2 then
places it exactly once in the corresponding special-pair bank.
This is an exact integral resolution for one pairing. Packets chosen from
different pairings can still collide, so it is not the global selector.

### Gate \(C_{\rm Q}\) [O]

Across pairings and packet orders, select \(t\) packets whose internal
middle targets \(C_1,\ldots,C_{b-1}\) are globally distinct. Let
\(\mathcal U_s\) be the union of their actual designated rank-\(s\) windows.
Prove
\[
\boxed{\sum_{\substack{b-H\le s\le b+H\\s\ne b}}
 \left[\binom{2b}s-|\mathcal U_s|\right]=o(W).}         \tag{I.Q.17}
\]
This is sufficient. Internal disjointness gives
\((b-1)t\le W\) and \(|\mathcal U_b|\ge(b-1)t\). Using the separate blocks
(I.Q.2a), their length plus the middle holes is at most
\[
(b+1+2H)t+W-|\mathcal U_b|
\le W+(2H+2)t=W+o(W).                                  \tag{I.Q.18}
\]
Equation (I.Q.17), A.4, and the central lower bound now give coefficient
one; bounded splices cover all dimensions. Ordered trails, ports, and
cross-join cleanliness are unnecessary. The selector remains distinct from
\(C_{\rm F}\): its integral blocks and collision problem differ.

## I.2 Coherent FIFO tours

Fix a perfect pairing
\[
 \mathcal P=\{P_j:j\in\mathbb Z_b\},\qquad
 P_j=\{a_j^0,a_j^1\},
 \tag{I.10}
\]
and a directed cyclic order of its pairs.  An initial state
\(x=(x_0,\ldots,x_{b-1})\in\mathbb F_2^b\) selects \(a_j^{x_j}\)
from \(P_j\). The boundary state \(C_{s,0}\) is a FIFO queue, in pair
order \(P_s,P_{s+1},\ldots,P_{s-1}\), containing the currently selected
member of each pair. For \(1\le k<b\), append the opposite member of
\(P_{s+k}\), eject the queue front, and call the resulting middle set
\(C_{s,k}\). Finally append the retained selected member of \(P_s\), eject
the front, and obtain
\[
                         C_{s,b}=C_{s+1,0}.            \tag{I.10a}
\]
Define, for \(1\le k<b\),
\[
 M_{s,k}=C_{s,k},\qquad
 L_{s,k}=C_{s,k}\cap C_{s,k+1},\qquad
 U_{s,k}=C_{s,k}\cup C_{s,k+1}.                    \tag{I.10b}
\]
Thus each packet flips every nonspecial pair once and then rotates the
coordinate queue and special index. Every pair is nonspecial in \(b-1\)
packets; since \(b-1\) is even, the \(b\) packets return both the selected
members and queue order, forming a cyclic tour \(T_{\mathcal P}(x)\).
The cyclic list of appended singleton labels is the tour word, and every
\(C_{s,k}\) above is its current length-\(b\) FIFO window.

Index the internal flags by
\[
                  (s,k),\qquad s\in\mathbb Z_b,\quad
                  1\le k<b,                              \tag{I.11}
\]
and put \(q=b(b-1)\).  The sets in (I.10b) are the attached targets at
ranks \(b-1,b,b+1\). Their
pair-occupancy signatures are
\[
\begin{array}{c|c|c}
\text{target}&\text{empty pairs}&\text{doubled pairs}\\ \hline
L_{s,k}&P_s&\varnothing\\
M_{s,k}&P_s&P_{s+k}\\
U_{s,k},\ k\le b-2&P_s&P_{s+k},P_{s+k+1}\\
U_{s,b-1}&\varnothing&P_{s-1}.
\end{array}                                                \tag{I.12}
\]
Every other pair is split.  On a split pair \(P_j\), the selected member
has the form
\[
                         a_j^{\,x_j+c_{s,k}(j)},             \tag{I.13}
\]
where the chronology constant \(c_{s,k}(j)\in\mathbb F_2\) is independent
of \(x\).  Formulas (I.12)--(I.13) follow directly by recording the pairs
already flipped in the FIFO packet.

Within one tour the middle targets are distinct because their ordered
empty/doubled pair \((P_s,P_{s+k})\) is recoverable.  The lower targets
from different packets have different empty pairs; within one packet
they are successive distinct transversals of a cube path.  The internal
upper signature recovers \(s,k\), and a boundary upper signature has a
different type and recovers \(s\).  Hence one tour has exactly \(q\)
distinct targets separately at all three displayed ranks.

## I.3 All-band pairing catalogues

A middle target is defect one relative to \(\mathcal P\) if one pair is
empty, a different pair is doubled, and every other pair is split.  The
defect-one stratum has size
\[
 |\mathcal V_{\mathcal P}^{(1)}|
 =b(b-1)2^{b-2}=q2^{b-2},                              \tag{I.14}
\]
because one chooses the ordered empty/doubled pair and one member from
each remaining pair.  Every coherent tour on \(\mathcal P\) uses one
target from each of the \(q\) ordered empty/doubled fibers.

Successive outputs from one pair have positional gap at least \(b-1\).
Hence every rank-\(b-1\) tour window is a partial transversal: it omits one
pair and chooses one member from every other pair. One pairing has exactly
\(b2^{b-1}\) such targets. Therefore covering all but \(o(W)\) targets at
that rank requires
\[
\boxed{R\ge(1-o(1)){\binom{2b}{b-1}\over b2^{b-1}}
=(1-o(1)){2\over\sqrt\pi}{2^b\over b^{3/2}}.}          \tag{I.15}
\]
Derivative-block joins do not alter this scale. If \(t=O(W/b)\) and
\(H=o(b)\), a rank-\(b-1\) interval inside a block uses exactly \(H\)
block letters and equals a clean length-\(b-1\) source window, hence is
again a partial transversal. A
cross-join interval ends among the next block's first \(H\) positions:
\(H+1\) consecutive block letters already unite to a clean \(b\)-window.
For a fixed endpoint, unions obtained by moving the start are nested, so
at most one distinct \((b-1)\)-target occurs. Thus joins add at most
\(Ht=o(W)\) exceptions.

More generally, for \(1\le q\le b-2\), put
\[
 N_q=\binom{2b}{b-q},\qquad
 p_q={\binom bq2^{b-q}\over N_q}.                       \tag{I.16}
\]
A random pairing makes a fixed \((b-q)\)-target a partial transversal with
probability \(p_q\). Whenever it does, choose an omitted pair as special,
place the met pairs first in the nonspecial packet order, and choose the
state bits to realize the target. Its complement is realized at rank
\(b+q\) by one full packet followed by \(q\) outputs of the next, with
exactly those \(q\) pairs doubled. Thus compatibility is sufficient on
both sides of the band.

The complete incidence of pairings with targets is also explicit.  Let
\[
 \mathfrak P=\frac{(2b)!}{2^bb!}.
 \tag{I.18}
\]
A fixed middle target \(C\) is defect one for
\[
\boxed{
 D_1=\binom b2^2(b-2)!=\frac{b!\,b(b-1)}4}
 \tag{I.19}
\]
pairings: choose the internal pair of \(C\), the internal pair of
\(\Omega\setminus C\), and biject the remaining vertices across the cut.
Double counting gives
\[
 p_M:=\frac{D_1}{\mathfrak P}
   =\frac{q2^{b-2}}{W}.                                  \tag{I.20}
\]

For two targets \(C,D\), put \(d=|C\setminus D|\), \(a=b-d\), and name
their Venn cells
\[
 A=C\cap D,\quad B=C\setminus D,\quad
 G=D\setminus C,\quad E=\Omega\setminus(C\cup D).
\]
Their sizes are \(a,d,d,a\).  Denote an edge between cells \(X,Y\) by
\(XY\), allowing \(X=Y\).  After the small core which
supplies the two defect-one incidences for each cut is removed, all
remaining pairing edges are forced between the two size-\(a\) cells and
between the two size-\(d\) cells.  The exhaustive core list, after
division by the remaining \(a!d!\) bijections, is
\[
\begin{array}{c|c}
AA,EE&a(a-1)/4\\
BB,GG&d(d-1)/4\\
GG,AB,BE;\ BB,AG,GE&ad(d-1)/2\ \text{each}\\
EE,AB,AG;\ AA,BE,GE&da(a-1)/2\ \text{each}\\
AB,AG,BE,GE&a(a-1)d(d-1).
\end{array}                                                \tag{I.21}
\]
The rows partition the four required internal cut incidences according
as two are supplied by one same-cell edge or all are supplied separately;
hence no core is omitted or counted twice.  Summing (I.21) proves that
the common pairing degree is
\[
\boxed{
 \Lambda_d=a!d!\left[
 ad(ad-1)+\frac{a(a-1)+d(d-1)}4\right].}
 \tag{I.22}
\]
Therefore
\[
 \frac{\Lambda_d}{D_1}
 =\frac{4ad(ad-1)+a(a-1)+d(d-1)}
 {b(b-1)\binom bd}.                                      \tag{I.23}
\]
After quotienting \(C\sim\Omega\setminus C\), for \(b\ge7\),
\[
\boxed{
 \max_{1\le d\le(b-1)/2}\frac{\Lambda_d}{D_1}
 =\frac{5(b-2)}{b^2}}                                    \tag{I.24}
\]
attained at \(d=1\).  Substitution gives the displayed value.  For
\(d=2\), the comparison reduces to
\(5b^3-54b^2+179b-186\ge0\).  For \(d\ge3\), use
\(\binom bd\ge\binom b3\) and
\[
 \frac{b^4}{4}+b^2
 \le\frac56(b-1)^2(b-2)^2 .
\]
Both inequalities hold at \(b=7\) and their differences increase
thereafter, proving (I.24).

From (I.16),
\[
 {p_{q+1}\over p_q}={b+q+1\over2(q+1)},\qquad
 p_1={(b+1)2^{b-1}\over W},\qquad
 p_q\ge{b\over4}p_1\quad(q\ge2).                       \tag{I.25}
\]
Also
\[
 p_M={b(b-1)\over2(b+1)}p_1\ge{b\over4}p_1.           \tag{I.25a}
\]
Thus the necessary adjacent scale exceeds the middle-only scale
\(1/p_M\) by \(p_M/p_1=b(b-1)/[2(b+1)]=(1/2+o(1))b\);
an \(o(b)\)-fold enlargement of the latter still exposes only \(o(W)\)
adjacent targets.
For \(1\le H\le b-2\) and any \(a_b\to\infty\), sample
\[
\boxed{R=\left\lceil{a_b\over p_1}\right\rceil
=(1+o(1))a_b{2\over\sqrt\pi}{2^b\over b^{3/2}}}       \tag{I.25b}
\]
independent uniform pairings and coalesce repetitions. By the catalogue
realization above, the expected aggregate number of missed targets at
ranks \(b-H,\ldots,b+H\) is at most
\[
\begin{aligned}
2N_1e^{-a_b}+We^{-a_b b/4}
 +2\sum_{q=2}^HN_qe^{-a_b b/4}
&\le2We^{-a_b}+(2H-1)We^{-a_b b/4}=o(W).             \tag{I.25c}
\end{aligned}
\]
Thus some menu has \(o(W)\) aggregate catalogue holes. Equation (I.15)
shows its scale is optimal up to the arbitrarily slow factor \(a_b\).
Catalogue availability does not select a compatible tour family.

## I.3A The all-pairing coherent-tour orbit [I]

Let \(b\ge5\) be odd and
\[
 \Omega=\mathbb Z_b\times\mathbb F_2,\qquad P_h=\{h^0,h^1\},\qquad
 \mathcal V={\Omega\choose b},\qquad W=|\mathcal V|={2b\choose b}. \tag{I.3A.1}
\]
Order the pairs cyclically and initially choose \(h^0\) from each. At
stage \(t\), keep the selected member of the special pair \(P_t\), flip
the other selected members in FIFO order, and rotate the pair queue. Every
coordinate is flipped \(b-1\) times, so the \(b\) packets close.

For \(t\ne i\), the internal middle window with empty pair \(P_t\) and
doubled pair \(P_i\) is
\[
 T_{t,i}=P_i\cup\{h^{\chi_{t,i}(h)}:h\notin\{t,i\}\},\qquad
 \chi_{t,i}(h)=t+\mathbf1_{(h-i)(t-i)>0}\pmod2,             \tag{I.3A.2}
\]
using integer representatives \(0,\ldots,b-1\). Before stage \(t\), the
bit at \(h\) is \(t+\mathbf1_{h<t}\pmod2\); the open arc from \(t\) to
\(i\) is then flipped once more, proving (I.3A.2). The empty/doubled
signature recovers \((t,i)\), hence
\[
 \mathcal K=\{T_{t,i}:t\ne i\},\qquad q=|\mathcal K|=b(b-1). \tag{I.3A.3}
\]

A label consists of a perfect pairing, rooted directed cyclic order, and
initial transversal, modulo the free \(b\) phase shifts. Therefore
\[
 |\mathcal E_{\rm lab}|={ (2b)!\over2^bb!}{b!2^b\over b}
 ={(2b)!\over b}.                                          \tag{I.3A.4}
\]
Parallel labels are retained temporarily.

### Theorem I.3A.1 (exact census and maximum codegree)

For \(M_d=|\{(A,B)\in\mathcal K^2:|A\setminus B|=d\}|\),
with empty ranges omitted,
\[
\boxed{\begin{aligned}
M_0&=b(b-1),&M_1&={b(b^2-5)\over2},\\
M_d&=b(b^2+1)&&(2\le d\le b-3,\ d\ {\rm even}),\\
M_d&=b(b^2-3)&&(3\le d\le b-4,\ d\ {\rm odd}),\\
M_{b-2}&={b(b+1)(3b-5)\over2},&
M_{b-1}&=2b^2,\qquad M_b=0.
\end{aligned}}                                              \tag{I.3A.5}
\]
The labelled orbit has
\[
 D_{\rm lab}=(b-1)(b!)^2,\qquad
 {\lambda_d^{\rm lab}\over D_{\rm lab}}
 ={M_d\over b(b-1){b\choose d}^2},                         \tag{I.3A.6}
\]
and consequently
\[
 \boxed{{\Delta_2\over D_{\rm lab}}
 ={b^2-5\over2b^2(b-1)}={1\over2b}+O(b^{-2}).}              \tag{I.3A.7}
\]

#### Proof

Substitution in (I.3A.2) gives this disjoint relation census; a count on a
range is the count at each displayed distance:
\[
\begin{array}{c|c|c}
\text{relation for }(t,i),(u,j)&d&\text{ordered pairs}\\ \hline
(t,i)=(u,j)&0&b(b-1)\\
t=u,\ i\ne j&1\le d\le b-2&2b(b-1-d)\\
i=j,\ t\ne u&1&b(b-1)(b-3)/2\\
i=j,\ t\ne u&b-2&b(b-1)^2/2\\
(u,j)=(i,t)&d\in\{2,4,\ldots,b-1\}&2b\\
\text{exactly one of }t=j,\ i=u&2\le d\le b-1&2b(b-1)\\
|\{t,i,u,j\}|=4&2\le d\le b-2&
b\{b^2-4b+3+4\lfloor d/2\rfloor\}.
\end{array}                                                 \tag{I.3A.8}
\]
For a common empty coordinate, doubled positions \(r,s\in[1,b-1]\) give
\(|r-s|\). For a common doubled coordinate, the two parities give only
\(1,b-2\). Reversed roles give every positive even distance; one crossed
role gives every distance \(2,\ldots,b-1\). In the four-distinct case fix
\(t=0\), write \(1\le x<y<z\le b-1\), and order the remaining roles as
\(IUJ,IJU,UIJ,UJI,JIU,JUI\) (first-double, second-empty,
second-double). For even second-empty position, the six distances are
\[
 z-x,\ b+x-y-1,\ 1-y+z,\ 1-y+z,\ b+x-y-1,\ b+x-z;          \tag{I.3A.9}
\]
for odd position they are their complements to \(b\). Solving these six
linear differences and pairing cases \(1/6,2/5,3/4\) cancels the endpoint
floors and gives the last row of (I.3A.8). The five nonidentity class
totals are
\[
 q(b-2),\quad q(b-2),\quad q,\quad2q(b-2),\quad
 q(b-2)(b-3),                                              \tag{I.3A.10}
\]
which sum to \(q(q-1)\). Thus the census is exhaustive, and summing it by
distance gives (I.3A.5).

The symmetric group is transitive on middle vertices and on ordered pairs
at each Johnson distance. There are \(W{b\choose d}^2\) ambient ordered
pairs at distance \(d\); double counting with (I.3A.4) proves
(I.3A.6). For \(2\le d\le b-2\), use
\(M_d\le M_{b-2}\) and \({b\choose d}\ge{b\choose2}\), obtaining
\[
 {2(b+1)(3b-5)\over b^2(b-1)^3}
 <{b^2-5\over2b^2(b-1)}.                                  \tag{I.3A.11}
\]
The cross-multiplied difference is
\(b^4-2b^3-16b^2+18b+15>0\) for \(b\ge5\). At \(d=b-1\)
the value is \(2/[b(b-1)]\), tying \(d=1\) only at \(b=5\).
This proves (I.3A.7). \(\square\)

Reversal preserves a tour support, so the labelled orbit is not simple.
All supports form one \(S_{2b}\)-orbit. If their common multiplicity is
\(\mu_b\), then
\[
 D_{\rm simp}=D_{\rm lab}/\mu_b,\qquad
 \lambda_{d,\rm simp}=\lambda_d^{\rm lab}/\mu_b,            \tag{I.3A.12}
\]
so (I.3A.6)--(I.3A.7) survive collapse. No value of \(\mu_b\) is used.

### Theorem I.3A.2 (exact fractional middle/adjacent loads)

For one packet's consecutive middle windows \(C_0,\ldots,C_b\), define
\[
 L_i=C_{i-1}\cap C_i,\qquad U_i=C_i\cup C_{i+1}
 \quad(1\le i<b).                                          \tag{I.3A.13}
\]
Each tour has \(q\) distinct targets separately at ranks \(b-1,b,b+1\).
The adjacent occurrence-degrees are
\[
 D_-=D_+={|\mathcal E_{\rm lab}|q\over{2b\choose b-1}}
 =(b-1)(b-1)!(b+1)!,\qquad
 {D_-\over D_{\rm lab}}={D_+\over D_{\rm lab}}={b+1\over b}. \tag{I.3A.14}
\]
Thus uniform tour weight \(1/D_{\rm lab}\) gives exact loads
\[
 \left({b+1\over b},1,{b+1\over b}\right),                 \tag{I.3A.15}
\]
and weight \(1/D_-\) gives \((1,b/(b+1),1)\).

#### Proof

An empty pair identifies a lower target's packet, and targets within the
packet are distinct vertices of its cube path. An internal upper target is
identified by its empty pair and consecutive doubled pairs; a packet-end
upper target has no empty pair and one doubled pair. Incidence counting on
the three transitive layers now gives (I.3A.14)--(I.3A.15). \(\square\)

These fractional loads do not prove an integral augmented matching:
middle-disjoint tours may share adjacent tokens. Also
\(q=b(b-1)\to\infty\), so fixed-uniformity matching theorems do not follow
from (I.3A.7).

### Theorem I.3A.3 (completed-tour cleanliness and compiler) [I]/[C]

The completed cyclic tour word has length \(b^2\), and every cyclic window
of length at most \(2b-2\) is clean. Indeed, represent
\(s,j\in\mathbb Z_b\) by \(0,\ldots,b-1\). Packet \(s\) emits the pairs in
the order \(s+1,\ldots,s-1,s\), so the occurrence of \(P_j\), with output
positions starting at one, is
\[
 \tau_s(j)=s(b-1)+j+b\mathbf1_{\{s\ge j\}}.                \tag{I.3A.16}
\]
Successive occurrences of \(P_j\) have gap \(b-1\), except from packet
\(j-1\) to packet \(j\), where the gap is \(2b-1\). The emitted member
flips in every nonspecial packet and is retained in the special packet.
Thus its two labels alternate except across that exceptional gap. For each
pair the forward same-label gaps are one \(2b-1\), one
\((b-1)+(2b-1)+(b-1)=4b-3\), and \(b-2\) copies of \(2b-2\). Hence the
complete inventory is
\[
\begin{array}{c|c}
\text{gap}&\text{multiplicity}\\ \hline
2b-2&b(b-2)\\
2b-1&b\\
4b-3&b .
\end{array}                                               \tag{I.3A.17}
\]
If a cyclic window of at most \(2b-2\) letters repeated a label, two
successive occurrences inside it would have forward gap at most \(2b-3\),
contradicting (I.3A.17).

For a completed tour \(T\), let \(K(T)\) be its \(q=b(b-1)\) internal
middle targets and, for \(|h|\le H\), let \(S_h(T)\) be the set of its
cyclic length-\(b+h\) windows. For a family \(\mathcal T\) of \(t\) tours,
put
\[
 W_h={2b\choose b+h},\qquad U_h=\bigcup_{T\in\mathcal T}S_h(T),
 \qquad h_h=W_h-|U_h|.                                  \tag{I.3A.18}
\]
Assume the \(K(T)\) are pairwise disjoint. Apply 3.4 to each clean cyclic
tour with \(L=b^2,\ell=b-H,u=b+H\), and let \(R_{\rm far}=o(W)\) be the
repair word from A.4. Then
\[
\begin{aligned}
\nu(2b)&\le(b^2+2H)t+\sum_{|h|\le H}h_h+R_{\rm far}\\
&=W+2Ht+\Delta_0+\sum_{0<|h|\le H}h_h+R_{\rm far},
                                                               \tag{I.3A.19}\\
\Delta_0&:=b^2t-|U_0|.
\end{aligned}
\]
The equality uses \(h_0=W-|U_0|\). Internal disjointness gives
\[
 qt\le W,\quad |U_0|\ge qt,\quad
 \Delta_0\le(b^2-q)t=bt\le{W\over b-1},\quad
 2Ht=O(HW/b^2)=o(W).                                     \tag{I.3A.20}
\]
Consequently
\[
\boxed{\nu(2b)\le W+O(W/b)+
 \sum_{0<|h|\le H}\left(W_h-|U_h|\right)+o(W).}           \tag{I.3A.21}
\]
Thus internal disjointness plus aggregate off-middle deficit \(o(W)\)
implies coefficient one; no boundary repair is needed. \(\square\)


## I.4 Cyclic derivative of internal collisions

Fix the pairing and order. Let \(\mathcal B\) be the nonzero state
differences causing equality among the \(q\) attached targets
\(L_{s,k},M_{s,k},U_{s,k}\) of (I.10b), \(1\le k<b\), at the same rank:
\[
 \mathcal B\subseteq\mathbb F_2^b\setminus\{0\}.       \tag{I.26}
\]
This is the internal-flag collision set, not the collision set of all
\(b^2\) completed cyclic starts. Define
\[
                  (\partial h)_j=h_j+h_{j-1}\pmod2,
                  \qquad j\in\mathbb Z_b.              \tag{I.27}
\]
Then
\[
\boxed{h\in\mathcal B\quad\Longrightarrow\quad
       \operatorname {wt}(\partial h)\in\{2,4\}.}       \tag{I.28}
\]

For lower-target equality, (I.12) forces the same empty pair \(s\).
Outside \(s\), comparing two positions of its packet makes \(h\) the
indicator of an interval in the linear nonspecial order; the bit at \(s\)
is free. Thus \(h=\mathbf1_J+\varepsilon e_s\), where
\(|J|\le b-2\). An interval and a singleton each have cyclic derivative
weight at most two. For middle equality the signature is unique and \(h\)
is supported on the empty and doubled positions. For an internal upper
flag it is supported on the empty position and two consecutive doubled
positions, hence has at most two cyclic runs; at a boundary upper flag only
one position is free. Internal and boundary signatures cannot cross.
Therefore every case has derivative weight at most four. A cyclic
derivative has even weight and vanishes only on \(0,\mathbf1\); the
descriptions exclude both (the proper lower interval omits a nonspecial
position), proving (I.28).

Finally, \(\mathcal B\) contains every word of weight one or two: in a
fixed empty/doubled middle fiber, precisely those two state bits are free.

## I.5 Quadratic-moment balanced code

Put \(m=\lceil\log_2b\rceil\), \(Q=2^m\), and identify
\(\mathbb F_Q^2\) with \(\mathbb F_2^{2m}\). Choose distinct
\(\gamma_0,\ldots,\gamma_{b-1}\in\mathbb F_Q\) and define
\[
\mathsf A x=\left(\sum_j\gamma_j(\partial x)_j,\quad
                  \sum_j\gamma_j^3(\partial x)_j\right),
\qquad\mathcal C=\ker\mathsf A.                         \tag{I.29}
\]
No binary vector \(z\) of weight two or four has both moments zero. Weight
two would equate two distinct \(\gamma\)'s. For support values \(a,b,c,d\),
the first moment gives \(d=a+b+c\), whereas in characteristic two
\[
a^3+b^3+c^3+(a+b+c)^3=(a+b)(a+c)(b+c)\ne0.             \tag{I.30}
\]
Thus (I.28) makes \(\mathcal C\cap\mathcal B=\varnothing\) for every
ordered injection \(\gamma\).

### Theorem I.2 (quadratic-moment separating code) [I]

For sufficiently large odd \(b\) and every integer \(H=o(b)\), the
\(\gamma_j\) can be chosen so that
\[
\boxed{\mathcal C\cap\mathcal B=\varnothing,\qquad
d(\mathcal C^\perp)>H,\qquad
|\mathcal C|={2^b\over Q^2}\ge{2^b\over4b^2}.}          \tag{I.31}
\]

#### Proof

Choose the ordered injection \(\gamma\) uniformly. Every
\(\mathbb F_2\)-linear functional on \(\mathbb F_Q^2\) is uniquely
\((u,v)\mapsto\operatorname {Tr}(\alpha u+\beta v)\). Its adjoint row is
\[
v_j=f(\gamma_j)+f(\gamma_{j+1}),\qquad
f(t)=\operatorname {Tr}(\alpha t+\beta t^3),            \tag{I.32}
\]
with cyclic indices. For \((\alpha,\beta)\ne(0,0)\), \(f\) is a
nonconstant Boolean polynomial of degree at most two. Indeed, if it
vanished identically, polarization would give, for all \(y,z\),
\[
0=f(y+z)+f(y)+f(z)
=\operatorname {Tr}\!\left[
(\beta y^2+(\beta y)^{Q/2})z\right].                    \tag{I.33}
\]
Nondegeneracy of the trace pairing makes the coefficient vanish for every
\(y\). When \(Q\ge8\), this polynomial of degree below \(Q\) forces
\(\beta=0\), and then nondegeneracy forces \(\alpha=0\), a contradiction.

A nonzero Boolean polynomial of degree at most two on \(m\) variables has
at least \(Q/4\) ones. Induct on \(m\), writing \(P=P_0+xP_1\). If
\(P_1\ne0\), each input where \(P_1=1\) contributes one 1 across the two
values of \(x\), and the degree-one induction gives \(Q/4\); if \(P_1=0\),
double the induction bound for \(P_0\). Apply this also to \(1+f\), which
is nonzero because \(f\) is nonconstant, so both fibers of \(f\) have size
at least \(Q/4\).

During the first \(Q/8\) draws of the injection, both fibers retain at
least \(Q/8\) elements. Hence any prescribed initial bit pattern has
probability at most
\[
                         (7/8)^{Q/8}=e^{-\Omega(b)}.    \tag{I.34}
\]
If the row (I.32) has weight at most \(H\), the cyclic sequence
\((f(\gamma_j))\) has at most \(H\) transitions. There are at most
\(2\sum_{i=0}^H\binom bi=\exp(o(b))\) such sequences. Union-bound (I.34)
over them and the fewer than \(Q^2\le4b^2\) nonzero coefficient pairs.
With probability \(1-o(1)\), every nonzero adjoint row has weight \(>H\).
Choose such an injection. A zero adjoint row is also excluded, so
\(\mathsf A\) has full binary rank \(2m\) (and \(2m\le b-1\) for large
\(b\)). Therefore \(|\ker\mathsf A|=2^{b-2m}=2^b/Q^2\), proving (I.31).
\(\square\)

### Corollary I.3 (three-rank banks and exact resolutions) [I]

For every coset \(z+\mathcal C\),
\[
 \mathfrak B_z=\{T_{\mathcal P}(x):x\in z+\mathcal C\}
 \tag{I.36}
\]
is target-disjoint on the three attached rank families in (I.10b). The
cosets resolve every defect-one middle target exactly four times.

#### Proof

Distinct states in one coset differ by a nonzero word of
\(\mathcal C\), which is outside \(\mathcal B\) by (I.31).  This proves
internal three-rank disjointness, including the within-tour statement in I.2.

Fix a defect-one target with empty/doubled pair \((P_t,P_i)\).  Its split
choices determine all state bits outside \(\{t,i\}\), so its four
preimages are
\[
             x_0+\{0,e_t,e_i,e_t+e_i\}.             \tag{I.37}
\]
Every nonzero difference of these states has weight one or two, hence
belongs to \(\mathcal B\) and not to \(\mathcal C\).  The four states
occupy four different cosets, and no other state produces the target.
\(\square\)

Since \(\partial\mathbf1=0\), every coset contains antipodal state pairs.
Thus this corollary deliberately does not assert disjointness among all
\(b^2\) completed cyclic starts; only its attached \(q\) flags are used.

The same argument records the adjacent multiplicities.  A lower target
with one empty pair and all others split has \(2(b-1)\) state-index
preimages: there are \(b-1\) positions in its packet and its empty-pair
bit is free.  An accessible internal upper target has eight preimages,
while a packet-boundary upper target has two.  Since any two preimages
share that target, they lie in distinct cosets.  Thus these are also the
exact numbers of coset banks containing the corresponding target.

### Lemma I.4 (dual distance gives exact projections) [I]

If \(J\subseteq[b]\) and \(|J|\le H\), the projection of
\(\mathcal C\) onto \(\mathbb F_2^J\) is surjective.  Every pattern on
\(J\) therefore occurs exactly \(|\mathcal C|/2^{|J|}\) times in every
coset.

#### Proof

If the projection were not onto, a nonzero linear functional on
\(\mathbb F_2^J\) would annihilate it.  Extending the functional by zero
outside \(J\) would give a nonzero word of
\(\mathcal C^\perp\) of weight at most \(H\), contrary to (I.31).
Every fiber of a surjective linear map has the same size, and translation
proves the coset assertion.
\(\square\)

### Theorem I.5 (coset-independent low-order profiles) [I]

Fix the pairing and order.  For every ground-coordinate set
\(S\subseteq\Omega\) with \(|S|\le H\), every coset bank contains the
same number of middle targets containing \(S\).  The same assertion holds
separately at ranks \(b-1\) and \(b+1\).  For one ground coordinate
\(a\),
\[
\boxed{
 |\{T:\ T\text{ is a middle target in }\mathfrak B_z,\ a\in T\}|
 =\frac{q|\mathcal C|}{2}.}
 \tag{I.38}
\]

#### Proof

At a fixed flag index, (I.12)--(I.13) show that containment of \(S\) is
either impossible, automatic on an empty or doubled pair, or prescribes
one state bit for every split pair met by \(S\).  It prescribes at most
\(|S|\le H\) bits.  Lemma I.4 makes the number of solutions independent
of the coset.  Sum over the \(q\) flag indices.  The same proof applies
to the adjacent signatures.

For (I.38), let \(a\in P_j\).  Among the \(q\) middle indices, \(b-1\)
have \(P_j\) empty, \(b-1\) have it doubled, and
\((b-1)(b-2)\) have it split. Averaged uniformly over the coset states,
their contribution is
\[
 0+(b-1)+\frac{(b-1)(b-2)}2=\frac q2.
 \tag{I.39}
\]
Coset independence turns the average into the exact value (I.38).
\(\square\)

Consequently any middle-target-disjoint union of whole coset banks is an
exact one-design: every coordinate lies in half of its selected middle
targets.  Its residual in the full middle layer is also an exact
one-design.  Across different pairings, higher-order profiles can differ.

There is also a useful global codegree consequence. For each pairing and
order, choose a map satisfying Theorem I.2, and then choose a uniform
coset. A fixed defect-one target belongs to four cosets. Two
targets belong to at most four common cosets.  Conditional on the pairing,
their normalized bank codegree is therefore at most one; averaging over
pairings and using (I.23)--(I.24) gives
\[
 \frac{\Pr(C,D\text{ lie in the sampled bank})}
      {\Pr(C\text{ lies in the sampled bank})}
 \le\frac{\Lambda_d}{D_1}
 \le\frac{5(b-2)}{b^2}                                  \tag{I.40}
\]
for noncomplementary targets and \(b\ge7\).  This supplies outer volume
and small pair codegree, but growing bank size prevents a conclusion from
a generic fixed-uniformity matching theorem.

## I.6 Exact remaining completed-tour selector

### Gate \(C_{\rm F}\) [O]

For every sufficiently large odd \(b\), select completed tours
\(\mathcal T\) from the balanced coset banks so that
\[
\boxed{
\begin{aligned}
 &K(T)\cap K(T')=\varnothing\quad(T\ne T'),\\
 &\sum_{0<|h|\le H}
 \left[\binom{2b}{b+h}-
 \left|\bigcup_{T\in\mathcal T}S_h(T)\right|\right]=o(W).
\end{aligned}}
 \tag{I.41}
\]
By I.3A.3 and bounded top-bit splices, (I.41) implies coefficient one in
all dimensions. The \(h=1\) term also forces near-full internal size:
\(W_1=bW/(b+1)\), \(|U_1|\le b^2t\), and (I.41) give
\[
 qt={b-1\over b}b^2t\ge{b-1\over b+1}W-o(W)=W-o(W), \tag{I.42}
\]
while internal disjointness gives \(qt\le W\). The \(b\) noninternal
middle starts per tour may repeat: their entire excess is
\(bt\le W/(b-1)=o(W)\).

Proved inputs are the all-band catalogue menu (I.25b), internally
three-rank-disjoint coset banks of size at least \(2^b/(4b^2)\), exact
fractional loads, (I.40), \(H\)-wise balance, and
I.3A.3. Only the correlated cross-pairing integral selection (I.41) at all
nonzero band offsets remains open; the listed marginal facts do not imply
it. No packet-boundary repair or common symmetric-chain factor is needed.

## I.7 Density-hole selectors after dimension extension [C]/[O]

Keep I.1's \(W,H\). For each sufficiently large odd \(b\), select \(a_b\)
completed tours with pairwise-disjoint internal middle supports, but require
only the simultaneous distinct-window deficit
\[
 D_b=\sum_{0<|h|\le H}\left[\binom{2b}{b+h}
             -\left|\bigcup_TS_h(T)\right|\right]
       =\delta_b4^b,\qquad\delta_b\to0.                    \tag{I.43}
\]
This weaker selection is [O]; its sufficiency is [C]. Compile each tour
separately as in I.3A.3 and append no holes. Its periodic singleton source
prefix has length \(b^2+b+H-1\), and the derivative block length is
\(b^2+2H\). Since \(b(b-1)a_b\le W\), the concatenation has length
\[
 n_b\le W\left(1+{1\over b-1}+{2H\over b(b-1)}\right),
 \qquad g_b\le D_b+W+{4^b\over2b^2},                       \tag{I.44}
\]
where \(g_b\) counts its actual holes. Middle holes cost at most \(W\);
far targets cost at most \(2\,4^be^{-H^2/b}\le4^b/(2b^2)\) by 3.3.
The family is nonempty for large \(b\), since otherwise (I.43) fails.
With \(\bar\eta_b=\delta_b+W/4^b+1/(2b^2)\), 3.9 therefore gives
\[
 \boxed{t_b=\lceil2b\bar\eta_b^{2/3}+\sqrt{2b}\rceil
     =O(b\delta_b^{2/3}+b^{2/3})=o(b),\qquad
 {\nu(2b+t_b)\over W(2b+t_b)}
 \le1+O(\delta_b^{2/3}+b^{-1/3}).}                         \tag{I.45}
\]
The relatively dense interpolation in 3.9 covers all dimensions, including
if the bases are only an increasing sequence of ratio tending to one.
Balanced cosets and adjacent disjointness are not used; even internal
disjointness can be replaced by the direct budget \(b^2a_b\le W+o(W)\).
Equation (3.46), not the adjacent argument for (I.42), then forces
\(b(b-1)a_b=(1-o(1))W\).

The identical weakening applies to phase packets: their blocks have length
\(b+1+2H\), internal disjointness gives \((b-1)a_b\le W\), and the
same hole bound in (I.44) gives length \(W(1+O(H/b))\) before extension.
For arbitrary fragments the sufficient conditions are simply actual
compiled length \(W+o(W)\) and actual holes \(o(4^b)\).
All deficits must refer to one common family and be summed over the growing
band: termwise \(o(4^b)\) is vacuous because every rank is already
\(O(W)=o(4^b)\). No near-width density-almost-cover family is constructed
here; these relaxed selectors remain [O]. The separate full-cube
coefficient-one manuscript is recorded in 9.2 [P], with its review limits.
