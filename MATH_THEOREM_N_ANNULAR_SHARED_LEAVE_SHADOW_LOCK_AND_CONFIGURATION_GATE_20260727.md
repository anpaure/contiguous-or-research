# Annular shared-leave repeat excess: balanced flag flow, a point-regular shadow lock, and the exact configuration gate

Date: 2026-07-27

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
 \qquad 0<a<b,
\]

and put

\[
 r=m-q_0,\qquad D=H-q_0,\qquad
 V_d=\binom{[n]}{r-d},\qquad N_d=|V_d|.
\]

For a constant-mass family of \(M\) depth-compatible occurrences, let
\(\mu_d\) be its depth-\(d\) load, let
\(B_d=|\operatorname{supp}\mu_d|\),
and let \(\widetilde E_d\) be repeat excess after subtracting the exact
integer floor.  The starting identity is

\[
 \boxed{
 H_d=(N_d-M)_++\widetilde E_d,
 \qquad
 \widetilde E_d=\min\{M,N_d\}-B_d.}
 \tag{0.1}
\]

This note proves the following.

1. **All abstract nested quotas can be synchronized exactly.**  If the
   top roots are free, one integral flow in the layered Boolean
   containment network gives \(M\) distinct-top nested flags whose load at
   every target is a floor or ceiling of \(M/N_d\).  Thus
   \(\widetilde E_d=0\) simultaneously for every \(d\).  Moreover, on
   \([2m]\), a symmetric-chain central bridge plus lower and upper Hall
   surjections gives an abstract two-sided strongly geodesic atlas with
   distinct initial middle owners and

   \[
      \widetilde E_q^- =\widetilde E_q^+=0
      \qquad(q_0\le q\le H).
   \]

   This is not one exact middle factor: the independently prescribed
   paths need not be iterates of one successor permutation.

2. **A deterministic leave-only inequality is false, even after exact
   point margins are imposed.**  Along an explicit infinite sequence of
   dimensions, partition \([n]\) into \(k\) equal blocks of logarithmic
   size and delete every rank-\(r\) root containing a complete block.  The
   leave has size

   \[
      (1+o(1))\frac{N_0}{\sqrt n}
   \]

   and is exactly point-regular.  Nevertheless every nested continuation
   of every retained root has

   \[
   \boxed{
      \sum_{d=0}^{D}\widetilde E_d
      \ge
      \left[
        \frac1{\sqrt2}\int_a^b e^{-u^2}\,du+o(1)
      \right]W.}
   \tag{0.2}
   \]

   Thus critical leave, exact point margins, top injectivity, and
   vertical nestedness do not force \(o(W)\) aggregate excess.  The
   construction is not proved to be the leave of an owner-disjoint packet
   matching, so (0.2) is not a physical counterexample to the packet
   theorem.

3. **The exact synchronized selection problem has a signed
   configuration dual.**  For a family of allowed whole histories over
   each entrance root, the fractional minimum of
   \(\sum_d\widetilde E_d\) is the maximum of one explicit signed Hall
   functional.  Unsaturated depths carry upper-capacity weights and
   saturated depths carry coverage weights.  The extremum over a root is
   taken over one whole history, not separately at each depth.  This is
   the exact reason rankwise independent nibbles do not compose.

4. **The adaptive packet formulation is an exact fresh-target
   telescope.**  If (Z_{d,t}(P)) is the number of fresh depth-(d)
   targets hit by a legal next packet and (C_{d,t}) is the increase in
   scalar support capacity, then

   \[
      \Delta\widetilde E_{d,t}=C_{d,t}-Z_{d,t}(P),
   \]

   with equality after summing over all stages and depths.  A proof now
   has to supply one extendible packet process with total signed deficit
   (o(W)); unbiased selection has the wrong, Poisson-sized drift.

5. **Corrected PBBS windows do synchronize locally, but do not yet solve
   the fixed-factor problem.**  The full uncut corrected deck has zero
   floor-correct excess at every depth, and the library of all coordinate
   conjugates contains an integral all-depth zero-excess section.  The
   same library also contains an all-depth-correct section with
   \(\Theta(W\sqrt m)\) excess.  After thinning one fixed PBBS factor, the
   exact ledger contains both an absorbing mortality staircase and the
   signed configuration problem.  PBBS support proves neither.  The upper
   tower is additionally tied to the opposite phase, and literal cyclic
   rebundling is still missing.

The precise boundary is therefore not vertical nestedness or integral
quota rounding.  It is **horizontal common-factor coherence**: selecting
whole lower/upper histories which are simultaneously low-excess and are
the windows of one exact successor permutation, then grouping those
successors into literal packet rows with affordable seams.

## 1. Exact floor identities and the hinge form

Let (M) occurrences be present at every depth and put

\[
 \mu_d(T)\in\mathbb Z_{\ge0},\qquad
 \sum_{T\in V_d}\mu_d(T)=M,
 \qquad
 B_d=|\{T:\mu_d(T)>0\}|.
 \tag{1.1}
\]

The raw repeat count is

\[
 E_d=\sum_T(\mu_d(T)-1)_+=M-B_d.
 \tag{1.2}
\]

Subtracting the unavoidable floor ((M-N_d)_+) gives

\[
 \widetilde E_d
 =M-B_d-(M-N_d)_+
 =\min\{M,N_d\}-B_d.
 \tag{1.3}
\]

Since (H_d=N_d-B_d), equation (0.1) follows.  There is also an exact
one-sided hinge description:

\[
 \boxed{
 \widetilde E_d=
 \begin{cases}
   \displaystyle\sum_{T\in V_d}(\mu_d(T)-1)_+,&M\le N_d,\\[2mm]
   \displaystyle\sum_{T\in V_d}(1-\mu_d(T))_+,&M>N_d.
 \end{cases}}
 \tag{1.4}
\]

At (M=N_d) the two expressions agree, because their difference is
\(\sum_T(\mu_d(T)-1)=0\).  Formula (1.4) is the correct mixed-regime
objective: before scalar saturation it penalizes collisions, and after
saturation it penalizes holes.

## 2. One integral flow balances every depth when the top is free

Consider the layered directed containment graph

\[
 V_0\longrightarrow V_1\longrightarrow\cdots\longrightarrow V_D,
 \qquad T\to R\iff R\subset T, |T\setminus R|=1.
 \tag{2.1}
\]

### Theorem 2.1 (free-top simultaneous balanced flags)

For every integer \(0\le M\le N_0\), there are \(M\) flags

\[
 T_{i,0}\supset T_{i,1}\supset\cdots\supset T_{i,D},
 \qquad |T_{i,d}|=r-d,
 \tag{2.2}
\]

whose top members are distinct and whose load at every \(R\in V_d\)
belongs to

\[
 \left\{
   \left\lfloor\frac{M}{N_d}\right\rfloor,
   \left\lceil\frac{M}{N_d}\right\rceil
 \right\}.
 \tag{2.3}
\]

Consequently \(\widetilde E_d=0\) for all \(0\le d\le D\).

#### Proof

Split every network vertex into an in-node and an out-node.  Give its
splitting arc the integral lower and upper capacities

\[
 \ell_d=\left\lfloor\frac{M}{N_d}\right\rfloor,
 \qquad
 u_d=\left\lceil\frac{M}{N_d}\right\rceil.
 \tag{2.4}
\]

Add a source and sink and require total flow (M).  At the top,
\(u_0\le1\), so an integral flow uses distinct top vertices.

A fractional feasible flow is uniform.  Give every vertex of layer (d)
throughput (M/N_d), and every containment arc from (V_d) to
\(V_{d+1}\) the value

\[
 \frac{M}{N_d(r-d)}
 =\frac{M}{N_{d+1}(n-r+d+1)}.
 \tag{2.5}
\]

The equality follows from

\[
 N_d(r-d)=N_{d+1}(n-r+d+1).
 \tag{2.6}
\]

Thus all balances and bounds hold.  The feasible-flow polytope of a
directed network with integral lower and upper capacities is integral.
Choose an integral flow and decompose its acyclic value-(M) flow into
unit source-sink paths.  These are the flags (2.2), and their node loads
are (2.3).  Such loads have support (M) when (M<N_d) and full support
when \(M\ge N_d\), proving zero excess. \(\square\)

The freedom at the top is essential.  For a prescribed top family one
must satisfy all cuts of the induced layered network; uniform fractional
flow is no longer available.

### Proposition 2.2 (distance to a balanced flag family)

Let \(\mu\) be any integer load of mass \(M\) on \(N\) targets, and let
\(b\) be a balanced mass-\(M\) load whose entries are
\(u=\lfloor M/N\rfloor\) or \(u+1\).  Then

\[
 \boxed{
  \widetilde E(\mu)
  \le \frac{\|\mu-b\|_1}{2\max\{1,u\}}.}
 \tag{2.7}
\]

If actual flags (T_{i,d}) are paired with balanced flags (B_{i,d}),
then

\[
 \boxed{
 \sum_d\widetilde E_d
 \le
 \sum_{i,d}
 \frac{\mathbf1_{\{T_{i,d}\ne B_{i,d}\}}}
      {\max\{1,\lfloor M/N_d\rfloor\}}.}
 \tag{2.8}
\]

#### Proof

If (u=0), the balanced support has size (M).  Its deficit mass relative
to \(\mu\) is at least
\(M-|\operatorname{supp}\mu|=\widetilde E(\mu)\).
If \(u\ge1\), then \(\widetilde E(\mu)\) is the number of zero cells, and
each zero cell is short of (b) by at least (u).  Equal total masses
make total deficit equal to \(\|\mu-b\|_1/2\), proving (2.7).

At one depth,

\[
 \|\mu_d-b_d\|_1
 \le\sum_i\|\mathbf1_{T_{i,d}}-\mathbf1_{B_{i,d}}\|_1
 =2|\{i:T_{i,d}\ne B_{i,d}\}|.
\]

Apply (2.7) and sum over \(d\). \(\square\)

This is a genuine deterministic inequality, but it transfers the problem
to finding one (o(W))-mismatch coupling with the actual entrance family
and actual histories.  The next section proves that critical leave and
exact point margins do not guarantee such a coupling.

## 3. A critical, point-regular shared leave with linear aggregate shadow lock

The construction is stated on an infinite sequence so that equal blocks
and exact coordinate transitivity are literal.

Fix \(0<a<b\).  Let \(t\to\infty\), and let \(k=k_t\) be the nearest even
integer to

\[
 2^{2t/3}t^{-1/3},
 \tag{3.1}
\]

and put

\[
 n=kt=2m.
 \tag{3.2}
\]

Partition ([n]) into (k) blocks

\[
 Y_1\dot\cup\cdots\dot\cup Y_k=[n],
 \qquad |Y_i|=t.
 \tag{3.3}
\]

Take \(q_0=a\sqrt m+O(1)\), \(H=b\sqrt m+O(1)\), and \(r=m-q_0\).
For \(0\le d\le D=H-q_0\), define the block-star family

\[
 \mathcal L_d=
 \{R\in V_d:Y_i\subseteq R\text{ for at least one }i\}.
 \tag{3.4}
\]

At the entrance retain

\[
 \mathcal A=V_0\setminus\mathcal L_0,
 \qquad M=|\mathcal A|=N_0-|\mathcal L_0|.
 \tag{3.5}
\]

### Theorem 3.1 (point-regular block-star shadow lock)

Uniformly for \(0\le d\le D\),

\[
 \boxed{
 \frac{|\mathcal L_d|}{N_d}
 =\frac{1+o(1)}{\sqrt n}.}
 \tag{3.6}
\]

The entrance leave \(\mathcal L_0\) is exactly point-regular:

\[
 \boxed{
 |\{R\in\mathcal L_0:x\in R\}|
 =\frac{r|\mathcal L_0|}{n}
 \qquad(x\in[n]).}
 \tag{3.7}
\]

For every choice of one nested flag

\[
 R=T_0(R)\supset T_1(R)\supset\cdots\supset T_D(R),
 \qquad T_d(R)\in V_d,
 \tag{3.8}
\]

from every \(R\in\mathcal A\), every member of \(\mathcal L_d\) is a
depth-\(d\) hole.  If

\[
 d_*=\left\lfloor\frac{1}{2\sqrt2\,a}\right\rfloor+1,
 \tag{3.9}
\]

then \(M\ge N_d\) for all \(d\ge d_*\) and all sufficiently large \(t\).
Consequently the flags in (3.8) satisfy the explicit asymptotic lower bound

\[
 \boxed{
 \sum_{d=0}^{D}\widetilde E_d
 \ge
 \left[
   \frac1{\sqrt2}\int_a^b e^{-u^2}\,du+o(1)
 \right]W.}
 \tag{3.10}
\]

#### Proof

For one fixed block, a uniformly random member of (V_d) contains it
with probability

\[
 p_{1,d}=\frac{(r-d)_t}{(n)_t},
 \tag{3.11}
\]

where ((x)_s=x(x-1)\cdots(x-s+1)).  Two prescribed blocks are both
contained with probability

\[
 p_{2,d}=\frac{(r-d)_{2t}}{(n)_{2t}}.
 \tag{3.12}
\]

Because \(t=O(\log n)\), \(r/n=1/2+O(n^{-1/2})\), and
\(d=O(\sqrt n)\), uniformly in the displayed range,

\[
 p_{1,d}=2^{-t}
 \left(1+O_{a,b}\left(\frac{t}{\sqrt m}+\frac{t^2}{m}\right)\right),
 \qquad
 p_{2,d}=2^{-2t}(1+o(1)).
 \tag{3.13}
\]

Bonferroni gives

\[
 kp_{1,d}-\binom{k}{2}p_{2,d}
 \le\frac{|\mathcal L_d|}{N_d}
 \le kp_{1,d}.
 \tag{3.14}
\]

The choice (3.1) satisfies

\[
 \sqrt n,k2^{-t}
 =k^{3/2}t^{1/2}2^{-t}\longrightarrow1,
 \tag{3.15}
\]

whereas (k^22^{-2t}=(1+o(1))/n).  Equations
(3.13)--(3.15) prove (3.6).

The wreath product \(S_t\wr S_k\) preserves \(\mathcal L_0\) and is
transitive on the (n) coordinates.  Hence all point degrees in the
leave are equal.  Double counting its \(r|\mathcal L_0|\) incidences
proves (3.7).

If (T_d(R)) contained some whole block (Y_i), then its ancestor
\(R\supseteq T_d(R)\) would also contain \(Y_i\), contrary to
\(R\in\mathcal A\).  Thus every target in \(\mathcal L_d\) is a hole,
independently of how the flags are chosen.

For fixed (d), the exact layer ratio gives

\[
 \frac{N_0-N_d}{N_0}
 =\frac{2ad+o(1)}{\sqrt m},
 \tag{3.16}
\]

whereas (3.6) gives

\[
 \frac{|\mathcal L_0|}{N_0}
 =\frac{1+o(1)}{\sqrt{2m}}.
 \tag{3.17}
\]

The definition (3.9) therefore gives
\(M=N_0-|\mathcal L_0|\ge N_{d_*}\)
for large (t).  Since (N_d) decreases with (d), the same holds for
all \(d\ge d_*\).  In that regime (1.3) says that excess is exactly the
hole count, so

\[
 \widetilde E_d\ge|\mathcal L_d|.
 \tag{3.18}
\]

Uniformly for \(d=x\sqrt m+O(1)\), \(0\le x\le b-a\),

\[
 \frac{N_d}{N_0}=e^{-2ax-x^2+o(1)}.
 \tag{3.19}
\]

Using (3.6), discarding the fixed number of depths below (d_*), and
taking the Riemann sum gives

\[
 \sum_d\widetilde E_d
 \ge
 \left[
   \frac1{\sqrt2}
   \int_0^{b-a}e^{-2ax-x^2}\,dx+o(1)
 \right]N_0.
 \tag{3.20}
\]

Finally

\[
 \frac{N_0}{W}=e^{-a^2+o(1)}.
 \tag{3.21}
\]

Substitute \(u=a+x\) in (3.20) to obtain (3.10). \(\square\)

### Scope of the obstruction

The retained entrance family \(\mathcal A\) has exactly the point margins
required of a union of complete cyclic packet decks, because (3.7) also
implies

\[
 |\{R\in\mathcal A:x\in R\}|=\frac{rM}{n}.
 \tag{3.22}
\]

But point regularity is only necessary.  It is not proved that
\(\mathcal A\) decomposes into owner-disjoint cyclic packet decks, that
\(M\) has the required packet divisibility, or that the complementary
upper targets can be realized in the same exact factor.  Therefore
Theorem 3.1 rules out every black-box implication

\[
 \text{critical leave + exact point margins + nestedness}
 \Longrightarrow \sum_d\widetilde E_d=o(W),
 \tag{3.23}
\]

but it does not refute a theorem using the full packet successor and its
history.

There is a useful conditional seam comparison.  If one altered
entrance-trace adjacency affects at most (d) depth-(d) descendants,
then (s) altered adjacencies can reduce the aggregate obstruction by at
most

\[
 s\sum_{d=1}^{D}d=\frac{sD(D+1)}2.
 \tag{3.24}
\]

With at most one such alteration per (n=2m) retained packet, this is at
most

\[
 \left[
   \frac{e^{-a^2}(b-a)^2}{4}+o(1)
 \right]W.
 \tag{3.25}
\]

Thus the block obstruction would survive that particular restricted
rebundling whenever

\[
 \frac1{\sqrt2}\int_a^b e^{-u^2}\,du
 >\frac{e^{-a^2}(b-a)^2}{4}.
 \tag{3.26}
\]

This holds for every sufficiently thin fixed annulus.  Equations
(3.24)--(3.26) are conditional on the stated adjacency-influence model;
unrestricted physical seams can have \(\Theta(W)\) aggregate influence.

## 4. A two-sided zero-excess atlas with distinct initial owners

The negative result above does not mean that two-sided integral
chronology is intrinsically inconsistent.  The following strengthens the
free-top theorem in the direction of common owners.

### Theorem 4.1 (SCD-seeded distinct-owner two-sided atlas)

For every \(0\le q_0\le H\le m\), there are
\(M=N_{q_0}=\binom{2m}{m-q_0}\) strongly geodesic \(H\)-step Johnson
paths

\[
 \Gamma_S=(X_{S,0},X_{S,1},\ldots,X_{S,H}),
 \qquad S\in\binom{[2m]}{m-q_0},
 \tag{4.1}
\]

such that:

1. the initial middle owners \(X_{S,0}\) are pairwise distinct;
2. at depth \(q_0\), the lower intersections are the distinct roots
   \(S\), and the upper unions are every rank-\((m+q_0)\) set exactly once;
3. for every \(q_0\le q\le H\), the lower-intersection map is surjective
   onto \(\binom{[2m]}{m-q}\), and the upper-union map is surjective onto
   \(\binom{[2m]}{m+q}\).

Consequently

\[
 \boxed{
 \widetilde E_q^- =\widetilde E_q^+=0
 \qquad(q_0\le q\le H).}
 \tag{4.2}
\]

#### Proof

Fix any symmetric chain decomposition of the Boolean lattice
\(2^{[2m]}\).  A chain containing a set \(S\) of rank \(m-q_0\) reaches
both ranks \(m\) and \(m+q_0\).  Let \(X_S\) and \(U_S\) be its unique
sets at those ranks.  Distinct \(S\)'s lie on distinct chains, so the
middle sets \(X_S\) are distinct.  Conversely every rank-\((m+q_0)\) set
lies on a symmetric chain which reaches rank \(m-q_0\).  Hence

\[
 S\longmapsto U_S
 \tag{4.3}
\]

is a bijection between the two entrance shores.

For every \(1\le k\le m\), the facet-containment graph from rank \(k\)
to rank \(k-1\) has a matching saturating the lower shore.  Indeed, if
\(\mathcal U\) is a family of \((k-1)\)-sets, incidence double counting
gives

\[
 k|N(\mathcal U)|\ge(2m-k+1)|\mathcal U|\ge k|\mathcal U|.
 \tag{4.4}
\]

Direct matched \(k\)-sets to their matched facets and direct every
unmatched \(k\)-set to an arbitrary facet.  This gives a surjection from
rank \(k\) onto rank \(k-1\).  Compose these maps below every entrance
root \(S\) to obtain strict lower flags \(L_{S,q}\), surjective at each
rank \(m-q\).

The reversed argument above the middle gives, for every \(k\ge m\), a
surjection from rank \(k\) onto rank \(k+1\) along containment.  Compose
these maps from the bijective upper entrances \(U_S\) to obtain strict
upper flags \(U_{S,q}\), surjective at each rank \(m+q\).

Order the \(q_0\) elements of \(X_S\setminus S\) as the first deletion
labels and the \(q_0\) elements of \(U_S\setminus X_S\) as the first
insertion labels.  The later deletion labels are the successive
differences of the lower flag and lie in (S); the later insertion
labels are the successive differences of the upper flag and lie outside
\(U_S\).  Thus all \(2H\) labels are pairwise distinct.  If they are

\[
 d_1,\ldots,d_H,qquad a_1,\ldots,a_H,
\]

put

\[
 X_{S,t}=X_S-\{d_1,\ldots,d_t\}
                +\{a_1,\ldots,a_t\}.
 \tag{4.5}
\]

This is strongly geodesic, its lower intersections are (L_{S,q}), and
its upper unions are (U_{S,q}).  The entrance maps are bijective and
all later maps are surjective.  Since \(M=N_{q_0}\ge N_q\), full support
is exactly zero floor-correct excess on both signs. \(\square\)

The theorem remains outside one exact factor.  To be windows of one
successor permutation \(P\) on middle owners, the independently defined
paths would have to satisfy

\[
 P^t(X_{S,0})=X_{S,t}
 \qquad(0\le t\le H)
 \tag{4.6}
\]

with one and the same \(P\).  In particular, whenever two displayed paths
meet, their entire future and past must agree as dictated by \(P\); two
paths may not merge and later diverge, and every used state must have one
predecessor and one successor.  Distinct initial owners do not imply any
of these conditions.  Even vertex-disjoint paths would still need
completion on omitted middle owners, cyclic phase grouping, and the
literal wreath cocycle.  Equation (4.6) is the first exact horizontal
closure gate suppressed by the abstract atlas.

For ordinary cyclic packet flags there is an additional phase-overlap
identity.  If \(T_{j,d}\) is the depth-\(d\) lower target at phase \(j\),
then

\[
 \boxed{T_{j,d+1}=T_{j,d}\cap T_{j+1,d}.}
 \tag{4.7}
\]

Equivalently, the deletion word at phase \(j+1\) is the one-step shift of
the deletion word at phase \(j\).  The network flow in Theorem 2.1 and
the atlas in Theorem 4.1 impose no such de Bruijn-type overlap.

## 5. The exact signed configuration LP

Let \(\mathcal R\) be a set of \(M\) entrance roots.  For each
\(x\in\mathcal R\), let \(\Omega(x)\) be a finite family of allowed whole
histories.  Assume for this section that every history is correct at every
controlled depth and supplies one target

\[
 T_d(\omega)\in V_d.
 \tag{5.1}
\]

A fractional common section consists of numbers

\[
 z_{x,\omega}\ge0,
 \qquad
 \sum_{\omega\in\Omega(x)}z_{x,\omega}=1
 \quad(x\in\mathcal R).
 \tag{5.2}
\]

Its target loads are

\[
 y_{d,T}(z)=
 \sum_{x\in\mathcal R}
 \sum_{\omega\in\Omega(x)}
 z_{x,\omega}\mathbf1_{\{T_d(\omega)=T\}}.
 \tag{5.3}
\]

Put

\[
 \mathcal U=\{d:M\le N_d\},
 \qquad
 \mathcal S=\{d:M>N_d\}.
 \tag{5.4}
\]

Define the fractional hinge objective

\[
 \mathcal E(z)=
 \sum_{d\in\mathcal U}\sum_{T\in V_d}(y_{d,T}(z)-1)_+
 +
 \sum_{d\in\mathcal S}\sum_{T\in V_d}(1-y_{d,T}(z))_+.
 \tag{5.5}
\]

For an integral section, (1.4) says exactly

\[
 \mathcal E(z)=\sum_d\widetilde E_d.
 \tag{5.6}
\]

### Theorem 5.1 (signed all-depth configuration dual)

The fractional optimum \(\mathcal E_{\rm frac}=\min_z\mathcal E(z)\)
equals

\[
\boxed{
\begin{aligned}
 \max_{\substack{0\le\alpha_{d,T}\le1\ (d\in\mathcal S)\\
                  0\le\beta_{d,T}\le1\ (d\in\mathcal U)}}
 \Bigg[&
   \sum_{d\in\mathcal S}\sum_T\alpha_{d,T}
   -\sum_{d\in\mathcal U}\sum_T\beta_{d,T}\\
 &+\sum_{x\in\mathcal R}
   \min_{\omega\in\Omega(x)}
   \left(
     \sum_{d\in\mathcal U}
       \beta_{d,T_d(\omega)}
     -\sum_{d\in\mathcal S}
       \alpha_{d,T_d(\omega)}
   \right)
 \Bigg].
\end{aligned}}
 \tag{5.7}
\]

In particular, \(\mathcal E_{\rm frac}=0\) if and only if, for every
such pair of weight arrays,

\[
\boxed{
 \sum_{x\in\mathcal R}
 \max_{\omega\in\Omega(x)}
 \left(
   \sum_{d\in\mathcal S}\alpha_{d,T_d(\omega)}
   -\sum_{d\in\mathcal U}\beta_{d,T_d(\omega)}
 \right)
 \ge
 \sum_{d\in\mathcal S,T}\alpha_{d,T}
 -\sum_{d\in\mathcal U,T}\beta_{d,T}.}
 \tag{5.8}
\]

#### Proof

For every real (y),

\[
 (y-1)_+=\max_{0\le\beta\le1}\beta(y-1),
 \qquad
 (1-y)_+=\max_{0\le\alpha\le1}\alpha(1-y).
 \tag{5.9}
\]

Substitute (5.9) into (5.5).  The resulting expression is bilinear in
the product-of-simplices variable (z) and the compact box of weights
\((\alpha,\beta)\).  Finite-dimensional linear-programming duality
interchanges the minimum and maximum.  For fixed weights, minimization
over (z) separates over the entrance roots and chooses the least-cost
whole history in each fibre.  This gives (5.7).

Every hinge is nonnegative, so the primal optimum is zero precisely when
the expression in (5.7) is at most zero for every weight array.  Multiply
the rootwise minima by \(-1\) to obtain (5.8). \(\square\)

When every depth is saturated, (5.8) reduces to the usual nonnegative
configuration-support inequality.  The \(\beta\) terms are the missing
half at unsaturated ranks: there one needs capacity at most one rather
than coverage at least one.  Most importantly, the maximum in (5.8) is
over one whole history \(\omega\).  Replacing it by independent maxima at
each depth gives a strictly weaker collection of rankwise Hall tests.

The integral optimum can exceed (5.7), because the product-of-simplices
configuration matrix is not proved integral.  Thus (5.8) is an exact
fractional gate, not the desired integral packet theorem.

## 6. The exact adaptive fresh-target process

For completeness, the process version can be stated without any
probabilistic approximation.  Suppose (t) legal packets have been
selected, each contributing (n) occurrences at every depth.  Put

\[
 G_t=nt,
 \qquad
 \mathcal B_{d,t}=\operatorname{supp}\mu_{d,t}.
 \tag{6.1}
\]

For a legal next packet (P), let

\[
 Z_{d,t}(P)=
 |\{\text{depth-}d\text{ targets of }P\}\setminus\mathcal B_{d,t}|,
 \tag{6.2}
\]

and let

\[
 C_{d,t}=
 \min\{G_t+n,N_d\}-\min\{G_t,N_d\}.
 \tag{6.3}
\]

### Theorem 6.1 (fresh-target telescope)

For every ordered entrance matching of packets,

\[
 \boxed{
 \widetilde E_{d,t+1}-\widetilde E_{d,t}
 =C_{d,t}-Z_{d,t}(P_{t+1}),}
 \tag{6.4}
\]

and hence

\[
 \boxed{
 \sum_d\widetilde E_{d,s}
 =\sum_{t=0}^{s-1}
   \left(
      \sum_d C_{d,t}-\sum_dZ_{d,t}(P_{t+1})
   \right).}
 \tag{6.5}
\]

#### Proof

After (t) packets,

\[
 \widetilde E_{d,t}=\min\{G_t,N_d\}-|\mathcal B_{d,t}|.
\]

The first term increases by (C_{d,t}), while support increases by
exactly (Z_{d,t}(P_{t+1})).  This proves (6.4); summing proves (6.5).
\(\square\)

Therefore it is sufficient to construct one extendible trajectory for
which the cumulative positive deficit in (6.5) is (o(W)).  Since there
are \(\Theta(W/n)\) selected packets, any implementation which pays only
nonnegative stage deficits needs average deficit (o(n)) per packet.
An unbiased complete-catalogue packet has expected fresh score
\(nH_{d,t}/N_d\), producing order-\(n\), not \(o(n)\), deficit when the
load is a positive fraction of a layer.  Thus ordinary independent
nibbling is quantitatively on the Poisson side of the gate.

## 7. Audit of corrected PBBS windows

This section uses the native odd PBBS ground set \(n=2m+1\).  Write
\(W_{\rm PBBS}=\binom{2m+1}{m}\), let \(g\) be the oriented step-two
PBBS successor, and write

\[
 L_q(X)=\bigcap_{j=0}^{q}g^jX.
 \tag{7.1}
\]

### 7.1 What is genuinely synchronized

If a PBBS start is correct at depth \(q+1\), it is correct at depth \(q\).
Indeed the rank excess

\[
 \eta_q(X)=|L_q(X)|-(m-q)
 \tag{7.2}
\]

is nondecreasing and increases by zero or one at each step.  Hence the
correct domains are nested.  One audited global-maximum PBBS terminal fan
also supplies one literal nested tower at every shallower depth.  A
generic correct deep lower window gives a correct-rank Johnson trace
path; it need not be geodesic because a previously deleted trace
coordinate may return.  The special global-maximum fan is geodesic by
its stronger chronology rule.

For the full uncut corrected deck at a fixed depth, every target occurs.
If its correct mass is \(G_q\ge N_q\), then raw repeats equal
\(G_q-N_q\), exactly the forced floor.  Thus

\[
 \boxed{\widetilde E_q^{\rm full}=0}
 \tag{7.3}
\]

at every depth.  The masses (G_q) vary with (q), so this is not yet a
constant-mass packet family.

If coordinate conjugates of PBBS are allowed to depend on the entrance
root, Hall-surjective facet maps give one strict descending flag per
entrance root, surjective at every later rank.  Symmetric-group
transitivity on ordered flags realizes each one in a suitable conjugate
of a fixed terminal PBBS fan.  This gives an exact integral all-depth
one-sided section with zero excess.  Conversely, choosing from each root
the flag which repeatedly deletes its largest remaining coordinate has
depth-\(j\) support

\[
 \binom{n-j}{m-q_0-j}
 \tag{7.4}
\]

and aggregate excess
\(\Theta_{a,b}(W_{\rm PBBS}\sqrt m)\).  Thus the same nested
conjugate-fan library contains both an exact good section and a maximally
bad one.  Nested fan availability alone has no preferred sign.

### 7.2 The exact thinning correction

Let (M=N_{q_0}-L) starts be selected, all correct at entrance depth.
Let (b_d) be the number which have become incorrect by depth
\(q_0+d\).  Mortality is absorbing, so

\[
 0=b_0\le b_1\le\cdots.
 \tag{7.5}
\]

The live mass is \(G_d=M-b_d\).  If \(\widetilde E_d\) is repeat excess
above the floor for this live mass, then the exact corrected hole identity
is

\[
 \boxed{
 H_d=
 \bigl(b_d+L-(N_{q_0}-N_{q_0+d})\bigr)_+
 +\widetilde E_d.}
 \tag{7.6}
\]

Therefore one selected PBBS section succeeds only if the same histories
satisfy both

\[
 \sum_d
 \bigl(b_d+L-(N_{q_0}-N_{q_0+d})\bigr)_+=o(W)
 \tag{7.7}
\]

and

\[
 \sum_d\widetilde E_d=o(W).
 \tag{7.8}
\]

PBBS all-depth support proves neither condition after thinning.

At one depth, selection is exactly Hall in the chronology-restricted
graph from entrance roots to eligible descendants.  Complete PBBS
support proves only the singleton Hall inequalities.  At all depths, the
correct fractional statement is the configuration inequality (5.8),
augmented by the live/dead indicators in (7.6); integral selection is
stronger still.

Finally, the two signs cannot be selected independently.  The PBBS
complement identity is

\[
 \boxed{
 U_q(X)=[n]\setminus L_{q-1}(fX),}
 \tag{7.9}
\]

so the upper depth-(q) tower is the phase-shifted complement of the
opposite lower tower.  The root-dependent conjugate construction does
not preserve this pairing inside one canonical factor.

### 7.3 PBBS verdict

Corrected PBBS windows can serve all depths simultaneously in three
limited senses:

1. one deep corrected fan supplies one common shallower tower;
2. the full uncut corrected deck has zero floor-correct excess at every
   depth with its own live mass;
3. the library of all coordinate conjugates admits an exact integral
   zero-excess lower section.

They do **not** presently give one critical-size, mortality-controlled,
two-phase section inside one fixed exact PBBS factor, nor a grouping of
that section into literal cyclic packet rows.  Those are precisely the
requirements that symmetrization and rankwise support discard.

## 8. Proved and open boundary

Proved here:

1. the exact support and hinge identities (1.3)--(1.4);
2. simultaneous free-top floor/ceiling balance by one integral layered
   flow;
3. the weighted \(L^1\)-to-repeat and flag-mismatch inequalities;
4. a critical-size, exactly point-regular leave which forces the explicit
   \(\Omega(W)\) lower bound (3.10) for every nested continuation;
5. an abstract two-sided strongly geodesic zero-excess atlas whose
   initial middle owners are distinct;
6. the exact mixed-regime signed configuration dual;
7. the exact adaptive fresh-target telescope;
8. the corrected PBBS mortality ledger and the precise good/bad
   all-conjugate comparison.

Not proved:

1. decomposition of the block-free entrance family in Theorem 3.1 into
   owner-disjoint cyclic packets or one exact factor;
2. a fixed-factor PBBS section satisfying both (7.7) and (7.8);
3. integrality, with \(o(W)\) objective, of the signed configuration LP
   for the physical packet/PBBS history catalogue;
4. a single successor permutation realizing the distinct-owner atlas in
   Theorem 4.1;
5. literal packet phase closure (4.7), the paired upper sign, and an
   \(o(W)\)-cost seam compilation; or
6. coefficient one.

The strongest exact conclusion is the following dichotomy.

> Vertical all-depth balancing is integrally feasible, and even distinct
> initial owners plus two-sided geodesicity are feasible.  On the other
> hand, critical point-regular leave and nestedness alone admit a linear
> shadow lock.  Therefore every successful constant-one argument must use
> the horizontal algebra of one exact successor factor—equivalently, it
> must prove the signed whole-history configuration inequalities together
> with successor/phase closure.  No rankwise independent nibble can supply
> that missing content.

## 9. Independent audit record

Two independent proof audits were performed.

1. The block-star audit verified the uniform one- and two-block
   probabilities, exact \(S_t\wr S_k\) point regularity, the cutoff
   \(d_*=\lfloor(2\sqrt2\,a)^{-1}\rfloor+1\), the Riemann-sum constant
   \[
      \frac1{\sqrt2}\int_a^b e^{-u^2}\,du,
   \]
   and the distinction between an abstract point-regular leave and a
   physically packet-realizable leave.  It also verified the conditional
   adjacency-seam constant in (3.25).

2. The configuration/SCD audit verified all signs in (5.7)--(5.8),
   including the equality case \(M=N_d\), and verified that the SCD bridge
   makes the initial middle owners distinct while leaving successor
   closure (4.6) completely unproved.  No additional mathematical
   correction was required.
