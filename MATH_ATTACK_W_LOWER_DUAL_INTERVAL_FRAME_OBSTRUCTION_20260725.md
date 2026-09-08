# Lower-dual pair-omission charts: exact seam atoms, collar rigidity, and failure of a full low-boundary frame

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or
long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom n m,
 \qquad T=\binom n{m-1},
\]

and use the pair-omission token convention

\[
 S_i=I_\pi(i,m-1),\qquad Y_i=I_\pi(i-1,m),
\]

\[
 L_q(i)=I_\pi(i+q-1,m-q),\qquad
 U_q(i)=I_\pi(i-1,m+q).
\]

There is an exact local lower-dual atom.  For (q\ge2), let

\[
 b=x_{i+q-2},\qquad a=x_{i+q-1},\qquad \tau=(a\ b).
\]

The original token and its conjugate by \(\tau\) have the same lower and
middle endpoints.  Every upper flag is fixed, every lower flag except the
one at depth (q) is fixed, and

\[
 \boxed{
 L_q(i)\longmapsto L_q(i)-a+b.}
\tag{0.1}
\]

Thus the lower-dual atoms at depth (q) are literal Johnson edges.  In the
coordinate-orbit token system they algebraically span the complete
zero-sum space on \(\binom{[n]}{m-q}\).  Several atoms over distinct lower
endpoints are automatically compatible with exact middle ownership,
because every alternate token is parallel to its original central edge.

This algebraic completeness does **not** give the required physical frame.
The exact row identity

\[
 \boxed{
 L_q(i)=\bigcap_{h=0}^{q-1}S_{i+h}}
\tag{0.2}
\]

forces every endpoint-aligned same-orientation interval chart to be
lower-inert away from a collar of (q-1) starts.  The audited reverse
interval chart has the equally sharp telescoping formula

\[
 z^-_{I,q}=E_{m-q}(I)-E_{m-q}(I+q-1).
\tag{0.3}
\]

In particular, at lower depth two every proper interval atom has

\[
 \boxed{
 z^-_{I,2}
 =\delta_{I_\pi(a,m-2)}-\delta_{I_\pi(b+1,m-2)}}
\tag{0.4}
\]

for (I=[a,b]), up to reversing the displayed sign.  A full cyclic
interval has zero innovation.  Hence one physical interval atom has
depth-two projected rank at most one and coordinate support at most two.

Let (B) be the total number of lower interval atoms in a proposed joint
catalogue.  Same-orientation partner-pair atoms from
`MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md`
have identically zero lower projection.  Consequently, with

\[
 N_2^-=\binom n{m-2},
\]

the common kernel of all catalogue innovations inside the zero-sum lower
depth-two layer has dimension at least

\[
 \boxed{N_2^- -1-B.}
\tag{0.5}
\]

There is also an explicit coordinate-supported kernel of dimension at
least (N_2^- -2B-1).  Since

\[
 \frac{N_2^-}{W}
 =\frac{m(m-1)}{(m+2)(m+3)}=1-o(1),
\tag{0.6}
\]

every **joint binary** catalogue with

\[
 B=o(W/H)
\tag{0.7}
\]

has a nonzero weighted excess mode which is exactly invisible to all its
upper partner-pair and lower-dual interval atoms.  Therefore no positive
linear frame inequality on the full weighted signed-flag space is possible
for that joint binary catalogue.

A multiway threshold on one long reverse path has many possible endpoint
vectors, so its affine span can be much larger than one; the preceding
rank argument must not be applied to it by counting the path as one binary
atom.  Nevertheless every chosen threshold changes the aggregate lower
depth-two load by only one positive and one negative unit.  Thus a product
of (B) multiway paths can repair at most (B) dispersed depth-two holes
in one corner.  Section 5 gives a linear factorial-floor witness which
retains \(\Theta(W)-B\) excess under every such corner.  Hence moving
thresholds evade the rank count but not the one-shot dispersed-excess
capacity obstruction.

This is sharp in scope.  A lower spike of multiplicity (s) can be burned
efficiently: depth-isolated seam atoms with a common old target and
distinct new targets have joined Gram gap (s(s-1)).  What fails is
uniform coverage of dispersed lower excess.  The obstruction does not
exclude a theorem special to the load vectors of one prepared factor, nor
does it exclude genuinely nonlocal necklace circuits which reorder lower
endpoints rather than using endpoint-aligned interval phases.  It does
refute the proposed full-mode frame for the certified partner-pair plus
lower-dual interval atlas.

No constant-one conclusion is claimed.

## 1. Exact seam atom

Let

\[
 \pi=(x_0,\ldots,x_{2m-2})
\]

be an oriented row of a local factor on
(Q_P=[n]\setminus P), with indices read cyclically.  Fix

\[
 2\le q\le m-2
\]

and a start (i).  Put

\[
 b=x_{i+q-2},\qquad a=x_{i+q-1},\qquad \tau=(a\ b).
\tag{1.1}
\]

Both (a) and (b) lie in (S_i), and neither lies in the omitted pair
(P).  Thus \(\tau\) preserves (Q_P), and the conjugate cyclic row
(\tau\pi) is a valid row in the conjugate exact local factor
(\tau F_P).

### Theorem 1.1 (depth-isolated parallel lower atom)

The token at start (i) in \(\pi\) and the token at the corresponding
start in \(\tau\pi\) have exactly the same central endpoints:

\[
 \tau S_i=S_i,\qquad \tau Y_i=Y_i.
\tag{1.2}
\]

Their signed flag difference is zero except at lower depth (q), where

\[
 d^-_q
 =\delta_{L_q(i)-a+b}-\delta_{L_q(i)}.
\tag{1.3}
\]

In particular, replacing any collection of such tokens over distinct
lower endpoints preserves lower saturation and middle simplicity exactly.

#### Proof

The two transposed coordinates belong to (S_i), so \(\tau S_i=S_i).
The middle owner is (Y_i=S_i\cup\{x_{i-1}\}), and
(x_{i-1}\notin\{a,b\}); hence \(\tau Y_i=Y_i\).

Every upper flag contains (S_i), and therefore contains both (a,b).
It is fixed setwise by \(\tau\).  At a lower depth (p<q), the interval
(L_p(i)) contains both (b) and (a).  At (p=q), it contains (a)
but not (b).  At (p>q), it contains neither.  This proves (1.3) and
the vanishing at all other signed depths.

The two token alternatives are parallel edges between the same lower and
middle vertices.  Replacing one by the other changes no central incidence.
The same is true simultaneously at any family of distinct lower vertices.
\(\square\)

The construction is literal in the coordinate-orbit token multigraph.  It
does not remain inside the one fixed local factor (F_P).  Granting the
whole coordinate orbit only strengthens the negative frame conclusion
below.

In fact, simultaneous availability inside the same exact local factor is
impossible.

### Proposition 1.2 (fixed-factor exclusion of the seam mate)

Assume (m\ge3).  If \(\pi\) is a row of an exact local factor (F_P),
then the adjacent-seam conjugate \(\tau\pi\) from (1.1) is not another row
of (F_P).

#### Proof

The row universe has size (2m-1).  A cyclic length-(m) window is
changed as a set by the adjacent transposition \(\tau=(a\ b)) only when
it contains exactly one of (a,b).  There are exactly two such cyclic
windows: the two windows whose boundary separates the adjacent positions.
Every other one of the (2m-1) middle windows contains both transposed
coordinates or neither and is therefore shared by \(\pi\) and
\(\tau\pi\).  Thus the two rows share at least (2m-3>0) middle targets.

They are distinct even as unoriented cyclic rows.  Otherwise the
transposition of the two labels would induce a nonidentity dihedral
automorphism of an odd cycle while fixing the other (2m-3\ge3) labelled
positions.  A nonidentity rotation fixes no position and a reflection of
an odd cycle fixes only one.

Distinct rows of an exact local factor have disjoint middle-window sets,
because those rows partition the local middle layer.  The shared targets
give a contradiction. \(\square\)

Thus Theorem 1.1 is an orbit-token or direct-literal primitive, not a
switch internal to one fixed (F_P).  The reverse-threshold chart of
Section 3 remains the certified lower-active construction using the fixed
transported rows.

A singleton replacement removes one selected position from its old typed
row and inserts one selected position in its conjugate typed row.  It adds
at most two physical selected-run components.  Thus the canonical
depth-isolated implementation has (O(1)) boundary cost per atom.

## 2. Algebraic span and positive spike curvature

Fix (q\ge2), and put (r=m-q).  The vectors in (1.3) are oriented edges
of the Johnson graph (J(n,r)).

### Proposition 2.1 (no algebraic lower invariant beyond total mass)

In the coordinate-orbit token system, every oriented Johnson edge

\[
 \delta_{L-a+b}-\delta_L,
 \qquad a\in L,\quad b\notin L,
\tag{2.1}
\]

is realized by a depth-(q) seam atom.  Consequently these atoms span

\[
 \left\{v\in\mathbb R^{\binom{[n]}r}:
              \sum_Lv_L=0\right\}.
\tag{2.2}
\]

#### Proof

Choose a set (D) of (q-2) coordinates disjoint from
(L\cup\{b\}), and put

\[
 S=L\cup\{b\}\cup D.
\]

Then (|S|=m-1).  Since (S) has fewer than (m) elements, it misses at
least one of the (m) disjoint priority pairs completely; choose such a
pair as the omitted pair (P).

Order (S) in a local row so that the first (q-2) positions are the
elements of (D), the next position is (b), the next is (a), and the
remaining positions are (L\setminus\{a\}).  Complete this to a cyclic
order on (Q_P).  Then its central lower window is (S), its depth-(q)
lower flag is (L), and the seam transposition is ((a\ b)).  Every
cyclic order occurs in a coordinate image of any one fixed local-factor
row, so the coordinate-orbit token system contains this atom.

The Johnson graph is connected: one can transform any (r)-set into any
other by replacing the elements of their set differences one at a time.
The oriented edge vectors of a connected graph span its vertex
augmentation space, proving (2.2). \(\square\)

The same atoms have the correct joined Gram sign on an individual spike.
Suppose (s) old occurrences have the same lower target (L), and choose
seam atoms whose new targets (L_1',\ldots,L_s') are distinct.  With

\[
 d_i=\delta_{L_i'}-\delta_L,
\]

one has

\[
 \|d_i\|_2^2=2,
 \qquad
 \langle d_i,d_j\rangle=1\quad(i\ne j).
\tag{2.3}
\]

Therefore

\[
 \boxed{
 \left\|\sum_{i=1}^sd_i\right\|_2^2
 -\sum_{i=1}^s\|d_i\|_2^2
 =s(s-1).}
\tag{2.4}
\]

Thus the lower-dual mechanism is not sign-defective.  It can obtain
quadratic curvature from a concentrated spike using only (O(s))
singleton boundaries.  The obstruction below comes from dispersed modes,
for which the curvature per activated occurrence is only (O(1)).

## 3. Endpoint-aligned interval charts are collar-local

The following identity is purely physical and does not use a coordinate
permutation.

### Lemma 3.1 (lower flags are consecutive-endpoint intersections)

For every token row and every (q\ge1),

\[
 \boxed{
 L_q(i)=S_i\cap S_{i+1}\cap\cdots\cap S_{i+q-1}.}
\tag{3.1}
\]

#### Proof

The leftmost surviving coordinate in the intersection is
(x_{i+q-1}), and the rightmost is (x_{i+m-2}).  Hence the intersection
is the cyclic interval (I_\pi(i+q-1,m-q)=L_q(i)). \(\square\)

### Theorem 3.2 (same-orientation collar rigidity)

Let (I=[a,b]) be a proper consecutive block.  Suppose two literal row
phases are aligned so that their lower endpoints agree in the same order,

\[
 S_i^0=S_i^1\qquad(i\in I).
\tag{3.2}
\]

Then their lower depth-(q) flags agree at every start

\[
 a\le i\le b-q+1.
\tag{3.3}
\]

Thus switching the whole block can change at most

\[
 \min\{q-1,|I|\}
\tag{3.4}

lower depth-(q) occurrences.  Its innovation has coordinate support at
most (2(q-1)).  In particular a depth-two projection has rank at most
one and support at most two.

#### Proof

For a start satisfying (3.3), all (q) lower endpoints on the right side
of (3.1) belong to (I).  Equation (3.2) makes their intersections equal
in the two phases.  Only the final (q-1) starts of (I) can differ.
Every changed occurrence removes one unit from one target and adds one to
another, proving the support bound. \(\square\)

This theorem includes every pure coordinate-conjugate lower chart for
which the conjugation fixes all central lower endpoints on the switched
interval.  For (q=2), fixing both (S_i) and (S_{i+1}) already fixes

\[
 L_2(i)=S_i\cap S_{i+1};
\]

bulk depth-two action is therefore impossible inside such an interval.

The audited reverse interval chart is not aligned in the same forward
order, but it has the same endpoint-only conclusion by an exact
telescoping calculation.  For a consecutive set (I), put

\[
 E_r(I)=\sum_{i\in I}\delta_{I_\pi(i,r)}.
\]

Its new-minus-old lower innovation is

\[
 z^-_{I,q}=E_{m-q}(I)-E_{m-q}(I+q-1).
\tag{3.5}
\]

The two start intervals have a symmetric difference of size at most
(2(q-1)).  At (q=2), if (I=[a,b]), cancellation gives exactly

\[
 z^-_{I,2}
 =\delta_{I_\pi(a,m-2)}-
   \delta_{I_\pi(b+1,m-2)},
\tag{3.6}
\]

unless (I) is the whole cyclic row, in which case the difference is
zero.  This independently audits the decisive depth-two constant.

## 4. Exact failure of a full joint-binary interval-chart frame

Consider a common-base catalogue consisting of:

1. any number of the same-orientation partner-pair interval atoms audited
   in
   `MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md`;
2. (B) lower-dual interval atoms satisfying Theorem 3.2 or the reverse
   formula (3.5).

The first family has zero lower innovation at every depth.  Let

\[
 p_C\in\mathbb R^{\binom{[n]}{m-2}}
\]

be the lower depth-two projection of lower atom (C).  By Section 3,

\[
 |\operatorname{supp}p_C|\le2,
 \qquad
 \dim\operatorname{span}\{p_C:C\}\le B.
\tag{4.1}
\]

Every (p_C) has coordinate sum zero.  Hence inside the zero-sum layer

\[
 \mathcal H_{2,0}^-
 =\left\{v:\sum_Rv_R=0\right\}
\]

the common orthogonal kernel

\[
 \mathcal K
 =\mathcal H_{2,0}^-
   \cap\operatorname{span}\{p_C:C\}^{\perp}
\]

satisfies

\[
 \boxed{
 \dim\mathcal K\ge N_2^- -1-B.}
\tag{4.2}
\]

There is a more concrete kernel.  Let

\[
 \Omega=\bigcup_C\operatorname{supp}p_C.
\]

Then (|\Omega|\le2B), and every zero-sum vector supported in
(\binom{[n]}{m-2}\setminus\Omega) is killed by all chart projections.
This subspace has dimension at least

\[
 N_2^- -2B-1.
\tag{4.3}
\]

### Corollary 4.1 (no positive full-space frame)

Let (w_2^->0).  For arbitrary nonnegative chart coefficients
(\alpha_C), no inequality of the form

\[
 \sum_C\alpha_C
  |\langle v,z_C\rangle_w|^2
 \ge \eta\|v\|_w^2
 \qquad(v\text{ in the full weighted zero-mass flag space})
\tag{4.4}

can hold with (eta>0) whenever (B<N_2^- -1).

#### Proof

Choose a nonzero (v\in\mathcal K), and embed it in the full signed flag
space by setting every component except lower depth two to zero.  Every
upper partner-pair innovation has zero lower projection, and every lower
atom is orthogonal to (v).  The left side of (4.4) is zero while the
right side is positive. \(\square\)

There is an independent invariant for the stricter proposal in which the
lower-dual charts are required to use the same fixed-partition coordinate
transports as the adjacent upper charts.

### Proposition 4.2 (fixed-partition transport kernel)

Write the priority pairs as

\[
 P_i=\{p_i^0,p_i^1\}\qquad(1\le i\le m)
\]

and let (z) be the unpaired coordinate.  The compatible adjacent
transports are

\[
 \theta_i=(p_i^0\ p_{i+1}^0)(p_i^1\ p_{i+1}^1).
\tag{4.4a}
\]

For (2\le r\le n-2), define on the rank-(r) layer

\[
 h_r(X)=\#\{i:P_i\subseteq X\}
 -\frac{m r(r-1)}{n(n-1)}.
\tag{4.4b}
\]

Then (h_r) is centered and nonzero, and every innovation made from the
transports \(\theta_i\) is orthogonal to it.  This remains true for every
block sum and for every word in the generated transport group.

#### Proof

A uniformly random rank-(r) set contains a specified pair with
probability (r(r-1)/[n(n-1)]), proving centeredness.  In the stated rank
range there are rank-(r) sets containing different numbers of complete
priority pairs, so (h_r\ne0).

Each \(\theta_i\) merely exchanges the two pair blocks (P_i,P_{i+1})
coordinatewise and fixes (z).  Hence

\[
 h_r(\theta_iX)=h_r(X).
\]

It follows that

\[
 \left\langle h_r,
   \delta_{\theta_iX}-\delta_X\right\rangle=0.
\]

Linearity proves the assertion for interval sums, and invariance under
the generators proves it for their group. \(\square\)

This proposition applies only to a lower-dual copy made from the same
double-transposition transports.  The arbitrary seam transposition of
Theorem 1.1 leaves that group and therefore escapes this algebraic kernel,
but Proposition 1.2 shows that it also leaves the one fixed local factor.
The reverse-threshold lower chart is governed instead by the endpoint
capacity theorem below.

Since

\[
 N_2^-=\frac{m(m-1)}{(m+2)(m+3)}W,
\tag{4.5}
\]

condition (B=o(W/H)) leaves a kernel of dimension
((1-o(1))W).  In particular a catalogue which sees every lower
depth-two coordinate mode must have

\[
 2B\ge N_2^- -1,
\tag{4.6}
\]

and therefore (B=\Omega(W)), far above the permitted (o(W/H)) scale.

If the physical catalogue counts endpoints rather than intervals, an
interval has at most two endpoints, and using the endpoint count in place
of (B) only weakens the displayed obstruction by an absolute factor.

## 5. A factorial-floor witness on the abstract load simplex

The kernel is not merely a rank statement.  At lower depth two,

\[
 \frac{T}{N_2^-}
 =\frac{m+3}{m-1}
 =1+\frac4{m-1}.
\tag{5.1}
\]

For (m\ge6), the balanced integral levels are therefore (1) and (2).
Let

\[
 \delta=T-N_2^-=\frac4{m-1}N_2^-.
\tag{5.2}
\]

Writing

\[
 \rho=\frac4{m-1},\qquad \lambda=1+\rho,
\]

the undoubled and doubled lower-depth-two floor excesses are

\[
 \Phi_2^-(x)
 =\frac12\sum_R(x_R-1)(x_R-2)
 =\frac12\left(\|x-\lambda\mathbf1\|_2^2
                 -N_2^-\rho(1-\rho)\right),
 \qquad Q_2^-(x)=2\Phi_2^-(x).
\tag{5.2a}
\]

The centered-square identity uses the fixed mass
\(\sum_Rx_R=T=N_2^-\lambda\); its linear term does not vanish
coordinatewise.

Start with a balanced load having value (2) at exactly \(\delta\)
targets and value (1) elsewhere.  Outside \(\Omega\), choose (R)
disjoint pairs of value-one targets and replace the two loads

\[
 (1,1)\longmapsto(2,0).
\tag{5.3}
\]

This preserves total mass.  For the undoubled factorial floor

\[
 e_1(x)=\frac{(x-1)(x-2)}2,
\]

each pair in (5.3) contributes exactly one unit of excess, all on a target
outside \(\Omega\).  Since every chart innovation is zero there, every
corner of the proposed catalogue retains at least (R) units of this
lower depth-two excess.

When (B=o(W/H)), one may take (R=\Theta(W)), because

\[
 N_2^- -\delta-|\Omega|=\Theta(W).
\]

Thus the full load simplex contains dispersed linear factorial excess
which the complete low-boundary catalogue cannot alter at all.

There is a separate capacity statement which does not assume binary path
variables and does not use one fixed support set \(\Omega\).

### Theorem 5.1 (multiway thresholds still have unit depth-two capacity)

Fix one reference threshold on every one of (B) reverse paths.  On each
path allow an arbitrary legal threshold, not merely two prescribed
thresholds.  Also allow endpoint-aligned same-orientation interval choices,
counting every selected interval component in (B).  If (x) is the
reference lower depth-two load and (y) is the load of any resulting
corner, define

\[
 V_+(y;x)=\sum_R(y_R-x_R)_+.
\]

Then

\[
 \boxed{V_+(y;x)\le B.}
\tag{5.4}
\]

The same conclusion holds after adjoining any number of the upper
partner-pair interval choices, because those have zero lower innovation.
Consequently, if (x) has (R_0) zero coordinates at lower depth two,
then every corner has undoubled factorial floor excess at least

\[
 \boxed{R_0-B.}
\tag{5.5}
\]

#### Proof

Relative to its reference endpoint, a threshold on one reverse path
switches one suffix interval (I=[a,b]).  Equation (3.6) says that its
complete lower depth-two innovation is one vector

\[
 \delta_A-\delta_D.
\]

An endpoint-aligned same-orientation interval changes at most one
depth-two occurrence by Theorem 3.2, and has the same form.  Hence the
positive part of the sum of (B) interval innovations has \(\ell_1\)-mass
at most (B), proving (5.4).

A zero coordinate of (x) ceases to contribute
(e_1(0)=1) only if it receives at least one positive unit.  Inequality
(5.4) permits this at no more than (B) of the (R_0) holes.  Every
other coordinate has nonnegative factorial floor energy, proving (5.5).
\(\square\)

More exactly, take

\[
 R_0=\left\lfloor\frac{N_2^- -\delta}{2}\right\rfloor.
\tag{5.6}
\]

Starting from a balanced load with exactly \(\delta\) twos, apply (5.3)
on (R_0) disjoint pairs of one-coordinates.  The resulting vector has
mass (T), exactly (R_0) zero coordinates, and

\[
 \Phi_2^-(x)=R_0,
 \qquad Q_2^-(x)=2R_0.
\tag{5.7}
\]

Thus every multiway corner satisfies

\[
 \Phi_2^-(y)\ge R_0-B,
 \qquad Q_2^-(y)\ge2(R_0-B).
\tag{5.8}
\]

With a lower-depth-two weight (w_2^->0), both right sides are simply
multiplied by (w_2^-).

Since (R_0=(1/2-o(1))W), a multiway threshold product with
(B=o(W/H)) retains \(\Theta(W)\) abstract lower depth-two excess.  A
multiway path may have
large affine span because its moving positive endpoint ranges over many
targets; it still moves only one unit in any one integral corner.  This is
why it evades Corollary 4.1's dimension proof but not Theorem 5.1's capacity
proof.

This last witness is an abstract integral flag-load vector.  Its
realization by one specified prepared pair-omission matching is not proved.
Accordingly it refutes a universal frame inequality on all weighted excess
modes; it does not refute a factor-specific theorem asserting that the
actual prepared load always lies in the visible subspace.

## 6. Compatibility and the exact remaining scope

The central compatibility statements are as follows.

1. Lower seam alternatives at distinct lower endpoints commute exactly,
   because they are parallel central edges and preserve their middle
   owners.  This produces an exact token matching in the coordinate-orbit
   multigraph; it is not by itself one exact wreath factor or one system of
   the originally fixed local factors.
2. They may be combined with an upper partner-pair corner after reserving
   disjoint lower-target carriers.  If both charts act at the same lower
   target, a joint multiway central choice must be checked separately; it
   is not supplied by the separate cube theorems.
3. A singleton seam atom costs at most two new physical runs.  A genuine
   endpoint-aligned interval bit also costs at most two, but Sections 3--4
   show that its lower-depth-two action is confined to one endpoint mode.
4. Unlimited seam atoms have full algebraic span.  The obstruction is
   exactly the incompatibility between depth isolation and the
   (o(W/H)) physical-boundary budget.
5. Allowing all thresholds on one fixed reverse path removes the binary
   rank obstruction, but every chosen threshold still has only one unit of
   positive lower-depth-two capacity.  It cannot repair a dispersed linear
   defect in one product corner.

Therefore the proposed completion of the same-orientation partner-pair
atlas by lower-dual interval charts cannot prove the desired charged frame
on every weighted excess mode.  A surviving positive theorem must use at
least one input not present here:

* a structural theorem forcing the actual prepared lower depth-two excess
  into (o(W/H)) collar coordinates;
* a genuinely nonlocal necklace circuit which changes the internal
  adjacency/intersection pattern of a long block while retaining exact
  middle ownership; or
* an exact duality reducing the lower modes to already charged upper modes
  inside the same selected token system.

A repeatedly renewed moving-seam menu is also not excluded: after changing
the factor, recomputed paths could have different endpoint strips.  Such a
renewal theorem would have to prove that the final boundary count remains
subcritical; it is not part of the fixed interval atlas.

None of these three statements is proved here.  In particular, the
Johnson-edge span by itself is not a quantitative frame theorem, and the
pair-omission interval floor descent remains an upper-sector theorem.

## 7. Independent audit of the decisive step

The decisive assertion is (3.6).  It can be checked without any geometric
interpretation.  For (I=[a,b]),

\[
 \begin{aligned}
 E_{m-2}(I)-E_{m-2}(I+1)
 &=\sum_{i=a}^b\delta_{I_\pi(i,m-2)}
   -\sum_{i=a+1}^{b+1}\delta_{I_\pi(i,m-2)}\\
 &=\delta_{I_\pi(a,m-2)}
   -\delta_{I_\pi(b+1,m-2)}.
 \end{aligned}
\]

All interior terms cancel with coefficient zero.  Proper cyclic windows
of length (m-2<2m-1) at distinct starts are distinct, so the two
surviving coordinates are different unless the interval is the full
cycle.  Therefore each interval contributes one zero-sum vector of rank
one and support two.  Summing (B) such vectors gives projected rank at
most (B), exactly as used in (4.2).  No probabilistic, asymptotic, or
factor-completion assumption enters this calculation.
