# Exact core renewal for the canonical truncated parallel-pair bridge

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Every upper-core word of rank \(m+2\) has a unique decomposition

\[
                         T=QV,
\]

where \(Q\) ends with the last up-step from height three to height four and
\(V\) is Dyck.  For the canonical MSW factor:

1. the first-shadow load of \(T\) is exactly the base load of \(Q\);
2. the truncated parallel-pair involution acts independently on \(Q\) and
   \(V\);
3. therefore every joint load-transition statistic has an exact Catalan
   renewal formula.

In particular, if \(p_k\) counts core words in semilength \(k\) whose
loads under the truncated involution are \((0,1)\), then every diagonal
replacement in semilength \(m\) retains at least

\[
 \boxed{
 P_m=\sum_{k=2}^{m}\operatorname {Cat}_{m-k}p_k}
\tag{0.1}
\]

first-shadow holes.  For the full parallel-pair involution the same lower
bound holds with \(k\le m-1\).  The symbolic semilength-four table gives
\(p_4=2\), recovering the floor \(2\operatorname {Cat}_{m-4}\).

Thus the question of a linear extension-disjoint obstruction is reduced to
the growth of one explicit finite-dimensional core sequence \((p_k)\).

## 1. Unique last-exit decomposition

Represent a rank-\((m+2)\) target on \([2m]\) by a binary path \(T\) with
\(m+2\) up-steps and \(m-2\) down-steps.  Its final height is four.

Let \(2k\) be the position of the last up-step which starts at height three.
Such a step exists, since the path starts at zero and ends at four.  After
this step the path never visits height three again.  Hence the suffix after
position \(2k\), translated down by four, is a Dyck word \(V\).  The prefix
\(Q\) has length \(2k\), ends at height four, and its last bit is one.
Parity forces the exit position to be even.  Thus

\[
 T=QV,
 \qquad |Q|=2k,
 \qquad |Q|_1=k+2,
 \qquad Q_{2k}=1,
 \qquad V\in\mathcal D_{m-k}.
\tag{1.1}
\]

The last exit is unique, so this decomposition is unique.

Let \(\mathcal C_k\) denote the family of all prefixes \(Q\) in (1.1).
Equivalently,

\[
 \mathcal C_k=
 \{Q\in\{0,1\}^{2k}:|Q|_1=k+2, Q_{2k}=1\}.
\tag{1.2}
\]

Indeed the last coordinate then starts at height three automatically, and
the empty suffix witnesses the required last-exit property.

## 2. Exact load localization

Let \(g_k(Q)\) be the multiplicity of the rank-\((k+2)\) target \(Q\) in
the internal semilength-\(k\) MSW map \(\Gamma\).  Equivalently, after
upper/lower complementation, it is the canonical first-shadow load of the
associated lower target in dimension \(2k+1\).

### Theorem 2.1

For every \(Q\in\mathcal C_k\) and \(V\in\mathcal D_{m-k}\),

\[
 \boxed{g_m(QV)=g_k(Q).}
\tag{2.1}
\]

### Proof

Suppose

\[
 \Gamma(x_i)=QV,
 \qquad x_i=QV\setminus\{a,b\},
\]

where \(a\) is inserted by the MSW map \(g\), and \(b\) is deleted by the
preceding \(h\)-move.  The prefix \(Q\) ends at height four.  If \(a\)
were in the suffix, its target starting height would be at least four;
deletion of \(b\) could lower it by at most two.  But \(g\) selects only a
down-step starting at height zero or one.  Therefore \(a\) lies in \(Q\).

The upper state supplied to \(h\) is \(QV\setminus\{a\}\).  Its prefix
ends at height two, so every up-step in the Dyck suffix starts at height at
least two.  Since \(h\) selects only among up-steps starting at height zero
or one, \(b\) also lies in \(Q\).

Thus every preimage has the form \(PV\), where \(P\) is a balanced
length-\(2k\) base state.  The MSW concatenation identity

\[
 \rho(uV)=\rho(u)\mathbin\Vert(2k+\rho(V))
\]

and uniqueness of the canonical owner show that \(PV\) belongs to the
column rooted at \(uV\) exactly when \(P\) belongs to the base column rooted
at \(u\).  Conversely every base preimage extends in this way.  This proves
(2.1). \(\square\)

## 3. Factorization of the truncated involution

Put

\[
 \sigma_{{\rm tr},m}
 =(2\ 3)(4\ 5)\cdots(2m-2\ \ 2m-1).
\tag{3.1}
\]

On \(Q\in\mathcal C_k\), define

\[
 \theta_k=(2\ 3)(4\ 5)\cdots(2k-2\ \ 2k-1).
\tag{3.2}
\]

On a suffix \(V\in\mathcal D_d\), define

\[
 \eta_d=(2\ 3)(4\ 5)\cdots(2d-2\ \ 2d-1).
\tag{3.3}
\]

Every factor of \(\eta_d\) preserves the Dyck family.  The two entries in
the boundary pair \((2k,2k+1)\) are both one: \(Q\) ends with one and a
nonempty Dyck word begins with one.  If the suffix is empty there is no
boundary pair.  Therefore

\[
 \boxed{
 \sigma_{{\rm tr},m}(QV)
 =\theta_k(Q)\,\eta_{m-k}(V).}
\tag{3.4}
\]

The map \(\theta_k\) preserves \(\mathcal C_k\): it fixes the final bit,
and its last internal swap preserves the height immediately before that
bit.  The map \(\eta_d\) is a bijection of \(\mathcal D_d\).

Combining (2.1) and (3.4),

\[
 \boxed{
 \bigl(g_m(QV),g_m(\sigma_{{\rm tr},m}(QV))\bigr)
 =\bigl(g_k(Q),g_k(\theta_kQ)\bigr).}
\tag{3.5}
\]

## 4. Exact renewal formula

For nonnegative integers \(a,b\), put

\[
 p_k(a,b)=
 \#\{Q\in\mathcal C_k:g_k(Q)=a, g_k(\theta_kQ)=b\}.
\tag{4.1}
\]

Let \(P_m(a,b)\) be the number of rank-\((m+2)\) core targets with joint
load pattern \((a,b)\) under the canonical factor and its truncated
parallel relabeling.  The unique decomposition (1.1), (3.5), and the count
\(|\mathcal D_{m-k}|=\operatorname {Cat}_{m-k}\) give

\[
 \boxed{
 P_m(a,b)=
 \sum_{k=2}^{m}\operatorname {Cat}_{m-k}\,p_k(a,b).}
\tag{4.2}
\]

This is an identity, not an asymptotic estimate.

Take

\[
 p_k=p_k(0,1).
\tag{4.3}
\]

After upper/lower complementation, every target counted by \(P_m(0,1)\)
belongs to an involution orbit with first-shadow loads \((0,1)\).  The
orbit-mass floor leaves one hole on every such orbit after every diagonal
row replacement.  Hence (0.1).

For the full involution

\[
 \sigma_{{\rm full},m}
 =\sigma_{{\rm tr},m}(2m\ \ 2m+1),
\]

the same factorization holds whenever \(m-k\ge1\): the last suffix bit and
the distinguished coordinate are both absent from the upper target.  Thus

\[
 \boxed{
 H_1((F\setminus A)\sqcup\sigma_{{\rm full},m}A)
 \ge
 \sum_{k=2}^{m-1}\operatorname {Cat}_{m-k}p_k.}
\tag{4.4}
\]

The empty-suffix sector \(k=m\) lies in the other full-involution chart and
is deliberately omitted.

## 5. First nonzero core coefficient

In semilength four, the complete symbolic \(\Gamma\)-table has exactly two
missing rank-six targets, with complements \(47\) and \(25\).  The map
\(\theta_4=(2\ 3)(4\ 5)(6\ 7)\) sends these complements to \(56\) and
\(34\), respectively.  Each image occurs exactly once in the same table.
Therefore

\[
 \boxed{p_4=2.}
\tag{5.1}
\]

Equations (0.1) and (4.4) consequently imply the explicit universal floor

\[
 \boxed{2\operatorname {Cat}_{m-4}}
\]

for the truncated bridge, and for the full bridge when \(m\ge5\).

No lower bound on the later coefficients \(p_k\) is proved here.  A linear
first-shadow floor would follow, for example, from

\[
 \sum_{k\le m}\operatorname {Cat}_{m-k}p_k=\Omega(W).
\tag{5.2}
\]

The renewal identity isolates this as a finite-core algebraic question,
rather than an owner-conductance or endpoint-extension question.

## 6. Why the marked-gap insertion does not amplify `p_k`

A tempting strategy is to prepend a Dyck word `U` to one of the two
semilength-four cores `B_i`.  Since

\[
                         Q=UB_i\in\mathcal C_k,
 \qquad |U|=2(k-4),
\tag{6.1}
\]

this produces `Cat_(k-4)` core words, and one might try to move the base
block through `Theta(k)` gaps of `U`, as in the marked-gap collision
theorem.  The two exact identities used by the renewal theorem both fail at
the left boundary.

### Proposition 6.1 (active parallel-pair boundary)

Let `U` be a nonempty Dyck word and let `B` be either `B_0` or `B_1`.
Then the truncated involution does not factor across `U|B`.

#### Proof

The length of `U` is even, its last bit is zero, and the first bit of each
`B_i` is one.  The truncated involution contains the boundary transposition

\[
                         (|U|,|U|+1).
\tag{6.2}
\]

It therefore changes the boundary word

\[
                             0\,|\,1
 \quad\longmapsto\quad
                             1\,|\,0.
\tag{6.3}
\]

In particular

\[
 \theta_k(UB_i)\ne \eta_{k-4}(U)\,\theta_4(B_i).
\tag{6.4}
\]

This is the opposite of the right-suffix factorization (3.4), where the
boundary bits are `1|1` and the crossing pair is inert. \(\square\)

### Proposition 6.2 (loss of `Gamma` localization on the left)

The height argument proving Theorem 2.1 does not localize preimages of
`UB_i` to the final eight coordinates.

#### Proof

For a right Dyck suffix in `QV`, the prefix `Q` ends at height four.  Any
candidate `g`- or `h`-coordinate in `V` therefore starts at height at least
four or, after one deletion, at least two.  This excludes it because the
canonical selectors act only at heights zero and one.

For `UB_i`, the word `U` starts and ends at height zero.  It contains down
steps starting at height one and up steps starting at height zero or one.
These are exactly the heights eligible for the `g` and `h` selectors.
Hence a preimage may use coordinates in `U`; the proof of the bijection
between base preimages and extended preimages has no analogue on this
side. \(\square\)

### Consequence

The existing identities certify only the terminal placement of the
semilength-four core followed by a Dyck suffix in the *ambient* target.
Inside the last-exit core counted by `p_k`, that suffix is empty because a
core word must end with the last up-step from height three to four.

Therefore the marked-gap count does not yield

\[
                         p_k\gg k\operatorname {Cat}_{k-4}.
\tag{6.5}
\]

The obstruction is not merely an unproved independence assumption: moving
the block to the left simultaneously activates a parallel-pair boundary and
reopens low-height canonical preimages.  Any linear lower bound on `p_k`
must use a new prefix-localization/cancellation identity that controls both
effects, rather than the present suffix-concatenation theorem.
