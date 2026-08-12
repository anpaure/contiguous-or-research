# Binary trace normal form for odd equivariant middle carriers

Date: 2026-07-29

Status: exact normal-form theorem and exact search-soundness boundary.  This
note extracts the useful mathematics from Claude's `cword.py`.  It does not
claim a new `k=15` carrier or contiguous-OR word.

## 1. Setup

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r},\qquad N=W/k=C_m.
\]

Identify the coordinates with `Z_k`, let `rho` be addition by one, and index
the physical positions by `Z_W`.  A voltage-one equivariant middle deck is a
sequence

\[
 T_{i+N}=\rho T_i.                                      \tag{1.1}
\]

For a binary cyclic word `c in {0,1}^{Z_W}`, define

\[
 T_i(c)=\{x\in\mathbb Z_k:c_{i-xN}=1\}.                \tag{1.2}
\]

All indices in (1.1)--(1.2) are cyclic.

## 2. Exact normal form

### Theorem 2.1

The correspondence (1.2) is a bijection between

1. voltage-one equivariant indexed middle decks satisfying (1.1), and
2. binary words satisfying the `N` class-sum equations

   \[
   \sum_{x\in\mathbb Z_k}c_{j-xN}=r
   \qquad(j\in\mathbb Z_N).                            \tag{2.1}
   \]

The inverse map is

\[
 c_i={\bf1}_{\{0\in T_i\}}.                            \tag{2.2}
\]

#### Proof

Equation (1.2) gives

\[
x\in T_{i+N}(c)
\iff c_{i+N-xN}=1
\iff c_{i-(x-1)N}=1
\iff x-1\in T_i(c),
\]

which is (1.1).  Its rank is the left side of (2.1).  Conversely, if
(1.1) holds, then

\[
x\in T_i
\iff 0\in \rho^{-x}T_i=T_{i-xN},
\]

so (2.2) recovers (1.2) uniquely.  \(\square\)

A unit-voltage deck `T_(i+N)=rho^v T_i` is reduced to (1.1) by the coordinate
multiplier `x -> v^{-1}x`.  Thus the normal form loses no unit-voltage deck.

## 3. Every carrier gate in `c`-space

The following consequences are exact.

### Johnson condition

By equivariance it is enough to impose, for `j in Z_N`,

\[
 \sum_{x\in\mathbb Z_k}
 \big(c_{j-xN}\mathbin{\mathsf{xor}}c_{j+1-xN}\big)=2. \tag{3.1}
\]

Then every physical transition is a Johnson edge.

### Hamilton condition

Rotation acts freely on ranks `m` and `m+1`: a stabilizer orbit length
`t|k` fixing such a set would divide `2 rank-k=+-1`.  Hence the deck is a
Hamilton ordering of the entire rank-`r` layer if and only if

\[
 T_0,\ldots,T_{N-1}
\]

belong to pairwise distinct rotation orbits.

### Exact first lower rainbow

Under (3.1), put `R_j=T_j cap T_(j+1)`.  Each `R_j` has rank `r-1=m`, whose
rotation action is also free.  The physical first lower shadow is exact if
and only if the `N` representatives `R_0,...,R_(N-1)` lie in distinct
rotation orbits.

### Residence

For every coordinate `x`,

\[
 {f1}_{\{x\in T_i\}}=c_{i-xN}.                       \tag{3.2}
\]

Thus all coordinate traces are cyclic shifts of the single word `c`.
Depth-`d` residence is exactly the assertion that `c` has no cyclic run of
ones of length `1,...,d`.

### Deeper shadows

For every `q>=0`,

\[
x\in\bigcap_{t=0}^{q}T_{i+t}
\iff \bigwedge_{t=0}^{q}c_{i+t-xN}=1,                 \tag{3.3}
\]

and

\[
x\in\bigcup_{t=0}^{q}T_{i+t}
\iff \bigvee_{t=0}^{q}c_{i+t-xN}=1.                  \tag{3.4}
\]

Equivariance reduces orbit coverage to the `N` base starting positions, but
does not bound the required window width.

## 4. Exact CEGAR clauses

This section records the distinction between a sound positive search and a
sound impossibility result.

Suppose two current quotient columns `a,b` lie in the same middle orbit.
Forbidding the current assignment of column `b` alone is invalid: a valid
solution may retain `b` and change `a`.  The exact collision nogood is the
single clause saying that at least one `c`-literal in the **joint current
assignments of both columns** changes.  The same joint-assignment rule
applies to a collision of two first-shadow edges; there the support is the
union of the two adjacent column pairs.

For a missing upper target `S`, it is not complete to demand a witness only
at widths near `|S|-r`.  A Johnson walk can remain inside `S` for arbitrarily
many transitions before the last member of `S` is first introduced.  Exact
coverage is

\[
 \exists i,\ell:\quad
 T_i\cup\cdots\cup T_{i+\ell}=S,                      \tag{4.1}
\]

with arbitrary cyclic `ell`.  A complete implementation must use one of:

1. all-width selectors;
2. an exact finite-state/separation formulation for (4.1); or
3. a full-current-state nogood after an exact audit.

Option 3 is weak but logically complete.  Restricting widths is a useful
sufficient search lane, but an UNSAT result in that lane is not an
obstruction to the original problem.

## 5. Compiler boundary

A binary word passing (2.1), (3.1), Hamiltonicity, residence, and all shadow
audits is only a decorated carrier.  It is not yet a word certificate.
Coefficient one additionally requires:

1. the cyclic envelope `P` at depth `d`;
2. an exact one-core `C<=P` satisfying `DC=DP`;
3. exact weighted quotient Hall and then a physical matching;
4. a safe linear cut; and
5. literal exhaustive verification of the emitted word.

The forced-port mask alone is not an exact one-core.  Therefore the correct
search object is a compiler-ready pair `(c,C)`, or a Benders loop alternating
binary carrier selection with exact one-core/Hall counterexamples.

## 6. Current finite calibration

The normal form reconstructs the saved strict equivariant `k=9` and `k=11`
carriers with zero Johnson, residence, Hamilton, first-shadow, lower-`q2`,
and upper defects.  Claude's current unseeded `k=11` CEGAR has not yet found
one because its collision clauses are over-strong and its all-different
encoding is weak.  This is a solver issue, not a defect in Theorem 2.1.

No `k=15` PASS or word follows from this note.  The rigorous frontier remains

\[
 6438\le \nu(15)\le6458.
\]
