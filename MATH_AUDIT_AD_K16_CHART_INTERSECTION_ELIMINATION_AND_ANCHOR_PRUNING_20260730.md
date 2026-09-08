# Independent audit: K16 chart-intersection elimination and anchor pruning

Date: 2026-07-30  
Lane: AD independent audit  
Status: **PASS**, with two non-substantive wording/notation corrections below

## 1. Frozen object and audit scope

The audited theorem is

```text
MATH_THEOREM_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 a0ec04cdd61fd551db1789f31020f513e18e9082813aa2d84fcb076e686b5dd6
```

The finite ledger checked against it is

```text
scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA-256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892

scratch/audit_k16_12873_three_profile_closure_model_20260730.py
SHA-256 29b4b252b3014abf7e9f0c28747b2ffdd02636f73ace645985794d5f0034b7d2
```

No SAT solver or finite word search was run in this audit.  I checked the
mathematical equivalences directly and replayed the displayed finite data
from the frozen JSON and authenticated word.

## 2. Maximal-context equivalence: PASS

Fix a repair target `T`, a local variable interval `I`, and write `V` for
the OR of the values on `I`.  In an exact `T`-witness, each chosen left and
right fixed context is a submask of `T`.  Because the compatible suffix and
prefix OR families are chains, each is below its unique largest member
contained in `T`.  Their two maxima can be chosen simultaneously by one
literal interval.  Therefore

\[
 \exists c\text{ literal compatible context}:c\vee V=T
 \quad\Longleftrightarrow\quad b_T(I)\vee V=T.
\]

This is occurrence-exact and preserves literal chronology.  It does not
preserve a previously selected pair of witness endpoints, exactly as the
theorem states.

One sentence in the proof should be read with an implicit qualifier.  The
statement “every allowed context obeys `ell subset ell_T` and
`r subset r_T`” is false for an arbitrary context containing a bit outside
`T`; it is true for every context participating in an exact `T`-witness,
because such a context is necessarily contained in `T`.  The proof uses
only this qualified statement, so this is a wording correction and not a
gap in Lemma 2.1.

## 3. Closure and chart-only projection: PASS

For any nonempty family `Q` of repair targets with nonzero intersection
`v`, one has

\[
 Q\subseteq S(v),\qquad
 v\subseteq\bigcap S(v)\subseteq\bigcap Q=v.
\]

Thus every nonzero active intersection is a fixed point of the closure.
The frozen artifact has exactly 245 nonzero fixed points, consistent with
the theorem.

For a one-chart-per-target selection, necessity of Theorem 3.1 is exact:
at every active cell `p`, its original nonzero value is contained in every
active target and hence in `K_p`; every target bit missing from its maximal
fixed context must occur at some cell of its selected interval, so it occurs
in the corresponding `K_p`.

Conversely, assigning `z_p=K_p` on used cells introduces no contaminating
bit into any selected witness, because `K_p` is contained in every target
active at `p`.  Condition (3.3) supplies every bit absent from the maximal
context.  Lemma 2.1 then gives a literal interval for every repair target.
Unused cells may receive any fixed nonzero closure value because none of
the selected repair witnesses uses them; fixed-gap targets retain their
old witnesses.  Hence Theorem 3.1 is an iff projection, not merely a Hall or
intersection relaxation.

The private-bit formula (3.5) is correct under Section 3's convention that
exactly one chart `I_U` is selected for each target `U`.  In the later
ALO-only CNF, where several selectors for the same `U` may be true, its
literal generalization is

\[
 I\setminus
 \bigcup_{(U,J):\,x_{U,J}=1,\ q\notin U}J\ne\varnothing
\]

for every true selector `(T,I)` and every required bit
`q in T minus b_T(I)`.  Proposition 5.1's proof does use this all-true-chart
interpretation.  The singular `I_U` notation should not be copied unchanged
into an ALO-only implementation.

## 4. Blocker CNF, ALO-only selectors, and overblocking: PASS

For a fixed set of true selectors, define the minimal blocker assignment by

\[
 B_{p,q}=1
 \quad\Longleftrightarrow\quad
 \text{some true chart through }p\text{ has a target omitting }q.
\]

Then (5.2) is exactly nonemptiness of the active target intersection and
(5.3) is exactly the durable-point condition.  This proves the forward
direction.

For an arbitrary satisfying blocker assignment, `B_{p,q}=0` together with
(5.1) certifies that every true chart through `p` has a target containing
`q`.  Clause (5.2) therefore gives a nonzero active intersection at every
used cell, while (5.3) supplies each required target bit at a point where it
belongs to that intersection.  Taking intersections over **all** true
charts and assigning those masks to the cells gives the literal word from
Theorem 3.1.

Thus:

* at-most-one selector clauses are unnecessary;
* extra true selectors can only add active-target constraints;
* extra true blocker bits can only tighten clauses (5.2)--(5.3);
* existential blocker assignment remains exact because the minimal blocker
  assignment is always available in the forward direction; and
* no closure-domain clauses are needed, provided a positive decoder builds
  the canonical cell values from the selected-chart intersections rather
  than misreading blocker bits as word bits.

The last point is an operational decoding caveat, not a theorem correction.

## 5. The `0x8000` anchor: PASS

The authenticated word has fixed-gap endpoint values

```text
G1 first  0x1009
G1 last   0x0600
G2 first  0x9620
G2 last   0x8c44
```

Each nonempty suffix or prefix entering a collar contains the adjacent
endpoint letter, and every displayed endpoint has a bit below `0x8000`.
Hence no nonempty boundary context is a submask of `H=0x8000`, so
`b_H(I)=0` for every local interval `I`.

The frozen repair list contains `0x8000` and has exactly 18 targets below
`0x8000`, hence exactly 18 repair targets omitting its high bit.  Any exact
`H` witness consists only of nonzero submasks of `H`, so every cell in it is
literally `0x8000`; any one such cell is a singleton `H` witness.  A selected
chart for a target omitting the high bit cannot use that cell.  Branching on
one of the 17 collar locations, selecting the singleton `H` chart there,
and excluding all 18 low-target charts through it is therefore iff-safe.
Multiple `0x8000` cells cause no problem: choose any one as the branch
anchor.

## 6. Exact count replay: PASS

The frozen artifact gives 57 repair targets, 245 closure masks, 17 cells,
and 272 blocker bits.  Its three maximal-context ledgers give the following
selector and implication counts:

| profile | selectors | negative implications | required-bit rows |
|---|---:|---:|---:|
| `(4,9,4)` | 3,705 | 91,840 | 28,292 |
| `(5,8,4)` | 3,477 | 78,400 | 26,442 |
| `(5,9,3)` | 3,762 | 94,080 | 28,695 |

Adding 57 target ALO rows and 17 cell nonemptiness rows gives, respectively,

\[
\begin{aligned}
91840+28292+57+17&=120206,\\
78400+26442+57+17&=104916,\\
94080+28695+57+17&=122849.
\end{aligned}
\]

Adding the 272 blockers to the selector counts gives 3,977, 3,749, and
4,034 variables.  All displayed counts in Section 5 are therefore exact.
They equal the old unrestricted-bit base counts because each old negative
cell-bit implication is replaced one-for-one by (5.1), and each old
required-bit witness row is replaced one-for-one by (5.3).  The removal is
of the 4,369 closure-domain clauses, not of those base rows.

## 7. Arbitrary adjacent-collapse criterion: PASS

After replacing adjacent cells by one cell `y`, every critical target has
no surviving witness avoiding `y`; hence every new witness has the form
`s_T or y`, with `s_T` a realizable left-suffix/right-prefix base.  Any
working nonzero `y` is contained in every critical target and therefore in
their intersection `K_p`.  Consequently every bit of `T minus K_p` must be
in `s_T`, proving necessity of (6.1).

Conversely, (6.1) implies `T minus s_T subset K_p`.  Thus

\[
 y_0=\bigvee_T(T\setminus s_T)
\]

is contained in `K_p`, contains every bit missing from every chosen base,
and introduces no bit outside any critical target.  Therefore
`s_T or y_0=T` simultaneously for all critical targets.  If `y_0=0`, every
chosen base already equals its target, and any nonzero one-bit submask of
nonzero `K_p` works.  The empty critical-family convention is also sound.

A suffix-OR chain on a 16-bit alphabet has at most 17 distinct members
including zero, so there are at most `17^2=289` side bases.  The criterion
is exact and source-relative; the theorem correctly does not claim that its
12,873-boundary census has been carried out there.

## 8. Reversal and final scope: PASS

Reversal swaps the ordered fixed gaps.  Their total ORs have ranks 15 and
16.  A Boolean-lattice automorphism is a coordinate permutation and
preserves rank, so no reversal followed by coordinate relabelling restores
this frozen ordered architecture.  This rules out only that obvious
quotient, exactly as Section 7 says; it is not a classification of every
conceivable transformation of unrelated length-12,873 words.

## 9. Verdict

All theorem-level implications survive.  The only corrections are:

1. qualify “every allowed context” in Lemma 2.1 as every context of an exact
   `T`-witness (equivalently, every allowed context contained in `T`); and
2. when passing from one-chart selections to the ALO-only CNF, union over
   every true chart of every `q`-omitting target, not a singular `I_U`.

Neither correction changes the claimed iff reductions, finite counts,
anchor pruning, collapse criterion, or source-relative scope.  No profile
SAT/UNSAT verdict and no new length-12,873 word is inferred.
