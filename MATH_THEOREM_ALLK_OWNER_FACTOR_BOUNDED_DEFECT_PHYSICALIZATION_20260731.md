# Owner factors versus physical words: the exact and bounded-defect Pascal recurrence

Date: 2026-07-31  
Lane: exact/O(1) recurrence audit  
Status: unconditional completion and recurrence implications; exact diagnosis
of the present gap.  No unconditional all-\(k\) upper bound is claimed.

## 0. Verdict

The authenticated `K17` artifact

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

closes the owner and immediate-lower-colour row of the `K15 -> K17`
Pascal/GMM transition: it is a Hamilton cycle on all 24,310 rank-nine
owners, and its 24,310 edge intersections are exactly all rank-eight
colours.  This is a genuine strengthening of a residual path factor.

It is not yet a physical near-optimal word.  A physical recurrence must
still correlate four rows:

1. a legal chain-aligned deadline schedule and nonempty row envelopes;
2. every upper target, at every depth, including all occurrences exposed by
   openings and seams;
3. coordinate residence sufficient for row recovery under that schedule;
4. one simultaneous common-cap assignment for the complete lower atlas.

The first three are not implied by an owner/q1 Hamilton cycle, and the last
is not implied by scalar capacity or marginal Hall.

There is also an exact regenerative tax on the third row.  In the odd
diamond transition (C_i=T_i\cap T_{i+1}), every proper old-coordinate run
of length at least two loses exactly one position; singleton runs vanish and
an all-one trace is unchanged.  Thus, in the intended lower-rainbow state, a
flat depth-(d) child is automatic only from parent proper minimum run
(d+2), not merely (d+1).  Otherwise the exported state must include a
certified cut/facet/nonflat compensation which meets every minimum parent run
and remains valid after the final chronology and compiler are chosen.

This note proves the exact implication which separates the two issues.

* A **zero-defect physicalization** of the Pascal/GMM owner transition gives
  \(\nu(k)=B(k)\).
* A uniformly **bounded-defect physicalization** gives
  \(\nu(k)\le B(k)+O(1)\).  It may leave a bounded number of literal target
  holes, which are then appended as singleton letters.
* The closed-form even splice and the present odd owner cycle do **not** prove
  the bounded-defect hypothesis.  Even from an exact odd parent, the closed
  splice is \(\Theta(\sqrt{k})\) above \(B(k)\), while the frozen `K17`
  cycle has thousands of upper/deeper-shadow and residence defects before a
  physical compiler is installed.

Thus no unconditional \(B(k)+O(1)\) theorem follows from the current
results.  In this recurrence coordinate the single missing theorem for
equality is **uniform zero-defect regenerative physicalization**.  The
strictly weaker theorem sufficient for a constant additive bound is
**uniform bounded-defect regenerative physicalization**.

## 1. Deadline notation

Put

\[
 r_k=\left\lceil\frac k2\right\rceil,
 \qquad W_k={k\choose r_k},
 \qquad
 \Lambda_k=\sum_{j=1}^{r_k-1}{k\choose j},                    \tag{1.1}
\]

and

\[
 d_k=\min\left\{d\ge0:
       dW_k+{d+1\choose2}\ge\Lambda_k\right\},
 \qquad B(k)=W_k+d_k.                                         \tag{1.2}
\]

The monotone-deadline theorem gives \(\nu(k)\ge B(k)\).  The purpose of a
Pascal recurrence is to construct the reverse inequality while paying the
deadline slack only once on the child, not once on each parent shore.

## 2. Exact physicalization of a middle chronology

Let \(T=(T_0,\ldots,T_{W_k-1})\) enumerate
\({[k]\choose r_k}\) exactly once.  Let

\[
 I_i=[s_i,e_i]\subseteq[0,L-1]                               \tag{2.1}
\]

be chain aligned: both endpoint sequences are strictly increasing and
successive intervals overlap or touch.  Consequently

\[
             \bigcup_{i=a}^{b}I_i=[s_a,e_b].                  \tag{2.2}
\]

Define the maximal row envelope

\[
 E_p=\bigcap_{i:p\in I_i}T_i,                                 \tag{2.3}
\]

where an empty intersection is the full ground set.  In particular the
definition also permits a bounded number of explicit collar positions not
belonging to a middle row.

Let \({\cal L}_k\) be the nonempty targets of rank below \(r_k\).  Choose
a set \(H^-\subseteq{\cal L}_k\) of lower holes and an injective assignment

\[
 \mu:{\cal L}_k\setminus H^-\longrightarrow
       \{\hbox{physical intervals in }[0,L-1]\}.              \tag{2.4}
\]

Its maximal common cap is

\[
 A_p=E_p\cap
     \bigcap_{S:p\in\mu(S)}S.                                 \tag{2.5}
\]

We call \((T,I,\mu)\) a **physicalization with upper-hole set** \(H^+\)
when all of the following hold.

1. Every \(A_p\) is nonempty.
2. Every middle row is recovered:
   \[
                  \bigcup_{p\in I_i}A_p=T_i.                  \tag{2.6}
   \]
3. Every selected lower cell is recovered:
   \[
                  \bigcup_{p\in\mu(S)}A_p=S
                  \quad(S\notin H^-).                         \tag{2.7}
   \]
4. For every target \(U\) of rank above \(r_k\), except those in \(H^+\),
   there is a consecutive block \([a,b]\) with
   \[
                  U=\bigcup_{i=a}^{b}T_i.                      \tag{2.8}
   \]

Condition (2.5)--(2.7) is the exact common-cap compiler, not ordinary
matching.  Conditions (2.3) and (2.6) are the exact schedule/residence row:
any proposed run criterion is useful only insofar as it proves these
equations.  Condition (2.8) includes the complete upper tower, rather than
only q1 or a fixed derivative depth.

### Lemma 2.1 (upper blocks lift physically)

Under (2.1)--(2.6), every equality (2.8) gives

\[
                  \bigcup_{p=s_a}^{e_b}A_p=U.                  \tag{2.9}
\]

#### Proof

Every position of \([s_a,e_b]\) lies in some \(I_i\), \(a\le i\le b\),
by (2.2), so its cap is contained in \(T_i\) and the left side of (2.9) is
contained in \(U\).  Conversely each recovered row \(T_i\),
\(a\le i\le b\), is the union of caps in \(I_i\subseteq[s_a,e_b]\).
Taking their union gives the reverse containment.  \(\square\)

### Theorem 2.2 (bounded-defect completion)

Suppose the physicalization has

\[
                         L=B(k)+c.                             \tag{2.10}
\]

Then

\[
 \boxed{
 \nu(k)\le B(k)+c+|H^+|+|H^-|.}                              \tag{2.11}
\]

In particular, zero defect \((c,H^+,H^-)=(0,\varnothing,\varnothing)\)
gives \(\nu(k)=B(k)\).

#### Proof

The word \(A_0\cdots A_{L-1}\) realizes every middle target by (2.6),
every nonhole lower target by (2.7), and every nonhole upper target by
Lemma 2.1.  Append one letter equal to each distinct mask in
\(H^+\cup H^-\).  Its one-letter interval realizes that mask, and appending
letters destroys no old witness.  This proves (2.11).  At zero defect the
deadline lower bound supplies equality.  \(\square\)

The append step is intentionally elementary.  It shows exactly how much a
bounded-hole theorem must prove and prevents a hidden assumption that every
temporary debt has to be repaired inside the central braid.

## 3. The two structural owner transitions

Let an odd regenerative state on \(2r-1\) coordinates contain the auxiliary
lower-rainbow factor and occurrence data needed by both children.

### 3.1 Odd to even: facet/staircase transition

Two matchings in the regular inclusion graph between ranks \(r-1\) and
\(r\) supply a perfect Pascal trace system.  If \(C_i\) is its rank-\(r\)
trace and \(F_i=C_{i-1}\cap C_i\), then

\[
       \bigcup_{j=0}^{q}F_{i+j}
       =\bigcup_{j=0}^{q-1}C_{i+j}.                            \tag{3.1}
\]

Thus plain vertices and top-marked facets supply the complete even middle
layer, and every **internal** marked shadow is inherited one parent depth
lower.  The exact one-jump staircase separately requires:

* the short-run frontier condition for row recovery;
* scalar capacity \(a\le\Delta_{2r}\);
* the literal hinge/top-singleton socket;
* sockets for all cut and terminal occurrence rays; and
* the common-cap equations (2.5)--(2.7).

Equation (3.1) does not prove any of these boundary or compiler rows.

### 3.2 Odd to odd: GMM macro transition

The tight enumeration on ranks \(r-2,r-1\) supplies the balanced residual
`A/X/Y` path forest.  A connected integral macro-port completion by the
pure `U` deck supplies a child owner factor with the complete immediate
lower palette.  This last connected completion is now literal for
`K15 -> K17`.

The frozen child has

\[
 {17\choose9}=24310
\]

owners and the same number of distinct rank-eight edge colours.  Its
remaining raw chronology diagnostics are

\[
\begin{array}{c|rrrr}
\text{upper rank}&10&11&12&13\\ \hline
\text{missing interval unions}&1891&910&128&3,
\end{array}                                                   \tag{3.2}
\]

and the displayed width-three/width-four lower-window ledgers miss 1,623
rank-seven and 1,013 rank-six values.  These latter figures are carrier
diagnostics, not yet holes of a compiled physical word.  Its coordinate
run census has 1,063 runs of length two and 1,829 of length three.  The
best single opening makes only three of those runs boundary runs, leaving
2,889 short internal runs for the flat depth-three residence test.

The fixed-macro audit makes the last point structural.  Exactly 605 of the
length-three runs, including their entering and leaving zero-edges, lie
strictly inside one of the 1,430 residual macros.  They survive every
permutation of the atomic objects, every macro reversal, and every change
of the integral `U`-to-port completion.  Hence **port b-flow optimization
alone cannot make this fixed macro family flat depth-three resident**.  A
second exact audit closes the apparent occurrence-transversal escape: among
the 1,425 internal `0 111 0` patterns, 165 use four rank-six colours having
unique physical occurrences.  Their four edges are forced under **every**
choice of one occurrence of each rank-six colour.  There are exactly eleven
such forced patterns for each old coordinate.  Therefore every occurrence
transversal in this fixed parent chronology fails flat depth-three residence.
The exact coupled optimum is stronger: every transversal leaves at least
`180` such internal packets, and one authenticated transversal attains
exactly `180`, twelve per old coordinate.  The upper bound is replayed from
the literal macro paths; the lower bound is the independently verified DRAT
refutation of the exact at-most-`179` CNF.  This is a packet-debt count, not
an edit or extra-cell lower bound.
A successful physicalization must change the parent chronology/macro
interiors more fundamentally, or use a genuinely nonflat schedule.  The same
audit splits the missing rank-ten unions by new-coordinate tag as

\[
                   (618,623,650,0)                              \tag{3.3}
\]

for `(none,Y,X,XY)`: upper-q1 remains a port-turn covering problem, while
the flat-residence obstruction is already internal.

This obstruction is the finite instance of a dimension-uniform identity.
For every cyclic Johnson parent component, putting

\[
                         C_i=T_i\cap T_{i+1}                   \tag{3.4}
\]

sends each proper positive coordinate run of length \(\ell\ge2\) to a run
of length exactly \(\ell-1\), with the same cyclic start.  A singleton
vanishes and an all-one trace is unchanged.  Lower-edge-colour injectivity
rules out singleton runs in the intended parent state.  Hence the
regenerative residence coordinate has exactly two proof-safe forms:

1. **one-unit margin:** the parent exports minimum run at least \(d+2\) for
   a flat depth-\(d\) child; or
2. **certified compensation:** an explicit cut/facet/nonflat actuator meets
   at least one of the \(d+1\) trace edges spanning every parent run of
   length \(d+1\), and the composed schedule/run automaton proves that no
   replacement short run is created.

The hitting condition in item 2 is the exact local escape condition; by
itself it is not a complete physicalization theorem.  Its interaction with
upper witnesses, envelopes and common caps must still be certified.

The occurrence choice already couples residence to upper service before any
port flow is chosen.  With (U_i=T_i\cup T_{i+1}), let (u_Z) be the number
of physical occurrences in depth-two fibre (Z) whose (U_i) has no other
parent provider.  For an actual transversal (S), selecting occurrence
(e_Z) in each fibre deletes exactly

\[
 D_U(S)=\sum_Z\left(u_Z-
       1_{\{e_Z\text{ is upper-unique}\}}\right),             \tag{3.5}
\]

and its unconstrained marginal minimum is

\[
                         \sum_Z(u_Z-1)^+.                      \tag{3.6}
\]

The residence hyperclauses, the provider rewards in (3.5), and the induced
macro endpoint demands live on the same one-hot variables.  Their separate
marginal optima cannot be pasted together.  A proof-safe odd state therefore
exports the literal occurrence vector (S), its remaining residence packets
or certified compensators, the identities of lost/surviving upper witnesses,
and its endpoint demand relation; only then may the connected `U`-port
`b`-flow be applied.

For the authenticated parent the (u_Z) profile is
`0^1835 1^2685 2^465 3^20`, giving marginal internal-provider debt `505`.
The saved octahedral `r2` parent improves this to
`0^1735 1^2865 2^405`, debt `405`, and independently certified residence
minimum `150` instead of `180`.  These are internal-witness and residence
packet ledgers, not final child-hole or edit counts.

Therefore the artifact proves the central/owner row and nothing stronger:
there is not yet a chain schedule, a cap word \(A\), or a common-cap lower
assignment to which Theorem 2.2 can be applied.

## 4. Exact regenerative recurrence

For constants \(c,h\ge0\), call an odd state \((c,h)\)-**regenerative** if
it exports the auxiliary Pascal/GMM data for the next step, including one
literal occurrence choice jointly decorated by upper-provider identities,
endpoint demands and either the one-unit residence margin or a certified
compensation set in the sense of (3.4)--(3.6), and has the following two
children.

1. Its even Pascal facet child has a physicalization of length at most
   \(B(2r)+c\) with \(|H^+|+|H^-|\le h\).
2. Its odd GMM macro child is another \((c,h)\)-regenerative state and has
   a physicalization of length at most \(B(2r+1)+c\) with
   \(|H^+|+|H^-|\le h\).

It is enough to require this along one compatible infinite sequence of odd
states.  Left-totality on a whole state family is a useful stronger
inductive statement, but is not logically necessary.

### Theorem 4.1 (bounded-defect odd-spine recurrence)

If there are absolute constants \(c,h\) and a compatible regenerative odd
spine from some dimension onward, then

\[
                 \boxed{\nu(k)\le B(k)+c+h}                    \tag{4.1}
\]

for every subsequent odd and even dimension.  For \(c=h=0\),

\[
                 \boxed{\nu(k)=B(k)}.                          \tag{4.2}
\]

#### Proof

At each odd state, apply Theorem 2.2 to its odd physicalization and to its
even child.  Their overhead is bounded absolutely by \(c+h\), not added to
the parent length.  Move to the exported next odd state and iterate.  Thus
the bound does not accumulate with the number of dimensions.  When
\(c=h=0\), combine the resulting upper bound with the deadline lower bound.
\(\square\)

### The exact missing theorem

In the Pascal/GMM coordinate, the weakest convenient single theorem for
equality is:

> **Uniform zero-defect regenerative physicalization.** There is a
> compatible all-rank odd spine such that both the even facet child and the
> odd macro child admit a legal chain-aligned schedule at their exact
> deadline length, exact recovery of every middle row, protected witnesses
> for every upper/deep-shadow target, one exact common-cap assignment for
> every lower target, and export of the next odd auxiliary state including
> the joint occurrence/provider/endpoint state and either one extra unit of
> residence or a certified compensation set.

At `K17`, where the owner/q1 cycle is now supplied, its finite specialization
is simply the existence of one zero-defect physicalization of a suitable
cycle in the authenticated macro-flow architecture.  Within the fixed parent
chronology, no rank-six occurrence transversal makes the macros flat
depth-three resident.  Thus a successful specialization must either use a
nonflat compiler or alter the parent chronology/macro interiors upstream;
port reconnection alone is insufficient.

The strictly weaker all-rank theorem sufficient for
\(\nu(k)\le B(k)+O(1)\) is the same statement with uniformly bounded length
overhead and uniformly bounded literal upper/lower hole sets.  It does not
require every debt to be absorbed internally, but it still requires the
margin/compensation coordinate to regenerate rather than deteriorate by one
unit at each odd diamond step.

## 5. Why the current theorems do not imply the bounded version

### 5.1 The closed even splice has square-root excess

For a word \(X\) on \(2m-1\) coordinates, the closed splice

\[
 X\,[z],((X\text{ without its last letter})+z)                 \tag{5.1}
\]

is universal and has length \(2|X|\).  If
\(|X|=B(2m-1)+e\), then its exact excess over the even lower bound is

\[
 2e+2d_{2m-1}-d_{2m}.                                        \tag{5.2}
\]

The depth dichotomy gives

\[
 d_{2m}\le d_{2m-1}\le d_{2m}+1,
 \qquad
 2d_{2m-1}-d_{2m}\in\{d_{2m},d_{2m}+2\}.                     \tag{5.3}
\]

Since \(d_k=\sqrt{\pi k/8}+O(1)\), even an exact odd parent gives only

\[
                     B(2m)+\Theta(\sqrt m),                    \tag{5.4}
\]

not \(B(2m)+O(1)\).  Across the odd closed-splice step there is additionally
a Catalan-width toll.  The facet/staircase and GMM macro transitions are
precisely what remove these arithmetic tolls at the **owner** level; they do
not by themselves compile the resulting owner order.

### 5.2 Common-cap failure can be extensive

Marginal Hall, even with constant-factor expansion, cannot replace
(2.5)--(2.7).  In the robust-Hall interface gadget, targets

\[
                 A=\{a,x\},\qquad B=\{b,y\}                    \tag{5.5}
\]

have five marginal cells, all through one center envelope \(\{a,b\}\),
and the outer envelopes are \(\{x,y\}\).  The marginal graph is
\(K_{2,5}\), yet a single nonempty center cap cannot realize both targets:
choosing only \(a\) loses \(B\), choosing only \(b\) loses \(A\), and
keeping both makes every center-crossing cell contain both unwanted center
bits.

Disjoint copies have uniform \(5/2\)-fold marginal Hall expansion but force
at least one common-cap hole per copy.  This is an abstract exact-compiler
interface, not a literal all-\(k\) carrier no-go.  It proves the logical
point needed here: owner/q1 exactness, scalar surplus, and even robust
marginal Hall do not imply a bounded number of compiler holes.

### 5.3 Upper service and residence are independent

The literal `K17` census (3.2) already separates immediate lower rainbowness
from the longer upper deck.  Likewise, the 2,892 short runs separate a
Johnson Hamilton cycle from an unchanged flat depth-three schedule.  A
variable staircase or an upstream global rethread may repair both; the
census is not a `K17` no-go.  But the 605 wholly internal length-three runs
prove that no mere port-flow change, object permutation, or macro reversal
can repair flat residence in the displayed macro family, and the 165 empty
occurrence-choice clauses extend that failure to every rank-six occurrence
transversal of the fixed parent chronology.  These facts are a direct
counterexample to the inference

\[
 \text{owner Hamilton + q1 rainbow}
 \quad\Longrightarrow\quad
 \text{upper completeness + flat residence}.                    \tag{5.6}
\]

The finite census alone is not a proof that these debts grow without bound.
What is proved is the failure of automatic zero defect and the failure of
the complete fixed-parent occurrence-transversal/port-flow flat repair
class.  No theorem currently
bounds the number of all-depth defects or the size of the exact compiler
boundary uniformly in \(k\).

The one-unit residence tax explains why this failure is regenerative rather
than accidental: an induction exporting only ordinary depth-\(d\) parent
residence presents depth \(d-1\) on the unmodified `A` shore.  Thus the
state must export one extra unit relative to the child's flat compiler need,
or an explicit compensation ledger.  This is an exact interface condition,
not a numerical lower bound on the number of edits.

## 6. What is now proved and what remains open

The current recurrence supplies:

* unconditional central Pascal trace systems on the even branch;
* exact internal facet-shadow transfer (3.1);
* a solver-free balanced residual GMM forest for `K15 -> K17`;
* an exact connected integral `U`-port completion, giving the authenticated
  lower-rainbow `K17` Hamilton owner cycle; and
* the exact arithmetic showing why child compilation must pay the deadline
  slack once.

It does not supply:

* a uniform connected GMM port completion in every odd dimension;
* a residence- and upper-aware opening/rethread of the resulting owner
  factor;
* a uniform one-extra-unit residence margin or certified compensation set
  which survives each odd diamond transition;
* a uniform joint occurrence selector carrying residence packets, literal
  upper-provider identities and induced endpoint demands before `b`-flow;
* uniformly bounded all-depth cut/seam debt;
* a legal chain schedule whose maximal envelopes recover all rows; or
* a zero- or bounded-defect common-cap compiler.

Accordingly, neither exact equality nor an unconditional constant-additive
upper bound is proved.  Theorem 4.1 is the strongest proof-safe recurrence
statement supported by the present inputs.

## 7. Frozen inputs used here

```text
MATH_THEOREM_K17_PARENT_INDUCED_MACRO_PORT_HAMILTON_CYCLE_20260731.md
  SHA-256 d02245596dd9f5097881e901243c850c89216f777eafaae4a06502c0dfe7309e

scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
  SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6

MATH_THEOREM_K17_GMM_ENDPOINT_ORIENTED_RESIDUAL_FACTOR_20260731.md
  SHA-256 20d37788b9927df7fe6c4f2e41597bec9158c432917d270b4e43c5ac28e2d5bd

MATH_THEOREM_ALLK_PASCAL_FACET_STAIRCASE_RECURRENCE_20260731.md
  SHA-256 b22b48a053fc94481885a4a3ec278953812ee34309e08a1ad80ec2668f0e31e7

MATH_THEOREM_EVEN_SPLICE_EXCESS_TWO_RANK_CARRIER_GATE_20260731.md
  SHA-256 659779fbf1236344a84734ec01b36de50b75a351e7e57f3646946b96eb9118d0

MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md
  SHA-256 b8f303475a169f6ad07f24a44c3ffa5989bf728687f7b2fe9735c7adb90d81fd

MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md
  SHA-256 ff3ec04346f9f0d7adaedac548f61a863066df397a2d257a88b6df47015b8498

MATH_AUDIT_ODD_DIAMOND_RESIDENCE_TAX_SCOPE_CORRECTION_20260731.md
  SHA-256 b718d49e6acadbeaa9446cf721cb3f99489897c7d474cc2983e5defa5ba88db3

scratch/audit_odd_diamond_residence_tax_independent_20260731.py
  SHA-256 12b6077518acb0864e895721534e1d362b651451514a9c19b596820bc8ed0128

scratch/odd_diamond_residence_tax_independent_20260731.audit.json
  SHA-256 f489de727b5b7026a66f51d9ec2949f21b8bf00723e566e237d1db8ed620bd77

MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md
  SHA-256 c2b0920221070de61ced078a30099e6dba8d421fd2de76070e16483456ace24e

MATH_AUDIT_ODD_DIAMOND_OCCURRENCE_COHERENCE_INDEPENDENT_20260731.md
  SHA-256 2e5067513de7353d97eff6bc636430e88a44511dd069695012230f209072f168

scratch/audit_odd_diamond_occurrence_coherence_independent_20260731.py
  SHA-256 1153d68a625f882ef04ab2e5d27bf535b8e7cf932f6579cbe08b0c5fd23e3ef1

scratch/odd_diamond_occurrence_coherence_independent_20260731.audit.json
  SHA-256 592bc21769d18d827eebc3e69d690656d28f7442e91b07ae5dc2c66b5fbba6a6

scratch/build_odd_diamond_depth3_residence_bound_cnf_20260731.py
  SHA-256 e3a1fa67caef12239acf19c50a4eba4a1a67cadc6dec7965d3d14124a1f0ed7f

scratch/k15_octahedral_translation_descent_r2.factor.json
  SHA-256 13c5ecaddc94bd4a240c9b2ce348f5db4508cb340658b2b0f4797b8c80472dfb

scratch/odd_diamond_occurrence_coherence_octa_r2_bound149_20260731.cnf
  SHA-256 a6ff6ef3533e27fd7143ce161e99eb27e3dd4adf33e12fd2992acb9ed997ad25

scratch/odd_diamond_occurrence_coherence_octa_r2_bound149_20260731.drat
  SHA-256 ac0a5512a9d7be7e0df90f52540d4404fa0eaa608ff5addd7963e6c4a53f3514

scratch/odd_diamond_occurrence_coherence_octa_r2_bound149_20260731.dratcheck.txt
  SHA-256 86c2294efccb1c516ccfb2cd424db177476b7d8c27f18fdf10244ab63ab7d449

scratch/k17_macro_residence_20260731.cnf
  SHA-256 3c66f122f094c02afc140127c51710d0ef1c404dc604e15c898f69f7a4349764

scratch/k17_macro_residence_20260731.map.json
  SHA-256 1d16bf9453627528370cda64f71c4088f54c4bc8c0c2b23510f7e17ea905f224

scratch/build_k17_macro_residence_cnf_20260731.py
  SHA-256 deea6a938c18ba457708e55f05e2d316c8698c23e6c5e6e4b741831d0e086871

scratch/build_k17_macro_residence_cnf_relax_forced_20260731.py
  SHA-256 f2947d5c88f5c6869abe30cba606e41acfe5f79e3255ee4a8eaabd5c92ea4d83

scratch/k17_macro_residence_optimal_20260731.json
  SHA-256 8ecf43e13bfb7e0c204847f3c480dadc76af39dec979d245dc73bd5a5b5717b4

scratch/solve_k17_macro_residence_maxsat_20260731.py
  SHA-256 2bb480d9625a1214429e9b92e86bcb37d67bb71da01ea756bbc2569c5b5f9639

scratch/verify_k17_macro_residence_optimum_20260731.py
  SHA-256 ac24039d853386e46b53deb1bfdf9d95039c7150ef6fc46181e5de35bf873ab6

scratch/k17_macro_residence_optimal_20260731.verify.json
  SHA-256 71ffd874fe520daf8609902cf2f12df181a55b1b38d3299633bb95c7e5e89a10

scratch/build_k17_macro_residence_bound_cnf_20260731.py
  SHA-256 65c0283ce09ae324e06f2c5190215a62a275ccdf93badb64c7eac321d9dc24fa

scratch/build_k17_macro_residence_bound_cnf_coordinate_20260731.py
  SHA-256 1d99c69afa19cb0c84906e1b3f81e1ba5b61b7e755accf499febe3fa78fade9f

scratch/k17_macro_residence_bound179_20260731.cnf
  SHA-256 4cbf25a3f4d322c54ce91b068dc08e49223e86019d3dfccc51f065a3860cf19c

scratch/k17_macro_residence_bound179_20260731.map.json
  SHA-256 f5b4095a131ad77ebb0a6d95d62a4a94a66852dc2979180759001ac08ec05466

scratch/k17_macro_residence_bound179_20260731.drat
  SHA-256 8d55ea0215b62b43aaba7a94eda194555227ffdb0a73eb174d227afa0695c018

scratch/k17_macro_residence_bound179_20260731.dratcheck.txt
  SHA-256 78bd2f06aa9938999374176d676dec9337fcb61a231a3f7287bfb6468f25d465
```

The literal cycle has an independent owner/intersection replay.  The quoted
upper, lower-window, and run counts are diagnostics of that cycle, not a
claim that its fixed order is impossible to repair.
