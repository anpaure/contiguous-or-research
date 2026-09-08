# OFHT: the Ferrers top-rail Hall cut and the chronology-correlation barrier

Date: 2026-08-01  
Lane: R, one-copy named rotor flag-colouring  
Status: unconditional exact cut theorem and probabilistic no-go for
ownerwise/high-entropy selection.  The theorem applies to strict
positive-age short/long/mixed rotor templates realizing the complete
Ferrers role multiset, with the optional normalization of unmarked zero
roles to full-source forced loops.  It excludes arbitrary zero-containing
age templates.  It does **not** refute OFHT: a chronology-first
selection may deliberately create the large conditional correlations which
the theorem proves necessary.

## 0. Outcome

Let

\[
 k\in\{2r-1,2r\},\qquad W=\binom{k}{r},
\]

and let a canonical Ferrers rotor template have depth \(d\).  Exactness of
only the top \(L\) named-target rows already forces almost all roles to be
**terminal rails**.  More precisely, for

\[
 1\le L\le \min\{d,r-d-1\},
\]

at least

\[
 W\left(1-\frac{L(L+1)(2L+1)}{6r}\right)                 \tag{0.1}
\]

roles have their last \(L\) age cells equal to singletons.

For such a state \(X\), every positive literal successor must copy an
ordered \((L-1)\)-tuple of those singleton cells and must live over one of
the \(k-r\) external owners in the exact terminal star.  This gives an
explicit Hall-cut family in the selected NRFC graph.

Under a candidate-selection law whose conditional distribution inside
every owner/type fibre is at most \(K\) times uniform, the probability that
one top-rail state has even one available positive successor is at most

\[
             \mu_L=\frac{K(k-r)}{(r)_{L-1}}.                 \tag{0.2}
\]

Consequently, with probability at least \(1-\sqrt{\mu_L}\), the exact
cycle-cover Hall deficiency is at least

\[
 (1-\sqrt{\mu_L})
 W\left(1-\frac{L(L+1)(2L+1)}{6r}\right).             \tag{0.3}
\]

For \(L=3\), an ownerwise product nibble has deficiency
\((1-o(1))W\) with probability \(1-o(1)\).  Thus the exponentially large
Ferrers buffers do not create expansion after independent flags have been
chosen.  Any successful probability measure supported on OFHT solutions
must amplify some compatible successor fibre above uniform by at least

\[
                         \frac{(r)_{L-1}}{k-r}.               \tag{0.4}
\]

The positive gate is therefore a chronology-first correlated rail matching,
not a one-point-symmetric or bounded-bias nibble.

## 1. Exact selected-state setting

Use the owner-changing age states and literal recurrence of
`MATH_THEOREM_R_NRFC_LABELLED_COMPATIBILITY_HALL_AND_OWNER_SYMMETRY_LIMIT_20260801.md`.
Thus a state is

\[
 X=(X_0,\ldots,X_d),\qquad T(X)=\dot\bigcup_iX_i\in\binom{[k]}r,
\]

and

\[
 X\longrightarrow Y
 \quad\Longleftrightarrow\quad
 Y_{i+1}=X_i\setminus Y_0\quad(0\le i<d),             \tag{1.1}
\]

together with the declared role-transition relation.

Fix one selected state per role and one state per rank-\(r\) owner.  The
strict uniform realization uses positive states, for which every `X_i` is
nonempty.  In particular, the original fractional construction may realize
an unmarked zero signature by the positive state

\[
                         H=(r-d,1,\ldots,1)
\]

with no marks.  It is also legal, as an explicitly chosen normalization of
an unmarked zero role, to use the full-source state

\[
                         Z_T=(T,\varnothing,\ldots,\varnothing). \tag{1.2}
\]

The theorem covers strict positive states together with any such prepared
full-source states.  The positive-composition long rotors, the mixed rotors
with their appended singleton rail, and the short state `H` are strict.

### Lemma 1.1 (forced full-source loops)

In a one-state-per-owner section, a selected state with \(X_d=\varnothing\)
has no possible successor owner other than \(T(X)\).  Its only possible
selected head is therefore itself.  The literal self-edge \(X\to X\)
exists if and only if

\[
                         X_1=\cdots=X_d=\varnothing.             \tag{1.3}
\]

Hence, if its declared role relation contains the self-edge, every selected
full-source state \(Z_T\) is forced to use its loop in every successor
perfect matching.  If that self-edge is absent, or if any other
zero-terminal state is selected, there is already a singleton Hall
obstruction.

#### Proof

The terminal-star formula permits deletion only from \(X_d\), so
\(X_d=\varnothing\) fixes the owner.  There is one selected state over that
owner.  Substituting \(Y=X\) in (1.1) gives

\[
 X_{i+1}=X_i\setminus X_0=X_i\qquad(i\ge1),
\]

because the age cells are disjoint.  Adjacent disjoint equal cells are
empty, and induction gives (1.3).  Conversely (1.2) plainly has its literal
self-edge.  \(\square\)

Let \(\mathcal Z\) be the selected full-source states with declared
self-edges.  Their tails have no alternative heads, so contraction of their
forced tail--head loops preserves perfect-matching feasibility and the
residual deficiency.  Below, “positive head” means a head remaining after
this contraction.

Arbitrary zero-containing types are intentionally excluded.  For example,
`(2,1,0,1)` can offer two consecutive top ranks without having two terminal
singleton cells.  Lemma 2.2 is therefore a strict-age statement.

## 2. Exact size of the forced top rail

For \(1\le j\le L\), let \(M_j\) be the set of roles marked at rank
\(r-j\), and put

\[
                              B_L=\bigcap_{j=1}^L M_j.           \tag{2.1}
\]

The condition \(L\le r-d-1\) places these ranks above the Ferrers deletion
boundary, so exact named-target coverage gives

\[
                              |M_j|=\binom{k}{r-j}.              \tag{2.2}
\]

### Theorem 2.1 (Ferrers top-rail census)

For both central parities,

\[
 1-\frac{\binom{k}{r-j}}{W}\le\frac{j^2}{r},                   \tag{2.3}
\]

and consequently

\[
 |B_L|\ge
 W\left(1-\frac1r\sum_{j=1}^Lj^2\right)
 =W\left(1-\frac{L(L+1)(2L+1)}{6r}\right).                    \tag{2.4}
\]

#### Proof

For \(k=2r\),

\[
 \frac{\binom{2r}{r-j}}{\binom{2r}{r}}
 =\prod_{i=0}^{j-1}\frac{r-i}{r+i+1}.
\]

Using \(1-\prod_i(1-a_i)\le\sum_i a_i\), its deficit is at most

\[
 \sum_{i=0}^{j-1}\frac{2i+1}{r+i+1}
 \le\frac{j^2}{r}.
\]

For \(k=2r-1\), the \(j=1\) ratio is one, and for \(j\ge2\),

\[
 \frac{\binom{2r-1}{r-j}}{\binom{2r-1}{r}}
 =\prod_{i=0}^{j-2}\frac{r-1-i}{r+1+i}.
\]

Its deficit is at most

\[
 \sum_{i=0}^{j-2}\frac{2i+2}{r+1+i}
 \le\frac{j(j-1)}r\le\frac{j^2}r.
\]

Finally,

\[
 U\setminus B_L=\bigcup_{j=1}^L(U\setminus M_j),
\]

so the union bound together with (2.2)--(2.3) proves (2.4).  \(\square\)

### Lemma 2.2 (consecutive marks force singleton terminal ages)

For every role \(u\in B_L\), its selected positive state satisfies

\[
                  |X_{d-L+1}|=\cdots=|X_d|=1.                 \tag{2.5}
\]

#### Proof

The proper prefix ranks of a positive state are strictly increasing, and
their successive differences are the positive age-cell sizes.  Since the
state offers every consecutive rank

\[
                         r-L,r-L+1,\ldots,r-1,
\]

its final \(L\) increments are all one.  \(\square\)

This is stronger than merely observing a large formal buffer coordinate:
the complete top Ferrers rows force a rail bank of size \((1-o(1))W\) for
every fixed \(L\).

## 3. The exact terminal rail-star Hall cut

For a selected rail state \(X\in B_L\), define its ordered outgoing rail
signature

\[
             \sigma_L(X)=(X_{d-L+1},\ldots,X_{d-1}).           \tag{3.1}
\]

It has length \(L-1\).

### Lemma 3.1 (forced rail shift and external owner)

If \(X\in B_L\) and \(Y\) is a positive literal successor, then

\[
        (Y_{d-L+2},\ldots,Y_d)=\sigma_L(X),                    \tag{3.2}
\]

and

\[
        T(Y)=T(X)-X_d+e\qquad\text{for some }e\in[k]\setminus T(X).
                                                                    \tag{3.3}
\]

Thus exactly \(k-r\) external owner fibres can contain a positive
successor.

#### Proof

For \(d-L+1\le i<d\), (1.1) gives

\[
                         Y_{i+1}=X_i\setminus Y_0.
\]

The left side is nonempty and the right side is a subset of the singleton
\(X_i\), proving (3.2).  The terminal-star theorem and \(|X_d|=1\)
allow either the same owner or precisely the exchanges (3.3).  In the
same-owner case the unique selected head is \(X\) itself, but a positive
state has \(X_1\ne\varnothing\), so Lemma 1.1 forbids \(X\to X\).
\(\square\)

For \(A\subseteq B_L\), let \(R_L(A)\) be the set of selected positive
heads which, for at least one \(X\in A\), satisfy the declared role edge,
the owner condition (3.3), and the forced ordered shift (3.2).  Other age
rows may reduce this set further.

### Theorem 3.2 (deterministic rail-star deficiency cut)

For every \(A\subseteq B_L\),

\[
 N^+(A\cup\mathcal Z)\cap\mathcal X
       \subseteq R_L(A)\cup\mathcal Z,                         \tag{3.4}
\]

and hence the exact selected-state Hall deficiency satisfies

\[
             \delta(\mathcal X)\ge |A|-|R_L(A)|.               \tag{3.5}
\]

In the forced-loop-contracted graph, (3.5) is the ordinary Hall cut
\(|A|-|N^+(A)|\).

#### Proof

Lemma 3.1 contains every positive successor of a rail state in \(R_L(A)\).
The only remaining possible selected successors are full-source states.
By Lemma 1.1, tails in \(\mathcal Z\) have only their own heads.  This
proves (3.4).  Therefore

\[
 |A\cup\mathcal Z|-|N^+(A\cup\mathcal Z)\cap\mathcal X|
 \ge |A|+|\mathcal Z|-|R_L(A)|-|\mathcal Z|,
\]

which is (3.5).  \(\square\)

This cut belongs to the literal NRFC graph; it is not an owner-projection
or rankwise relaxation.

## 4. Exact two-bank min--max after a transversal is selected

The near-spanning rail bank also gives a useful exact reformulation of the
positive cycle-cover test.  Work in the graph after contracting
\(\mathcal Z\).  Let \(H\) be its head ground set, let \(B=B_L\) be the
rail tails, and let \(C\) be the complementary tails.  Thus

\[
                         |H|=|B|+|C|.
\]

On ground set \(H\), define the head-transversal matroid \(M_B\): a subset
of heads is independent when it can be matched to distinct tails of \(B\).
Define \(M_C\) analogously.

### Theorem 4.1 (rail/complement common-base criterion)

The selected literal graph has a successor perfect matching if and only if

\[
                         r_{M_B}(S)+r_{M_C}(S)\ge |S|
                         \qquad(S\subseteq H).                  \tag{4.1}
\]

The rail rank in (4.1) is computed from the **full literal recurrence**.
Lemma 3.1 gives only a necessary rail-star supergraph and therefore an
upper bound on this rank: earlier age rows can delete rail-star edges.

#### Proof

Put \(q=|C|\).  A perfect matching is equivalent to choosing a \(q\)-set
\(J\subseteq H\) which is a base of \(M_C\) and whose complement is a
base of \(M_B\).  Equivalently, \(J\) is a common base of \(M_C\) and the
dual matroid \(M_B^*\).  Edmonds' matroid-intersection min--max gives the
criterion

\[
 r_{M_C}(S)+r_{M_B^*}(H\setminus S)\ge q
                         \qquad(S\subseteq H).
\]

The dual-rank formula gives

\[
 r_{M_B^*}(H\setminus S)
 =|H\setminus S|-r_{M_B}(H)+r_{M_B}(S).
\]

The displayed inequalities at \(S=H\), together with the rank upper
bounds, force \(r_{M_B}(H)=|B|\) and \(r_{M_C}(H)=q\).  Substitution then
reduces them exactly to (4.1).  Conversely (4.1), at \(S=H\) and at every
other \(S\), supplies these full ranks and the common-base inequalities.
\(\square\)

This is not an OFHT existence proof: selecting the state transversal while
retaining all nested target rows is still outside the two fixed matroids.
It is the exact min--max that a chronology-first construction has to make
true.

For example, at `d=L=3`,

\[
 X=(\{1\},\{2\},\{3\},\{4\}),\qquad
 Y=(\{1\},\{5\},\{2\},\{3\})
\]

pass the owner exchange and ordered two-singleton suffix tests, but fail
`Y_1=X_0\setminus Y_0`.  Thus the rail-star supergraph cannot replace the
literal matroid.

## 5. A quantitative no-go for ownerwise nibbling

We now formalize “bounded-bias ownerwise selection.”  Conditional on a
selected rail state \(X\), fix an external owner \(T'\) from (3.3) and a
positive target type \(c'\).  Suppose that, conditional also on type \(c'\)
being placed over \(T'\), the chosen partition has the spread bound

\[
 \Pr(Y\in\mathcal S\mid X,c',T')
 \le K\frac{|\mathcal S|}{|\Omega_{c'}(T')|}                  \tag{5.1}
\]

for every subset \(\mathcal S\) of that owner/type fibre.  No independence
between different owners is assumed.

### Lemma 5.1 (exact ordered-suffix slice)

If the cells in the positions \(d-L+2,\ldots,d\) of type \(c'\) are
singletons, the fraction of partitions in one owner fibre which equal a
fixed ordered \((L-1)\)-tuple there is exactly

\[
                              \frac1{(r)_{L-1}}.                \tag{5.2}
\]

If any one of those cell sizes is not one, the required slice is empty.

#### Proof

There are \(r!/\prod_i c'_i!\) partitions of the owner.  After fixing the
ordered singleton contents, the remaining count is

\[
                         \frac{(r-L+1)!}{\prod_{i\notin I}c'_i!},
\]

where \(I\) is the set of the fixed singleton positions.  Their ratio is
\((r-L+1)!/r!=1/(r)_{L-1}\).  \(\square\)

### Theorem 5.2 (Ferrers anti-nibble theorem)

Under (5.1), every selected rail source is nonisolated in the contracted
positive-head graph with probability at most

\[
                              \mu_L=\frac{K(k-r)}{(r)_{L-1}}.   \tag{5.3}
\]

If \(\mu_L\le1\), then with probability at least
\(1-\sqrt{\mu_L}\), the exact Hall deficiency is at least

\[
 (1-\sqrt{\mu_L})|B_L|
 \ge (1-\sqrt{\mu_L})W
    \left(1-\frac{L(L+1)(2L+1)}{6r}\right).                   \tag{5.4}
\]

#### Proof

For each of the \(k-r\) external owners, condition on its selected positive
type.  Lemma 5.1 and (5.1) bound the probability of the forced signature by
\(K/(r)_{L-1}\).  A union bound proves (5.3); additional role and age-row
constraints can only decrease this probability.

Let \(Q\) be the number of nonisolated rail sources.  Linearity of
expectation gives

\[
                              \mathbb E Q\le\mu_L|B_L|.
\]

Markov's inequality gives

\[
 \Pr\{Q>\sqrt{\mu_L}|B_L|\}\le\sqrt{\mu_L}.
\]

On the complementary event, take \(A\) to be the isolated rail states and
apply Theorem 3.2.  This proves (5.4).  \(\square\)

The standard ownerwise product model, including uniform random assignment
of role types to owners followed by a uniform partition inside every owner,
has \(K=1\) after conditioning on the type at an external owner.  Exact
nested-target conditioning is not a product model and is not covered by
this assertion.

### Corollary 5.3 (the first explicit scale)

For \(L=3\),

\[
 |B_3|\ge W(1-14/r),\qquad
 \mu_3=\frac{K(k-r)}{r(r-1)}\le\frac K{r-1}.                  \tag{5.5}
\]

Thus \(K=1\) gives deficiency \((1-o(1))W\) with probability
\(1-o(1)\).  More generally, for any fixed \(C\), choosing a fixed
\(L>C+2\) defeats every \(K\le r^C\), once the canonical depth permits
that \(L\).  If \(L=o(r^{1/3})\), the rail census remains
\((1-o(1))W\); hence the same calculation excludes every
\(K=\exp(o(r^{1/3}\log r))\) by choosing \(L\) to dominate
\(\log K/\log r\), provided \(L\le d\).

## 6. Necessary correlation in every successful measure

### Corollary 6.1 (successor-fibre amplification)

Let a probability measure be supported on genuine OFHT cycle covers of the
fixed strict-or-full-source role template.  Conditional on a selected rail
state `X`, let `q_(e,c)` be the probability that external owner `e` carries
positive type `c`, and let `s_(e,c)` be the further conditional probability
of its required ordered-suffix slice.  Full-source heads are already
consumed by forced loops, so

\[
 \sum_{e,c}q_{e,c}s_{e,c}\ge1,
 \qquad \sum_{e,c}q_{e,c}=k-r.                              \tag{6.1}
\]

Therefore some owner/type fibre has conditional density, relative to its
uniform ordered-suffix slice, at least

\[
                              \frac{(r)_{L-1}}{k-r}.             \tag{6.2}
\]

#### Proof

If every occupied owner/type fibre had suffix probability below
`1/(k-r)`, the first sum in (6.1) would be below one.  Hence some fibre has
suffix probability at least `1/(k-r)`.  Lemma 5.1 gives uniform slice
density `1/(r)_(L-1)`, proving (6.2).  \(\square\)

For fixed \(L\ge3\), the required amplification is polynomially unbounded;
for growing \(L\) it is superpolynomial.  Exponential multiplicity of roles
does not alter this per-source conditional requirement.

## 7. Exact implication boundary

The following are proved here.

1. In every strict-or-full-source canonical package template, the complete
   Ferrers top rows force the near-spanning rail bank (2.4), independently
   of how its positive short/long/mixed packages are decomposed.
2. Terminal-star geometry and literal age equality give the exact ordered
   rail constraint (3.2)--(3.3).
3. These constraints give the deterministic NRFC Hall cuts (3.4)--(3.5)
   and the exact rail/complement common-base min--max (4.1).
4. Every bounded-bias ownerwise nibble has the quantitative deficiency
   (5.4).  In particular, exponential buffer multiplicity does not rescue
   independent owner/flag selection.

This does **not** prove that the canonical Ferrers OFHT instance is
infeasible.  The complete nested-target rows may be selected together with
successor arcs and thereby create precisely the amplification (6.2).  A
positive theorem must now be stated in that chronology-first form:

> choose the common owner--flag section and its rail successor matching
> simultaneously so that the two-bank rank cuts (4.1) hold, rather than
> first choosing an ownerwise section and then invoking symmetry or a
> nibble.

After OFHT, connectivity, residence, upper/deep shadows, and common-cap
compiler compatibility remain separate.  No \(B(k)+O(1)\) or equality
claim follows from this note.
