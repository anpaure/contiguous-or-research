# Prime-equivariant cyclic packets: an exact fractional absorber and the orbit obstruction

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or web input
is used.

## 0. Result and exact boundary

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname{Cat}_m,
\qquad K=\lceil A\sqrt m\rceil,
\]

and

\[
N_q=\binom n{m-q},\qquad
\lambda_q=W/N_q,\qquad c_q=\lfloor\lambda_q\rfloor .
\]

This note does **not** prove \((\mathrm{CA}_A)\).  It proves the following
new exact coupling theorem.

* If a prime-cyclic invariant, extendible partial wreath factor has a
  sufficiently large canonical core, and the explicit uniform deletion
  flow on the uncovered middle owners lies in the residual
  floor/ceiling boxes, then quotient integrality produces one common
  integral balanced resolution which leaves every core owner canonical.
  There are no remaining Hall, integrality, or path-concatenation
  conditions under this displayed pointwise hypothesis.

The note also proves a packet-level obstruction which is invisible in the
prime flag-flow network.

* If \(n=2m+1\) is prime and \(m\ge3\) is odd, no exact wreath factor is
  invariant under a fixed coordinate \(n\)-cycle.  More sharply, an
  invariant whole-wreath core of an exact factor must leave at least
  \(m-1\) wreaths, hence at least \(n(m-1)\) middle owners, outside the
  core.  This lower bound is polynomial and therefore does not contradict
  the \(o(W/\sqrt m)\) exceptional-owner allowance in \((\mathrm{CA}_A)\).

Consequently the prime-equivariant flag flow cannot simply be intersected
with the exact packet equations and rounded by total unimodularity.  A
positive proof must either construct a near-complete invariant packet core
and route its exceptional owners, or break prime equivariance while
controlling the resulting labelled cost.

## 1. Oriented invariant partial factors

Let \(n=p\) be prime and identify the coordinates with \(\mathbb Z_p\).
Write

\[
\sigma(x)=x+1.
\]

A wreath row is an unoriented cyclic order modulo rotation and reversal.
An orientation chooses one of the two cyclic directions.  An **oriented
partial exact wreath factor** \(G\) is a set of oriented rows whose
length-\(m\) interval families are pairwise disjoint.  It is
**extendible** if its underlying rows are contained in an exact wreath
factor \(F\).  It is **\(\sigma\)-invariant** if \(\sigma G=G\), with the
orientations transported by \(\sigma\).

For a middle owner \(X\) belonging to a row of \(G\), let

\[
\Gamma_q(X)\in\binom{[n]}{m-q}
\]

be its canonical oriented interval at depth \(q\), and put

\[
g_q(S)=\#\{X\text{ owned by }G:\Gamma_q(X)=S\}.
\tag{1.1}
\]

If \(G\) has \(B-b\) rows, its core contains \(n(B-b)\) middle owners.
Let

\[
E=\binom{[n]}m\setminus\{\text{middle owners of }G\}.
\tag{1.2}
\]

Then

\[
|E|=nb.
\tag{1.3}
\]

Since the core owner set is \(\sigma\)-invariant, so is \(E\).  If
\(G\subseteq F\), then \(E\) is exactly the union of the middle-owner
sets of the \(b\) exceptional wreaths in \(F\setminus G\), even though
those exceptional rows need not themselves form \(\sigma\)-orbits.

For later floor bookkeeping, every rank in the controlled window consists
of free \(\sigma\)-orbits.  Hence \(p\mid N_q\), and since \(p\mid W\),

\[
\rho_q=W-c_qN_q
\tag{1.4}
\]

is divisible by \(p\).  Thus a \(\sigma\)-invariant balanced load has an
integral number \(\rho_q/p\) of high node-orbits; there is no concealed
floor congruence in the flag quotient.

## 2. The uniform residual flag flow

For \(X\in E\), put unit mass uniformly on the \(m!\) orders in which the
elements of \(X\) can be deleted.  This is a fractional nested path flow.
At depth \(q\), its load at \(S\in\binom{[n]}{m-q}\) is

\[
u_q^E(S)
=\frac{\#\{X\in E:S\subseteq X\}}{\binom mq}.
\tag{2.1}
\]

Indeed, among the \(\binom mq\) possible sets of the first \(q\) deleted
elements of \(X\), exactly one leaves a prescribed descendant \(S\).
The entire fractional path flow, not only the node-load vector (2.1), is
\(\sigma\)-invariant.

### Theorem 2.1 — exact prime-equivariant packet-core completion

Fix \(A>0\).  Suppose \(p=2m+1\) is prime, \(K\le m-1\), and there are
an exact oriented wreath factor \(F\) and a \(\sigma\)-invariant oriented
subfactor \(G\subseteq F\) with \(B-b\) rows.  Assume that for every
\(1\le q\le K\) and every \(S\in\binom{[n]}{m-q}\),

\[
\boxed{
c_q\ \le\ g_q(S)+u_q^E(S)\ \le\ c_q+1 .
}
\tag{2.2}
\]

Then there is a \(\sigma\)-equivariant integral balanced nested
resolution \(P\) such that

\[
P_q(X)=\Gamma_q(X)
\qquad
(X\text{ owned by }G,\ 0\le q\le K).
\tag{2.3}
\]

Consequently

\[
e_q(F,P)\le nb\qquad(1\le q\le K),
\tag{2.4}
\]

and

\[
\sum_{q=1}^K\frac{e_q(F,P)}{c_q}
\le nb\sum_{q=1}^K\frac1{c_q}.
\tag{2.5}
\]

In particular, for fixed \(A\), the existence of such \((F,G)\) with

\[
b=o_A(B/\sqrt m)
\tag{2.6}
\]

implies \((\mathrm{CA}_A)\) along these prime dimensions.

#### Proof

Freeze all canonical paths belonging to \(G\).  At a depth-\(q\) node
\(S\), the residual throughput interval is

\[
\ell_q(S)=\max\{0,c_q-g_q(S)\},
\qquad
h_q(S)=c_q+1-g_q(S).
\tag{2.7}
\]

Condition (2.2) implies

\[
0\le \ell_q(S)\le u_q^E(S)\le h_q(S).
\tag{2.8}
\]

In particular, all upper capacities in (2.7) are nonnegative.  The
uniform deletion flow on \(E\) is therefore a feasible real flow in the
residual node-split Boolean inclusion network, with the integral lower and
upper node capacities (2.7).  Every residual middle root \(X\in E\) has
supply one.

All data in this residual network are \(\sigma\)-invariant.  Since \(p\)
is prime, every nonempty proper subset of \(\mathbb Z_p\) has a free
\(\langle\sigma\rangle\)-orbit.  The same is true of every internal
deletion arc.  Moreover, an arc orbit contains at most one arc leaving a
fixed representative: if two such arcs were translates, a nonidentity
power of \(\sigma\) would fix their common tail.

Quotient the residual node-split network by \(\langle\sigma\rangle\).
Each orbit of residual middle roots supplies one unit.  There are

\[
|E|/p=b
\]

such source orbits.  The quotient node has precisely the same integral
throughput bounds \(\ell_q(S),h_q(S)\) as any physical representative of
its orbit.  Parallel inclusion arcs are harmless.  The invariant uniform
deletion flow descends to a feasible real quotient flow.

The quotient is an ordinary directed network with integral lower and upper
capacities.  Network integrality gives an integral quotient flow.
Decompose it into \(b\) unit paths.  A quotient path has a unique lift once
its initial representative is fixed, because an arc orbit has at most one
arc leaving that representative.  Taking all \(p\) translates of every
lift gives exactly one integral residual path from every root in \(E\).

Now adjoin, without reconnecting them, the frozen canonical paths of
\(G\).  At a depth-\(q\) node \(S\), the resulting load is

\[
g_q(S)+r_q(S)\in\{c_q,c_q+1\}.
\]

If \(\lambda_q\) is an integer, total mass is
\(W=c_qN_q\), so every load is automatically \(c_q\); no spurious high
node is possible.  Thus the full resolution is balanced with the exact
floor/ceiling baseline at every depth.  It is nested by path construction,
and the frozen paths give (2.3).

The lifted residual flow and the frozen core are both equivariant, so the
full resolution is equivariant.  Equations (2.4) and (2.5) follow because
only the \(nb\) exceptional owners can disagree with their canonical
\(F\)-paths.  Finally,

\[
\sum_{q\le K}1/c_q\le K=O_A(\sqrt m),
\]

so (2.6) makes the right side of (2.5) \(o(nB)=o(W)\).  \(\square\)

### Exact deletion-column consequence

Every owner orbit is free.  Equivariance gives

\[
d_t(\sigma^jX)=\sigma^jd_t(X).
\]

Thus, on each of the \(B=W/p\) owner orbits, the deletion label at a
fixed time \(t\) runs once through all coordinates.  The resolution in
Theorem 2.1 consequently satisfies

\[
\#\{X:d_t(X)=x\}=B
\qquad(t\le K,\ x\in[n]).
\tag{2.9}
\]

This is an output of the packet-preserving completion, not an independently
chosen marginal condition.

## 3. Why the uniform absorber respects the verified star structure

Theorem 2.1 uses the pointwise box condition (2.2), which is much stronger
than a collection of star moments.  Nevertheless the cyclic packet
structure gives exact control of every fixed-order star moment of the
uniform absorber.

Let \(T\subseteq[n]\) have size \(t\ge1\), and let

\[
M_q^E(T)=\#\{X\in E:\Gamma_q^F(X)\supseteq T\}
\]

be the canonical contribution of the \(b\) exceptional wreaths.  Set

\[
U_q^E(T)=
\sum_{\substack{S\in\binom{[n]}{m-q}\\T\subseteq S}}u_q^E(S).
\]

### Lemma 3.1 — exact uniform-residual star law

For every \(1\le t\le m-q\),

\[
\boxed{
U_q^E(T)
=\frac{\binom{m-t}{q}}{\binom mq}\,M_0^E(T).
}
\tag{3.1}
\]

If \(q\le m/2\), then

\[
\boxed{
|U_q^E(T)-M_q^E(T)|
\le (2t+1)qb.
}
\tag{3.2}

For \(t=1\), equality is exact:

\[
U_q^E(\{x\})=M_q^E(\{x\})=b(m-q)
\qquad(x\in[n]).
\tag{3.3}

#### Proof

For a fixed exceptional root \(X\supseteq T\), exactly

\[
\binom{m-t}{q}
\]

of its \(\binom mq\) depth-\(q\) descendants contain \(T\).  Summing over
the roots in \(E\) proves (3.1).

For one exceptional wreath row \(R\), let \(a_R(T)\) be the number of its
middle intervals containing \(T\).  Cyclic span truncation gives

\[
M_0^E(T)=\sum_R a_R(T),
\qquad
M_q^E(T)=\sum_R(a_R(T)-q)_+.
\tag{3.4}
\]

Hence

\[
0\le M_0^E(T)-M_q^E(T)\le qb.
\tag{3.5}
\]

Put

\[
\kappa=\frac{\binom{m-t}{q}}{\binom mq}
=\prod_{i=0}^{q-1}\left(1-\frac{t}{m-i}\right).
\]

The elementary product bound gives

\[
0\le1-\kappa
\le\sum_{i=0}^{q-1}\frac{t}{m-i}
\le\frac{tq}{m-q+1}.
\tag{3.6}
\]

Also \(a_R(T)\le m-t+1\), so \(M_0^E(T)\le bm\).  Combining
(3.1), (3.5), and (3.6), and using \(q\le m/2\), gives

\[
|U_q^E(T)-M_q^E(T)|
\le qb+\frac{tq}{m-q+1}bm
\le(2t+1)qb.
\]

For \(t=1\), every length-\(m\) row contains a fixed coordinate in exactly
\(m\) middle intervals and in exactly \(m-q\) intervals of length
\(m-q\).  Since

\[
\binom{m-1}{q}/\binom mq=(m-q)/m,
\]

(3.3) follows.  \(\square\)

If \(b=o_A(B/\sqrt m)\), then for every fixed \(t\), uniformly for
\(q\le A\sqrt m\), the error in (3.2) is \(o(B)\), while the point
moment is unchanged exactly.  This explains why the verified point-star
and fixed-star collar is compatible with the uniform absorber.  It does
**not** imply the pointwise box condition (2.2), and it does not control an
arbitrary residual Hall cut.

### The depth-one box law

For \(m\ge3\), at \(q=1\),

\[
\lambda_1=\frac{m+2}{m},\qquad c_1=1,
\qquad
u_1^E(S)=d_E(S)/m,
\]

where

\[
d_E(S)=\#\{X\in E:S\subset X\}.
\]

Thus (2.2) has the following exact, non-asymptotic form:

\[
\begin{array}{c|c}
g_1(S)&\text{allowed }d_E(S)\\ \hline
0& m\le d_E(S)\le m+2,\\
1& 0\le d_E(S)\le m,\\
2& d_E(S)=0.
\end{array}
\tag{3.7}
\]

No value \(g_1(S)\ge3\) is allowed.  In particular, a core-saturated
target cannot be a facet of any exceptional root, while a core hole must
have at least \(m\) of its \(m+2\) parents exceptional.  This demonstrates
both the strength and the literal cyclic/root compatibility content of
the uniform certificate.  Survival alone does not imply (3.7).

## 4. Exact orbit arithmetic for wreath packets

We now classify the rows fixed by \(\sigma\).

### Lemma 4.1 — fixed rows are affine cyclic orders

An unoriented wreath row is fixed by \(\sigma:x\mapsto x+1\) if and only
if it has a cyclic representative

\[
(a,a+d,a+2d,\ldots,a+(p-1)d)
\tag{4.1}
\]

for some \(d\in\mathbb Z_p^\times\).  Rotation removes \(a\), and reversal
identifies \(d\) with \(-d\).  Hence there are exactly

\[
(p-1)/2=m
\tag{4.2}
\]

fixed unoriented rows.

#### Proof

If a row is fixed, the action of \(\sigma\) on its cyclic positions is a
dihedral automorphism.  It cannot be a reflection: a reflection has order
two, whereas the induced permutation has order dividing the odd prime
\(p\), and it is nontrivial because \(\sigma\) fixes no coordinate.
Therefore the induced action is a nonzero rotation by some
\(s\in\mathbb Z_p^\times\).

For a cyclic representative \((z_i)_{i\in\mathbb Z_p}\),

\[
z_{i+s}=z_i+1.
\]

Writing \(d=s^{-1}\), iteration gives \(z_i=a+di\).  Conversely every
order (4.1) is carried to itself by a rotation of its positions.  The
rotation and reversal identifications give (4.2).  \(\square\)

### Lemma 4.2 — Catalan residue

For \(p=2m+1\) prime,

\[
\boxed{B=\operatorname{Cat}_m\equiv2(-1)^m\pmod p.}
\tag{4.3}
\]

#### Proof

Since

\[
B=\frac1{m+1}\binom{p-1}{m},
\]

the standard product expansion gives
\(\binom{p-1}{m}\equiv(-1)^m\pmod p\).  Also

\[
2(m+1)=p+1\equiv1\pmod p,
\]

so \((m+1)^{-1}\equiv2\pmod p\).  This proves (4.3).  \(\square\)

### Theorem 4.3 — exact invariant-packet obstruction

Let \(G\) be a \(\sigma\)-invariant partial exact wreath factor with
\(B-b\) underlying rows.  Let \(f\) be the number of selected
\(\sigma\)-fixed underlying rows.  Then

\[
0\le f\le m,
\qquad
B-b=f+pt
\tag{4.4}
\]

for some integer \(t\ge0\).

Consequently:

1. if \(m\) is odd, then
   \[
   \boxed{b\ge m-1;}
   \tag{4.5}
   \]
2. if \(m\) is odd and \(m\ge3\), no \(\sigma\)-invariant exact wreath
   factor exists;
3. if \(m\) is even and a \(\sigma\)-invariant exact wreath factor exists,
   it contains exactly two fixed underlying rows.

These are necessary arithmetic conditions; they do not assert existence of
an invariant partial or full packing attaining the permitted row counts.

#### Proof

Every nonfixed row orbit under the prime cyclic group has size \(p\).
There are only the \(m\) fixed underlying rows classified in Lemma 4.1.
This proves (4.4).  Orientations cause no extra underlying row: both
directions of a fixed row are stable under \(\sigma\), but a partial exact
factor can select at most one because the two directions have the same
middle support.

If \(m\) is odd, (4.3) gives \(B\equiv p-2\pmod p\).  Therefore

\[
b\equiv p-2-f\pmod p.
\]

For \(0\le f\le m=(p-1)/2\), the least possible nonnegative residue on
the right is attained at \(f=m\) and equals

\[
p-2-m=m-1.
\]

Thus every nonnegative \(b\) satisfies (4.5), and \(b=0\) is impossible
for \(m\ge3\).

If \(m\) is even and \(b=0\), (4.3) gives \(f\equiv2\pmod p\).  Since
\(0\le f\le m<p\), necessarily \(f=2\).  \(\square\)

### Row count versus owner count

The lower bound (4.5) is on exceptional **wreath rows**.  Since every row
has \(p=n\) distinct middle owners, the corresponding exceptional-owner
bound is

\[
|E|=nb\ge n(m-1).
\tag{4.6}
\]

It is not \(m-1\) owners, and it is not \(n-(m-1)\) rows.  Conversely,
an arithmetically minimal invariant core would leave exactly \(m-1\)
rows and \(n(m-1)\) owners.  Since \(B\) is exponential in \(m\),

\[
m-1=o(B/\sqrt m),
\qquad
n(m-1)=o(W/\sqrt m).
\tag{4.7}
\]

Thus the obstruction forbids exact equivariance but leaves ample room for
the residual theorem required by \((\mathrm{CA}_A)\).

## 5. Why network integrality cannot select the packets

The uniform fractional wreath vector assigns weight \(1/D_0\) to every
row and covers every middle set with total weight one.  It is
\(\sigma\)-invariant and therefore descends to the row-orbit quotient.

When \(m\) is odd and at least three, Theorem 4.3 says that the same
quotient exact-cover system has no integral solution: an integral solution
would select whole row orbits and give a \(\sigma\)-invariant exact factor.
Hence the row-orbit exact-cover polytope has a feasible invariant fractional
point but no integral point.

This is an exact packet-level obstruction.  The prime-equivariant balanced
flag network is integral because it is a directed network after quotienting.
Adjoining the requirement that the middle sources be grouped into literal
cyclic wreath packets destroys that conclusion already at depth zero.
Therefore a proof cannot choose the packet factor and the flag flow by one
unqualified quotient-TU argument.

## 6. Adversarial audit

1. **No proof of \((\mathrm{CA}_A)\).**  Theorem 2.1 is conditional on the
   pointwise fractional box condition (2.2).  Neither the verified
   star-collar theorem nor prime equivariance proves (2.2).

2. **The certificate is sufficient, not necessary.**  A residual flow can
   avoid a saturated node even when the uniform flow assigns positive mass
   to it.  Therefore failure of (2.2), including failure of the depth-one
   law (3.7), is not a counterexample to residual Hall or to
   \((\mathrm{CA}_A)\).

3. **Literal packets are preserved where claimed.**  The paths of all core
   owners are frozen before quotienting.  They are adjoined after the
   residual path decomposition, so suffix exchange cannot change a core
   owner's canonical path.  Exceptional owners may use arbitrary nested
   deletion paths, as allowed in labelled alignment.

4. **The exact factor remains one object.**  The theorem assumes one exact
   factor \(F\) containing the same core \(G\) at every depth.  The factor,
   core, exceptional family, and residual flow are not chosen separately
   across ranks.

5. **Prime use is exact.**  Ordinary network integrality alone would yield
   some integral residual flow under (2.2).  Prime quotienting is what
   preserves equivariance and gives (2.9).  Prime packet selection is not
   integral, as Theorem 4.3 demonstrates.

6. **The congruence no-go has the right scale.**  It rules out a fully
   invariant exact factor for odd \(m\), but its sharp arithmetic residual
   is only \(m-1\) rows.  It therefore closes the zero-exception
   equivariant coupling, not the asymptotic residual coupling.

7. **Smallest unproved statement in this sublane.**  For every fixed
   \(A\), construct an exact factor containing a \(\sigma\)-invariant
   oriented core of \(B-o_A(B/\sqrt m)\) rows for which either (2.2) holds,
   or, more generally, the residual quotient network with node intervals
   (2.7) has a feasible real flow.  Theorem 2.1 proves that the first
   alternative has no further obstruction; quotient integrality proves the
   same for the second once real feasibility is supplied.  Neither
   construction is presently proved.
