# Fixed-H rail compiler damage: exact selector and a ray-amplification counterexample

Date: 2026-08-01  
Lane: A, additive-constant compiler damage  
Status: exact compiler-interface theorem and sharp fixed-cap counterexample.
No impossibility for a cap-optimizing Pascal child is claimed.

## 0. Outcome

The shortest rotating-hole rail has a local source/cap footprint of order
`Hh`, where `H` is the number of planted rails and `h=d(k)` is the compiler
depth.  This footprint does **not** control how many cells of a reference
compiler matching are destroyed.  One screened source occurrence can lie in
`h-1` distinct matched interval cells, and all of them can be forced.

More precisely, the current rail, fixed-`H` common-`Q`, and bounded-eviction
theorems do not imply such a bound uniformly over prescribed cap faces.
Already for `H=1`, every `h>=2` admits an exact typed-socket common-`Q`
instance with one legal task cell and at least `h-1` forced matched
casualties.  The old and new source words in the example have the same
depth-`h` derivative, so the loss is invisible to the middle-owner equations.

The correct exact bridge is a retainable-submatching optimization.  For a
legal joint rail/task choice `theta`, append the literal equality row of a
set `F` of reference-matching edges to the plus-state common-`Q` system.  If
`CQ(theta,F)` denotes the maximal-letter feasibility test, then the minimum
number of displaced or damaged reference edges is

\[
 \Delta(\theta)=|M_0|-\max\{|F|:
 F\subseteq M_0,\ F\cup E_{\rm task}(\theta)
                  \text{ is a matching},
 \ \operatorname{CQ}(\theta,F)\},                       \tag{0.1}
\]

where `E_task(theta)` is the prescribed task matching and `B_theta` is its
cell set.  Consequently the desired
bridge is exactly

\[
                         \min_\theta\Delta(\theta)=O(H), \tag{0.2}
\]

not a consequence of the number of rail parameters or of local common-`Q`
feasibility.

A sufficient positive hypothesis is an `M_0`-relative diffuse ray-load
bound.  If a probability distribution on legal joint choices satisfies

\[
 \sum_{e\in M_0}
 \Pr_\theta\bigl(e\text{ conflicts with }E_{\rm task}(\theta)
          \text{ or }e
          \text{ fails in the final plus word}\bigr)\le CH,             \tag{0.3}
\]

then some choice has at most `CH` casualties.  No independence is needed.
The rotating-rail menu size `(m-2)(m-2)_h` supplies no such incidence bound.

## 1. Exact matched-damage identity

Fix a reference nonzero source word `Q^-` and a reference matching `M_0`.
An edge `e in M_0` has target `S_e` and interval cell `I_e`; thus

\[
                         S_e=\bigcup_{p\in I_e}Q^-_p.       \tag{1.1}
\]

For \(F\subseteq M_0\), write \(C(F)=\{I_e:e\in F\}\); in particular
\(C(e)=I_e\).

Fix a legal plus-state common-`Q` choice `theta`, including its caps, assigned
rows and prescribed task matching `E_task(theta)`, whose cell set is
`B_theta`.  If `F subseteq M_0`, augment the assigned plus rows by

\[
                         \bigcup_{p\in I_e}A_p=S_e
                         \qquad(e\in F).                  \tag{1.2}
\]

When only part of `I_e` is live, (1.2) is read in the standard mixed-row
form

\[
 E_e\cup\bigcup_{p\in J_e}A_p=S_e,                       \tag{1.3}
\]

where `E_e` is the frozen exterior OR and `J_e` is the live part.  Write
`CQ(theta,F)` when the exact maximal-letter conditions hold: every exterior
is contained in its target, every screened live letter is nonempty, and
every assigned row is reproduced by the maximal letters.

### Theorem 1.1 (retainable-submatching min-max)

Among all plus words satisfying the rows of `theta` and all task edges on
`B_theta`, the minimum number of reference-matching edges which must be
deleted is exactly (0.1).

#### Proof

Let `A` be any feasible plus word.  Let `F(A)` consist of those edges of
`M_0` which are vertex-disjoint from `E_task(theta)` and still realize their
old targets in `A`.  Adding their equalities (1.2) changes no value of `A`, so
`CQ(theta,F(A))` is feasible.  Therefore

\[
 |F(A)|\le\max\{|F|:F\cup E_{\rm task}(\theta)
                                  \text{ is a matching},
                         \operatorname{CQ}(\theta,F)\}.
\]

Conversely, if `F` attains the maximum, the maximal-letter theorem applied
to the augmented system gives a nonzero plus word retaining every edge in
`F`.  By hypothesis `F union E_task(theta)` is a matching, so the task edges
can coexist with them.  Deleting all other reference edges and adding the task edges yields
exactly `|M_0|-|F|` casualties.  This proves (0.1).  \(\square\)

This is a finite exact characterization, not a claim that the optimization
is automatically easy.  The coupling among edges in `F` is precisely the
common-cap shrinkage which isolated ticket tests omit.

For one fixed feasible plus word `Q^+`, there is a useful occurrence form.
For every coordinate `x`, put

\[
 O_x^- =\{p:x\in Q^-_p\},\qquad
 O_x^+ =\{p:x\in Q^+_p\}.                                \tag{1.4}
\]

Define

\[
 D_x=\left\{e\in M_0:
 \mathbf 1[I_e\cap O_x^-\ne\varnothing]
 \mathbin\oplus
 \mathbf 1[I_e\cap O_x^+\ne\varnothing]=1\right\}.      \tag{1.5}
\]

### Proposition 1.2 (coordinate ray decomposition)

The exact damaged reference-edge set is

\[
                         D_{M_0}=\bigcup_xD_x.             \tag{1.6}
\]

Hence, with `lambda_x=|D_x|`,

\[
 |D_{M_0}|\le\sum_x\lambda_x,
 \qquad
 \max_x\lambda_x\le |D_{M_0}|.                           \tag{1.7}
\]

#### Proof

The coordinate `x` belongs to the OR of an interval exactly when the
interval meets its occurrence set.  The old and new interval ORs are equal
exactly when these two hit indicators agree for every coordinate.  This is
(1.6), and (1.7) is the union bound and containment.  \(\square\)

It would be incorrect to replace (1.5) by the condition that `I_e` meets
the symmetric difference \(O_x^-\mathbin\triangle O_x^+\): an interval can meet both
occurrence sets at different positions and then retains `x`.

### Corollary 1.3 (diffuse-load selector)

Suppose each legal `theta` comes with one feasible final plus word, and the
task cells are distinct and legal.  Under (0.3), some `theta` satisfies
`Delta(theta)<=CH`.

#### Proof

For each `theta`, delete exactly the reference edges which conflict with a
task edge or whose literal equality fails.  The expected size of this set is
the left side of (0.3).  Therefore one outcome has size at most `CH`.
Theorem 1.1 can only improve this displayed feasible choice.  \(\square\)

Thus a theorem controlling `sum_x lambda_x`, or directly the expectation in
(0.3), would close bounded damage.  Counting source positions does not.

## 2. A counterexample inside one rotating-hole rail

Fix `h>=2` and a middle rank `m` with `h<=m-2`, and put `n=h+3`.  Let `K` be a set of size
`m-h-2` (possibly empty), let `epsilon` be a further coordinate, and choose
the cyclically ordered active coordinates

\[
                         u_{-1},u_0,u_1,\ldots,u_{h+1}.    \tag{2.1}
\]

Extend by `u_(p+n)=u_p`.  These are the `h+3` active labels of the
rotating-hole rail.  Thus the
physical middle owners are

\[
 T_i=K\cup\{\epsilon\}\cup
          \{u_i,u_{i+1},\ldots,u_{i+h}\},                \tag{2.2}
\]

with cyclic indices.  They have rank `m`, form the rail cycle, and have the
private q1 palettes and residence asserted by the frozen rail theorem.

The canonical erosion source would put `K+epsilon+u_p` at every active
position.  Instead use the following plus-state source on one linear
unrolling of the cycle:

\[
 A_p^+=
 \begin{cases}
 K\cup\{u_p,\epsilon\},&p=-1\text{ or }p=h,\\
 K\cup\{u_p\},&p=0,1,\ldots,h-1\text{ or }p=h+1,
 \end{cases}                                             \tag{2.3}
\]

and define the whole plus unrolling by `A_(p+n)^+=A_p^+`.  Thus the backup
residues are `-1` and `h` modulo `n`.  Their successive gaps are `h+1` and
`2`, so every consecutive block of `h+1` source letters contains at least
one backup.  Its union is exactly the corresponding owner (2.2).

Give position `0` the cap

\[
                         P_0=K\cup\{u_0,\epsilon\},        \tag{2.4}
\]

give every other displayed position its exact plus letter as cap, and
assign the literal task

\[
                         \tau=K\cup\{u_0\}
                         \quad\text{to }[0,0].             \tag{2.5}
\]

The assigned common-`Q` rows consist of all middle equations (2.2), the
task row (2.5), and any unchanged rail rows already certified by the
physical carrier.

### Lemma 2.1 (literal plus-state common-`Q` rail)

The maximal-letter test is feasible, and its plus word is exactly (2.3).
In particular the task is a strict-lower target and every middle owner and
rail q1 resource is unchanged.

#### Proof

At position `0`, intersection with the singleton task target removes
`epsilon` from (2.4) and leaves the nonempty letter `K+u_0`.  Every other
cap is already exact.  Each middle block containing `0` contains one of the
backup positions `-1,h`, while every middle block avoiding `0` is unchanged.
Hence all maximal letters reproduce (2.2); the other rail resources depend
only on those physical owners and therefore remain unchanged.

Finally, `|tau|=|K|+1=m-h-1<m`, so the task is strict lower.  \(\square\)

Define the reference word by restoring the redundant occurrence at the
single physical task position `p=0`, not at its translated copies:

\[
 A_0^-=K\cup\{u_0,\epsilon\},\qquad
 A_p^-=A_p^+\quad(p\ne0).                                \tag{2.6}
\]

### Lemma 2.2 (depth-`h` owner neutrality)

The reference and plus words have the same depth-`h` derivative:

\[
                              D^hA^-=D^hA^+=T.            \tag{2.7}
\]

#### Proof

Only the occurrence of `epsilon` at position `0` is removed.  A linear
`(h+1)`-window containing `0` starts at some `s in [-h,0]`.  If `s<0`, it
contains position `-1`; if `s=0`, it contains position `h`.  Thus it still
contains `epsilon`.  On the cyclic rail, the complement of an
`(h+1)`-window is a consecutive pair, while the two backup positions are
not consecutive, so the same conclusion holds.  Every other coordinate is
unchanged.  \(\square\)

For `1<=j<h`, let

\[
                         I_j=[0,j],                       \tag{2.8}
\]

which has legal compiler width `j+1<=h`, and put

\[
 S_j=\bigcup_{p=0}^jA_p^-
     =K\cup\{\epsilon,u_0,u_1,\ldots,u_j\}.              \tag{2.9}
\]

These are strict-lower targets because

\[
                         |S_j|=m-h+j\le m-1.              \tag{2.10}
\]

### Theorem 2.3 (forced ray amplification on the rail)

The targets `S_1,...,S_(h-1)` are distinct, and `I_j` is the unique
reference compiler cell of width at most `h` which realizes `S_j`.  In the
plus word,

\[
                         \bigcup_{p=0}^jA_p^+
                              =S_j\setminus\{\epsilon\}. \tag{2.11}
\]

Consequently every reference matching saturating these targets uses all
`h-1` cells `I_j`, and every complete plus-state damage set contains them.
The task cell `[0,0]` is distinct from all `I_j`.  Hence

\[
                         |D\cap C(M_0)|\ge h-1             \tag{2.12}
\]

for every such reference matching.

#### Proof

Distinctness follows from the last active coordinate `u_j`.  In a cyclic
order of `n=h+3` distinct labels, a consecutive active-label set of size at
most `h` determines its starting residue.  Hence any interval with active
set `{u_0,...,u_j}` starts at a position congruent to `0 modulo n` and ends
at the corresponding offset `j`.

A translated copy with nonzero period contains no backup: offsets
`0,...,j` have `j<=h-1`, whereas the backup residues are `h` and
`h+2=-1 modulo n`.  It therefore lacks `epsilon`.  Only the physical copy
starting at `0` has the extra reference occurrence.  Equivalently, any
interval using a backup contains the forbidden active guard `u_h` or
`u_(-1)`.  Thus `I_j` is the unique reference witness among all cells of
width at most `h`.

Equation (2.11) is immediate.  The old edge `S_j-I_j` therefore fails for
each `j`, and completeness of `D` forces every `I_j` into it.  \(\square\)

Only one source-coordinate occurrence changes, yet it has matched ray load
`h-1`.  The full local cap support remains `Theta(h)`.  The case `H=1`
already refutes a depth-uniform fixed-cap implication.  Under an additional
disjoint-host hypothesis, `H` resource-private copies give `H(h-1)` forced
cells.

## 3. What the counterexample does and does not close

The construction is parameter-independent on this fixed-cap face: every
ordered active-label choice of the frozen rail admits the same two-backup
pattern, task at `0`, and prefix ray.  Thus the formal menu
`(m-2)(m-2)_h` does not by itself reduce the damage.  The example also
survives the middle-owner check, because (2.7) keeps the complete chronology
fixed.

There is an essential qualification.  The exact ordinary-position subcaps
in (2.3) are part of the compiler instance.  The envelope induced by the
middle owners alone is larger:

\[
                         P_p^{\rm owner}=K\cup\{u_p,\epsilon\}.          \tag{3.1}
\]

If the fixed subcaps are relaxed and no protected row screens `epsilon`, one
may put `epsilon` at position `1` and preserve the whole ray.  Thus Theorem
2.3 is a literal **fixed-cap** counterexample.  It refutes an inference from
rail geometry, menu size, footprint, and separate common-`Q` feasibility;
it does not refute the existential physically integrated Pascal bridge in
which the final cap state is also chosen.  Equation (0.1) identifies exactly
what that stronger coupling must prove.

## 4. Sharp remaining hypothesis

The minimum additional hypothesis has one exact form and one stronger
sufficient form.

1. **Exact retainability.**  For every fixed sidecar of size at most `H`,
   there is a legal joint choice `theta` and a subset `F subseteq M_0`
   such that `F union E_task(theta)` is a matching, `CQ(theta,F)` holds, and

   \[
                             |M_0\setminus F|\le CH.       \tag{4.1}
   \]

2. **Sufficient diffuse load.**  There is a distribution on legal joint
   choices satisfying (0.3), or the stronger checkable energy bound

   \[
                  \mathbb E_\theta\sum_x\lambda_x(\theta)\le CH.       \tag{4.2}
   \]

The first is necessary and sufficient; the second is only sufficient.  Either
must include task-cell displacement and the **complete** common-cap damage,
not only locally changed rows.  An exterior alternate witness can reduce a
ray load, while a unique occurrence such as `epsilon` makes it unavoidable.

Thus the surviving O(1) compiler gate is an `M_0`-relative ray-load or
retainable-submatching theorem for a physically integrated Pascal host.
The local footprint `Theta(Hh)`, the number of formal rail parameters, and
separate common-`Q` feasibility are insufficient.

## 5. Adversarial audit

1. The damaged cells (2.8) have lengths `2,...,h`, so the example lies
   inside `COMP_h`; it does not use arbitrary long intervals.
2. The lower bound is independent of the displayed choice of `M_0` because
   each `S_j` has a unique reference witness.
3. The task cell `[0,0]` is not one of the damaged cells.  If a larger old
   target system also matches something to `[0,0]`, that task displacement
   is an additional casualty and cannot weaken (2.12).
4. The two backup residue classes are essential to owner neutrality (2.7),
   but they cannot realize a ray target: they carry the guard coordinates
   `u_(-1)` and `u_h`.
5. Equation (1.6), not source-position counting, is the literal damage
   ledger.  One changed position can occur in many matched intervals.
6. The example closes only the fixed-cap compiler-interface implication.
   It does not construct a full all-lower reference matching; (2.12) applies
   to every such saturating matching if one exists.  Owner/q1 topology,
   upper witnesses, cap-state selection and regeneration are not claimed
   impossible under a stronger joint Pascal construction.
