# Nested-star atoms: exact Farkas dual, arithmetic invariants, and the even-\(m\) \(BA\)-flow obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,
 \qquad L=m(m+1),
 \]

and let \(\mathcal A\) be the fully labelled canonical nested-star atom
catalogue from
`MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md`.
Every atom \(\alpha\) has

* three source states \(I(\alpha)\);
* three \(A\)-successor states \(AI(\alpha)\);
* six distinct middle owners \(\Omega(\alpha)\); and
* zero nested Johnson divergence at every protected depth.

Write \(C=BA\).  The exact atom-flow equation says that the selected
source set is \(C\)-invariant.

This note gives three conclusions.

First, the fractional minimum-owner-leave LP has the exact dual

\[
 \boxed{
 \begin{aligned}
 \tau_f=\max\quad&\sum_Xu_X\\
 \text{subject to}\quad
 &u_X\le1 &&(X\in\tbinom{[n]}m),\\
 &\sum_{X\in\Omega(\alpha)}u_X
   +\sum_{e\in I(\alpha)}(\phi_e-\phi_{Ce})\le0
   &&(\alpha\in\mathcal A),
 \end{aligned}}
 \tag{0.1}
\]

where \(u_X,\phi_e\) are free.  Signed-divergence potentials disappear
because every complete atom column has divergence exactly zero.  The
uniform atom point has no owner leave and exact \(BA\)-flow, so

\[
                             \boxed{\tau_f=0.}
 \tag{0.2}
\]

More generally, with owner leave at most \(R\) and half-\(\ell^1\)
signed \(BA\)-flow residual at most \(\Delta\), the exact Farkas
right-hand side is

\[
 R\max\{0,\max_Xu_X\}
 +\Delta\max_{Q\in\mathcal E/\langle BA\rangle}
      \operatorname{osc}_Q(\phi).
 \tag{0.2a}
\]

Thus owner leave is dual to the largest positive owner price, while
flow error is dual to the largest potential oscillation on one
\(BA\)-orbit.

Second, every integral exact-flow solution with \(a\) atoms, \(k\)
activated \(BA\)-orbits, and \(\ell\) omitted owners obeys

\[
 6a=W-\ell,\qquad 3a=Lk,qquad
 \boxed{W-\ell=2Lk.}
 \tag{0.3}
\]

Hence

\[
 W-\ell\equiv0\pmod{\operatorname{lcm}(6,2L)}.
 \tag{0.4}
\]

If \(\ell_c\) is the number of omitted owners containing coordinate
\(c\), then

\[
                             \boxed{\ell_c\equiv0\pmod m.}
 \tag{0.5}
\]

In particular an exact full cover would require

\[
                             \boxed{2m(m+1)\mid\operatorname{Cat}_m.}
 \tag{0.6}
\]

These congruences alone are only polynomial-scale: their total modulus
is \(O(m^2)=o(W)\), and the smallest nonempty owner leave satisfying
(0.5) has size exactly \(m+1\).

Third, there is a much stronger parity obstruction.  If \(m\) is even,
then for every permutation state \(\pi\),

\[
                         \boxed{\kappa(A\pi)
                         =\kappa(C^{m+1}\pi).}
 \tag{0.7}
\]

Exact \(C\)-flow makes \(C^{m+1}\pi\) a selected source whenever
\(\pi\) is.  Equation (0.7) then repeats the owner of the selected
\(A\)-successor of \(\pi\).  Owner capacity forbids this.  Consequently,
for every even \(m\ge4\), the integral program has only the zero atom
selection:

\[
                             \boxed{\tau_{\mathbb Z}=W.}
 \tag{0.8}
\]

Thus the uniform fractional point cannot be rounded with \(o(W)\)
owner leave, even though it has exact \(BA\)-flow and zero signed
divergence.  This is an infinite-subsequence obstruction to the complete
nested-star atom architecture, not merely a TU failure.

For odd \(m\), the two owner-position sets in (0.7) have different
cardinalities on the two coordinate cycles of \(BA\), so this parity
collision vanishes.  The odd-\(m\) orbit-factor problem remains open.
No coefficient-one conclusion is claimed.

## 1. Atom columns and the exact LP/ILP

Let \(\mathcal E\) be the permutation-state set, identified with
injective \((n-1)\)-word de Bruijn arcs.  For an atom
\(\alpha\in\mathcal A\), define

\[
 A_{X,\alpha}=\mathbf1_{\{X\in\Omega(\alpha)\}},
 \tag{1.1}
\]

and

\[
 F_{e,\alpha}
 =\mathbf1_{\{e\in I(\alpha)\}}
 -\mathbf1_{\{e\in CI(\alpha)\}}.
 \tag{1.2}
\]

The complete nested-star identity gives, for every protected signed
target coordinate \((q,T)\),

\[
 G_{q,T;\alpha}=0.
 \tag{1.3}
\]

Thus the signed-divergence rows are literal zero rows after complete
atoms, rather than inequalities which still need rounding.

Use atom variables \(x_\alpha\) and owner-leave variables \(r_X\).  The
fractional minimum-leave program is

\[
 \begin{aligned}
 \tau_f=\min\quad&\sum_Xr_X\\
 \text{subject to}\quad
 &\sum_\alpha A_{X,\alpha}x_\alpha+r_X=1 &&(X),\\
 &\sum_\alpha F_{e,\alpha}x_\alpha=0 &&(e),\\
 &x_\alpha,r_X\ge0.
 \end{aligned}
 \tag{1.4}
\]

The ILP uses

\[
                         x_\alpha,r_X\in\{0,1\}.
 \tag{1.5}
\]

Because every atom column already satisfies (1.3), either program has
aggregate signed divergence exactly zero.  A prescribed leave budget
\(R\) is the additional inequality \(\sum_Xr_X\le R\).

### Theorem 1.1 (exact Farkas/LP dual)

The dual of (1.4) is (0.1).  Consequently the fractional system with
leave budget \(R\) is feasible if and only if every \((u,\phi)\)
satisfying the constraints in (0.1) obeys

\[
                             \sum_Xu_X\le R.
 \tag{1.6}
\]

#### Proof

Give the owner equalities free dual variables \(u_X\) and the flow
equalities free variables \(\phi_e\).  An atom has primal cost zero, so
its dual column inequality is

\[
 \sum_XA_{X,\alpha}u_X+\sum_eF_{e,\alpha}\phi_e\le0.
\]

By (1.2), the second sum is
\(\sum_{e\in I(\alpha)}(\phi_e-\phi_{Ce})\).  A leave variable has
cost one and appears only in its owner row, giving \(u_X\le1\).
The dual objective is the owner right-hand side \(\sum_Xu_X\).  This is
(0.1).  Both programs are feasible---take \(x=0,r=1\)---and the primal
is bounded, so finite-dimensional strong duality applies.  The budget
criterion (1.6) is exactly the assertion \(\tau_f\le R\). \(\square\)

If formal signed-divergence rows are retained with free potentials
\(\theta_{q,T}\), every atom constraint acquires
\(\sum_{q,T}\theta_{q,T}G_{q,T;\alpha}=0\).  Hence they do not change
the dual.  This is why the remaining obstruction is flow/ownership,
not Johnson discrepancy inside an atom.

### Proposition 1.2 (uniform fractional point)

Let

\[
 d_{\rm own}=m^2(m+1)(m-1)^3,
 \qquad
 d_{\rm lab}=2((m-1)!)^4d_{\rm own}.
 \tag{1.7}
\]

Then

\[
                         x_\alpha^*={1\over d_{\rm lab}},
 \qquad r_X^*=0
 \tag{1.8}
\]

is feasible in (1.4), and therefore proves (0.2).

#### Proof

The canonical catalogue is exactly owner-regular of labelled degree
\(d_{\rm lab}\), so every owner equation has load one.  Every state has
the same number of source-atom occurrences by relabelling transitivity.
The same is true of its \(C\)-preimage, and \(C\) is a permutation of
states.  Hence the two sides of every flow row have equal uniform load.
Equation (1.3) gives exact signed cancellation. \(\square\)

For completeness, there is also an exact Farkas form when the signed
\(BA\)-flow residual itself is allowed.  Put

\[
                         h_e=\sum_\alpha F_{e,\alpha}x_\alpha.
 \tag{1.9}
\]

Let \(\mathcal P(R,\Delta)\) consist of the owner equations in (1.4),
nonnegativity, and the two budgets

\[
                         \sum_Xr_X\le R,
 \qquad {1\over2}\sum_e|h_e|\le\Delta.
 \tag{1.10}
\]

Every residual \(h\) generated by atom columns has coordinate sum zero
on each \(C\)-orbit.

### Theorem 1.3 (leave-and-flow-defect Farkas criterion)

The system \(\mathcal P(R,\Delta)\) is fractionally feasible if and
only if the following implication holds for every free owner vector
\(u\) and free state potential \(\phi\).  If

\[
 \sum_{X\in\Omega(\alpha)}u_X
 +\sum_{e\in I(\alpha)}(\phi_e-\phi_{Ce})\le0
 \qquad(\alpha\in\mathcal A),
 \tag{1.11}
\]

then

\[
 \boxed{
 \sum_Xu_X\le
 R\max\{0,\max_Xu_X\}
 +\Delta\max_{Q\in\mathcal E/\langle C\rangle}
       \operatorname{osc}_Q(\phi),}
 \tag{1.12}
\]

where

\[
 \operatorname{osc}_Q(\phi)
 =\max_{e\in Q}\phi_e-\min_{e\in Q}\phi_e.
\]

#### Proof

Assume first that \((x,r,h)\) is feasible.  Multiply (1.11) by
\(x_\alpha\) and sum.  The owner equations and (1.9) give

\[
                         \sum_Xu_X
 \le u\mathbin\cdot r-\phi\mathbin\cdot h.
 \tag{1.13}
\]

The support function of
\(\{r\ge0:\sum_Xr_X\le R\}\) is
\(R\max\{0,\max_Xu_X\}\).  On one \(C\)-orbit, \(h\) has coordinate
sum zero, and the dual norm of \(\frac12\|h\|_1\) on that subspace is
the oscillation of \(\phi\).  With one aggregate budget, the support
function over all orbit blocks is
\(\Delta\max_Q\operatorname{osc}_Q(\phi)\).  This proves (1.12).

Conversely, separate the owner-and-flow image of the nonnegative atom
cone from the product of the leave simplex and the orbitwise zero-sum
\(\ell^1\)-ball.  A separating functional is exactly a pair
\((u,\phi)\) satisfying (1.11) and violating (1.12).  The
finite-dimensional Farkas alternative therefore proves sufficiency.
\(\square\)

The uniform point has \(R=\Delta=0\), so averaging (1.11) against it
gives \(\sum_Xu_X\le0\).  Hence no fractional dual cut obstructs even
the zero-budget system.

## 2. Orbit and congruence invariants

Let \((x,r)\) be an integral feasible point of (1.4).  Put

\[
 a=\sum_\alpha x_\alpha,
 \qquad \ell=\sum_Xr_X,
 \tag{2.1}
\]

and define the selected-source multiplicity

\[
                         s_e=\sum_{\alpha:e\in I(\alpha)}x_\alpha.
 \tag{2.2}
\]

Two selected atoms through one source state would share its source
owner, contrary to the owner equation.  Thus \(s_e\in\{0,1\}\).  The
flow rows say

\[
                             s_e=s_{C^{-1}e}.
 \tag{2.3}
\]

The position permutation \(C=BA\) has disjoint cycles of lengths
\(m\) and \(m+1\), so every state orbit has length \(L=m(m+1)\).
Therefore \(S=\{e:s_e=1\}\) is a union of \(k\) complete \(C\)-orbits.

### Theorem 2.1 (total modular ledger)

Every integral feasible point satisfies (0.3) and (0.4).  More
explicitly,

\[
 W-\ell\equiv0\pmod{M_m},
 \qquad
 M_m=\operatorname{lcm}(6,2m(m+1))
 ={6m(m+1)\over\gcd(3,m(m+1))}.
 \tag{2.4}
\]

#### Proof

Every selected atom covers six owners, giving \(6a=W-\ell\).  It has
three source states, so \(|S|=3a\).  Since \(S\) is a union of \(k\)
full orbits, \(3a=Lk\).  Elimination of \(a\) gives (0.3).  The covered
owner count is divisible by both six and \(2L\), proving (2.4).
\(\square\)

The modulus \(M_m=O(m^2)\) is \(o(W)\).  Hence this scalar congruence
alone cannot exclude an \(o(W)\) owner leave.

### Lemma 2.2 (the \(BA\)-flow matrix has no finite torsion)

On every \(C\)-orbit \(Q\),

\[
 (I-C)\mathbb Z^Q
 =\left\{h\in\mathbb Z^Q:\sum_{e\in Q}h_e=0\right\}.
 \tag{2.5}
\]

Equivalently, the Smith normal form of the directed-cycle incidence
matrix is

\[
                         \operatorname{diag}(1,\ldots,1,0).
 \tag{2.6}
\]

#### Proof

The inclusion from left to right follows by summing a discrete
difference around the cycle.  Conversely, enumerate
\(Q=(e_0,Ce_0,\ldots,C^{L-1}e_0)\).  If \(\sum_jh_j=0\), define

\[
                         s_0=0,\qquad
                         s_j=\sum_{i=1}^{j}h_i.
\]

Then \(h=s-Cs\), after choosing the cyclic orientation consistently.
Thus the image is the full integral zero-sum lattice.  Equivalently,
deleting one row and one column from the cycle incidence matrix leaves
a triangular matrix of determinant one, proving the displayed Smith
form. \(\square\)

In particular, an interval of any prescribed length on one \(C\)-orbit
has only two nonzero boundary entries.  The bare flow lattice therefore
has no hidden mod-\(p\) obstruction to an \(o(W)\) boundary; all further
arithmetic restrictions come from coupling its phases to complete atom
and owner columns.

There is also a coordinatewise congruence.  Let

\[
 \ell_c=\sum_{X\ni c}r_X.
 \tag{2.7}
\]

For one \(C\)-orbit \(\mathcal O\), let \(P(\mathcal O)\) be the set of
the \(m\) labels occupying the length-\(m\) coordinate cycle of \(C\).

### Theorem 2.2 (coordinate leave and exact-cover divisibility)

If \(k_c\) of the \(k\) active orbits have
\(c\in P(\mathcal O)\), then

\[
 m\operatorname{Cat}_m-\ell_c=m^2k+mk_c.
 \tag{2.8}
\]

Consequently (0.5) holds.  If \(\ell=0\), then

\[
 k={n\operatorname{Cat}_m\over2m(m+1)},
 \qquad
 k_c={\operatorname{Cat}_m\over2(m+1)},
 \tag{2.9}
\]

and (0.6) is necessary.

#### Proof

The two position cycles of \(C\) have lengths \(m\) and \(m+1\).
Across the source-owner position set \(\{1,\ldots,m\}\) and the
\(A\)-successor-owner position set \(\{2,\ldots,m+1\}\), the total
number of positions lying on each coordinate cycle is exactly \(m\).

During a full \(C\)-orbit, a label on the length-\(m\) cycle visits
each of its positions \(m+1\) times.  It therefore occurs in
\(m(m+1)=L\) source/successor owner incidences.  A label on the
length-\(m+1\) cycle visits each position \(m\) times and occurs in
\(m^2\) incidences.  Summing over the \(k\) active orbits gives
\(m^2k+mk_c\).

There are

\[
 \binom{n-1}{m-1}=m\operatorname{Cat}_m
\]

middle owners containing \(c\).  Removing the \(\ell_c\) omitted ones
proves (2.8), and divisibility by \(m\) gives (0.5).

For an exact cover, (0.3) gives the displayed value of \(k\), and
(2.8) gives the displayed value of \(k_c\).  Finally

\[
 \gcd(2m+1,2m(m+1))=1.
\]

Since \(k\) is integral and
\(W=(2m+1)\operatorname{Cat}_m\), this forces (0.6). \(\square\)

### Proposition 2.3 (endpoint-balance and mod-three invariants)

For every exact-flow integral atom family,

\[
                             \boxed{2m+1\mid k.}
 \tag{2.10}
\]

Consequently

\[
                             W-\ell\equiv0
                             \pmod{2m(m+1)(2m+1)}.
 \tag{2.11}
\]

Moreover, for distinct labels \(a,b\), let \(k_{a\mid b}\) count
active \(C\)-orbits whose length-\(m\) coordinate cycle contains \(a\)
and whose length-\(m+1\) cycle contains \(b\).  Then

\[
                             \boxed{k_{a\mid b}\equiv0\pmod3.}
 \tag{2.12}
\]

#### Proof

Let \(k_c\) count active orbits placing \(c\) on the length-\(m\)
position cycle.  Across one such orbit, \(c\) occurs in position one
exactly \(m+1\) times and never in position \(n\).  Across any other
active orbit, it occurs in position \(n\) exactly \(m\) times and never
in position one.  In every oriented star atom, each endpoint label
occurs equally often in the first and missing-coordinate positions.
Therefore

\[
                         (m+1)k_c=m(k-k_c),
 \qquad (2m+1)k_c=mk.
 \tag{2.13}
\]

Since \(\gcd(m,2m+1)=1\), this proves (2.10); (0.3) then gives (2.11).

For the ordered-pair assertion, one full \(C\)-orbit contains exactly
one phase with endpoint pair \((\pi(1),\pi(n))=(a,b)\) precisely when
\(a\) lies on its first coordinate cycle and \(b\) on its second.  This
is the Chinese remainder theorem for the coprime lengths \(m,m+1\).
Exact flow bijects selected sources with their \(C\)-images.  In
\(C\pi\), the final two entries of the canonical ordered suffix are
\(\pi(1),\pi(n)\).  The three sources of one atom have a common ordered
suffix, so every such suffix pair is counted in multiples of three.
Thus \(k_{a\mid b}\equiv0\pmod3\). \(\square\)

All these moduli are polynomial in \(m\); none alone excludes an
\(o(W)\) leave.

### Proposition 2.4 (the coordinate congruence is polynomially cheap)

Every nonempty simple owner leave satisfying (0.5) has size at least
\(m+1\), and this bound is attained.

#### Proof

Choose one omitted owner \(X\).  Each of its \(m\) coordinates has
positive leave degree and hence, by (0.5), degree at least \(m\).
Thus

\[
                         m\ell=\sum_c\ell_c\ge m^2,
\]

so \(\ell\ge m\).  Equality would force the \(m\) owners in the leave
all to contain the same \(m\)-set \(X\), impossible for a simple family.
Hence \(\ell\ge m+1\).

Conversely, for any \((m+1)\)-set \(U\), the top clique
\(\binom U m\) contains \(m+1\) owners.  Every coordinate in \(U\)
has leave degree \(m\), and every outside coordinate has degree zero.
This attains the bound. \(\square\)

For example, if \(m=p>2\) is prime, then
\(\operatorname{Cat}_p\equiv2\pmod p\), so (0.6) excludes an exact
cover.  Proposition 2.3 shows why this modular argument alone cannot
exclude a polynomial, hence \(o(W)\), leave.

## 3. The even-\(m\) orbit-owner collision

Let \(\sigma\) be the position permutation characterized by

\[
                         (C\pi)_j=\pi_{\sigma(j)}.
 \tag{3.1}
\]

Directly from

\[
 C(x_1,\ldots,x_n)
 =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2),
\]

its two cycles are

\[
 \sigma=(1\ 3\ 5\ \cdots\ 2m-1)
        (2\ 4\ 6\ \cdots\ 2m\ 2m+1).
 \tag{3.2}
\]

Put

\[
                         P_0=\{1,\ldots,m\},
 \qquad P_1=\{2,\ldots,m+1\}.
 \tag{3.3}
\]

Thus \(\kappa(\pi)=\pi(P_0)\) and
\(\kappa(A\pi)=\pi(P_1)\), where \(\pi(P)\) denotes the set of labels
in the position set \(P\).

### Lemma 3.1 (even parity identity)

If \(m\) is even, then

\[
                             P_1=\sigma^{m+1}P_0,
 \tag{3.4}
\]

and consequently (0.7) holds.

#### Proof

Write \(m=2s\).  On the first cycle of (3.2), the set
\(P_0\) occupies

\[
                         \{1,3,\ldots,2s-1\},
\]

whereas \(P_1\) occupies

\[
                         \{3,5,\ldots,2s+1\}.
\]

Thus it is shifted by one step.  Since \(m+1\equiv1\pmod m\),
\(\sigma^{m+1}\) makes precisely this shift.  On the second cycle,
both \(P_0\) and \(P_1\) occupy \(\{2,4,\ldots,2s\}\), and
\(m+1\equiv0\pmod{m+1}\), so that part is fixed.  This proves (3.4).

Finally,

\[
 \kappa(C^{m+1}\pi)
 =\pi(\sigma^{m+1}P_0)
 =\pi(P_1)=\kappa(A\pi).
\]

\(\square\)

### Theorem 3.2 (exact-flow no-go for even \(m\))

For every even \(m\ge4\), an integral solution of (1.4) has
\(x_\alpha=0\) for every atom.  Therefore (0.8) holds.

#### Proof

Suppose some source \(\pi\) is selected.  Exact flow (2.3) makes the
whole \(C\)-orbit selected, in particular \(C^{m+1}\pi\).

The atom through \(\pi\) uses \(\kappa(A\pi)\) as one of its successor
owners.  The atom through \(C^{m+1}\pi\) uses
\(\kappa(C^{m+1}\pi)\) as one of its source owners.  Lemma 3.1 says
these owners are equal.  They are two distinct owner occurrences:
within one canonical atom all six owners are distinct, and for
\(m\ge3\) its three sources lie in distinct \(C\)-orbits.  Hence the
owner row has load at least two, contradicting (1.4).

Thus the selected source set is empty, and every atom variable is zero.
The owner equations then force \(r_X=1\) for all \(W\) owners, proving
\(\tau_{\mathbb Z}=W\). \(\square\)

For odd \(m=2s+1\), \(P_0\) occupies \(s+1\) positions on the
length-\(m\) cycle and \(P_1\) occupies \(s\), while their counts on
the other cycle are \(s\) and \(s+1\).  Powers of \(\sigma\) preserve
these two counts, so no identity of the form (3.4) exists.  This proves
that Theorem 3.2 is a sharp parity obstruction at the single-orbit level.

## 4. What happens if exact \(BA\)-flow is relaxed

The parity identity also gives a quantitative, but sublinear-scale,
boundary.  Let \(x\) be any integral owner-disjoint atom packing, not
necessarily flow-balanced, and put

\[
 S=\bigcup_{\alpha:x_\alpha=1}I(\alpha),
 \qquad
 \mathfrak b_C(S)=|S\triangle CS|.
 \tag{4.1}
\]

### Proposition 4.1 (sharp-order approximate-flow toll)

For even \(m\),

\[
 \boxed{
 \mathfrak b_C(S)\ge{2|S|\over m+1}
 ={W-\ell\over m+1}.}
 \tag{4.2}
\]

Equivalently, for the half-\(\ell^1\) budget in (1.10),

\[
                         \Delta\ge{W-\ell\over2(m+1)}.
 \tag{4.3}
\]

#### Proof

Lemma 3.1 and owner-disjointness imply

\[
                             S\cap C^{m+1}S=\varnothing.
 \tag{4.4}
 \]

On each cyclic \(C\)-orbit, write the indicator of \(S\) as a cyclic
binary word.  Every run of consecutive ones has length at most \(m+1\),
for otherwise its first and \((m+2)\)-nd positions would violate (4.4).
If the word has \(r\) one-runs, it contains at most \((m+1)r\) ones and
contributes exactly \(2r\) to \(|S\triangle CS|\).  Summing over the
orbits proves the first inequality.

Every selected atom has three source states and six covered owners, so
\(|S|=3a=(W-\ell)/2\).  This proves the equality in (4.2). \(\square\)

The order of (4.2) is sharp before the atom-triple constraint is imposed.
On one \(C\)-orbit choose the consecutive phases

\[
                         S_0=\{\pi,C\pi,\ldots,C^m\pi\}.
 \tag{4.5}
\]

It has \(|S_0\triangle CS_0|=2\).  Source owners and successor owners
within this block are all distinct: source--source and
successor--successor repetitions would stabilize \(P_0\) or \(P_1\),
while a cross repetition requires phase difference exactly \(m+1\) by
Lemma 3.1, larger than any difference in the block.  Thus the bare
orbit-owner projection attains equality in (4.2).  What is not known is
how to partition many such blocks into legal nested-star triples while
keeping their owner families disjoint.

The toll in (4.2)--(4.3) is \(\Theta(W/m)=o(W)\).  Therefore the exact-flow
no-go does **not** exclude a different architecture which permits an
\(o(W)\) \(BA\)-boundary and repairs it globally.  It only closes the
exact atom-circulation LP/ILP posed here.

## 5. Proved boundary

Proved:

1. (0.1) is the exact Farkas dual of the exact owner-leave plus
   \(BA\)-flow atom LP, and (1.12) is the exact leave-and-flow-defect
   Farkas criterion.
2. The uniform point has fractional leave zero and exact signed
   divergence.
3. Every integral solution obeys the total, coordinatewise,
   endpoint-balance, and ordered-pair congruence invariants in Section 2.
4. On every even \(m\ge4\), exact \(BA\)-flow and owner capacity force
   the zero atom solution, so no rounding with \(o(W)\) owner leave is
   possible.
5. If exact flow is weakened, the parity obstruction costs only
   \(\Theta(W/m)=o(W)\) boundary, so approximate-flow rounding remains a
   separate open problem.

Not proved:

1. an odd-\(m\) exact-flow near-cover;
2. an owner near-cover with \(o(W)\) \(BA\)-boundary; or
3. the coefficient-one theorem.

The nested-star atom lane is therefore exhausted in its exact-flow form.
A successor construction must either work only on the odd subsequence
and bridge parity externally, or permit and globally absorb a Catalan-
scale \(BA\)-boundary.
