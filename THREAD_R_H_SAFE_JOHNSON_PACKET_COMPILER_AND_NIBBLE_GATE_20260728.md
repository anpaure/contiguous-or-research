# H-safe Johnson packets: exact \(m^2\) owner geometry, the first-flag fibre, and the literal compiler interface

Date: 2026-07-28

Method: pure mathematics only.  No web search, computation, finite search,
solver, or certificate data is used.

Status: the packet hypergraph census, open-path capacity bounds, compiler
interface, PBBS fragment obstruction, and first-shadow conveyor identities
are proved.  The target-decorated packet matching remains unproved.
Packet-PCSH is an additional exact condition only when prescribed targets
must be installed inside fixed packet blocks without appended repair letters.
No Hamiltonization or coefficient-one theorem is claimed.

## 0. Outcome

There is a genuine non-wreath successor to row-power packets, but the
frequently suggested inference

\[
 \text{Johnson step degree }\asymp m^2
 \quad\Longrightarrow\quad
 \text{nibble leave }O(W/m)
\tag{0.1}
\]

is not a theorem.  The exact conclusions are as follows.

1. The orbit of all globally geodesic \(\ell\)-edge paths in
   \(J(n,r)\) is an exactly regular \((\ell+1)\)-uniform owner
   hypergraph.  If two owners have Johnson distance \(j\), its normalized
   codegree is

   \[
   \frac{2(\ell-j+1)}{\ell+1}
   \frac1{\binom rj\binom{n-r}{j}}.
   \tag{0.2}
   \]

   In \(J(2m,m)\), for every \(2\le H\le m-2\) and
   \(\ell=m-H\), the maximum is the adjacent-owner value

   \[
   \frac{\Delta_{OO}}D
      =\frac{2\ell}{(\ell+1)m^2}
      =\frac{2(m-H)}{m-H+1}m^{-2}.
   \tag{0.3}
   \]

   The last expression is \((2+o(1))m^{-2}\) when \(m-H\to\infty\);
   that asymptotic is not uniform up to \(H=m-2\).

   By contrast, the maximal complementary paths \(\ell=m\) force an
   antipodal codegree \(2/(m+1)\).  Truncating before the complement
   endpoint removes exactly this row-power rigidity.

2. The full locally safe catalogue has a finite-memory presentation.
   Requiring every \(H+1\) consecutive transitions to use distinct
   physical directions gives a memory graph with exact outdegree

   \[
                     (r-H)(n-r-H)\asymp m^2.
   \tag{0.4}
   \]

   This is real step entropy.  For long packets, however, it gives only a
   crude owner codegree bound \(O(\ell/m^2)\).  An \(O(m^{-2})\)
   long-return bound requires a new spectral/return theorem for the memory
   graph.

3. Even the favorable geodesic owner hypergraph has an unavoidable
   owner--first-flag link of order \(m^{-1}\).  For a lower \(q\)-flag
   \(S\subset X\),

   \[
   \frac{\operatorname {codeg}_{\rm same}(X,S)}D
   =
   \frac{\ell-q+1}{\ell+1}\binom rq^{-1},
   \tag{0.5}
   \]

   and dually the upper ratio uses \(\binom{n-r}{q}^{-1}\).  At \(q=1\)
   this is \((1+o(1))/m\).  Thus an ordinary owner-and-target matching
   lift reinstates the critical first-row fibre.  Owner entropy alone
   does not control the colored flag cover.

4. Open paths have a deterministic all-depth capacity loss.  If \(G\)
   selected owner occurrences lie in \(K\) paths, then at depth \(q\)
   there are at most \(G-qK\) internal windows.  Consequently

   \[
   h_q^\pm\ge
   \left[\binom{2m}{m\pm q}-(G-qK)\right]_+.
   \tag{0.6}
   \]

   For a spanning family of essentially uniform \(\ell\)-edge paths in
   the regime \(\ell=o(m)\), with the resulting critical depth still at
   most \(H\), aggregate \(o(W)\) flag repair requires

   \[
                         \ell=\omega(m^{2/3}).
   \tag{0.7}
   \]

   When \(H=o(m^{2/3})\) this is stronger than the collar requirement
   \(\ell/H\to\infty\); in general the two conditions are independent.

5. Full wreath structure is not required by the literal compiler.
   A family of compiler-\(H\)-safe Johnson path packets with \(p\)
   components has an endpoint-capped factor of cost \(Hp\).  If
   \(h_q^-,h_q^+\) are its actual chronological flag holes, then the
   central band has a literal word of length

   \[
                W+Hp+\sum_{q=1}^{H}(h_q^-+h_q^+).
   \tag{0.8}
   \]

   Complete actual setwise flag support is already sufficient for this
   literal provider-union theorem.  If one additionally forbids appended
   repair letters and requires a compatible placement inside fixed blocks,
   the exact extra condition is the existential multi-packet
   pin-compatible sandwich Hall condition of Theorem 5.2; the witness
   intervals need not be prescribed beforehand.

6. Rethreading retained PBBS fragments cannot exploit the new \(m^2\)
   entropy before paying the old residence toll.  If \(J\) PBBS
   transitions are cut and the fragments are sewn into compiler-safe
   paths, then

   \[
                         J\ge\tau_H(P_m)\ge\nu_H(P_m).
   \tag{0.9}
   \]

   The exact literal cost is at most

   \[
                         W+Hp+(4H-1)J.
   \tag{0.10}
   \]

   Thus segment-retaining rebundling is equivalent to the existing PBBS
   residence gate.  A genuine escape must replace a bulk family of
   transitions and recertify the flag profiles.

7. There is a positive non-wreath first-shadow conveyor.  A path
   partition of the saturated rank-\(m\) row can be lifted to
   rank-\((m+1)\) owner paths so that every rank-\(m\) target remains
   exactly an adjacent intersection.  All deeper lower flags become
   consecutive intersections in the lower paths.  This removes the
   unavoidable \(q=1\) loss of an ordinary open owner-path cover, at the
   price of one extra owner occurrence per path.

The resulting open theorem is a target-decorated, compiler-safe Johnson
path near-tiling.  A useful regime is

\[
 \sqrt m\,\omega(m)\le H=o(\ell),\qquad
 m^{2/3}\ll\ell=o(m).
\tag{0.11}
\]

An owner-disjoint selection with \(O(W/\ell)\) long packets and aggregate
flag holes \(o(W)\) would imply coefficient one through Theorem 5.1;
packet-PCSH is needed only for the stronger fixed-block, no-repair version.
No current nibble theorem supplies the required simultaneous selection.

## 1. Three safety notions and the off-by-one

Let

\[
 T=(T_0,\ldots,T_s)
\]

be a directed path in \(J(n,r)\), with

\[
                T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\tag{1.1}
\]

For \(q\ge0\), put

\[
 L_{q,i}=\bigcap_{j=0}^{q}T_{i+j},\qquad
 U_{q,i}=\bigcup_{j=0}^{q}T_{i+j}.
\tag{1.2}
\]

We distinguish the following.

* \(G_H\): in every \(H\)-transition window, the \(2H\) labels
  \(a_i,b_i,\ldots,a_{i+H-1},b_{i+H-1}\) are pairwise distinct.
* \(P_H\): every internally bounded positive coordinate run in \(T\)
  has at least \(H+1\) vertices.
* compiler-\(H\)-safe: \(G_H\) and \(P_H\) both hold.

The stronger condition \(G_{H+1}\) implies compiler-\(H\)-safety.

### Lemma 1.1 (exact traces under \(G_H\))

If \(G_H\) holds, then for every \(q\le H\),

\[
 L_{q,i}=T_i\setminus\{a_i,\ldots,a_{i+q-1}\},
\tag{1.3}
\]

\[
 U_{q,i}=T_i\cup\{b_i,\ldots,b_{i+q-1}\}.
\tag{1.4}
\]

In particular the ranks are \(r-q\) and \(r+q\).

#### Proof

No coordinate inserted in the window is deleted later in the same window,
and no deleted coordinate is reinserted.  The deletion and insertion labels
are individually distinct.  Hence precisely the displayed coordinates are
lost from the intersection and gained by the union.  \(\square\)

The off-by-one matters.  A coordinate inserted at transition \(i\) and
removed at transition \(i+H\) is not repeated in one \(H\)-transition
window, so \(G_H\) permits a positive run of exactly \(H\) vertices.
Such a run is erased by the delay-\(H\) erosion.  Thus \(G_H\) alone does
not imply \(P_H\); either \(P_H\) or the sufficient strengthening
\(G_{H+1}\) must be retained in a literal compiler theorem.

## 2. Exact orbit of globally geodesic path packets

Put

\[
             b=n-r,\qquad N_0=\binom nr,
\]

and fix \(1\le\ell\le\min(r,b)\).  An oriented globally geodesic packet is

\[
 X_t=X_0-\{a_1,\ldots,a_t\}+\{c_1,\ldots,c_t\},
 \qquad0\le t\le\ell,
\tag{2.1}
\]

where \(a_1,\ldots,a_\ell\) are distinct members of \(X_0\) and
\(c_1,\ldots,c_\ell\) are distinct members of \(X_0^c\).
Then

\[
                         d_J(X_i,X_j)=|i-j|,
\tag{2.2}
\]

so the owner sequence is simple and is compiler-\(H\)-safe for every
\(H<r\).  The vertex set of the path determines its order up to reversal.

Let \({\cal G}_{n,r,\ell}\) be the owner multihypergraph of all oriented
packets.  Treating the two orientations as separate formal edges multiplies
all degrees and codegrees by the same factor and does not change matchings
or normalized ratios.

### Theorem 2.1 (exact owner degree and every shell codegree)

The number of formal packets and the common owner degree are

\[
 |E({\cal G}_{n,r,\ell})|
       =N_0(r)_\ell(b)_\ell,
\tag{2.3}
\]

\[
 D_0=(\ell+1)(r)_\ell(b)_\ell.
\tag{2.4}
\]

If \(X,Y\) have Johnson distance \(j\), then their codegree is zero for
\(j>\ell\), while for \(1\le j\le\ell\),

\[
 \boxed{
 \frac{\operatorname {codeg}(X,Y)}{D_0}
 =
 \frac{2(\ell-j+1)}{\ell+1}
 \frac1{\binom rj\binom bj}.}
\tag{2.5}
\]

#### Proof

There are \((r)_\ell(b)_\ell\) ordered deletion/insertion lists from a
fixed initial owner, proving (2.3).  Double-count owner incidences to get
(2.4).

Suppose first that \(X\) precedes \(Y\) at distance \(j\) in the packet.
There are \(\ell-j+1\) possible phase pairs.  The \(j\) transitions from
\(X\) to \(Y\) may order the \(j\) elements of \(X\setminus Y\) and the
\(j\) elements of \(Y\setminus X\) independently, in \((j!)^2\) ways.
The remaining \(\ell-j\) transitions choose ordered unused deletion and
insertion labels, giving

\[
                 (r-j)_{\ell-j}(b-j)_{\ell-j}.
\tag{2.6}
\]

The reverse order contributes the same amount.  Hence

\[
\operatorname {codeg}(X,Y)
=2(\ell-j+1)(j!)^2
 (r-j)_{\ell-j}(b-j)_{\ell-j}.
\tag{2.7}
\]

Divide by (2.4), and use

\[
 (r)_\ell=(r)_j(r-j)_{\ell-j},\qquad
 \frac{j!}{(r)_j}=\binom rj^{-1},
\]

and the analogous identity for \(b\).  This proves (2.5).  \(\square\)

### Corollary 2.2 (truncation removes the antipodal codegree)

In \(J(2m,m)\), assume \(m\ge4\) and
\(1\le\ell\le m-2\).  Then the maximum nontrivial codegree is attained
at \(j=1\), and

\[
 \boxed{
 \frac{\Delta_{OO}}{D_0}
 =\frac{2\ell}{(\ell+1)m^2}.}
\tag{2.8}
\]

For \(\ell=m\), in contrast, a complementary pair \(X,X^c\) has

\[
 \boxed{
 \frac{\operatorname {codeg}(X,X^c)}{D_0}
 =\frac2{m+1}.}
\tag{2.9}
\]

#### Proof

For \(2\le j\le\ell\le m-2\),

\[
 \binom mj\ge\binom m2.
\]

Thus (2.5) is at most
\(2/\binom m2^2<2\ell/((\ell+1)m^2)\), while \(j=1\) gives the latter
quantity exactly.  At \(\ell=m,j=m\), formula (2.5) gives (2.9).
\(\square\)

The favorable owner geometry (2.8) is therefore not a heuristic.  It is an
exact consequence of allowing long open paths which stop before their
forced complementary endpoint.

## 3. The full locally safe memory graph

The geodesic catalogue never reuses a direction.  A locally safe path may
reuse it after the compiler memory expires and therefore has more sustained
entropy.

Define \(D_{H+1}(n,r)\) as follows.  A state consists of a current owner
\(X\), the ordered \(H\) most recent departure labels, and the ordered
\(H\) most recent arrival labels, all distinct and consistent with
membership in \(X\).  An arc chooses a new departure and arrival outside
these queues and shifts the queues by one.

### Lemma 3.1 (exact memory degree)

Above every owner there are

\[
                         (r)_H(b)_H
\tag{3.1}
\]

memory states.  Every state has in- and outdegree

\[
                         d_H=(r-H)(b-H).
\tag{3.2}
\]

Every walk projects to a \(G_{H+1}\), hence compiler-\(H\)-safe, Johnson
walk.  Conversely every \(G_{H+1}\) Johnson walk with its initial memory
queue specified has a unique lift.  Here \(H<\min(r,b)\).

#### Proof

The recent arrivals are \(H\) ordered elements currently in \(X\), and the
recent departures are \(H\) ordered elements currently outside \(X\).
This gives (3.1).  A new departure may be any of the \(r-H\) current
coordinates outside the arrival queue; a new arrival may be any of the
\(b-H\) absent coordinates outside the departure queue.  Shifting is
reversible, proving both degrees and the walk correspondence.  \(\square\)

If owner simplicity is imposed and \(t\) owners have already appeared,
at most \(t\) of the \(d_H\) next owners are forbidden.  Thus a fixed
memory state begins at least

\[
                         \prod_{t=0}^{\ell-1}(d_H-t)
\tag{3.3}
\]

owner-simple safe walks of length \(\ell<d_H\).  In particular the local
branching remains \(m^2(1-o(1))\) throughout every
\(\ell=o(m)\) packet in the central regime \(H=o(m)\).

This count alone does not control long returns.  For a uniformly chosen
memory above owner \(X\), let \(p_j(X,Y)\) be the probability that the
projected owner after \(j\) steps is \(Y\).  In the unrestricted regular
walk multicolumn, in which a repeated owner is counted once for every phase
occurrence, the exact phase-occurrence pair ledger is

\[
 \frac{\operatorname {codeg}(X,Y)}D
 =
 \frac1{\ell+1}\sum_{j=1}^{\ell}
   (\ell-j+1)\bigl(p_j(X,Y)+p_j(Y,X)\bigr).
\tag{3.4}
\]

One has \(p_1(X,Y)=1/(rb)\) for adjacent owners.  Since a state has at most
one outgoing transition to a prescribed next owner,

\[
                         p_j(X,Y)\le d_H^{-1}
\tag{3.5}
\]

for every \(j\ge1\), after conditioning at the penultimate state.  Hence

\[
                 \frac{\Delta_{OO}}D=O(\ell/d_H)
                    =O(\ell/m^2).
\tag{3.6}
\]

This is not yet an exact support codegree, because an unrestricted walk can
visit one owner more than once.  For the owner-simple subcatalogue put

\[
 \theta_{\ell,H}=\frac{(d_H)_\ell}{d_H^\ell}
 \ge1-\frac{\ell(\ell-1)}{2d_H}.
\tag{3.7}
\]

The extension count (3.3) and the unrestricted numerator give the rigorous
support bound

\[
 \frac{\Delta_{OO}}{D_{\rm simp}}
 \le \theta_{\ell,H}^{-1}\frac{\ell}{d_H}
 =\left(1+O\left(\frac{\ell^2}{d_H}\right)\right)
   \frac{\ell}{d_H}
\tag{3.8}
\]

when \(\ell^2=o(d_H)\).  For \(\ell=\Theta(m)\), the unrestricted bound
(3.6) is only \(O(1/m)\), while (3.8) no longer has a small conditioning
loss.  Proving an \(O(m^{-2})\) long-packet bound therefore requires a
genuine owner-simple return or spectral estimate.  The \(m^2\) outdegree by
itself does not prove it.

## 4. Flag incidences and the deterministic open-path toll

For a geodesic packet, define the actual traces

\[
 L_{q,t}=\bigcap_{i=0}^{q}X_{t+i},\qquad
 U_{q,t}=\bigcup_{i=0}^{q}X_{t+i}.
\tag{4.1}
\]

For each sign, the \(\ell-q+1\) targets in one packet are distinct.

### Theorem 4.1 (target degrees and the unavoidable mixed link)

Under the full coordinate orbit, every lower and upper target has degree

\[
 D_q^-=
 \frac{N_0(r)_\ell b_\ell(\ell-q+1)}
      {\binom n{r-q}},
\qquad
 D_q^+=
 \frac{N_0(r)_\ell b_\ell(\ell-q+1)}
      {\binom n{r+q}},
\tag{4.2}
\]

where \(b_\ell=(b)_\ell\).  Equivalently, the uniform owner-perfect
fractional weight \(1/D_0\) gives target loads

\[
 \rho_q^-=
 \frac{N_0}{\binom n{r-q}}
 \frac{\ell-q+1}{\ell+1},
\qquad
 \rho_q^+=
 \frac{N_0}{\binom n{r+q}}
 \frac{\ell-q+1}{\ell+1}.
\tag{4.3}
\]

For a same-phase nested pair \(S\subset X\), \(|S|=r-q\),

\[
 \boxed{
 \frac{\operatorname {codeg}_{\rm same}(X,S)}{D_0}
 =
 \frac{\ell-q+1}{\ell+1}\binom rq^{-1}.}
\tag{4.4}
\]

For \(T\supset X\), \(|T|=r+q\), the corresponding upper ratio is

\[
 \boxed{
 \frac{\operatorname {codeg}_{\rm same}(X,T)}{D_0}
 =
 \frac{\ell-q+1}{\ell+1}\binom bq^{-1}.}
\tag{4.5}
\]

These are lower bounds for the full owner--target codegrees in any
augmented packet hypergraph.

#### Proof

The packet orbit has \(N_0(r)_\ell(b)_\ell\) formal edges, and each edge
has \(\ell-q+1\) distinct targets of either sign.  Coordinate transitivity
on each target layer proves (4.2), and division by (2.4) proves (4.3).

Each lower flag occurrence has one distinguished initial owner containing
it.  The coordinate group is transitive on the
\(N_0\binom rq\) nested pairs \(S\subset X\).  Double-count the
packet/phase incidences to get

\[
 \operatorname {codeg}_{\rm same}(X,S)
 =\frac{(r)_\ell(b)_\ell(\ell-q+1)}{\binom rq}.
\]

Divide by (2.4).  Complementation proves (4.5).  \(\square\)

At \(q=1\), (4.4)--(4.5) are \(\Theta(1/m)\), even when (2.8) is
\(\Theta(1/m^2)\).  An ordinary matching hypergraph which makes flag
targets exclusive hard vertices therefore loses the very codegree gain
seen on the owner shore.  The faithful object is a packing-covering system:
owners are exclusive, targets need coverage, and repetitions up to the
floor quota are allowed.

### Theorem 4.2 (open-path flag capacity)

Let an owner-disjoint family contain \(G\) owner vertices in \(K\) open
paths, every one having at least \(H+1\) vertices.  Let \(h_q^-\) and
\(h_q^+\) be its numbers of missing actual lower and upper targets at
depth \(q\le H\).  Then

\[
 h_q^\pm\ge
 \left[
 \binom n{r\pm q}-(G-qK)
 \right]_+.
\tag{4.6}
\]

In \(J(2m,m)\), if \(G=W\), put

\[
             Q=\left\lfloor\frac{Km}{2W}\right\rfloor.
\tag{4.7}
\]

When \(1\le Q\le H\),

\[
 \sum_{q=1}^{H}(h_q^-+h_q^+)
 \ge \frac K2Q(Q+1)
 =\Omega\!\left(\frac{m^2K^3}{W^2}\right).
\tag{4.8}
\]

If moreover \(\ell=o(m)\), then \(Q=\Theta(m/\ell)\ge1\).  For
essentially uniform \(\ell\)-edge paths, \(K\asymp W/\ell\), so

\[
 \sum_{q=1}^{H}(h_q^-+h_q^+)
 =\Omega\!\left(W\frac{m^2}{\ell^3}\right).
\tag{4.9}
\]

Consequently, under the hypotheses

\[
 G=W,\qquad K\asymp W/\ell,\qquad
 \ell=o(m),\qquad 1\le Q\le H,
\tag{4.9a}
\]

aggregate \(o(W)\) flag repair requires
\(\ell=\omega(m^{2/3})\).  No such conclusion follows from this floor
argument when \(Q=0\), in particular not uniformly near \(\ell=m\).

#### Proof

A path with \(g\) vertices has at most \(g-q\) windows of \(q\) edges.
Summing gives at most \(G-qK\) lower and upper occurrences, proving
(4.6).

For the central even layers,

\[
 \frac{\binom{2m}{m-q}}W
 =\prod_{j=0}^{q-1}\left(1-\frac{2j+1}{m+j+1}\right).
\]

The elementary inequality
\(1-\prod_j(1-x_j)\le\sum_jx_j\) gives

\[
               W-\binom{2m}{m-q}\le\frac{Wq^2}{m}.
\tag{4.10}
\]

For \(1\le q\le Q\), (4.6) is therefore at least

\[
 qK-\frac{Wq^2}{m}\ge\frac{qK}{2}
\]

for each sign.  Sum over \(q\le Q\) to obtain (4.8).  Under
\(\ell=o(m)\) and \(K\asymp W/\ell\), one has
\(Q=\Theta(m/\ell)\), and substitution gives (4.9).  \(\square\)

There is an exact first-row endpoint.  In the globally geodesic central
catalogue every path has at most \(m+1\) owners.  Complete internal
depth-one support would require

\[
 W-K\ge\binom{2m}{m-1}=W-\frac{W}{m+1}.
\]

Thus \(K\le W/(m+1)\), whereas the path-length bound gives the reverse
inequality.  Equality forces \(K=W/(m+1)\) and \(\ell=m\) on every path,
which restores the antipodal codegree (2.9).  Exact internal first-row
coverage and the \(m^{-2}\) truncated-path regime are incompatible.
Asymptotically, \(O(W/\ell)\) explicit first-row repairs are harmless when
\(\ell\to\infty\).

## 5. Exact literal compiler interface

The following theorem answers what \(H\)-safe packets do and do not supply.

### Theorem 5.1 (blockwise packet literalization)

Let \({\cal P}\) be an owner-disjoint family of compiler-\(H\)-safe
Johnson paths in \(J(k,r)\), with \(M\) selected owners and \(p\)
components.  Put \(W=\binom kr\), and let
\(h_q^-,h_q^+\) be the actual target holes of the internal traces
(1.2).  Assume \(1\le H<r\).  For the symmetric lower/upper statement
assume in addition \(H\le k-r\); otherwise truncate the upper depths at
\(k-r\).

Then there is a nonzero literal word covering every selected trace through
depth \(H\), every middle owner, and every missing central-band target, of
length

\[
 \boxed{
 L_H\le
 W+Hp+\sum_{q=1}^{H}(h_q^-+h_q^+).}
\tag{5.1}
\]

#### Proof

For one path \(P=(T_0,\ldots,T_{\ell-1})\), give it a physical block of
length \(\ell+H\) and define its endpoint-capped maximal envelope

\[
 E_s=
 \bigcap_{\substack{0\le i<\ell\\s\in[i,i+H]}}T_i.
\tag{5.2}
\]

Condition \(P_H\) is exactly the coordinatewise condition ensuring

\[
                         D^HE=T.
\tag{5.3}
\]

Every entry is nonempty because at most \(H<r\) initial coordinates can
be lost in a window of \(H\) transitions.  Moreover,

\[
 (D^{H-q}E)_{i+q}=L_{q,i},
\qquad
 (D^{H+q}E)_i=U_{q,i}
\tag{5.4}
\]

whenever the indicated path window exists.  Thus the block realizes all
its actual traces literally and costs \(\ell+H\).

Concatenate the \(p\) blocks.  Append each of the \(W-M\) unused middle
owners as a one-letter word, and append one literal letter for every
missing target counted by the \(h_q^\pm\).  Cross-boundary unions can only
add occurrences and do not destroy any existing one.  The total length is

\[
 M+Hp+(W-M)+\sum_q(h_q^-+h_q^+),
\]

which is (5.1).  \(\square\)

Therefore full wreaths are unnecessary for the asymptotic literal
compiler.  If \(H/\sqrt m\to\infty\) slowly, the proved outer-tail
construction may be appended.  Conditions

\[
 Hp=o(W),\qquad
 \sum_{q\le H}(h_q^-+h_q^+)=o(W)
\tag{5.5}
\]

then give coefficient one.  If a long-packet selection uses
\(p_0=O(W/\ell)\) packets and one deliberately completes its \(R\) unused
owners by endpoint-capped singleton packets, that optional completion has
packet overhead

\[
                         H(p_0+R).
\tag{5.6}
\]

This is only a sufficient packetized completion.  The proof of Theorem 5.1
instead appends unused owners as ordinary one-letter literals inside the
baseline \(W\), with no \(HR\) toll.  Any genuine restriction on \(R\) must
therefore come from its induced trace holes, not from component topology.

### Corollary 5.1a (defect-tolerant occurrence version)

Let the same construction use \(p\) compiler-\(H\)-safe paths with \(G\)
total owner occurrences, allowing repeated owners.  Let \(h_0\) be the
number of distinct middle owners not occurring, and let \(h_q^\pm\) be the
actual trace holes.  Then

\[
 L_H\le
 G+Hp+h_0+\sum_{q=1}^{H}(h_q^-+h_q^+).
\tag{5.6a}
\]

#### Proof

The endpoint-capped blocks cost \(G+Hp\).  Append each of the \(h_0\)
missing middle owners once and each missing target once.  Repeated owner
occurrences do not invalidate any realized interval.  \(\square\)

If the ambient middle layer has size \(W\), the collision excess of these
occurrences is

\[
 c_{\rm own}=G-(W-h_0),
\tag{5.6b}
\]

so the owner part of (5.6a) is exactly \(W+c_{\rm own}+Hp\).

For a stronger exact finite compiler in which residual lower targets must
be placed compatibly inside the fixed packet blocks, rather than appended
as repairs, the maximal envelope must coordinate an existential interval
injection.

### Theorem 5.2 (multi-packet PCSH, necessary and sufficient)

Assume now that vertex-disjoint paths

\[
 P_a=(T_{a,0},\ldots,T_{a,\ell_a-1}),\qquad a\in[c],
\]

partition the whole middle layer.  Give packet \(a\) the disjoint physical
block

\[
 B_a=[b_a,b_a+\ell_a+H-1]
\]

and central pin intervals

\[
 C_{a,i}=[b_a+i,b_a+i+H]\longmapsto T_{a,i}.
\tag{5.7}
\]

Let \(E_p\) be the maximal envelope, equivalently the intersection of all
central-pin labels whose intervals contain \(p\).  Let \({\mathscr J}\)
be the physical intervals which contain no complete central interval
\(C_{a,i}\), and let

\[
 {\cal L}=\{S\subseteq[k]:1\le|S|<r\}.
\]

For an injection

\[
                         \phi:{\cal L}\hookrightarrow{\mathscr J},
\tag{5.8}
\]

put

\[
 Z_x(\phi)=
 \{p:x\in E_p\}\setminus
 \bigcup_{S:\,x\notin S}\phi(S).
\tag{5.9}
\]

There is a nonzero word \(A\) realizing every central pin and every
lower target \(S\) exactly on \(\phi(S)\) if and only if

\[
 \phi(S)\cap Z_x(\phi)\ne\varnothing
 \quad(S\in{\cal L},\ x\in S),
\tag{5.10}
\]

\[
 C_{a,i}\cap Z_x(\phi)\ne\varnothing
 \quad(x\in T_{a,i}),
\tag{5.11}
\]

and

\[
                         \bigcup_xZ_x(\phi)=\bigcup_aB_a.
\tag{5.12}
\]

When these conditions hold, the entrywise maximal realization is

\[
                         A_p=\{x:p\in Z_x(\phi)\}.
\tag{5.13}
\]

Every interval in \({\mathscr J}\) has at most \(H\) positions when it
lies in one packet block, crosses at most one packet boundary, and has at
most \(2H\) positions in all cases.

#### Proof

Every realization of the central pins is entrywise contained in \(E\).
A lower-rank target interval cannot contain a complete central pin, since
its union would contain an \(r\)-set.  Thus its witness lies in
\({\mathscr J}\), and distinct target values require distinct witness
intervals.

Once \(\phi\) is fixed, a coordinate \(x\notin S\) is forbidden throughout
\(\phi(S)\).  Removing all such forbidden occurrences from \(E\) gives
exactly (5.9).  Conditions (5.10), (5.11), and (5.12) are respectively
the positive-coordinate requirements for lower witnesses, central pins,
and nonzero letters.  They prove necessity.  Conversely (5.13), together
with those three conditions, realizes every demanded equality, proving
sufficiency.

An interval of \(H+1\) positions inside one block contains a central pin.
An interval crossing two packet boundaries contains a whole intervening
block and hence a central pin.  At one boundary, avoiding the final central
pin on the left and the first on the right permits at most \(H\) positions
on either shore.  This proves the locality statements.  \(\square\)

For \(1\le q\le H\), a designated lower flag

\[
 S=L_{q,i}
\]

survives literally by imposing

\[
              \phi(S)=[b_a+i+q,b_a+i+H].
\tag{5.14}
\]

All upper packet flags survive automatically from
\(D^{H+q}A=D^qT\).  Hence \(H\)-safety plus complete setwise flag support
already suffices for the extra-letter provider-union theorem 5.1.  In the
stronger fixed-block, no-repair problem, where a compatible interval
injection for prescribed residual targets must be found, the exact
remaining conditions are (5.10)--(5.12), the packet-PCSH gate.

An ordinary Hall graph or a hypersimplex marginal decomposition cannot
replace these statewise positive-coordinate conditions.  Abstractly, take
targets \(S_i=\{a,e_i\}\), cells \(I_j=\{j-1,j\}\), and envelope
\(\{a,e_1,\ldots,e_M\}\) at every position.  Declare every target eligible
for every cell, so the ordinary graph is \(K_{M,M}\).  Under any bijection,
only the two endpoint cells can retain their assigned private markers;
at least \(M-2\) internal target equalities fail.  This is a genuine
statewise PCSH obstruction, although it is not asserted here to be an
embedded Johnson-packet counterexample.

## 6. Why retained PBBS fragments do not escape

The PBBS factor already supplies complete all-depth flag support.  One
might cut it into unsafe fragments and use the ambient Johnson degree to
resew them.  The following theorem gives the exact boundary.

### Theorem 6.1 (PBBS fragment rebundling with charts)

Delete \(J\) transitions from the complement-projected PBBS owner cycles.
Retain every resulting path interior, with either orientation, and sew the
fragments into \(p\) compiler-\(H\)-safe Johnson paths partitioning all
\(W\) owners.  Then there is a literal central-band word of length at most

\[
 \boxed{
                         W+Hp+(4H-1)J.}
\tag{6.1}
\]

#### Proof

Endpoint-capped erosion of the new safe paths costs \(W+Hp\).  Fix, for
each required target through depth \(H\), one canonical PBBS witness
window.  If its old window meets no deleted edge, it remains inside one
retained fragment; reversal only reverses an intersection or union and
does not change its value.

If the witness crosses one or more deleted edges, choose one crossed edge.
The proved dominance-staircase chart at that old PBBS cut has length
\(4H-1\) and realizes every floor-correct lower crossing window and every
upper crossing union through depth \(H\).  Append one such chart for every
deleted edge.  A multi-cut witness is charged to any one of its crossed
edges, and cyclic boundaries are themselves among the deleted cuts.  Thus
all canonical PBBS targets are restored within (6.1).  \(\square\)

### Theorem 6.2 (mandatory residence transversal)

In the setting of Theorem 6.1, let \(\tau_H(P_m)\) be the minimum
transition-edge transversal of the old PBBS positive residence intervals
of length at most \(H\).  Then

\[
 \boxed{
                  J\ge\tau_H(P_m)\ge\nu_H(P_m).}
\tag{6.2}
\]

#### Proof

Any old short residence interval containing no deleted transition lies
wholly in a retained fragment.  It remains an internally bounded short
positive run after the fragment is reversed or reoriented.  Therefore a
compiler-\(H\)-safe output requires the deleted set to meet every such
interval.  This is exactly \(J\ge\tau_H\).  Every transversal has size at
least a maximum edge-disjoint interval packing, giving
\(\tau_H\ge\nu_H\).  \(\square\)

The \(\Theta(m^2)\) seam supply acts only after these mandatory cuts.  It
cannot improve the PBBS residence scale.  To use the new packet geometry,
one must replace bulk transitions rather than retain PBBS interiors, and
then solve the target service problem anew.

There is also a saturated first-row obstruction.  On the projected PBBS
owner transition,

\[
                         X_i\cap X_{i+1}=A_{i+1},
\tag{6.3}
\]

and the \(A_{i+1}\)'s enumerate all \(W\) rank-\(m\) targets exactly once.
Deleting any old transition therefore deletes a unique canonical
depth-one witness.  A path cover of all \(W\) owners with \(p\) components
has only \(W-p\) internal transitions, hence at least \(p\) internal
first-row holes.  Replacement seams or explicit boundary charts are
unavoidable.

## 7. A positive first-shadow conveyor

The depth-one loss can be avoided without a wreath by taking the saturated
row itself as the packet universe.

### Theorem 7.1 (lower-row path conveyor)

Let

\[
 C_0,C_1,\ldots,C_{\ell-1}
\]

be a simple path of rank-\(m\) sets in \(J(2m+1,m)\), where \(\ell\ge2\).
Assume at every
internal index that

\[
 C_{i-1}\setminus C_i\ne C_{i+1}\setminus C_i.
\tag{7.1}
\]

Choose

\[
 u\notin C_0\cup C_1,\qquad
 v\notin C_{\ell-2}\cup C_{\ell-1},
\]

and define rank-\((m+1)\) owners

\[
 T_0=C_0\cup\{u\},
\tag{7.2}
\]

\[
 T_i=C_{i-1}\cup C_i\quad(1\le i<\ell),
\tag{7.3}
\]

\[
 T_\ell=C_{\ell-1}\cup\{v\}.
\tag{7.4}
\]

Then consecutive \(T_i\)'s are Johnson adjacent and

\[
                         T_i\cap T_{i+1}=C_i
                         \quad(0\le i<\ell).
\tag{7.5}
\]

For every \(q\ge1\) and every available window,

\[
 \boxed{
 \bigcap_{j=0}^{q}T_{i+j}
 =
 \bigcap_{j=0}^{q-1}C_{i+j}.}
\tag{7.6}
\]

#### Proof

For an internal transition, write

\[
 T_i=C_i\cup(C_{i-1}\setminus C_i),\qquad
 T_{i+1}=C_i\cup(C_{i+1}\setminus C_i).
\]

The two displayed extras are distinct by (7.1), so these are adjacent
\((m+1)\)-sets with intersection \(C_i\).  The choices of \(u,v\) prove
the endpoint cases.  Equation (7.6) follows by intersecting the adjacent
identities (7.5).  \(\square\)

If a family of \(p\) such \(C\)-paths partitions all \(W\) rank-\(m\)
sets, its lifted \(T\)-paths have \(W+p\) owner occurrences and preserve
the complete rank-\(m\) first-shadow row exactly.  Let

* \(h_0\) be the number of missing distinct rank-\((m+1)\) owners among
  the lifted occurrences;
* \(h_q^-\) for \(q\ge2\) be the deeper lower target holes; and
* \(h_q^+\) for \(q\ge1\) be the upper target holes.

The number of distinct lifted owners is \(W-h_0\), so their exact collision
excess is

\[
 (W+p)-(W-h_0)=p+h_0.
\tag{7.6a}
\]

If the lifted paths are compiler-\(H\)-safe, Corollary 5.1a gives

\[
 \boxed{
 L_H\le
 W+(H+1)p+h_0+
 \sum_{q=2}^{H}h_q^-+
 \sum_{q=1}^{H}h_q^+.}
\tag{7.7}
\]

This is the clean non-wreath positive target:

\[
 p=O(W/m),\qquad
 h_0+\sum_{q=2}^{H}h_q^-+\sum_{q=1}^{H}h_q^+=o(W).
\tag{7.8}
\]

Here "essentially distinct" can only mean the quantitative condition
\(p+h_0=o(W)\); the lifted paths are never literally owner-disjoint.  A
packet-PCSH certificate is needed only if prescribed targets must be
installed compatibly inside these fixed blocks without the explicit repair
letters already counted in (7.7); PCSH chooses the interval injection even
when its intervals were not prescribed in advance.

## 8. The faithful packet problem and the proved boundary

For any packet catalogue \({\cal P}\), introduce binary variables \(z_P\).
The faithful owner-packing and flag-cover system is

\[
 \sum_{P\ni X}z_P\le1
 \quad\left(X\in\binom{[n]}r\right),
\tag{8.1}
\]

\[
 \sum_{\substack{P,t\\L_{q,t}(P)=S}}z_P+r_{q,S}^-\ge1,
\tag{8.2}
\]

\[
 \sum_{\substack{P,t\\U_{q,t}(P)=T}}z_P+r_{q,T}^+\ge1,
\tag{8.3}
\]

with integral repair variables \(r_{q,S}^\pm\ge0\).  Target resources are
covering colors, not exclusive matching vertices; their desired
multiplicities differ by rank.

If

\[
 R=W-\sum_P|V(P)|z_P,
\]

the unused owners are appended as ordinary one-letter literals inside the
baseline \(W\).  The exact excess objective supplied by Theorem 5.1 is

\[
 H\sum_Pz_P
 +\sum_{q,S}r_{q,S}^-+\sum_{q,T}r_{q,T}^+.
\tag{8.4}
\]

Adding \(HR\) is an optional stronger objective only if every unused owner
is deliberately made into an endpoint-capped singleton packet.

A theorem making (8.4) \(o(W)\), followed by the proved outer-tail
construction, gives coefficient one.  The numerical regime

\[
 H=\sqrt m\,\omega(m),\qquad
 m^{2/3}\ll\ell=o(m),\qquad H=o(\ell),
\tag{8.5}
\]

is not excluded by the two deterministic costs: \(O(W/\ell)\) long packets
cost \(o(W)\), and the lower bound (4.9) itself is \(o(W)\).  This says only
that the unavoidable counting obstruction vanishes; it does **not** prove
that the actual flag holes are \(o(W)\).

What is not proved is an integral solution of (8.1)--(8.3) with (8.4)
\(o(W)\).  The exact obstructions to inferring it from owner codegrees are:

1. the long-return kernel (3.4) for locally safe walks;
2. the unavoidable first-flag fibre (4.4)--(4.5);
3. the open-window capacity (4.6)--(4.9);
4. the simultaneous lower/upper flag cover, rather than independent
   rankwise balancing; and
5. packet-PCSH only for the stronger fixed-block, no-repair compiler.

Fixing a complete ordered lower and upper flag at every root destroys the
new entropy: the nested flag differences determine the first departure and
arrival, and a compatible successor must shift the same queues.  In a
fixed SCD/PBBS flag assignment the root-state compatibility graph therefore
has outdegree at most one.  The \(m^2\) entropy is available only if flag
witnesses are allowed to migrate between roots.  This is why the packet
hypergraph must be target-decorated.

The proved conclusion is therefore:

\[
\boxed{
\begin{array}{c}
\text{Long compiler-safe Johnson packets can replace wreaths in the
literal interface,}\\
\text{but \(H\)-safety and owner packing alone do not preserve the
all-depth flag tower.}
\end{array}}
\tag{8.6}
\]

The exact next theorem is a target-decorated safe-path near-tiling, or the
defect-tolerant first-shadow conveyor version (7.8).  Packet-PCSH is a
separate strengthening when repairs are forbidden.  This is a strictly
different problem from Hamiltonizing PBBS.
