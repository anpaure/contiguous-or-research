# Independent audit of the complete five-slot two-gate reduction

**Date:** 2026-08-04  
**Verdict:** **GO**, after the least-maximizer wording correction now present
in the audited theorem.  The reduction is logically complete and every
comparison is used in the proof-safe direction.  This audit does not assert
either of the two residual analytic inequalities.

## 1. Audited statement and exact binding

Primary theorem:

`MATH_THEOREM_FIVE_SLOT_COMPLETE_TWO_REPEATED_GAP_REDUCTION_20260804.md`

SHA-256:

`b7763d92d857ce811de7a0b2a9cc8e3b283e2f141536be9c3d176c47388708a6`

The following dependencies were read against the indicated bytes.

| role | file | SHA-256 |
|---|---|---|
| positivity through four slots | `MATH_THEOREM_FOUR_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `1624cff37c4f6b45edd16234e054d43c99ceb722d7dac4b57d058a40465b68b9` |
| five-slot efficiency partition and exact normal forms | `MATH_THEOREM_FIVE_SLOT_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e` |
| complete size-two branch | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| least-critical endpoint normalization | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complete size-five branch | `MATH_THEOREM_FIVE_SLOT_ENDPOINT_EFFICIENT_THRESHOLD_CLOSURE_20260804.md` | `db22119a59eae766e51c9461111f207342280309a3144fe43d0caf214c704027` |
| size-four three-face reduction | `MATH_THEOREM_FIVE_SLOT_FOUR_EFFICIENT_THREE_FACE_BOUNDARY_REDUCTION_20260804.md` | `332debcb96ff54fa47d9c85e153d9a36c01460ccbf9552ee20a2e73baee90c5b` |
| active size-four face | `MATH_THEOREM_FIVE_SLOT_FOUR_EFFICIENT_THRESHOLD_FACE_CLOSURE_20260804.md` | `9cee07d666ae51411550cfad13b8cb8f0ac8006e8968c5983583353dacb10722` |
| complementary-pair inert reduction | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| complete size-four inert closure | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| size-three threshold and delayed-face reduction | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| delayed-`b` concavity and pure-lattice reduction | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md` | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| `q=1,2` one-dimensional sufficient gate | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_PURE_LATTICE_Q12_CONVEX_ONE_DIMENSIONAL_GATE_20260804.md` | `aabfd99e588999b4011a12b81565bc441446925bae16255adb0750b391c2559c` |

## 2. Exhaustion of the efficiency branches

The first-crossing theorem plus complete positivity through four slots
reduces a possible counterexample to a five-slot table with first crossing
at slot five.  Internal superadditivity gives

\[
 {c_2\over2}\ge c_1.
\]

Consequently some member of `2,3,4,5` is maximally efficient.  Selecting
the least maximizer **within this four-element set** gives a disjoint
partition and loses no table.  The audited theorem now states this
restriction explicitly.  The earlier unqualified phrase "least
maximum-density denomination" would have been literally false when sizes
one and two tie; that wording was corrected before this freeze.

There is no mismatch with the endpoint-normalization theorem.  If the
restricted rule selects size five, then none of sizes two, three, or four
is a maximizer.  Size one cannot be a maximizer either, since that would
force size two to be one.  Hence size five is also the global least
maximizer and the endpoint theorem legitimately yields `c_5=A`.

The four branches are then exhausted as follows.

1. The size-two theorem is unconditional and retains both finite pulses.
2. The endpoint normalization followed by the endpoint-period lower bound
   closes size five with strict margin `1/400`.
3. The size-four endpoint normalization has exactly the faces `T=A`,
   `T=P+x`, and `T=y+z`.  The active theorem closes the first with margin
   `199/2310000`; the compact Gaussian theorem closes both inert faces.
4. The size-three threshold face is positive with margin `69/10000`.
   Its strict inert face reduces exactly to `w=y` and `w=2a`, as used in
   the audited theorem.

Thus no efficiency class, finite Apéry head, or endpoint face is omitted.

## 3. Direction audit

Every implication has the correct order for excluding a nonpositive
table.

* In the size-two branch the exact formula is a positive lattice plus two
  nonnegative corrections.
* In the size-five and size-four branches the endpoint-period expressions
  are lower bounds for the literal Bellman functional.  Their strict
  positivity therefore implies strict positivity of the table.
* On the size-three `w=y` face, the literal functional satisfies
  `Phi >= L_3(p;a,y)`.  The one-variable boundary reduction says the
  minimum of this lower train occurs at the threshold boundary, the
  overlap `y=2a`, or `2y=p+a`.  The first is already positive, the second
  belongs to the other face, and the third is exactly `R(a,beta)`.
* On the `w=2a` face, `Phi >= H(p,a,b)`.  Strict concavity gives

  \[
  H(p,a,b)\ge
  \min\{H(p,a,A-p),\,P(p,a)\}.
  \]

  The first endpoint is already positive.  Hence positivity of `P` closes
  the face.

In particular, if an original five-slot table were nonpositive, the
relevant lower bound would also be nonpositive.  Since the other branches
are unconditionally positive, such a table would produce either a point
with `R<=0` or a point with `P<=0`.  The contrapositive in Theorem 1 is
therefore valid.

## 4. Exact domain audit

### 4.1 Repeated-gap gate

At the only new boundary of the `w=y` face,

\[
 2y=p+a,qquad
 \beta={p-a\over2},qquad
 p=a+2\beta,qquad y=a+\beta.
\]

The residual conditions become

\[
 0\le a\le\beta,qquad
 2a+2\beta<A\le2a+3\beta.
\]

Equality on the right is the already-positive threshold endpoint.  Thus
the main theorem correctly needs the unresolved inequality only on

\[
 0\le a\le\beta,qquad
 2a+2\beta<A<2a+3\beta.
\]

The residues `0,a,a+beta` modulo `a+2 beta` have cyclic gaps
`(a,beta,beta)` exactly.

### 4.2 Pure-lattice gate

The delayed-`b` theorem leaves

\[
 0<a<{A\over4},\quad p\ge3a,\quad
 p>A-2a,\quad p<A-a.
\]

The boundary `p=3a` is `P(3a,a)=C(a)>0`; the boundary `p=A-2a` is the
closed threshold endpoint, and `p=A-a` is the already-positive four-slot
boundary.  Therefore the main theorem's unresolved open domain

\[
 0<a<{A\over4},\qquad
 \max\{3a,A-2a\}<p<A-a
\]

is exact after removing proved-positive boundary pieces.  The residues
`0,a,2a` modulo `p` have cyclic gaps `(a,a,p-2a)`.

## 5. Independent audit of the embedded `q=1,2` statement

Set

\[
 t={p\over A},\quad \alpha={a\over A},\quad
 r=1-t,\quad s=r-\alpha.
\]

The pure-lattice domain gives

\[
 0<r<{2\over5},\qquad 0<s<{r\over2},\qquad
 s\ge {4r-1\over3},
\]

where the weak last inequality harmlessly includes the already-positive
`p=3a` boundary.  Conversely these inequalities imply
`alpha=r-s<1/4`: this is immediate for `r<=1/4`, while for `r>1/4` the
last inequality gives

\[
 \alpha\le {1-r\over3}<{1\over4}.
\]

The three normalized `q=1` arguments are

\[
 1-r,qquad 1-s,qquad 1+r-2s.
\]

Using the below-threshold derivative identity for the first two and the
above-threshold identity for the third gives exactly

\[
 h(2-r)-h(r)+h(2-s)-h(s)+h(2+r-2s).
\]

The `q=2` arguments are `2-2r`, `2-r-s`, and `2-2s`; all exceed one and
give the three coefficient-two terms in `B(r,s)`.  Every `q>=3` argument
also exceeds one and contributes strictly positively.  Hence

\[
 {1\over2A}{\partial P\over\partial p}>B(r,s)
\]

with the displayed strict direction.

Twice differentiating the displayed `B` gives

\[
 B_{ss}=h''(2-s)-h''(s)+4h''(2+r-2s)
       +2h''(3-r-s)+8h''(3-2s).
\]

Here `s<1/5`, so `h''(s)<0`; every other argument is greater than `9/5`,
where `h''>0`.  Thus `B` is strictly convex in `s`.  The clipped interval

\[
 I_r=\left[\max\left(0,{4r-1\over3}\right),{r\over2}\right]
\]

is nondegenerate for `0<r<2/5`, so it has a unique minimizer.  Therefore
`Psi(r)>=0` implies `B(r,s)>=0`, hence strict increase of `P` in `p`.
The lower-period boundary `p=max(3a,A-2a)` is already positive, proving
the stated sufficient implication.  This exactly matches the dedicated
source theorem.

## 6. Scope

The audited theorem is a complete structural reduction, not a positivity
proof for the two remaining trains.  It proves neither `R>0` nor `P>0`,
and therefore does not yet prove five-slot Bellman positivity, the
all-grid Bellman inequality, or any `B(k)+O(1)` statement.
