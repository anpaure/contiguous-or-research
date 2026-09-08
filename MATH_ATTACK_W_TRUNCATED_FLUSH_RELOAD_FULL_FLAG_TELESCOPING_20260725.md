# Full hard-flag trace of the truncated flush/reload compiler

Date: 2026-07-25

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2Q,\qquad a_0=m-Q.
\]

For one adjacent row transposition \(\tau=(u\ v)\), the full incidence
difference of a flush/reload route is now explicit at every hard prefix
rank \(a_0+h\), \(0\le h\le n\).  It is the sum of two trails:

* a source-flush trail
  \[
  \mathbf 1_{r<h\le n}d_\tau(K_h)-d_\tau(J_h),
  \]
* and a target-reload trail
  \[
  \mathbf 1_{h\le r}d_\tau(L_h),
  \]

where

\[
 d_\tau(C):=e_{C+v}-e_{C+u}.
\]

The bases \(K_h,J_h,L_h\) are given exactly in Theorem 2.1 below.  This
determines, without a variance estimate or projection, the complete
designated-state hard-flag change under one cube bit.

The proposed adjacent-port telescoping is **false**.  If

\[
 E_{i,j+1}=E_{ij},\qquad r_{i,j+1}=r_{ij}+2,
\]

then the routes

\[
 A_j\longrightarrow B_j,
 \qquad
 C_j\longrightarrow A_{j+1}
\]

have opposite row orientations, but equivariantly shifted buffers do not
make their traces equal.  There are two independent obstructions.

1. The two-route segment has nonzero singleton margin \(e_v-e_u\) at
   each of the three ranks
   \[
   h=r,\quad r+1,\quad r+2,
   \]
   and zero singleton margin elsewhere.  Hence it cannot reduce to the
   point-neutral marked sum \(\rho_{ij}+\rho_{i,j+1}\).
2. At the set level, the next column label \(a'\) belongs to every base
   of the second route and to no base of the first route.  It is a forced
   tail choice and is unavailable as a buffer.  Thus neither the high
   source trails nor the low reload trails can cancel for any buffer
   choices.  The uncancelled part persists through \(\Theta(Q)\) hard
   ranks, although most of it is point-neutral.

Complementary reloads do have a clean positive description: they form an
entire ladder of elementary octahedral rectangles, one at every
\(0\le h\le r\).  The marked rectangle is only the last rung; it is not
the whole physical difference.

Exact cross-carrier cancellation is a rigid signature-matching problem.
A first high-rank connector already determines its row pair and its two
base trails.  Its active scaffold has size

\[
 m+Q+1.
\]

There are many carriers containing that scaffold, but inactive-tail
extensions only clone the same signature.  The obvious negative copy,
obtained by reversing the row orientation, also negates the marked
rectangle.  No marked-preserving negative-signature matching follows from
carrier abundance.

There is a different exact two-route **funnel identity**.  Cross-associate
two collar orders with two core/tail block types so that the two route
types coalesce after their first update.  Then every connector state
cancels statewise and only the two initial states remain.  At rank
\(a_0+h\) their difference is the four-corner trade

\[
 \Omega_h=
 e_{A+P_h(z)}+e_{A-a+b+P_h(z^*)}
 -e_{A+P_h(z^*)}-e_{A-a+b+P_h(z)}.
\]

One adjacent collar swap gives exactly the desired rank-isolated marked
rectangle.  Reversing the two collar halves separately gives exact total
square distance

\[
 2\left\lfloor\frac{Q^2}{4}\right\rfloor
\]

and total pair-shadow norm

\[
 8\left\lfloor\frac{Q^2}{4}\right\rfloor
\]

at literal route cost \(O(Q)\), while the middle load is unchanged.

This funnel is not yet an exact-factor gadget.  In one physical
configuration its two routes already have the same middle owner after the
first update (for the static lower-half row swaps), and later actually
coalesce.  Thus it has a genuine common-owner collision.  The proved
object is an integral positive two-word incidence circuit, not a
one-owner-per-middle-set switch.  Exact-factor installation still needs a
rotating tag or a cross-carrier owner separation which preserves the
statewise connector cancellation.

## 1. Notation and endpoint convention

Fix one carrier \(U\), \(|U|=M=m+H\).  A radius-\(Q\) quotient state is

\[
 \omega=(A;z_1,\ldots,z_n;B),
 \qquad |A|=a_0,quad |B|=H-Q.
\]

Its hard prefix at index \(h\) is

\[
 F_h(\omega)=A+z_1+\cdots+z_h,
 \qquad 0\le h\le n.
\tag{1.1}
\]

The middle owner is \(F_Q\).  For an ordered collar
\(z=(z_1,\ldots,z_n)\), write

\[
 P_h(z)=\{z_1,\ldots,z_h\}.
\tag{1.2}
\]

Suppose an active adjacent row pair occupies collar positions \(r,r+1\):

\[
 z_r=u,\qquad z_{r+1}=v.
\]

For every base \(C\) avoiding \(u,v\), put

\[
 d_\tau(C)=e_{C+v}-e_{C+u}.
\tag{1.3}
\]

Then

\[
 \partial_1d_\tau(C)=e_v-e_u,
\tag{1.4}
\]

independently of \(C\).

Route incidences below are **half-open**: the source state is excluded and
every state reached by an update is included.  This convention makes
concatenated routes additive without double-counting their common marked
state.  Initial and final path endpoints are added separately in
Theorem 3.1.

## 2. Exact trace of one flush/reload route

Consider the route

\[
 R:\quad
 (A;z_1,\ldots,z_n;B)
 \longrightarrow
 (A-a+b;w_1,\ldots,w_n;B-b+a),
\tag{2.1}
\]

where \(a\in A\), \(b\in B\).  Choose distinct buffers

\[
 x_1,\ldots,x_n,a\in A.
\]

The first \(n+1\) core choices are

\[
 x_1,\ldots,x_n,a,
\]

and the tail choices are

\[
 b,z_n,z_{n-1},\ldots,z_1.
\]

The last \(n\) core choices are

\[
 w_n,w_{n-1},\ldots,w_1,
\]

and the tail choices are \(x_1,\ldots,x_n\).

Put

\[
 s_*=n-r+1.
\]

### Theorem 2.1 (full half-open transposition trace)

For \(h=r+s\), \(1\le s\le n-r\), define

\[
 K_h^R=
 A+\{b,z_1,\ldots,z_{r-1},z_{n-s+2},\ldots,z_n\}.
\tag{2.2}
\]

For every \(0\le h\le n\), define

\[
\begin{aligned}
 J_h^R={}&
 \left(A-\{x_1,\ldots,x_{s_*}\}\right)
 +\{b,z_{r+2},\ldots,z_n\}\\
 &+\operatorname{pref}_h
 (x_{s_*},\ldots,x_1,z_1,\ldots,z_{r-1}).
\end{aligned}
\tag{2.3}
\]

For \(0\le h\le r\), define

\[
 L_h^R=
 \left(A-\{a,x_{n-r+h+1},\ldots,x_n\}\right)
 +\{b,w_1,\ldots,w_{r-1}\}.
\tag{2.4}
\]

Let \(\varepsilon=+1\) if the untoggled source has order \(u,v\), and
\(\varepsilon=-1\) if it has order \(v,u\).  The source-collar part of
the route difference is exactly

\[
 \boxed{
 S^R_{\varepsilon,r,h}
 =\varepsilon\left(
 \mathbf1_{r<h\le n}d_\tau(K_h^R)-d_\tau(J_h^R)
 \right).}
\tag{2.5}
\]

If the target collar is toggled in positions \(r,r+1\) with sign
\(\eta\), its reload contribution is exactly

\[
 \boxed{
 T^R_{\eta,r,h}
 =\eta\mathbf1_{h\le r}d_\tau(L_h^R).}
\tag{2.6}
\]

When both endpoints are toggled, (2.5) and (2.6) add.  At \(h=n\),

\[
 K_n^R=J_n^R,
\]

so the source trail cancels exactly at the top hard rank.

#### Proof

After \(s\le n\) flush updates the collar is

\[
 (x_s,x_{s-1},\ldots,x_1,z_1,\ldots,z_{n-s}).
\tag{2.7}
\]

Before either active label drops, the transposition boundary moves from
prefix \(r\) to prefix \(r+s\).  The buffer deletions from the core cancel
the buffer labels in that prefix, leaving exactly (2.2).  Hence this moving
boundary contributes the first term of (2.5).

At update \(s_*\), one active label has entered the core and the other has
entered the tail.  Every prefix distinguishes the two routes with the
opposite orientation.  Reading the core and collar at this state gives
(2.3), hence the second term of (2.5).  One update later both active labels
are in the core and the source order is forgotten.  At \(h=n\), the moving
boundary and split-state bases coincide.

During reload, the label destined for target position \(r+1\) is removed
from the core first.  The transposition boundary then moves successively
through prefix indices \(0,1,\ldots,r\).  At its visit to \(h\), direct
substitution of the returned buffers and the fixed target prefix gives
(2.4).  No target-order difference remains above \(r\).  This proves
(2.6). \(\square\)

The formula is integral and concerns actual route states.  It is not a
formal difference of unavailable states.

## 3. Complete path difference under one static-cube bit

Fix an interior port \(0<j<t-1\), a row index \(i\), and toggle
\(E_{ij}:0\to1\).  Put

\[
 r=Q-q_{ij}.
\]

Let

* \(I\) be the incoming route \(C_{j-1}\to A_j\);
* \(M\) be the route \(A_j\to B_j\);
* \(O\) be the outgoing route \(C_j\to A_{j+1}\).

The two cyclic states after \(B_j\) have transposition-edge bases
\(D_1,D_2\).  The sign at \(A_j\) is positive, while the signs at
\(B_j,C_j\) are negative.

### Theorem 3.1 (one-bit full hard-flag difference)

For the unpadded compiled path, at rank \(a_0+h\) the complete difference
is

\[
\boxed{
\begin{aligned}
 \Delta_h={}&
 \mathbf1_{h\le r}d_\tau(L_h^I)
 -d_\tau(J_h^M)
 +\mathbf1_{r<h\le n}d_\tau(K_h^M)
 -\mathbf1_{h\le r}d_\tau(L_h^M)\\
 &-\mathbf1_{h=r+1}d_\tau(D_1)
 -\mathbf1_{h=r+2}d_\tau(D_2)
 +d_\tau(J_h^O)
 -\mathbf1_{r+2<h\le n}d_\tau(K_h^O).
\end{aligned}}
\tag{3.1}
\]

For \(j=0\), replace the incoming term by the initial-state term

\[
 \mathbf1_{h=r}
 d_\tau(A_0+z_1+\cdots+z_{r-1}).
\tag{3.2}
\]

For \(j=t-1\), omit the two cyclic terms and the outgoing route.  Any
optional padding after the final marked state has its own transposition
trace and is not included in (3.1).

#### Proof

Apply (2.6) to the incoming target with sign \(+1\).  Apply (2.5) and
(2.6) to \(A_j\to B_j\) with source sign \(+1\) and target sign \(-1\).
The two common cyclic updates shift the negatively oriented row pair by
one collar position each, giving the two displayed single-edge terms.
Finally apply (2.5) to the negatively oriented source \(C_j\), whose
boundary is \(r+2\).  The half-open convention accounts for every path
state once. \(\square\)

Equation (3.1) is the requested full hard-flag answer.  The designated
identity

\[
 J(E+e_{ij})-J(E)=\rho_{ij}
\]

is only the endpoint subprojection of (3.1).

## 4. Complementary reloads are a rectangle ladder

At port \(j\), let the crossing column pair be

\[
 a\in A,\qquad b\in B.
\]

Use the same buffers on the incoming route and on \(A_j\to B_j\).  For
\(0\le h\le r\), put

\[
 G_h=
 \left(A-\{a,x_{n-r+h+1},\ldots,x_n\}\right)
 +\{z_1,\ldots,z_{r-1}\}.
\tag{4.1}
\]

Then the two reload bases are

\[
 L_h^I=G_h+a,
 \qquad
 L_h^M=G_h+b.
\tag{4.2}
\]

Consequently

\[
\boxed{
 d_\tau(L_h^I)-d_\tau(L_h^M)
 =d_\tau(G_h+a)-d_\tau(G_h+b)}
\tag{4.3}
\]

is one elementary octahedral rectangle with axes \(\{u,v\}\) and
\(\{a,b\}\), at every rank \(0\le h\le r\).  The member at \(h=r\)
is \(\rho_{ij}\).

Thus the exact positive statement is a **rankwise rectangle ladder**.  It
is not a telescope to one marked rectangle.

## 5. The adjacent-port telescoping hypothesis

Now impose

\[
 E_{i,j+1}=E_{ij}.
\]

Write

\[
 r=r_{ij},\qquad r_{i,j+1}=r+2.
\]

Let \((a,b)\) be the current column pair and \((a',b')\) the next one.
The two cyclic updates in the \(\beta\)-frame choose core labels
\(c_1,c_2\) and tail labels \(a,b'\).  If the core before the first route
is \(A\), then the core of \(C_j\) is

\[
 A(C_j)=A-\{c_1,c_2\}+\{b,b'\}.
\tag{5.1}
\]

The outgoing route exchanges \(b'\) for \(a'\).

Choose the first two buffers of the first route as

\[
 x_1=c_1,\qquad x_2=c_2,
\]

and shift the early buffers of the second route by

\[
 y_\ell=x_{\ell+2},
 \qquad 1\le\ell\le n-r-1.
\tag{5.2}
\]

This is the most favorable equivariant shifted-buffer coupling.

Put

\[
 P=\{z_1,\ldots,z_{r-1}\},
 \qquad
 O=\{z_{n-1},z_n\},
 \qquad
 N=\{a',b'\}.
\tag{5.3}
\]

The exact boundary bases are

\[
 D_1=K_{r+1}^{1}=A+b+P,
\tag{5.4}
\]

\[
 K_{r+2}^{1}=A+b+P+z_n,
 \qquad
 D_2=A+b+b'+P.
\tag{5.5}
\]

For \(h=r+2+\ell\), \(1\le\ell\le n-r-2\), there is a common base

\[
 G_h=A+b+P+\{z_{n-\ell},\ldots,z_{n-2}\}
\tag{5.6}
\]

such that

\[
 K_h^1=G_h+O,
 \qquad
 K_h^2=G_h+N.
\tag{5.7}
\]

The special split bases have the analogous form

\[
 J_h^1=R+O+\operatorname{pref}_h(\mathcal X_1),
 \qquad
 J_h^2=R+N+\operatorname{pref}_h(\mathcal X_2),
\tag{5.8}
\]

where \(\mathcal X_2\) is the two-step shift of \(\mathcal X_1\).  At a
rank which splits another row pair, the prefix difference in (5.8) is one
additional row-by-row octahedral rectangle; it is not zero.

Equations (5.4)--(5.8) give exact cancellation at \(h=r+1\), because
\(K_{r+1}^1=D_1\).  At \(h=r+2\), the remaining moving-edge term is

\[
 d_\tau(A+b+P+z_n)-d_\tau(A+b+P+b').
\tag{5.9}
\]

For every \(r+3\le h<n\), it is

\[
 \left[d_\tau(G_h+O)-d_\tau(G_h+N)\right]
 -d_\tau(J_h^1)+d_\tau(J_h^2).
\tag{5.10}
\]

### Theorem 5.1 (exact failure of shifted-buffer telescoping)

No choice of legal buffers makes the two route traces cancel on their
common high or low rank intervals.

#### Proof

The next inside label \(a'\) is the forced first tail choice of the second
route.  Hence it belongs to every second-route source and reload base.  It
belongs to no first-route base or cyclic base.  Since \(a'\) begins in the
second route's tail, it is unavailable as a buffer and this membership
difference cannot be altered by (5.2) or by any other legal buffer choice.
Thus no first-route transposition edge equals an oppositely signed
second-route edge.

At low ranks the obstruction is visible directly:

\[
 L_h^1=A-a-X_h+b+P,
 \qquad 0\le h\le r,
\tag{5.11}
\]

whereas

\[
 L_h^2=A+b+a'-Y_h+P,
 \qquad 0\le h\le r+2.
\tag{5.12}
\]

Every set in (5.12) contains \(a'\), and no set in (5.11) does.  The
same forced-membership separation appears in (5.7)--(5.8).  Therefore
exact set cancellation is impossible. \(\square\)

There is also a buffer-independent one-line audit.  Let

\[
 \sigma=e_v-e_u.
\]

For a complete complementary route with cut \(r\), the singleton-margin
coefficient is \(-2\sigma\) below \(r\), \(-\sigma\) at \(r\), and zero
above \(r\).  The opposite route with cut \(r+2\) contributes the reverse
profile.  Counting the single intermediate cyclic states once gives

\[
\boxed{
 \partial_1\Delta_{a_0+h}
 =\begin{cases}
 \sigma,&h\in\{r,r+1,r+2\},\\
 0,&\text{otherwise}.
 \end{cases}}
\tag{5.13}
\]

The desired marked sum is

\[
 \rho_{ij}+\rho_{i,j+1},
\]

which has zero singleton margin at each rank.  Equation (5.13) therefore
rules out the proposed identity before any higher shadow is considered.

The marked terms themselves remain exactly

\[
 \rho_{ij}
 =d_\tau(A+P)-d_\tau(A-a+b+P)
 \quad\text{at }h=r,
\tag{5.14}
\]

and

\[
 \rho_{i,j+1}
 =d_\tau(A+b+a'+P)-d_\tau(A+b+b'+P)
 \quad\text{at }h=r+2.
\tag{5.15}
\]

Thus the failure is connector-only, but it is not confined to \(O(1)\)
ranks at the set-incidence level.

## 6. Exact cross-carrier support conditions

At the first high rank \(h=r+1\), a source connector has the form

\[
 C_{r+1}=d_\tau(K_{r+1})-d_\tau(J_{r+1}).
\tag{6.1}
\]

For the static parameters,

\[
 |K_{r+1}\setminus J_{r+1}|=2Q-r-1\ge Q.
\tag{6.2}
\]

Hence the only Johnson-neighbor pairs among its four support masks are the
two \(\tau\)-edges.  The signed vector (6.1) therefore determines

* the unordered row pair \(\{u,v\}\);
* the two bases \(K_{r+1},J_{r+1}\);
* their signed pairing.

The union of its support is

\[
 D=A+\{z_1,\ldots,z_n\}+\{b\},
 \qquad |D|=m+Q+1.
\tag{6.3}
\]

### Proposition 6.1 (carrier containment and exact supply)

If a carrier \(U'\) supports an exact opposite copy of (6.1), then

\[
 D\subseteq U',
 \qquad
 |U\cap U'|\ge m+Q+1.
\tag{6.4}
\]

For a fixed scaffold \(D\), the number of size-\(M\) carrier extensions
inside \([2m]\) is exactly

\[
 \boxed{
 \binom{m-Q-1}{H-Q-1}.}
\tag{6.5}
\]

#### Proof

Exact equality of a nonzero transposition edge recovers its two endpoints,
hence their intersection base and symmetric-difference pair.  Equation
(6.2) prevents an alternative pairing of the four masks.  Thus an opposite
copy must contain the full union (6.3).  There are
\(2m-|D|=m-Q-1\) unused global labels, and a carrier extension chooses
\(M-|D|=H-Q-1\) of them. \(\square\)

For the adjacent pair of ports, the union of the two active scaffolds has
size at most

\[
 m+Q+4.
\tag{6.6}
\]

Thus raw carrier support remains abundant whenever \(H-Q\to\infty\).
This is not the pairing theorem: silent-tail extensions reproduce a given
signature, rather than its negative.

For any two bases \(K,J\) of the same size,

\[
 \Gamma_2\bigl(d_\tau(K)-d_\tau(J)\bigr)
 =(e_v-e_u)\otimes(\mathbf1_K-\mathbf1_J),
\tag{6.7}
\]

and therefore

\[
 \boxed{
 \left\|\Gamma_2\bigl(d_\tau(K)-d_\tau(J)\bigr)\right\|_1
 =4|K\setminus J|.}
\tag{6.8}
\]

So even a residue on only two hard ranks can retain \(\Theta(Q)\) pair
discrepancy unless its complete star profile is matched.

An exact pairwise cross-carrier absorber must match the full ordered
signature

\[
 \Sigma(R)=\bigl(h,\tau,K_h,J_h,L_h\bigr)_{0\le h\le n}
\tag{6.9}
\]

to its negative, not merely find another carrier containing \(D\).  If
carriers have capacities \(\kappa(U')\), the necessary and sufficient
bipartite assignment condition is the Hall family

\[
 \boxed{
 |\mathcal A|
 \le
 \sum_{U'\in N(\mathcal A)}\kappa(U')
 \quad\text{for every gadget subfamily }\mathcal A,}
\tag{6.10}
\]

where \(N(\mathcal A)\) contains only carriers carrying exact negative
signatures and satisfying the required owner-disjointness constraints.

Reversing \(\tau\) supplies an exact negative signature, but also negates
every marked rectangle with row axis \(\tau\).  A marked-preserving partner
would need to reverse a connector-only base axis while fixing the marked
column axes.  No such partner is supplied by the flush/reload family.

Therefore cross-carrier **containment** is plentiful; cross-carrier
**negative signatures with surviving marked drift** remain unproved.

## 7. A connector-free two-route funnel

The failure above belongs to the chronological route
\(A_j\to B_j\).  There is a different exact coupling.

Let

\[
 A^*=A-a+b,
 \qquad
 B^*=B-b+a,
\tag{7.1}
\]

where \(a\in A\), \(b\in B\).  Choose

\[
 d\in A-\{a\},
\]

and distinct buffers

\[
 x_1,\ldots,x_n\in A-\{a,d\}.
\]

Thus it is enough that

\[
 |A|\ge n+2.
\tag{7.2}
\]

For any collar order \(z\), define two route types.

* Type \(0\) starts at \((A;z;B)\), uses distinguished core label \(d\),
  and first tail label \(b\).
* Type \(1\) starts at \((A^*;z;B^*)\), uses the same \(d\), and first
  tail label \(a\).

After the first update both are exactly the state

\[
 \left(
 A-x_1+b;
 x_1,z_1,\ldots,z_{n-1};
 B-b+z_n
 \right).
\tag{7.3}
\]

Use identical legal choices thereafter, and a fixed target collar
independent of the source order.

### Theorem 7.1 (statewise connector cancellation)

Let \(z,z^*\) be any two orders of the same collar-label set.  Compare the
two positive route systems

\[
 \mathcal R_0
 =R_0(z)\sqcup R_1(z^*),
 \qquad
 \mathcal R_1
 =R_0(z^*)\sqcup R_1(z).
\tag{7.4}
\]

Their route-state multisets agree after their two initial states.  Hence,
at every hard prefix rank,

\[
\boxed{
 I_{a_0+h}(\mathcal R_0)-I_{a_0+h}(\mathcal R_1)
 =\Omega_h,}
\tag{7.5}
\]

where

\[
\boxed{
 \Omega_h=
 e_{A+P_h(z)}+e_{A^*+P_h(z^*)}
 -e_{A+P_h(z^*)}-e_{A^*+P_h(z)}.}
\tag{7.6}
\]

#### Proof

Equation (7.3) says that, for a fixed source order, the two route types
coincide after one update.  Thus the post-initial trajectory associated
with \(z\) occurs once in each system in (7.4), and the same is true for
\(z^*\).  All connector states cancel state by state.  The four uncancelled
initial states give (7.6). \(\square\)

If \(z,z^*\) differ by one adjacent swap \((u\ v)\) across prefix cut
\(r\), then \(\Omega_h=0\) for \(h\ne r\), while

\[
 \Omega_r=
 e_{C+a+u}+e_{C+b+v}
 -e_{C+a+v}-e_{C+b+u}
\tag{7.7}
\]

for a common core \(C\).  This is exactly the desired elementary marked
rectangle.  Products of disjoint adjacent swaps give the corresponding
support-disjoint static row rectangles at their distinct cuts.

More generally, put

\[
 d_h=|P_h(z)-P_h(z^*)|/2
 =|P_h(z)\setminus P_h(z^*)|.
\tag{7.8}
\]

Then

\[
 \boxed{\|\Gamma_2\Omega_h\|_1=4d_h,}
\tag{7.9}
\]

and the exact unit-octahedron distance of \(\Omega_h\) is \(d_h\).

Indeed, a Johnson geodesic between the two prefix sets telescopes
\(\Omega_h\) into \(d_h\) elementary rectangles.  Conversely (7.9) and
the fact that one octahedron has pair-shadow norm four give the matching
lower bound.

Take \(z^*\) to reverse positions \(1,\ldots,Q\) internally and positions
\(Q+1,\ldots,2Q\) internally.  Then

\[
 P_Q(z)=P_Q(z^*),
\]

so the middle difference is exactly zero, and

\[
 d_h=
 \begin{cases}
 \min(h,Q-h),&0\le h\le Q,\\
 \min(h-Q,2Q-h),&Q\le h\le2Q.
 \end{cases}
\tag{7.10}
\]

Therefore

\[
 \boxed{
 \sum_{h=0}^{2Q}d_h
 =2\left\lfloor\frac{Q^2}{4}\right\rfloor,}
\tag{7.11}
\]

and

\[
 \boxed{
 \sum_{h=0}^{2Q}\|\Gamma_2\Omega_h\|_1
 =8\left\lfloor\frac{Q^2}{4}\right\rfloor.}
\tag{7.12}
\]

Each route has \(2n+1\) updates and \(2n+2\) states.  A standalone
literal word for one route has length

\[
 (2n+2)+(n+1)=3n+3=6Q+3.
\]

Thus one two-route system has the exact upper bound

\[
 \boxed{12Q+6}
\tag{7.13}
\]

on literal word length.  If its two source states are already installed,
the two routes add \(4n+2=8Q+2\) new state occurrences.

The initialization positions in the standalone words expose additional,
uncredited OR witnesses.  Equations (7.5)--(7.12) concern the complete
quotient route-state incidences, not those transient initialization
prefixes.

### Proposition 7.2 (exact-factor obstruction for the funnel)

For the static row swaps, which lie strictly inside the lower half of the
collar, the two routes in either system (7.4) have the same middle owner
already after their first update.  Later their quotient trajectories
coalesce.  Hence the funnel is not a one-owner-per-middle-set exact-factor
switch.

#### Proof

After the first update the unordered cores of the two routes agree by
(7.3).  Their collars differ only by permutations of pairs wholly inside
the first \(Q\) positions, so their first-\(Q\) collar sets agree.  Their
middle owners are therefore equal.  Once the permuted source collar has
flushed, (7.3) and the common continuation make the quotient states
identical. \(\square\)

Using distinct final distinguished labels can separate a final endpoint,
but it does not repair the first-update owner collision.  A valid exact
factor would need a tag which keeps the route owners distinct while being
invisible to every hard-flag connector cancellation.  No such rotating tag
is constructed here.

### Proposition 7.3 (sharp two-route tag dichotomy)

There is a canonical attempted repair, and it proves that two routes are
not enough.  Choose a spare

\[
 c\in B-\{b\}.
\]

Keep type \(0\) as above, but let type \(1\) use first tail label \(c\)
instead of \(a\).  If neither \(a\) nor \(c\) is later chosen, then after
the first update the two route types are exact \((a\ c)\)-twins, and this
relation persists throughout their coupled continuations.  Their owners
are therefore distinct: one contains \(a\) and the other contains \(c\).

Under the association swap \(z\leftrightarrow z^*\), every connector
difference now has the form

\[
 e_{S(z)}+e_{(ac)S(z^*)}
 -e_{S(z^*)}-e_{(ac)S(z)}.
\tag{7.14}
\]

Thus every connector term is point-neutral and lies in the octahedral
rectangle lattice with tag axis \(\{a,c\}\).  For one adjacent row swap,
each nonzero term in (7.14) is itself an elementary rectangle.

However, because the active cut satisfies \(r<Q\), the complete middle
difference is nonzero.  In the trace notation it is

\[
 (I-(ac))\bigl(d_\tau(K_Q)-d_\tau(J_Q)\bigr),
\tag{7.15}
\]

and \(K_Q\ne J_Q\).  Hence the tagged coupling is owner-disjoint but does
not preserve the middle-owner multiset.

Consequently the two-route same-schedule family has an exact dichotomy:

* choosing \(c=a\) cancels all connectors, but forces a duplicate middle
  owner after the first update;
* choosing \(c\ne a\) separates the owners, but leaves the nonzero tagged
  middle train (7.15).

No two-route member of this family simultaneously retains the desired
source rectangle, has owner-disjoint positive support, and preserves the
middle histogram.  A three-tag circulation or a genuinely multi-route
coupling is necessary.

## 8. Proved and unproved boundary

### Proved

1. Equations (2.5)--(2.6) give the exact full hard-flag trace of one
   flush/reload route.
2. Equation (3.1) gives the complete unpadded path difference under one
   static-cube bit.
3. Complementary reloads form a rectangle at every lower hard rank, not
   only at the marked rank.
4. The adjacent-port condition \(E_{i,j+1}=E_{ij}\) does not telescope the
   actual compiler.  The three-rank singleton residue (5.13) and the
   forced \(a'\)-membership obstruction are exact.
5. Carriers containing a connector scaffold are abundant, with exact
   count (6.5), but exact negative-signature supply is a strictly stronger
   requirement.
6. The two-route funnel cancels every route connector statewise and leaves
   precisely the initial four-corner trades.
7. Half-reversal gives an integral middle-neutral circuit of total square
   distance \(2\lfloor Q^2/4\rfloor\) at \(O(Q)\) literal cost.

### Not proved

1. No cross-carrier matching of the actual adjacent-port connector
   signatures is proved which preserves \(\rho_{ij}+\rho_{i,j+1}\).
2. No owner-simple exact-factor embedding of the funnel is proved; the
   naive embedding is ruled out by Proposition 7.2.
   Proposition 7.3 further rules out the obvious one-spare-tag repair.
3. Repeating one \(O(Q)\)-cost funnel at each of \(\Theta(M/Q)\) ports
   has a linear constant-factor toll.  No shared-path coefficient-one
   compilation of all funnels is proved.
4. Initialization-transient flags are not included in the signed route
   identity.  They are harmless extra witnesses for a literal cover but
   would need a separate coupling in a full occurrence-load kernel.

The current compiler's specific telescoping hypothesis is therefore
closed negatively.  The exact surviving route is the funnel identity plus
an owner-separating, entry-neutral tag theorem; that theorem is the new
integral gate.
