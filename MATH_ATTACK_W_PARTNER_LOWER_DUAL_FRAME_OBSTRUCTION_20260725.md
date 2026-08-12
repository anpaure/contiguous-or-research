# Partner-pair plus endpoint-dual charts: an exact depth-two frame obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web search
is used.

## 0. Outcome and scope

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 N_2^-=\binom{n}{m-2}.
\]

The positive adjacent-priority partner-pair chart has no lower-flag
innovation at any depth.  The natural endpoint-aligned lower companion has
an equally rigid, but opposite, defect: at lower depth two, one arbitrarily
long physical interval changes only its two endpoint targets.

Consequently, suppose a jointly compatible catalog consists of

* any number of the audited same-orientation partner-pair intervals; and
* \(B\) endpoint-shift lower-dual intervals of the audited
  predecessor/successor form (2.2).  Equivalently for the argument, each
  atom may be any endpoint-aligned interval whose depth-two displacement is
  one target substitution.  If a convention exposes both seams and hence
  two substitutions per atom, every occurrence of \(2B\) below may be
  replaced by \(4B\); the rank and asymptotic conclusions are unchanged.

Then the complete lower-depth-two innovation space has dimension at most
\(B\) and is supported on at most \(2B\) rank-\((m-2)\) targets.  In
particular, if

\[
 B=o(W/H),
\tag{0.1}
\]

then it has an \((N_2^--1-B)\)-dimensional kernel inside the zero-mass
target space.  Since

\[
 \boxed{
 N_2^-
 =\frac{m(m-1)}{(m+2)(m+3)}W
 =(1-O(m^{-1}))W,}
\tag{0.2}
\]

this kernel has dimension \((1-o(1))W\) throughout every Gaussian window.
Thus no positive frame inequality on **all** weighted target modes can hold
for partner-pair charts plus endpoint-aligned lower duals under the required
\(o(W/H)\) boundary catalog.

This conclusion grants, rather than assumes, simultaneous compatibility of
all catalog atoms.  The existing adjacent-priority theorem actually proves
only a menu of separate cubes, so the obstruction remains valid under a
strictly stronger hypothesis than is presently available.

The scope is exact.  This note does not construct a literal exact factor
whose load is one of the obstructing ambient modes.  It therefore refutes
an unrestricted target-space frame theorem, not a factor-restricted theorem
augmented by a new proof that every physically realizable load has negligible
projection on the kernel.  It also does not exclude a genuinely nonlocal
lower chart which transports a different ordered lower-endpoint chain
through the interior of a long block.  Such a chart would not be
endpoint-aligned and is precisely the required escape from the theorem.

## 1. The lower flag is determined by consecutive lower endpoints

In a physical cyclic row

\[
 \pi=(x_i)_{i\in\mathbb Z_{2m-1}},
\]

write

\[
 S_i=I_\pi(i,m-1),\qquad
 L_q(i)=I_\pi(i+q-1,m-q).
\tag{1.1}
\]

### Lemma 1.1 (intersection identity)

For every \(1\le q\le m-1\),

\[
 \boxed{L_q(i)=\bigcap_{h=0}^{q-1}S_{i+h}.}
\tag{1.2}
\]

#### Proof

The position intervals defining \(S_i,S_{i+1},\ldots,S_{i+q-1}\) are

\[
 [i,i+m-2],\ [i+1,i+m-1],\ldots,
 [i+q-1,i+m+q-3].
\]

Their common position interval is

\[
 [i+q-1,i+m-2],
\]

of length \(m-q\), which is exactly the interval defining \(L_q(i)\).
The row has distinct coordinate labels, so equality of position intervals
gives equality of the corresponding sets. \(\square\)

It follows immediately that if two phases have the same ordered lower
endpoints throughout an interval \(I\), their lower depth-\(q\) flags agree
at every start whose whole \(q\)-tuple of consecutive lower endpoints lies
inside \(I\).  Only the \(q-1\) starts at each relevant seam can change.

## 2. Exact depth-two endpoint formula

For a cyclic index set \(I\) and a window length \(r\), put

\[
 E_{\pi,r}(I)=\sum_{i\in I}\delta_{I_\pi(i,r)}.
\tag{2.1}
\]

The audited predecessor/successor interval atom has lower displacement

\[
 z^-_{I,q}
 =E_{\pi,m-q}(I)-E_{\pi,m-q}(I+q-1).
\tag{2.2}
\]

More generally, (1.2) shows that an endpoint-aligned two-phase interval has
only endpoint-strip lower action: after cancelling identical interior
\(q\)-tuples, only seam-crossing tuples remain.  The exact one-substitution
formula below is asserted for the audited predecessor/successor shift.  A
two-seam convention has at most two substitutions and therefore at most
four target cells of support.

At depth two, let \(I=[a,b]\) be a proper cyclic interval, cut linearly at
a point outside \(I\).  Equation (2.2) telescopes exactly:

\[
 \boxed{
 z^-_{I,2}
 =\delta_{I_\pi(a,m-2)}-
   \delta_{I_\pi(b+1,m-2)}.}
\tag{2.3}
\]

If \(I\) is the full cyclic row, both multisets in (2.2) are identical and
\(z^-_{I,2}=0\).

Thus one interval, regardless of its physical length, contributes one
oriented edge between two rank-\((m-2)\) target cells.  In particular

\[
 \|z^-_{I,2}\|_2^2\le2.
\tag{2.4}
\]

The same-orientation partner-pair interval contributes nothing at lower
depth two: its two tokens over a changed lower target \(S\) are related by
a coordinate transport fixing \(S\) pointwise, and every lower flag is a
subset of \(S\).  In the notation of the audited interval theorem,

\[
 (d_S)_q^-=0\qquad(1\le q\le H).
\tag{2.5}
\]

## 3. The endpoint graph and its exact kernel

Let \(\mathscr I\) be the endpoint-shift lower-dual interval catalog and
\(B=|\mathscr I|\).  Form a multigraph \(\Gamma_2\) whose vertices are the
rank-\((m-2)\) targets and whose edge belonging to \(I=[a,b]\) joins the
two cells in (2.3).  Loops represent zero innovations and may be discarded.

Let

\[
 \mathcal Z_2^-=
 \operatorname{span}\{z^-_{I,2}:I\in\mathscr I\}
 \subseteq\mathbb R^{\binom{[n]}{m-2}}.
\tag{3.1}
\]

### Theorem 3.1 (depth-two catalog obstruction)

For every such catalog,

\[
 \boxed{
 \dim\mathcal Z_2^-\le B,
 \qquad
 |\operatorname{supp}\mathcal Z_2^-|\le2B.}
\tag{3.2}
\]

More precisely, \(\mathcal Z_2^-\) is contained in the incidence space of
\(\Gamma_2\), so its rank is at most

\[
 |V(\Gamma_2)|-c(\Gamma_2)\le B,
\tag{3.3}
\]

where \(c(\Gamma_2)\) counts the nonempty connected components.
Consequently, in the zero-mass space

\[
 \mathcal H_{2,0}^-=
 \left\{v:\sum_Xv(X)=0\right\},
\tag{3.4}
\]

one has

\[
 \boxed{
 \dim\bigl(\mathcal H_{2,0}^-\cap
                 (\mathcal Z_2^-)^\perp\bigr)
 \ge N_2^--1-B.}
\tag{3.5}
\]

All partner-pair intervals may be added to the catalog without changing
any assertion.

#### Proof

Formula (2.3) is exactly the signed incidence column of one edge of
\(\Gamma_2\).  An incidence matrix with \(B\) columns has rank at most
\(B\), and its nonzero rows are among the at most two endpoints per column.
The sharper graph rank in (3.3) is standard and follows directly by
choosing a spanning forest in every component: every remaining edge column
is a signed sum of forest-edge columns around its fundamental cycle.

Every edge column has coordinate sum zero, so
\(\mathcal Z_2^-\subseteq\mathcal H_{2,0}^-\).  Subtracting its rank from
\(\dim\mathcal H_{2,0}^-=N_2^--1\) gives (3.5).  Equation (2.5) shows that
partner-pair columns add no lower-depth vector. \(\square\)

If \(B=o(W/H)\), then \(B=o(W)\), and (0.2) turns (3.5) into

\[
 \dim\bigl(\mathcal H_{2,0}^-\cap
                 (\mathcal Z_2^-)^\perp\bigr)
 =(1-o(1))W.
\tag{3.6}
\]

In particular, because at most \(2B<N_2^--1\) cells occur in the endpoint
graph for all sufficiently large \(m\), choose two untouched targets
\(X,Y\).  Then

\[
 v=\delta_X-\delta_Y
\tag{3.7}
\]

is an explicit nonzero zero-mass mode orthogonal to every compatible chart
innovation.  This is an exact kernel vector, not an asymptotic estimate.

### Corollary 3.2 (no all-mode frame)

There is no \(\gamma_m>0\) for which a frame inequality of the form

\[
 \sum_{I\in\mathscr I}a_I
       |\langle v,z^-_{I,2}\rangle|^2
 \ge\gamma_m\|v\|_2^2
\tag{3.8}
\]

holds for every \(v\in\mathcal H_{2,0}^-\), for arbitrary nonnegative
finite coefficients \(a_I\).  The same is true after adjoining every
partner-pair chart and after stacking arbitrary positive weights at all
other signed depths.

#### Proof

Use the vector (3.7).  Every term on the left is zero, while the right side
is \(2\gamma_m>0\).  Stacking other depths cannot help a vector supported
only in the lower-depth-two summand. \(\square\)

## 4. A mass-correct integral ambient load obstruction

The preceding failure is linear.  There is also an integral load profile
of the correct rankwise mass whose floor energy remains linear outside the
entire endpoint support.

At lower depth two,

\[
 D_m:=W-N_2^-
 =\frac{6(m+1)}{(m+2)(m+3)}W
 =O(W/m).
\tag{4.1}
\]

Let \(E=V(\Gamma_2)\), so \(|E|\le2B=o(W)\).  For all sufficiently large
\(m\), choose disjoint subsets

\[
 Z,Y,A\subseteq\binom{[n]}{m-2}\setminus E,
\qquad |Z|=|Y|=R,\qquad |A|=D_m,
\tag{4.2}
\]

where

\[
 R=\left\lfloor\frac{N_2^--|E|-D_m}{2}\right\rfloor
 =\Theta(W).
\tag{4.3}
\]

Start with load one on every target, put load zero on \(Z\), load two on
\(Y\), and raise the load from one to two on \(A\).  Call the resulting
integer vector \(x\).  Then

\[
 \sum_Xx(X)=N_2^- -R+R+D_m=W.
\tag{4.4}
\]

Since \(W/N_2^-=1+O(1/m)<2\), the adjacent-integer floor is \(c=1\), and
the unhalved floor polynomial is

\[
 Q_2^-(x)=\sum_X(x(X)-1)(x(X)-2).
\tag{4.5}
\]

The loads one and two cost zero, while a zero costs two.  Therefore

\[
 \boxed{Q_2^-(x)=2R=\Theta(W).}
\tag{4.6}
\]

Every catalog corner has exactly the same load as \(x\) on
\(\binom{[n]}{m-2}\setminus E\).  Hence its contribution from the cells
in \(Z\) alone remains \(2R=\Theta(W)\).  No charged coverage inequality
on all integral mass-\(W\) target profiles can bound this energy by the
curvature of the stated catalog.

The quantifier here is important: (4.2)--(4.6) define a legitimate integral
rankwise load vector, but no claim is made that it is the lower-depth-two
histogram of a literal exact wreath factor.  To retain a frame theorem only
on physically realizable histograms, one must prove the new structural
assertion

\[
 Q_2^-(F;\binom{[n]}{m-2}\setminus E)=o(W)
\tag{4.7}
\]

for every high-energy endpoint and its adaptively constructed endpoint
catalog.  Neither exact middle ownership nor the audited interval theorem
implies (4.7).

The same construction applies verbatim before the final middle completion,
when the lower-saturating token core has mass

\[
 T=\binom{n}{m-1}=\frac{m}{m+2}W.
\]

Indeed,

\[
 T-N_2^-=
 \frac{4m}{(m+2)(m+3)}W=O(W/m),
\]

and \(\lfloor T/N_2^-\rfloor=1\) for all sufficiently large \(m\).
Replacing \(D_m\) in (4.1)--(4.4) by this difference gives the same
\(\Theta(W)\) untouched floor excess.  Thus the ambient obstruction is
independent of whether the proposed frame is stated for the token core or
for the completed mass-\(W\) factor.

## 5. A second, representation-theoretic kernel for one priority partition

There is an independent obstruction if all transports use one fixed
priority partition

\[
 [n]=P_1\sqcup\cdots\sqcup P_m\sqcup\{z\}.
\tag{5.1}
\]

After labelling the two coordinates in \(P_1\), labels can be propagated
along the priority path so every adjacent transport is label-preserving.
The generated coordinate group is then the diagonal copy of \(S_m\) which
permutes the pair indices and fixes \(z\).  In particular it is not
transitive on any nontrivial subset layer.

For a rank \(r\), define

\[
 h_r(X)=
 \#\{i:P_i\subseteq X\}
 -m\frac{r(r-1)}{n(n-1)}.
\tag{5.2}
\]

The second term is the uniform-layer mean of the first.  Thus
\(\sum_{|X|=r}h_r(X)=0\); and for \(2\le r\le n-2\), the function is
nonzero because rank-\(r\) sets can contain different numbers of complete
priority pairs.  Every adjacent transport \(\theta\) preserves \(h_r\), so

\[
 \left\langle h_r,
        \delta_{\theta X}-\delta_X\right\rangle=0.
\tag{5.3}
\]

This annihilates all block sums of the partner-pair innovations.  Any lower
dual built from the same coordinate transports has the same group kernel.
Therefore even an unrestricted number of fixed-partition transport charts
cannot be a full target-space frame.  Re-pairing the coordinates, in
particular moving the distinguished singleton through another near-perfect
matching, is algebraically necessary unless the fixed-group projection is
proved harmless on every physical endpoint.

This group obstruction is weaker in scope than Theorem 3.1: it can be
removed by adding transports from sufficiently different pairings, whereas
the depth-two endpoint-support obstruction applies to every pairing as long
as the lower atoms remain endpoint-aligned and their total number is
\(o(W/H)\).

## 6. A cumulative partner catalog needs Omega(W) intervals

The preceding fixed-partition kernel can be removed algebraically by using
partner pairs from a coordinate-spanning star.  It still cannot be removed
inside an \(o(W/H)\) **cumulative** interval catalog.

Consider first the star with one fixed omitted pair \(A\).  Every partner
chart compares \(A\) with a two-set \(B\subseteq[n]\setminus A\).  In each
of the \(R_m=\operatorname{Cat}_{m-1}\) rows of \(F_A\), there is at least
one nonempty interval of rank-\((m-1)\) starts avoiding \(B\): deleting the
two positions of \(B\) leaves two cyclic arcs of total length \(2m-3\), so
one arc has length at least \(m-1\).  Therefore every nontrivial star chart
has at least

\[
 R_m
\tag{6.1}
\]

physical interval atoms.

A family of \(s\) common-\(A\) partner transports moves, besides the two
coordinates of \(A\), at most \(2s\) other coordinates.  If \(s<m\), then

\[
 2+2s<2m+1=n,
\]

so some coordinate \(z\) is fixed by every transport.  The centered
first-upper membership mode

\[
 h_{z,m+1}(U)={\bf1}_{\{z\in U\}}-\frac{m+1}{n}
\tag{6.2}
\]

is then killed by every partner signal on the rank-\((m+1)\) upper layer.
Every depth-isolated lower seam atom fixes all upper flags, while the
audited predecessor/successor interval atom has \(z^+_{I,1}=0\).  Thus
adjoining either certified lower-dual catalog does not see (6.2).  Hence a
full signed-layer frame
requires at least \(m\) partner charts and therefore at least

\[
 \boxed{
 mR_m\quad\text{interval atoms},
 \qquad
 \frac{mR_m}{W}
 =\frac{m(m+1)}{2(2m-1)(2m+1)}
 \longrightarrow\frac18.}
\tag{6.3}
\]

In particular its cumulative catalog is \(\Omega(W)\), not \(o(W/H)\).

The kernel is not confined to the degree-one membership statistic.  If
\(2d\) untouched coordinates
\(z_1,\ldots,z_{2d}\) remain, then on any subset layer on which it is
nonzero the function

\[
 h_d(U)=\prod_{j=1}^d
 \left({\bf1}_{\{z_{2j-1}\in U\}}-
       {\bf1}_{\{z_{2j}\in U\}}\right)
\tag{6.3a}
\]

is fixed by every partner transport, has multilinear degree \(d\), and has
zero layer sum: swapping
\(z_1,z_2\) pairs its positive and negative values.  Thus a sublinear
number of partner charts leaves invariant modes of every fixed multilinear
degree, not only a first-moment mode which might vanish for structural
reasons on a particular factor class.

Even if the omitted pair \(A\) is allowed to vary with the chart, one
double-transposition transport moves at most four coordinates.  Fewer than
\(\lceil n/4\rceil\) charts leave some coordinate fixed, and the identical
mode (6.2) survives.  Since every first-position pair exchange again has at
least \(R_m\) nonempty row intervals, every coordinate-spanning cumulative
partner catalog has at least

\[
 \left\lceil\frac n4\right\rceil R_m=\Omega(W)
\tag{6.4}
\]

intervals.

Equations (6.3)--(6.4) refute the joint or cumulative-catalog reading of
the desired frame without using the depth-two rank argument.  They do not
refute a renewable menu which pays for only one \(O(R_m)\)-interval chart
at each endpoint and reconstructs a full algebraic menu after every move.
Such common-base endpoint renewal is a separate, presently unproved
theorem.

## 7. Exact implication boundary

The following is proved.

1. Partner-pair adjacent-priority intervals give no lower innovation.
2. Every endpoint-aligned lower interval gives one depth-two incidence edge,
   independent of its length.
3. A catalog of \(B=o(W/H)\) such intervals leaves a
   \((1-o(1))W\)-dimensional lower-depth-two kernel.
4. Consequently the desired all-weighted-mode frame inequality is false
   for the currently certified partner-plus-endpoint-dual architecture.
5. For a fixed priority pairing there is an additional exact group-invariant
   kernel even without the boundary restriction.

The following is not proved.

1. No literal exact factor with \(\Theta(W)\) energy in the kernel is
   constructed here.  The factor-restricted charged inequality remains
   logically possible, but only after a new theorem bounds the invariant
   projection of every realizable load.
2. A lower chart which transports a genuinely different ordered chain of
   lower endpoints through the interior of a long block is not ruled out.
   Such a chart must preserve exact middle ownership and literal
   realizability while changing \(\Omega(W)\) depth-two occurrences using
   only \(o(W/H)\) physical seams.
3. Separate adjacent-priority cubes are not known to be simultaneously
   compatible.  Proving joint compatibility would not repair the
   depth-two kernel, but it remains necessary for any positive atlas.

Thus the next viable constant-one lemma cannot merely add more
endpoint-aligned partner and dual intervals.  It must prove either a
factor-specific kernel bound such as (4.7), or a non-endpoint-aligned exact
lower transport with macroscopic interior action per subcritical boundary
catalog.

## 8. Fixed-factor impossibility of a pure parallel lower atom

The coordinate-orbit lower seam construction has a further exact scope
restriction.  It cannot be realized by two different rows of one fixed
exact local factor.

### Proposition 8.1 (unique-owner obstruction)

Let \(F_P\) be one exact local factor on
\(Q_P=[n]\setminus P\).  Suppose two pointed tokens of \(F_P\) have the
same rank-\(m\) middle owner \(Y\).  Then they are the same pointed
occurrence and have identical flags at every depth.  Consequently there is
no nonzero token innovation inside \(F_P\) which preserves both its lower
root and its middle owner.

#### Proof

Exactness says that the length-\(m\) cyclic intervals of the rows of
\(F_P\) partition \(\binom{Q_P}{m}\).  Hence \(Y\) has exactly one
pointed row occurrence.  Two tokens with owner \(Y\) must use that same
occurrence.  Their physical row, start, lower root, and every nested flag
are therefore identical. \(\square\)

In particular, the depth-isolated seam atom obtained by conjugating a row
with the transposition of two coordinates inside its lower root has the
same central owner and a different lower flag, so its alternate row lies in
the conjugate factor \(\tau F_P\), not in \(F_P\).  The algebraically
complete Johnson-edge dictionary therefore intrinsically requires typed
coordinate-orbit copies or a change of endpoint factor.  It is not an
available chart inside the same fixed local factors used by the audited
adjacent-priority construction.
