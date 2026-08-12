# Independent audit of the resident long-return completion of the rolling reset

**Date:** 2026-08-01  
**Lane:** K, functional attachment / protected reset  
**Status:** proved local theorem with exact scope.  The long return rail closes
the rolling reset's three projected return paths in one literal
occurrence-labelled cycle, and complete reversal preserves every internal
cyclic upper window and every lower derivative-row inventory.  This is not an
exterior planting, common-cap, augmentation, or positive-density theorem.

## 0. Audited conclusion

The proposed construction is valid after making its coordinate supply and
quantifiers explicit.

Let `d>=1`, put

\[
             n=d+1,\qquad N=2n,
\]

and let the rank-`r` two-queue reset have permanent core `K` and private
coordinates `X_0,...,X_(N-1)`, so

\[
 T_a=K\cup\{X_a,X_{a+1},\ldots,X_{a+n-1}\}
 \quad(a\in\mathbb Z_N).                                      \tag{0.1}
\]

Open the reset at

\[
 E=T_0,\qquad F=T_{N-1}.                                     \tag{0.2}
\]

Assume

\[
 |K|\ge d+1                                                   \tag{0.3}
\]

and choose distinct `x_1,...,x_d,b in K`.  Choose distinct
`y_1,...,y_d` outside the entire reset support
`K union {X_0,...,X_(N-1)}`.  Attach the long rail `R_d` from `F` back to
`E`, using the `x`'s as its deleted labels and the `y`'s as its inserted
labels.  Then:

1. the reset path and the interior of the return rail are disjoint on the
   root, immediate-lower, and immediate-upper shores;
2. their union is one simple Johnson cycle on `4d+2` roots with simple
   immediate palettes;
3. every nonconstant positive coordinate run has length at least `d+1`;
4. the opposite phase may be taken to be the complete directed reversal;
5. the two phases have identical cyclic interval-union spectra at every
   width;
6. their maximal depth-`d` antecedents are nonempty reversed words, and all
   derivative-row inventories agree; and
7. the attachment difference is one alternating cycle and the predecessor
   difference is two alternating parity cycles.  Restricted to the opened
   reset, the rail supplies exactly its one attachment return and two
   predecessor returns.

For the displayed uniform construction it is enough to assume

\[
             r\ge2d+2,\qquad k-r\ge2d+1,                    \tag{0.4}
\]

because `|K|=r-d-1` and the number of coordinates outside the reset support
is `k-r-d-1`.

The untouched anchor `b` in (0.3) is useful and load-bearing for a literal
nonzero antecedent.  Residence alone proves exact factorization, but without
an anchor it does not by itself say that every source letter is nonempty.

## 1. Literal rail and root separation

Put

\[
 L=E\cap F,\quad \delta=E-L=X_{n-1},\quad
 \alpha=F-L=X_{N-1}.                                      \tag{1.1}
\]

For `X[j]={x_1,...,x_j}` and `Y[j]={y_1,...,y_j}`, define

\[
 P_j=(L-X[j])+Y[j]+\alpha\quad(0\le j\le d),              \tag{1.2}
\]

\[
 Q_0=(L-X[d])+Y[d]+\delta,                                 \tag{1.3}
\]

and

\[
 Q_j=L-\{x_{j+1},\ldots,x_d\}
       +\{y_{j+1},\ldots,y_d\}+\delta
       \quad(1\le j\le d).                                \tag{1.4}
\]

Thus `P_0=F`, `Q_d=E`, and

\[
 R_d=(F=P_0,P_1,\ldots,P_d,Q_0,Q_1,\ldots,Q_d=E)           \tag{1.5}
\]

is a Johnson path with `2d+1` edges.

### Lemma 1.1 (all internal return roots are private)

Every internal root of (1.5) contains at least one `y_j` and omits at least
one `x_j`.  Every reset root contains every `x_j` and no `y_j`.  Hence the
two root families meet only in `E,F`.

#### Proof

For `j>=1`, `P_j` contains `Y[j]` and omits `X[j]`.  For `j<d`, `Q_j`
contains `y_(j+1),...,y_d` and omits `x_(j+1),...,x_d`.  Equation (0.1)
contains all of `K`, hence all `x_j`, and uses no exterior `y_j`.  This is
the claimed separation. \(\square\)

### Lemma 1.2 (immediate resource separation)

The internal return roots are pairwise distinct, and its lower and upper
edge colours are separately pairwise distinct.

Every reset lower colour contains all of `K`, and every reset upper colour
contains no `y_j`.  Every return upper colour contains some `y_j`.  Every
return lower colour contains some `y_j`, except its first and last colours

\[
                         F-x_1,\qquad E-x_d,                 \tag{1.6}
\]

which omit a member of `K`.  Consequently no return lower or upper colour
is a reset lower or upper colour.

Moreover, an intersection of a consecutive return block that uses an
internal return root omits some `x_j`, whereas every reset-only intersection
contains all `x_j`.  A union of a consecutive return block that uses an
internal return root contains some `y_j`, whereas every reset-only union
contains no `y_j`.  Thus the same separation holds at every width for
blocks lying wholly on one side of the two-segment decomposition.

#### Proof

The strict prefix index distinguishes the `P_j`, the strict suffix index
distinguishes the `Q_j`, and `alpha` versus `delta` distinguishes the two
families.  The immediate lower colours have respectively the forms

\[
 L-X[j]+Y[j-1]+\alpha,\quad L-X[d]+Y[d],\quad
 L-\{x_j,\ldots,x_d\}+\{y_{j+1},\ldots,y_d\}+\delta,       \tag{1.7}
\]

while the upper colours have the same three membership types `alpha only`,
`alpha and delta`, and `delta only`, with a strict prefix or suffix index
inside each type.  Hence both return palettes are simple.

On the `P` half only the first lower edge has no inserted `y`; on the `Q`
half only the last lower edge has none.  Every upper edge sees the `y`
inserted at that step or retained from the previous step.  The block
statement follows directly from Lemma 1.1. \(\square\)

The last statement is deliberately about *pure reset* versus *pure return*
blocks.  Windows crossing their junction are not claimed to be private;
they are handled instead by complete reversal in Section 3.

## 2. Exact run census

Write the forward combined cycle, without repeating its first root, as

\[
 Z^+=(T_0,T_1,\ldots,T_{N-1},
       P_1,\ldots,P_d,Q_0,\ldots,Q_{d-1}).                  \tag{2.1}
\]

It has `N+2d=4d+2` roots.  Define `Z^-` to be the same cyclic list in the
opposite direction, based at `T_0`.

### Theorem 2.1 (complete coordinate-run ledger)

Every nonconstant coordinate has one cyclic positive run.  Its length is

\[
\begin{array}{c|c}
\text{coordinate}&\text{positive-run length}\ \hline
y_j&d+1\\
x_j&3d+1\\
\alpha,\delta&2d+1\\
X_i\in(E\cap F)\setminus K&3d+1\\
X_i\notin E\cup F&d+1.
\end{array}                                                \tag{2.2}
\]

Coordinates in `K-{x_1,...,x_d}` are constant one; unused ground
coordinates are constant zero.  In particular both orientations are
depth-`d` resident.

#### Proof

On the return, `y_j` occurs on

\[
 P_j,\ldots,P_d,Q_0,\ldots,Q_{j-1},                        \tag{2.3}
\]

which has `(d-j+1)+j=d+1` roots, and nowhere on the reset.

On the return, `x_j` occurs on the complementary pieces

\[
 Q_j,\ldots,Q_d,E=T_0,\ldots,F=P_0,\ldots,P_{j-1};          \tag{2.4}
\]

before the reset seam is expanded.  Their rail-cycle total is `d+1`.
Replacing the edge `E--F` by the reset path inserts `N-2=2d` further roots,
all containing `x_j`, so (2.4) has length `3d+1`.

The ordinary reset run of `alpha` ends at `F` and has length `d+1`; its
rail run begins at `F` and also has length `d+1`.  Their shared endpoint is
counted once, giving `2d+1`.  The argument for `delta` at `E` is symmetric.

Every reset-private coordinate in \((E\cap F)\setminus K\) has a reset run crossing
the opened seam and is present on the complete return.  Its original
`d+1` run therefore gains the `2d` internal return roots.  Every private
coordinate outside \(E\cup F\) has a reset run disjoint from the seam and
is absent on the return, so its run stays `d+1`.  Reversal preserves cyclic
run lengths. \(\square\)

This proves the candidate's proposed `x`-, `y`-, and seam-coordinate
mechanism exactly; there is no hidden length-two run of the bare Johnson
square.

## 3. All-width reversal and the maximal antecedent

### Lemma 3.1 (run criterion for maximal cyclic factorization)

Let `V=(V_i)` be a cyclic set word, and suppose every nonconstant positive
coordinate run has length at least `d+1`.  Put

\[
 A_j=\bigcap_{t=0}^{d}V_{j-t}.                              \tag{3.1}
\]

Then

\[
                         D^dA=V,                            \tag{3.2}
\]

where

\[
                    (D^dA)_i=\bigcup_{j=i}^{i+d}A_j.
\]

If some coordinate belongs to
every `V_i`, then every `A_j` is nonempty.

#### Proof

The inclusion \(D^dA\subseteq V\) is immediate from (3.1).  Let a coordinate
belong to `V_i`.  The positive run containing `i` has at least `d+1`
positions, so it contains a consecutive `(d+1)`-subinterval which also
contains `i`.  Write that subinterval as `[j-d,j]`.  Then `j` lies in
`[i,i+d]`, the coordinate belongs to `A_j`, and hence it belongs to
`(D^dA)_i`.  This proves the reverse inclusion.  A constant-one coordinate
belongs to every intersection (3.1). \(\square\)

Apply the lemma to (2.1).  The reserved coordinate `b` is never removed,
so the two maximal antecedents

\[
 A_j^+=\bigcap_{t=0}^{d}Z^+_{j-t},\qquad
 A_j^-=\bigcap_{t=0}^{d}Z^-_{j-t}                           \tag{3.3}
\]

are nonempty and satisfy `D^d A^epsilon=Z^epsilon`.

### Theorem 3.2 (complete reversal identities)

Let `M=4d+2` and index the reversal by `Z_i^-=Z^+_{-i}`.  Then

\[
                         A_i^-=A^+_{d-i}.                   \tag{3.4}
\]

For every `0<=q<=d`,

\[
             (D^qA^-)_i=(D^qA^+)_{d-q-i}.                  \tag{3.5}
\]

Consequently the two phases have identical inventories in every lower
derivative row.  Reversing the endpoints and order of any cyclic interval
also proves equality of:

* the complete cyclic interval-OR spectra of `Z+` and `Z-` at every width;
* the complete cyclic interval-OR spectra of `A+` and `A-` at every width.

#### Proof

Substitute `Z_i^-=Z^+_{-i}` in (3.3):

\[
 A_i^-=\bigcap_{t=0}^{d}Z^+_{t-i}=A^+_{d-i}.
\]

Taking unions of `q+1` consecutive cells gives (3.5).  A reversal does not
change the member sets of an interval, only their order, proving both OR
statements. \(\square\)

Here "complete spectrum" means all internal cyclic windows, not coverage of
the entire Boolean target universe.  It gives exact phase transparency of
the closed packet and nothing about an unchanged exterior chronology.

## 4. Functional attachment and Rado contraction

For every cycle edge `Z_i Z_(i+1)`, put

\[
 I_i=Z_i\cap Z_{i+1},\qquad U_i=Z_i\cup Z_{i+1}.             \tag{4.1}
\]

Use the forward atoms `Z_i -> Z_(i+1)` in one phase and the reverse atoms
`Z_(i+1) -> Z_i` in the other.

### Theorem 4.1 (one literal compatible three-return lift)

Both phases are four-resource cycle factors on the same simple root,
lower, and upper palettes.  Their head--owner overlay is one alternating
cycle.  Their predecessor overlay is two alternating cycles, because two
alternating steps change the root index by two and

\[
                         gcd(4d+2,2)=2.                      \tag{4.2}
\]

On restriction to the opened reset segment, these become its one
head--owner path and two predecessor parity paths; the oppositely oriented
return rail closes all three.  Every projected edge is the projection of
the same literal oriented Johnson atom, so this is a compatible
three-return lift rather than three independently paired projection paths.

#### Proof

At upper owner `U_i`, the selected head changes from `Z_(i+1)` to `Z_i`.
Following alternating incidences advances once around the root cycle.  For
predecessors the two phase matchings are the neighbour permutations `+1`
and `-1`; their alternating product advances by two, giving (4.2).  Cutting
away the rail turns these cycles into exactly the path components stated in
the rolling-reset theorem. \(\square\)

### Corollary 4.2 (exact reset-contracted Rado interface)

Suppose a global construction treats every root copy, lower colour, upper
owner, suffix resource, and guard used by this packet as a forced protected
bank, and suppose the two phase contractions leave literally the same
exterior occurrence-labelled instance.  Then the packet contributes full
rank in both functional projections in either phase, and the residual Rado
rank inequalities are identical.  One residual functional completion
therefore extends either phase.

This is a conditional contraction statement.  The internal reversal proves
the packet part of the hypothesis, including equality of derivative-row
inventories.  It does **not** prove that an ambient factor offers the same
exterior incidence lists, that a common cut exists, or that cells crossing
that cut have a common cap.

## 5. Minimality and exact scope

The construction is the resident non-Cartesian expansion of the seam-deleted
support-four Johnson-square role converter.  The sign obstruction proves
that support below four cannot supply the reset signature, and a ternary
Boolean hex has the wrong attachment parity.  But the resident packet here
uses `4d+2` roots.  It must not be advertised as a literal bounded-support
four-root move.

The theorem closes the following local rows:

* reset-versus-return root and immediate-palette separation;
* exact depth-`d` coordinate residence;
* one nonzero depth-`d` antecedent in each phase;
* every internal upper window and every lower derivative inventory;
* the literal `1+2` functional-return signature.

It does not close:

* planting the `2d` new return roots in a spanning owner factor;
* preservation of arbitrary exterior crossing windows;
* global upper-target coverage;
* a phase-common exterior common-cap matching;
* topology after the closed packet is opened into the ambient factor;
* positive-density, collision-free conjugate supply; or
* regenerative same-parity Pascal export.

In particular, there is no Hall augmentation inside the packet: both phases
are perfect on the same internal shores.  Any global gain must come from the
way a protected opening meets an exterior deficient shore.

## 6. Dependency and replay audit

This proof independently rederives the claims from the displayed set
formulas.  It agrees with the frozen exhaustive replay

```text
scratch/audit_reset_return_rail_complete_reversal_20260801.cpp
scratch/audit_reset_return_rail_complete_reversal_20260801.out
```

which checks the tight-coordinate cases `d=1,...,12`.  The replay is useful
finite calibration; none of the proofs above depends on it.

Audited inputs at the time of this note:

```text
7be54fc68ed13d1cae5b663fd08fafb3559124634d14ff59b8964189f1ae87af
  MATH_THEOREM_BOOLEAN_HEX_RESIDENT_LONG_SQUARE_COLLAR_20260801.md

0439efa1b3b65889a7f8a32f0f695c0ca58d1ecedb10e1e016e6143a8a3c04ad
  MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md

f2a1c1bedcd58ce74c9c1b983affb2995a07d4fe73017e74e939dc6c5e0f8ac0
  MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md

9c4ff9ed1179fa064a5779051d4a7b1c36d5560f19719ae59fbafee091e734ca
  scratch/audit_reset_return_rail_complete_reversal_20260801.cpp
```
