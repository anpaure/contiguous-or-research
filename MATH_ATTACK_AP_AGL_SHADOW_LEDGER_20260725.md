# Arithmetic-progression wreaths under \(AGL(1,p)\)

## Exact rainbow shadows, zero density, and the equivariance boundary

Date: 2026-07-25

This note is purely algebraic.  No computation or web input is used.

Put

\[
 p=2m+1\quad\hbox{prime},\qquad
 W=\binom pm,\qquad B=W/p=\operatorname{Cat}_m,
\]

and identify the labels with \(\mathbb F_p\).  Wreath rows are unoriented
cyclic orders, modulo rotation and reversal.  For \(a\ne0\), let

\[
 C_a=(0,a,2a,\ldots,(p-1)a),
\]

so \(C_a=C_{-a}\) as an unoriented row.  Write

\[
 P_r=\{0,1,\ldots,r-1\}\subset\mathbb F_p.
\]

The length-\(r\) interval targets of \(C_a\) are exactly

\[
 S_{a,b}^{(r)}=b+aP_r\qquad(b\in\mathbb F_p).
\tag{0.1}
\]

The word *rainbow* has two different meanings in this setting.  The AP
rows are perfectly rainbow in the ordinary target space when all multiplier
rows are taken once.  They are maximally collapsed after quotienting targets
by translations: the \(p\) intervals of one AP row form one translation
orbit.  Both statements are exact and compatible.

## 1. The affine stabilizer of a central interval

### Lemma 1.1

If \(2\le r\le m\), then

\[
 \operatorname{Stab}_{AGL(1,p)}(P_r)
 =\{x\mapsto x,\ x\mapsto r-1-x\}.
\tag{1.1}
\]

Consequently

\[
 |AGL(1,p)P_r|=\frac{p(p-1)}2=pm.
\tag{1.2}
\]

#### Proof

For \(d\ne0\), put

\[
 \nu(d)=|P_r\cap(P_r+d)|.
\]

Since \(2r\le p-1\), the maximum of \(\nu(d)\) over nonzero \(d\) is
\(r-1\), and it is attained exactly at \(d=1\) and \(d=-1\).  If
\(x\mapsto ux+v\) stabilizes \(P_r\), it preserves this difference
multiplicity and hence \(u\{1,-1\}=\{1,-1\}\).  Thus \(u=1\) or \(u=-1\).
A nonempty proper subset of \(\mathbb F_p\) has no nonzero translation
stabilizer.  Therefore \(v=0\) when \(u=1\), while direct comparison gives
\(v=r-1\) when \(u=-1\).  This proves (1.1), and orbit--stabilizer gives
(1.2).  \(\square\)

Complementation gives the same statement when
\(2\le p-r\le m\).  The endpoint ranks \(r=1,p-1\) are exceptional:
there are only \(p\) singleton targets or singleton complements.

## 2. Exact AP shadow multiplicities

### Theorem 2.1 -- full multiplier rainbow

Fix \(2\le r\le m\).  Across the \(m=(p-1)/2\) distinct AP rows
\(C_a\), \(a\in\mathbb F_p^\times/\{\pm1\}\), all \(pm\) length-\(r\)
interval targets are distinct.  Their support is the single affine orbit

\[
 \mathcal A_r=AGL(1,p)P_r,
\tag{2.1}
\]

and the load is exactly

\[
 \mu_r^{\rm AP}(S)=\mathbf1_{\{S\in\mathcal A_r\}}.
\tag{2.2}
\]

#### Proof

Every target (0.1) is an affine image of \(P_r\), so the support lies in
\(\mathcal A_r\).  Conversely every affine image has the form (0.1).
If

\[
 b+aP_r=d+cP_r,
\]

then an affine map carrying \(P_r\) to itself has multiplier \(c/a\).
Lemma 1.1 gives \(c/a=\pm1\).  The two cases either give the same pointed
interval or replace \(a\) by \(-a\) and reverse the same underlying row.
Thus there is no collision between distinct unoriented pointed AP rows.
There are \(pm\) such incidences, which equals \(|\mathcal A_r|\) by
(1.2).  \(\square\)

This also supplies the complete convention ledger.

* Deduplicated unoriented AP rows give multiplicity one on \(\mathcal A_r\).
* Taking the \(p-1\) oriented slopes gives multiplicity two.
* Taking all \(g\in AGL(1,p)\) as a raw multiset of images of one AP row
  gives multiplicity \(2p\): the underlying row stabilizer has order
  \(2p\).
* At \(r=1\) or \(p-1\), each of the \(p\) targets occurs in all \(m\)
  underlying AP rows.

For a fixed Gaussian window and large \(m\), one has
\(r=m-q\ge2\), so (2.2) applies at every controlled depth.

### Proposition 2.2 -- high-stabilizer targets are exponentially negligible

For every \(1\le k\le p-1\), the number of \(k\)-sets \(S\subseteq
\mathbb F_p\) with

\[
 |\operatorname{Stab}_{AGL(1,p)}(S)|>2
\]

is at most

\[
 \boxed{2p^2\,2^{(p-1)/3}.}
\tag{2.3}
\]

#### Proof

Put \(K=\operatorname{Stab}_{AGL(1,p)}(S)\).  Its intersection with the
translation subgroup is trivial: a nonzero translation generates all of
\(\mathbb F_p\), so an invariant subset would be empty or full.  Hence the
multiplier projection \(K\to\mathbb F_p^\times\) is injective.  In
particular, \(d=|K|\) divides \(p-1\).

The affine average

\[
 z=\frac1d\sum_{g\in K}g(0)
\]

is fixed by every element of \(K\).  After translating \(z\) to zero,
\(K\) is therefore the unique scalar subgroup \(H\le\mathbb F_p^\times\)
of order \(d\).  An \(H\)-invariant subset is a union of the singleton
\(\{0\}\) and the \((p-1)/d\) nonzero scalar orbits.  For fixed \((z,d)\)
there are consequently at most

\[
 2^{1+(p-1)/d}\le2\,2^{(p-1)/3}
\]

such subsets when \(d>2\).  There are \(p\) choices of \(z\) and fewer
than \(p\) possible divisors \(d\), proving (2.3).  Restricting to one
cardinality \(k\) can only decrease the count.  \(\square\)

If \(E_q\) is the exceptional family at rank \(m-q\), then for fixed
\(A\),

\[
 \sum_{q\le A\sqrt m}c_q|E_q|
 \le O_A\!\left(p^{5/2}2^{p/3}\right)=o(W).
\tag{2.4}
\]

Indeed \(c_q=O_A(1)\) throughout the window and
\(W=\Theta(2^p/\sqrt p)\).  Thus leaving every target with affine
stabilizer larger than two uncovered costs only \(o(W)\) in total weighted
shallow-shadow mass.  High stabilizers create no coefficient-one-scale
obstruction to a generic large-orbit construction.

Here is the exact orbit reason these targets may have to be discarded.
The affine stabilizer of any pointed occurrence--an unoriented row together
with one distinguished proper cyclic interval--has order at most two.  For
a non-AP row this follows from its row stabilizer having order at most two.
For an AP row, the row stabilizer is dihedral of order \(2p\), but the
stabilizer of one proper arc among its \(p\) starts has order at most two.
If the target \(S\) of a pointed occurrence has stabilizer order \(d>2\),
the equivariant orbit map

\[
 G/\operatorname{Stab}(\hbox{pointed occurrence})
 \longrightarrow G/\operatorname{Stab}(S)
\]

has fibre size greater than one.  Selecting the whole pointed row orbit
therefore repeats every target in \(GS\).  A \(G\)-invariant **rainbow
shadow** family, whose target multiplicities are required to be at most
one, cannot cover that orbit.  At rank \(m\) this applies directly to a
middle packing; at shallower ranks ordinary factors may instead have
collisions, so the targets are not forced holes there.  Equation (2.4)
shows that voluntarily deleting all such shallow targets still costs only
\(o(W)\).  The AP intervals in Theorem 2.1 are the equality case: both
stabilizers have order two, so the orbit map is bijective.

## 3. AP-only families have macroscopic weighted defect

Let

\[
 N_q=\binom p{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad 1\le q\le A\sqrt m.
\]

Any multiset made only from AP rows, with arbitrary repetitions but with
exactly \(B\) rows (hence total rank-\((m-q)\) slot mass \(W\)), has
rank-\((m-q)\) support of size at most \(pm\).  Therefore its balanced
lower deficit satisfies

\[
 D_q=\sum_S(c_q-\mu_q(S))_+
 \ge c_q(N_q-pm).
\tag{3.1}
\]

In particular, for the usual weighted overload
\(J_A=\sum_q O_q/c_q\), where \(O_q\ge D_q\),

\[
 J_A\ge
 \sum_{1\le q\le A\sqrt m}(N_q-pm).
\tag{3.2}
\]

Uniformly in this fixed window,

\[
 \frac{N_q}{W}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+2+j}
 =\Theta_A(1).
\tag{3.3}
\]

Since \(pm=O(m^2)=o(W)\), (3.2) gives

\[
 \boxed{J_A=\Omega_A(W\sqrt m).}
\tag{3.4}
\]

Thus the exact rainbow property of the AP multiplier orbit does not come
close to coefficient one: it is a polynomial-size perfect packing inside
an exponential-size target layer.  Repeating the orbit changes its loads
but not its support.

On the other hand, the AP orbit is harmless as a seed inside a genuinely
large construction.  It has \(m\) rows and \(pm\) middle owners.  If all
of its canonical flags through

\[
 K=\lceil A\sqrt m\rceil
\]

are discarded or recoded, the resulting labelled cost is at most

\[
 pmK=O_A(m^{5/2})=o(W).
\tag{3.5}
\]

Thus keeping the AP orbit frozen gives perfect local shadows, while
throwing it away is asymptotically free.  It cannot by itself decide the
coefficient-one question.

There is also an exact obstruction to the most naive residual coupling.

### Proposition 3.1 -- the uniform absorber already fails at depth two

Assume \(p\ge29\).  Freeze all \(pm\) AP middle owners with their
canonical paths, and put the uniform deletion flow on every other middle
root.  At every AP target \(S\in\mathcal A_{m-2}\), the resulting
depth-two fractional load is

\[
 \boxed{2+\frac6{m-1}>2.}
\tag{3.6}
\]

Since \(c_2=1\) for \(m\ge8\), this violates the balanced upper capacity
\(c_2+1=2\).

#### Proof

First, an AP \((m-2)\)-set is contained in exactly three AP middle
owners.  It is enough to prove that any AP middle owner containing it has
the same slope.  Normalize one such pair to

\[
 P_{m-2}\subseteq P_m,
\]

and suppose \(P_{m-2}\subseteq t+uP_m=:X\).  Then

\[
 |X\mathbin\triangle P_m|\le4.
\]

Translation by one and the triangle inequality give

\[
 |X\mathbin\triangle(X+1)|\le10.
\]

In the cyclic order of slope \(u\), translation by one shifts the start
by \(u^{-1}\), so the least signed residues of both \(u^{-1}\) and,
by the symmetric argument using translation by \(u\), of \(u\), have
absolute value at most five.  Choose representatives \(v,w\) with

\[
 |v|,|w|\le5,\qquad vw\equiv1\pmod p.
\]

For \(p\ge29\), \(|vw-1|<p\), so \(vw=1\) over the integers.  Hence
\(u=\pm1\).  In the standard cyclic order exactly three length-\(m\)
intervals contain \(P_{m-2}\).

The uniform deletion flow on all middle roots has constant depth-two
load

\[
 \lambda_2=\frac{W}{N_2}
 =\frac{(m+2)(m+3)}{m(m-1)}.
\]

For the frozen AP owner set, its uniform descendant contribution at
\(S\) is

\[
 \frac3{\binom m2}.
\]

Replacing that contribution by the one canonical AP occurrence gives

\[
 \lambda_2+1-\frac3{\binom m2}
 =2+\frac6{m-1},
\]

as claimed. \(\square\)

Thus the exact rainbow seed does not satisfy the pointwise
uniform-residual box condition.  A positive near-equivariant construction
would need a tailored common residual flow which deliberately avoids the
AP depth-two orbit; fractional averaging alone is insufficient.

More generally, one full \(AGL(1,p)\)-orbit of an arbitrary row has at
most

\[
 p|AGL(1,p)|=p^2(p-1)
\tag{3.7}
\]

rank-\(r\) interval targets.  Hence any architecture using
\(o(W/p^3)\) affine row-orbit shapes still misses \(\Theta_A(W)\) targets
at every depth in a fixed Gaussian window.  A positive-density affine
orbit construction would have to select exponentially many generic
non-AP orbits; the AP orbit can only be boundary data.

## 4. Exact \(AGL\)-equivariance is impossible

Let \(G=AGL(1,p)\), of order

\[
 |G|=p(p-1)=2pm.
\]

### Lemma 4.1 -- complete row-orbit classification

The AP rows form one \(G\)-orbit of size \(m\), and their row stabilizer
has order \(2p\).  Every non-AP unoriented row has affine stabilizer of
order \(1\) or \(2\).  Consequently every non-AP row orbit has size

\[
 2pm\quad\hbox{or}\quad pm.
\tag{4.1}
\]

Hence every \(G\)-invariant row family has cardinality

\[
 \boxed{R=m(\varepsilon+pt),\qquad
        \varepsilon\in\{0,1\},\quad t\in\mathbb Z_{\ge0}.}
\tag{4.2}
\]

#### Proof

The affine stabilizer of a cyclic order embeds in its dihedral
automorphism group \(D_p\).  If it contains a nonidentity translation,
then, because \(p\) is prime, it contains the whole translation group.
The induced action on cyclic positions is a rotation, and iteration shows
that the row labels are an arithmetic progression.  Conversely an AP row
is stabilized by all translations and by one affine reflection, giving a
dihedral stabilizer of order \(2p\).

For a non-AP row the affine stabilizer meets the rotation subgroup of
\(D_p\) trivially.  A subgroup of \(D_p\) with no nontrivial rotation has
order at most two.  Orbit--stabilizer gives (4.1).  The AP orbit is
transitive and may be selected either completely or not at all; all other
orbit sizes are multiples of \(pm\).  This proves (4.2). \(\square\)

For

\[
 B=\operatorname{Cat}_m=\frac1{m+1}\binom{p-1}{m},
\]

one has

\[
 B\equiv2(-1)^m\pmod p.
\tag{4.3}
\]

### Theorem 4.2 -- exact row-count obstruction

For every prime \(p=2m+1\ge7\), no exact middle wreath factor is
\(G\)-invariant.

More precisely, if a \(G\)-invariant partial factor with \(B-b\) rows is
contained in some exact factor, then for one
\(\varepsilon\in\{0,1\}\),

\[
 \boxed{b\equiv B-\varepsilon m\pmod{pm}.}
\tag{4.4}
\]

In particular,

\[
 b\ge
 \begin{cases}
 m-1,&m\text{ odd},\\
 2,&m\text{ even and }m\ge4.
 \end{cases}
\tag{4.5}
\]

#### Proof

An exact invariant factor would require

\[
 B=m(\varepsilon+pt).
\]

Modulo \(p\), the case \(\varepsilon=0\) contradicts (4.3).  In the
case \(\varepsilon=1\), multiplication by two gives

\[
 4(-1)^m\equiv-1\pmod p.
\]

If \(m\) is even this forces \(p\mid5\); if \(m\) is odd it forces
\(p\mid3\).  Thus no \(p\ge7\) is possible.  Applying (4.2) to a partial
factor gives (4.4).  Reducing (4.4) modulo \(p\), the least possible
residue is \(m-1\) for odd \(m\) and \(2\) for even \(m\), proving
(4.5). \(\square\)

The least residue permitted by (4.4) is below \(pm=O(m^2)\).  This says
only that the divisibility obstruction is polynomial; it does not
construct a partial factor attaining that residue.

### Theorem 4.3 -- the quadratic-residue owner obstruction

Let

\[
 Q=\{x^2:x\in\mathbb F_p^\times\},
\qquad
 H=\{x\mapsto ax:a\in Q\}.
\]

Then:

1. \(|Q|=m\), \(\operatorname{Stab}_G(Q)=H\), and
   \[
   |GQ|=2p;
   \tag{4.6}
   \]
2. no \(G\)-invariant middle-layer row packing covers \(Q\), or any
   member of its \(2p\)-element affine orbit;
3. there is no \(G\)-equivariant first-deletion selector
   \[
   d:\binom{\mathbb F_p}{m}\longrightarrow\mathbb F_p,
   \qquad d(X)\in X.
   \tag{4.7}
   \]
   Consequently there is no fully \(G\)-equivariant integral nested
   flag resolution of all middle roots.

#### Proof

The square multipliers \(H\) have order \(m\), preserve \(Q\), and act
regularly on it.  A nonempty proper subset has no translation
stabilizer.  Any \(p'\)-subgroup of \(G\) has a common fixed point; a
stabilizer containing \(H\) must therefore fix zero and lie in the
multiplier group.  Exactly the square multipliers preserve \(Q\).
This proves \(\operatorname{Stab}_G(Q)=H\) and (4.6).

For an unoriented row \(R\) with a distinguished proper cyclic interval
\(X\), the affine stabilizer of the pointed row \((R,X)\) has order at
most two.  For a non-AP row this follows from Lemma 4.1.  For an AP row,
its dihedral stabilizer acts on the \(p\) interval starts, and a proper
arc has point stabilizer of order two.

Suppose a \(G\)-invariant row packing contained a row \(R\) owning \(Q\).
For every \(h\in H\), the row \(hR\) would also be selected and would
also own \(Q\).  Uniqueness of the owner in a packing forces
\(hR=R\), so

\[
 H\le\operatorname{Stab}_G(R,Q),
\]

contradicting the pointed stabilizer bound because \(m\ge3\).  The same
argument applies to every affine image of \(Q\).

Finally, equivariance of (4.7) would give

\[
 d(Q)=h\,d(Q)\qquad(h\in H).
\]

The only field element fixed by every square multiplier is zero, but
\(0\notin Q\).  This is impossible.  A nested integral flag would in
particular supply such a first deletion. \(\square\)

The same stabilizer argument gives a bounded-degree strengthening.  In a
\(G\)-invariant exact \(t\)-fold middle cover, the rows above \(Q\) split
into \(H\)-orbits.  A pointed stabilizer has order at most two, so every
such orbit has size \(m\) when \(m\) is odd, and size \(m\) or \(m/2\)
when \(m\) is even.  Therefore

\[
 \boxed{
 m\mid t\quad(m\text{ odd}),\qquad
 \frac m2\mid t\quad(m\text{ even}).
 }
\tag{4.8}
\]

In particular, no bounded-degree affine-invariant multicover exists as
\(m\to\infty\).

These are exact obstructions, but their forced leave is small at the
coefficient-one scale.  The quadratic-residue orbit forces only \(2p\)
uncovered owners.  More generally Proposition 2.2 shows that the union
of all targets with affine stabilizer larger than two has total weighted
mass \(o(W)\) throughout every fixed Gaussian window.  Thus exact affine
equivariance is impossible, while an almost-equivariant core with an
exceptional high-stabilizer leave is not excluded.

## 5. Fractional equivariance exists but is annealed

Let \(\Omega\) be the set of all unoriented cyclic orders.  Then

\[
 |\Omega|=\frac{(p-1)!}{2},
\]

and a fixed rank-\(r\) target occurs as an interval in exactly

\[
 d_r=\frac{p!}{2\binom pr}
\tag{5.1}
\]

rows.  Giving every row weight \(1/d_m\) yields an
\(S_p\)-invariant, hence \(G\)-invariant, fractional exact middle factor.
At rank \(m-q\), every target then has the exactly uniform load

\[
 \frac{d_{m-q}}{d_m}=\frac W{N_q}=\lambda_q\in[c_q,c_q+1].
\tag{5.2}
\]

Thus the fractional balanced defect is identically zero at every depth.
Moreover this vector is a genuine fractional resolution into exact factors:
if \(F\) is any exact factor, averaging \(\sigma F\) over
\(\sigma\in S_p\) assigns weight \(1/d_m\) to every row.

This does not produce a low-defect integral constituent.  Relabelling
preserves the weighted shallow-shadow defect exactly, so every factor in
the orbit of \(F\) has defect \(J_A(F)\).  The orbit aggregate is perfectly
balanced only after loads from all constituents are superposed.  More
generally, an orbit resolution has average constituent defect \(o(W)\)
only if one of its seed factors already has defect \(o(W)\).

## 6. Exact frontier

The algebraic line therefore has the following exact verdict.

1. The distinct AP multiplier rows have exactly rainbow ordinary shadows
   at every central depth, with multiplicity ledger (2.2).
2. Their support has size only \(pm\), so AP-only weighted defect is
   \(\Omega_A(W\sqrt m)\), not \(o(W)\).  Even when used as a frozen
   seed, the uniform residual absorber violates the depth-two upper box
   by \(6/(m-1)\); a tailored residual flow is necessary.
3. The complete row-orbit sizes are \(m,pm,2pm\).  A degree-one
   \(AGL(1,p)\)-equivariant exact factor is impossible for every prime
   \(p\ge7\), and every invariant near-factor obeys the exact congruence
   (4.4).
4. The quadratic-residue owner orbit cannot be covered by any invariant
   row packing.  More strongly, its transitive stabilizer forbids an
   equivariant first-deletion selector, so a fully affine-equivariant
   integral nested resolution does not exist.
5. A perfectly balanced equivariant fractional resolution exists, but its
   balance is annealed and does not improve any constituent factor.
6. The high-stabilizer middle owners are a mandatory leave, while at
   shallow ranks one may voluntarily discard all high-stabilizer targets;
   the resulting fixed-window weighted mass is \(o(W)\).  The row-count
   residue is only polynomial.  Hence these exact obstructions do not
   rule out an almost-equivariant core made from exponentially many
   generic non-AP affine orbits.

The minimal positive theorem still missing is therefore:

> construct one exact wreath factor containing a \(G\)-invariant union of
> row orbits with \(B-o_A(B/\sqrt m)\) rows, after removing the mandatory
> high-stabilizer owners, and prove that the residual common nested flow
> has total fixed-window labelled cost \(o(W)\).

Neither extendibility of the AP orbit into a prescribed exact factor nor
the required generic large-orbit matching is proved here.  Any successful
construction must break full affine equivariance on the exceptional roots;
Theorem 4.3 shows that exact equivariant completion is impossible.

## 7. Adversarial audit

1. **Rainbow is not coverage.**  Theorem 2.1 proves multiplicity one on
   exactly \(pm\) targets.  Since \(N_q=\Theta_A(W)\), it gives no
   positive-density shallow resolution.

2. **Middle holes versus shallow collisions.**  A target stabilizer
   larger than two forces a hole only when multiplicity at most one is
   required.  This is mandatory at the middle layer.  At shallower ranks
   a factor may cover such a target several times; Proposition 2.2 is
   used there only to show that deleting the whole exceptional family is
   affordable.

3. **The depth-two failure is certificate-specific.**  Proposition 3.1
   refutes the uniform residual flow with frozen AP paths.  It does not
   refute a tailored residual flow which routes non-AP roots away from
   \(\mathcal A_{m-2}\).

4. **No hidden integral averaging.**  The fractional vector in Section 5
   is a convex average of exact factors, but affine relabelling preserves
   each constituent's defect.  Its zero aggregate defect cannot be
   assigned to one constituent by linearity.

5. **The absolute obstruction has narrow scope.**  Theorems 4.2--4.3
   rule out full \(AGL(1,p)\)-equivariance.  They do not rule out
   translation equivariance, an affine-invariant core with exceptional
   roots, or a non-equivariant exact factor with \(o(W)\) shallow defect.

6. **No near-factor is claimed.**  The congruence class (4.4) and the
   \(o(W)\) exceptional-orbit estimate are necessary/affordable ledgers,
   not an existence theorem for a union of compatible generic row
   orbits.
