# Functional tensor disintegration and the odd-portal obstruction

## Status and purpose

This note isolates the exact gap between a stationary fractional literal
turn circulation and a one-owner-once functional attachment.  It proves a
positive disintegration theorem whenever the predecessor and owner choices
are conditionally independent (or a bounded rail-state mixture of such
products).  It also gives the exact linear feasibility system in general
and identifies the first possible support obstruction: a portal-free clean
physical `C5`.

Nothing below proves that the stationary pull-clock tensor has the required
product structure.  The result is a proof-safe criterion for when the
fractional-to-functional step is automatic and a sharp description of how
it can fail.

## 1. The turn tensor

Let `P,Q,O` be three finite shores of the same cardinality `N`.  Think of
`P,Q` as tail and head roots and `O` as owners.  Let

\[
 \mathcal E\subseteq P\times Q\times O
\]

be the legal literal turn atoms.  A fractional perfect turn tensor is a
nonnegative tensor `x=(x_{pqo})`, supported on `E`, such that

\[
 \sum_{q,o}x_{pqo}=1,\qquad
 \sum_{p,o}x_{pqo}=1,\qquad
 \sum_{p,q}x_{pqo}=1                         \tag{1.1}
\]

for every `p,q,o`, respectively.

Its head--owner projection

\[
                         y_{qo}:=\sum_p x_{pqo}                 \tag{1.2}
\]

is doubly stochastic.  In the Boolean application its support lies in the
middle-level incidence graph `q subset o`.  Hence Birkhoff--von Neumann
decomposes `y` into incidence bijections

\[
 y=\sum_{\theta\in\Theta}\lambda_\theta\chi^\theta,
 \qquad \lambda_\theta\ge0,
 \qquad \sum_\theta\lambda_\theta=1,             \tag{1.3}
\]

where `theta:Q -> O` is a bijection and
`chi^theta_{qo}=1_{o=theta(q)}`.

The point requiring proof is that a decomposition of the projection need
not lift to a decomposition of the whole tensor.

### Definition 1.1 (functional disintegration)

A functional disintegration of `x` consists of weights
`lambda_theta` and doubly stochastic tail--head matrices
`A^theta=(a^theta_{pq})` such that

\[
 x_{pqo}=\sum_{\theta:\,\theta(q)=o}
                  \lambda_\theta a^\theta_{pq},                 \tag{1.4}
\]

and every positive term in (1.4) is a legal atom.  Thus each component is a
fractional perfect matching in the functional predecessor graph

\[
 B_\theta=(P,Q;\{pq:(p,q,\theta(q))\in\mathcal E\}).          \tag{1.5}
\]

Since `B_theta` is bipartite, every component can then be rounded inside
its own positive support to a perfect functional turn matching.

## 2. Exact disintegration linear system

The following is an exact reformulation, useful even when no product
structure is present.

### Theorem 2.1 (weighted functional-flow criterion)

The tensor `x` has a functional disintegration if and only if there are
numbers

\[
                  z^\theta_{pq}\ge0,\qquad \lambda_\theta\ge0,
\]

indexed by incidence bijections `theta`, satisfying

\[
 \begin{aligned}
  \sum_q z^\theta_{pq}&=\lambda_\theta &&(p\in P),\\
  \sum_p z^\theta_{pq}&=\lambda_\theta &&(q\in Q),\\
  \sum_{\theta:\,\theta(q)=o}z^\theta_{pq}&=x_{pqo}
                  &&(p,q,o),                                   \tag{2.1}
 \end{aligned}
\]

with `z^theta_{pq}=0` whenever `(p,q,theta(q))` is illegal.

#### Proof

Given a functional disintegration, put
`z^theta=lambda_theta A^theta`.  The equations are immediate.

Conversely, discard the zero-weight indices and put

\[
                         A^\theta={z^\theta\over\lambda_\theta}.
\]

The first two rows of (2.1) say that `A^theta` is doubly stochastic; the
third gives (1.4).  Summing the third equation over `p` also gives

\[
       y_{qo}=\sum_{\theta:\,\theta(q)=o}\lambda_\theta,
\]

so the weights form a Birkhoff decomposition of `y`.  Finally, summing over
`o` and then `q` gives `sum_theta lambda_theta=1`.  `square`

The system (2.1) is a coupled multicommodity transportation system.  Each
fixed `theta` block is totally unimodular, but the reconstruction equations
couple the blocks.  Thus ordinary Birkhoff decomposition of `y` alone is
not a proof of disintegration.

### Corollary 2.2 (convex-hull interpretation)

The tensor `x` has a functional disintegration if and only if it is a
convex combination of integral perfect turn matchings contained in
`E`.

#### Proof

If `x` has a functional disintegration, decompose each doubly stochastic
`A^theta` into tail--head permutation matrices.  Adding the fixed owner
attachment `theta` turns each such permutation into an integral perfect
turn matching.

Conversely, an integral perfect turn matching induces a tail--head
permutation and a head--owner permutation `theta`; it is therefore a
functional component.  Convex combinations preserve the conclusion.
`square`

Thus functional disintegration is exactly the integral-normality question
for the particular fractional point `x`.  The usefulness of the next
criterion is that it proves this normality by ordinary Birkhoff twice.

## 3. Headwise rank-one disintegration

There is, however, a large exact positive class.

### Theorem 3.1 (conditional-independence disintegration)

Suppose there are doubly stochastic matrices

\[
                   A=(a_{pq})_{P\times Q},\qquad
                   Y=(y_{qo})_{Q\times O}
\]

such that

\[
                         x_{pqo}=a_{pq}y_{qo}                    \tag{3.1}
\]

for every triple.  Assume, as usual, that positive products in (3.1) are
legal atoms.  Then `x` has a functional disintegration.  In fact **every**
Birkhoff decomposition

\[
                         Y=\sum_\theta\lambda_\theta\chi^\theta
\]

lifts, and the tail--head matrix in every component may be chosen to be the
same matrix `A`.

#### Proof

For every `theta`, set

\[
                         z^\theta_{pq}:=\lambda_\theta a_{pq}.
\]

The row and column sums of `z^theta` are `lambda_theta`.  Moreover,

\[
 \sum_{\theta:\,\theta(q)=o}z^\theta_{pq}
 =a_{pq}\sum_{\theta:\,\theta(q)=o}\lambda_\theta
 =a_{pq}y_{qo}
 =x_{pqo}.
\]

Theorem 2.1 applies.  `square`

Equation (3.1) says exactly that, under the normalized turn tensor,

\[
                         P\ \perp\ O\mid Q.                     \tag{3.2}
\]

Equivalently, for each fixed head `q`, the `P x O` slice of `x` has rank
one and its normalized predecessor distribution is independent of the
chosen owner.  This is the precise version of a payload-transparent
rectangle sufficient for functional attachment.

### Theorem 3.2 (finite rail-state mixture)

More generally, suppose

\[
 x_{pqo}=\sum_{s\in S}\gamma_s a^s_{pq}y^s_{qo},
 \qquad \gamma_s\ge0,\qquad\sum_s\gamma_s=1,                    \tag{3.3}
\]

where every `A^s=(a^s_{pq})` and `Y^s=(y^s_{qo})` is doubly stochastic and
every positive product is legal.  Then `x` has a functional
disintegration.

#### Proof

For each state `s`, choose a Birkhoff decomposition

\[
                  Y^s=\sum_\theta\lambda_{s,\theta}\chi^\theta.
\]

Use functional component `(s,theta)` with weight
`gamma_s lambda_{s,theta}` and tail--head matrix `A^s`.  Summing these
components gives (3.3).  `square`

This is the natural positive theorem for a finite rail-state construction:
one may condition on the rail state, but within each state the predecessor
law must be independent of the owner choice given the head.  No common
tail--head matrix across different states is required.

### 3.3 The Boolean uniqueness collapse

For physical Boolean turns, the positive criterion above is much more
rigid than it first appears.  The owner is uniquely determined by the two
roots:

\[
                              o=p\cup q.                       \tag{3.4}
\]

### Theorem 3.3 (a product state is already functional)

Assume every legal atom has the uniqueness property (3.4).  If a product
tensor

\[
                             x_{pqo}=a_{pq}y_{qo}               \tag{3.5}
\]

is supported on legal atoms and `A,Y` are doubly stochastic, then every row
of `Y` has exactly one positive entry.  Hence `Y` is already the permutation
matrix of one functional attachment.

Consequently, in the state-mixture theorem, every nonzero state `s` must
already carry its own functional attachment whenever all its positive
products are physical Boolean turns.

#### Proof

Fix `q`.  Since the `q`-column of `A` sums to one, choose `p` with
`a_{pq}>0`.  If two distinct owners `o_1,o_2` had
`y_{q,o_i}>0`, then (3.5) would make both `(p,q,o_1)` and `(p,q,o_2)`
positive.  By (3.4) both owners would equal `p union q`, a contradiction.
Thus each row of `Y` has at most one positive entry.  Its row sum is one,
so that entry equals one.  Column sums now make these entries a
permutation.  Apply the same argument separately to every state in (3.3).
`square`

This theorem prevents an overclaim: conditional independence is a valid
positive criterion, but for the physical Boolean support it does not
manufacture a functional attachment from a genuinely mixed owner row.  It
works only after the rail state has already selected the owner.

### 3.4 Exact residual dependence under stabilizer averaging

The obstruction can be quantified without choosing a norm.  For fixed
head `q`, the predecessor supports

\[
 \mathcal P(q,o)=\{p:(p,q,o)\in\mathcal E\}                 \tag{3.6}
\]

are pairwise disjoint as `o` varies, again by (3.4).  Therefore the
`P x O` slice at `q` has nonnegative rank equal to the number of its
nonzero owner columns.  Indeed, one nonnegative rank-one summand cannot
meet two disjoint nonzero columns without creating a forbidden cross
entry, while one summand per column always suffices.

For odd Boolean dimension `k=2m+1`, a rank-`m` head has `m+1` incident
rank-`m+1` owners.  Under coordinate-stabilizer averaging, and after
conditioning on any **unlabelled** age/block/rail state `s` which does not
distinguish a complement coordinate,

\[
                 \Pr(O=o\mid Q=q,S=s)={1\over m+1}             \tag{3.7}

for every `o superset q`.  Hence the conditional slice has nonnegative
rank exactly `m+1`, not one.

There is an equivalent information identity.  Because `O=P union Q` on
every positive physical atom,

\[
 I(P;O\mid Q,S)=H(O\mid Q,S).                                \tag{3.8}
\]

Under (3.7) this equals `log(m+1)`, the maximum possible value.  Conditional
predecessor distributions belonging to two different owners even have
disjoint support and total-variation distance one.

The corrected pull-clock construction averages over owners, private sets,
private orders, omitted core subsets, and coordinate permutations.  Its
unlabelled block type `(delta,j)` and phase/age-composition data do not name
the outside extension coordinate.  Therefore any natural equivariant
physical turn lift, conditioned only on those states, has (3.7) and fails
the rank-one criterion maximally.  To make (3.1) true one must refine the
state by the outside coordinate, equivalently by the owner itself; that
refinement has at least `m+1` local states and has already performed the
functional attachment.

There is also a scope point.  The stationary pull-clock theorem by itself
constructs a marked trace circulation inside repeated owners; it does not
canonically select a one-copy physical root/owner turn tensor.  The
calculation above applies to its natural fully symmetric physical lift, or
to any other lift retaining complement-stabilizer symmetry.  A correlated
non-equivariant lift could have a different `y`, but constructing precisely
such a lift is the open owner-attachment problem rather than a consequence
of the pull-clock marginals.

## 4. Why proportional splitting usually fails

For an arbitrary tensor and a chosen Birkhoff decomposition of `y`, the
only canonical local split is

\[
 z^\theta_{pq}:=
 \begin{cases}
 \displaystyle \lambda_\theta{x_{p,q,\theta(q)}}
                              {y_{q,\theta(q)}} ,
      &y_{q,\theta(q)}>0,\\[1ex]
 0,&y_{q,\theta(q)}=0.
 \end{cases}                                                   \tag{4.1}
\]

It reconstructs `x` and has the correct head sums, but its tail load is

\[
 \sum_q z^\theta_{pq}
 =\lambda_\theta\sum_q
      {x_{p,q,\theta(q)}}{y_{q,\theta(q)}}.                     \tag{4.2}
\]

There is no reason for the last sum to equal one.  Under (3.1) it becomes
`sum_q a_{pq}=1`, which explains exactly why the rank-one theorem works.
The missing equations (4.2) are the tail-side correlation gate.

## 5. A support obstruction to every functional disintegration

Functional disintegration has a strong necessary consequence.

### Lemma 5.1 (support-perfect-matching necessity)

If `x` has a functional disintegration, then its positive support contains
an integral perfect turn matching.

#### Proof

Choose a component `theta` of positive weight.  Its matrix `A^theta` is a
fractional perfect matching in the bipartite graph `B_theta`, and every
positive edge of `A^theta` lies in the positive support of `x` by (1.4) and
nonnegativity.  Bipartite matching integrality gives a perfect matching in
that support.  Attaching owner `theta(q)` to the edge ending at `q` gives a
turn matching using every tail, head, and owner exactly once.  `square`

### Theorem 5.2 (portal-free odd-cycle obstruction)

Let `R` be an odd set of resource rows.  Suppose every atom in the positive
support of `x` meets `R` in an even number of rows.  Then `x` has no
functional disintegration.

In particular, suppose the rows `R` form a clean strong odd cycle and the
only positive atoms meeting `R` are its cycle atoms.  Then disintegration
is impossible.

#### Proof

If a perfect turn matching `M` existed in the positive support, then

\[
                         \sum_{e\in M}|e\cap R|=|R|.             \tag{5.1}
\]

The left side is even and the right side is odd, a contradiction.  Apply
Lemma 5.1.  `square`

An atom meeting `R` oddly is precisely an **odd portal** for this parity
cut.  Thus the obstruction concerns the positive support of `x`, not the
complete legal catalogue: a legal portal assigned zero fractional mass is
unavailable to every disintegration of that particular tensor.

## 6. Minimal physical obstruction

The physical Boolean turn hypergraph has no clean strong `C3`.  A clean
physical `C5` is known and is therefore the first possible odd-cycle
support obstruction.  This gives the following sharp audit target for any
stationary fractional pull-clock tensor:

> For every positive clean `C5`, does the positive support also contain an
> odd portal, or can one find a `C5` whose selected rows are saturated using
> only even-incidence atoms?

A portal-free positive `C5` answers the disintegration question negatively
for that tensor by Theorem 5.2.  Conversely, the mere presence of a `C5` in
the legal catalogue is not a negative result.  The authenticated `k=17`
connected-inventory `C5` has a one-row portal and is locally absorbable, so
it witnesses non-TU but not failure of functional disintegration.

## 7. Consequences for integral rotor fusion

The fractional trace-circulation theorem closes rank marginals and literal
stationarity.  The results here separate its next owner gate into two
proof targets.

1. **Positive route.**  Refine the stationary circulation into finitely
   many rail states satisfying the factorization (3.3).  Then functional
   owner attachment and fractional tail--head perfection follow
   automatically; bipartite TU performs the one-owner-once rounding inside
   each component.

2. **Negative audit.**  Search the positive support, not the whole legal
   turn catalogue, for a portal-free clean `C5`.  Such a cycle is the
   smallest possible physical certificate that no functional
   disintegration of the given tensor exists.

The exact unresolved statement is therefore no longer whether the
head--owner projection is Birkhoff-decomposable; it always is.  It is
whether the predecessor conditional laws can be coupled to that
decomposition so that all tail equations (4.2) hold.  Conditional
independence closes those equations, while a portal-free odd cycle can
forbid them outright.
