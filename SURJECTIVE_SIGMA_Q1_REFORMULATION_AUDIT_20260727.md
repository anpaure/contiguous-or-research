# The surjective-\(\sigma\) reformulation: exact at depth one

Date: 2026-07-27

## 1. Verdict

Let \(k=2r-1\).  The proposed map

\[
\sigma:\binom{[k]}{r-1}\longrightarrow\binom{[k]}{r+1},
\qquad X\subset\sigma(X),
\]

is an exact and very useful reformulation of the **two-sided immediate-shadow
problem**.  It packages a lower-rainbow middle-level 2-factor and its upper
union colours into one local choice at each \((r-1)\)-set.

Three qualifications are essential.

1. Surjectivity is not the only constraint: the degree-two equations are a
   coupled integral constraint, and connectedness is a further global one.
2. A surjective Hamiltonian \(\sigma\) solves depth \(q=1\), but it does not
   enforce the minimum-residence condition needed to write the middle path as
   \(D^dA\).
3. It does not by itself cover the upper ranks \(r+2,r+3,\ldots\).  Those are
   higher-window conditions, not consequences of capacity.

Thus the reformulation sharply reduces the first open finite gate, especially
at \(k=11\), but it does not collapse the whole formula \(\nu(k)=B(k)\) to one
map.

## 2. Ballot blocks from the lower rainbow

Let \(T_0,\ldots,T_{W-1}\) be a cyclic ordering of all rank-\(r\) sets whose
consecutive intersections enumerate every rank-\((r-1)\) set once.  For a
fixed \(t\)-set \(Q\), put

\[
S_Q=\{i:Q\subseteq T_i\}.
\]

The number \(b_Q\) of cyclic blocks of \(S_Q\) is

\[
\begin{aligned}
b_Q
&=|S_Q|-\#\{i:Q\subseteq T_i\cap T_{i+1}\}\\
&=\binom{2r-1-t}{r-t}-\binom{2r-1-t}{r-1-t}\\
&=\boxed{\frac tr\binom{2r-1-t}{r-t}}.
\end{aligned}
\tag{2.1}
\]

For a path with missing lower colour \(C_*\), the right side gains
\(\mathbf 1_{Q\subseteq C_*}\).  Hence the complete ballot block profile is
indeed forced by the one-hole lower rainbow; it is not an independent design
condition.

In particular, each coordinate has exactly \(C_{r-1}\) cyclic containing
blocks.

## 3. The immediate upper excess design

Let

\[
A_i=T_i\cup T_{i+1}\in\binom{[k]}{r+1},
\qquad
\mu(A)=|\{i:A_i=A\}|.
\]

If every upper target is covered, define the nonnegative excess multiset

\[
\widetilde D(A)=\mu(A)-1.
\]

Then

\[
|\widetilde D|
=W-\binom{k}{r+1}
=\boxed{C_r}.
\tag{3.1}
\]

For every coordinate \(x\), (2.1) with \(t=1\) gives

\[
\sum_{A\ni x}\mu(A)
=|S_x|+b_x
=\binom{2r-2}{r-1}+C_{r-1}.
\]

After subtracting the complete rank-\((r+1)\) layer,

\[
\boxed{d_{\widetilde D}(x)=2C_{r-1}}
\qquad(x\in[k]).
\tag{3.2}
\]

Without upper coverage, the same identity holds for the **signed** multiset
\(\mu-1\), but it is not yet an excess design.  This is the only hypothesis
missing from the two-line calculation.

If \(k=2r-1\ge5\) is prime, then

\[
C_r=\frac{2k}{r+1}C_{r-1},
\qquad k\mid C_r.
\tag{3.3}
\]

The cyclic action is free on the nontrivial subset levels.  A full orbit of an
\((r+1)\)-set has size \(k\) and coordinate degree \(r+1\), so any union of
\(C_r/k\) such orbits is a simple regular design with exactly the parameters
(3.1)--(3.2).  This proves that the **static** excess parameters have no
arithmetic obstruction.  It does not yet couple that design to a middle-level
2-factor.

## 4. Exact \(\sigma\)-theorem

For every \(X\in\binom{[k]}{r-1}\), write

\[
\sigma(X)\setminus X=\{a_X,b_X\}
\]

and put into \(G_\sigma\) the two middle-level edges

\[
X--(X+a_X),\qquad X--(X+b_X).
\]

Then every left vertex has degree two, while

\[
\deg_{G_\sigma}(Y)
=\#\left\{X\in\binom{Y}{r-1}:Y\subseteq\sigma(X)\right\}.
\tag{4.1}
\]

Consequently:

> **Theorem 4.1.**  \(G_\sigma\) is a spanning 2-factor of the middle-levels
> graph if and only if the quantity in (4.1) equals two for every rank-\(r\)
> set \(Y\).  If this 2-factor is one Hamilton cycle, then its rank-\(r\)
> projection is lower-rainbow, and the immediate upper-union multiset is
> exactly \(\{\sigma(X):X\in\binom{[k]}{r-1}\}\).

Indeed, at the passage

\[
Y_i-X-Y_{i+1}
\]

one has

\[
Y_i\cap Y_{i+1}=X,
\qquad
Y_i\cup Y_{i+1}=\sigma(X).
\tag{4.2}
\]

It follows that

\[
\boxed{\text{doubly-rainbow depth-one cycle}}
\quad\Longleftrightarrow\quad
\boxed{\text{surjective \(\sigma\), degree two, and connected}}.
\tag{4.3}
\]

This equivalence is exact.

## 5. What Hall proves, and what it does not

In the containment graph from rank \(r-1\) to rank \(r+1\), the two degrees
are \(\binom r2\) and \(\binom{r+1}2\).  Thus for every family \(\mathcal A\)
of upper sets,

\[
|N(\mathcal A)|\binom r2
\ge |\mathcal A|\binom{r+1}2,
\]

so \(|N(\mathcal A)|>|\mathcal A|\).  Hall therefore supplies an injection
of the upper layer into the lower layer, and hence a surjective containment
map after assigning the unused lower sets arbitrarily.

This proves that **surjectivity by itself** is abundant.  It says nothing
about the degree-two equations (4.1): choosing one value \(\sigma(X)\)
simultaneously consumes two degree units at rank \(r\) and one upper colour.
The resulting object is a pair-choice exact-cover problem (and, after adding
connectedness, a global transition-factor problem), not an ordinary Hall
matching.

In binary variables

\[
z_{X,A}=\mathbf1_{\sigma(X)=A}
\qquad (X\in\tbinom{[k]}{r-1},\ A\in\tbinom{[k]}{r+1},\ X\subset A),
\]

the exact q1 system is

\[
\begin{aligned}
\sum_{A\supset X}z_{X,A}&=1 &&\text{for every }X,\\
\sum_{X\subset Y\subset A}z_{X,A}&=2 &&\text{for every }Y,\\
\sum_{X\subset A}z_{X,A}&\ge1 &&\text{for every }A.
\end{aligned}
\tag{5.1}
\]

The constant fractional point

\[
z_{X,A}=\binom r2^{-1}
\tag{5.2}
\]

satisfies the first two systems exactly and gives every upper target load

\[
\frac{\binom{r+1}{2}}{\binom r2}=\frac{r+1}{r-1}>1.
\]

Thus there is no fractional capacity obstruction.  Integrality is genuine:
for one fixed \(X\) and three outside elements \(a,b,c\), the three variables
for \(X+ab,X+ac,X+bc\), restricted to the three middle-degree rows
\(X+a,X+b,X+c\), form the triangle incidence matrix, whose determinant has
absolute value two.  Hence the constraint matrix is not totally unimodular.

Mere surjectivity does **not** force upper loads to lie in \(\{1,2\}\).
Loads three and higher are allowed.  The profile \(1^{18}2^{12}\) at
\(k=11\) follows only after imposing the additional cap
\(\sum_{X\subset A}z_{X,A}\le2\), equivalently a simple excess design or
CPCR zero at q1.

## 6. Prime quotient and the \(k=11\) instance

For prime \(k\), equivariance reduces the counts to

\[
\frac1k\binom{k}{r-1}=C_{r-1},
\qquad
\frac1k\binom{k}{r+1}=\frac{r-1}{r+1}C_{r-1}.
\]

At \(k=11\), \(r=6\):

| item | quotient count |
|---|---:|
| rank-five variables | 42 |
| choices per variable | 15 |
| rank-six degree equations | 42 |
| rank-seven coverage inequalities | 30 |
| unavoidable upper excess | 12 orbit-units |

These counts are correct.  Each variable chooses a pair of quotient edges and
one upper orbit.  A candidate is Hamiltonian precisely when the resulting
84-vertex quotient 2-factor is one cycle and its voltage is nonzero in
\(\mathbb Z_{11}\); then its lift is a single 924-vertex alternating cycle.

The relaxed integral part is already solved.  The complemented centered PBBS
factor is translation-equivariant and supplies a degree-two \(\sigma\) whose
upper loads are between one and three.  Thus it covers every upper orbit.
Moreover its quotient has at least one nonzero-voltage component: if every
component had zero voltage, every lifted PBBS component length would force the
total quotient size to be divisible by 11, contradicting \(42\not\equiv0
\pmod {11}\).

Therefore the 42-variable system **without connectedness or cap two** is not
open.  What remains is a connected quotient cycle (and, for the stronger
CPCR-zero normal form, upper loads \(1^{18}2^{12}\)).  The system is still a
small mathematical CSP specification, but “SAT-trivial” is not a theorem:
the pair constraints are coupled, and connectivity/voltage are global.  See
`MATH_PRIME_EQUIVARIANT_SIGMA_FACTOR_AUDIT_20260727.md`.

## 7. Cutting the cycle

Suppose a surjective Hamiltonian \(\sigma\) exists.  Because

\[
W>\binom{k}{r+1},
\]

some upper colour has multiplicity at least two.  Cut the corresponding
projected adjacency.  The resulting ordering of all \(W\) rank-\(r\) sets
has:

- exactly one missing lower colour, namely the cut \((r-1)\)-set;
- no missing immediate upper colour, because the removed upper colour has
  another occurrence.

This part of the proposed \(k=11\) reduction is correct.

## 8. The gates that remain after the cut

The cut path is not automatically a central derivative of an optimal word.
For \(T=D^dA\), every internal coordinate run of \(T\) must have length at
least \(d+1\), together with the endpoint compatibility conditions.  An
arbitrary middle-level Hamilton cycle can have many runs of length two or
three.  The known \(k=11\) q1-perfect connector is an explicit example: it
has both immediate rainbows but fails delay-three residence in many places.

Likewise, surjectivity of \(\sigma\) covers rank \(r+1\), but a three-vertex
window is a rank-\((r+2)\) condition and is not determined by (4.1).  For
\(k=11\), rank seven is solved by \(\sigma\); rank eight remains a separate
q2 condition.

Finally, a disconnected surjective 2-factor cannot yet be assumed mergeable
without loss.  A cycle-joining switch must preserve the rank-six degree
equations, retain every rank-seven colour, and ultimately respect residence.
The available upper excess is a useful reservoir, not an automatic joining
theorem.

The exact local **marginal** algebra is now known.  On a four-coordinate
Boolean octahedron, every integral change preserving the lower loads, middle
degrees, and complete upper-load vector is an integer circulation of \(K_4\).
Its primitive simple moves are:

- an alternating six-edge triangle (the alpha trade); and
- an eight-edge four-cycle trade, which reconnects the same external ports
  and is component-inert.

There is no nontrivial two-row trade.  The component effect of an alpha trade
is **not** determined just by how many old cycles contain its three deleted
edges: it depends on the pairing/interlacement of the six exposed strands.
In particular, a single alpha trade can merge either three components or two
components, so the earlier proposed component-parity invariant is false.
The three removed alpha edges all flip the same spare coordinate.  Therefore,
inside an \(H\)-fresh chronology, the two cuts needed on one component are
automatically separated by more than \(H\); binary absorption is locally
small in chord support but nonlocal in time.  The exact strand-pairing
criterion and the global supply of residence-safe charts remain the joining
gate.  See
`PRESCRIBED_DESIGN_CYCLE_JOINING_THEOREM_20260727.md`.

For the complemented PBBS seed at (k=11), this supply question now has a
sharp negative answer in its static form.  Cyclic-parenthesis analysis gives
38 translation-orbits (418 labelled instances) of canonical pure alpha
charts, but the alternating PBBS component is incident with **no** alpha
chart at all, including mixed charts.  Hence the initial factor admits no
static spanning alpha-absorption tree.  A successful alpha route must first
create a portal to that component by a preliminary marginal-preserving
commutator, or use a larger trade that touches it directly.  See
`K11_PBBS_ALPHA_CHART_SYMBOLIC_AUDIT_20260727.md`.

## 9. Revised finite target

The highest-value finite question is therefore:

> Can the relaxed equivariant PBBS \(\sigma\)-factor be joined, through
> marginal-preserving trades that first create a portal to its isolated
> alternating component, into one nonzero-voltage quotient cycle,
> and can the joined chronology be chosen so that after a safe cut it has
> delay-three residence and the required rank-eight coverage?

Adding cap two asks simultaneously for the stronger upper profile
\(1^{18}2^{12}\).  It is useful but not necessary for q1 coverage.  The
residence and q2 clauses are the still-open interface to \(\nu(11)=465\).
