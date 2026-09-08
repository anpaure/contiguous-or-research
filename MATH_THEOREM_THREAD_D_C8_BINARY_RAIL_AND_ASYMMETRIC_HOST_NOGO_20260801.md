# The asymmetric planted ray and every one-hot K2,2 rail fail the four-block C8 owner row

Date: 2026-08-01  
Lane: Thread D, physicalization of the nonzero four-block C8 source relation  
Status: exact scoped no-go for `d>=5`.  Sparse rails with a zero state and a
genuinely nonflat owner weave remain open.

## 0. Result

Use the Klein four-block relation with relabelings

\[
 1,\qquad \beta=(a_1a_3),\qquad \alpha=(a_0a_2),\qquad
 \alpha\beta
\]

and phase vectors `0110` and `1001`.  The source-signature relation and its
pointwise phase-common caps are genuine.  They do not make the seven planted
ray menu into a flat physical macro.

There are two additional exact obstructions beyond the repeated-owner theorem
in `MATH_THEOREM_THREAD_D_C8_FOURBLOCK_SEVEN_HOST_REFEREE_20260801.md`.

1. The phase-zero asymmetric planted ray has `d+1` consecutive source cells
   whose union has rank `r+2`.  It cannot occur as an internal rank-`r`
   depth-`d` owner window.  Only a rejected linear/component boundary or a
   new nonflat deadline can hide it.
2. The natural position-dependent **one-hot** edge-shared rail on the
   cancellation graph `K_(2,2)` cannot separate the four owner copies.
   Two long residual-interval components force two binary matching states;
   a fourfold owner class collides for all four choices of those states.

The second obstruction is sharp for the one-hot model.  Inside each critical
owner window, a sparse parallel/crossed pair can avoid every residual interval
only at one of four endpoint pairs

\[
 \{e,e+1\}\mathbin\times\{e+d-1,e+d\}.
\]

Thus a zero-state sparse rail is not excluded.  It must use precisely these
staggered endpoints (and their translated copy), or leave the binary
edge-shared model.

## 1. The asymmetric planted host is off rank

Retain the notation of the seven-host menu and put `|K|=r-d-3`.  Its
phase-zero asymmetric slot is

\[
\begin{aligned}
 B_S^0&=K\cup\{a_3\}\cup F[1,3],\\
 X_S&=K\cup\{a_1,a_3\}\cup F[1,d+1].
\end{aligned}
\]

The advertised outward additions are

\[
 f_4,f_5,\ldots,f_{d+1},\qquad \{a_0,a_2\}.
\]

Consequently the split host, its base, and the `d-1` additions occupy exactly
`d+1` consecutive source positions.  Their depth-`d` union is

\[
 K\cup F[1,d+1]\cup\{a_0,a_1,a_2,a_3\},
\]

of rank

\[
 (r-d-3)+(d+1)+4=r+2.                         \tag{1.1}
\]

This calculation is independent of exterior letters and orientation.  A
flat rank-`r` chronology cannot retain this owner row.  The four-block move
contains two `1 -> 0` phase changes, hence two phase-zero asymmetric
obligations if the local seven-ray repair is applied blockwise.  They may be
placed at rejected component endpoints, but endpoint placement cannot repair
the repeated protected interior owner bank proved in the referee theorem.

Every menu refinement `X -> X,B` also has the general internal stutter:
when `B subseteq X` enters while `X` remains in the source window, the next
owner is contained in the preceding owner.  Equal rank makes the two owners
equal.  Formula (1.1) is stronger for the asymmetric slot: even the complete
ray owner has the wrong rank.

## 2. Exact shallow cancellation graph

Index the four blocks by `0,1,2,3` so the signed shallow residual has positive
shore `{0,1}` and negative shore `{2,3}`.  For every graded phase-sensitive
interval of width at most `d`, there are exactly two positive occurrences,
one in each of blocks `0,1`, and two negative occurrences, one in each of
blocks `2,3`.  Thus each residual key may be paired by either perfect matching
of `K_(2,2)`.

Use edge labels

\[
 t_{02},t_{03},t_{12},t_{13}.
\]

A one-hot rail chooses at every relative source position one of the two
matching states

\[
\begin{array}{c|cccc}
 &0&1&2&3\\ \hline
 P&t_{02}&t_{13}&t_{02}&t_{13}\\
 X&t_{03}&t_{12}&t_{12}&t_{03}.
\end{array}                                               \tag{2.1}
\]

### Lemma 2.1 (monochromatic residual intervals)

A phase-sensitive interval preserves its tagged two-versus-two multiset if
and only if all of its source positions have the same state in (2.1).

#### Proof

An all-`P` interval gives the two matched singleton tags `t_02,t_13`; an
all-`X` interval gives `t_03,t_12`.  If both states occur, the four block tag
sets are

\[
 \{02,03\},\quad\{12,13\},\quad\{02,12\},\quad\{03,13\},
\]

which are pairwise different.  The positive and negative two-multisets
cannot agree.  This exhausts the one-hot states.  \(\square\)

## 3. The forced owner collision

The overlap hypergraph of shallow residual intervals has, among its six
components, the two components

\[
 E=[2d+5,3d+7],\qquad
 L=E+(4d+12)=[6d+17,7d+19].                 \tag{3.1}
\]

Lemma 2.1 forces one state `c_E` on `E` and one state `c_L` on `L`.  Put

\[
 e=2d+5,\qquad \ell=6d+17.
\]

The untagged owner rows contain the two fourfold equality classes

\[
\begin{aligned}
 \mathcal C_A&=\{(0,e),(3,e),(1,\ell),(2,\ell)\},\\
 \mathcal C_B&=\{(1,e),(2,e),(0,\ell),(3,\ell)\}.       \tag{3.2}
\end{aligned}
\]

Here `(b,i)` denotes the depth-`d` owner window starting at relative source
position `i` in block `b`.  Both `[e,e+d]` and `[ell,ell+d]` lie wholly in
their respective components, so their tag sets are the singleton entries of
(2.1).

### Theorem 3.1 (one-hot rail no-go)

No choice `(c_E,c_L) in {P,X}^2` separates `C_A` (and hence no one-hot rail
makes the four-block owner bank simple).

#### Proof

If `c_E=X`, the first two members `(0,e),(3,e)` both have tag `t_03`.
Therefore `c_E=P` is necessary; their tags are then `t_02,t_13`.

If `c_L=P`, the last two members `(1,ell),(2,ell)` have tags `t_13,t_02`,
repeating the first two.  If `c_L=X`, those last two both have tag `t_12`.
Either way `C_A` still collides.  \(\square\)

## 4. Sharp sparse escape pattern

The no-go above uses one nonzero matching state at every source position.
Allowing a zero state breaks Lemma 2.1's propagation through overlaps.  The
exact interval geometry nevertheless leaves only four ways to put opposite
nonzero states into the critical owner window without one shallow residual
interval seeing both:

\[
 \bigl\{(p,q):e\le p<q\le e+d,
  \text{ no residual interval contains both }p,q\bigr\}
 =\{e,e+1\}\times\{e+d-1,e+d\}.              \tag{4.1}
\]

The translated statement holds at `ell`.  Formula (4.1) explains the
observed fixed start/end clustering of the seven planted rays.  It is a
necessary local pattern, not a construction: a sparse rail must still
separate every other repeated owner, keep owner rank and Johnson adjacency,
preserve all crossing intervals, residence, and one common cap.

## 5. Length and cap ledger

Without planted splits, each sharp block has `9d+23` source positions and the
four-block relation has zero differential phase length.  The cap

\[
 P_{g,p}=\rho_g(Q_p^0\cup Q_p^1)
\]

is phase common at every position.

If the seven menu slots are installed blockwise as literal adjacent splits,
each block has seven additional positions in both phases (the phase-one
seventh slot is neutral).  Thus the fixed bank costs `28` source positions
over four blocks.  It does not *grow per switch* if kept permanently, but it
is not a zero-charge physicalization of the raw relation.  Returning from
`X,B` to `X` contracts the ray itself; regenerating it requires the same
position again.  No reclaim of those 28 positions follows from source-deck
or cap equality.

At a planted slot both pieces do lie in the phase-common cap `X_h`.  Hence
common-cap containment is locally positive; owner rank/simplicity and
regeneration, not cap containment, are the obstructions proved here.

## 6. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_threadD_c8_binary_rail_and_asymmetric_host_nogo_20260801.py --write
```

The dependency-free replay checks `5<=d<=32`: the asymmetric rank `r+2`
row, the exact `K_(2,2)` residual occurrence shores through width `d`, the
components (3.1), the owner equalities (3.2), all four binary states, and the
sharp sparse-pair formula (4.1).

