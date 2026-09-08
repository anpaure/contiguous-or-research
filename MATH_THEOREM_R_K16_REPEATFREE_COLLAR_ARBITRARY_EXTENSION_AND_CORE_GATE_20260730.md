# The exact arbitrary-extension gate for 18-cell K16 free-collar reuse

Date: 2026-07-30  
Lane: R  
Status: proved source-independent reduction and sharp obstruction to an ordinary Hall model; no length-12873 word and no K16 no-go claimed

## 1. Scope

Let `X,Y` be any two nonzero K15 words of length 6438.  Put

\[
 A=X[6:6436],\qquad B=\{z\}\vee Y[7:6432],
 \qquad z=2^{15}.
\]

For positive integers `n_0,n_1,n_2` satisfying

\[
 n_0+n_1+n_2=18,                                                        \tag{1.1}
\]

the length-12873 tri-window fibre considered here is

\[
 W(C)=C^{(0)}\,A\,C^{(1)}\,B\,C^{(2)},                                  \tag{1.2}
\]

where

\[
 |C^{(r)}|=n_r\quad(r=0,1,2).                                           \tag{1.3}
\]

and all eighteen free cells are required to be nonempty subsets of the
sixteen-coordinate ground set.  The proofs below do not use universality or
repeat-freeness of `X,Y`; those hypotheses only improve the fixed-body cover
and hence shrink the residual target set.

The running specialization is `(n_0,n_1,n_2)=(4,9,5)`, the live
DIMACS/implicit-search layout.  This is a **free-collar reuse fibre**: no
theorem below says that an arbitrary optimal K16 word has this form.

The result treats **all** literal intervals of (1.2).  In particular, it does
not assume the `maxext=40` truncation in
`scratch/build_k16_triwindow_dimacs_20260730.py`.

## 2. Exact compression of arbitrary interval extensions

We first state the compression for an arbitrary fixed/free word.

Let

\[
 p_1<p_2<\cdots<p_n
\]

be the free positions in a word.  Let `G_0` be the fixed word before `p_1`,
let `G_i` be the fixed word strictly between `p_i` and `p_(i+1)` for
`1<=i<n`, and let `G_n` be the fixed word after `p_n`.  Empty gaps are
allowed.  For a fixed word `G`, define

\[
 \mathcal S(G)=\{\operatorname{OR}(\hbox{a suffix of }G)\},\qquad
 \mathcal P(G)=\{\operatorname{OR}(\hbox{a prefix of }G)\},              \tag{2.1}
\]

including the empty suffix and prefix, whose OR is zero.  Write

\[
 H_{ij}=\bigvee_{t=i}^{j-1}\operatorname{OR}(G_t)                       \tag{2.2}
\]

for `1<=i<=j<=n`, with `H_ii=0`.

### Theorem 2.1 (complete arbitrary-extension shape catalogue)

The Boolean data of every physical interval containing at least one free
cell are represented by exactly one of the triples

\[
 (i,j,F),\qquad
 1\le i\le j\le n,\qquad
 F=s\vee H_{ij}\vee t,                                                   \tag{2.3}
\]

where

\[
 s\in\mathcal S(G_{i-1}),\qquad t\in\mathcal P(G_j).                    \tag{2.4}
\]

Here the interval contains precisely the consecutive free cells
`p_i,...,p_j`, and `F` is the OR of all its fixed cells.  Conversely every
triple in (2.3)--(2.4) has a literal interval representative.

After duplicate OR masks are identified,

\[
 |\mathcal S(G)|,|\mathcal P(G)|\le 17                                  \tag{2.5}
\]

for a sixteen-coordinate word.  Consequently a collar of eighteen free
cells has at most

\[
 \binom{19}{2}17^2=49,419                                                 \tag{2.6}
\]

distinct arbitrary-extension triples before duplicate `(i,j,F)` triples are
removed.

#### Proof

Take a physical interval `I` containing free cells.  Its first and last free
cells are uniquely `p_i,p_j`, and it contains every free position between
them.  Its fixed cells consist of a suffix of `G_(i-1)`, every complete gap
`G_i,...,G_(j-1)`, and a prefix of `G_j`.  This gives (2.3).  Conversely,
choosing the corresponding suffix and prefix endpoints gives a literal
interval realizing the triple.

Starting with zero and extending a prefix or suffix, its OR mask changes
only when at least one previously absent coordinate first appears.  There
are sixteen coordinates.  Thus there are at most seventeen distinct masks,
including zero.  Summing the product bound `17^2` over the
`binom(n+1,2)` choices of `(i,j)` gives (2.6).  QED.

### Corollary 2.2 (the six shores and saturation localization)

For (1.2), the six ordered window shores are

1. the empty exterior shore to the left of `C^(0)`;
2. the prefix-profile shore of `A` to its right;
3. the suffix-profile shore of `A` to the left of `C^(1)`;
4. the prefix-profile shore of `B` to the right of `C^(1)`;
5. the suffix-profile shore of `B` to the left of `C^(2)`;
6. the empty exterior shore to the right of `C^(2)`.

Thus all arbitrary extensions across the six shores are captured by four
nontrivial monotone OR chains and two singleton zero chains.  Intervals that
cross an entire fixed body are included through the complete-gap term
`H_ij`; they are not silently discarded.

Suppose now that

\[
 \operatorname{OR}(A)=\Omega=[15],\qquad
 \operatorname{OR}(B)=\Omega\cup\{z\}=[16].                             \tag{2.7}
\]

Both saturation masks already lie in the fixed cover: `Omega` is realized
by the whole interval `A`, and `[16]` by the whole interval `B`.  Any interval
whose free cells meet both `C^(0)` and `C^(1)` contains all of `A`, so its OR
is either `Omega` or `[16]`.  Any interval meeting both `C^(1)` and `C^(2)`
contains all of `B`, so its OR is `[16]`; the same is true a fortiori for an
interval meeting the first and third windows.  Consequently no residual
target needs a multi-window host.  The arbitrary-extension residual
catalogue localizes exactly to the six one-window shores.

Let

\[
 p_A=|\mathcal P(A)|,\quad s_A=|\mathcal S(A)|,\quad
 p_B=|\mathcal P(B)|,\quad s_B=|\mathcal S(B)|,                          \tag{2.8}
\]

and put

\[
 u_{AB}=|\{s\vee t:s\in\mathcal S(A),\ t\in\mathcal P(B)\}|.           \tag{2.9}
\]

After canonicalizing `(i,j,F)`, the exact number of one-window shape triples
is

\[
\begin{split}
 N_{\rm port}={}&\binom{n_0}{2}+n_0p_A\\
 &+\binom{n_1-1}{2}+(n_1-1)(s_A+p_B)+u_{AB}\\
 &+\binom{n_2}{2}+n_2s_B.                                               \tag{2.10}
\end{split}
\]

Indeed, a subinterval strictly before the right end of the first window has
fixed OR zero, while each of the `n_0` subintervals ending there has one
choice from `P(A)`.  In the middle window, internal subintervals number
`binom(n_1-1,2)`, the `n_1-1` proper left-anchored and right-anchored
subintervals use `S(A)` and `P(B)`, and the whole middle window uses the
distinct unions counted by `u_AB`.  The last-window count is the reversal of
the first.

For the six authenticated K15 source files, every relevant prefix/suffix
chain has at most eleven nonzero change states, hence at most twelve states
including zero; their retained `A,B` bodies also satisfy (2.7).  Therefore,
for `(n_0,n_1,n_2)=(4,9,5)`,

\[
 N_{\rm port}\le
 6+4\cdot12+28+8(12+12)+12^2+10+5\cdot12
 =\boxed{488}.                                                          \tag{2.11}
\]

Without the saturation localization (2.7), the generic `4/9/5` worst-case
bound is `1003`: number the free cells `1,...,18`.  A nontrivial left profile
occurs only for `i=5,14`, and a nontrivial right profile only for `j=4,13`.
The four disjoint exceptional classes contribute

\[
 (8\cdot17+17^2+5\cdot17)+5\cdot17+4\cdot17+12\cdot17=867.
\]

The remaining `171-(14+5+4+12)=136` free intervals have a single fixed OR,
giving `867+136=1003`.  Duplicate triples can only lower this count.

### Corollary 2.3 (when a finite `maxext` catalogue is complete)

Let `H_full` be the catalogue of Theorem 2.1 and `H_E` the catalogue obtained
by allowing at most `E` fixed cells beyond each free window.  After
canonicalizing by `(i,j,F)`, one has `H_E=H_full` if and only if every full
triple has a representative obeying the extension bound `E`.  Equality of
the two catalogues is sufficient for semantic equivalence for every residual
target family and every collar assignment.

For one particular residual family, the exact weaker statement is this:
every `H_E` solution is a full solution, and a full solution is an `H_E`
solution precisely when it admits a witnessing host choice using only
triples in `H_E`.  Thus equality of feasibility without catalogue equality
requires an explicit alternative-host certificate; it cannot be inferred
from the number of coordinates.  For shapes whose free cells lie in one
window, it is sufficient that every distinct prefix and suffix OR profile on
the adjacent nontrivial shores be attained within `E` cells of its shore.
This does **not** by itself recover a shape spanning two free windows: the
truncated enumerator must also reach that physical free-cell span from at
least one window, or one must prove every omitted spanning triple redundant
for the particular residual family.

Under the saturation hypothesis (2.7), Corollary 2.2 supplies exactly that
redundancy proof.  In the saturated reuse fibre, attainment within `E` of
all four one-window shore profiles is therefore sufficient for semantic
completeness on the residual target family even though the enumerator does
not list the physically long multi-window intervals.

In a general unsaturated reuse fibre, `maxext=40` is not automatically
complete merely because there are sixteen coordinates: an OR chain may have
a plateau longer than forty before acquiring a new coordinate, and the two
fixed bodies are much longer than forty, so body-spanning free intervals are
not enumerated.  A decoded SAT word is still sound after literal replay.  To
promote truncated UNSAT, an unsaturated source needs both the shore-profile
and multi-window-span checks; a source satisfying (2.7) has already
discharged the second check and needs only the shore-profile-radius audit.

## 3. Fixed cover and legal hosts

Let `C_fix` be the set of nonempty masks realized by intervals wholly inside
one fixed gap `G_i`.  In (1.2), this is exactly the union of the interval-OR
covers internal to `A` and internal to `B`.  Put

\[
 \mathcal R=(2^{[16]}\setminus\{\varnothing\})\setminus\mathcal C_{fix}. \tag{3.1}
\]

Every target in `R` must use at least one free cell.  A shape
`h=(i,j,F)` is a **legal host** for `M in R` when

\[
 F\subseteq M.                                                           \tag{3.2}
\]

If the free cell masks are `C_1,...,C_n`, that host realizes `M` exactly
when

\[
 F\vee\bigvee_{q=i}^j C_q=M.                                             \tag{3.3}
\]

This is the literal arbitrary-width contiguous-OR condition, not a maximal
extension proxy.

## 4. Necessary and sufficient host-intersection theorem

### Theorem 4.1 (exact core gate)

The fixed/free collar has a nonzero assignment covering every target in
`R` if and only if one can choose one legal host

\[
 h_M=(i_M,j_M,F_M)                                                        \tag{4.1}
\]

for every `M in R` such that the following holds.  Define the cell core

\[
 K_q=\bigcap_{M:\ i_M\le q\le j_M}M,                                    \tag{4.2}
\]

with the empty intersection interpreted as the full sixteen-coordinate
mask.  Then

\[
 K_q\ne\varnothing\quad(1\le q\le n),                                  \tag{4.3}
\]

and, for every `M in R`,

\[
 M=F_M\vee\bigvee_{q=i_M}^{j_M}K_q.                                     \tag{4.4}
\]

When (4.1)--(4.4) hold, the canonical assignment

\[
 C_q=K_q                                                                \tag{4.5}
\]

is a literal nonzero collar solution.

#### Proof

Suppose first that a collar assignment covers `R`.  For each target choose
one witnessing physical interval and hence its triple `h_M`.  Whenever that
host uses cell `q`, equality (3.3) gives `C_q subseteq M`.  Therefore

\[
 \varnothing\ne C_q\subseteq K_q,                                       \tag{4.6}
\]

which proves (4.3).  Also, every coordinate of `M\setminus F_M` must occur
in some `C_q` with `i_M<=q<=j_M`, hence in the corresponding `K_q`.  The
reverse containment in (4.4) follows from legality and the definition of
`K_q`.

Conversely assume (4.1)--(4.4), and set `C_q=K_q`.  Condition (4.3) makes
all cells nonzero.  Equation (4.4) says exactly that host `h_M` realizes
`M` for every residual target.  Fixed targets were already covered inside a
fixed gap.  Thus the complete physical word is universal.  QED.

### Equivalent blocked-demand form

For a chosen host system, a required pair `(M,b)` with

\[
 b\in M\setminus F_M                                                     \tag{4.7}
\]

is discharged if and only if some used cell `q in [i_M,j_M]` has the
property

\[
 b\in N\quad\hbox{for every target `N` whose chosen host uses `q`}.       \tag{4.8}
\]

Thus infeasibility has one of two exact forms:

* a **zero-core obstruction**, where the chosen target masks using one cell
  have empty total intersection; or
* a **covered-demand obstruction**, where, for some `(M,b)`, every cell of
  its host is used by at least one chosen target omitting `b`.

This is a target-labelled set-cover obstruction, not a capacity deficit.

### Corollary 4.2 (bounded obstruction rows)

Make one option vertex `v=(M,h)` for every legal target-host pair and write
`Q(v)=[i_h,j_h]`.  Partition the vertices by target and require exactly one
option from each part.  Add the following forbidden option hyperedges.

* A **zero-core hyperedge at `q`** is an inclusion-minimal set of options,
  all using `q`, for which the omitted-coordinate sets `[16]\M_v` cover all
  sixteen coordinates.
* A **demand hyperedge rooted at `(M,h,b)`**, where `b in M\F_h`, consists of
  the root option `(M,h)` and an inclusion-minimal set of blocker options
  `v` with `b notin M_v` whose used-cell intervals cover `Q(M,h)`.

Then the collar closes if and only if this partitioned option hypergraph has
a transversal avoiding every forbidden hyperedge.  Once such a transversal
is chosen, the cells are the cores (4.2).

Every minimal zero-core hyperedge has at most sixteen vertices: each member
of a minimal cover has a private coordinate.  Every minimal blocker cover
has at most eighteen vertices, one with a private collar cell, so a rooted
demand hyperedge has at most nineteen vertices.  Equivalently, for a fixed
chosen-host system, failure of the exact core gate always has a certificate
involving at most nineteen chosen target-host rows.

Under saturation localization, every residual host lies in one window, so
the demand-hyperedge rank improves to

\[
 1+\max(n_0,n_1,n_2).                                                    \tag{4.9}
\]

For `4/9/5` this is at most ten.  Zero-core hyperedges still have rank at
most sixteen, so the complete saturated forbidden-option hypergraph has
rank at most sixteen.

* If `K_q=empty`, then for each of the sixteen coordinates choose one target
  whose host uses `q` and whose mask omits that coordinate.  These at most
  sixteen rows certify the zero core.
* If (4.4) fails for `(M,b)`, then retain the row for `M` and, for each of the
  at most eighteen cells of its host, choose one target row using that cell
  and omitting `b`.  These at most nineteen rows certify that every possible
  supplier cell is blocked.

Conversely, either displayed certificate makes the corresponding core row
fail.  Therefore the exact host-selection problem can be written as a
one-host-per-target set-partition system plus forbidden hyperedges of rank at
most nineteen.  This is the bounded exact replacement for a false ordinary
Hall condition.

### Corollary 4.3 (small semilattice formulation)

Equivalently, choose eighteen nonempty masks `C_q` and define the 171
interval joins

\[
 U_{ij}=\bigvee_{q=i}^jC_q.                                              \tag{4.10}
\]

They obey

\[
 U_{ij}=U_{i,j-1}\vee U_{jj}.                                           \tag{4.11}
\]

The collar closes exactly when every residual target `M` belongs to

\[
 \{F\vee U_{ij}:(i,j,F)\in\mathcal H_{full}\}.                           \tag{4.12}
\]

Hence the source-independent gate has only 18 physical mask variables (or
288 cell-bit variables), 171 derived joins, and the at-most-49,419 exact
arbitrary-extension shapes in general.  In the saturated `4/9/5` source
fibre, only the at-most-488 one-window port shapes can host residual targets.
Witness selectors can be introduced for targets, but no suffix automaton or
arbitrary-width proxy is needed.

## 5. Why ordinary Hall matching is not the exact gate

The host-intersection theorem identifies the precise obstruction to a plain
target-to-port matching or single-commodity flow.

### Proposition 5.1 (capacity-one Hall is not necessary)

Take one free cell `q`, a fixed singleton `{a}` immediately to its left and
a fixed singleton `{b}` immediately to its right, with `a,b,x` distinct.
Setting `C_q={x}` simultaneously realizes

\[
 \{a,x\}\quad\hbox{and}\quad\{b,x\}                                    \tag{5.1}
\]

on the two intervals ending and starting at `q`.  Thus one physical cell
may service two distinct residual targets.  Any target-to-cell Hall model
with capacity one rejects this feasible collar.

### Proposition 5.2 (target-to-interval Hall is not sufficient)

In the same one-cell geometry, take four distinct coordinates `a,b,x,y` and
require the two residual targets

\[
 M_1=\{a,x\},\qquad M_2=\{b,y\}.                                       \tag{5.2}
\]

They have two distinct literal host intervals: left-plus-`q` and
`q`-plus-right.  Hence the target-to-host incidence graph has a perfect
matching.  Nevertheless any realization of `M_1` forces `x in C_q` and
`y notin C_q`, while any realization of `M_2` forces `y in C_q` and
`x notin C_q`.  Equivalently, the unique cell core is
`M_1 intersect M_2=empty`.  No nonzero collar assignment exists.

The example is minimal in the number of free cells and required targets.
It does not say that no enlarged network representation is possible; it
does prove that target/host incidence and capacities alone omit the exact
coordinate-core constraints.

### Proposition 5.3 (pairwise compatibility is also insufficient)

At one cell, three selected target masks

\[
 \{1,2\},\quad\{2,3\},\quad\{1,3\}                                     \tag{5.3}
\]

have nonempty pairwise intersections but empty total intersection.  Thus
pairwise conflict deletion does not imply (4.3).  The correct invariant is
the total component core (4.2), together with all covered-demand rows
(4.4).

This proposition is an abstract host-system obstruction; it is not asserted
that these three masks are the complete residual set of one authenticated
K15 source pair.

## 6. What repeat-freeness supplies, and what it does not

For an authenticated repeat-free K15 source, the fixed bodies may cover all
but a small boundary-debt set.  Theorems 2.1 and 4.1 then turn its K16
free-collar reuse into a finite exact selection problem on that debt set.
Repeat-freeness does
not alter the compatibility law: two targets assigned through the same
physical collar cell must still share every coordinate placed in that cell,
and each missing coordinate of each target must survive on at least one cell
of its chosen interval.

Among the six authenticated source files
`scratch/k15_repeatfree_parents_20260730/k15seed_0.word` through
`k15seed_5.word`, exactly seeds `1` and `5` are depth-two repeat-free; seeds
`0,2,3,4` each have one repeat and are comparison sources only.  One may
compare all ordered source pairs by the following source-independent data:

1. the fixed-body cover `C_fix`;
2. the four nontrivial prefix/suffix OR-profile chains of `A,B`;
3. the resulting legal-host lists for `R`;
4. the exact core rows (4.3)--(4.4).

No live DIMACS or implicit search has to be rerun to define or audit this
gate.

## 7. Exact constructive and negative interfaces

The theorem yields two fail-closed outcomes for any ordered source pair.

* **Positive certificate.**  Give one shape `(i_M,j_M,F_M)` for every
  residual target, compute all eighteen intersections `K_q`, verify
  (4.3)--(4.4), and output the literal collar `C_q=K_q`.  A final independent
  start-by-start replay remains mandatory.
* **Negative certificate for the full 18-cell fibre.**  One must exclude
  every host selection under the complete arbitrary-extension catalogue of
  Theorem 2.1, for example by a proof certificate for the exact core formula.
  UNSAT under a `maxext` truncation, a maximal-extension proxy, an ordinary
  Hall matching, or pairwise conflicts alone is not such a certificate.

The theorem neither proves that one of the authenticated source pairs closes nor
rules out the entire repeat-free collar class.  It identifies the exact
remaining invariant: a simultaneous selection of interval hosts whose
eighteen target intersections retain all demanded coordinates.

## 8. Direct audit against the DIMACS semantics

The reduction matches `scratch/build_k16_triwindow_dimacs_20260730.py` as
follows.

1. `body_coverage(a_body, FULL15)` and `body_coverage(b_body, FULL)` compute
   exactly `C_fix` for the two nonempty fixed gaps.
2. Canonicalization by `(fixed_or, free_positions)` is canonicalization by
   `(F,[i,j])` in Theorem 2.1, because the free positions in a physical
   interval are consecutive.
3. The test `fixed_or & ~target == 0` is exactly host legality `F subseteq M`.
4. The witness implications forbidding bits outside `M` in every used free
   cell give `C_q subseteq M`.  The needed-bit clauses require every bit of
   `M\F` in at least one used free cell.  Together these are exactly (3.3).
5. The one positive clause per cell is exactly the nonempty condition used in
   (4.3).
6. The only semantic difference is catalogue scope: the current builder
   enumerates `maxext`-local shapes, whereas Theorem 2.1 defines all physical
   shapes.  Corollaries 2.2--2.3 give the precise promotion condition.

Thus the existing decoder's literal replay makes every decoded SAT word
sound.  A negative result is promoted to the complete saturated reuse fibre
only after the one-window shore profiles are certified complete.

## 9. Audited implication boundary

Proved here:

1. arbitrary physical extensions compress to at most 49,419 exact shapes in
   a general eighteen-cell collar, at most 1,003 in the `4/9/5` layout, and
   at most 488 for the saturated authenticated shore profiles;
2. the six-shore layout includes body-spanning intervals, while saturation
   rigorously localizes all residual hosts to one window;
3. the core conditions (4.3)--(4.4) are necessary and sufficient;
4. setting each cell equal to its target-intersection core is constructive;
5. ordinary target-cell Hall is not necessary, target-host Hall is not
   sufficient, and pairwise compatibility is not sufficient;
6. the precise extra audit required to promote a `maxext` model to the full
   arbitrary-extension fibre.

Not proved here:

1. a universal length-12873 K16 word;
2. UNSAT of the complete 18-cell fibre for any authenticated source pair;
3. completeness of `maxext=40` for any particular source pair, except where
   separately certified by the source-specific audit;
4. a WLOG reduction from arbitrary K16 equality words to this collar;
5. that repeat-freeness alone implies the core conditions.

The global exact bracket remains

\[
 12873\le \nu(16)\le12874.
\]
