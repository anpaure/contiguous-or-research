# The sharp octagon needs eight/nine native endpoint rays, and current-letter splits cannot reset it

Date: 2026-08-01  
Lane: Thread D, physical interpretation of the sharp source-deck width  
Status: exact all-`d` theorem for `d>=5`.  It closes the proposed
`6/7 = host count` inference and the stronger current-word refinement route.
It does not exclude newly planted two-sided hosts.

## 0. Verdict

For the two expanded sharp octagon source words, the phase-only deck posets
have widths `6` and `7`.  Those numbers are **not** physical host counts.
If a native endpoint ray means a family of interval values having one common
literal left endpoint or one common literal right endpoint, then the exact
minimum cover numbers are

\[
                         \rho_0=8,\qquad \rho_1=9.       \tag{0.1}
\]

The already frozen `8/9` partitions therefore are optimal.  The abstract
Dilworth covers splice chains across endpoint-disjoint source corridors.
In particular, a model assigning one existing physical endpoint ray to each
abstract chain cannot use at most seven rays: phase zero already needs eight
and phase one needs nine.

There is a stronger obstruction for literal split hosts in the **current**
source.  Replacing any number of its letters by consecutive nonempty blocks
with the same unions cannot equalize the decks.  In either direction exactly

\[
                              3d-3                       \tag{0.2}
\]

phase-only masks lie outside the full arbitrary-block-refinement closure of
the opposite word.  Thus seven current-letter splits fail, as do seventy.

This does not rule out seven newly **planted** binary hosts.  One binary host
can expose a left and a right ray, and planting changes the antecedent word.
For that more permissive claim, neither (0.1) nor the Dilworth width is a
certificate.  Section 4 states the missing literal equations.

## 1. Endpoint-ray cover number

Let `Y^epsilon` be the expanded sharp source word, indexed from zero, and
let

\[
 \Delta_\epsilon=\operatorname{Deck}(Y^\epsilon)
              -\operatorname{Deck}(Y^{1-\epsilon}).      \tag{1.1}
\]

For `S in Delta_epsilon`, define its complete endpoint signature

\[
 E_\epsilon(S)=
 \{L(s):\exists t,\ \bigvee Y^\epsilon[s,t]=S\}
 \cup
 \{R(t):\exists s,\ \bigvee Y^\epsilon[s,t]=S\}.        \tag{1.2}
\]

A native fixed-endpoint ray anchored at `L(s)` or `R(t)` contains exactly
those phase-only values whose signature contains that anchor.  Hence a set
of targets with pairwise disjoint signatures needs pairwise distinct ray
anchors.

Write `F[i,j]={f_i,...,f_j}` and suppress the fixed core `K`.

### Theorem 1.1 (eight-ray obstruction in phase zero)

The following eight members of `Delta_0` have pairwise disjoint complete
endpoint signatures:

\[
\begin{array}{c|l}
S& E_0(S)\\ \hline
a_3+F[0,1]&\{L(7d+22),R(7d+22)\}\\
z+a_1+F[1,3]&\{L(6d+19),R(6d+21)\}\\
z+a_3+f_0+F[d,d+1]&\{L(7d+19),R(7d+21)\}\\
a_1+F[1,d+1]&\{L(5d+17),R(6d+16)\}\\
z+a_3+F[d-1,d+1]&\{L(7d+18),R(7d+20)\}\\
z+a_3+F[2,d]&\{L(6d+21),R(7d+19)\}\\
a_0a_2a_3+F[0,d]&
 \{L(s):8d+24\le s\le9d+24\}\cup\{R(9d+25)\}\\
a_1a_2a_3+F[0,d+1]&
 \{L(1)\}\cup\{R(t):d+3\le t\le2d+4\}.
\end{array}                                               \tag{1.3}
\]

Therefore `rho_0>=8`.

### Theorem 1.2 (nine-ray obstruction in phase one)

The following nine members of `Delta_1` have pairwise disjoint signatures:

\[
\begin{array}{c|l}
S&E_1(S)\\ \hline
z+a_1+f_d&\{L(3d+7),R(3d+7)\}\\
z+a_1+f_0+F[d-1,d+1]&\{L(3d+6),R(3d+9)\}\\
a_3+F[2,3]&\{L(d+6),R(d+6)\}\\
z+a_3+f_1&\{L(2d+7),R(2d+7)\}\\
z+a_1+F[3,d+1]&\{L(2d+10),R(3d+8)\}\\
a_3+F[1,d]&\{L(d+5),R(2d+3)\}\\
a_0a_1a_3+F[0,d+1]&
 \{L(s):7d+22\le s\le8d+23\}\cup\{R(9d+25)\}\\
a_1+F[0,2]&\{L(3d+10),R(3d+11)\}\\
a_0a_2a_3+F[1,d+1]&
 \{L(1)\}\cup\{R(t):2\le t\le d+2\}.
\end{array}                                               \tag{1.4}
\]

Therefore `rho_1>=9`.

The explicit endpoint-ray partitions in
`MATH_THEOREM_THREAD_D_OCTAGON_SOURCE_DECK_WIDTH_AND_PHYSICAL_RAYS_20260801.md`
give the reverse inequalities `rho_0<=8,rho_1<=9`, proving (0.1).

### Proof of (1.3)--(1.4)

Sweep both endpoints in the literal sharp source.  Before entering the next
active corridor, changing one endpoint changes only a consecutive filler
prefix or suffix.  On leaving it, the next active label enters and the union
is no longer the displayed target.  This gives exactly the endpoint sets in
(1.3)--(1.4), not merely one chosen witness per target.  Their affine index
ranges are pairwise disjoint as **side-tagged** endpoints for `d>=5`.
Thus no fixed-left or fixed-right ray contains two displayed targets.  The
audit performs the complete endpoint sweep through `d=64`.

## 2. Why Dilworth width does not give host count

Every fixed-endpoint ray is an inclusion chain, so Dilworth gives only

\[
                    \rho_0\ge6,\qquad\rho_1\ge7.          \tag{2.1}
\]

The converse is false because an arbitrary inclusion chain need not have a
common literal endpoint.  In the six- and seven-chain covers, the constant
top/bottom masks are joined to filler chains after an active-label jump.
Equations (1.3)--(1.4) show that those joined values have disjoint complete
endpoint signatures.  They are comparable as sets but not consecutive
addresses on one physical ray.

Accordingly, a width-`7` census can be used as a lower bound or as a target
for a **newly designed** host word.  It cannot certify seven hosts in the
authenticated word.

## 3. Stronger no-go for splitting current letters

A literal current-word binary split at position `p` is

\[
                         X_p\longmapsto Z_p,T_p,
 \qquad Z_p,T_p\ne\varnothing,
 \qquad Z_p\cup T_p=X_p.                                \tag{3.1}
\]

Allowing more than two pieces and arbitrarily many split positions only
strengthens the operation.  If `Ref(Y)` denotes the interval masks obtainable
after all such refinements, then the exact side-cell normal form is

\[
\begin{split}
 \varnothing\ne S\in\operatorname{Ref}(Y)\Longleftrightarrow{}&
 S\subseteq Y_p\text{ for some }p,\quad\text{or}\\
 &\exists a<b:\ U_{a,b}\subseteq S\subseteq
 U_{a,b}\cup Y_a\cup Y_b,\\
 &S\cap Y_a\ne\varnothing,\quad S\cap Y_b\ne\varnothing,
\end{split}                                               \tag{3.2}
\]

where `U_(a,b)=union_(a<i<b)Y_i`.  This permits independent trimming of both
endpoint blocks and every arity for one named target.  It is an existential
one-target criterion; individual reachability does not imply that one common
refinement realizes several targets simultaneously.

The exact sharp-deck audit gives

\[
 |\Delta_0-\operatorname{Ref}(Y^1)|
 =|\Delta_1-\operatorname{Ref}(Y^0)|=3d-3.               \tag{3.3}
\]

Therefore no family of splits of existing letters makes either opposite
deck complete.  In particular, interpreting the eight current filler traces
as eight available split sites does not help: their union-preserving
refinements are already included in (3.2).

## 4. What remains possible for newly planted hosts

A planted host changes the antecedent and is outside (3.2).  Seven planted
binary hosts are not excluded by this theorem because each binary split can
expose two rays.  But a valid claim needs considerably more than a chain
cover.  At every proposed cut it must exhibit:

1. for a reversible common-host construction, an actual phase-common old
   letter `X` and nonempty phase-oriented halves `Z^epsilon,T^epsilon` with
   `Z^epsilon union T^epsilon=X` in both phases.  A more general construction
   may use phase-specific unions `X^epsilon`, but must then supply an explicit
   cross-phase occurrence transport; a common cap alone does not identify the
   two letters;
2. literal direct-address equations
   `C_i=Z union L_1 union ... union L_(ell_i)` or
   `C_i=T union R_1 union ... union R_(r_i)` for every assigned target;
3. adjacency which pairs the two rays assigned to one binary host--two
   unrelated endpoint anchors cannot be paired merely because their target
   masks are comparable;
4. owner-rank, `d+1`-window deadline and residence legality for every new
   half-window;
5. containment in one prescribed common cap and matching-safe contraction;
6. equality of the **new** internal/prefix/suffix decks, or a guarded Hall
   assignment for every residual protected mask.  Covering the old directed
   differences is insufficient if the planted splits create fresh
   phase-exclusive values.

Under the convention “one host supplies one physical ray”, (0.1) itself
rules out seven.  If both halves of a binary host may carry rays, the endpoint
count alone yields only the coarse lower bound `ceil(9/2)=5`; the decisive
conditions are the pairing and common-union equations above.  No seven-host
positive theorem follows from the present width data.

## 5. Exact remaining statement

The weakest honest positive target is a **guarded planted-ray theorem**:
construct a common capped antecedent with binary hosts whose half-rays
saturate both directed banks, whose new phase-only deck is empty (or has a
joint protected-occurrence matching), and whose contractions preserve all
owner/deadline rows.  The target bank is constant-family/linear-size, but its
physical realization is not supplied by Dilworth.

Absent such planting, the exact remaining terminal condition remains the
deadline/common-cap guarded Hall matching of the full-source-deck theorem.

## 6. Replay

Run

```text
python3 scratch/audit_threadD_octagon_native_ray_cover_obstruction_20260801.py --write
```

The replay checks `5<=d<=64`, exact phase-only membership, all complete
endpoint signatures in (1.3)--(1.4), their pairwise disjointness, the frozen
`8/9` covering anchors, and the `3d-3` arbitrary-refinement obstruction.

An independent referee replayed the literal formulas and accepted both the
`8/9` endpoint-ray lower bound and the any-current-refinement obstruction.
