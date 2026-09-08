# Protected resident facet extraction has an exact cascade ledger and an
# \(h\)-scale absorption threshold

Date: 2026-08-01  
Lane: all-\(k\) resident facet socket / protected extraction / two-stratum
interface  
Status: **exact local extraction, guard Hall, child-branching, topology,
and endpoint-cocycle theorems; exact conditional Rado/weighted closure;
and a prospective duplicate-provider sufficient condition. A raw socket
in an upper-injective component-neutral factor is proved supercritical.
The asymptotic two-stratum bank can protect the resulting \(o(W)\)
footprint under the stated parity/avoidance hypotheses, but it does not
itself pay the socket endpoint excess. No all-\(k\) equality construction
is claimed.**

## 0. Corrected compact socket

Let \(h\ge1\), put \(H=h+1\), and let \(U\) be a rank-\((r+1)\)
set. Choose distinct \(v_0,\ldots,v_h\in U\), put

\[
                         F_i=U-\{v_i\},                         \tag{0.1}
\]

and consider the facet path

\[
                         F_0F_1\cdots F_h.                     \tag{0.2}
\]

Its \(h\) internal upper colours are all \(U\), while its lower colours

\[
 K_i=F_i\cap F_{i+1}=U-\{v_i,v_{i+1}\},\qquad 0\le i<h,        \tag{0.3}
\]

are distinct. These facts alone do not make (0.2) resident in an arbitrary
chronology.

For each coordinate \(x\), let \(\ell_x\) be the positive-run suffix age
immediately before (0.2), and let \(\rho_x\) be the positive-run prefix age
immediately after it. Call an age **clean** when it is \(0\) or at least
\(H\). The exact boundary conditions are

\[
\begin{array}{rll}
v_0:&\ell_{v_0}\text{ clean},&\rho_{v_0}\ge1,\\
v_j\ (1\le j<h):
   &\ell_{v_j}\ge h+1-j,&\rho_{v_j}\ge j+1,\\
v_h:&\ell_{v_h}\ge1,&\rho_{v_h}\text{ clean},
\end{array}                                                     \tag{0.4}
\]

together with clean \(\ell_x,\rho_x\) for every \(x\notin U\).
These clean rows are necessary: a socket zero may terminate a short
exterior run of an outside coordinate or an omitted endpoint label.
The literal counterexample and complete coordinatewise proof are in
`MATH_AUDIT_RESIDENT_FACET_SOCKET_BOUNDARY_AND_EXTRACTION_20260801.md`.

This note proves four complementary facts.

1. For fixed exterior pieces, protected socket availability is exactly one
   ordinary Hall test.
2. Retaining two old guard incidences deletes at most \(2h\) old seams,
   and arbitrary child branching is at most that cut count.
3. Conversely, one raw socket in an upper-injective component-neutral
   factor necessarily leaves at least \(h\) outside holes. Thus the raw
   process is supercritical.
4. Zero branching becomes provable with prospective duplicate providers.
   Otherwise the first scalar-possible uncompensated capacity scale is
   \(\Theta(h)\), which is \(o(W)\) on the Pascal scale and is compatible
   in size with the two-stratum bank.

## 1. Guard Hall and protected facet availability

For fixed \(U\) and exterior pieces define

\[
\begin{aligned}
A_0&=\{x\in U:\ell_x\text{ clean and }\rho_x\ge1\},\\
A_h&=\{x\in U:\ell_x\ge1\text{ and }\rho_x\text{ clean}\},\\
A_j&=\{x\in U:\ell_x\ge h+1-j,\ \rho_x\ge j+1\},
                         \qquad 1\le j<h.                       \tag{1.1}
\end{aligned}
\]

Let \(\mathcal P\) be a set of old witness edges which must survive. Work
on the conservative **facet-disjoint protected face**, meaning that no
selected socket facet may be incident with an edge of \(\mathcal P\).
(Allowing a protected edge itself to be one of the two retained guards is
a larger boundary-assignment problem and is not encoded below.) Because
\(U\) is missing, an old edge has at most one endpoint which is a facet of
\(U\): two such endpoints would have union \(U\). Define

\[
B_{\mathcal P}=
\{v\in U:U-v\text{ is incident with an edge of }\mathcal P\}.   \tag{1.2}
\]

Then

\[
                         |B_{\mathcal P}|\le|\mathcal P|.       \tag{1.3}
\]

Fix also the physical guard-retention state. Let \(E_j\subseteq U\) be
the labels whose facet \(U-x\) is physically eligible at socket position
\(j\) in that state. In the bare local socket, \(E_j=U\); with fixed
exterior owner pieces, \(E_0,E_h\) additionally encode the two Johnson
joins. Put

\[
                         C_j=(A_j\cap E_j)\setminus B_{\mathcal P}.
                                                                    \tag{1.3a}
\]

### Theorem 1.1 (facet-disjoint protected fixed-boundary Hall)

Assume the outside-\(U\) cleanliness row following (0.4). A compact
resident socket on the facet-disjoint protected face exists if and only if

\[
\boxed{
\left|\bigcup_{j\in J}C_j\right|\ge |J|
\quad\text{for every }J\subseteq\{0,\ldots,h\}.}                \tag{1.4}
\]

#### Proof

The trace of \(v_j\) on (0.2) is \(1^j0\,1^{h-j}\), so the exact boundary
lemma says precisely \(v_j\in A_j\). The fixed guard state additionally
requires \(v_j\in E_j\), and facet-disjoint protection removes (1.2).
Distinct facets require distinct representatives. Hall's theorem now
proves (1.4). \(\square\)

If guard retention is not fixed, exact feasibility is the finite
disjunction of (1.4) over the possible guard states. In particular, the
test above does not misclassify a protected edge retained as a guard; that
larger case belongs to a different state rather than to
\(B_{\mathcal P}\).

Before guard-order restrictions, (1.3) leaves at least

\[
                         {r+1-|\mathcal P|\choose h+1}          \tag{1.5}
\]

unordered facet choices whenever \(r\ge h+|\mathcal P|\).
Formula (1.5) is only a supply bound; it does not imply (1.4).

## 2. Exact extraction and signed resource decks

Let \(F\) be an incumbent linear forest on rank-\(r\) owners, with maximum
degree at most two, and suppose \(U\) is absent from its immediate-upper
deck. The facets of \(U\) are independent in \(F\). Put

\[
                         X=\{F_0,\ldots,F_h\}.                   \tag{2.1}
\]

Let \(K\) be the set of old incidences at \(X\) retained as exterior guard
edges. Every other old edge incident with \(X\) must be deleted, so

\[
D=E_F(X,V(F))-K,\qquad
\boxed{q:=|D|=\sum_{x\in X}\deg_F(x)-|K|.}                      \tag{2.2}
\]

There is no double counting because \(X\) is independent. In a two-regular
factor,

\[
                         q=2h+2-|K|.                            \tag{2.3}
\]

Thus two retained old guards give \(q=2h\), one gives \(2h+1\), and two
new guard joins give \(2h+2\). A selected global endpoint lowers the
corresponding value by one. The retained-guard value \(2h\) is sharp.

Let \(J\) be the new non-socket connector edges. For an edge \(e\), write

\[
                         R(e)=\bigcup e,\qquad Q(e)=\bigcap e.   \tag{2.4}
\]

The exact signed immediate-upper and immediate-lower changes are

\[
\boxed{
\Delta^+=h\mathbf e_U+\sum_{e\in J}\mathbf e_{R(e)}
                        -\sum_{e\in D}\mathbf e_{R(e)},}        \tag{2.5}
\]

\[
\boxed{
\Delta^-=\sum_{i=0}^{h-1}\mathbf e_{K_i}
             +\sum_{e\in J}\mathbf e_{Q(e)}
             -\sum_{e\in D}\mathbf e_{Q(e)}.}                  \tag{2.6}
\]

The socket repairs the resource \(U\), but installs \(h\) occurrences of
it; \((h-1)[U]\) is repeat/cap debt. Likewise, distinctness of the \(K_i\)
does not imply lower exactness: (2.6) is the literal lower/compiler row.

For a previously present old upper colour \(R\), let \(P_R\ne\varnothing\)
be its complete provider-edge set. Its exact child-hole condition is

\[
P_R\subseteq D
\quad\text{and no new edge has upper colour }R.                 \tag{2.7}
\]

Consequently the raw child set obeys

\[
                         \boxed{|\Gamma_U|\le q.}               \tag{2.8}
\]

If one protected witness \(b_R\in P_R\) is fixed for every old colour
outside a terminal family \(\mathcal A\), then

\[
D\cap\{b_R:R\notin\mathcal A\}=\varnothing
\quad\Longrightarrow\quad
\Gamma_U\subseteq\mathcal A.                                   \tag{2.9}
\]

Equations (1.4), (2.2), (2.6), and (2.9), not (2.8) alone, form the
protected extraction interface.

## 3. The sharp repeat-upper/topology lower bound

Let \(F'\) be a linear forest on the same owner vertex set, obtained from
\(F\) by simultaneous socket replacements. Put

\[
D=E(F)-E(F'),\quad B=E(F')-E(F),\quad q=|D|,                    \tag{3.1}
\]

and define

\[
\mu=c(F)-c(F')=|B|-|D|.                                        \tag{3.2}
\]

Thus \(\mu\) is the component-merger credit. Let \(u(D)\) be the number of
previously present old upper colours whose complete provider set lies in
\(D\), and define

\[
                         \rho=q-u(D).                           \tag{3.3}
\]

Thus \(\rho\) is the repeated-provider credit among the cuts.

Suppose \(T\) distinct targets receive \(h\) new socket edges each and
\(H_0\) of those targets were missing before the operation. Assume these
\(hT\) socket edges lie in \(B\). Let \(\kappa\) be the number of genuinely
auxiliary provider slots available in addition to the new edges counted
in \(B\).

### Theorem 3.1 (exact scalar cascade bound)

The number of newly missing old colours outside the target set is at least

\[
\boxed{
|\Gamma_{\rm out}|
\ge\bigl((h-1)T+H_0-\mu-\rho-\kappa\bigr)_+.}                   \tag{3.4}
\]

Hence every closed absorber necessarily satisfies

\[
\boxed{\kappa+\mu+\rho\ge(h-1)T+H_0.}                           \tag{3.5}
\]

#### Proof

Deleting \(D\) kills \(u(D)=q-\rho\) old colours. At most \(T-H_0\) of
them are already-covered target colours, so at least

\[
                         q-\rho-(T-H_0)                         \tag{3.6}
\]

killed colours lie outside the target set. By (3.2), \(B\) has
\(q+\mu\) edges. After removing the \(hT\) repeated target edges, at most
\(q+\mu-hT\) new edges can restore outside colours. The \(\kappa\)
auxiliary slots restore at most \(\kappa\) more. Subtraction gives (3.4).
\(\square\)

For one missing target in an upper-injective, component-neutral factor,

\[
T=H_0=1,\qquad \rho=\mu=\kappa=0,                               \tag{3.7}
\]

and at least \(h\) outside holes remain. One hole becomes at least \(h\)
holes; its defect count rises by \(h-1\). Thus the raw socket is strictly
supercritical for \(h\ge2\).

The same tax appears in the collapsed endpoint ledger. Since

\[
\mathbf1_{F_i}+\mathbf1_{F_{i+1}}-\mathbf1_{K_i}
                         =\mathbf1_U,                            \tag{3.8}
\]

paying for the target \(U\) leaves

\[
\boxed{
E_{\rm sock}
=\sum_{i=0}^{h-1}
  (\mathbf1_{F_i}+\mathbf1_{F_{i+1}}-\mathbf1_{K_i})
    -\mathbf1_U
=(h-1)\mathbf1_U.}                                             \tag{3.9}
\]

If only additional rank-\((r-1)\) lower holes compensate this excess,
then for \(h\ge2\) and \(r\ge2h+1\) their number is at least

\[
\left\lceil{(h-1)(r+1)\over r-1}\right\rceil=h.                 \tag{3.10}
\]

Indeed the ratio is \(h-1+2(h-1)/(r-1)\), strictly between \(h-1\)
and \(h\). Thus \(O(1)\) extra lower capacity is impossible for growing
\(h\) unless redundancy, component merger, or a signed extraction boundary
cancels the tax. The first scalar-possible uncompensated scale is
\(\Theta(h)\); equation (3.10) is not by itself a construction at that
scale.

## 4. Conditional absorption and the matroidal face

Fix the sockets, cut sets, and all already frozen backup objects. Delete
unavailable objects and contract the frozen independent set. For each
child \(R\in\Gamma\), let \(N(R)\) be its possible objects in the resulting
ground set. On a private aligned face, suppose all remaining backup
resource and graphic constraints are represented by one matroid \(M\).
Rado's theorem gives the exact max-min

\[
\nu=\min_{Y\subseteq\Gamma}
       \bigl(|\Gamma-Y|+r_M(N(Y))\bigr)
   =|\Gamma|-\eta_M(\Gamma),                                   \tag{4.0}
\]

and hence the exact full-backup criterion

\[
\boxed{
|Y|\le r_M(N(Y))\quad\text{for every }Y\subseteq\Gamma.}        \tag{4.1}
\]

Its deficiency is

\[
\eta_M(\Gamma)=
\max_{Y\subseteq\Gamma}\bigl(|Y|-r_M(N(Y))\bigr).               \tag{4.2}
\]

The full-set cut must also respect (3.5). If physical compatibility is an
intersection of several matroids rather than the single face above, (4.1)
is only one necessary row and is not asserted sufficient.

### Theorem 4.1 (protected zero-cascade composition)

A finite owner-disjoint family of compact sockets is a zero-cascade
replacement if all of the following hold.

1. Every socket passes (1.4), and every new connector is resident.
2. Protected witnesses satisfy (2.9), and all declared children receive
   compatible backups satisfying (4.1), or the literal joint constraints
   outside the private face.
3. The owner-slot rows keep every indegree and outdegree at most one and
   every underlying owner degree at most two. The edge-count and graphic
   rows realize the declared component change with no cycle. For one
   socket with \(q\) cuts, its \(h\) internal edges require \(q-h\)
   further connectors to preserve the component count.
4. The signed lower row (2.6) vanishes or belongs to a declared auxiliary
   lower-reservoir fibre.
5. The signed upper row (2.5), including repeated target copies, vanishes
   after targets and backups are credited.

Then all processed holes close, no undeclared upper or lower hole is
created, the owner set is unchanged, and the final graph has the declared
components and residence state.

#### Proof

The owner and boundary assertions follow from (1.4). Sum (2.5) and (2.6)
over the global edge sets, charging a shared cut once. Items 2, 4, and 5
cancel every palette coordinate. Item 3 supplies the exact edge count,
owner degree bound, and absence of cycles, hence a linear forest. These
are exactly the asserted invariants. \(\square\)

This is a composition theorem, not an availability theorem: it does not
manufacture the credits in (3.5).

There is a weighted alternative. Give every nonterminal target weight
\(w(R)>0\), and let \(\Phi_t\) be the total weight of all active
nonterminal defects after \(t\) moves. Assume either one globally
compatible simultaneous choice or an online rule valid in every reachable
state. Every reopened defect and every destroyed earlier backup is included
in \(\Phi_{t+1}\). If the move processing \(R_t\) satisfies

\[
\Phi_{t+1}-\Phi_t\le-(1-\theta)w(R_t),\qquad\theta<1,            \tag{4.3}
\]

then telescoping gives

\[
\boxed{
\sum_t w(R_t)\le{\Phi_0\over1-\theta}
   ={\sum_{R\in\mathcal D_0}w(R)\over1-\theta}.}                \tag{4.4}
\]

If \(w_{\min}\) is the minimum nonterminal weight, the number \(T\) of
sockets is at most (4.4)/\(w_{\min}\). Their owner, cut, and internal-lower
loads are bounded by

\[
                    (h+1)T,\qquad(2h+2)T,\qquad hT.             \tag{4.5}
\]

Thus fixed \(h,T\) costs \(O(1)\); more generally \(hT=o(W)\) costs
\(o(W)\). A local child inequality
\(\sum_{S\in\Gamma(R_t)}w(S)\le\theta w(R_t)\) implies (4.3) only
when there are no uncharged side effects. The event-count conclusion also
requires \(w_{\min}>0\), or another well-foundedness condition, and a
separately closing terminal family. The raw estimate (2.8) supplies no
\(\theta<1\).

## 5. A prospective zero-child theorem

The supercritical result uses an upper-injective incumbent. Prospective
duplicate providers change the conclusion.

Let \(\mathcal V_U\) be an allowed set of \(n\) facets of the missing
target \(U\), each of degree at most two in the incumbent support. Thus
\(\mathcal V_U\) is independent. Assume that every old colour either has
a permanent provider not incident with \(\mathcal V_U\), or has provider
edges incident with at least \(a\) distinct facets of \(\mathcal V_U\).
Assume also that all socket deletions are incidences of the selected
facets; in particular, no permanent provider is cut elsewhere by a
connector rethread.

Let \(\mathscr X\) be a distribution on guard-legal \((h+1)\)-subsets of
\(\mathcal V_U\). Suppose every fixed \(a\)-subset
\(A\subseteq\mathcal V_U\) satisfies

\[
                         \Pr[A\subseteq X]\le\pi_a.             \tag{5.1}
\]

### Theorem 5.1 (multiplicity-averaged zero branching)

Under these hypotheses,

\[
                         \mathbb E|\Gamma_U|
                              \le {2n\over a}\pi_a.              \tag{5.2}
\]

If the right side is below one, some guard-legal socket has no raw child
hole.

#### Proof

There are at most \(\lfloor2n/a\rfloor\) vulnerable colours, because
allowed facets carry
at most \(2n\) provider incidences and every vulnerable colour uses at
least \(a\) of them. Killing one such colour requires selecting a fixed
\(a\)-subset of its provider facets, an event of probability at most
\(\pi_a\). Sum over colours and use integrality. The conclusion concerns
raw upper children only; lower, topology, and endpoint rows remain
separate. \(\square\)

For a uniform \((h+1)\)-subset of all \(n\) allowed facets,

\[
                         \pi_a={(h+1)_a\over(n)_a},              \tag{5.3}
\]

provided every such subset is guard-legal or the same inclusion bound
holds after conditioning on guard legality. Hence

\[
\mathbb E|\Gamma_U|
\le {2n\over a}{(h+1)_a\over(n)_a}.                             \tag{5.4}
\]

For \(a=2\), a zero-child choice follows from

\[
                         \boxed{h(h+1)<n-1.}                    \tag{5.5}
\]

This has Pascal-scale margin when \(h^2/r\to\pi/4\) and \(n\sim r\).
It does not apply to the present upper-exact four-row factor, where
vulnerable colours have provider multiplicity one. It is a prospective
planting criterion.

## 6. Fixed-\(M_0\) phases and the facet functional graph

Suppose a perfect incidence matching \(M_0\) is a bijection from the
rank-\((r-1)\) lower colours to the rank-\(r\) owners and sends every
lower colour to a containing owner. Call a socket \(M_0\)-supported when
\(M_0(K_i)\in\{F_i,F_{i+1}\}\) for every \(i\). Along such a socket, write
\(L\) or \(R\) according as \(M_0(K_i)=F_i\) or \(F_{i+1}\).
The pattern \(RL\) is impossible because it would assign both
\(K_{i-1}\) and \(K_i\) to \(F_i\). Hence the word is exactly

\[
                         L^pR^{h-p},\qquad0\le p\le h,           \tag{6.1}
\]

and uses every socket facet except \(F_p\). Conversely every abstract
endpoint assignment in (6.1) is injective; whether it is supplied by a
fixed \(M_0\) is encoded by the graph below. If a retained exterior guard is \(M_0\)-assigned
inward, its socket endpoint must be \(F_p\); two retained guards therefore
cannot both be assigned inward.

For each facet \(F\) of \(U\), let \(K(F)\) be its unique \(M_0\)-preimage.
Exactly two facets of \(U\) contain \(K(F)\): \(F\) and one other facet
\(F'\). Draw

\[
                              F'\longrightarrow F.              \tag{6.2}
\]

Call the resulting graph \(\Gamma_U(M_0)\).

### Proposition 6.1 (common-basis facet graph)

The graph \(\Gamma_U(M_0)\) is simple, has \(r+1\) vertices and \(r+1\)
edges, every vertex has indegree one, and every underlying component is
unicyclic. Its simple paths are exactly the \(M_0\)-supported facet
sockets, with phase (6.1).

#### Proof

The matching gives one preimage \(K(F)\) for each \(F\). Its rank is
\(r-1\), so \(U-K(F)\) has two points and determines the two facets in
(6.2). Opposite parallel edges would require one lower set to have two
\(M_0\)-images, so the graph is simple. The counts follow. Each underlying
component therefore has equal vertex and edge counts and is unicyclic.
The path interpretation is exactly the endpoint assignment above.
\(\square\)

For \(h=3\), failure of a four-vertex path is equivalent to every component
being a triangle. Consequently

\[
                         3\nmid(r+1)                             \tag{6.3}
\]

guarantees an \(M_0\)-supported four-facet socket. If \(3\mid(r+1)\), a
triangle factor is the sharp obstruction. For general \(h\), joining
\(t=\lceil(h+1)/3\rceil\) triangle components requires at least \(t-1\)
component-changing operations before one can form a path on \(h+1\)
vertices. At the abstract graph level, breaking one cycle edge in each
used triangle and concatenating the resulting paths shows that \(t-1\)
joins also suffice. Thus the triangle-factor obstruction has exact
\(\Theta(h)\) abstract merger scale, not \(O(1)\); availability of those
joins as physical resource-safe rows remains separate.

## 7. Two-stratum reconciliation

At this interface the socket owner rank is \(r=m\), so its internal lower
colours have the same rank \(m-1\) as the two-stratum hole family. Use the
Catalan notation

\[
W={2m-1\choose m-1},\qquad C=\operatorname {Cat}_m={2W\over m+1},
\qquad N={2m-3\choose m-2}.                                    \tag{7.1}
\]

The paired Kneser theorem selects a resource-disjoint bank of order \(C\)
from central supply \(N\), with

\[
                         {C\over N}
                 ={4(2m-1)\over m(m+1)}=O(m^{-1}).              \tag{7.2}
\]

A family of \(T\) sockets has typed footprint \(O(hT)\).

* In the even paired-block construction, any prospectively planted typed
  footprint \(Z\) with \(|Z|=o(N)\) removes only \(o(1)\) of the raw block
  density, so the disjoint paired bank still exists.
* In the odd construction, the present random-relabelling proof moves the
  standard odd seed off an arbitrary footprint when
  \(|Z|=o(N/m)=o(C)\). For a larger \(o(N)\) footprint, plant the odd seed
  first and avoid it prospectively, or prove a stronger seed-avoidance
  lemma.
* The balanced lower-hole normal form has maximum orbit density
  \(8/(m+1)\). A uniform permutation of \(G\), fixing the two special
  coordinates individually, therefore avoids any prescribed lower
  footprint of size \(<(m+1)/8\) while preserving its endpoint vector.
  This includes a fixed number of depth-\(\Theta(\sqrt m)\) sockets.
* If a socket target \(U\subseteq G\), its internal lowers omit both special
  coordinates and are automatically outside the normal-form lower-hole
  family. Its owners and target are also signature-disjoint from the
  packet banks.

For as many as \(T=C\) sockets with \(h=o(m)\),

\[
                         (h+1)C,\quad2(h+1)C,\quad hC=o(W)       \tag{7.3}
\]

for owner, cut, and internal-lower loads. This is scale compatibility, not
absorption.

Indeed the two-stratum endpoint law is

\[
                         E=2c\mathbf1+d_{\mathcal H},            \tag{7.4}
\]

where \(\mathcal H\) is a \(C\)-element lower-hole family. Differences of
two such degree vectors have total coordinate sum zero. The private socket
excess (3.9) has positive sum \((h-1)(r+1)\), so changing only
\(\mathcal H\) cannot absorb it.

Let \(\mathcal A_L\subseteq{\Omega\choose m-1}\) be the allowed lower-hole
family. Let \(\gamma\) be the full signed change to the endpoint excess
\(E\) contributed by the ambient extraction and connectors, excluding
(3.9), and let \(Z_L\) be the planted lower footprint. Exact endpoint
composition with an incumbent hole family \(\mathcal H_0\) is equivalent
to

\[
\boxed{
d_{\mathcal H_0}+(h-1)\mathbf1_U+\gamma
       \in\mathfrak D_C(\mathcal A_L\setminus Z_L),}            \tag{7.5}
\]

where \(\mathfrak D_C\) is the exact \(C\)-set hole-degree fibre. In
particular,

\[
                         \sum_x\gamma_x=-(h-1)(r+1)             \tag{7.6}
\]

is necessary. The paired bank supplies private resource avoidance, not
this negative endpoint current.

If the socket path is selected inside \(\Gamma_U(M_0)\), its internal
lower rows retain their pre-existing matched owners and create no new
common-\(M_0\) Hall debt. Extraction guards, connectors, and backups must
still pass the residual common-basis Hall row.

## 8. Exact all-\(k\) conclusion

The all-\(k\) socket interface is now proof-safe.

* Compact \(h+1\)-facet repair with two staircase guards is equivalent to
  the protected Hall row (1.4).
* Two retained guards give the sharp cut bound \(q\le2h\), and raw child
  branching is at most \(q\).
* The converse scalar row (3.5) proves that a private upper-injective
  socket needs \(h\) outside providers or equivalent credits. Thus
  \(O(1)\) closure for growing \(h\) is impossible on the raw face.
* A weighted selector costs \(O(hT)\), and prospective provider
  multiplicity gives the concrete zero-child criterion (5.5).
* The asymptotic two-stratum bank can be selected around an admissible
  \(o(W)\) planted object, but exact composition still requires the signed
  endpoint-fibre condition (7.5) and residual common-\(M_0\) Hall.

The remaining regenerative theorem is therefore precise: plant
boundary-clean facet paths with separated backup multiplicity and an
extraction boundary satisfying (3.5), (4.1), and (7.5) simultaneously.
No density count omitting any one of these rows can prove closure.
