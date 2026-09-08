# Sharp rainbow collision financing and the entry-neutral typed-frame obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Let the selected upper-collision occurrences be divided into nonempty
source-phase/depth strata \(\alpha\).  In stratum \(\alpha\), let the
collision-fibre loads be

\[
  \mu_{\alpha 1},\ldots,\mu_{\alpha r_\alpha}\ge 2,
\]

and put

\[
 T_\alpha=\sum_j\mu_{\alpha j},\qquad
 C_\alpha=\sum_j\binom{\mu_{\alpha j}}2,
 \qquad
 M_\alpha=\max_j\mu_{\alpha j}.
\]

For packets which stay inside one stratum, have size at most \(H\), and
contain at most one occurrence from each collision fibre, the exact minimum
packet count is

\[
 \boxed{
 P_* = \sum_\alpha
 \max\left\{M_\alpha,
             \left\lceil\frac{T_\alpha}{H}\right\rceil
      \right\}.}
 \tag{0.1}
\]

This exact occupancy formula has the sharp collision-financed form

\[
 \boxed{
 P_*
 \le \frac{2C}{H}
      +\sum_\alpha\rho_{H,M_\alpha},
 \qquad
 \rho_{H,K}:=\max_{2\le r\le K}
 \left(r-\frac{r(r-1)}H\right),}
 \tag{0.2}
\]

where \(C=\sum_\alpha C_\alpha\).  Both the coefficient \(2\) and the
uniform additive function \(\rho_{H,K}\), for the class of inputs whose
loads are at most \(K\), are sharp.  For \(H\ge2\),

\[
 \rho_{H,\infty}
 =\frac{\lfloor(H+1)^2/4\rfloor}{H}
 =\frac H4+O(1).
 \tag{0.3}
\]

Consequently, if there are \(s\) nonempty strata,

\[
 P_*
 \le \frac{2C}{H}
 +s\frac{\lfloor(H+1)^2/4\rfloor}{H}.
 \tag{0.4}
\]

In the pair-omission application \(s\le mH\).  Thus

\[
 s\rho_{H,\infty}=O(mH^2)=o(W/H)
 \tag{0.5}
\]

whenever \(mH^3=o(W)\), in particular for fixed \(A\) and
\(H=\lceil A\sqrt m\rceil\).  Hence the exact abstract target is indeed

\[
 \boxed{P_*\le 2C/H+o(W/H).}
 \tag{0.6}
\]

This is not merely an occupancy estimate: the rainbow partition preserves
every nonnegative certified collision-pair Gram term.  The leading
constant \(2\) is forced by load-two fibres.

The desired black-box physical lift, however, is false.  There are two
independent exact obstructions.

1. For fixed typed entrance/exit states, connector-free packetization is
   an Euler-trail problem.  Its port-imbalance lower bound can be \(T\),
   even when (0.1) is \(T/H\).  Collision rainbowness contains no port
   balance information.
2. In the actual pair-omission spike atlas, one MTF update between two
   same-phase/depth spiked endpoints preserves the entering
   \(A\)-coordinate and the complete shallow cap \(U_{q-1}\).  There are,
   inside one integral local factor, growing rainbow families with
   pairwise distinct shallow caps.  They cannot be compiled at one update
   per occurrence.  When each full signed tower is literalized by its
   complete signed Johnson owner window, two marked starts are in fact
   separated by at least \(H+1\) principal owner positions.  Under the
   stronger global Pascal/Gray
   hypothesis that every shifted start is physical through depth \(H\),
   the separation is \(H+q\).

If \(T\) same-stratum spikes are split among \(P\) independent modules and
the applicable start separation is \(d\), their total principal-owner
length obeys

\[
 \boxed{
 L_{\rm tot}\ge P+d(T-P)
             =T+(d-1)(T-P).}
 \tag{0.7}
\]

For the proposed complete signed-tower packets one may take \(d=H+1\).
Thus an entry-neutral bound \(L_{\rm tot}\le T+cP\), with \(c\) fixed
independently of \(H\), forces

\[
 \boxed{P\ge \frac{H}{H+c}\,T.}
 \tag{0.8}
\]

This is asymptotically one packet per occurrence, not one packet per
\(H\) occurrences.  In the load-two extremizer, \(T=2C\), a putative
\(P=2C/H\) realization would have

\[
 L_{\rm tot}\ge 2CH,
 \tag{0.9}
\]

before lower-order endpoint conventions.  The standalone entry-neutral
rainbow-packet compiler is therefore refuted.

There is a genuine positive integral subclass: frame changes whose relative
permutations stabilize the current ordered-partition state are exactly
absorbed into the next MTF update.  A particularly transparent subclass
keeps one shallow cap and its entering \(A\)-coordinate fixed.  What is not
proved is an exact-factor supply of enough such common-cap occurrences with
common old/spiked ports.

The remaining route is a global cross-phase age scheduler which fills each
forced residence gap with useful occurrences of other phases, an
age-compatible rainbow path-cover theorem designed before packetization, or
a non-Pascal literal-OR construction.  No constant-one conclusion follows
from the abstract theorem alone.

---

## 1. Exact stratified rainbow binning

We first isolate the abstract problem completely.

### Definition 1.1 -- stratified rainbow packets

Fix one nonempty stratum and suppress \(\alpha\).  Its occurrence set is a
disjoint union of collision fibres

\[
 G_1\sqcup\cdots\sqcup G_r,
 \qquad |G_j|=\mu_j\ge2.
\]

A packet is **rainbow** if it meets every \(G_j\) in at most one
occurrence.  It is **\(H\)-bounded** if its cardinality is at most \(H\).
Packets from different strata are counted separately because the
owner-fixed physical charts have a fixed source phase and a fixed
distinguished depth.  Mixing strata is a different, global scheduling
problem and is not part of this theorem.

### Theorem 1.2 -- exact minimum packet count

Let

\[
 T=\sum_j\mu_j,
 \qquad M=\max_j\mu_j.
\]

The minimum number of \(H\)-bounded rainbow packets is

\[
 \boxed{p(T,M)=\max\left\{M,\left\lceil\frac TH\right\rceil\right\}.}
 \tag{1.1}
\]

#### Proof

Every packet contains at most one member of a fibre of size \(M\), so at
least \(M\) packets are necessary.  Capacity gives the independent lower
bound \(\lceil T/H\rceil\).

Put

\[
 p=\max\left\{M,\left\lceil\frac TH\right\rceil\right\}.
\]

Start with \(p\) empty bins.  Process the fibres in arbitrary order.  For a
fibre of size \(\mu\), place its members into \(\mu\) distinct currently
least-loaded bins.  This is possible because \(\mu\le M\le p\).

After every step the bin loads differ by at most one.  Indeed, suppose the
current loads are \(a\) and \(a+1\).  If at least \(\mu\) bins have load
\(a\), increment \(\mu\) of those.  Otherwise increment all load-\(a\)
bins and the required number of load-\((a+1)\) bins.  The new loads are,
respectively, contained in \(\{a,a+1\}\) or in
\(\{a+1,a+2\}\).

At termination the maximum load is

\[
 \left\lceil\frac Tp\right\rceil\le H.
\]

Members of each fibre were put into distinct bins.  Thus the lower bound is
attained. \(\square\)

Summing (1.1) over the nonempty strata gives (0.1).

### Theorem 1.3 -- exact worst case at fixed collision count

Fix integers \(H\ge1\), \(K\ge2\), and \(c\ge1\).  Among all finite
multisets

\[
 2\le\mu_j\le K,
 \qquad
 \sum_j\binom{\mu_j}{2}=c,
\]

the largest possible exact packet count is

\[
 \boxed{
 \max\left\{
   \min\left(K,
       \left\lfloor\frac{1+\sqrt{1+8c}}2\right\rfloor
   \right),
   \left\lceil\frac{2c}{H}\right\rceil
 \right\}.}
 \tag{1.2}
\]

#### Proof

Let

\[
 r(c)=\max\{r\ge2:\binom r2\le c\}
     =\left\lfloor\frac{1+\sqrt{1+8c}}2\right\rfloor.
\]

For every admissible multiset,

\[
 M\le\min(K,r(c)).
\]

Also, for every \(\mu\ge2\),

\[
 \mu\le\mu(\mu-1)=2\binom\mu2,
\]

and hence \(T\le2c\).  Theorem 1.2 gives the upper bound in (1.2).

For the second term, take \(c\) fibres of load two.  Then \(T=2c\).
For the first term, put

\[
 a=\min(K,r(c))
\]

and take one fibre of load \(a\), together with

\[
 c-\binom a2
\]

fibres of load two.  The resulting packet count is at least \(a\).  The
two constructions attain the two competing terms, while the preceding
upper bound prevents either construction from exceeding their maximum.
\(\square\)

This theorem makes clear that \(2C/H\) is the correct collision-financed
scale.  It is not an estimate obtained by pretending that the occurrences
are independent balls.

---

## 2. The sharp additive collision-financing term

Define

\[
 f_H(r)=r-\frac{r(r-1)}H
       =\frac{r(H+1-r)}H,
 \qquad
 \rho_{H,K}=\max_{2\le r\le K}f_H(r).
 \tag{2.1}
\]

### Theorem 2.1 -- sharp affine collision bound

For every nonempty stratum,

\[
 \boxed{
 \max\left\{M,\left\lceil\frac TH\right\rceil\right\}
 \le \frac{2C}{H}+\rho_{H,M}.}
 \tag{2.2}
\]

For fixed \(H,K\), the uniform additive constant \(\rho_{H,K}\) cannot be
decreased over the class of strata whose fibre loads are at most \(K\).

#### Proof

The largest fibre contributes \(\binom M2\) collision pairs, so

\[
 \frac{2C}{H}\ge\frac{M(M-1)}H.
\]

Therefore

\[
 M\le\frac{2C}{H}+f_H(M)
   \le\frac{2C}{H}+\rho_{H,M}.
 \tag{2.3}
\]

If \(H=1\), then \(T\le2C\), and
\(\rho_{1,M}\ge f_1(2)=0\), so the capacity term also satisfies (2.2).
Assume \(H\ge2\).  Since \(T\le2C\),

\[
 \left\lceil\frac TH\right\rceil
 \le \frac TH+\frac{H-1}{H}
 \le \frac{2C}{H}+\frac{H-1}{H}.
\]

But

\[
 \rho_{H,M}\ge f_H(2)=2-\frac2H
                       \ge\frac{H-1}{H}.
\]

Thus both terms in the maximum satisfy (2.2).

For uniform sharpness under the load cap \(K\), choose one fibre of load
\(r\), where \(2\le r\le K\) maximizes \(f_H(r)\).  Its exact packet
count is \(r\),
and

\[
 r-\frac{2\binom r2}{H}=f_H(r)=\rho_{H,K}.
\]

No smaller additive constant works. \(\square\)

### Corollary 2.2 -- exact universal overhead

For \(H\ge2\),

\[
 \boxed{
 \rho_{H,\infty}
 =\max_{r\ge2}\frac{r(H+1-r)}H
 =\frac{\lfloor(H+1)^2/4\rfloor}{H}.}
 \tag{2.4}
\]

For \(H=1\), \(\rho_{1,\infty}=0\).  If
\(2\le K\le(H+1)/2\), then

\[
 \rho_{H,K}=\frac{K(H+1-K)}H.
 \tag{2.5}
\]

#### Proof

The integer product \(r(H+1-r)\) is concave and is maximized at one of
the two integers nearest \((H+1)/2\).  For \(H\ge2\), at least one such
integer lies in the permitted range \(r\ge2\), giving (2.4).  For
\(H=1\), the maximum over \(r\ge2\) is zero at \(r=2\).  Before the
vertex, the product is increasing, proving (2.5). \(\square\)

Applying Theorem 2.1 in every stratum proves (0.2)--(0.5).

### Proposition 2.3 -- the leading coefficient two is necessary

Let one stratum consist of \(c\) load-two fibres.  Then

\[
 C=c,\qquad T=2c,
\]

and the exact packet count is

\[
 p=\max\left\{2,\left\lceil\frac{2c}{H}\right\rceil\right\}.
 \tag{2.6}
\]

If \(c=\Theta(W)\) and \(H\to\infty\) with \(H=o(W)\), then

\[
 p=\frac{2C}{H}+O(1).
\]

Thus a bound

\[
 p\le (2-\varepsilon)C/H+o(W/H)
\]

fails for every fixed \(\varepsilon>0\).  The allowed error is
\(o(W/H)=o(C/H)\) and cannot absorb the missing \(\varepsilon C/H\).

---

## 3. The rainbow partition retains the complete collision Gram

The packet theorem is useful only because it finances the actual collision
curvature.

### Theorem 3.1 -- lossless nonnegative collision packetization

Fix a stratum and let \(d_x\) be vectors in a real Hilbert space, one for
each occurrence.  Assume

\[
 \langle d_x,d_y\rangle\ge0
 \qquad(x\ne y)
 \tag{3.1}
\]

within the stratum.  Let \(\mathcal P\) be any rainbow partition and put

\[
 z_P=\sum_{x\in P}d_x.
\]

Then

\[
 \boxed{
 \left\|\sum_xd_x\right\|^2
 -\sum_{P\in\mathcal P}\|z_P\|^2
 \ge
 2\sum_j\ 
   \sum_{\{x,y\}\subseteq G_j}
       \langle d_x,d_y\rangle.}
 \tag{3.2}
\]

In particular, if every pair in a collision fibre at depth \(q\) has
inner product at least \(w_q^+\), the retained curvature is at least

\[
 2\sum_q w_q^+C_q.
 \tag{3.3}
\]

#### Proof

Expanding the squares gives

\[
 \left\|\sum_Pz_P\right\|^2-
 \sum_P\|z_P\|^2
 =2\sum_{P<Q}\langle z_P,z_Q\rangle
 =2\sum_{P<Q}\sum_{x\in P,y\in Q}
     \langle d_x,d_y\rangle.
\]

Every term is nonnegative.  The two members of each same-fibre pair lie
in different packets, so every term on the right side of (3.2) appears in
the displayed cross-packet sum. \(\square\)

Rainbowness is also necessary for a **universal** assertion of the form
(3.2).  If two members of one fibre lie in the same packet, set their two
vectors equal to one unit vector and all other vectors to zero.  The
coherent-versus-packet gap is zero, whereas the certified pair term is
positive.

For the owner-fixed upper spikes, the required nonnegative cross-Gram
property is available inside one source-phase chart.  This statement does
not automatically extend to the lower-dual spike, where different lower
targets can have negative old/image cross terms.  A two-sided theorem
needs a further marker stratification.

---

## 4. The exact typed-port theorem: occupancy is not physicality

Abstract packets become literal blocks only if their entrance and exit
states can be joined without connector entries.

### Definition 4.1 -- typed port arcs

Let \(\mathcal V\) be the finite set of allowed ordered-partition port
states.  After a local frame/orientation is chosen, a physical typed
occurrence \(x\) has an entrance state \(e(x)\in\mathcal V\) and an exit
state \(f(x)\in\mathcal V\).  Regard it as a directed arc

\[
 e(x)\longrightarrow f(x).
\]

Two occurrence blocks concatenate entry-neutrally exactly when the first
exit equals the second entrance.

### Theorem 4.2 -- connector-free packet criterion

For a fixed choice of one oriented port arc for every occurrence in a
packet, the occurrences can be ordered into one connector-free physical
packet if and only if their directed multigraph has an Euler trail.
Equivalently, after isolated vertices are deleted:

1. the underlying undirected graph is connected; and
2. either every vertex has equal indegree and outdegree, or exactly one
   vertex has outdegree minus indegree equal to \(1\), exactly one has
   indegree minus outdegree equal to \(1\), and every other vertex is
   balanced.

#### Proof

A connector-free ordering is precisely an ordering of all arcs in which
the head of each arc is the tail of the next, namely an Euler trail.  The
degree and weak-connectivity conditions are necessary.

If all degrees balance, the usual maximal-trail splicing argument gives an
Euler circuit: start with a maximal directed trail; balance prevents it
from stopping away from its start, and any unused arc in the same weak
component can be spliced into the current closed trail.  In the open case,
add one temporary arc from the negative-imbalance vertex to the
positive-imbalance vertex, find an Euler circuit, and delete the temporary
arc. \(\square\)

With occurrence-specific frame menus, the true selection problem is:
choose one arc from every menu and then decompose the selected arcs into
rainbow Euler trails of at most \(H\) arcs.  This is strictly stronger than
Theorem 1.2.

### Proposition 4.3 -- port-imbalance lower bound

For fixed selected arcs, write

\[
 b(v)=\operatorname{out}(v)-\operatorname{in}(v),
 \qquad
 B_{\rm port}=\sum_v b(v)_+
             =\frac12\sum_v|b(v)|.
 \tag{4.1}
\]

Every decomposition into \(P\) directed trails satisfies

\[
 \boxed{P\ge B_{\rm port}.}
 \tag{4.2}
\]

If the trails are additionally required to be rainbow packets of at most
\(H\) arcs, the decomposition also satisfies the independent bounds

\[
 P\ge M,\qquad P\ge\left\lceil\frac TH\right\rceil,
 \tag{4.3}
\]

and at least one trail is needed in each weak component containing an arc.

#### Proof

The imbalance vector of an open trail has one \(+1\), one \(-1\), and
zeros elsewhere; a closed trail has zero imbalance.  The positive
\(\ell_1\)-mass of the sum of \(P\) such vectors is at most \(P\).
This proves (4.2).  The other two bounds are the fibre and capacity bounds
from Theorem 1.2. \(\square\)

If every occurrence has the sole arc \(u\to v\), then

\[
 B_{\rm port}=T.
\]

The abstract optimum may still be \(T/H\).  Thus low collision load and
rainbow binning do not imply the port balance required at the target
packet count.  A successful rotating-frame theorem would first have to
select frames with

\[
 B_{\rm port}\le 2C/H+o(W/H)
\]

and then prove the rainbow, length-bounded Euler decomposition.  Neither
conclusion follows from occupancy.

---

## 5. A genuine entry-neutral rotating-frame subclass

There is an exact way to rotate frames without paying a connector, but its
compatibility condition is restrictive.

For an ordered partition \(\Pi=(B_1,\ldots,B_r)\) and nonempty update mask
\(X\), write

\[
 M_X(\Pi)=(X,B_1\setminus X,\ldots,B_r\setminus X),
 \tag{5.1}
\]

with empty blocks deleted.  Coordinate permutations act on every block.
The action is equivariant:

\[
 \theta M_X(\Pi)=M_{\theta X}(\theta\Pi).
 \tag{5.2}
\]

### Theorem 5.1 -- stabilizer-gauge rotation

Let

\[
 \Pi_{i+1}=M_{X_{i+1}}(\Pi_i)
 \qquad(0\le i<L)
 \tag{5.3}
\]

be an exact MTF state path.  Choose coordinate permutations
\(\theta_0,\ldots,\theta_L\).  If

\[
 \boxed{
 \theta_{i+1}^{-1}\theta_i\in\operatorname{Stab}(\Pi_i)
 \qquad(0\le i<L),}
 \tag{5.4}
\]

then the conjugated states \(\Sigma_i=\theta_i\Pi_i\) form the exact
one-update path

\[
 \boxed{
 \Sigma_{i+1}
 =M_{\theta_{i+1}X_{i+1}}(\Sigma_i).}
 \tag{5.5}
\]

No reset, dummy mask, or additional middle owner is used.

#### Proof

Condition (5.4) gives

\[
 \theta_i\Pi_i=\theta_{i+1}\Pi_i.
\]

Using (5.2),

\[
 M_{\theta_{i+1}X_{i+1}}(\Sigma_i)
 =M_{\theta_{i+1}X_{i+1}}(\theta_{i+1}\Pi_i)
 =\theta_{i+1}M_{X_{i+1}}(\Pi_i)
 =\theta_{i+1}\Pi_{i+1}
 =\Sigma_{i+1}.
\]

This is literal and integral. \(\square\)

If \(\theta_0\Pi_0=\Pi_0\) and
\(\theta_L\Pi_L=\Pi_L\), the rotated and unrotated paths have common
entrance and exit states.  Thus Theorem 5.1 is a true two-port construction
for stabilizer-compatible frame sequences.

In a canonical tight state, the queue blocks following the main core are
singletons.  Its ordered-partition stabilizer fixes every singleton
coordinate individually and can permute only inside nonsingleton blocks.
Occurrence-specific helper conjugacies generally move different queue
markers, so they do not satisfy (5.4).  This observation alone is only a
limitation of Theorem 5.1, not a no-go theorem.  The next section supplies
the exact no-go.

---

## 6. The shallow-cap lock

Fix one omitted source pair

\[
 A=\{\alpha,\beta\}
\]

and one distinguished depth \(1\le q\le H\le m-2\).  An old saturated
upper tower is

\[
 Y=U_0\subset U_1\subset\cdots\subset U_H,
 \qquad |U_p|=m+p,
 \tag{6.1}
\]

and avoids \(A\).  Let

\[
 b\in U_q\setminus U_{q-1},
 \qquad z\notin U_H\cup A,
\]

and exchange \(A\) with \(\{b,z\}\) by an owner-fixed helper
conjugacy.  Write

\[
 \gamma=\theta(b)\in A,
 \qquad \bar\gamma=A\setminus\{\gamma\}.
\]

In the spiked tower, the flags below \(q\) remain old, the unique new
increment at depth \(q\) is \(\gamma\), and \(\bar\gamma\) remains absent
through depth \(H\).  An ordered-partition state exposing the tower
therefore has the block order

\[
 \text{blocks whose union is }U_{q-1},\quad
 \{\gamma\},\quad\ldots,\quad
 \text{a later block containing }\bar\gamma.
 \tag{6.2}
\]

### Theorem 6.1 -- one-update shallow-cap lock

Suppose one nonempty MTF update carries one phase-\(A\), depth-\(q\)
owner-fixed spiked endpoint to another.  If their entering coordinates and
shallow caps are \((\gamma,U_{q-1})\) and
\((\gamma',U'_{q-1})\), respectively, then

\[
 \boxed{\gamma'=\gamma,
        \qquad U'_{q-1}=U_{q-1}.}
 \tag{6.3}
\]

#### Proof

Let the update mask be \(X\).  In the target ordered partition, its first
block \(X\) lies inside the target central owner \(Y'\).  The central owner
is fixed from the phase-\(A\) source chart and avoids \(A\).  Hence

\[
 X\cap A=\varnothing.
 \tag{6.4}
\]

An MTF update avoiding both \(\alpha\) and \(\beta\) preserves their
relative block order.  In the source state \(\gamma\) precedes
\(\bar\gamma\); in the target state \(\gamma'\) is the member of \(A\)
which precedes the other.  Thus \(\gamma'=\gamma\).

Because \(X\) avoids \(\gamma\), the union of all updated blocks before
the unchanged singleton \(\{\gamma\}\) is

\[
 X\cup(U_{q-1}\setminus X)=X\cup U_{q-1}.
 \tag{6.5}
\]

This union is the target shallow cap \(U'_{q-1}\).  Both shallow caps have
cardinality \(m+q-1\), while the right side of (6.5) contains
\(U_{q-1}\).  Equality of cardinalities forces

\[
 X\subseteq U_{q-1}
 \quad\text{and}\quad
 U'_{q-1}=U_{q-1}.
\]

This proves (6.3). \(\square\)

### Corollary 6.2 -- cap fragmentation

Every uninterrupted run of designated spiked endpoints has a constant
label \((\gamma,U_{q-1})\).  Therefore \(t\) selected occurrences with
pairwise distinct shallow caps require at least \(t-1\) nondesignated MTF
updates between their designated endpoints.  The span from the first to
the last designated endpoint contains at least

\[
 \boxed{2t-1}
 \tag{6.6}
\]

update positions under the usual occurrence-count convention.

More generally, if \(s_V\) selected spikes have shallow cap \(V\), the
number \(R\) of cap-constant runs satisfies

\[
 R\ge |\{V:s_V>0\}|
 \ge \frac{(\sum_Vs_V)^2}{\sum_Vs_V^2}
 =\frac{T^2}{T+2\sum_V\binom{s_V}{2}}.
 \tag{6.7}
\]

The middle inequality is Cauchy--Schwarz.  In particular, if every cap
class has size at most \(K_0\), then \(R\ge T/K_0\).

This identifies the missing statistic: a packet theorem at scale \(T/H\)
needs average shallow-cap concentration of order \(H\).  Collision-fibre
load alone says nothing about that concentration.

### Proposition 6.3 -- exact cap-locked positive path

Fix one shallow cap \(V\), one entering coordinate \(\gamma\), and one
common ordered suffix \(\Xi\) partitioning the ground set outside
\(V\cup\{\gamma\}\).  Let

\[
 \Pi_i=(\Lambda_i,\{\gamma\},\Xi),
\]

where \(\Lambda_i\) is an ordered partition of \(V\).  If

\[
 \Lambda_{i+1}=M_{X_{i+1}}(\Lambda_i),
 \qquad X_{i+1}\subseteq V,
\]

then

\[
 \boxed{\Pi_{i+1}=M_{X_{i+1}}(\Pi_i).}
 \tag{6.8}
\]

#### Proof

The update is disjoint from \(\{\gamma\}\) and from the suffix ground
set.  It acts on the blocks of \(\Lambda_i\) exactly as the internal MTF
update and leaves the displayed suffix order unchanged. \(\square\)

Thus a supplied entrance port can traverse \(t\) cap-locked endpoints in
exactly \(t-1\) updates.  This is a nontrivial entry-neutral realization,
not merely a fractional flow.  It does not prove that an exact factor
supplies growing common-cap families, nor that the old and spiked paths
can be given the same entrance and exit ports.

---

## 7. An integral exact-factor supply of obstructing rainbow packets

The cap obstruction is not an artificial port assignment.  It occurs in
the frozen local pair-omission factor.

Fix \(A\) and put

\[
 Q=[2m+1]\setminus A,
 \qquad |Q|=2m-1.
\]

Let \(F_A\) be one exact local factor on \(Q\).  Its start atlas has one
occurrence for every rank-\((m-1)\) root: in each cyclic row the complement
in \(Q\) of a consecutive \((m-1)\)-root is a consecutive \(m\)-owner,
and exact ownership of all \(m\)-sets therefore gives exact ownership of
their complementary roots.  Hence

\[
 T_0=\binom{2m-1}{m-1}
 \tag{7.1}
\]

occurrences.  At upper depth \(q\), there are at most

\[
 M_q=\binom{2m-1}{m+q}
 \tag{7.2}
\]

targets.

### Theorem 7.1 -- a growing distinct-cap rainbow family

Let \(1\le q\le H=o(m)\).  There is a set of collision occurrences in
\(F_A\) whose upper targets \(U_q\) are pairwise distinct and whose
shallow caps \(U_{q-1}\) are pairwise distinct, of cardinality at least

\[
 \boxed{
 \left\lceil
  \frac{T_0-M_q}{2D_q-1}
 \right\rceil,
 \qquad
 D_q:=\binom{m+q}{m-1}.}
 \tag{7.3}
\]

In particular, for all sufficiently large \(m\), this cardinality is at
least

\[
 \boxed{
 \frac{2^{m-H-1}}{(m+1)(2m+1)}>H.}
 \tag{7.4}
\]

#### Proof

At most \(M_q\) occurrences can lie in singleton upper-target fibres.
Therefore at least

\[
 T_0-M_q
 \tag{7.5}
\]

occurrences belong to collision fibres.

For a fixed upper target \(U_q\), every associated distinct root is an
\((m-1)\)-subset of \(U_q\).  Root ownership in the exact local factor is
injective, so the fibre has size at most

\[
 \binom{m+q}{m-1}=D_q.
\]

The same bound applies to occurrences with a fixed shallow cap
\(U_{q-1}\), since

\[
 \binom{m+q-1}{m-1}\le D_q.
\]

Greedily select a collision occurrence and delete every remaining
occurrence sharing either its \(U_q\) or its \(U_{q-1}\).  One selection
deletes at most \(2D_q-1\) candidates.  This proves (7.3).

For \(q\ge1\), the upper binomial coefficients decrease away from the
central rank, and

\[
 M_q\le M_1
 =\frac{m-1}{m+1}T_0.
\]

Thus

\[
 T_0-M_q\ge\frac{2T_0}{m+1}.
 \tag{7.6}
\]

Also

\[
 D_q\le2^{m+H},
 \qquad
 T_0\ge\frac{2^{2m-1}}{2m+1}.
\]

Combining (7.3)--(7.6) gives (7.4).  Since \(H=o(m)\), its right side is
exponential in \(m-H\) and eventually exceeds \(H\). \(\square\)

Choose \(H\) occurrences supplied by Theorem 7.1.  They are rainbow for
the original collision fibres because their \(U_q\)'s are distinct, and
their shallow caps are pairwise distinct.  Every helper exists because

\[
 |Q\setminus U_H|=m-H-1\ge1.
\]

Corollary 6.2 forces at least \(2H-1\) positions already at the
one-update state level.  Under the complete signed-tower realization,
Section 8 below gives the stronger quadratic span.

At \(q=2\), every upper collision fibre has load at most

\[
 D_2=\binom{m+2}{3},
\]

so the counterpacket lies in a polynomially bounded-load sector.  This
does not prove the same cap-dispersion conclusion under an additional
restriction \(K=o(H)\); that narrower factor class remains unproved.

The exact **abstract** packet count under the additional rule that every
packet stays inside one shallow cap is

\[
 \boxed{
 P_{\rm cap}
 =\sum_V
 \max\left\{
      \max_U\mu_{V,U},
      \left\lceil\frac{T_V}{H}\right\rceil
 \right\},}
 \tag{7.7}
\]

where \(\mu_{V,U}\) counts occurrences having shallow cap \(V\) and upper
collision target \(U\), and \(T_V=\sum_U\mu_{V,U}\).  Equation (7.7) is
Theorem 1.2 applied separately inside every cap.  It is a necessary
cap-refined occupancy count, not a sufficient physical packet theorem:
the entering orientation \(\gamma\), the suffix, and the internal MTF path
must still be made compatible.  It need not be controlled by \(2C/H\):
the family in Theorem 7.1 contributes one to \(P_{\rm cap}\) for every
selected occurrence while it fits into one abstract rainbow packet.

---

## 8. The phase-age spacing theorem, with corrected quantifiers

This section records the exact spacing hierarchy.  The distinction between
a complete tower at each marked occurrence and a module physical at every
shifted start is essential.

Let

\[
 X_0,X_1,\ldots,X_{L-1}\in\binom{[2m+1]}m
 \tag{8.1}
\]

be the principal middle-owner sequence.  At a marked start \(t\), define

\[
 L_h(t)=\bigcap_{j=0}^hX_{t+j},
 \qquad
 U_h(t)=\bigcup_{j=0}^hX_{t+j}.
 \tag{8.2}
\]

The complete signed Pascal tower through \(H\) has Johnson transitions and

\[
 |L_h(t)|=m-h,
 \qquad |U_h(t)|=m+h
 \qquad(1\le h\le H).
 \tag{8.3}
\]

For a switched phase-\(A\), depth-\(q\) owner-fixed spike, all upper flags
below \(q\) avoid \(A\), while exactly one coordinate
\(a\in A\) first appears in \(X_{t+q}\).  The central owner \(X_t\) and
every other marked phase-\(A\) central owner avoid all of \(A\).

### Lemma 8.1 -- marked-tower residence

Assume the complete signed tower (8.3) at start \(t\).  The newly entering
coordinate \(a\) remains present in

\[
 X_{t+q},X_{t+q+1},\ldots,X_{t+H}.
 \tag{8.4}
\]

#### Proof

Suppose \(a\) departs during one of the first \(H\) Johnson transitions.
The coordinate \(a\) was not in \(X_t\), so that departure removes no
element of the initial owner.  Every other transition removes at most one
element of \(X_t\).  Hence at most \(H-1\) initial elements are absent
from the full intersection, giving

\[
 |L_H(t)|\ge m-H+1,
\]

contrary to (8.3). \(\square\)

### Lemma 8.2 -- shifted-start residence

Assume instead that the entire owner path is physical through depth \(H\)
at every valid shifted start.  If a coordinate first enters at

\[
 X_{r-1}\longrightarrow X_r
\]

and \(X_{r+s}\) is the first later owner not containing it, then

\[
 \boxed{s\ge H.}
 \tag{8.5}
\]

If the recursive Gray convention requires residence strictly greater than
\(H\), then \(s\ge H+1\).

#### Proof

If \(s<H\), inspect the shifted window

\[
 X_{r-1},X_r,\ldots,X_{r+s},
\]

which has \(s+1\le H\) transitions.  The coordinate both enters and
leaves and was not in the initial owner.  At most \(s\) departures can
remove elements of \(X_{r-1}\), so the intersection has size at least
\(m-s\), whereas shifted-start physicality requires
\(m-(s+1)\).  This is impossible. \(\square\)

### Theorem 8.3 -- exact separation hierarchy

Let \(t<t'\) be two marked switched starts from the same source phase
\(A\) and the same distinguished depth \(q\).  Then the following bounds
hold under the corresponding hypotheses:

\[
 \boxed{
 t'-t\ge
 \begin{cases}
 q+1,&\text{upper \(q\)-clean data and fixed central owners only},\\[1mm]
 H+1,&\text{a complete signed tower through \(H\) at each marked start},\\[1mm]
 H+q,&\text{the whole module is physical through \(H\) at every shift},\\[1mm]
 H+q+1,&\text{strict recursive-Gray residence greater than \(H\)}.
 \end{cases}}
 \tag{8.6}
\]

#### Proof

Let \(a\in A\) first enter at \(X_{t+q}\).

If \(0<t'-t<q\), put

\[
 h=q-(t'-t),
\]

so \(1\le h<q\).  The below-\(q\) upper window beginning at \(t'\)
contains \(X_{t+q}\), hence contains \(a\), contradicting its required
avoidance of \(A\).  If \(t'-t=q\), then the next marked central owner is
exactly \(X_{t+q}\), also a contradiction.  This proves the first line.

Under the complete marked tower, Lemma 8.1 keeps \(a\) present through
\(X_{t+H}\).  Every next marked central owner avoids \(A\), so
\(t'-t\ge H+1\).  This proves the second line.

Under global shifted-start physicality, Lemma 8.2 keeps \(a\) in

\[
 X_{t+q},\ldots,X_{t+q+H-1}.
\]

The next marked central owner cannot occur at any of those positions, and
the below-\(q\) argument excludes the earlier positions.  Hence
\(t'-t\ge H+q\).  Strict residence retains \(a\) for one further owner and
gives the last line. \(\square\)

The second line is the safe consequence of the six packet conditions in
`DIFFUSE_COLLISION_FUSION_ATTACK_20260725.md`, provided “full flag tower”
means the complete signed Johnson tower (8.3).  The third line is the
stronger conclusion valid for recursive Pascal/Gray modules, where every
shifted start is physical.  It must not be asserted from the packet clauses
alone.

The distinction is real.  Start with an \(A\)-avoiding \(m\)-set and take
an \(H\)-step Johnson geodesic with distinct departures from the initial
set and distinct fresh arrivals, choosing \(a\in A\) as the arrival at
step \(q\).  This realizes the first complete signed tower and retains
\(a\) through \(X_H\).  Remove \(a\) at the next edge.  Then
\(X_{H+1}\) may again avoid \(A\), so a second marked tower can begin at
gap \(H+1<H+q\) when \(q>1\).  The path fails the shifted-start condition
exactly where Lemma 8.2 would be needed.

### Corollary 8.4 -- exact module-length lower bound

Suppose an applicable line of (8.6) gives separation \(d\).  If a module
of \(L_j\) principal owner positions contains \(p_j\ge1\) marked starts,
then

\[
 \boxed{L_j\ge1+d(p_j-1).}
 \tag{8.7}
\]

If \(T\) occurrences are divided among \(P\) nonempty resettable modules,
then

\[
 \boxed{
 L_{\rm tot}\ge P+d(T-P)
 =T+(d-1)(T-P).}
 \tag{8.8}
\]

#### Proof

Order the marked starts in one module.  Consecutive starts differ by at
least \(d\), so their first-to-last span is at least
\(d(p_j-1)\).  Add the first owner position and sum over the modules.
\(\square\)

If each proposed packet has length at most \(p_j+c\), with \(c\) uniform
in \(H\), then (8.8) implies

\[
 T+cP\ge T+(d-1)(T-P),
\]

and hence

\[
 \boxed{
 P\ge\frac{d-1}{d-1+c}\,T.}
 \tag{8.9}
\]

For the complete signed-tower seam, \(d=H+1\), giving (0.8).  If the
collision-fibre loads are at most \(K\), then

\[
 C
 =\sum_j\binom{\mu_j}{2}
 \le\frac{K-1}{2}\sum_j\mu_j
 =\frac{K-1}{2}T,
\]

so

\[
 \boxed{
 P\ge
 \frac{d-1}{d-1+c}\frac{2C}{K-1}.}
 \tag{8.10}
\]

For \(K=o(H)\), \(C=\Omega(W)\), and \(d\ge H+1\), this is larger than
the target \(2C/H+o(W/H)\) by an unbounded factor of order \(H/K\).
For load-two fibres, \(T=2C\); substituting
\(P=2C/H+o(W/H)\) and \(d=H+1\) in (8.8) gives

\[
 L_{\rm tot}\ge2CH-o(W).
 \tag{8.11}
\]

If all modules concatenate into one continuous same-phase physical path,
the spacing also applies across the alleged module boundaries, and the
stronger bound is

\[
 L\ge1+d(T-1).
\]

Equation (8.8) is the conservative bound which grants one genuine reset at
every packet boundary.

---

## 9. The exact interval polytope audit

There is no fractional scheduling or dependent-rounding escape from the
phase-age bound.

Fix a path of \(L\) possible marked starts and a separation parameter
\(d\).  For \(L\ge d\), impose

\[
 \sum_{t=r}^{r+d-1}y_t\le1
 \qquad(0\le r\le L-d),
 \tag{9.1}
\]

and \(y_t\ge0\).  If \(L<d\), use the single inequality
\(\sum_ty_t\le1\).

### Theorem 9.1 -- exact integral phase-age capacity

The polytope in (9.1) is integral.  Its integral points are exactly the
sets of starts with pairwise distance at least \(d\), and

\[
 \boxed{
 \max\sum_ty_t
 =1+\left\lfloor\frac{L-1}{d}\right\rfloor
 =\left\lceil\frac Ld\right\rceil.}
 \tag{9.2}
\]

#### Proof

Order the rows of the interval matrix by their left endpoints.  The rows
containing any fixed column are consecutive.  For every subset of rows,
give its rows alternating signs in the induced order.  In each column the
signed sum is \(-1,0\), or \(1\).  The Ghouila--Houri criterion proves
total unimodularity.  With integral right side and nonnegativity, every
extreme point is integral.

The interval inequalities are equivalent to pairwise distance at least
\(d\).  The positions

\[
 0,d,2d,\ldots
\]

give \(\lceil L/d\rceil\) starts, and summing consecutive gaps gives the
matching upper bound. \(\square\)

Thus the exact integral relaxation itself yields (8.7).  A color-balanced
nibble, determinantal selection, or dependent rounding cannot repair the
missing capacity inside an independently compiled same-phase packet.

---

## 10. What a correct physical rainbow theorem would have to prove

The abstract theorem and the physical obstruction combine into a precise
replacement gate.

For every occurrence, one would need a menu of integral owner-preserving
typed realizations.  A successful theorem must simultaneously choose one
menu element per occurrence and decompose the choices into at most

\[
 \frac{2C}{H}+o(W/H)
\]

packets such that:

1. every packet is rainbow in the original collision fibres;
2. every packet has at most \(H\) designated occurrences;
3. its selected port arcs form one Euler trail, or its internal bridge
   entries are charged explicitly;
4. the total selected port imbalance and weak-component fragmentation are
   at most \(2C/H+o(W/H)\);
5. shallow-cap changes obey the lock of Theorem 6.1;
6. same-phase marked starts obey the appropriate age separation in
   Theorem 8.3;
7. all forced intervening owner positions are useful occurrences of other
   phases/depths rather than paid reset positions;
8. middle ownership remains integral inside one exact factor; and
9. the output is a literal contiguous-OR word, not a fractional packet
   covariance.

For a load-two sector, \(T=2C\).  Reaching the target count requires

\[
 T-P
 =2C-\frac{2C}{H}-o(W/H)
 \tag{10.1}
\]

entry-neutral joins.  This is a near-complete compatible path cover, not an
ordinary occupancy theorem.  Theorems 6.1 and 8.3 show that same-phase
standalone packets have nowhere near this many legal joins.

Three routes remain logically open.

1. **Global cross-phase age interleaving.**  While a coordinate of phase
   \(A\) is forced to reside, owner positions from other phases could do
   useful work.  Such a schedule must be chosen globally before abstract
   binning.
2. **Age/cap-compatible packetization.**  Prove a rainbow path-cover
   theorem in a compatibility graph whose vertices already carry phase,
   age, shallow-cap, and port data.  Its conclusion, not its hypothesis,
   must have the sharp \(2C/H\) count.
3. **Non-Pascal direct OR.**  Realize collision targets as literal crossing
   intervals without making them canonical unions of consecutive principal
   owners.  Middle injectivity and the complete lower/upper ledger must then
   be reproved directly.

---

## 11. Audit corrections and implication scope

1. The exact per-stratum packet count uses the actual maximum load
   \(M_\alpha\), not a uniform upper bound \(K\).  Replacing it by \(K\)
   loses sharpness.
2. The older additive estimate \((K+1)s\) is valid but unnecessary.  The
   sharp overhead is \(\sum_\alpha\rho_{H,M_\alpha}\), universally
   \(O(sH)\), even when \(K\) grows.
3. The coefficient \(2\) in \(2C/H\) is sharp at the allowed
   \(o(W/H)\) error scale, not merely at fixed finite size.
4. Formula (3.2) requires nonnegative cross-Gram inside the stratum.  It is
   proved for the upper owner-fixed chart; it must not be transferred to
   lower-dual charts without a separate sign audit.
5. Port imbalance is a necessary condition after a frame choice.  Small
   imbalance alone is not sufficient: weak connectivity, Euler degree
   conditions, rainbowness, and length \(H\) must still be solved.
6. The stabilizer-gauge lemma is a sufficient exact construction.  Failure
   of its hypothesis is not itself an impossibility theorem; the shallow
   cap lock and phase-age theorems supply the actual obstructions.
7. The \(H+q\) spacing in
   `MATH_ATTACK_S14_ENTRY_NEUTRAL_ROTATING_FRAME_INVARIANT_20260725.md`
   is correct for a module physical through depth \(H\) at every shifted
   start.  It is not implied solely by the six packet clauses in the
   diffuse-fusion report.  Under their complete signed-tower content the
   hypothesis-safe spacing is \(H+1\).  This correction does not weaken
   the no-go conclusion.
8. Theorem 7.1 gives an actual integral packet obstruction in the local
   exact factor and a polynomial load bound at \(q=2\).  It does not prove
   cap dispersion for the narrower sector \(K=o(H)\).
9. The aggregate length bound (8.8) applies to independently compiled
   same-phase/depth modules.  It cannot be charged again after a global
   construction has legitimately filled the forced gaps with useful
   occurrences of other phases.
10. Nothing here proves that all literal contiguous-OR constructions must
    use canonical Pascal towers.  The non-Pascal escape remains open.

### Precise proved boundary

Proved:

* the exact stratified rainbow minimum (0.1);
* the exact fixed-collision extremum (1.2);
* the sharp collision-financed bound (0.2)--(0.4);
* sharpness of both the leading coefficient and the additive overhead;
* lossless retention of all certified nonnegative collision-pair Gram;
* the typed-port Euler criterion and port-imbalance lower bound;
* the exact stabilizer-compatible entry-neutral frame rotation;
* the one-update shallow-cap lock;
* a growing, integral, bounded-load exact-factor supply of distinct-cap
  rainbow occurrences;
* the corrected phase-age separation hierarchy;
* the exact aggregate module-length lower bound; and
* integrality of the phase-age interval-capacity polytope.

Refuted:

* the universal same-phase/depth entry-neutral rotating-frame packet of
  length \(|\mathcal P|+O(1)\);
* any deduction of the target packet count from collision occupancy alone.

Not proved:

* a global cross-phase phase-age scheduler;
* an age/cap/port-compatible rainbow path-cover theorem with
  \(2C/H+o(W/H)\) paths;
* common old/spiked two-port closure for growing cap-locked families;
* a non-Pascal direct-OR substitute;
* the constant-one theorem.
