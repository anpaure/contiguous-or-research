# Clipped residence across a monotone Johnson connector is exactly two interval matchings

**Date:** 2026-08-06  
**Method:** literal run/gap accounting and interval-bigraph Hall; no
computation or search  
**Status:** unconditional connector theorem.  It converts every endpoint
residence flag into a release time and deadline on the deletion or insertion
order of one monotone Johnson geodesic.  This isolates the exact tail-splice
port condition.  It does not prove that an arbitrary pair of clipped paths
satisfies that condition.

## 1. Endpoint signatures

Let

\[
 P=(\ldots,P_{-1},P_0),\qquad P_0=A,
\tag{1.1}
\]

and

\[
 Q=(Q_0,Q_1,\ldots),\qquad Q_0=B,
\tag{1.2}
\]

be simple rank-`r` Johnson paths.  They need not have the same length.  Fix
a residence deadline `d`.

For every coordinate `z`, let

\[
p_A(z)=\max\{h\ge1:
  {\bf1}_{\{z\in P_{-h+1}\}}=\cdots={\bf1}_{\{z\in P_0\}}\},
\tag{1.3}
\]

truncated at `d+1`, and define `p_B(z)` analogously from the initial owners
`Q_0,...,Q_(h-1)`.  Thus `p_A(z)` and `p_B(z)` record the lengths, including
the endpoint owner, of the current positive run or zero gap on the two
sides.

Assume every run and gap wholly internal to `P` or `Q` already has length
at least `d+1`.  Only the endpoint signatures (1.3) remain to be joined.

Let

\[
 D=A\setminus B,\qquad I=B\setminus A,
 \qquad |D|=|I|=:q.
\tag{1.4}
\]

A monotone Johnson connector is obtained by ordering

\[
 D=(x_1,\ldots,x_q),\qquad I=(y_1,\ldots,y_q)
\tag{1.5}
\]

and swapping `x_j` for `y_j` at transition `j`.

For every changed coordinate `z in D union I`, define

\[
 L_z=\max\{1,d+2-p_A(z)\},
 \qquad
 U_z=\min\{q,q+p_B(z)-d-1\}.
\tag{1.6}
\]

The interval may be empty.

## 2. Exact connector theorem

### Theorem 2.1 (two interval matchings)

Suppose `q>=d`.  The monotone connector may be ordered so that every
positive run and every zero gap meeting either seam has length at least
`d+1` if and only if each of the two interval bigraphs

\[
 \mathcal G_D=(D,[q];\ z\sim j\Longleftrightarrow L_z\le j\le U_z)
\tag{2.1}
\]

and

\[
 \mathcal G_I=(I,[q];\ z\sim j\Longleftrightarrow L_z\le j\le U_z)
\tag{2.2}
\]

has a perfect matching.

Equivalently, for `X=D` and separately for `X=I`,

\[
 \boxed{
 \#\{z\in X:[L_z,U_z]\subseteq[a,b]\}\le b-a+1
 \quad(1\le a\le b\le q).}
\tag{2.3}
\]

#### Proof

Write the connector owners as

\[
                         A=A_0,A_1,\ldots,A_q=B.
\]

First let `z=x_j in D`.  Its positive run ending at transition `j`
contains at least the `p_A(z)` old owners counted in (1.3) and the `j-1` later
connector owners `A_1,...,A_(j-1)`.  Its length is therefore

\[
                         p_A(z)+j-1
\tag{2.4}
\]

for purposes of comparison with `d+1` (the actual length can be larger
when the signature was truncated).

After deletion, its zero gap contains `A_j,...,A_(q-1)` and the initial
zero segment of `Q`, of relevant length at least

\[
                         q-j+p_B(z).
\tag{2.5}
\]

Both quantities are at least `d+1` exactly when

\[
                         L_z\le j\le U_z.
\tag{2.6}
\]

Now let `z=y_j in I`.  Before insertion its zero gap has length
`p_A(z)+j-1`, and after insertion its positive run has length
`q-j+p_B(z)`.  The identical condition (2.6) results.

Coordinates in `A cap B` keep value one across all `q+1` connector owners,
and coordinates outside `A union B` keep value zero.  Since `q>=d`, their
joined run or gap automatically has length at least `d+1`.  Every other
run or gap is internal to `P` or `Q` and is safe by hypothesis.  Thus a
legal deletion order is exactly a perfect matching of (2.1), and a legal
insertion order is exactly a perfect matching of (2.2).  The two orders are
independent and are paired position by position, so both matchings are
necessary and sufficient.

Finally, a family of intervals on a line has a system of distinct
representatives exactly when no interval `[a,b]` contains more member
intervals than its number of integer positions.  This is the standard
interval form of Hall's theorem and gives (2.3). \(\square\)

The theorem prices positive and zero residence simultaneously.  Checking
only the positive suffixes is not sufficient: the same changed coordinate
also has the opposite-polarity deadline at the other endpoint.

## 3. Useful sufficient forms

### Corollary 3.1 (fully seasoned endpoints)

If

\[
                         p_A(z),p_B(z)\ge d+1
 \qquad(z\in D\cup I),
\tag{3.1}
\]

then every deletion and insertion order is residence-safe.

#### Proof

Equation (1.6) gives `[L_z,U_z]=[1,q]` for every changed coordinate.
\(\square\)

### Corollary 3.2 (nested signature criterion)

Suppose the intervals `( [L_z,U_z] )_(z in D)` are nested, and the same is
true on `I`.  Then the connector exists if and only if, after ordering the
intervals on either shore from smallest to largest,

\[
                         |[L_j,U_j]|\ge j
 \qquad(1\le j\le q).
\tag{3.2}
\]

#### Proof

For a nested interval family, every inclusion-minimal Hall obstruction is
one member interval.  The first `j` intervals in the inclusion order lie in
the `j`-th interval, so (3.2) is necessary; it is also precisely (2.3).
\(\square\)

### Corollary 3.3 (ordered endpoint queues)

Assume that on each of `D` and `I` the endpoint histories can be labelled
so that

\[
 p_A(z_1)\ge\cdots\ge p_A(z_q),
 \qquad
 p_B(z_1)\le\cdots\le p_B(z_q),
\tag{3.3}
\]

and that

\[
 d+2-p_A(z_j)\le j\le q+p_B(z_j)-d-1
 \qquad(1\le j\le q).
\tag{3.4}
\]

Then assigning `z_j` to transition `j` is legal.  If (3.3)--(3.4) hold
separately for deletions and insertions, the resulting connector is
residence-safe.

#### Proof

Equation (3.4) is exactly `j in [L_(z_j),U_(z_j)]`.  Use these two explicit
perfect matchings in Theorem 2.1. \(\square\)

This is the abstract form of the ordered marker/background bridge: short
left histories are deleted late, while short right histories are installed
early.

### Theorem 3.4 (sparse clipped flags make long connectors automatic)

Fix one shore `X`, either `D` or `I`, and put

\[
 a_X=|\{z\in X:p_A(z)\le d\}|,
 \qquad
 b_X=|\{z\in X:p_B(z)\le d\}|.
\tag{3.5}
\]

Its interval bigraph has a perfect matching whenever

\[
 q\ge
 \max\{d+a_X,\ d+b_X,\ 2d+\min(a_X,b_X)\}.
\tag{3.6}
\]

Consequently, if on each of the deletion and insertion shores at most `d`
coordinates have a short history at either endpoint, then

\[
                         q\ge3d
\tag{3.7}
\]

is sufficient for a residence-safe connector.  No ordering of the endpoint
flags has to be prescribed in advance.

#### Proof

Use the interval Hall form (2.3).  A coordinate with a seasoned left
history has `L_z=1`, and one with a seasoned right history has `U_z=q`.
Every interval satisfies

\[
                         L_z\le d+1,
 \qquad                  U_z\ge q-d.
\tag{3.8}
\]

Consider a possible Hall container `[u,v]`.

* If `u=1` and `v=q`, it contains all `q` intervals and Hall is equality.
* If `u>1` and `v=q`, only the `a_X` left-short intervals can be contained.
  If one is contained then `u<=d+1`, so the container has at least `q-d`
  positions.  The first inequality in (3.6) is therefore sufficient.
* If `u=1` and `v<q`, the symmetric argument counts at most `b_X`
  intervals and uses the second inequality in (3.6).
* If `u>1` and `v<q`, every contained interval is short at both endpoints,
  so there are at most `min(a_X,b_X)` of them.  By (3.8), any one such
  interval, and hence its container, has length at least `q-2d`.  The third
  inequality in (3.6) proves Hall.

These are all containers.  Apply the argument separately to `D` and `I`,
then Theorem 2.1.  If all four short-history counts are at most `d`, each
term on the right side of (3.6) is at most `3d`, proving (3.7). \(\square\)

### Corollary 3.5 (automatic long-context interface)

Suppose the supplied left context contains at least `d` transitions before
its port, and the supplied right context contains at least `d` transitions
after its port.  At either port there are at most `d` short positive
histories and at most `d` short zero histories on the corresponding side.
Hence any monotone connector of distance at least `3d` between two such
ports is residence-safe.  No one-pass or coordinate-distinctness assumption
on the two contexts is needed.

#### Proof

A short terminal positive history has its most recent zero-to-one change in
the last `d` transitions, and a short terminal zero history has its most
recent one-to-zero change there.  Distinct short histories have distinct
most recent change transitions, so there are at most `d` of each.  The
initial statement is the same with time reversed.  Invoke Theorem 3.4.
\(\square\)

### Theorem 3.6 (explicit three-zone order and free middle aperture)

Under the hypotheses of Corollary 3.5 and `q>=3d`, each shore has a legal
order in which every coordinate short at either endpoint is assigned inside
the three-zone set

\[
 [1,d]\ \cup\ [d+1,2d]\ \cup\ [q-d+1,q].
\tag{3.9}
\]

All coordinates seasoned at both endpoints may be ordered arbitrarily on
the remaining positions.  In particular, after the endpoint constraints
are fixed, at least `q-3d` deletion labels and `q-3d` insertion labels retain
independent permutation aperture.

#### Proof

On one shore put

\[
 A=\{z:p_A(z)\le d\},
 \qquad B=\{z:p_B(z)\le d\}.
\tag{3.10}
\]

Assign `B setminus A` injectively to `[1,d]`, assign `A cap B` injectively
to `[d+1,2d]`, and assign `A setminus B` injectively to `[q-d+1,q]`.
All three sets have size at most `d`.  A member of `B setminus A` has
interval `[1,U_z]` with `U_z>=q-d>=d`; a member of `A setminus B` has
interval `[L_z,q]` with `L_z<=d+1<=q-d+1`; and a member of `A cap B` has

\[
 [d+1,2d]\subseteq[L_z,U_z]
\tag{3.11}
\]

because `L_z<=d+1`, `U_z>=q-d`, and `q>=3d`.  The three position zones are
disjoint.  Every remaining coordinate has interval `[1,q]`, so an arbitrary
bijection to the unused positions completes the order.  Apply this
independently to deletions and insertions. \(\square\)

## 4. Tail-splice consequence

For the antipodal construction, a proposed tail splice no longer needs a
new ad hoc residence proof.  It must supply endpoint owners `A,B` at
Johnson distance `q>=d` and verify the finite interval inequalities (2.3)
for the clipped signatures of its two retained witness paths.  Once these
hold, the connector is literal, monotone, and simultaneously positive- and
zero-resident.

In particular, Theorem 3.4 reduces the common sparse-interface case to the
single distance inequality `q>=3d`.  The remaining tail construction must
still produce such one-pass endpoint halos and make their owner and both
immediate-palette resources private; those conclusions are not consequences
of interval Hall alone.

This reduction is exact but not vacuous.  A port frozen without regard to
the opposite endpoint can give several singleton intervals `[L_z,U_z]`
at the same transition and fail (2.3).  Thus large Johnson distance alone
does not close the tail-splice residence gate; the two ports and their
endpoint histories must be selected jointly.
