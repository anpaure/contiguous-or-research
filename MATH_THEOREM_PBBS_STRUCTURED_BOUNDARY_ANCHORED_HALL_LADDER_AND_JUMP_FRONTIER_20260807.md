# The packet boundary passes every Greene--Kleitman cut, but the sharp compiler is an anchored Hall ladder

**Date:** 2026-08-07  
**Status:** unconditional exact min--max reduction, unconditional Boolean
cut theorem, unconditional packet-precoloured jump extension, and an
unconditional adjacent-rank no-go.  This note does **not** prove the
depth-\(d+2\) anchored chain factor.

## 1. Residual anchored factor and exact min--max

Let \(\mathcal O\) be one middle Boolean rank, \(|\mathcal O|=W\), and
let \(\mathcal L\) be its nonempty strict lower ideal.  Let

\[
 \mathcal R=\mathcal L\setminus\mathcal B,
 \qquad |\mathcal B|=h,
 \qquad |\mathcal R|=dW.
 \tag{1.1}
\]

The PBBS **depth** convention counts strict-lower targets and does not
count the terminal owner.  Put

\[
                         D=d+2.
 \tag{1.2}
\]

If instead “chain length” is taken to include the owner, use target cap
\(d+1\) in Sections 1--3 and 6.  Sections 4--5 use the native physical
collar width \(D=d+2\), so their symbol \(D\) is not shifted by that
terminological convention.

For an ordered partition

\[
             \mathcal R=A_1\mathbin{\dot\cup}\cdots
                          \mathbin{\dot\cup}A_D,
 \tag{1.3}
\]

put, for \(1\le i<D\),

\[
 N_i(X)=\{Y\in A_{i+1}:S\subsetneq Y
                    \text{ for some }S\in X\},
 \tag{1.4}
\]

and

\[
 N_D(X)=\{T\in\mathcal O:S\subsetneq T
                    \text{ for some }S\in X\}.
 \tag{1.5}
\]

Define the row deficiencies

\[
 \delta_i(A_\bullet)=
 \max_{X\subseteq A_i}\bigl(|X|-|N_i(X)|\bigr)
 \quad(1\le i\le D)
 \tag{1.6}
\]

and the anchored Hall-ladder deficiency

\[
 \boxed{
 \Delta_D(\mathcal R)=
 \min_{\mathcal R=A_1\dot\cup\cdots\dot\cup A_D}
          \max_{1\le i\le D}\delta_i(A_\bullet).}
 \tag{1.7}
\]

The empty set in (1.6) shows that every deficiency is nonnegative.

### Theorem 1.1 (exact anchored min--max)

The residual family \(\mathcal R\) has a partition

\[
                         (C_T:T\in\mathcal O)
 \tag{1.8}
\]

into strict inclusion chains, with \(C_T\subseteq\mathcal P(T)\) and
\(|C_T|\le D\), if and only if

\[
                         \boxed{\Delta_D(\mathcal R)=0.}
 \tag{1.9}
\]

#### Proof

Right-align every nonempty chain in \(D\) slices.  Consecutive elements
give injections

\[
 A_i\longrightarrow A_{i+1}\quad(1\le i<D),
 \qquad A_D\longrightarrow\mathcal O,
 \tag{1.10}
\]

along strict inclusion.  Hall's theorem makes these injections equivalent
to \(\delta_i=0\) in every row.

Conversely, choose all row injections independently.  Their union has
indegree and outdegree at most one, and slice indices strictly increase.
Its components are therefore paths ending at distinct owners.  Transitivity
of inclusion puts every target on a path below its terminal owner, and a
path contains at most one target from each of the \(D\) slices.  This gives
(1.8).  \(\square\)

Formula (1.7) is an exact finite min--max, but not a scalar closed form:
the minimization co-chooses the named time slices.  After the slices are
fixed, ordinary Hall is complete.  The slice choice is the correlated
integer gate.

## 2. Every global and owner-local Greene--Kleitman cut passes

For a finite poset \(P\), let

\[
 a_p(P)=\max\{|X|:X\text{ is a union of }p
                         \text{ antichains of }P\}.
 \tag{2.1}
\]

### Proposition 2.1 (global cuts pass at the stronger depth \(d\))

For every \(p\ge1\),

\[
 \boxed{
 a_p(\mathcal R)\le W\min(p,d)
                 \le W\min(p,D).}
 \tag{2.2}
\]

#### Proof

Every antichain in a Boolean lower half has size at most the middle rank
\(W\).  Hence a union of \(p\) antichains has size at most \(pW\).
It also has size at most \(|\mathcal R|=dW\).  Taking the smaller bound
gives (2.2).  \(\square\)

There is a stronger anchored version.  For \(Q\subseteq\mathcal O\), put

\[
 \mathcal R[Q]=
 \{S\in\mathcal R:N_{\mathcal O}(S)\subseteq Q\};
 \tag{2.3}
\]

these are the targets forced to owners in \(Q\).

### Theorem 2.2 (all localized anchored cuts pass)

Assume the arbitrary-boundary capacity theorem: every \(dW\)-subset of
\(\mathcal L\) matches to \(d\) labelled copies of each owner.  Then for
every \(Q\subseteq\mathcal O\) and every \(p\ge1\),

\[
 \boxed{
 a_p(\mathcal R[Q])\le |Q|\min(p,d).}
 \tag{2.4}
\]

#### Proof

Fix one symmetric-chain decomposition of the Boolean lattice.  Every
symmetric chain crosses the owner rank exactly once.  Send each lower set
to that owner on its symmetric chain.  If \(X\) is a union of \(p\)
antichains, one symmetric-chain fibre contains at most \(p\) members of
\(X\).  For \(X\subseteq\mathcal R[Q]\), every image owner lies in \(Q\),
so

\[
                              |X|\le p|Q|.
 \tag{2.5}
\]

The arbitrary-boundary matching sends every subfamily of \(\mathcal R\)
to owner copies injectively.  Applied to \(X\subseteq\mathcal R[Q]\), all
available copies lie over \(Q\), whence

\[
                              |X|\le d|Q|.
 \tag{2.6}
\]

Combining (2.5)--(2.6) and maximizing over \(p\)-families proves (2.4).
\(\square\)

Thus even the natural owner-localized Greene--Kleitman inequalities see no
obstruction.  This is stronger than checking only the whole lower ideal.

## 3. Why the Greene--Kleitman norm points in the wrong direction

For a chain partition \(\mathscr C\), write

\[
 \|\mathscr C\|_D=
       \sum_{C\in\mathscr C}\min(D,|C|).
 \tag{3.1}
\]

A maximum chain length at most \(D\) is equivalent to

\[
                         \|\mathscr C\|_D=|\mathcal R|,
 \tag{3.2}
\]

the **maximum** possible value of this norm.  Greene--Kleitman computes

\[
 a_D(\mathcal R)=
       \min_{\mathscr C}\|\mathscr C\|_D,
 \tag{3.3}
\]

the opposite extremum.  Its minimizing partition may also depend on the
chosen norm and carries no owner labels.  Therefore neither (2.2), (2.4),
nor simultaneous saturation of adjacent norms supplies the common slice
partition in (1.7).

This mismatch is structural, not a missing algebraic manipulation.  The
general cardinality-restricted chain-cover problem is not governed by the
separate \(a_p\)-cuts; the connected normal strong-Sperner three-arm
example in the capacitated Hall-ladder note passes all of them and still
needs an extra bounded chain.

## 4. What the packet-produced boundary actually adds

Use the native clean-packet notation

\[
 n=2m+1,\qquad D=d+2,\qquad a=m-d-2=m-D.
 \tag{4.1}
\]

A Hamilton-first packet bank supplies \(h=O(d^2)=O(m)\) pairwise distinct
bottoms and owners

\[
 M_j\in{[n]\choose a},qquad
 T_j\in{[n]\choose m},qquad M_j\subset T_j,
 \tag{4.2}
\]

with distinct endpoints.  Its deleted boundary targets satisfy

\[
 S_j\subseteq M_j,qquad 1\le |S_j|\le d.
 \tag{4.3}
\]

The next theorem shows that all prescribed packet jumps fit inside the
macroscopic Boolean jump row.

### Theorem 4.1 (polynomial precoloured jump matching extends)

Assume \(D=\Theta(\sqrt m)\).  For all sufficiently large \(m\), every
prescribed matching of size \(h=O(m)\) in the inclusion graph

\[
 { [n]\choose a}\longrightarrow { [n]\choose m}
 \tag{4.4}
\]

extends to a matching saturating the whole rank-\(a\) shore.  In
particular all packet pairs \(M_j\subset T_j\) in (4.2) can be retained.

#### Proof

Put

\[
 A={n\choose a},\qquad W={n\choose m},\qquad \rho=W/A.
 \tag{4.5}
\]

Since

\[
 {A\over W}=
 \prod_{j=0}^{D-1}{m-j\over m+2+j},
 \tag{4.6}
\]

and \(D=\Theta(\sqrt m)\), there is an absolute
\(\eta>0\) such that \(\rho\ge1+\eta\) for all large \(m\).
Normalized matching between Boolean ranks gives

\[
                         |N(X)|\ge\rho|X|
 \tag{4.7}
\]

for every \(X\subseteq{[n]\choose a}\).

Delete the \(h\) prescribed left and right endpoints.  In the residual
graph,

\[
                         |N'(X)|\ge\rho|X|-h.
 \tag{4.8}
\]

This is at least \(|X|\) whenever \(|X|\ge h/\eta\).  For nonempty
smaller \(X\), its neighborhood contains the entire neighborhood of one
rank-\(a\) set, of size

\[
                         {m+D+1\choose D}.
 \tag{4.9}
\]

That quantity dominates every polynomial in \(m\), whereas
\(h/\eta=O(m)\).  Hence \(|N'(X)|\ge|X|\) also for all smaller \(X\),
once \(m\) is large.  Hall matches the residual left shore; adjoining the
prescribed edges proves the theorem.  \(\square\)

This closes one honest packet-precoloured row.  It does not place the
other residual ranks into the same chains.

### Proposition 4.2 (exact marker-compatible reinsertion condition)

Let \((C_T)\) be any depth-\(D\) anchored factor of the packet residual.
Each surviving marker \(M_j\) lies in a different owner chain.  All deleted
targets \(S_j\) can be reinserted, with maximum depth increasing by at most
one, provided

\[
                         C_{T(j)}\cup\{S_j\}
                         \text{ is a chain for every }j,
 \tag{4.10}
\]

where \(T(j)\) is the owner chain containing \(M_j\).  Condition (4.10) is
equivalent to requiring every member of \(C_{T(j)}\) below \(M_j\) to be
comparable with \(S_j\); all members above \(M_j\) automatically contain
\(S_j\).  In particular, it holds if every \(M_j\) is the minimum of its
owner chain.

#### Proof

The \(M_j\)'s are distinct and have the same rank, so one strict chain
contains at most one of them.  Under (4.10), insert \(S_j\) into that chain.
The affected chains are distinct, every insertion preserves inclusion, and
each chain gains at most one target.  Conversely, in the fixed factor,
inserting \(S_j\) into its marker chain is possible exactly when it is
comparable with every existing member; the stated simplification follows
from \(S_j\subset M_j\).  \(\square\)

Thus a packet-residual factor is not automatically a complete-lower
factor.  Marker-compatible slice selection is the exact extra condition
needed for the simplest one-step reinsertion.

## 5. Adjacent-rank chainization is impossible at depth \(d+2\)

The packet boundary is supported in ranks at most \(d\).  For large \(m\),
it therefore leaves the two ranks

\[
                         m-1,qquad a-1=m-D-1
 \tag{5.1}
\]

untouched.

### Theorem 5.1 (the exact two-tooth interval obstruction)

The residual rank histogram cannot be decomposed into \(W\) skipless
rank intervals of length at most \(D\).  An exact dual certificate is

\[
 y_{m-1}=y_{a-1}=1,qquad y_s=0\quad(s\ne m-1,a-1).
 \tag{5.2}
\]

#### Proof

The two displayed ranks differ by \(D\).  An interval containing both has
at least \(D+1\) rank positions, so every interval of length at most \(D\)
meets at most one of them.  The required number of interval rows is
therefore at least

\[
 {n\choose m-1}+{n\choose a-1}.
 \tag{5.3}
\]

Now

\[
 {n\choose m-1}={m\over m+2}W
 \tag{5.4}
\]

and

\[
 {{n\choose a-1}\over W}
 =\prod_{j=0}^{D}{m-j\over m+2+j}.
 \tag{5.5}
\]

Because \(D=\Theta(\sqrt m)\), the product in (5.5) is bounded below by
a positive absolute constant.  It is therefore larger than
\(2/(m+2)\) for all large \(m\).  Equations (5.3)--(5.5) give a strict
lower bound greater than \(W\).  Formula (5.2) is precisely the dual
feasible vector for the consecutive-ones/TU interval min--max.  \(\square\)

The obstruction is not a Boolean-chain counterexample: arbitrary strict
chains may jump ranks.  It proves that jumps are macroscopically necessary.

### Corollary 5.2 (a positive density of chains must jump)

In any partition into at most \(W\) strict chains of size at most \(D\),
at least

\[
 {n\choose m-1}+{n\choose a-1}-W=\Omega(W)
 \tag{5.6}
\]

chains meet both ranks in (5.1), and every such chain has an inclusion step
whose rank increment is at least two.

Indeed, the two ranks are antichains, so (5.6) is the elementary overlap
bound.  A chain spanning rank difference \(D\) with at most \(D\) vertices
has at most \(D-1\) steps; not all increments can equal one.

Since the packet bank marks only \(h=O(m)=o(W)\) chains, its local collars
cannot by themselves provide the bulk jump compiler.  Theorem 4.1 shows
that the packet-prescribed jumps are compatible with one macroscopic jump
matching; Corollary 5.2 shows that a positive density of additional jumps
still has to be co-chosen with all remaining Hall rows.

## 6. Exact surviving Boolean frontier

The capacity theorem and a fixed symmetric-chain decomposition supply two
different projections:

* balanced owner loads, with no nestedness; and
* nested owner fibres, with no \(d+2\) balance.

The packet bank adds a polynomial precoloured submatching to a jump row.
None of these projections chooses the common ordered partition in (1.7).
The remaining statement is exactly

\[
 \boxed{
 \min_{\mathcal R=A_1\dot\cup\cdots\dot\cup A_D}
 \max\left\{
 \max_{i<D}\max_{X\subseteq A_i}
       (|X|-|N_{A_{i+1}}(X)|),
 \max_{X\subseteq A_D}
       (|X|-|N_{\mathcal O}(X)|)
 \right\}=0.}
 \tag{6.1}
\]

An all-dimensional proof of the same statement for the **complete** lower
ideal at depth \(d+O(1)\) would, by complement pairing, give a full Boolean
\(W\)-chain partition with maximum length

\[
                         {2^k\over W}+O(1).
 \tag{6.2}
\]

This is the additive one-sided Füredi frontier.  The packet-residual
statement (6.1) alone is slightly weaker: its \(h\) deleted targets remain
in separately priced boundary chains.  To obtain (6.2) from (6.1), one
would additionally need a marker-compatible reinsertion/absorption of
those boundary chains into the \(W\) owner chains with only constant depth
loss.  Neither that absorption nor the complete-lower theorem is supplied
by Greene--Kleitman, normalized matching, or the known asymptotically
uniform decompositions.
