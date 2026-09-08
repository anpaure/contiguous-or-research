# A bounded phased local bank extends to an ordered two-SDR

**Date:** 2026-08-12
**Method:** Ore--Ryser with selected and forbidden edges, followed by a
private alternating path completion
**Status:** unconditional abstract extension theorem for one bounded
common-core occurrence bank.  It applies to the common-mate MNW `C8`
partial bank after its endpoint incidences are fixed.  It does **not**
produce the suffix-cylindrical recursive module, protect `q>=3` crossing
windows, or prove the required terminal socket action.

## 1. Setup

Let `ML_m` be the bipartite containment graph between

\[
 {\cal L}={ [2m-1]\choose m-1},\qquad
 {\cal U}={ [2m-1]\choose m}.
\]

It is `m`-regular and both shores have size

\[
                         W={2m-1\choose m}.
\]

The existing small protected-factor theorem says that every
`P subset ML_m` with

\[
                         \Delta(P)\le2,
 \qquad |E(P)|\le m-2                                    \tag{1.1}
\]

is contained in a spanning two-factor.  We first add a forbidden bank.

## 2. Selected and forbidden edges

### Theorem 2.1 (small protected-and-forbidden factor theorem)

Let `P,N subset E(ML_m)` be disjoint.  If

\[
 \Delta(P)\le2,
 \qquad |E(P)|+|N|\le m-2,                              \tag{2.1}
\]

then `ML_m` has a spanning two-factor `F` such that

\[
                         P\subset F,
 \qquad F\cap N=\varnothing.                            \tag{2.2}
\]

#### Proof

Suppose otherwise, and choose an inclusion-minimal `H subset P` for which
no two-factor contains `H` while avoiding `N`.  Put

\[
 b(v)=2-d_H(v),\qquad G_0=ML_m-E(H)-N.                  \tag{2.3}
\]

Ore--Ryser supplies `A subseteq cal L` such that

\[
 \sum_{x\in A}b(x)>
 \sum_{U\in{\cal U}}\min\{b(U),d_{G_0}(U,A)\}.          \tag{2.4}
\]

No edge of `H` meets `A`.  Indeed, deleting an edge `xU` of `H` with
`x in A` raises the left side of (2.4) by one, while restoring that edge
and raising `b(U)` can raise the right side by at most one.  The strict
integer violation survives, contrary to the minimality of `H`.

Write

\[
 a=|A|,\qquad c=W-a,
 \qquad h=|E(H)|.                                      \tag{2.5}
\]

Let

\[
 S_2(A)=\sum_{U\in{\cal U}}\min\{2,d_A(U)\}.
\]

The middle-shadow theorem gives

\[
 S_2(A)-2a\ge\min\{m-2,2c\}.                         \tag{2.6}
\]

First suppose we are in the first case of the proof of (2.6), so

\[
                         S_2(A)-2a\ge m-2.
\]

Put

\[
 n_U=d_N(U,A).
\]

Since no edge of `H` meets `A`, termwise

\[
 \min\{2-d_H(U),d_A(U)-n_U\}
 \ge \min\{2,d_A(U)\}-d_H(U)-n_U.                    \tag{2.7}
\]

Thus (2.4) implies

\[
 h+|N\cap E(A,{\cal U})|>S_2(A)-2a\ge m-2,           \tag{2.8}
\]

contradicting (2.1).

It remains to consider the second case of (2.6).  Then `c<m-1`,
`N(A)={\cal U}`, and every upper vertex has

\[
                         d_A(U)\ge m-c\ge2.          \tag{2.9}
\]

neighbours in `A`.  Put `h_U=d_H(U)` and

\[
 \delta_U=
 \bigl(2-h_U-(d_A(U)-n_U)\bigr)_+,
 \qquad D=\sum_U\delta_U.                            \tag{2.10}
\]

The right side of (2.4) is exactly `2W-h-D`; hence (2.4) says

\[
                         h+D>2c.                    \tag{2.11}
\]

If `D=0`, this contradicts `h<=2c`, because every lower endpoint of `H`
lies in the `c`-vertex complement of `A` and has `H`-degree at most two.
If `D>0`, then at every upper vertex contributing to `D`,

\[
 n_U=\delta_U+d_A(U)-2+h_U
 \ge\delta_U+(m-c-2)+h_U.
\]

Consequently

\[
 |N\cap E(A,{\cal U})|
 \ge D+(m-c-2),                                      \tag{2.12}
\]

and, using the integral form `h+D>=2c+1` of (2.11),

\[
 |E(P)|+|N|
 \ge h+D+m-c-2
 \ge m+c-1
 \ge m-1,                                           \tag{2.13}
\]

again contradicting (2.1).  This proves (2.2).  \(\square\)

The theorem is stronger than merely finding two uncoloured matchings:
it permits every proposed new edge of a switch to be declared initially
forbidden.

## 3. Phase-compatible ports

Let a subgraph be properly edge-coloured by phases `0,1`.  At an endpoint
`v` of a nontrivial coloured path, let `c(v)` be the colour of its unique
incident edge, and put

\[
 \epsilon(v)=c(v)\mathbin\oplus
 \mathbf 1_{\{v\in{\cal U}\}}.                      \tag{3.1}
\]

### Lemma 3.1 (port parity)

The two endpoints of every properly two-coloured path have opposite
`epsilon` values.  Two endpoints can be joined by an incidence path whose
edge colours alternate and extend the old colouring if and only if their
`epsilon` values are opposite.

#### Proof

For a path of odd length, its endpoints lie on opposite shores and its
first and last edges have the same colour.  For a path of even length,
the endpoints lie on the same shore and the endpoint colours are
opposite.  Both statements are exactly (3.1).  The same parity calculation
with the two missing endpoint colours proves the joining assertion.
\(\square\)

Thus every coloured path has one `epsilon=0` port and one `epsilon=1`
port.  Any prescribed list of such path components can be concatenated by
joining the `1` port of one to the `0` port of the next.

## 4. Private connectors in a bounded face

Fix an integer `t>=1` and a common set

\[
                         |C|=m-1-t.                 \tag{4.1}
\]

The **bounded face over `C`** consists of the lower and upper vertices
containing `C`; after deleting `C` these have sizes `t` and `t+1` in a
ground set of size `m+t`.

### Lemma 4.1 (bounded-face private connector)

Fix `t` and `s`.  For all sufficiently large `m`, any at most `s`
phase-compatible pairs of distinct ports in the bounded face can be joined
by pairwise internally vertex-disjoint incidence paths, avoiding any
prescribed bank of at most `s` vertices and edges.  Every joining path has
length at most

\[
                         4t+10.                     \tag{4.2}
\]

#### Proof

For every requested connector choose one private marker `z`, outside the
noncommon supports of both endpoints and every earlier connector.  Also
reserve a distinct core label for each upper-endpoint escape; the core has
unbounded size while the number of escapes is fixed.

A lower endpoint `C union A`, `|A|=t`, can be moved in two incidence edges
to a lower face vertex containing the private marker by one swap
`a -> z`.

For an upper endpoint `C union A`, `|A|=t+1`, choose distinct
`a,b in A`, a private `c in C`, and a private `z` outside the endpoint.
The five-edge path

\[
\begin{aligned}
 C+A
 &\supset (C-c)+A
 \subset (C-c)+A+z\\
 &\supset (C-c)+(A-a)+z
 \subset C+(A-a)+z\\
 &\supset C+(A-a-b)+z
\end{aligned}                                        \tag{4.3}
\]

ends at a lower vertex of the bounded face.  The private choices make all
internal vertices new and avoid the forbidden bank.  The first internal
vertex in (4.3) is distinguished by its reserved missing core label; every
later one contains the private outside label `z`.

Now connect the two resulting lower `t`-sets through a `t`-set `Z`
containing `z`: swap the first set to `Z` one element at a time without
ever removing `z`, then `Z` to the second set under the same rule.  This
uses at most `4t` incidence edges.  Every internal vertex contains the
marker private to this connector, except the first internal vertex of an
upper escape, which is instead distinguished by its reserved missing core
label.  Hence different connectors and the forbidden bank cannot meet.
Adding the two endpoint escapes gives (4.2).  Finally colour the path
alternately; Lemma 3.1 gives the required colour at both ends. \(\square\)

The constant is deliberately coarse.  Its role is that it is independent
of `m`.

## 5. Ordered two-SDR extension

### Theorem 5.1 (bounded phased-bank extension)

Fix `t,p,n`.  For all sufficiently large `m`, let

* `P=P_0 dotcup P_1` be a properly two-edge-coloured linear forest in one
  bounded face, with at most `p` edges;
* `N` be a bank of at most `n` initially forbidden incidences, disjoint
  from `P`; and
* an order and orientation of the nontrivial components of `P` be given
  such that consecutive exposed ports have opposite `epsilon` values.

Then there is an ordered pair `(M_0,M_1)` of edge-disjoint perfect
matchings of `ML_m` such that

\[
                         P_i\subset M_i,
 \qquad (M_0\cup M_1)\cap N=\varnothing,             \tag{5.1}
\]

and the components of `P` occur in the prescribed order on one oriented
path segment of `M_0 union M_1`.

#### Proof

Use Lemma 4.1 to join the coloured path components in the prescribed
order.  The result is one properly coloured path `Q superset P`, avoiding
`N`, with

\[
 |E(Q)|
 \le p+(p-1)(4t+10).                                \tag{5.2}
\]

For sufficiently large `m`,

\[
                         |E(Q)|+|N|\le m-2.          \tag{5.3}
\]

Apply Theorem 2.1 to obtain a spanning two-factor `F` containing `Q` and
avoiding `N`.  The component of `F` containing `Q` is an even cycle.
Its alternating edge-colouring has a unique orientation extending the
colours already fixed on `Q`; colour every other cycle arbitrarily.
The two colour classes are edge-disjoint perfect matchings `(M_0,M_1)`.
The orientation of `Q` gives the prescribed component order. \(\square\)

Closed properly coloured components may be retained separately: they are
already saturated factor components, while Theorem 5.1 is applied to the
linear part.

## 6. Application to the common-mate MNW bank

In one fixed suffix fibre, every ten-prefix-bit MNW owner and colour has a
common suffix core of size `m-6`; hence the local bank lies in the case

\[
                         t=5.                       \tag{6.1}
\]

The old banks of

* the phase-zero contextual source `C8`,
* the phase-one detour creator `C8`, and
* the four common mates

form a proper two-coloured linear forest.  Their complementary new banks
are a finite forbidden set.  The same remains true after adjoining any
fixed finite list of explicitly prescribed replacement-endpoint
incidences, provided those incidences respect the phase-port condition of
Lemma 3.1.

Therefore Theorem 5.1 proves:

> **One-occurrence abstract extension.**  The common-mate `C8` partial
> old bank extends to an ordered two-SDR avoiding its complete new bank in
> every sufficiently large `ML_m`.  Any explicitly supplied endpoint-
> relocation incidences may be retained as well, provided their union with
> the old bank is a proper two-coloured linear forest.

This removes ordinary matching extendability and phase colouring as
obstructions for one bounded occurrence.  In particular, no additional
matroid-intersection theorem is needed at this scale.

This statement deliberately distinguishes an **edge-specified** relocation
from a permutation-only socket request.  If the desired immediate
successor arcs are already realized by the protected incidences, they are
retained.  If only their endpoint permutation is named, the private
connectors prove merely the requested order with unspecified intermediate
owners; they do not realize the exact partial successor map `omega`.

## 7. Exact scope boundary

The theorem does **not** prove the required all-dimensional MNW host.

1. The direct sum over all Dyck suffix fibres has Catalan many prescribed
   edges, so (5.3) cannot be applied by summing the fibres.
2. The arbitrary private connector path need not preserve `q>=3`
   cross-windows, residence, or the inherited recursive attachment marks.
3. Although a chosen compatible component order is realized, insertion of
   private intermediate owners is not the exact occurrence-level socket
   chronology required by the MNW recursive module.
4. It supplies an ambient ordered two-SDR, not a finite subtree replacement
   with the same exported MNW terminal partition.

Thus the remaining phase gate is not abstract two-SDR existence.  It is
the **connector-faithful recursive occurrence lift** of this bounded local
extension, together with the higher-window and socket signature.
