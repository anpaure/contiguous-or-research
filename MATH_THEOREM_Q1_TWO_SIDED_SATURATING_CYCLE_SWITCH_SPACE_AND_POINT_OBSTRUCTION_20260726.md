# Two-sided \(q=1\) saturating cycles: the exact switch lattice, point-margin obstruction, and a pentagonal escape

Date: 2026-07-26

Method: pure mathematics only.  The two-level saturating-cycle theorem is
used only through the exact lower-rainbow Johnson cycle already proved.

## 0. Outcome

Let \(n\in\{2m,2m+1\}\), and put

\[
 \mathcal M=\binom{[n]}m,\qquad
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1},
 \qquad N_-=|\mathcal L|.                            \tag{0.1}
\]

The two-level saturating-cycle theorem supplies a simple Johnson cycle
\[
 C=X_0X_1\cdots X_{N_--1}X_0                         \tag{0.2}
\]
on \(N_-\) distinct middle owners such that the lower colours
\[
                         X_i\cap X_{i+1}              \tag{0.3}
\]
are exactly the members of \(\mathcal L\), once each.

Write
\[
 u_C(U)=\#\{i:X_i\cup X_{i+1}=U\},\qquad
 R^+(C)=\sum_{U\in\mathcal U}(u_C(U)-1)_+.            \tag{0.4}
\]

Then the exact upper hole count is
\[
 \boxed{
 M^+(C)=|\mathcal U|-N_-+R^+(C).}                    \tag{0.5}
\]
Thus the two-sided \(q=1\) target is \(R^+(C)=o(W)\).  On even ground,
\(|\mathcal U|=N_-\), so upper holes and upper repeats are equal.

This note proves the following.

1. The natural fixed-owner, lower-rainbow switch lattice is
\[
 \mathcal T=\ker_{\mathbb Z}B_0\cap
             \ker_{\mathbb Z}B_-,                   \tag{0.6}
\]
where \(B_0\) records middle endpoints and \(B_-\) records lower
colours.  Its upper action satisfies the exact invariant
\[
 \boxed{P_{m+1}B_+z=0\qquad(z\in\mathcal T),}         \tag{0.7}
\]
where \(P_k\) is point-versus-\(k\)-set incidence.

2. Consequently the point margins of the upper load cannot be changed by
any switch which keeps the owner set and the exact lower rainbow.  On
even ground, if
\[
 r_v=|\{X\in V(C):v\in X\}|,
\]
then every such state obeys
\[
\boxed{
R^+(C)\ge
\max\left\{
 {1\over m+1}\sum_{v=1}^{2m}
       \left|r_v-{N_-\over2}\right|,
 \ \max_v\left|r_v-{N_-\over2}\right|
\right\}.}                                           \tag{0.8}
\]
Hence a saturating cycle with point discrepancy
\(\Omega(mW)\) in the first sum has \(\Omega(W)\) upper repeats in
every fixed-owner lower-rainbow state.  The saturating-cycle theorem gives
no bound on this discrepancy.

3. Every lower- and owner-neutral switch supported on one
four-coordinate \(J(4,2)\) interval is upper-neutral.  Therefore no
sequence of ordinary octahedral rectangle switches can improve the upper
histogram at all.

4. Upper mobility is nevertheless real.  Complementing the rooted
six-coordinate pentagon gives two port-identical path factors with the
same middle-owner ledger and the same exact lower-colour ledger, but upper
difference
\[
 \boxed{
 \Delta_{\rm pent}^+
 =e_{\widehat{25}}+e_{\widehat{36}}+e_{\widehat{14}}
  -e_{\widehat{15}}-e_{\widehat{34}}-e_{\widehat{26}},}        \tag{0.9}
\]
where \(\widehat{ij}=[6]\setminus\{i,j\}\).  Thus the full trade lattice
is not upper-rigid.

5. For an eligible forward pentagon, let \(A\) be the three positive
targets in (0.9) and \(D\) the three negative targets.  Its exact change
in repeat excess is
\[
 \boxed{
 \Delta R^+
 =|\{U\in A:u_C(U)\ge1\}|
  -|\{U\in D:u_C(U)\ge2\}|.}                         \tag{0.10}
\]
This is a literal missing-shadow descent formula, not CPCR.

6. There is a sharp statewise obstruction to the pentagon library.  All
six targets of one pentagon have Johnson diameter at most two.  If
\[
 d_J(\{U:u_C(U)\ge2\},\{U:u_C(U)=0\})\ge3,            \tag{0.11}
\]
then neither orientation of any eligible pentagon strictly decreases
\(R^+\).

Accordingly the one-sided saturating theorem cannot simply be locally
polished into a two-sided cycle.  A positive proof must first choose a
point-balanced saturating cycle, or change its owner set, and must then
supply a positive-density family of non-octahedral eligible trades which
connect repeat targets to holes.  The six-coordinate pentagon is an exact
such direction, but saturation alone does not guarantee that its negative
path factor occurs in the chosen cycle.

## 1. The upper repeat identity

Every edge of \(C\) has one upper colour, so
\[
                         \sum_{U\in\mathcal U}u_C(U)=N_-.       \tag{1.1}
\]
If \(S=\{U:u_C(U)>0\}\), then
\[
 R^+(C)=\sum_U(u_C(U)-1)_+=N_--|S|.                 \tag{1.2}
\]
The number of missing upper targets is
\[
 |\mathcal U|-|S|
 =|\mathcal U|-N_-+R^+(C),                           \tag{1.3}
\]
which proves (0.5).

For \(n=2m\),
\[
 |\mathcal U|=\binom{2m}{m+1}
              =\binom{2m}{m-1}=N_-.                 \tag{1.4}
\]
For \(n=2m+1\),
\[
 |\mathcal U|=\binom{2m+1}{m+1}
              =\binom{2m+1}m=:W,
\qquad
 W-N_-={2W\over m+2}.                                \tag{1.5}
\]
Thus in both cases the coefficient-one question is exactly whether
\(R^+(C)=o(W)\).

## 2. The exact switch space

Let \(\mathscr E\) be the edge set of \(J(n,m)\).  For an edge
\(e=\{X,Y\}\), put
\[
 L(e)=X\cap Y,\qquad U(e)=X\cup Y.                   \tag{2.1}
\]

Define the three incidence maps
\[
\begin{aligned}
 B_0e&=e_X+e_Y,\\
 B_-e&=e_{L(e)},\\
 B_+e&=e_{U(e)}.
\end{aligned}                                                   \tag{2.2}
\]

The edge indicator \(x_C\in\{0,1\}^{\mathscr E}\) satisfies
\[
 B_-x_C=\mathbf1_{\mathcal L},\qquad
 B_0x_C=2\mathbf1_{V(C)}.                             \tag{2.3}
\]

### Definition 2.1 (fixed-owner lower-rainbow trade)

An integral vector \(z\in\mathbb Z^{\mathscr E}\) is a fixed-owner
lower-rainbow trade when
\[
                         B_0z=0,\qquad B_-z=0.        \tag{2.4}
\]
It is legal at \(C\) if \(x_C+z\) is the indicator of a simple connected
two-regular graph on \(V(C)\).

The algebraic conditions (2.4) preserve middle degrees and every lower
colour.  Binary support, simplicity, and connectedness are separate
integral conditions; they are not consequences of membership in the
lattice.

## 3. The point-margin identity

For \(k\ge1\), let \(P_k\) be the point-versus-\(k\)-set incidence
matrix:
\[
                         (P_k)_{v,A}=\mathbf1_{\{v\in A\}}.     \tag{3.1}
\]

### Theorem 3.1 (diamond valuation identity)

On the full Johnson edge module,
\[
 \boxed{
 P_{m-1}B_-+P_{m+1}B_+=P_mB_0.}                     \tag{3.2}
\]

Consequently every trade in (2.4) satisfies (0.7).

#### Proof

Fix \(e=\{X,Y\}\) and a coordinate \(v\).  Since \(X,Y\) differ by one
exchange,
\[
 \mathbf1_{\{v\in X\cap Y\}}
 +\mathbf1_{\{v\in X\cup Y\}}
 =\mathbf1_{\{v\in X\}}+\mathbf1_{\{v\in Y\}}.       \tag{3.3}
\]
This is exactly the \(v,e\) entry of (3.2).  Apply (3.2) to \(z\) and
use (2.4). \(\square\)

For the cycle \(C\), define its owner point counts
\[
                         r_v=(P_m\mathbf1_{V(C)})_v.            \tag{3.4}
\]
Writing \(u=B_+x_C\), (3.2)--(2.3) give
\[
 \boxed{
 P_{m+1}u
 =2r-P_{m-1}\mathbf1_{\mathcal L}.}                 \tag{3.5}
\]
Thus the upper point margins are already fixed by the used owner set and
the exact lower rainbow.

## 4. Quantitative statewise obstruction

We first give a form valid on odd and even ground.  Put
\[
 \mathcal B=
 \left\{b\in\{0,1\}^{\mathcal U}:
                  \sum_{U\in\mathcal U}b(U)=N_-\right\},       \tag{4.1}
\]
and define
\[
 \Delta_{\rm pt}(C)=
 \min_{b\in\mathcal B}
 \left\|
  2r-P_{m-1}\mathbf1_{\mathcal L}-P_{m+1}b
 \right\|_1.                                          \tag{4.2}
\]

### Theorem 4.1 (point-distance lower bound)

Every lower-rainbow cycle on the owner set \(V(C)\) satisfies
\[
 \boxed{
 R^+(C)\ge{\Delta_{\rm pt}(C)\over2(m+1)}.}           \tag{4.3}
\]
The same lower bound holds after every legal trade in (2.4).

#### Proof

Let \(s=\mathbf1_{\{u>0\}}\).  By (1.2),
\[
                         |s|=N_--R^+(C).              \tag{4.4}
\]
Add any \(R^+(C)\) zero coordinates to \(s\), obtaining
\(b\in\mathcal B\).  This is possible because
\[
 |\mathcal U|-|s|
 =|\mathcal U|-N_-+R^+(C)\ge R^+(C).                 \tag{4.5}
\]
Removing the repeated units from \(u\) to reach \(s\) costs
\(R^+(C)\) in \(L^1\), and adding the new unit coordinates costs another
\(R^+(C)\).  Hence
\[
                         \|u-b\|_1=2R^+(C).           \tag{4.6}
\]
Every column of \(P_{m+1}\) has \(m+1\) ones, so
\[
 \|P_{m+1}(u-b)\|_1
 \le(m+1)\|u-b\|_1=2(m+1)R^+(C).                    \tag{4.7}
\]
Use (3.5) and minimize over \(b\).  Invariance under (2.4) follows from
Theorem 3.1. \(\square\)

### Corollary 4.2 (even-ground formula)

For \(n=2m\), equation (0.8) holds.

#### Proof

Here \(|\mathcal U|=N_-\), so the only member of \(\mathcal B\) is
\(\mathbf1_{\mathcal U}\).  For every coordinate \(v\),
\[
\begin{aligned}
 (P_{m-1}\mathbf1)_v&=\binom{2m-1}{m-2},\\
 (P_{m+1}\mathbf1)_v&=\binom{2m-1}{m}.
\end{aligned}                                                   \tag{4.8}
\]
Their sum is \(N_-\).  Thus the vector inside the norm in (4.2) is
\[
                         2\left(r-{N_-\over2}\mathbf1\right).  \tag{4.9}
\]
Substitution in (4.3) gives the first inequality in (0.8).

For one coordinate \(v\),
\[
 2\left|r_v-{N_-\over2}\right|
 =\left|\sum_{U\ni v}(u(U)-1)\right|
 \le\|u-\mathbf1\|_1=2R^+(C),                       \tag{4.10}
\]
because total load equals \(|\mathcal U|\).  This proves the maximum
bound. \(\square\)

The obstruction is statewise.  It does not say that every saturating
cycle is point-unbalanced.  It says that point balance is an additional
necessary selection theorem, and that no reordering of the same owner set
which preserves the lower rainbow can repair its failure.

## 5. Four-coordinate trades are completely upper-neutral

Fix an \((m-2)\)-set \(K\), disjoint from a four-set
\[
                         D=\{1,2,3,4\}.              \tag{5.1}
\]
The local middle owners are \(K\cup Q\), \(Q\in\binom D2\).  A local
Johnson edge is indexed uniquely by an ordered pair \((i,j)\), \(i\ne j\):
its lower colour is
\[
                         K\cup\{i\},                 \tag{5.2}
\]
and its upper colour is
\[
                         K\cup(D\setminus\{j\}).      \tag{5.3}
\]
Let \(z_{ij}\) be its signed coefficient.

### Theorem 5.1 (octahedral upper rigidity)

If the local signed edge vector is owner-neutral and lower-neutral, then
it is upper-neutral:
\[
 B_0z=0,\quad B_-z=0
 \quad\Longrightarrow\quad B_+z=0.                  \tag{5.4}
\]

#### Proof

Lower neutrality gives the four row equations
\[
                         \sum_{j\ne i}z_{ij}=0.       \tag{5.5}
\]
At the middle owner \(K\cup\{a,b\}\), with
\(\{c,d\}=D\setminus\{a,b\}\), owner neutrality is
\[
                         z_{ac}+z_{ad}+z_{bc}+z_{bd}=0.        \tag{5.6}
\]
Using the row equations in (5.6) gives
\[
                         z_{ab}+z_{ba}=0.             \tag{5.7}
\]
Thus the matrix \(z\) is skew-symmetric.  The coefficient of the upper
colour \(K\cup(D\setminus\{j\})\) is the \(j\)-th column sum
\[
                         \sum_{i\ne j}z_{ij}.
\]
By skew-symmetry this is minus the \(j\)-th row sum, hence zero.
\(\square\)

The theorem covers arbitrary integral multiplicities, not merely one
named rectangle.  Therefore every conformal or nonconformal sum of legal
four-coordinate lower-preserving switches has zero upper action.  The
ordinary octahedral trade library cannot change \(R^+\) by even one.

## 6. A six-coordinate lower-neutral trade with nonzero upper action

Let \(D=[6]\), and temporarily suppress a common \((m-3)\)-set \(K\).
Consider the following two five-path factors on the twenty local
three-subsets.

The old paths are
\[
\begin{array}{c|cccc}
1&456&245&235&123\\
2&356&345&234&124\\
3&346&236&126&125\\
4&246&146&136&135\\
5&256&156&145&134.
\end{array}                                                   \tag{6.1}
\]
The new paths are
\[
\begin{array}{c|cccc}
1&456&345&234&123\\
2&356&156&126&124\\
3&346&146&145&125\\
4&246&245&235&135\\
5&256&236&136&134.
\end{array}                                                   \tag{6.2}
\]

These are the coordinate complements of the old and new rooted pentagon
path factors.

### Theorem 6.1 (complemented-pentagon upper trade)

After adjoining \(K\) to every displayed state, replacing (6.1) by
(6.2) has all of the following properties.

1. The five row endpoints agree row by row.
2. The middle-owner degree ledger is unchanged.
3. The lower-colour multiset is exactly
\[
                         \binom D2                         \tag{6.3}
\]
once in each factor.
4. The upper signed difference is (0.9), with every displayed local
four-set adjoined to \(K\).

#### Proof

Both tables enumerate all twenty three-subsets once.  Their ten endpoints
are the same row by row, and their ten internal states are the same set.
Therefore every local middle owner has the same path degree in the two
tables.

Complementing a path exchanges intersections with complements of unions.
Before complementation, both rooted-pentagon factors have adjacent-union
multiset equal to all fifteen four-subsets of \(D\).  Hence after
complementation both lower-intersection multisets are all fifteen
two-subsets, proving Item 3.

For completeness, the original lower-intersection multisets differ only
as follows:
\[
\begin{array}{c|c}
\text{old-only}&15,\ 34,\ 26\\
\text{new-only}&25,\ 36,\ 14.
\end{array}                                                   \tag{6.4}
\]
Complementing these pairs inside \(D\) gives exactly (0.9).
\(\square\)

Thus there is no global upper-rigidity theorem beyond the point margins:
the trade (6.1)--(6.2) belongs to the lattice (0.6) and has nonzero
upper action.  If five vertex-disjoint old paths (6.1), with a common
embedded \(K,D\), occur as ported subpaths of one cycle, then replacing
them by (6.2) preserves the external ports and hence preserves the one
cycle.  Such an occurrence will be called an **eligible pentagon**.

The two-level saturating theorem does not assert that even one eligible
pentagon occurs.

## 7. Exact repeat descent

For one eligible pentagon, define
\[
\begin{aligned}
 A&=\{K\cup\widehat{25},K\cup\widehat{36},
                         K\cup\widehat{14}\},\\
 D&=\{K\cup\widehat{15},K\cup\widehat{34},
                         K\cup\widehat{26}\}.
\end{aligned}                                                   \tag{7.1}
\]
All six targets are distinct.

### Theorem 7.1 (literal pentagon descent formula)

Equation (0.10) holds.

#### Proof

Removing one occurrence from a target of load at least two decreases
\((u-1)_+\) by one; removing the sole occurrence changes it by zero.
Adding one occurrence to an already occupied target increases
\((u-1)_+\) by one; adding the first occurrence changes it by zero.
Apply these four cases to the three negative and three positive entries
of (0.9). \(\square\)

In particular, a forward pentagon decreases repeats by three if all three
members of \(D\) are repeated and all three members of \(A\) are holes.
More generally it is a strict descent precisely when
\[
 |\{U\in D:u(U)\ge2\}|
 >
 |\{U\in A:u(U)\ge1\}|.                              \tag{7.2}
\]

If a family of eligible pentagons has pairwise disjoint middle supports,
ports, and upper target supports, their changes add exactly.  Hence \(k\)
such copies satisfying (7.2) with margin at least one reduce
\(R^+\) by at least \(k\).  Reaching \(o(W)\) repeats from a linear initial
defect therefore requires a linear supply of compatible descending
occurrences, not merely the existence of one local identity.

## 8. A statewise lock for the pentagon library

Let
\[
 \mathcal R=\{U:u_C(U)\ge2\},\qquad
 \mathcal H=\{U:u_C(U)=0\}.                          \tag{8.1}
\]

### Theorem 8.1 (distance-two pentagon lock)

If (0.11) holds, then no eligible complemented-pentagon move, in either
orientation, strictly decreases \(R^+\).

#### Proof

All six upper targets of a pentagon contain the same \((m-3)\)-set \(K\)
and four of the same six active coordinates.  Any two of their local
four-sets intersect in at least two points.  Hence any two targets in one
pentagon intersect in at least \(m-1\) points and have Johnson distance at
most two.

Suppose first that a negative target of the proposed orientation belongs
to \(\mathcal R\).  By (0.11), none of the three positive targets can be
a hole.  Thus all three additions increase repeat excess, while at most
three removals decrease it.  The net change is nonnegative.  If no
negative target is repeated, no removal decreases repeat excess, so again
the change is nonnegative.  The argument is symmetric under reversing the
pentagon. \(\square\)

The lock is a genuine statewise obstruction to this trade library.  It
does not rule out a larger trade whose upper support has diameter at least
three.  It shows exactly why a bounded local identity is not, by itself,
a global absorption theorem: repeat mass and holes may occupy separated
regions of the upper Johnson layer.

## 9. Consequence for constant one

The \(q=1\) lower-saturating cycle closes the lower target layer exactly,
but it supplies none of the two additional inputs now shown to be
necessary.

1. **Point balance.**  On even ground a repair restricted to the same
owner set requires
\[
 \sum_v\left|r_v-{N_-\over2}\right|=o(mW).           \tag{9.1}
\]
On odd ground the corresponding necessary condition is
\[
                         \Delta_{\rm pt}(C)=o(mW).    \tag{9.2}
\]

2. **Nonlocal eligible descent.**  Four-coordinate switches have zero
upper action.  The complemented pentagon has a genuine action, but one
needs enough eligible copies whose negative targets see repeats and whose
positive targets see holes.  The distance-two lock shows that this need
not follow from the scalar equality between holes and repeats.

There are therefore two mathematically distinct positive routes:

* strengthen the saturating-cycle theorem so that the chosen cycle is
point-balanced and contains a dense, well-distributed pentagon or
larger-trade atlas; or
* permit owner-changing trades, for which \(B_0z\ne0\), and use the owner
change to correct the point margins while preserving the lower rainbow.

The complement of an even-ground lower-rainbow cycle has exact upper
rainbow, so the two endpoints of the desired interpolation exist
separately.  What is missing is an integral interpolation which restores
the lower ledger while mixing their owner sets.  The invariant (3.2), the
octahedral no-go, and the pentagon formula (0.10) give the exact tests for
such a construction.
