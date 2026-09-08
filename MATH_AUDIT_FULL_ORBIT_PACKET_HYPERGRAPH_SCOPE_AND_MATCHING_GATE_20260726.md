# Full-orbit packet hypergraphs: scope correction, exact incidence, and the genuine matching gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, web input,
or crossed recursion is used.

## 0. Audited verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},\qquad
 p_q={N_q\over W}.                                      \tag{0.1}
\]

The proposed packet escape is real, but it is not yet an integral
rounding theorem.

1.  The literal orientation packet
    \[
      P(F,M)=\{F\cup S:S\text{ chooses one endpoint of each }e\in M\}
                                                               \tag{0.2}
    \]
    has the exact edge, degree, and owner-codegree census
    \[
    \begin{aligned}
      |\mathscr P_r|&={(2m)!\over2^rr!(m-r)!^2},\\
      D_r&=\binom mr^2r!,\\
      D_r(d)&=d!(r-d)!\binom{m-d}{r-d}^{\!2},\\
      {D_r(d)\over D_r}&={\binom rd\over\binom md^2}
                         \quad(0\le d\le r),             \tag{0.3}
    \end{aligned}
    \]
    and codegree zero for (d>r).

2.  Quota-marking the injective traces with density (p_q), taking the
    full (S_n)-orbit, and clearing denominators gives an exactly regular
    multipartite hypergraph: every middle owner and every mandatory
    signed-depth target has one common degree.  Its complete pair-codegree
    table is a finite Venn-census of the base packets; formula (4.7) below
    is exact.

3.  There is a small but important scope correction to the existing
    (J(4,2)) example.  Its three (Q_1)'s really are an integral
    mixed-frame partition and the union of their completed frames is
    (K_4).  Each (Q_1), however, is an affine face of a completed-frame
    status cell, not a whole status cell.  The example therefore refutes
    global-frame locking for the **arbitrary subcube packet model**, but
    it is not a counterexample to the complete-status-component theorem.

4.  For a whole (Q_r) owner packet, the exact mandatory
    owner--depth-(q)-target relative codegree is
    \[
       \boxed{{2^q\over\binom{m+q}{q}}}.                    \tag{0.4}
    \]
    For a single isometric (2r)-cycle packet, the corresponding exact
    number is
    \[
       \boxed{{q+1\over\binom{m+q}{q}}}.                    \tag{0.5}
    \]
    Thus the previously stated (q+1) bound is valid for a cube but is
    not sharp there.  Both models force (2/(m+1)) at (q=1).

5.  Consequently a generic growing-rank nibble is not justified.  A
    quota-marked (Q_r) column has rank
    \[
       K=(1+o(1))\,2^{r+1}\sqrt m
          \int_0^A e^{-x^2}\,dx                         \tag{0.6}
    \]
    on (H=A\sqrt m+o(\sqrt m)), whereas
    \(\Delta_2/D\ge2/(m+1)\).  Hence
    \[
                         K\Delta_2/D\to\infty            \tag{0.7}
    \]
    whenever (r\ge2H).  This closes only arguments whose hypotheses
    require this crude growing-rank parameter to vanish.  It does not
    prove that a chronologically correlated packet matching is impossible.

6.  The exact additional all-depth spread condition is not ordinary
    pairwise independence.  For an owner-disjoint packet law, its joined
    target-overlap kernels must satisfy the floor-covariance identity
    \[
    \sum_a\left[
      \sum_{P\ne P'}K_a(P,P')\Pr(P,P'\text{ selected})
      -2c_aS+N_ac_a(c_a+1)
    \right]=o(W),                                       \tag{0.8}
    \]
    where \(S\) is the covered owner mass,
    \(c_a=\lfloor S/N_a\rfloor\), and
    \(K_a(P,P')=|A_a(P)\cap A_a(P')|\).  The formula is
    proved as (7.13) below.  Together with \(W-S=o(W/H)\), this condition
    rigorously gives aggregate target leave \(o(W)\).  It demands a
    linear-order negative overlap covariance; an
    asymptotically independent packet law has floor energy
    \(\Theta(W)\) at a shallow depth.

The complete-quartet connected-component no-go therefore does **not**
apply to this finer hypermatching model.  It applies again only after one
adds the extra law that packet decisions must be constant on each common
status component.  No such law follows from owner disjointness or from the
valid local context-array factor.

## 1. Literal packets and their exact owner census

Fix (1\le r\le m).  Choose a full core

\[
                         F\subset[2m],\qquad |F|=m-r,        \tag{1.1}
\]

and an (r)-edge matching (M) disjoint from (F).  The unused set

\[
                         G=[2m]\setminus(F\cup V(M))         \tag{1.2}
\]

also has size (m-r).  Define (P(F,M)) by (0.2).  Its indicators are
fixed to one on (F), fixed to zero on (G), and have xor one on every
edge of (M).  Thus

\[
                         |P(F,M)|=2^r.                       \tag{1.3}
\]

Let \(\mathscr P_r\) contain every physical packet once.

### Theorem 1.1 (edge and degree census)

The first two formulae in (0.3) hold.

#### Proof

Choose (F), the (2r) active coordinates, and their perfect matching:

\[
\begin{aligned}
 |\mathscr P_r|
 &=\binom{2m}{m-r}\binom{m+r}{2r}{(2r)!\over2^rr!}\\
 &={(2m)!\over2^rr!(m-r)!^2}.                         \tag{1.4}
\end{aligned}
\]

For a fixed owner (X\in\binom{[2m]}m), choose the (r) active
endpoints in (X), the (r) active endpoints in (X^c), and a
bijection between them.  This gives

\[
                         D_r=\binom mr^2r!.                   \tag{1.5}
\]

The consistency identity

\[
                         |\mathscr P_r|2^r=WD_r              \tag{1.6}
\]

follows either algebraically or by counting owner--packet incidences.
\(\square\)

### Theorem 1.2 (Johnson-shell codegrees)

If owners (X,Y) have Johnson distance

\[
                         d=|X\setminus Y|=|Y\setminus X|,   \tag{1.7}
\]

then their codegree is (D_r(d)) in (0.3) for (d\le r), and zero for
(d>r).

#### Proof

Every point of (X\setminus Y) must be paired with one point of
(Y\setminus X), in (d!) ways.  Choose (r-d) further active selected
endpoints from (X\cap Y), (r-d) unselected endpoints from
([2m]\setminus(X\cup Y)), and biject them.  This gives

\[
 d!\binom{m-d}{r-d}^{\!2}(r-d)!.                         \tag{1.8}
\]

No packet can contain the pair when (d>r).  Division by (1.5) gives

\[
 {D_r(d)\over D_r}
 ={d!(r-d)!\over r!}
   \left({\binom{m-d}{r-d}\over\binom mr}\right)^2
 ={\binom rd\over\binom md^2}.                         \tag{1.9}
\]

This proves the theorem. \(\square\)

The ratio of consecutive nontrivial expressions is

\[
 {D_r(d+1)/D_r\over D_r(d)/D_r}
 ={(d+1)(r-d)\over(m-d)^2}.                              \tag{1.10}
\]

Hence, if (r=o(m)), the largest owner codegree occurs at (d=1) and

\[
                         {\Delta_{OO}\over D_r}={r\over m^2}. \tag{1.11}
\]

## 2. The (J(4,2)) mosaic and its exact scope

Take (m=2,r=1).  The three packets

\[
\begin{aligned}
 P_1&=P(\{1\},\{23\})=\{12,13\},\\
 P_2&=P(\{4\},\{12\})=\{14,24\},\\
 P_3&=P(\{3\},\{24\})=\{23,34\}                       \tag{2.1}
\end{aligned}
\]

are pairwise disjoint and partition all six vertices of (J(4,2)).
Complete their active pairs to the perfect matchings

\[
 \widehat M_1=23|14,\qquad
 \widehat M_2=12|34,\qquad
 \widehat M_3=24|13.                                    \tag{2.2}
\]

Their union contains all six edges of (K_4), hence is connected.

The exact status-cell point is the following.  Relative to
\(\widehat M_1\), the packet (P_1) lets the orientation on edge (23)
vary but fixes the orientation on edge (14) to endpoint (1).  The
whole status cell with both edges split has four owners, not two.  Thus
(P_1) is an affine (Q_1)-face of that (Q_2)-status cell.  The same
holds cyclically for (P_2,P_3).

Therefore (2.1) proves exactly

\[
 \boxed{
 \text{connected union of completed frames does not lock an arbitrary
 subcube packet matching to one frame}.}                  \tag{2.3}
\]

It does not contradict the theorem that a whole-shore recoupling on the
single common status component chooses one global shore.  Moreover,
(r=1) carries no positive protected range under a gate such as
(H\le r/2); (2.1) is an ownership-scope counterexample, not an
all-depth construction.

## 3. Integral quota markings

Let

\[
                         \mathcal I
 =\{(q,\epsilon):1\le q\le H,\ \epsilon\in\{-,+\}\}.       \tag{3.1}
\]

A packet type \(\alpha\) has an owner cube (P_\alpha), of size
(B_\alpha=2^{r_\alpha}), and injective trace maps

\[
 \tau_{\alpha,a}:P_\alpha\longrightarrow
 \mathcal T_a=\binom{[n]}{m+\epsilon q}
 \qquad(a=(q,\epsilon)).                                  \tag{3.2}
\]

The same local factor supplies all maps in (3.2).

### Lemma 3.1 (exact integral quota menu)

There is a finite multiset of (M_\alpha) joint all-depth markings

\[
                         A_{\alpha,a}^\mu\subseteq P_\alpha \tag{3.3}
\]

such that

\[
 |A_{\alpha,a}^\mu|
 \in\{\lfloor B_\alpha p_q\rfloor,
       \lceil B_\alpha p_q\rceil\},                         \tag{3.4}
\]

and every (x\in P_\alpha) belongs to exactly
(M_\alpha p_q) of the (a)-marking sets.

#### Proof

Put (b=\lfloor B_\alpha p_q\rfloor) and
\(\theta=B_\alpha p_q-b\).  Under the uniform distribution on the
(b)-subsets of (P_\alpha), every point has marginal (b/B_\alpha);
under the uniform distribution on the ((b+1))-subsets it has marginal
((b+1)/B_\alpha).  Mix these two laws with weights (1-\theta,\theta).
Every point then has marginal (p_q), and (3.4) holds.

All numbers are rational because (p_q=N_q/W).  Take the Cartesian
product of these laws over the finitely many (a\in\mathcal I), and
multiply by a common denominator.  The resulting integral multiset has
the asserted one-point counts simultaneously at every signed depth.
\(\square\)

The markings are certificates.  Every unmarked physical trace remains in
the exact factor and can only help; it is not consumed as a matching
resource.

## 4. Exact orbit regularity and every pair codegree

The resource classes are

\[
 \mathcal V_0=\binom{[n]}m,\qquad
 \mathcal V_a=\{a\}\times\mathcal T_a.                    \tag{4.1}
\]

For (g\in S_n), a packet type \(\alpha\), and a joint marking \(\mu\),
make the indexed hyperedge

\[
 E(\alpha,\mu,g)
 =gP_\alpha\ \dot\cup\!
   \bigdotcup_{a\in\mathcal I}
   \{(a,g\tau_{\alpha,a}(x)):x\in A_{\alpha,a}^\mu\}.
                                                               \tag{4.2}
\]

Put

\[
                         \mathcal B
 =\sum_\alpha M_\alpha B_\alpha.                         \tag{4.3}
\]

### Theorem 4.1 (common degree and Venn codegrees)

Every genuine resource vertex has common indexed degree

\[
                         D=(m!)^2\mathcal B.                 \tag{4.4}
\]

Let (u,v) have resource types (a,b), underlying ranks (r_a,r_b),
and underlying intersection size (t).  Let (I_{ab}(t)) be the number,
summed over the base packet types and their integral joint markings, of
ordered pairs of distinct claimed base resources of types (a,b) with
intersection (t).  Then

\[
 \boxed{
 d(u,v)=I_{ab}(t)\,
 t!(r_a-t)!(r_b-t)!(n-r_a-r_b+t)! .}                    \tag{4.5}
\]

Equivalently, if

\[
 \mathcal O_{r,s,t}
 ={n!\over t!(r-t)!(s-t)!(n-r-s+t)!},                    \tag{4.6}
\]

then

\[
 \boxed{{d(u,v)\over D}
 ={W I_{ab}(t)\over\mathcal B\mathcal O_{r_a,r_b,t}}.}   \tag{4.7}
\]

#### Proof

A fixed base owner maps to a prescribed middle owner under exactly
((m!)^2=n!/W) permutations.  Type \(\alpha\) supplies
(M_\alpha B_\alpha) marked base-owner occurrences.

A fixed target at signed depth (q) has stabilizer order
((m-q)!(m+q)!=n!/N_q).  Type \(\alpha\) supplies
(M_\alpha B_\alpha p_q) accepted base-target occurrences.  Since

\[
 p_q{n!\over N_q}={n!\over W}=(m!)^2,                    \tag{4.8}
\]

its contribution to the target degree equals its owner contribution.
Summing proves (4.4).

For the pair claim, the four Venn regions have sizes

\[
                         t,\ r_a-t,\ r_b-t,\ n-r_a-r_b+t. \tag{4.9}
\]

Every base pair in this orbit has exactly the product of the factorials
in (4.5) coordinate permutations taking it to ((u,v)).  Summing over
(I_{ab}(t)) proves (4.5).  Since that factorial product is
(n!/\mathcal O_{r_a,r_b,t}), division by
(D=\mathcal Bn!/W) proves (4.7). \(\square\)

Formula (4.7), rather than owner codegree alone, is the exact cross-depth
target census.  It retains every chronology-dependent intersection class
of the local factor.

## 5. Exact owner--target endpoint codegrees

Fix one accepted lower depth-(q) target (T) of a whole orientation
cube.  Its affine (q)-face fixes the orientations on (r-q) active
pairs and leaves (q) orientations free.  Exactly (2^q) owners of the
whole cube contain (T).  No other cube owner contains it.  Dually,
exactly (2^q) cube owners lie inside the corresponding upper target.

The full coordinate group is transitive on nested pairs

\[
 T\subset X,\quad |T|=m-q,\ |X|=m,                         \tag{5.1}
\]

and there are

\[
                         \binom{m+q}{q}                     \tag{5.2}
\]

middle supersets (X) of a fixed (T).  Since the target degree is
exactly (D), double counting the incidences ((E,T,X)) gives

\[
 \boxed{{d(T,X)\over D}={2^q\over\binom{m+q}{q}}}          \tag{5.3}
\]

for every nested pair.  Complementation gives the upper formula.

For a single cyclic strip packet

\[
 X_t=K\cup I_z(t,r),\qquad t\in\mathbb Z/(2r),             \tag{5.4}
\]

the lower target is (K\cup I_z(t+q,r-q)).  Exactly (q+1) cyclic
length-(r) intervals contain this fixed length-((r-q)) interval.
Similarly, exactly (q+1) length-(r) intervals lie in an upper
length-((r+q)) interval.  The same orbit double count gives

\[
                         {d(T,X)\over D}
 ={q+1\over\binom{m+q}{q}}.                              \tag{5.5}
\]

In both cases (q=1) yields

\[
                         {d(T,X)\over D}={2\over m+1}.       \tag{5.6}
\]

This incidence is forced by literal output, independent of how frames are
mixed.

## 6. What the codegree calculation does and does not prove

At (q\le A\sqrt m), uniformly for fixed (A),

\[
 \log p_q=-{q^2\over m}
 +O_A\left({q\over m}+{q^3\over m^2}\right),               \tag{6.1}
\]

and therefore

\[
 \sum_{q=1}^{A\sqrt m+o(\sqrt m)}p_q
 =(1+o(1))\sqrt m\int_0^Ae^{-x^2}\,dx.                    \tag{6.2}
\]

For a (Q_r) packet, (B=2^r).  The quota edge has average size

\[
 B\left(1+2\sum_{q\le H}p_q\right).                       \tag{6.3}
\]

Its floor/ceiling error is at most (2H), which is
(o(B\sqrt m)) in the intended growing packet range.  Equations
(6.2)--(6.3) prove (0.6).  Combining with (5.6) gives (0.7); already the
weaker bounds (K\ge2^r), (r\ge2H), and (H=A\sqrt m) suffice.

For each fixed uniformity (K), a near-regular hypergraph with sufficiently
small relative pair codegrees lies in the classical nibble regime.  That
statement has no uniform content when (K=K_m\to\infty) unless the
dependence on (K) is supplied.  In particular, arguments which estimate
the second-order conflict correction by (K^2\Delta_2) against a
first-order scale (KD) require

\[
                         K\Delta_2/D=o(1),                    \tag{6.4}
\]

and (0.7) disproves their hypothesis here.

Nothing in this calculation proves a Hall cut or matching nonexistence.
The endpoint incidences belong to one chronological face and may be
handled collectively by a structure-sensitive algorithm.  The precise
conclusion is only that an unquantified invocation of a fixed-rank
small-codegree theorem is invalid.

## 7. Two exact sufficient integral gates

### 7.1 Mandatory-slot matching

Let \(\mathcal M\) be a matching in (4.2), and let

\[
 L_0=\left|\mathcal V_0\setminus\bigcup_{E\in\mathcal M}E\right|,
 \qquad
 L_T=\sum_{a\in\mathcal I}
 \left|\mathcal V_a\setminus\bigcup_{E\in\mathcal M}E\right|. \tag{7.1}
\]

Then the selected packet owners are disjoint and every covered target
vertex has a literal occurrence.  Quarantining one uncovered owner can
forfeit at most one occurrence at each of the (2H) signed depths.
Consequently the total charged loss is at most

\[
                         L_T+2HL_0.                           \tag{7.2}
\]

Thus

\[
                         L_0=o(W/H),\qquad L_T=o(W)           \tag{7.3}
\]

is sufficient.  A stronger classwise leave bound (eta_m) is sufficient
when (eta_mH\to0).

### 7.2 Floor-balanced joined-owner spread

There is a less restrictive formulation which allows the unavoidable
surplus outputs to collide.  Let an owner-disjoint packet family cover
exactly (S=W-L) owners.  At resource type (a), let
(A_a(P)) be the distinct target set of packet (P), and put

\[
 Z_a(T)=\#\{P:T\in A_a(P)\},\qquad
 c_a=\left\lfloor{S\over N_a}\right\rfloor.               \tag{7.4}
\]

Define the floor energy

\[
 Q_a=\sum_T(Z_a(T)-c_a)(Z_a(T)-c_a-1).                     \tag{7.5}
\]

Every summand is the product of two consecutive integers, hence is
nonnegative.

### Theorem 7.1 (exact floor-energy cover bound)

If (M_a=\#\{T:Z_a(T)=0\}), then

\[
 \boxed{
 M_a\le(N_a-S)_++{Q_a\over2}.}                            \tag{7.6}
\]

Consequently

\[
 \boxed{
 2HL+{1\over2}\sum_aQ_a=o(W)}                             \tag{7.7}
\]

implies aggregate all-depth target leave (o(W)).

#### Proof

If (c_a\ge1), every hole contributes
(c_a(c_a+1)\ge2) to (Q_a), while every other summand is nonnegative.
Thus (M_a\le Q_a/2).

If (c_a=0), then

\[
 M_a=N_a-S+\sum_T(Z_a(T)-1)_+.                            \tag{7.8}
\]

For every integer (z\ge1), (z(z-1)/2\ge z-1).  Hence the last sum
in (7.8) is at most (Q_a/2), proving (7.6).

Since (S=W-L) and (N_a\le W), one has
((N_a-S)_+\le L).  There are (2H) resource types.  Summing (7.6)
proves (7.7). \(\square\)

Now define the target-overlap kernel

\[
                         K_a(P,P')=|A_a(P)\cap A_a(P')|.     \tag{7.9}
\]

Because every packet is internally trace-injective,

\[
 \boxed{
 Q_a=
 \sum_{P\ne P'}K_a(P,P')
 -2c_aS+N_ac_a(c_a+1),}                                  \tag{7.10}
\]

where the packet-pair sum is ordered.  Indeed,

\[
 \sum_TZ_a(T)(Z_a(T)-1)
 =\sum_{P\ne P'}|A_a(P)\cap A_a(P')|,                    \tag{7.11}
\]

and expansion of (7.5), using (sum_TZ_a(T)=S), gives
(7.10).

Suppose now that a probability law is supported on owner-disjoint packet
families with the same covered mass (S), and write

\[
                         \pi_{P,P'}=\Pr(P,P'\text{ selected}). \tag{7.12}
\]

Taking expectations in (7.10) shows that the exact sufficient
cross-depth spread condition is

\[
 \boxed{
 \sum_a\left[
   \sum_{P\ne P'}K_a(P,P')\pi_{P,P'}
   -2c_aS+N_ac_a(c_a+1)
 \right]=o(W).}                                         \tag{7.13}
\]

The bracket is (mathbb E Q_a\ge0), so no cancellation between depths
is hidden.  If (HL=o(W)), (7.13) and the probabilistic method give one
deterministic family satisfying (7.7).

This is stronger and more precise than pairwise pseudorandomness of packet
selection.  At a symmetric independent-scale law with target mean
(\lambda=c+\theta), (0\le\theta<1), the factorial second moment is
approximately (lambda^2), so (7.5) has expectation

\[
                         N(c+\theta^2)+o(W)=\Theta(W)          \tag{7.14}
\]

at a shallow depth (up to the negligible diagonal correction of the
finite packet degree).  Successful rounding must create a negative
target-overlap covariance of this same linear order.

## 8. Exact relationship to the complete-quartet no-go

The complete-quartet theorem studies a different integral variable.  One
starts with complete frame partitions and switches whole shores on common
owner-overlap components.  If the coordinate union graph is connected,
there is one such component, so the variable chooses one global frame.

The packet hypergraph starts instead with individual subcubes or cycles.
Its sole owner constraint is physical disjointness of the chosen owner
sets.  Unused cells of a frame need not be selected.  The partition (2.1)
shows that this distinction persists even when the union of the completed
frames is connected.

Accordingly:

* the connected-component/global-frame conclusion does not apply to the
  finer packet matching;
* the fixed-frame Gaussian pair-type Hall cut does not apply unless one
  first proves that almost all selected packets share one ambient frame;
* the component no-go returns if an additional completion law forces every
  packet decision to be constant on the generated status component.

No such completion law is presently proved.  Conversely, neither exact
orbit regularity nor the (J(4,2)) mosaic proves the all-depth packet
matching.  The precise open positive statement is (7.3), or equivalently
the more flexible floor-covariance gate (7.7)--(7.13).

## 9. Proved boundary

The audit proves the following.

1.  The packet counts (0.3) are correct, including all indexing-free
    normalizations.
2.  The quota construction is integral and the full orbit is exactly
    regular on owners and every mandatory target class.
3.  Formula (4.7) gives every mixed owner/target and cross-depth target
    codegree exactly from the local Venn census.
4.  The exact cube endpoint coefficient is (0.4); the exact cyclic-strip
    coefficient is (0.5).
5.  The (J(4,2)) example is valid precisely as a subcube mosaic, not as a
    mosaic of whole status cells.
6.  The complete-quartet global-frame no-go does not extend to arbitrary
    owner-disjoint packets.
7.  A conventional growing-rank low-codegree nibble is not licensed, and
    the exact positive replacement is the joined floor-covariance
    condition (7.13) with owner leave (o(W/H)).

What remains open is whether the valid recursive packet library admits
that negative-covariance owner matching.  Thus this finer architecture is
a genuine escape from the previous obstruction, not a completed
coefficient-one proof.
