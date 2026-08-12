# Mathematical attack J: recursive Euler coloring and exact RSCD lifting

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computer-assisted enumeration was used.

## 0. Verdict

This attack does **not** prove \(\mathrm{RSCD}_A\), MWB, or the
contiguous-OR conjecture.  It gives four unconditional advances and isolates
two constructive integral gates together with one exact frozen-resolution
criterion.

1. For every collection \(\mathcal R\) of *native*, unclipped radii, the
   singleton forests in an arbitrary full SCD give an exact SCD-color
   resolution whose corrected prefix overhead is
   \[
   Q_m\sum_{d\in\mathcal R}2d\,c_d.
   \]
   The combined prefix and physical-initialization charge is
   \[
   O\!\left(
      \frac{Q_mW}{m}\sum_{d\in\mathcal R}(2d+1)^2
   \right).
   \]
   Hence it is \(o(Q_mW)\) for every fixed finite set of native radii, for
   all native radii \(d\le D=o(m^{1/3})\), and for the dyadic native radii
   \(1,2,4,\ldots,D\) whenever \(D=o(\sqrt m)\).  This is an exact
   integral SCD resolution, but it does not control the clipped top class
   \(\gamma_H=N_H\).

2. For each fixed \(H\), an explicit family of \(2\ell\)-state rotor cycles,
   combined with the fixed-uniformity Pippenger--Frankl--Rödl matching
   theorem and a slow diagonal \(\ell\to\infty\), gives a mask-disjoint
   packing of radius-\(H\) band chains which misses only \(o(W)\) masks and
   has only \(o(W)\) rotor cycles.  Cutting each cycle once gives the exact
   word ledger
   \[
   W+o(W)
   \]
   for the fixed central band.  This is an integral partial chain packing
   and a direct band word, not yet a saturated band SCD.  A concrete
   \(B_4\) example shows that correct residual rank counts do not imply
   completion.

3. There is an exact recursive one-layer lift theorem.  A retained
   radius-\(h\) rotor edge lifts to radius \(h+1\) precisely under four
   explicit endpoint constraints.  After these constraints are imposed,
   extending the active chains is equivalent to **two genuine perfect
   matchings**, one on lower endpoints and one on complementary upper
   endpoints.  If \(s_h\) active/inactive crossings and \(k_h\) retained
   edges are cut at layer \(h\), the corrected toll changes by the exact
   amount
   \[
   \boxed{
   \Delta\widehat\Phi_h
      =2h\,s_h+2b_{A,h}+2(h+1)k_h .}
   \]
   Using the exact odd-cut middle-layer paths and globally contiguous clipped
   radius blocks gives
   \[
   \boxed{
   \widehat\Phi_H
      \le H(H-1)+2H(\operatorname{Cat}_m+1)+2HK_H,}
   \]
   where \(K_H=\sum_{h<H}k_h\).  Thus the exact constrained-Hall lift lemma
   \(K_H=o(W/H)\) would prove \(\mathrm{RSCD}_A\) for
   \(H=\lceil A\sqrt m\rceil\).  The exact central-band extension theorem
   then supplies the outer ranks automatically.
   This is the smallest replacement lemma found for the recursive route.

4. The low-run pseudo-resolution and any prescribed genuine SCD-orbit
   resolution can be reconciled exactly by a packet-palette optimization.
   Its optimum \(V_d^*\) is exactly the number of internal color switches,
   provided the packets are open paths and packet copies may be permuted
   freely from one layer to the next.  The exact hard-cut run count is
   \[
   Q_mp_d^0+V_d^*,
   \]
   and a path-annihilating test function gives a rigorous dual lower bound
   on \(V_d^*\).  This identifies a representation-theoretic obstruction
   space, but no missing isotype of the required asymptotic size is proved.

The principal unresolved statement is therefore not a fractional balancing
claim.  It is an integral, common-owner pair of recursively coupled Hall
matchings with a subcritical number of deleted rotor adjacencies.

## 1. Corrected RSCD ledger

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
N_d=\binom{2m}{m-d},\qquad
Q_m=(2m-1)(2m)!.
\]

Let \(N_{m+1}=0\) and

\[
c_d=N_d-N_{d+1}\qquad(0\le d\le m).
\]

For a band of depth \(H\), the numbers of clipped chain states are

\[
\gamma_d=c_d\quad(0\le d<H),
\qquad
\gamma_H=N_H.
\tag{1.1}
\]

Thus

\[
\sum_{d=0}^H\gamma_d=W,
\qquad
\sum_{d=q}^H\gamma_d=N_q.
\tag{1.2}
\]

A radius-\(d\) labelled chain state is

\[
\omega=(L;z_1,\ldots,z_{2d};R),
\qquad |L|=|R|=m-d,
\tag{1.3}
\]

and represents the chain

\[
L,\ L+z_1,\ \ldots,\ L+z_1+\cdots+z_{2d}.
\tag{1.4}
\]

For \(d\ge1\), a directed rotor successor is

\[
(L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
\quad x\in L,\ y\in R.
\tag{1.5}
\]

At \(d=0\), it is the ordinary Johnson swap

\[
(L;\ ;R)\longmapsto(L-x+y;\ ;R-y+x).
\tag{1.6}
\]

For a full SCD \(\mathcal D\), clipped at depth \(H\), let
\(p_d^*(\mathcal D)\) be the minimum number of components in a spanning
vertex-disjoint directed path forest of the radius-\(d\) state set of
\(\mathcal D\).  Define

\[
\widehat\Phi_H(\mathcal D)
   =\sum_{d=0}^H2d\,p_d^*(\mathcal D).
\tag{1.7}
\]

The corrected form of \(\mathrm{RSCD}_A\) is:

> For every fixed \(A>0\), with \(H=\lceil A\sqrt m\rceil\), there is a
> full integral SCD \(\mathcal D_{m,A}\) such that
> \[
> \widehat\Phi_H(\mathcal D_{m,A})=o(W).
> \tag{1.8}
> \]

The word “full” is essential.  Separate decompositions at separate depths do
not establish (1.8).  A *complete saturated SCD* of the central band is
sufficient, however, because of Theorem 1.2 below.

### Lemma 1.1 (exact hard-reset prefix toll)

A directed run through \(t\) radius-\(d\) states, with \(0\le d<m\), has
exact hard-reset prefix length

\[
\boxed{t+2d.}
\tag{1.9}
\]

#### Proof

For the first state write

\[
\{z_{2d}\},\{z_{2d-1}\},\ldots,\{z_1\},L.
\]

Its successive suffix ORs are exactly the \(2d+1\) masks in (1.4).  If
(1.5) uses \(x,y\), append \(L-x+y\).  The new last-occurrence blocks are

\[
L-x+y,\{x\},\{z_1\},\ldots,\{z_{2d}\},
\]

followed by older blocks partitioning \(R-y\), and hence give precisely the
successor state.  Every later state costs one entry.  Conversely, the first
endpoint must expose \(2d+1\) distinct nested suffix ORs, and every later
endpoint requires a later entry.  Therefore the length is exactly
\((2d+1)+(t-1)=t+2d\).  \(\square\)

The residual block \(R\) need not be written.  Writing it gives the
conservative toll \(2d+1\), not the exact prefix toll.  At radius zero the
overhead is therefore zero.  This exactness is confined to the hard-reset
prefix architecture; it is not a universal lower bound for arbitrary words
which share setup between runs.

For reference, if

\[
\Phi_H(\mathcal D)=\sum_{d=0}^H(2d+1)p_d^*(\mathcal D),
\]

then, for \(H\ge1\),

\[
\widehat\Phi_H\le\Phi_H
\le\frac32\widehat\Phi_H+\frac{W}{m+1}.
\tag{1.10}
\]

Indeed, \(p_0^*\le c_0=W/(m+1)\), while
\(\sum_{d\ge1}p_d^*\le\widehat\Phi_H/2\).  Thus the two ledgers have the
same \(o(W)\) threshold, but their finite reset counts must not be
identified.

### Theorem 1.2 (exact central-band extension)

Every saturated symmetric-chain decomposition of the ranks

\[
m-H,m-H+1,\ldots,m+H
\]

extends integrally to a full SCD of \(B_{2m}\), preserving every band chain
as a contiguous subchain.

#### Proof

Suppose ranks \(r=m-q\) through \(2m-r=m+q\) have already been
decomposed symmetrically.  Let \(Y\) be the chains meeting both boundary
ranks, and write their correlated endpoints as

\[
A_y\in\binom{[2m]}r,
\qquad
B_y\in\binom{[2m]}{2m-r}.
\]

Put

\[
X=\binom{[2m]}{r-1},
\qquad
Z=\binom{[2m]}{2m-r+1}.
\]

Form a bipartite graph with sides \(X\sqcup Y^-\) and
\(Z\sqcup Y^+\).  Add the comparison edges

\[
x\sim y^+\iff x\subset A_y,
\qquad
y^-\sim z\iff B_y\subset z,
\]

and the identity edge \(y^-y^+\) for every \(y\).  Let

\[
\alpha=m+q+1,
\qquad
\beta=m-q.
\]

Give every comparison edge weight \(1/\alpha\), and every identity edge
weight

\[
1-\frac\beta\alpha
=\frac{2q+1}{m+q+1}.
\]

Every \(x\in X\) and \(z\in Z\) has \(\alpha\) comparison neighbors;
every \(y^-\) and \(y^+\) has \(\beta\) comparison neighbors plus its
identity edge.  Hence every row and every column has total weight one.  This
is a fractional perfect matching on a square bipartite graph.  Its support
satisfies Hall's condition and therefore contains an integral perfect
matching.

If \(y^-y^+\) is selected, the chain \(y\) stops at its current endpoints.
Otherwise the matching supplies a unique \(x\subset A_y\) and a unique
\(z\supset B_y\), extending it symmetrically by one rank on each side.  All
new outer masks are used exactly once.  Iterate from \(q=H\) to \(m-1\).
The original band chains remain intact inside the resulting full SCD.
\(\square\)

Thus full-SCD RSCD and saturated central-band RSCD are equivalent.  An
arbitrary partial packing is still insufficient: it must first be completed
to a saturated band SCD.

## 2. An exact native-radius and dyadic special case

The following elementary case is useful because it is fully integral and
uses genuine full-SCD colors.

### Lemma 2.1 (exact orbit resolution with prescribed forests)

Fix a full SCD \(\mathcal D\), and at each considered radius \(d\) fix a
spanning directed path forest \(F_d\) with \(p_d\) components.  The complete
coordinate orbit, with \(2m-1\) copies, resolves the exact rotor master into
\(Q_m\) genuine full-SCD colors and admits a chronology with at most
\(Q_mp_d\) hard runs at radius \(d\).

#### Proof

Write \(r=m-d\) and \(G=(2m)!\).  There are

\[
|\Omega_d|=\frac{G}{r!^2}
\]

radius-\(d\) states.  A state has stabilizer \(r!^2\), while a directed
rotor arc has stabilizer \((r-1)!^2\).  Index colors by
\((b,\sigma)\in[2m-1]\times S_{2m}\), with color \((b,\sigma)\) carrying
\(\sigma\mathcal D\) and \(\sigma F_d\).  Each state then occurs

\[
(2m-1)\gamma_dr!^2
\]

times, exactly its master occurrence multiplicity.  Since \(F_d\) has
\(\gamma_d-p_d\) arcs, its orbit uses every directed rotor arc

\[
(2m-1)(\gamma_d-p_d)(r-1)!^2
\]

times.  The unused multiplicity of every arc is therefore

\[
(2m-1)p_d(r-1)!^2.
\]

At each state the residual indegree and outdegree are equal, and both equal
the number of colored forest starts and ends there.  Pair residual incoming
arcs with colored starts, contract each connector followed by its colored
path, and Eulerize every balanced macrocomponent.  Expanding gives a
chronology using every master-arc copy exactly once and keeping every
selected colored path consecutive.  Cutting at path boundaries uses at most
\(Q_mp_d\) runs.  All colors remain exact integral SCDs.  \(\square\)

### Theorem 2.2 (native-radius low-toll resolution)

Let \(\mathcal R_m\subseteq\{0,1,\ldots,m-1\}\) be any set of native full-SCD
radii.  There is an exact genuine-SCD resolution whose corrected prefix
overhead on these radii is at most

\[
Q_m\sum_{d\in\mathcal R_m}2d\,c_d,
\tag{2.1}
\]

and whose prefix overhead plus separate physical circuit initialization is
at most

\[
2Q_m\sum_{d\in\mathcal R_m}(2d+1)c_d.
\tag{2.2}
\]

Moreover,

\[
\sum_{d\in\mathcal R_m}(2d+1)c_d
\le
\frac{W}{m}\sum_{d\in\mathcal R_m}(2d+1)^2.
\tag{2.3}
\]

#### Proof

Every full SCD has exactly \(c_d\) native radius-\(d\) chains.  Take every
state as a singleton path, so \(p_d=c_d\), and apply Lemma 2.1.  Lemma 1.1
gives (2.1).  A physical circuit containing a radius-\(d\) singleton path
can be initialized in at most \(2d+2\) entries.  Consequently the combined
charge is at most

\[
Q_m\sum_{d\in\mathcal R_m}(2d+2d+2)c_d
=2Q_m\sum_{d\in\mathcal R_m}(2d+1)c_d,
\]

which is (2.2).

Finally,

\[
\frac{N_{d+1}}{N_d}=\frac{m-d}{m+d+1},
\qquad
c_d=N_d\frac{2d+1}{m+d+1}.
\]

Since \(N_d\le W\) and \(m+d+1\ge m\),

\[
(2d+1)c_d\le\frac{W}{m}(2d+1)^2.
\]

Summing proves (2.3).  \(\square\)

### Corollary 2.3

The charge in (2.2) is \(o(Q_mW)\) whenever

\[
\sum_{d\in\mathcal R_m}(2d+1)^2=o(m).
\tag{2.4}
\]

In particular this holds for:

1. every fixed finite collection of native radii;
2. all native radii \(0\le d\le D\) when \(D=o(m^{1/3})\); and
3. the dyadic native radii \(1,2,4,\ldots,D\) when
   \(D=o(\sqrt m)\).

For the second case the square sum is \(O(D^3)\); for the third it is
\(O(D^2)\).

This does not prove even fixed-window clipped RSCD: at clipped depth \(H\),
the top multiplicity is \(\gamma_H=N_H\sim W\), not \(c_H=O_H(W/m)\).

## 3. Exact reductions inside the clipped window

### Proposition 3.1 (fixed-depth top-bucket reduction)

For every fixed integer \(H\ge1\), uniformly over full SCDs,

\[
\widehat\Phi_H(\mathcal D)
=2H\,p_H^*(\mathcal D)+O_H(W/m).
\tag{3.1}
\]

Hence fixed-depth clipped RSCD is equivalent to finding a full SCD with
\(p_H^*=o(W)\).  At \(H=\lceil A\sqrt m\rceil\), the top class alone forces

\[
p_H^*=o(W/\sqrt m).
\tag{3.2}
\]

#### Proof

For \(d<H\), use singleton forests and Theorem 2.2:

\[
\sum_{d=0}^{H-1}2d\,p_d^*
\le\sum_{d=0}^{H-1}2d\,c_d=O_H(W/m).
\]

The remaining term is exactly \(2Hp_H^*\), proving (3.1).  Equation (3.2)
is immediate from nonnegativity.  \(\square\)

At \(H=0\), the corrected toll is identically zero.  The \(W\) middle masks
may simply be written as \(W\) one-entry words; no radius-zero reset overhead
exists.

### Proposition 3.2 (tail-count identity and dyadic checkpoints)

For any forest counts \(p_0,\ldots,p_H\), put

\[
P_q=\sum_{d=q}^Hp_d.
\]

Then

\[
\boxed{
\sum_{d=0}^H2d\,p_d=2\sum_{q=1}^HP_q.}
\tag{3.3}
\]

If \(H=2^J\) and

\[
D_H=\sum_{j=0}^J2^jP_{2^j},
\]

then

\[
\boxed{D_H\le\widehat\Phi_H\le2D_H.}
\tag{3.4}
\]

#### Proof

Expand \(2d=2\sum_{q=1}^d1\) and interchange the finite sums to get
(3.3).  Since \(P_q\) is decreasing, for \(j\ge1\),

\[
2\sum_{q=2^{j-1}+1}^{2^j}P_q
\ge2^jP_{2^j},
\]

and the \(j=0\) term is bounded by \(2P_1\).  Summing gives the left side
of (3.4).  Conversely, on
\(2^j\le q<2^{j+1}\),

\[
\sum_qP_q\le2^jP_{2^j}.
\]

Adding the terminal point \(q=H\) proves
\(2\sum_qP_q\le2D_H\).  \(\square\)

Thus a multiscale proof may target dyadic tail component counts without
losing more than a factor two.

### Proposition 3.3 (rotor clipping homomorphism)

For \(d>h\ge1\), define

\[
\begin{aligned}
\pi_{d,h}(L;z_1,\ldots,z_{2d};R)
=\big(&L+\{z_1,\ldots,z_{d-h}\};\\
&z_{d-h+1},\ldots,z_{d+h};\\
&R+\{z_{d+h+1},\ldots,z_{2d}\}\big).
\end{aligned}
\tag{3.5}
\]

Every directed radius-\(d\) rotor edge projects to a directed
radius-\(h\) rotor edge.  At \(h=0\) it projects to an ordinary Johnson
swap.  Consequently, for every full SCD \(\mathcal D\) and \(h\le H\),

\[
\boxed{
\widehat\Phi_h(\mathcal D)\le\widehat\Phi_H(\mathcal D).}
\tag{3.6}
\]

#### Proof

Let the radius-\(d\) edge use \(x\in L\), \(y\in R\).  In (3.5), the new
lower set is obtained from the old one by removing \(z_{d-h}\) and inserting
\(y\).  Its singleton word becomes

\[
z_{d-h},z_{d-h+1},\ldots,z_{d+h-1},
\]

and its residual set loses \(y\) and gains \(z_{d+h}\).  This is exactly
(1.5).  At \(h=0\), the projected center changes by
\(-z_d+y\), which is (1.6).

For (3.6), keep the forests below radius \(h\).  Project every path at each
radius \(d\ge h\) to radius \(h\) and take their union.  Different paths
refer to different SCD chains, so their projected vertices remain distinct.
The top radius-\(h\) class then has at most
\(\sum_{d=h}^Hp_d\) components.  Hence

\[
\widehat\Phi_h
\le\sum_{d<h}2d\,p_d+2h\sum_{d=h}^Hp_d
\le\sum_{d=0}^H2d\,p_d.
\]

Minimize over the forests.  \(\square\)

It follows that it suffices to prove \(\mathrm{RSCD}_A\) for dyadic values
of \(A\), or for one sequence \(A_m\to\infty\).  Rounding the window by one
rank changes none of these conclusions.

## 4. Fixed-depth rotor-cycle packing

This section proves a genuine low-reset integral packing.  Its failure to
complete to a full SCD is stated separately.

### Theorem 4.1 (near-spanning fixed-\(H\) rotor-cycle packing)

Fix \(H\ge1\).  For all sufficiently large \(m\), there is a family of
pairwise mask-disjoint saturated symmetric chains in the ranks
\(m-H,\ldots,m+H\) with the following properties.

1. The chosen chains split into \(t_m=o(W)\) directed radius-\(H\) rotor
   cycles.
2. The family contains the same number \(M_m\) of masks in every band rank,
   and
   \[
   W-M_m=o(W),\qquad N_q-M_m=o(W)\quad(1\le q\le H).
   \tag{4.1}
   \]
3. Cutting every rotor cycle once and appending every uncovered band mask as
   a one-entry word gives a central-band word of exact length
   \[
   W+2\sum_{q=1}^H(N_q-M_m)+2Ht_m=W+o(W).
   \tag{4.2}
   \]

#### Construction of one atom

Fix an integer \(\ell>H\).  Choose a middle set \(X\), distinct ordered
elements

\[
a_0,\ldots,a_{\ell-1}\in X,
\qquad
b_0,\ldots,b_{\ell-1}\notin X.
\]

Starting at \(X_0=X\), first perform

\[
a_0\to b_0,\ a_1\to b_1,\ldots,a_{\ell-1}\to b_{\ell-1},
\]

and then

\[
b_0\to a_0,\ b_1\to a_1,\ldots,b_{\ell-1}\to a_{\ell-1}.
\]

This is a cycle \(X_0,X_1,\ldots,X_{R-1}\) of distinct middle sets, where
\(R=2\ell\).  Let transition \(t\) remove \(r_t\) and insert \(s_t\), with
indices read modulo \(R\).  For \(0\le q\le H\), define

\[
L_{t,q}=\bigcap_{j=0}^qX_{t+j},
\qquad
U_{t,q}=\bigcup_{j=0}^qX_{t-j}.
\tag{4.3}
\]

Because every window of at most \(H<\ell\) transitions uses distinct active
pairs,

\[
|L_{t,q}|=m-q,
\qquad
|U_{t,q}|=m+q.
\]

Thus

\[
L_{t,H}\subset\cdots\subset L_{t,0}=X_t
\subset\cdots\subset U_{t,H}
\tag{4.4}
\]

is a saturated radius-\(H\) chain.

For fixed \(q\), the \(R\) lower masks \(L_{t,q}\) are distinct, and so are
the \(R\) upper masks \(U_{t,q}\).  Indeed, modulo \(\ell\), the set of
\(q\) active pair labels which have been erased, respectively doubled,
determines the start of the interval.  The two starts \(t\) and
\(t+\ell\) have the same pair-label interval but opposite orientations on
every untouched active pair; at least one such pair exists because
\(q<\ell\).  The centers are distinct by the same orientation description.
Therefore the \(R\) chains in (4.4) are pairwise mask-disjoint.

The labelled state of the chain at \(t\) is

\[
\omega_t=
\big(L_{t,H};
r_{t+H-1},r_{t+H-2},\ldots,r_{t-H};
[2m]\setminus U_{t,H}\big).
\tag{4.5}
\]

Take

\[
x=r_{t+H},\qquad y=s_t.
\]

Then \(x\in L_{t,H}\), \(y\notin U_{t,H}\), and direct substitution gives

\[
L_{t+1,H}=L_{t,H}-x+y.
\]

The singleton list in (4.5) shifts by inserting \(x\) at the front and
dropping \(r_{t-H}\), while the residual set loses \(y\) and gains
\(r_{t-H}\).  Hence \(\omega_t\to\omega_{t+1}\) is exactly a rotor edge.
The atom is therefore a directed \(R\)-state rotor cycle.

#### Hypergraph matching

Make a multi-hypergraph whose vertices are all masks in the \(2H+1\) band
ranks and whose hyperedges are the mask sets of all parameterized atoms.
It is

\[
k=2\ell(2H+1)
\]

uniform.  The exact number of parameterized atoms is

\[
E=W(m)_\ell^2.
\tag{4.6}
\]

Every atom contains \(R=2\ell\) vertices in each rank.  Coordinate
transitivity therefore gives degree

\[
d_q=\frac{ER}{N_q}
\tag{4.7}
\]

at rank \(m\pm q\).  Since \(H,\ell\) are fixed,

\[
\frac{N_q}{W}=1+O_H(1/m),
\]

so all degrees are \((1+o(1))D\), where

\[
D=R(m)_\ell^2=\Theta_{H,\ell}(m^{2\ell}).
\tag{4.8}
\]

For two distinct masks, fix their two positions inside an atom.  Every
coordinate outside the \(2\ell\)-element active support has the same
membership in every mask of the atom.  Hence any coordinate in the nonempty
symmetric difference of the two prescribed masks must occupy one of the
\(2\ell\) active positions.  Fixing that coordinate removes one free
\(\Theta(m)\) choice.  Summing over the bounded number of position pairs
gives maximum pair codegree

\[
O_{H,\ell}(m^{2\ell-1})=o(D).
\tag{4.9}
\]

Parallel parameterizations of one atom have bounded multiplicity for fixed
\(H,\ell\), so (4.9) remains valid for the multi-hypergraph.

We now use the standard fixed-uniformity Pippenger--Frankl--Rödl theorem:
an asymptotically regular \(k\)-uniform hypergraph with maximum pair
codegree \(o(D)\) has a matching leaving \(o(|V|)\) vertices uncovered.
Equations (4.7)--(4.9) verify its hypotheses.  The resulting matching covers
the same number \(M\) of masks in every rank; because the total leftover is
\(o(W)\), (4.1) follows.

For each fixed \(\ell\), the uncovered fraction tends to zero as
\(m\to\infty\).  Choose successive thresholds and let
\(\ell=\ell(m)\to\infty\) sufficiently slowly, always with \(\ell>H\).
This diagonal uses only fixed-uniformity instances of the theorem.  The
number of selected atoms is

\[
t_m=\frac{M_m}{2\ell(m)}=o(W).
\]

Cutting one \(R\)-state rotor cycle gives, by Lemma 1.1, exact length
\(R+2H\).  Thus the selected cycles use \(M_m+2Ht_m\) entries.  The number
of uncovered band masks is

\[
E_m=(W-M_m)+2\sum_{q=1}^H(N_q-M_m).
\]

Appending them individually gives

\[
M_m+2Ht_m+E_m
=W+2\sum_{q=1}^H(N_q-M_m)+2Ht_m,
\]

which is (4.2).  \(\square\)

### Exact completion gate for Theorem 4.1 -- UNPROVED

The following is the smallest missing statement in the fixed-depth packing
route.

> **Exact fixed-band absorption \(\mathrm{EFA}_H\).**  For fixed \(H\), one
> may choose the matching in Theorem 4.1 so that its selected chains can be
> completed, using the uncovered band masks, to a saturated symmetric-chain
> decomposition of the whole depth-\(H\) band.

If \(\mathrm{EFA}_H\) holds, cut the selected rotor cycles once and treat the
remaining \(N_H-M_m=o(W)\) top chains as singleton paths.  Then

\[
p_H^*\le t_m+N_H-M_m=o(W),
\]

and Proposition 3.1 proves fixed-depth clipped RSCD.

It is not enough to partition the leftover masks with correct rank counts.
The leftover masks must complete the selected chains to one common saturated
band SCD.  Once that is done, Theorem 1.2 extends it automatically to a full
SCD while preserving every band chain.

### Proposition 4.2 (rank counts do not imply completion)

In \(B_4\), at depth \(H=1\), the three disjoint chains

\[
\{2\}<\{1,2\}<\{1,2,3\},
\]

\[
\{3\}<\{1,3\}<\{1,3,4\},
\]

\[
\{4\}<\{1,4\}<\{1,2,4\}
\]

have a residual profile consisting of one radius-one chain and two middle
singletons, but they cannot be completed even to a band SCD.

#### Proof

The unused lower mask is \(\{1\}\), the unused upper mask is
\(\{2,3,4\}\), and the unused middle masks are

\[
\{2,3\},\ \{2,4\},\ \{3,4\}.
\]

Any chain joining \(\{1\}\) to \(\{2,3,4\}\) needs an unused middle mask
which contains \(1\), and none exists.  \(\square\)

## 5. A complete radius-one local invariant

The fixed-depth obstruction can be sharpened at \(H=1\).

Write a radius-one state as its chain triple

\[
C=(L,T,U),
\qquad |L|=m-1,\ |T|=m,\ |U|=m+1.
\]

### Theorem 5.1 (radius-one rotor criterion)

For two radius-one chain triples \(C=(L,T,U)\) and
\(C'=(L',T',U')\),

\[
C\longrightarrow C'
\]

is a directed rotor edge if and only if

\[
\boxed{
L=T\cap T',\qquad U'=T\cup T',}
\tag{5.1}
\]

and

\[
\boxed{
T'\setminus L'\subset L,
\qquad
(T'\setminus T)\cap U=\varnothing.}
\tag{5.2}
\]

#### Proof

Write \(T=L+z_1\), \(U=T+z_2\).  If the rotor edge uses
\(x\in L\), \(y\notin U\), its successor is

\[
(L-x+y;x,z_1;([2m]\setminus U)-y+z_2).
\]

Its center is \(T'=L+y\), its upper endpoint is \(U'=T+y\), and its new
first singleton is \(x\).  This gives (5.1),
\(T'\setminus L'=\{x\}\subset L\), and
\(T'\setminus T=\{y\}\) is disjoint from \(U\).

Conversely, (5.1) determines \(y=T'\setminus T\).  The first condition in
(5.2) determines \(x=T'\setminus L'\in L\), while the second gives
\(y\notin U\).  Substitution into (1.5) recovers \(C'\).  \(\square\)

### Corollary 5.2 (two-sided rainbow-shadow condition)

Let \(T_1,\ldots,T_s\) be the middle centers of a radius-one rotor path.
Then its internal lower labels are

\[
T_i\cap T_{i+1},
\]

and its internal upper labels are

\[
T_{i-1}\cup T_i.
\]

Every three consecutive centers form a directed Johnson two-geodesic: the
coordinate just inserted is not immediately removed, and the next inserted
coordinate lies outside the preceding two centers.

If a forest with \(p\) paths spans the \(N_1\) active centers of an exact
band SCD, its \(N_1-p\) internal edges must have pairwise distinct
intersections and pairwise distinct unions.  The missing lower masks must be
matched to legal terminal caps, the missing upper masks to legal initial
caps, and exactly

\[
c_0=W-N_1=\operatorname{Cat}_m
\]

middle centers remain inactive.

#### Proof

The formulas follow from (5.1).  Distinctness follows because every lower
and upper mask occurs once in an exact band SCD.  At a terminal center with
predecessor, its lower cap must contain the coordinate inserted on the last
edge, equivalently its deleted singleton must lie in the predecessor
intersection.  Dually, an initial upper cap must avoid the coordinate
inserted on its first outgoing edge.  These are exactly (5.2).  The inactive
count is \(W-N_1=c_0\).  \(\square\)

A useful sufficient *band* form is therefore a family of vertex-disjoint
directed two-geodesic cycles on \(N_1\) middle sets such that their edge
intersections biject the rank-\(m-1\) masks and their edge unions biject the
rank-\(m+1\) masks.  Taking outgoing intersections and incoming unions as
the chain endpoints gives an exact radius-one band SCD; the other
\(\operatorname{Cat}_m\) centers are singletons.  Few cycles give a low-reset
band word, and Theorem 1.2 automatically extends the band SCD to a full SCD.
Thus a construction with \(o(W)\) such cycles would prove the fixed-depth
\(H=1\) instance.

The invariant shows why Eulerianity of the center graph alone is
insufficient: it does not enforce the two simultaneous rainbow shadows, the
common active-center set, or the endpoint-cap Hall conditions.

## 6. Exact recursive one-layer lifting

The previous packing works horizontally at one depth.  The next theorem
describes exactly what is required to build a common SCD vertically through
successive depths.

Suppose an exact symmetric-chain decomposition of the band through depth
\(h\) has been constructed.  Its top class \(V_h\) has \(N_h\) states.  To
pass to depth \(h+1\), choose an active set

\[
A_h\subseteq V_h,
\qquad |A_h|=N_{h+1};
\tag{6.1}
\]

these chains continue, while the other \(c_h=N_h-N_{h+1}\) chains stop at
radius \(h\).

For

\[
v=(L_v;z_1(v),\ldots,z_{2h}(v);R_v),
\]

an extension is determined by

\[
\ell_v\in L_v,
\qquad u_v\in R_v,
\]

and has state

\[
\widetilde v=
\big(L_v-\ell_v;
\ell_v,z_1(v),\ldots,z_{2h}(v),u_v;
R_v-u_v\big).
\tag{6.2}
\]

### Theorem 6.1 (exact lift of one rotor edge)

Let \(h\ge1\), and let \(v\to w\) be a radius-\(h\) rotor edge using
\(x\in L_v\), \(y\in R_v\).  Then

\[
\widetilde v\longrightarrow\widetilde w
\]

is a radius-\(h+1\) rotor edge if and only if

\[
\boxed{
\ell_v=x,\qquad
u_w=z_{2h}(v),\qquad
\ell_w\ne y,\qquad
u_v\ne y.}
\tag{6.3}
\]

At \(h=0\), the second equality is replaced by \(u_w=x\); the other three
conditions retain their evident meanings.

#### Proof

Apply a radius-\(h+1\) rotor move to (6.2), removing a coordinate \(\xi\)
from \(L_v-\ell_v\) and inserting a coordinate \(Y\) from \(R_v-u_v\).
The successor singleton sequence is

\[
\xi,\ell_v,z_1(v),\ldots,z_{2h}(v).
\tag{6.4}
\]

Since

\[
w=(L_v-x+y;x,z_1(v),\ldots,z_{2h-1}(v);
R_v-y+z_{2h}(v)),
\]

the singleton sequence of \(\widetilde w\) is

\[
\ell_w,x,z_1(v),\ldots,z_{2h-1}(v),u_w.
\tag{6.5}
\]

Equating (6.4) and (6.5) gives

\[
\xi=\ell_w,qquad \ell_v=x,qquad u_w=z_{2h}(v).
\]

Equality of the lower sets then forces \(Y=y\).  The legality conditions
\(\xi\in L_v-x\) and \(Y\in R_v-u_v\) are respectively equivalent to
\(\ell_w\ne y\) and \(u_v\ne y\), because
\(\ell_w\in L_w=L_v-x+y\).  The residual sets then agree automatically.
This proves (6.3).

When \(h=0\), the old singleton word is empty.  Comparing the two new
singletons gives \(u_w=\ell_v=x\).  \(\square\)

The theorem converts the simultaneous extension problem into exact Hall
systems.

### Theorem 6.2 (constrained Hall characterization)

Let \(F\) be a directed path forest on the active set \(A_h\), after any
chosen edge deletions.  For each \(v\in A_h\), let
\(\mathcal L_v\subseteq L_v\) and \(\mathcal U_v\subseteq R_v\) consist of
the choices which satisfy all equalities and inequalities in (6.3) on the
retained incident edges.

There is a simultaneous integral one-layer extension which preserves every
edge of \(F\) if and only if both of the following bipartite graphs have a
perfect matching:

\[
v\sim L_v-\ell
\quad(\ell\in\mathcal L_v),
\tag{6.6}
\]

from \(A_h\) onto all rank-\((m-h-1)\) masks, and

\[
v\sim R_v-u
\quad(u\in\mathcal U_v),
\tag{6.7}
\]

from \(A_h\) onto all rank-\((m-h-1)\) masks.  The second matching labels
the complements of the new upper endpoints.

#### Proof

In any exact band SCD, the new lower endpoints of the continued chains must
be all rank-\((m-h-1)\) masks, once each.  By (6.2), these endpoints are
exactly \(L_v-\ell_v\), so the lower choices are equivalent to a perfect
matching in (6.6).  Similarly, the new upper endpoints have complements
\(R_v-u_v\), and exact coverage is equivalent to a perfect matching in
(6.7).

The edge constraints in Theorem 6.1 separate: all conditions on
\(\ell_v\) involve only the lower choice and all conditions on \(u_v\)
involve only the upper choice.  Thus any pair of the two perfect matchings
may be chosen simultaneously, and Theorem 6.1 then lifts every retained
edge.  Necessity is immediate from the same observations.  \(\square\)

Equivalently, the exact obstruction at one layer is the pair of Hall
deficiencies

\[
\max_{S\subseteq A_h}
\bigl(|S|-|N_{\mathcal L}(S)|\bigr)_+,
\qquad
\max_{S\subseteq A_h}
\bigl(|S|-|N_{\mathcal U}(S)|\bigr)_+.
\tag{6.8}
\]

This is an integer ownership condition.  Doubly stochastic or separate
depthwise solutions do not imply it.

### Theorem 6.3 (exact one-layer toll surgery)

Let \(F_h\) be a spanning directed path forest on \(V_h\), with \(p_h\)
components.  Color its vertices active or inactive.  Let

* \(b_A\) be the number of maximal active runs in \(F_h\);
* \(b_I\) be the number of maximal inactive runs; and
* \(s_h\) be the number of forest edges crossing between the two classes.

Delete \(k_h\) additional edges inside the active induced forest, and
suppose Theorem 6.2 then lifts every retained active edge.  The new forests
have

\[
p_h^{\mathrm{new}}=b_I,
\qquad
p_{h+1}=b_A+k_h,
\tag{6.9}
\]

and the exact corrected toll increment is

\[
\boxed{
\Delta\widehat\Phi_h
=2h\,s_h+2b_A+2(h+1)k_h.}
\tag{6.10}
\]

#### Proof

Along every old path, the active and inactive runs alternate.  Therefore

\[
b_A+b_I=p_h+s_h.
\tag{6.11}
\]

The inactive runs become the radius-\(h\) paths.  The active runs, after the
\(k_h\) additional cuts, become the lifted radius-\(h+1\) paths, proving
(6.9).  The old top contribution was \(2hp_h\); the new contribution is

\[
2hb_I+2(h+1)(b_A+k_h).
\]

Subtract \(2hp_h\) and use (6.11):

\[
\begin{aligned}
\Delta\widehat\Phi_h
&=2h(b_A+b_I-p_h)+2b_A+2(h+1)k_h\\
&=2h s_h+2b_A+2(h+1)k_h.
\end{aligned}
\]

This is (6.10).  \(\square\)

### Theorem 6.4 (global contiguous-block reset bound)

Use the audited exact odd-cut factor to partition the middle layer into

\[
B=\operatorname{Cat}_m=\frac{W}{m+1}
\tag{6.12}
\]

directed Johnson paths.  Concatenate the paths in any fixed order and assign
the clipped radius labels \(0,1,\ldots,H\) in globally contiguous blocks of
sizes

\[
c_0,c_1,\ldots,c_{H-1},N_H.
\]

Thus at stage \(h<H\), the active centers form one global suffix of size
\(N_{h+1}\).

Assume recursive lifts are carried out without merging previously separated
paths.  Let \(k_h\) be the new retained-edge deletions at layer \(h\), and

\[
K_H=\sum_{h=0}^{H-1}k_h.
\]

If both exact Hall matchings of Theorem 6.2 exist at every layer used, then
the resulting depth-\(H\) forest system satisfies

\[
\boxed{
\widehat\Phi_H
\le H(H-1)+2H(B+1)+2HK_H.}
\tag{6.13}
\]

#### Proof

A global suffix has at most one active/inactive boundary along all retained
edges, so

\[
s_h\le1.
\tag{6.14}
\]

All retained paths are subpaths of the original \(B\) paths, split only by
previous deletions and possibly by the single global boundary.  Hence

\[
b_{A,h}\le B+1+\sum_{i<h}k_i.
\tag{6.15}
\]

Starting from zero radius-zero toll, sum (6.10) for
\(0\le h<H\).  Equations (6.14)--(6.15) give

\[
\sum_{h=0}^{H-1}2h s_h\le H(H-1)
\]

and

\[
\sum_{h=0}^{H-1}2b_{A,h}
\le2H(B+1)+2\sum_{i=0}^{H-1}(H-1-i)k_i.
\]

Adding \(2\sum_{i=0}^{H-1}(i+1)k_i\) from the last term of (6.10) gives
coefficient \(2H\) on every \(k_i\).  This proves (6.13).  \(\square\)

The exact odd-cut input in (6.12) follows by cutting a known exact odd
wreath factor at its distinguished coordinate.  It is part of the audited
rotor baseline; no fractional factor is being invoked.

For \(H=\lceil A\sqrt m\rceil\),

\[
H(H-1)=O_A(m)=o(W)
\]

and

\[
2H(B+1)=O_A(W/\sqrt m)+O_A(\sqrt m)=o(W).
\]

Therefore only the deletion term remains at the critical scale.

### Exact constrained recursive lift lemma -- UNPROVED

> **\(\mathrm{CRHL}_A\).**  Let \(H=\lceil A\sqrt m\rceil\).  Starting
> from the odd-cut paths and the globally contiguous clipped-radius blocks in
> Theorem 6.4, there is a sequence of integral lower and upper choices which:
>
> 1. satisfies both perfect-matching systems (6.6)--(6.7) for every
>    \(0\le h<H\), and therefore constructs one saturated SCD of the
>    depth-\(H\) band;
> 2. preserves the inherited rotor edges below depth \(H\), except for new
>    deletions with
>    \[
>    K_H=o(W/H);
>    \tag{6.16}
>    \]
> 3. introduces no merger during these recursive lifts between paths already
>    separated at an earlier layer.

Theorem 1.2 then extends the completed depth-\(H\) band SCD to a full SCD
without altering its rotor paths.

### Corollary 6.5 (conditional RSCD)

If \(\mathrm{CRHL}_A\) holds, then \(\mathrm{RSCD}_A\) holds.

#### Proof

By (6.13) and (6.16),

\[
\widehat\Phi_H
\le O_A(m)+O_A(W/\sqrt m)+o(W)=o(W).
\]

The first clause gives one common saturated band SCD, and Theorem 1.2 extends
it to a full integral SCD without changing any band state.  Thus the estimate
is exactly (1.8), not a separate-depth statement.  \(\square\)

For completeness, the resulting central-band word has exact length

\[
W+\widehat\Phi_H=W+o(W),
\]

because the forest paths contain all \(W\) clipped chain states and Lemma 1.1
charges \(2d\) per component.  Combining this with the independently audited
outer-tail construction gives

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{\binom{2m}{m}}
\le 1+O\!\bigl((1+A^2)e^{-A^2}\bigr).
\tag{6.17}
\]

Here \(\nu(n)\) denotes the minimum contiguous-OR word length in dimension
\(n\).

Thus \(\mathrm{CRHL}_A\) for every fixed \(A\), followed by
\(A\to\infty\), yields coefficient one in even dimension; the audited
trimmed one-bit lift gives the odd dimensions.  Equation (6.17) is a
conditional use of the established outer-tail theorem, not a new tail proof
in this report.

Within this recursive architecture, \(\mathrm{CRHL}_A\) is the smallest
replacement lemma obtained: Theorems 6.1--6.4 prove all rotor compatibility
and reset estimates once the two integral Hall systems are solved with the
stated deletion budget.

## 7. Exact reconciliation of the two rotor resolutions

The recursive theorem attacks one SCD directly.  This section instead
freezes the two exact master resolutions:

1. the low-run pseudo-color resolution obtained from the odd-cut rotor
   forest; and
2. the complete coordinate orbit of a prescribed genuine SCD.

The remaining integral coloring problem has an exact packet formulation.

Fix one radius \(d\).  Declare every pseudo-forest path to be an open
hard-cut piece.  Group pieces with the same ordered state sequence

\[
P=(\omega_0,\ldots,\omega_{\ell(P)})
\]

into a packet of multiplicity \(k_P\).  At each position, the packet has a
\(k_P\)-element occurrence fiber, and consecutive fibers are joined by the
fixed pseudo-path bijection.  The fibers over all packet positions equal to
a state \(\omega\) partition all occurrences of \(\omega\).  If the
pseudo-forest has \(p_d^0\) paths per pseudo-color, then

\[
\sum_Pk_P=Q_mp_d^0.
\tag{7.1}
\]

Fix a labelled target resolution by genuine SCD colors \(c\), and put

\[
A_\omega=\{c:\omega\text{ belongs to the radius-}d
\text{ class of color }c\}.
\tag{7.2}
\]

State multiplicities in the two exact resolutions agree, so the number of
target colors in \(A_\omega\) equals the number of pseudo-occurrence slots
at \(\omega\).

A **palette field** is a family

\[
C_{P,i}\subseteq A_{\omega_i},
\qquad |C_{P,i}|=k_P,
\tag{7.3}
\]

such that, at every state \(\omega\), the palettes over all packet positions
equal to \(\omega\) partition \(A_\omega\).  Define

\[
V_d(C)=
\sum_P\sum_{i=0}^{\ell(P)-1}
\bigl(k_P-|C_{P,i}\cap C_{P,i+1}|\bigr),
\qquad
V_d^*=\min_CV_d(C).
\tag{7.4}
\]

### Theorem 7.1 (packet-palette theorem)

Assume the packet pieces are open paths and that the \(k_P\) copies may be
assigned target colors freely at each occurrence fiber.  Then:

1. the minimum possible number of target-color changes on internal packet
   edges is exactly \(V_d^*\);
2. after every copy of every pseudo path is declared a hard-cut piece, the
   exact number of monochromatic radius-\(d\) runs is
   \[
   \boxed{Q_mp_d^0+V_d^*;}
   \tag{7.5}
   \]
3. over all radii, the exact hard-reset prefix length is
   \[
   \boxed{
   Q_mW+\sum_{d=0}^H2d\bigl(Q_mp_d^0+V_d^*\bigr).}
   \tag{7.6}
   \]

#### Proof

Any integral recoloring induces the palettes of colors used on the packet
fibers.  Across the edge from position \(i\) to \(i+1\), at most
\(|C_{P,i}\cap C_{P,i+1}|\) colors can remain unchanged.  Thus every
recoloring has at least \(V_d(C)\) internal switches.

Conversely, fix a palette field.  On the first fiber of an open packet,
assign its \(k_P\) slots bijectively to \(C_{P,0}\).  Inductively, at the
next fiber retain every color in
\(C_{P,i}\cap C_{P,i+1}\) along its incoming copy edge, and biject the
remaining slots to the remaining colors of \(C_{P,i+1}\).  Because the path
is open, this creates no closing constraint, and it realizes exactly

\[
k_P-|C_{P,i}\cap C_{P,i+1}|
\]

switches on every internal edge simultaneously.  The statewise palette
partition makes the union of these assignments a bijection between slots
and the prescribed colors at every state.  Hence each final color is exactly
its prescribed integral SCD.

An open path copy with \(s\) switches has \(1+s\) monochromatic runs.  Sum
over the \(Q_mp_d^0\) hard-cut copies in (7.1) to obtain (7.5).  Every
clipped SCD has \(W\) chain states, giving baseline \(Q_mW\), and Lemma 1.1
charges exactly \(2d\) per hard run.  This proves (7.6).  \(\square\)

Equation (7.5) is exact for the declared hard-cut pieces.  It is not the
optimized run count in an Euler chronology where equal colors may merge
across packet boundaries.

For a target coordinate orbit of one SCD \(\mathcal D\), (7.5) also gives

\[
\boxed{
V_d^*\ge Q_m\bigl(p_d^*(\mathcal D)-p_d^0\bigr)_+.}
\tag{7.7}
\]

Indeed, the runs of each final color form a spanning directed path forest of
its radius-\(d\) class, so there are at least
\(Q_mp_d^*(\mathcal D)\) runs in total.

Thus the frozen two-resolution route is reduced exactly to

\[
\sum_{d=0}^H2d\,V_d^*=o(Q_mW),
\tag{7.8}
\]

because the audited pseudo-forest baseline already has
\(\sum_d2d\,p_d^0=o(W)\) on every fixed Gaussian window.  No proof of
(7.8) is obtained here.

### Theorem 7.2 (dual palette-moment obstruction)

Let \(f:\Omega_d\to\mathbb R\) satisfy

\[
\sum_{i=0}^{\ell(P)}f(\omega_i)=0
\tag{7.9}
\]

for every packet template \(P\).  Put

\[
F_{P,j}=\sum_{i=0}^jf(\omega_i),
\qquad
K_f=\max_{P,j}|F_{P,j}|,
\tag{7.10}
\]

and assume \(K_f>0\).  Then

\[
\boxed{
V_d^*\ge
\frac1{2K_f}
\sum_c
\left|
\sum_{\omega\in(\mathcal D_c)_d}f(\omega)
\right|.}
\tag{7.11}
\]

#### Proof

For a palette field, let

\[
x_{P,i,c}=1_{\{c\in C_{P,i}\}}.
\]

The statewise partition condition gives

\[
\sum_{P,i:\,\omega_i=\omega}x_{P,i,c}
=1_{\{\omega\in(\mathcal D_c)_d\}}.
\tag{7.12}
\]

Using (7.9), summation by parts on every open packet gives

\[
\sum_{\omega\in(\mathcal D_c)_d}f(\omega)
=\sum_P\sum_{j=0}^{\ell(P)-1}
F_{P,j}(x_{P,j,c}-x_{P,j+1,c}).
\tag{7.13}
\]

Take absolute values, sum over \(c\), and use

\[
\sum_c|x_{P,j,c}-x_{P,j+1,c}|
=2\bigl(k_P-|C_{P,j}\cap C_{P,j+1}|\bigr).
\tag{7.14}
\]

Then the left side of (7.11) is at most \(2K_fV_d(C)\).  Minimize over
palette fields.  \(\square\)

### Corollary 7.3 (representation-theoretic certificate)

Let

\[
M_{\mathrm{pseudo}}
=\operatorname{span}\{\sigma1_P:
P\text{ a packet template},\ \sigma\in S_{2m}\}.
\tag{7.15}
\]

Suppose an irreducible \(S_{2m}\)-submodule
\(U\subseteq M_{\mathrm{pseudo}}^\perp\) has dimension \(r_U\).  Let
\(f\in U\) be a unit vector, so it annihilates every packet path, and assume
\(K_f>0\).  For the coordinate orbit of a target radius-\(d\) class
\(D_d\), of size \(\gamma_d\),

\[
\boxed{
V_d^*\ge
\frac{(2m-1)(2m)!}{2K_f}
\frac{\|\operatorname{proj}_U1_{D_d}\|_2^2}
     {r_U\sqrt{\gamma_d}}.}
\tag{7.16}
\]

#### Proof

Schur orthogonality on the irreducible module \(U\) gives

\[
\sum_{\sigma\in S_{2m}}
|\langle f,\sigma1_{D_d}\rangle|^2
=\frac{(2m)!}{r_U}
\|\operatorname{proj}_U1_{D_d}\|_2^2.
\tag{7.17}
\]

Since \(\|f\|_2=1\),

\[
\max_\sigma|\langle f,\sigma1_{D_d}\rangle|
\le\sqrt{\gamma_d}.
\]

The inequality \(\|a\|_1\ge\|a\|_2^2/\|a\|_\infty\), the
\(2m-1\) labelled copies of every coordinate orbit, and Theorem 7.2 now give
(7.16).  \(\square\)

No irreducible module satisfying (7.15) and producing a scale-sharp nonzero
right side in (7.16) has been found.  Thus (7.16) is a valid obstruction
certificate, not a counterexample to RSCD.

### Proposition 7.4 (holonomy alone is not an obstruction)

For a \(k\)-sheet packet cycle with palettes
\(C_0,\ldots,C_{r-1}\), cut all \(k\) lifted edges at one seam \(j\).  The
remaining open paths can be colored with at most

\[
k+\sum_{i\ne j}
\bigl(k-|C_i\cap C_{i+1}|\bigr)
\tag{7.18}
\]

runs.  In particular, a constant palette needs exactly \(k\) runs,
regardless of the product of the transport permutations around the cycle.

#### Proof

After deleting the seam, inductively align common colors along every
remaining edge exactly as in Theorem 7.1.  There are \(k\) initial open
paths and the displayed number of internal switches.  With a constant
palette all \(k\) paths are monochromatic.  \(\square\)

Consequently parity, sign, or nontrivial permutation holonomy cannot by
itself force high reset cost.  Palette variation together with the
statewise partition constraint is the relevant obstruction.

## 8. Exact open ledger

The results above leave the following clean alternatives.

### Direct recursive gate

Prove \(\mathrm{CRHL}_A\): solve the two constrained integral Hall systems
through one saturated depth-\(H\) band SCD while deleting only \(o(W/H)\)
inherited edges below \(H=A\sqrt m\).  Theorems 6.1--6.4 give every rotor
and reset estimate, and Theorem 1.2 supplies the full SCD.

### Fixed-depth absorption gate

Prove \(\mathrm{EFA}_H\) for each fixed \(H\): choose the near-perfect
rotor-cycle packing so that the leftover masks complete it to a saturated
band SCD.  Theorem 1.2 then extends it.  This would prove the fixed-depth
version, but by itself gives no uniform control when \(H\asymp\sqrt m\).

### Frozen two-resolution gate

Construct packet palettes satisfying

\[
\sum_{d\le H}2d\,V_d^*=o(Q_mW).
\]

Theorem 7.2 supplies dual certificates against such a construction.  No
certificate of the required size and no low-variation palette construction
is proved.

The direct recursive gate is the most economical of these for the stated
task because it keeps exact common ownership at every layer and its sole
quantitative requirement is the scale-correct deletion budget
\(o(W/H)\).

## 9. Adversarial audit

The strongest claims were independently audited, and the following failure
tests were applied.

1. **Corrected toll.**  Every exact reset statement uses \(2d\), because a
   \(t\)-state open run has prefix length \(t+2d\).  The value \(2d+1\) is
   only a conservative canonical reset.  Physical master-circuit
   initialization is kept separate.  The fixed-band direct word in
   Theorem 4.1 does not need an abstract master-circuit initialization
   ledger.

2. **Native versus clipped radii.**  Theorem 2.2 uses multiplicity \(c_d\).
   It does not replace the clipped top multiplicity \(\gamma_H=N_H\).
   Therefore the dyadic native-radius corollary is not advertised as
   \(\mathrm{RSCD}_A\).

3. **Fixed \(H\) versus Gaussian \(H\).**  The Pippenger--Frankl--Rödl
   argument fixes \(H\) and \(\ell\) before taking \(m\to\infty\).  The slow
   diagonal lets \(\ell\to\infty\) only after fixed-parameter thresholds.
   It supplies no estimate uniform for \(H=A\sqrt m\).

4. **Packing versus band SCD.**  Theorem 4.1 is a partial band packing.
   Proposition 4.2 disproves the inference from small residual histograms to
   a saturated band completion.  Both \(\mathrm{EFA}_H\) and
   \(\mathrm{CRHL}_A\) explicitly demand one common band SCD; Theorem 1.2
   then gives the full SCD automatically.

5. **Hypergraph estimates.**  Each atom contains \(2\ell\) masks in every
   band rank.  Degrees are exactly \(ER/N_q\).  A distinct prescribed pair
   forces a fixed coordinate into the bounded active support, giving the
   required factor \(m^{-1}\) in codegree.  Fixed parallel multiplicities do
   not change \(o(D)\).  An independent audit found no missing factor in the
   construction or in the exact \(2H\)-per-cycle reset charge.

6. **Recursive lift.**  Direct comparison of the full singleton sequences
   verifies all four conditions in (6.3).  Lower and upper choices are
   independent only after every retained-edge equality and inequality has
   been inserted into \(\mathcal L_v,\mathcal U_v\).  The perfect matchings
   in (6.6)--(6.7), not fractional flows, enforce exact rank coverage.

7. **Global reset sum.**  The bound (6.13) requires globally contiguous
   clipped-radius blocks, persistent cuts, and no later mergers.  These are
   hypotheses, not automatic properties.  Under them, \(s_h\le1\), and a
   cut made at layer \(i\) contributes exactly \(2H\) to the summed upper
   bound: \(2(H-1-i)\) through later active-run counts and \(2(i+1)\) at its
   creation.

8. **Outer extension.**  The exact comparison-plus-identity matching in
   Theorem 1.2 proves that every saturated central-band SCD extends to a full
   SCD while preserving its band chains.  Thus no unproved outer-extension
   clause remains.  This theorem does not help a merely partial packing,
   which must first be completed inside the band.

9. **Radius-one invariant.**  Two-sided rainbow intersections and unions
   are necessary for the internal edges.  If they produce a complete
   saturated band SCD, Theorem 1.2 extends it automatically; the unresolved
   issue is constructing the two simultaneous rainbow resolutions.

10. **Packet exactness.**  The equality defining \(V_d^*\) requires open
    packets and free layerwise assignment of packet copies.  It need not hold
    on a cyclic packet with fixed copy identities.  The run formula (7.5)
    hard-cuts every packet copy; optional mergers across packet boundaries
    can only improve a separately optimized chronology.

11. **Dual normalization.**  The quantity \(K_f\) is the maximum *absolute*
    prefix sum and must be positive.  Formula (7.16) assumes
    \(\|f\|_2=1\), \(f\in U\subseteq M_{\mathrm{pseudo}}^\perp\), and hence
    path annihilation.  Nonzero target projection alone does not imply the
    existence of a useful path-annihilating isotype; that is a separate
    hypothesis.

12. **No conjectural overclaim.**  No low-deletion Hall solution, exact
    band absorber, or scale-sharp palette certificate is proved.  Accordingly,
    neither \(\mathrm{RSCD}_A\) nor the contiguous-OR conjecture is claimed.

Subject to these qualifications, all displayed estimates and exact
equivalences in this report are unconditional.  The only statements marked
UNPROVED are \(\mathrm{EFA}_H\) and \(\mathrm{CRHL}_A\); the palette target
(7.8) is explicitly an open optimization criterion rather than a lemma.
