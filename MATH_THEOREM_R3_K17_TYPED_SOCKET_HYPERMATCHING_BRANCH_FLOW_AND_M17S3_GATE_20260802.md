# R3 theorem: typed-socket hypermatching, exact branch--flow oracle, and the M17_s3 state gate

**Date:** 2026-08-02  
**Status:** proof-safe structural theorem and finite calibration.  The outer
short bank retains its exact cotransversal rank oracle.  A private/Rado
socket face gives an ordinary matroid-intersection theorem.  The actual
shared predecessor/successor/state layer is instead a typed hypermatching;
after fixing one endpoint assignment and all shared state, its residual
completion is exactly one bipartite flow.  The authenticated round47
catalogue has a smallest possible augmentation failure.  The current
`M17_s3` carrier has only a supplier-projection audit, so no round47 typed
socket claim is transported to it.  This document does **not** assert a
state-balanced compiler, residence closure, a source chronology, or a
length-24,313 word.

## 0. Verdict

There are three different objects which must not be conflated.

1. The `1748` short hard slots of an outer-feasible bottom table are bases
   of the cotransversal matroid

   \[
                    M_{\rm short}=(M/F)^* .                 \tag{0.1}
   \]

   Its rank and fundamental circuits are ordinary bipartite-matching
   queries.

2. If complete socket tickets have private footprints, or their residual
   conflicts form a matroid, the socket projection is a transversal/Rado
   matroid.  Edmonds' theorem then decides whether it has a common
   `1748`-set with (0.1).

3. A real typed socket consumes a short, one predecessor port and one
   successor port, and couples the two port copies when the same physical
   long role is used on both sides.  This is a stateful three-way matching,
   not a second matroid in general.  The frozen round47 catalogue contains
   a literal three-short augmentation failure, so no gammoid or other
   matroid can represent that hereditary partial-socket family exactly.

The exact replacement for a nonexistent socket rank oracle is:

> branch on the materialized common state and one injective endpoint
> assignment; complete the other endpoint assignment by maximum flow.

This is an exact augmented-state formulation.  It is polynomial at every
fixed branch, but not a polynomial algorithm for the unrestricted problem:
the unrestricted ticket layer contains three-dimensional matching.

## 1. The outer rank oracle remains exact

Let `F` be the `1748` mandatory free receivers and `H` the `18646` eligible
hard slots of the authenticated K17 bottom-token table.  Let `M` be the
transversal matroid on `F dotcup H` presented by the real-token containment
graph.  Its rank is `18646`, while `r_M(F)=1748`.  Put

\[
                     N=M_{\rm short}=(M/F)^* .               \tag{1.1}
\]

Then `r_N(H)=1748`, and for every `S subseteq H`,

\[
\boxed{
 r_N(S)=|S|-18646+
        r_M\bigl(F\mathbin{\dot\cup}(H\setminus S)\bigr).
}                                                            \tag{1.2}
\]

Thus one maximum matching in the real-token containment graph is an exact
rank oracle.  If `B` is a basis and `e notin B`, one alternating search in
the corresponding primal matching gives the full fundamental circuit
`C_N(e,B)` and hence every legal exchange `B-f+e`.

This theorem depends on the bottom-token containment presentation, not on a
carrier score or a marginal socket count.

## 2. Exact typed-socket formulation

Fix an owner phase and a materialized outer table.  Let

- `E` be the candidate short hard slots;
- `P` be the predecessor-port copy of the long roles;
- `Q` be the successor-port copy;
- `Theta` be a complete assignment of every shared flag, history, cap and
  other state which can couple two socket records.

After rejecting every record inconsistent with `Theta`, a completed socket
record has the form

\[
                         g=(e,p,q,a),                        \tag{2.1}
\]

where `e in E`, `p in P`, `q in Q`, and `a` is a private address/mode label.
All nonprivate resources must already be represented either by `p`, by `q`,
or by the fixed state `Theta`; otherwise (2.1) is not a completed ticket.

For binary variables `x_g` and `s_e`, the exact local degree/state layer is

\[
\begin{aligned}
 \sum_{g:e(g)=e}x_g &=s_e                         &&(e\in E),\\
 \sum_{g:p(g)=p}x_g &\le1                         &&(p\in P),\\
 \sum_{g:q(g)=q}x_g &\le1                         &&(q\in Q),\\
 x_g&\in\{0,1\}.                                  \tag{2.2}
\end{aligned}
\]

Together with `S={e:s_e=1}` being a basis of `M_short`, (2.2) is the exact
outer-plus-socket selection problem on this fixed state face.

### Proposition 2.1 (hypermatching characterization)

For fixed `Theta`, the socket-feasible short sets are precisely the
projections onto `E` of matchings in the three-partite, three-uniform
hypergraph with hyperedges `(e,p,q)` induced by (2.1).

#### Proof

The first row of (2.2) chooses exactly one hyperedge incident with every
selected short.  The second and third rows say that no two chosen
hyperedges repeat their `P`- or `Q`-vertex.  Conversely, every such
hypermatching satisfies (2.2).  The fixed state has already removed every
cross-side flag/history inconsistency. \(\square\)

Arbitrary three-dimensional matching is obtained by taking an arbitrary
set of triples as the ticket catalogue.  Therefore the unrestricted typed
socket problem is not reduced to max flow merely by materializing flags.

## 3. Exactly when the matroid-intersection route is valid

Let `T` be a set of completed ticket objects and
`G subseteq E cross T` the literal short-to-ticket compatibility graph.

### Theorem 3.1 (private/Rado face)

Suppose the allowed ticket subsets are the independent sets of a matroid
`K` on `T`.  Declare `S subseteq E` socket-feasible when it can be matched
through `G` to a `K`-independent ticket set.  Then the feasible short sets
form the Rado matroid `R(G,K)`, with rank

\[
 r_R(X)=\min_{Y\subseteq X}
        \bigl(|X-Y|+r_K(N_G(Y))\bigr).                       \tag{3.1}
\]

There is an outer-feasible, socket-complete short bank of size `1748` if
and only if

\[
 r_{M_{\rm short}}(X)+r_R(E\setminus X)\ge1748
                 \qquad(X\subseteq E).                       \tag{3.2}
\]

Private tickets are the special case in which `K` is free.  Laminar
capacity rows give another valid case because they present a laminar
matroid.  Rank-`1748` truncation is understood when `r_R(E)>1748`.

#### Proof

Equation (3.1) is Rado's matroidal matching theorem.  Equation (3.2) is
Edmonds' target-cardinality matroid-intersection min--max theorem; (1.2)
supplies the outer rank oracle. \(\square\)

The hypothesis is load-bearing.  Predecessor-capacity and
successor-capacity rows are two crossing partition matroids on tickets.
Their intersection need not be a matroid, and projecting through ticket
menus does not repair augmentation in general.

### Corollary 3.2 (no exact gammoid for a nonmatroid socket family)

If the hereditary partial-socket family violates matroid augmentation, no
strict gammoid, transversal matroid, Rado matroid, or other matroid can
represent that family exactly on the same short ground set.

This does not forbid a gammoid relaxation or a valid private subatlas.  It
forbids identifying the full shared-state family itself with a matroid.

## 4. Exact branch--flow theorem

The nonmatroid layer still has a sharp polynomial oracle after one endpoint
assignment is fixed.

Fix a short set `S`, a complete shared state `Theta`, and an injective map

\[
                           \mu:S\longrightarrow P.            \tag{4.1}
\]

Build the bipartite graph `B_(Theta,mu)` with left shore `S`, right shore
`Q`, and edge `e q` whenever the materialized catalogue contains at least
one completed ticket `(e,mu(e),q,a)`.

### Theorem 4.1 (one-shore branch, one-flow completion)

The predecessor assignment `mu` extends to a typed socket packing of all
shorts in `S` if and only if `B_(Theta,mu)` has a matching saturating `S`.
Equivalently,

\[
             |N_{B_{\Theta,\mu}}(X)|\ge |X|
                       \qquad(X\subseteq S).                  \tag{4.2}
\]

The extension and a minimum obstruction are obtained by one maximum-flow
and residual-min-cut computation.  The symmetric statement holds after
fixing successors instead of predecessors.

#### Proof

Injectivity of `mu` has already enforced every predecessor-capacity row.
`Theta` has already enforced all shared state equalities.  Choosing one
edge from every left vertex of `B_(Theta,mu)` with distinct right endpoints
is therefore exactly choosing one compatible ticket for each short while
enforcing all successor-capacity rows.  Hall's theorem proves (4.2).
\(\square\)

### Corollary 4.2 (sound exact branching and Benders cuts)

Use variables `y_ep` for the branched predecessor assignment.  At a fixed
state branch, if the inner matching returns a Hall set `X` for the current
map `mu`, then

\[
                     \sum_{e\in X}y_{e,\mu(e)}\le |X|-1       \tag{4.3}
\]

is a sound no-good: retaining all those same predecessor choices preserves
the same deficient successor graph on `X`.

If `Theta` was fixed only by assumptions rather than globally, the no-good
must also contain the full signed state assumptions on which the filtered
ticket graph depends.  Omitting them would transport a state-specific Hall
cut unsoundly.

Independently, if a proposed short set is dependent in `M_short`, an outer
circuit `C` gives the sound cut

\[
                         \sum_{e\in C}s_e\le |C|-1.           \tag{4.4}

\]

Equations (4.3)--(4.4), alternating outer rank queries (1.2), and the inner
successor flow give an exact branch-and-cut architecture.  It is not a
claim of polynomial total running time: branching chooses the missing
coordinate of a three-way matching.

## 5. Smallest actual exchange failure: round47

The authenticated relaxed-nine round47 catalogue is

```text
scratch/k_rots_k17_joint_1s_20260802/frozen_relaxed9/
  short_reset_triples.tsv
SHA-256 381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97
```

It has `2188` records on `1426` short roles.  The following menus are
singletons:

\[
\begin{array}{c|ccccc}
\text{short}&\text{pred}&\text{succ}&\text{pred flag}&\text{address}&\text{succ flag}\\ \hline
4183&11218&3987 &3&8&2\\
4218& 3756&3987 &3&8&3\\
4250& 3988&11218&0&7&0.
\end{array}                                                 \tag{5.1}
\]

Let `I={4183}` and `J={4218,4250}`.  Both are partially socket-packable.
But `I+4218` repeats successor `3987`, while `I+4250` uses physical long
`11218` on opposite sides with incompatible flags `3` and `0`.  Hence no
element of `J` augments `I`.

Three ground elements are the minimum possible size of an independence
augmentation failure (`|I|<|J|` and both nonempty).  This is therefore a
smallest actual obstruction to any exact socket-matroid/gammoid rank oracle
for this declared hereditary layer.

The statement is deliberately not promoted to complete-cycle-cover
extendability: unused long roles and global canonical completion are absent
from the definition of the audited partial family.

The independent C++ replay is frozen at

```text
scratch/r3_k17_typed_socket_branch_flow_20260802/
  audit_r3_k17_typed_socket_branch_flow_20260802.cpp
    SHA-256 2011937d125a6ce0f0c55da02571b6a3b994b612502accf034137a199702a84c
  theorem.audit.json
    SHA-256 f0ea2b5996c87cd97851f0d2a07f5e1774aeea5cc90b8218547e0124e3c0818f
```

It parses all `2188` catalogue rows, verifies all `1426` short menus and
replays the three singleton tickets and both failed augmentations.  The
same executable also checks the M17_s3 projection and containment rows in
Section 6; it does not infer a typed M17_s3 socket catalogue.

## 6. Calibration on the current M17_s3 carrier

The authoritative checkpoint is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_compiler_joint_res1916_deep1678_def59_zero45_s3/
```

Its compiler projection transports the same authenticated round47 target
table while retaining every chain ID, target list, length and root and
changing only the owner phase.  Thus the bottom-token containment
presentation and the cotransversal rank oracle (1.2) remain the relevant
outer face.  The carrier checkpoint has

```text
R=1916, H=1678, Phi=5510
both openings: old-target loss 0, gain 1
```

and exact supplier projections

| phase | matching / hard heads | deficiency | zero heads | edges | graph FNV64 |
|---:|---:|---:|---:|---:|---|
| 0 | 16842 / 16898 | 56 | 42 | 72064 | `67615aed653041de` |
| 1 | 16839 / 16898 | 59 | 45 | 72130 | `d9363cb106034277` |

The load-bearing hashes are

```text
model                         d9ec3d9b5f06670292edaa5da7e0f2e925215266ca941c6a7e5870fd217c98d6
checkpoint manifest          ac0aa113ba257aaaa8b656bb7698672918b25226fb2e4c0bcc7f3a57d95ce3ae
projection manifest          7821e7a117e149a1b6d999041b794a1faae78dda0849e312b4baa6bfd770e2c2
projection score             0734ae9ea14b0d49054b296ff6b62039d9a09ec4fb2e6ebefb6686c23fe0f7f4
containment table            5bb46d8935e80292f6a8b3cde0fc07037b296aeabcc99c3c64a501fb900f8676
```

These rows are union-supplier Hall projections.  They do **not** enumerate
completed common-state sockets.  In particular, the round47 socket
catalogue in Section 5 cannot be declared to be the socket catalogue of
`M17_s3`.

This restriction is empirically load-bearing, not bureaucratic.  On the
earlier `s7` carrier, rebuilding the exact common-state census improved the
supplier projection but *lost* exact socket tuples and *gained* zero-socket
shorts relative to C1.  Socket support is therefore not monotone or
carrier-agnostic under owner transport.

### M17_s3 decision gate

For each of its two owner phases, one must now do one of the following.

1. Rebuild the materialized long-state/socket catalogue and prove a
   private or Rado subatlas of rank at least `1748`; then apply (3.2).
2. Rebuild the complete typed catalogue and solve (2.2) jointly with
   `M_short`, using the exact state/predecessor branch and successor-flow
   oracle of Section 4.

Until that rebuild occurs, the proof-safe M17_s3 statement is exactly

```text
outer cotransversal rank oracle: available
supplier projection:            robust deficiency/zero = 59/45
typed socket matroid:            not established
typed common-state census:       not yet regenerated
```

## 7. What is resolved and what remains

Resolved:

- the outer short-bank matroid and its polynomial rank/exchange oracle;
- the exact private/Rado condition under which ordinary matroid
  intersection is sound;
- impossibility of an exact matroid/gammoid representation of the frozen
  round47 partial shared-socket family;
- an exact augmented-state branch--flow formulation for the nonmatroid
  typed layer;
- the precise proof-safe rebase of that formulation onto M17_s3.

Still open:

- a regenerated M17_s3 common-state catalogue in both phases;
- a size-1748 common solution of the outer basis and typed socket
  hypermatching;
- residence, arbitrary-upper completion, source chronology and the full
  K17 compiler.

### Postscript: the phase-0 retained private face is nonempty at full rank

The subsequent certificate
[MATH_THEOREM_Q_K17_PHASE0_RETAINED_WITNESS_PRIVATE_OUTER_BASIS_20260802.md](MATH_THEOREM_Q_K17_PHASE0_RETAINED_WITNESS_PRIVATE_OUTER_BASIS_20260802.md)
finds `1,748` retained phase-0 tickets with all `3,496` predecessor/successor
hosts globally distinct, `3,495` distinct movable bottom tokens and one
fixed soft endpoint.  Its forced edges extend to a complete outer matching.
Thus the requested private subface attains a common `M_short` basis and has
zero target deficiency.  This closes the static private-ticket/outer gate
for that phase-0 origin face.  It does not regenerate an M17_s3 socket
census and does not supply the directed-history/reset completion.

The correct algorithmic conclusion is therefore not “run matroid
intersection on the current sockets.”  It is:

\[
\boxed{
\text{outer cotransversal exchange}
\; + \;
\text{state/one-shore branching}
\; + \;
\text{opposite-shore max flow}.
}
\]
