# Full-private K17 LLR transfers: supplier-rank Benders theorem

**Date:** 2026-08-02  
**Status:** exact optimization formulation and min--max theorem on any
declared row-disjoint LLR-transfer face whose supplier states and protected
rows come from one common parent.  The present finite calibration has
`4,803` edges after a transplanted row-ID footprint filter, maximum transfer
matching `470`, and a warm47-derived table with supplier rank
`16,872/16,898`.  Its `7,213` excluded row IDs were assembled from a private
bank materialized on a different parent, so this finite object is **not yet
a literal private-bank-preservation certificate**.  The note does not prove
that rank `16,898` is attainable, nor does it close common state, chronology,
residence, upper, source, compiler, or word gates.

## 1. Transfer master

Let `D` be the old `L-M-R` donor rows and `H` the old direct `L-R` host
rows.  A transfer edge `e=dh` is admitted only when

1. the donor low target is a strict subset of the host low target;
2. the new `M-R` short is marginally positive in both required phases;
3. the declared private/protected tests pass on the same materialized parent;
   and
4. neither endpoint is one of the declared protected rows.

For the current calibration, condition 3 has only been checked as a
transplanted **row-footprint** exclusion: the transfer table is warm47 while
the private-bank materialization is the authenticated `b268...` parent.  It
produces a graph `J_P subseteq D times H` with `4,803` edges and maximum
matching size `470`, but literal ticket values must be replayed on one common
parent before calling that graph full-private.

For `z_e in {0,1}`, the exact maximum-transfer face is

\[
\begin{aligned}
 \sum_{e\ni d}z_e&\le1 &&(d\in D),\\
 \sum_{e\ni h}z_e&\le1 &&(h\in H),\\
 \sum_ez_e&=470.                                            \tag{1.1}
\end{aligned}
\]

Every solution preserves all named targets, roots, owners, the length
histogram, and every excluded row ID.  When the exclusion ledger and tickets
are replayed on the same parent, it also preserves those literal protected
rows.  Its chain-type ledger is forced to be

\[
 (LLR,LMR,LR,MR)=(470,16445,4392,3003).                    \tag{1.2}
\]

Dropping the last equality gives the full downward row-disjoint face; a
lexicographic optimization may instead maximize transfer cardinality before
supplier rank.

## 2. Row states and primitive supplier incidences

The new state of a host is **edge-labelled**.  If `e=dh`, its new `LLR`
payload is

\[
                  (\ell_d,u_h,r_h),                          \tag{2.1}
\]

so different donors incident with the same host generally give different
states.  Collapsing all selected states of a host to one bit is unsound.

For every row `v` let `Sigma_v` consist of its old mode `0` and one mode
labelled by each incident transfer edge.  Put

\[
 s_{v,0}=1-\sum_{e\ni v}z_e,
 \qquad
 s_{v,e}=z_e\quad(e\ni v).                                  \tag{2.2}
\]

Exactly one mode is active.  For a donor, all selected edge-labelled modes
have the same `MR` payload and may optionally be quotiented after their
activation provenance is no longer needed.  For a host they must remain
distinct because (2.1) contains `ell_d`.  Every row outside `J_P` has only
its fixed mode zero.

Let

\[
 K_{uv}^{\sigma\tau}\in\{0,1\}                       \tag{2.3}
\]

be the independently replayable generalized supplier predicate saying that
supplier row `u` in state `sigma` can serve hard-head row `v` in state
`tau`.  Only hard states are retained on the head shore.  Define exact
primitive activation variables

\[
 w_{uv}^{\sigma\tau}
 =K_{uv}^{\sigma\tau}s_{u,\sigma}s_{v,\tau}.                \tag{2.4}
\]

For a retained predicate, (2.4) is linearized by

\[
 w\le s_{u,\sigma},\quad w\le s_{v,\tau},\quad
 w\ge s_{u,\sigma}+s_{v,\tau}-1.                           \tag{2.5}
\]

The lower AND row is load-bearing in any Benders cut that counts available
neighbours; unsupported `w=1` would create false suppliers.

## 3. Exact integrated matching model

For every compatible mode edge use a matching variable
`q_(uv,sigma,tau)` and impose

\[
\begin{aligned}
 q_{uv}^{\sigma\tau}&\le w_{uv}^{\sigma\tau},\\
 \sum_{v,\sigma,\tau}q_{uv}^{\sigma\tau}&\le1 &&(u),\\
 \sum_{u,\sigma,\tau}q_{uv}^{\sigma\tau}
   &\le \sum_{\tau\text{ hard}}s_{v,\tau} &&(v).           \tag{3.1}
\end{aligned}
\]

Together with (1.1), maximizing

\[
                       \sum_{u,v,\sigma,\tau}q_{uv}^{\sigma\tau} \tag{3.2}
\]

is an exact 0--1 optimization model for supplier rank on this transfer
face.  It contains no marginal approximation: a supplier edge is usable
only in the two selected physical row states, every supplier identity is
used at most once, and every active hard head is matched at most once.

This is a proof-safe MILP, not a total-unimodularity claim.  The transfer
matching and supplier matching are individually integral, but their
state-AND coupling need not be.

## 4. Why ordinary transfer weights are insufficient

Supplier rank is not additive over transfer edges, even when the transfer
edges are row-disjoint.

* **Redundancy:** two transfers may activate two suppliers for the same one
  head.  Each alone raises rank by one, while selecting both still raises it
  by one.
* **Synergy:** one transfer may activate the supplier state of a primitive
  edge and another row-disjoint transfer may activate its head state.  Each
  alone has zero gain, while the pair has gain one.

No assignment of fixed per-transfer weights represents either pattern for
all subsets.  The second pattern is exactly the product in (2.4).  Thus
pointwise supplier-absence or degree scores are legitimate seed weights,
but they cannot certify the joint supplier rank.

## 5. Sharp min--max statement

Let `mathcal M_470(J_P)` be the set of size-470 matchings in the transfer
graph.  For `z` in this family, let `G_z` be its exact active supplier graph
and `H_z` its `16,898` active hard heads.  By the deficiency form of Hall's
theorem,

\[
 \nu(G_z)=16898-\delta(z),\qquad
 \delta(z)=\max_{X\subseteq H_z}
                  \bigl(|X|-|N_{G_z}(X)|\bigr).             \tag{5.1}
\]

Therefore the exact Pareto value is

\[
 \boxed{
 \max_{z\in\mathcal M_{470}(J_P)}\nu(G_z)
 =16898-
   \min_{z\in\mathcal M_{470}(J_P)}
   \max_{X\subseteq H_z}
       \bigl(|X|-|N_{G_z}(X)|\bigr).
 }                                                            \tag{5.2}
\]

The current selected table has

\[
 \nu(G_z)=16872,qquad\delta(z)=26,                          \tag{5.3}
\]

with `23` zero heads.  One maximum-deficiency DM shore has `36` active
heads and only `10` supplier identities.  Thus the shore deficit is exactly
`36-10=26`; zero-head repair alone is not a proof of perfect supplier rank.

## 6. Exact Hall--Benders cuts

Use one fixed universe of potential mode-labelled hard-head occurrences.
For a potential occurrence `h`, let `a_h(z)` be its exact active-state
literal.  For a fixed occurrence set `X` and supplier identity `u`, define

\[
 n_{X,u}(z)=
 \bigvee_{h\in X,\sigma,\tau}
       w_{uh}^{\sigma\tau},                                 \tag{6.1}
\]

where only mode edges ending at the declared occurrence of `h` enter the
OR.  Encode (6.1) bidirectionally:

\[
 n_{X,u}\ge w_e\ (e\text{ in the OR}),\qquad
 n_{X,u}\le\sum_{e\text{ in the OR}}w_e.                   \tag{6.2}
\]

For a requested supplier deficiency at most `k`, the globally valid Hall
row is

\[
 \boxed{
   \sum_{h\in X}a_h(z)-\sum_u n_{X,u}(z)\le k.
 }                                                            \tag{6.3}
\]

At an integral transfer matching, build `G_z`, compute one maximum supplier
matching, and return a maximum-deficiency DM shore `X`.  If (6.3) fails,
add its exact activation AND/OR rows.  Repeating this process is an exact
finite Benders algorithm for the decision problem

\[
                         \nu(G_z)\ge16898-k.                  \tag{6.4}
\]

No supplier augmenting-circuit catalogue is needed for correctness: one
maximum matching plus alternating-reachability/min-cut supplies the minimal
recourse oracle.  A naked cut on the current `36` head IDs is unsound if it
continues to count a head after its row changes state; the activity terms
`a_h(z)` in (6.3) are essential.

For the frozen `36/10` shore, beating the present rank requires

\[
 \sum_{h\in X}a_h(z)-\sum_u n_{X,u}(z)\le25,                \tag{6.5}
\]

while supplier perfection requires the same left-hand side to be at most
zero for every generated shore.

## 7. Minimal circuit interpretation

Two size-470 transfer matchings differ by row-disjoint alternating cycles
and even alternating paths in `J_P`.  Flipping one such component preserves
(1.1).  A supplier improvement is certified only after the resulting
supplier graph contains an augmenting path relative to its current supplier
matching.

There need not be a single transfer component whose flip improves rank:
the synergy example in Section 4 may require two components simultaneously.
Therefore a search restricted to individually improving fundamental
transfer circuits is incomplete.  The proof-safe alternatives are

1. the integrated model (1.1)--(3.2); or
2. transfer-matching branching with the activated Hall cuts (6.3).

The second is the weaker exact oracle: it exposes only a deficient supplier
shore and the primitive state incidences needed to expand its neighbour
bank.

## 8. Scope

The warm47-derived finite table associated with the current 470-edge matching has type
ledger (1.2) and the audited supplier tuple

\[
 (\text{rank},\text{deficiency},\text{zero heads})
 =(16872,26,23).
\]

These statements concern the generalized warm47 supplier projection and
retention of the transplanted row-ID footprint.  They do not assert literal
retention of the `b268...` private tickets on this different parent, a
simultaneous exact socket-ticket packing, common state circulation, connected
chronology, residence, upper shadows, source/compiler closure, or a
length-24313 word.  Common-parent identity plus complete literal ticket
replay is a prerequisite for promoting the finite face to genuinely
full-private.

## 9. Local artifact bindings

The load-bearing local inputs for the declared transfer face are

```text
e3e14e5831553465148ca87a81aa86bc680fe0ea340591bcf1384c717a67f650
  scratch/q1_k17_llr_socket_matching_20260802/
    llr_fullprivate_socket_matching.audit.json

34838ee1e8d2149feaa5254bcd51fb02f4659c6a35bb77b4938bf2d73f9e674e
  scratch/q1_k17_llr_socket_matching_20260802/
    llr_fullprivate470.table.tsv

66f62610f685418e61f46e17bc9b9b19019500f2a9e5ee3ac5eb75a6301b9911
  scratch/q1_k17_llr_socket_matching_20260802/
    llr_fullprivate_socket_matching.selected.tsv
```

The exploratory random-Pareto source is

```text
22ece7e2a5ef2fa3fbdfca24f2a4f652301a2062c255c1ca4301abf8c6542ff0
  scratch/search_k17_llr_fullprivate_supplier_pareto_20260802.cpp
```

Random sampling is not an optimality certificate.  Equations (3.1)--(6.3),
not that search procedure, define the exact supplier-rank optimization.
