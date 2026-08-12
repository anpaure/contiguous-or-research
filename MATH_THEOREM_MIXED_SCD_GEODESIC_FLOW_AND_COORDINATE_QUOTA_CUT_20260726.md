# Mixed-SCD geodesic strata: exact flow rounding and the coordinate-quota cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Result and scope

Let \(A\mathbin{\dot\cup}B\) be two coordinate halves of size \(m\). Fix

\[
 h=m-2r>0,\qquad N_r=\binom mr^2.                              \tag{0.1}
\]

Consider the complete set of monotone cross-half Johnson paths of length
\(h\) from status \(r\) to status \(m-r\). The full independently labelled
coordinate-conjugacy orbit of any product SCD contains every such path.

For the endpoint-linkage objective on this complete fixed-radius path set,
there is no integral rounding gap. It is the source-to-sink path set of a
layered directed network. A uniform fractional flow of value \(N_r\)
respects every physical-owner capacity, and integral max flow gives
exactly \(N_r\) owner-disjoint paths, covering both endpoint layers.

This \(N_r\)-path family is a complete fixed-radius geodesic flow, not the
exact-radius stratum of one product-SCD factor. In one product-SCD factor,
the number of paths of exact length \(h=m-2r\) is

\[
 P_h=N_r-N_{r-1}
     =\binom mr^2-\binom m{r-1}^2.                             \tag{0.2}
\]

Here \(N_{-1}=0\) when \(r=0\).

Longer product paths already occupy \(N_{r-1}\) owners in every layer of
the radius-\(r\) slab. Selecting the correct \(P_h\) paths in their
complement, simultaneously for all radii, is a separate cross-radius
problem. Thus the theorem below is not called a global SCD atlas.

The complete orbit incidence is quantitatively sparse. At phase \(t\), its
path degree is

\[
 D_t=\left((r+t)_t(r+h-t)_{h-t}\right)^2.                      \tag{0.3}
\]

Two compatible owners at phases \(s<t\), with \(d=t-s\), have codegree

\[
 \lambda_{s,t}
 =\left((r+s)_s\,d!\,(r+h-t)_{h-t}\right)^2.                  \tag{0.4}
\]

Consequently

\[
 \frac{\lambda_{s,t}}{D_s}
   =\binom{r+h-s}{d}^{-2},
 \qquad
 \frac{\lambda_{s,t}}{D_t}
   =\binom{r+t}{d}^{-2}.                                      \tag{0.5}
\]

Every nonzero pair codegree is therefore at most \(1/(r+1)^2\) of
the degree at either endpoint. At \(r=m/2-O(\sqrt m)\), this is
\(O(m^{-2})\).

There is nevertheless an exact dynamic transport quota. Every integral
packing which misses \(\ell_0\) low endpoints and \(\ell_h\) high
endpoints uses each coordinate \(z\in A\) as an insertion direction
\(n_z\) times, where

\[
 \left|n_z-\frac hmN_r\right|\le \ell_0+\ell_h.                \tag{0.6}
\]

The analogous identity holds for every removal coordinate in \(B\).
Hence a coefficient-scale packing with
\(\ell_0+\ell_h=o(N_r/H)\) must realize all \(2m\) direction quotas to
additive \(o(N_r/H)\).

This requirement is sharp. If one common \(A\)-coordinate is forbidden
on every path, then the exact maximum packing size is

\[
 \boxed{\left(1-\frac hm\right)N_r}.                            \tag{0.7}
\]

Thus at least \((h/m)N_r\) endpoint owners are left. For
\(h=C\sqrt m\) and \(H=\sqrt m\log\log m\), this exceeds \(N_r/H\)
by the factor \(C\log\log m\).

Relative to the natural exact-radius count, the same deficit is
macroscopic. Indeed,

\[
 \frac{P_h}{N_r}
 =1-\left(\frac r{m-r+1}\right)^2
 =\frac{(h+1)(m+1)}{(m-r+1)^2}
 =\left(4+o(1)\right)\frac hm                              \tag{0.8}
\]

when \(h\to\infty\) and \(h=o(m)\). Thus \((h/m)N_r\) is
\((1/4+o(1))P_h\) in the Gaussian range.

More generally, for common forbidden sets \(F_A\subseteq A\) and
\(F_B\subseteq B\), Section 4 gives the exact maximum packing. Common
arc-local filters therefore round exactly. The unresolved dynamic case
has owner/history-dependent forbidden sets. It is not closed under path
splicing, so it is not the path set of one network. Separate
history-option biregularity does not enforce the simultaneous quotas
(0.6).

## 1. The complete fixed-radius path set

For \(0\le t\le h\), let

\[
 \mathcal V_t
 =\left\{S\mathbin{\dot\cup}T:
       S\subseteq A,\ |S|=r+t,\ 
       T\subseteq B,\ |T|=m-r-t\right\}.                       \tag{1.1}
\]

Then

\[
 |\mathcal V_t|=\binom m{r+t}^2.                               \tag{1.2}
\]

Join \(X=S\mathbin{\dot\cup}T\in\mathcal V_t\) to

\[
 X'=(S\cup\{a\})\mathbin{\dot\cup}(T\setminus\{b\})
       \in\mathcal V_{t+1}                                    \tag{1.3}
\]

for \(a\in A\setminus S\) and \(b\in T\). A directed path from
\(\mathcal V_0\) to \(\mathcal V_h\) is uniquely specified by a low
owner \(S_0\mathbin{\dot\cup}T_0\), an ordered \(h\)-tuple of distinct
elements of \(A\setminus S_0\), and an ordered \(h\)-tuple of distinct
elements of \(T_0\). Its vertices are

\[
 X_t=
 \left(S_0\cup\{a_1,\ldots,a_t\}\right)
 \mathbin{\dot\cup}
 \left(T_0\setminus\{b_1,\ldots,b_t\}\right).                  \tag{1.4}
\]

### Lemma 1.1 (the full orbit contains every path)

Let \(\mathscr D_A,\mathscr D_B\) be arbitrary SCDs of the two
\(m\)-cubes, retaining conjugating permutations as labels. The independent
orbit under \(\mathfrak S_A\times\mathfrak S_B\) contains every path
(1.4).

#### Proof

Every SCD of \(B_m\) has

\[
 \binom mr-\binom m{r-1}>0
\]

chains of minimum rank \(r\). Such a chain is specified by an ordered
partition into its bottom \(r\)-set, its ordered active word of length
\(h\), and its outside \(r\)-set. The symmetric group is transitive on
these ordered partitions. Hence the orbit contains the saturated chain

\[
 S_0\subset S_0+a_1\subset\cdots
       \subset S_0+\{a_1,\ldots,a_h\}.
\]

The same argument in \(B\), traversed backwards, realizes the ordered
removals \(b_1,\ldots,b_h\). Their rank-\(m\) product diagonal is (1.4).
\(\square\)

Different labelled colours may realize the same physical path. The lemma
asserts only, and exactly, that every physical path in the complete
fixed-radius network is a legal product-SCD occurrence somewhere in the
full orbit.

## 2. Exact degrees and codegrees

Write \((u)_v=u(u-1)\cdots(u-v+1)\).

### Theorem 2.1 (degree census)

Every owner \(X\in\mathcal V_t\) lies on exactly \(D_t\) directed paths,
where \(D_t\) is (0.3). The total number of directed paths is

\[
 |\mathcal P_h|
 =|\mathcal V_t|D_t
 =\left(\frac{m!}{(r!)^2}\right)^2,                            \tag{2.1}
\]

independently of \(t\).

#### Proof

At phase \(t\), the already inserted \(A\)-labels are an ordered
\(t\)-tuple from the \(r+t\) present \(A\)-coordinates. The future
insertions are an ordered \((h-t)\)-tuple from the \(r+h-t\) absent
\(A\)-coordinates. This gives

\[
 (r+t)_t(r+h-t)_{h-t}                                         \tag{2.2}
\]

possibilities in \(A\). The already removed and future removed
\(B\)-labels give the same factor. Squaring proves (0.3).

Finally,

\[
 \binom m{r+t}(r+t)_t(r+h-t)_{h-t}
 =\frac{m!}{(r!)^2}.                                          \tag{2.3}
\]

Multiplication by (1.2) proves (2.1). \(\square\)

### Theorem 2.2 (pair-codegree census)

Take \(X\in\mathcal V_s\) and \(Y\in\mathcal V_t\), where \(s<t\) and
\(d=t-s\). Their codegree is zero unless

\[
 S_X\subset S_Y,\qquad T_Y\subset T_X.                        \tag{2.4}
\]

When (2.4) holds, their codegree is (0.4), and the relative identities
(0.5) hold.

#### Proof

A monotone path can contain \(X\) before \(Y\) only under (2.4). Under
that condition, the \(d\) labels in \(S_Y\setminus S_X\) may be ordered
in \(d!\) ways, as may the \(d\) labels in \(T_X\setminus T_Y\).
Before \(X\), each half contributes \((r+s)_s\) choices. After \(Y\),
each half contributes \((r+h-t)_{h-t}\) choices. This proves (0.4).

Moreover,

\[
 \frac{d!(r+h-t)_{h-t}}{(r+h-s)_{h-s}}
 =\binom{r+h-s}{d}^{-1},                                     \tag{2.5}
\]

and

\[
 \frac{(r+s)_s d!}{(r+t)_t}
 =\binom{r+t}{d}^{-1}.                                       \tag{2.6}
\]

Dividing by (0.3) at phases \(s\) and \(t\) proves (0.5).
\(\square\)

In particular,

\[
 \lambda(X,Y)\le
 \frac{\min(D_s,D_t)}{(r+1)^2}.                               \tag{2.7}
\]

Thus the fixed-radius orbit is in a favourable pair-codegree regime.
Indeed, with path size \(k=h+1\),

\[
 k\,\frac{\lambda(X,Y)}{\min(D_s,D_t)}
 \le \frac{h+1}{(r+1)^2}
 =m^{-3/2+o(1)}                                               \tag{2.8}
\]

through the Gaussian range \(h=m^{1/2+o(1)}\).
The exact integral theorem below is stronger than a generic
growing-uniformity nibble for this unfiltered stratum.

## 3. Exact integral flow rounding

Split every owner vertex into an entrance and exit joined by a
capacity-one arc. Retain the arcs (1.3) between consecutive layers, and
add a supersource adjacent to \(\mathcal V_0\) and a supersink adjacent
from \(\mathcal V_h\). All source, sink, and owner capacities are one.

### Theorem 3.1 (integral fixed-radius geodesic flow)

The network has a flow of value \(N_r\). Consequently it has an integral
flow of value \(N_r\), which decomposes into exactly \(N_r\) pairwise
owner-disjoint paths from \(\mathcal V_0\) to \(\mathcal V_h\). Every
endpoint owner is used exactly once.

#### Proof

Put

\[
 v_t=|\mathcal V_t|,\qquad \theta_t=\frac{N_r}{v_t}.           \tag{3.1}
\]

The endpoint layers have size \(N_r\), and binomial unimodality gives
\(v_t\ge N_r\). Hence \(0<\theta_t\le1\).

Every vertex of \(\mathcal V_t\) has forward degree

\[
 d_t^+=(r+h-t)^2,                                             \tag{3.2}
\]

while every vertex of \(\mathcal V_{t+1}\) has backward degree

\[
 d_{t+1}^-=(r+t+1)^2.                                         \tag{3.3}
\]

Send \(\theta_t/d_t^+\) units through every arc from phase \(t\) to
phase \(t+1\). The incoming flow at a phase-\((t+1)\) vertex is

\[
 \frac{d_{t+1}^-\theta_t}{d_t^+}
 =\theta_t\frac{(r+t+1)^2}{(r+h-t)^2}
 =\frac{N_r}{v_{t+1}}
 =\theta_{t+1}.                                               \tag{3.4}
\]

Thus flow is conserved and every owner load is at most one. At both
endpoint layers, \(\theta_0=\theta_h=1\), so the flow value is \(N_r\).

The vertex-split network has integral capacities. The augmenting-path
proof of the integral max-flow theorem therefore gives an integral flow
of the same value. The network is layered and acyclic, so flow
decomposition gives \(N_r\) owner-disjoint paths. Since each endpoint
layer has exactly \(N_r\) vertices, every endpoint is used. \(\square\)

The theorem recouples fractional path mass without losing endpoint-linkage
value because the full set is closed under prefix-suffix splicing. It does
not say that an arbitrary fractional path-variable vector is rounded while
preserving every prescribed internal-owner load. In particular it does
not, by itself, repair a determinant-two exact-cover corner on three
specified internal rows. Nor does it choose the cross-radius complements
required by (0.2).

### Corollary 3.2 (arc-local filtered rounding)

Delete an arbitrary collection of arcs from the layered network. If the
remaining network admits a fractional owner-capacity flow of value \(M\),
then it admits an owner-disjoint integral path family of size
\(\lfloor M\rfloor\).

#### Proof

Apply the integral max-flow theorem to the vertex-split filtered network.
\(\square\)

Thus an arc-local single-commodity catalogue has only ordinary vertex-cut
obstructions for maximum endpoint linkage. Exact prescribed coverage of
internal rows, or loss of the network/splicing representation, can still
introduce determinant and odd-set constraints.

## 4. Exact common-forbidden packing

Let \(F_A\subseteq A\), \(|F_A|=f\), and
\(F_B\subseteq B\), \(|F_B|=g\). Retain only paths which never change a
coordinate of \(F_A\cup F_B\). Along such a path the signatures

\[
 P=X\cap F_A,\qquad Q=X\cap F_B                                \tag{4.1}
\]

are constant. Put \(i=|P|\) and \(j=|Q|\). The number of owners of this
signature at phase \(t\) is

\[
 v_t(i,j)
 =\binom{m-f}{r+t-i}
  \binom{m-g}{m-r-t-j}.                                       \tag{4.2}
\]

An inadmissible lower index means that the term is zero.

### Theorem 4.1 (exact common-forbidden formula)

The largest owner-disjoint family of length-\(h\) paths avoiding
\(F_A\cup F_B\) has size

\[
 \boxed{
 M(F_A,F_B)
 =\sum_{P\subseteq F_A}\sum_{Q\subseteq F_B}
       \min\{v_0(|P|,|Q|),v_h(|P|,|Q|)\}.}                    \tag{4.3}
\]

#### Proof

Every allowed path preserves \((P,Q)\), so within one signature its
number is at most the smaller endpoint population. This proves the upper
bound.

Fix a signature. Between phases \(t\) and \(t+1\), the forward and
backward degrees are

\[
 \begin{aligned}
 d_t^+&=(r+h-f-t+i)(r+h-t-j),\\
 d_{t+1}^-&=(r+t+1-i)(r+t+1-g+j).
 \end{aligned}                                                \tag{4.4}
\]

The ratio in (4.2) is exactly

\[
 \frac{v_{t+1}(i,j)}{v_t(i,j)}
 =\frac{d_t^+}{d_{t+1}^-}.                                    \tag{4.5}
\]

The sequence \(v_t(i,j)\) is a product of two binomial-coefficient
sequences, hence is log-concave. A positive log-concave sequence is
unimodal, so its minimum on \(0\le t\le h\) occurs at an endpoint. Let

\[
 M_{P,Q}=\min\{v_0(i,j),v_h(i,j)\}.                            \tag{4.6}
\]

Give every phase-\(t\) vertex load \(M_{P,Q}/v_t(i,j)\le1\), splitting
it equally over outgoing arcs. Equation (4.5) gives flow conservation.
Corollary 3.2 rounds this flow to \(M_{P,Q}\) integral paths. Different
signatures use disjoint owner sets, so their union attains (4.3).
\(\square\)

### Corollary 4.2 (one-coordinate cut)

If \(F_A=\{z\}\) and \(F_B=\varnothing\), then

\[
 M(\{z\},\varnothing)
 =2\binom{m-1}{r-1}\binom mr
 =\frac{2r}{m}N_r
 =\left(1-\frac hm\right)N_r.                                \tag{4.7}
\]

#### Proof

For \(z\) absent at the low endpoint, the low and high populations are

\[
 \binom{m-1}r\binom mr,\qquad
 \binom{m-1}{r-1}\binom mr,
\]

and they are interchanged when \(z\) is present. Formula (4.3) takes the
smaller value in both signatures. Finally,
\(\binom{m-1}{r-1}=(r/m)\binom mr\). \(\square\)

This cut is integral and fractional: forbidding \(z\) splits the network
into the two \(z\)-status fibres, whose endpoint populations are
imbalanced in opposite directions.

### Corollary 4.3 (local dynamic Hall does not imply global grouping)

Assume \(r\ge1\).
Orient every path from its high endpoint to its low endpoint, so its
\(A\)-active alphabet is removed and its \(B\)-active alphabet is
inserted. Fix \(z\in A\). At a high endpoint
\(X=S\mathbin{\dot\cup}T\), choose

\[
 i_X=
 \begin{cases}
 z,&z\in S,\\
 \text{any element of }S,&z\notin S,
 \end{cases}
 \qquad b_X\in B\setminus T.                                  \tag{4.8}
\]

The one-step predecessor

\[
 X-i_X+b_X\longrightarrow X
\]

has live insertion support \(I_X=\{i_X\}\) and live removal support
\(R_X=\{b_X\}\). Require the next \(A\)-removal alphabet to avoid \(I_X\)
and its \(B\)-insertion alphabet to avoid \(R_X\). Then:

1. every endpoint has a nonempty full-orbit safe-option fibre;
2. every endpoint has the same queue-size type and exact safe-option
   fraction
   \[
   \left(\frac{\binom{m-r-1}h}{\binom{m-r}h}\right)^2
   =\left(1-\frac h{m-r}\right)^2;                            \tag{4.9}
   \]
3. each fixed queue-size/type block retains the exact biregular
   empty-rectangle Hall inequality; but
4. every globally safe path preserves the membership of \(z\), and hence
   every owner-disjoint safe packing has size at most
   \((1-h/m)N_r\).

#### Proof

The displayed predecessor is one Johnson move, so both singleton queues
are literally reachable and no coordinate is repeated. The full orbit
independently realizes every \(h\)-subset of \(S\) as removal alphabet
and every \(h\)-subset of \(B\setminus T\) as insertion alphabet. Avoiding
one prescribed label on each side gives (4.9).

The complete typed history-option block is a product of two usual
disjointness incidences and is biregular. Hence every history subfamily,
including the prescribed field above, satisfies the normalized
empty-rectangle inequality relative to the full typed shores. This is not
ordinary one-to-one Hall after histories are collapsed by physical
endpoint.
Globally, a high endpoint containing \(z\) may not remove it, while a high
endpoint not containing \(z\) cannot remove it on a high-to-low path.
Thus no safe path changes \(z\). The allowed catalogue is a subcatalogue
of the common-\(z\) catalogue of Corollary 4.2, proving the upper bound.
\(\square\)

For \(h=C\sqrt m\), (4.9) is \(1-O(m^{-1/2})\): the obstruction persists
even when every local option list is asymptotically complete. The
counterexample uses a prescribed family of individually reachable
one-step queue states. It does not assert that the predecessor edges are
simultaneously owner-disjoint or generated by one coherent route. It
proves exactly that orbit biregularity, even with near-unit local survival,
is insufficient for integral owner grouping without a history-dispersion
invariant.

## 5. Mandatory direction dispersion

Let \(\mathcal M\) be an arbitrary owner-disjoint family of
length-\(h\) paths. Let \(L_0\subseteq\mathcal V_0\) and
\(L_h\subseteq\mathcal V_h\) be the uncovered endpoint sets, of sizes
\(\ell_0,\ell_h\). For \(z\in A\), let \(n_z(\mathcal M)\) be the
number of selected paths whose insertion alphabet contains \(z\).

### Theorem 5.1 (exact coordinate quota)

For every \(z\in A\), inequality (0.6) holds. For every \(z\in B\), the
number of selected paths which remove \(z\) obeys the same bound.

#### Proof

Along a monotone path, an \(A\)-coordinate is unchanged or changes once
from absent to present. Therefore

\[
 n_z(\mathcal M)
 =|\{Y\in\mathcal V_h\setminus L_h:z\in Y\}|
  -|\{X\in\mathcal V_0\setminus L_0:z\in X\}|.                \tag{5.1}
\]

In the complete endpoint layers, the two populations are

\[
 \frac{m-r}{m}N_r,\qquad \frac r mN_r,                         \tag{5.2}
\]

respectively. Their difference is \((h/m)N_r\). Removing the two leave
sets changes the difference by at most \(\ell_0+\ell_h\). The argument
for \(B\)-removals is dual. \(\square\)

Thus any dynamic safe-path library capable of endpoint leave
\(o(N_r/H)\) must supply, simultaneously for every coordinate in both
halves,

\[
 \frac hmN_r+o(N_r/H)                                         \tag{5.3}
\]

owner-disjoint uses of that direction. Endpointwise positive degree and
normalized history-option empty-rectangle expansion do not imply (5.3):
many owners may retain large option sets while those options collectively
avoid one common direction. Corollary 4.2 gives the exact loss.

There is a multicoordinate transport form. For \(F\subseteq A\), every
selected path transports

\[
 J=|X_0\cap F|
 \quad\hbox{to}\quad
 J'=J+|U_A\cap F|.                                             \tag{5.4}
\]

A full endpoint resolution therefore couples the exact low and high
histograms

\[
 \begin{aligned}
 \mu_0(j)
 &=\binom{|F|}j\binom{m-|F|}{r-j}\binom mr,\\
 \mu_h(j)
 &=\binom{|F|}j\binom{m-|F|}{m-r-j}\binom mr,
 \end{aligned}                                                \tag{5.5}
\]

with support on \(j'\ge j\). The one-coordinate quota is the first-moment
projection of this exact transport requirement.

For the natural product-SCD exact-radius count \(P_h\), the analogous
quota cannot be obtained by simply replacing \(N_r\) with \(P_h\).
Longer radii consume part of each endpoint layer, and their coordinate
usage must be subtracted. This is another reason cross-radius simultaneous
selection remains load-bearing.

### Proposition 5.2 (the cumulative quota holds in every SCD)

Let \(\mathscr D\) be any SCD of \(B_m\), and fix a coordinate
\(z\). Among the \(\binom mr\) chains of minimum rank at most \(r\),
exactly

\[
 \frac hm\binom mr                                             \tag{5.6}
\]

insert \(z\) between their rank-\(r\) and rank-\((m-r)\) members.
Consequently, in the product of any two fixed SCDs, exactly

\[
 \frac hmN_r                                                   \tag{5.7}
\]

of the \(N_r\) product paths of length at least \(h\) use \(z\) in their
\(A\)-segment while crossing the radius-\(r\) slab.

#### Proof

Every rank-\(r\) set and every rank-\((m-r)\) set lies on a chain of
minimum rank at most \(r\). Pair these two ranks along their SCD chains.
Monotonicity implies that the number of pairs which insert \(z\) is the
difference between the number of upper and lower members containing
\(z\):

\[
 \binom{m-1}{m-r-1}-\binom{m-1}{r-1}
 =\binom{m-1}r-\binom{m-1}{r-1}
 =\frac hm\binom mr.
\]

For the product statement, pair each of these \(A\)-chains with any of
the \(\binom mr\) \(B\)-chains of minimum rank at most \(r\). This gives
(5.7). \(\square\)

Thus the coordinate current in Theorem 5.1 is not an artefact of
averaging over the full orbit. Every integral product-SCD resolution has
the same cumulative current through each radius slab.

### Theorem 5.3 (exact cross-radius residual quota)

Assume \(r\ge1\). Suppose an owner-disjoint family
\(\mathcal L\) of \(N_{r-1}\) longer
paths has already been selected, and every path of \(\mathcal L\) crosses
the whole radius-\(r\) slab. For \(z\in A\), let
\(u_z^{\mathcal L}(r)\) be the number of those path segments which insert
\(z\) between status \(r\) and status \(m-r\).

Let \(\mathcal M_h\) be a family of exact-length-\(h\) paths in the
physical-owner complement of \(\mathcal L\). If it leaves
\(\ell_0,\ell_h\) residual owners uncovered in the two boundary layers,
and \(n_z^{(h)}\) is its number of insertions of \(z\), then

\[
 \left|
 n_z^{(h)}
 -\left(\frac hmN_r-u_z^{\mathcal L}(r)\right)
 \right|
 \le \ell_0+\ell_h.                                           \tag{5.8}
\]

Moreover,

\[
 \sum_{z\in A}u_z^{\mathcal L}(r)=hN_{r-1}.                   \tag{5.9}
\]

Thus the average residual demand in (5.8) is exactly
\(hP_h/m\), but its coordinatewise distribution is balanced only when

\[
 u_z^{\mathcal L}(r)
 =\frac hmN_{r-1}+o(P_h/H)                                    \tag{5.10}
\]

uniformly in \(z\).

#### Proof

Let \(C_0(z)\) and \(C_h(z)\) be the numbers of longer-path owners
containing \(z\) on the two slab boundaries. Monotonicity gives

\[
 C_h(z)-C_0(z)=u_z^{\mathcal L}(r).                            \tag{5.11}
\]

The full boundary populations differ by \((h/m)N_r\), as in (5.2).
After removing the longer-path owners, the residual boundary difference
is therefore

\[
 \frac hmN_r-u_z^{\mathcal L}(r).                             \tag{5.12}
\]

Applying the endpoint argument from Theorem 5.1 to
\(\mathcal M_h\) inside those residual boundary sets proves (5.8).
Every longer path segment has exactly \(h\) insertion edges in \(A\), so
double counting path-direction incidences proves (5.9). Finally,
\(P_h=N_r-N_{r-1}\), and subtracting the balanced value in (5.10) from
\((h/m)N_r\) gives \(hP_h/m\). \(\square\)

Equation (5.8) is the exact recursive demand property. A cross-radius
construction cannot merely keep the total longer-path count: its child
library must realize the entire residual vector
\((hN_r/m-u_z^{\mathcal L}(r))_z\). For a symmetric child library this is
equivalent to keeping every parent current balanced at the finer additive
scale \(o(P_h/H)\), as in (5.10). This first-moment condition is not
sufficient: the residual layered network can have additional
multicoordinate vertex cuts.

### Theorem 5.4 (biregular queue designs round direction quotas exactly)

Put \(k=m-r\), and let \(\mathcal X=\mathcal V_h\) be the high endpoint
layer. For each \(X=S_X\mathbin{\dot\cup}T_X\in\mathcal X\), prescribe
a forbidden set \(I_X\subseteq S_X\). Assume

\[
 |I_X|=f\quad(X\in\mathcal X),\qquad
 |\{X:z\in I_X\}|=\frac{fN_r}{m}\quad(z\in A),                 \tag{5.13}
\]

and \(f\le k-h=r\). Then there are sets

\[
 U_X\subseteq S_X\setminus I_X,\qquad |U_X|=h,                 \tag{5.14}
\]

such that every \(z\in A\) belongs to exactly

\[
 \frac{hN_r}{m}                                               \tag{5.15}
\]

of the selected active alphabets \(U_X\).

#### Proof

Form the bipartite graph between \(\mathcal X\) and \(A\), joining
\(X\) to \(z\) when \(z\in S_X\setminus I_X\). Every left degree is
\(k-f\).

Before deletion, each \(z\in A\) lies in

\[
 \binom{m-1}{k-1}\binom mr
 =\frac{kN_r}{m}
\]

high endpoints. By (5.13), every right degree after deletion is
\((k-f)N_r/m\). Thus the safe incidence graph is biregular.

Give every safe edge the fractional weight

\[
 \alpha=\frac{h}{k-f}\le1.
\]

The incident weight is \(h\) at every left vertex and

\[
 \alpha\frac{(k-f)N_r}{m}=\frac{hN_r}{m}
\]

at every right vertex. This is a feasible fractional bipartite
\(b\)-matching. Equivalently, connect a source to each \(X\) with
capacity \(h\), give every safe incidence edge capacity one, and connect
each coordinate to a sink with capacity \(hN_r/m\). The displayed
fractional flow has value \(hN_r\). All capacities are integral, so
integral max flow gives a \(0\)-\(1\) edge set with the same left and
right degrees. Its neighbourhood at \(X\) is \(U_X\). \(\square\)

The same theorem applies independently to the removal half \(B\). It is
an exact integral group-design statement: balanced history incidence,
not random independence, suffices to eliminate every one-coordinate
transport cut.

It does not yet select a joint pair \((U_A,U_B)\) whose resulting low
endpoints are distinct, and it does not route the associated paths
through distinct internal owners. Those are higher-order coupling
conditions. The theorem identifies a concrete necessary target for a
coherent-history invariant: make the queue-coordinate incidence
approximately biregular at a precision which can be absorbed to
\(o(P_h/H)\), then solve the joint path coupling.

### Theorem 5.5 (arbitrary queue fields: exact marginal rounding)

The equal-size and biregularity assumptions in Theorem 5.4 are not needed
for marginal rounding. For arbitrary sets

\[
 I_X\subseteq S_X,\qquad |I_X|\le k-h,
\]

put

\[
 a_X=k-|I_X|,
 \qquad
 L_z=\sum_{\substack{X\in\mathcal X\\z\in S_X\setminus I_X}}
          \frac h{a_X}.                                       \tag{5.16}
\]

There are safe active alphabets \(U_X\subseteq S_X\setminus I_X\),
\(|U_X|=h\), such that their coordinate multiplicities \(n_z\) obey

\[
 n_z\in\{\lfloor L_z\rfloor,\lceil L_z\rceil\}
 \qquad(z\in A).                                               \tag{5.17}
\]

In particular, if

\[
 \max_{z\in A}\left|L_z-\frac{hN_r}{m}\right|
 =o(P_h/H),                                                    \tag{5.18}
\]

then all \(A\)-direction quotas are rounded simultaneously to
\[
 n_z=\frac{hN_r}{m}+o(P_h/H).
\]

#### Proof

In the safe endpoint-coordinate incidence graph, give every edge incident
with \(X\) weight \(h/a_X\). The incident weight at \(X\) is exactly
\(h\), and the incident weight at coordinate \(z\) is \(L_z\).

Build a flow network with source-to-\(X\) lower and upper capacity \(h\),
safe incidence edges of capacity one, and coordinate-to-sink lower and
upper capacities \(\lfloor L_z\rfloor,\lceil L_z\rceil\). The displayed
edge weights form a feasible fractional flow. A network with integral
lower and upper capacities has an integral feasible flow whenever it has
a fractional one: subtract the lower bounds, add the usual demand-balancing
source and sink, and apply integral max flow. The integral incidence
edges selected at \(X\) form \(U_X\), and the coordinate degrees satisfy
(5.17). Equation (5.18) and the additive rounding error one give the last
assertion. \(\square\)

Theorem 5.5 completely resolves the one-coordinate integral rounding
problem. The live marginal quantity is the weighted load \(L_z\), not the
raw number of histories forbidding \(z\). What remains is to prove
(5.18) from coherent route chronology and to round the joint
\((U_A,U_B)\)-to-physical-path coupling.

### Corollary 5.6 (exact synchronized one-shore FIFO propagation)

Let \(K\ge1\) satisfy \(Kh\le r\). On a common trajectory index set
\(\mathcal X\) of size \(N_r\), suppose there are \(K\) previous alphabet
layers

\[
 U_X^{(1)},\ldots,U_X^{(K)}\subseteq S_X
\]

such that:

1. \(|U_X^{(j)}|=h\) for every \(X,j\);
2. the \(K\) sets are pairwise disjoint for each fixed \(X\); and
3. for every layer \(j\) and coordinate \(z\in A\),
   \[
   |\{X:z\in U_X^{(j)}\}|=\frac{hN_r}{m}.                      \tag{5.19}
   \]

Then there is a next layer \(U_X^{(0)}\) which is disjoint from all
\(K\) previous layers at each \(X\), has size \(h\), and again satisfies
(5.19). After dropping \(U^{(K)}\), the same hypotheses hold for
\(U^{(0)},U^{(1)},\ldots,U^{(K-1)}\). Hence the balanced FIFO alphabet
schedule can be continued for arbitrarily many rounds.

#### Proof

Put

\[
 I_X=\bigcup_{j=1}^K U_X^{(j)}.
\]

Pointwise disjointness gives \(|I_X|=Kh\). Summing (5.19) over the
\(K\) layers shows that every coordinate belongs to exactly
\(KhN_r/m\) of the sets \(I_X\). Thus (5.13) holds with \(f=Kh\).
The inequality \(Kh\le r=k-h\) permits Theorem 5.4, which supplies
\(U_X^{(0)}\subseteq S_X\setminus I_X\) with the required balanced
coordinate multiplicities. The new pointwise disjointness is automatic.
Dropping the oldest layer preserves all three hypotheses, so induction
continues the schedule. \(\square\)

At \(h=\Theta(\sqrt m)\) and memory \(H=\sqrt m\log\log m\), one may
take \(K=\lceil H/h\rceil=O(\log\log m)\), and \(Kh\le r\) for all
large \(m\). Thus a synchronized one-shore whole-block conservative
queue has no marginal integrality obstruction. In the physical
two-signed-queue automaton, insertion and removal roles alternate and
complementation interchanges the eligible shores. Applying this corollary
there requires two dual FIFO schedules and a proof that their handoff
preserves the common trajectory labelling. The corollary is also
conditional on physical path routing which realizes every chosen
alphabet layer. It proves the exact one-shore alphabet invariant, not
either coupling fact.

## 6. Where dynamic queues destroy network integrality

Theorems 3.1 and 4.1 apply because the allowed path set is closed under
splicing: if an allowed prefix and suffix meet at an owner, their
concatenation is allowed. This makes the catalogue the path set of one
directed network.

For a dynamic queue, the forbidden support is attached to the incoming
history. A prefix legal for history \(\sigma\) and a suffix legal for
history \(\tau\) need not concatenate: the prefix may insert a coordinate
which the suffix removes before it expires. Hence independently rooted
safe options are not closed under splicing.

Duplicating a physical owner by queue state does not by itself repair the
issue. Requiring total capacity one over all state copies while preserving
state identity is not an ordinary node-capacity gadget: one common
capacity edge permits an incoming state to exit through a different state
copy. The projection is a terminal/history-commodity path packing, where
determinant and odd-set obstructions can occur.

The exact positive continuation must therefore supply at least one of:

1. a state-preserving splicing theorem which converts the dynamic safe
   catalogue into an arc-local flow while retaining (5.3);
2. a coloured path-packing theorem which rounds all owner/history
   commodities and proves (5.3)--(5.5) to error \(o(N_r/H)\); or
3. absorbers which repair all residual direction, cross-radius, and
   odd-set deficits with total endpoint leave \(o(N_r/H)\).

The complete orbit solves the bare fixed-radius endpoint-packing problem
exactly and has relative pair codegree \(O(m^{-2})\). The surviving
obstruction is chronology-dependent loss of splicing closure, together
with cross-radius ownership and the exact direction transports.

## 7. Audited boundary

Proved:

* the full labelled SCD orbit contains every monotone cross-half
  length-\(h\) geodesic;
* the exact degrees (0.3) and codegrees (0.4)--(0.5);
* an exact integral fixed-radius flow of \(N_r\) owner-disjoint paths;
* exact integral rounding for every common arc-local forbidden set;
* the common-forbidden packing formula (4.3);
* the one-coordinate deficit (0.7); and
* the mandatory all-coordinate dispersion law (0.6), its universal
  fixed-SCD cumulative form (5.6)--(5.7), and the exact cross-radius
  residual identity (5.8); and
* exact integral direction-quota rounding for every biregular queue
  incidence design (Theorem 5.4); and
* floor/ceiling-optimal simultaneous marginal rounding for arbitrary
  queue fields (Theorem 5.5).

Not proved:

* selection of the natural exact-radius count
  \(P_h=N_r-N_{r-1}\) in the complement of all longer selected paths;
* simultaneous cross-radius owner coverage;
* an integral packing for owner/history-dependent queue filters;
* simultaneous multicoordinate transport after adaptive history
  assignment; or
* coefficient one.

Thus fractional orbit averaging is not the endpoint of the argument. In
the splicing-closed fixed-radius model it rounds exactly by flow. In the
actual dynamic model it must be strengthened by a history-coupled
transport and cross-radius recoupling theorem; without such dispersion,
even one common forbidden coordinate causes the coefficient-scale loss
(0.7).
