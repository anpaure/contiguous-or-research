# Independent audit: the exact proved support below `PCS` Row 2

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot / `PCS(m,d)` Row 2  
**Status:** proof audit and one unconditional projection corollary.  No
all-`m` protected upper-exact Hamilton path is claimed.

## 0. Verdict

The repository already proves three strong but differently quantified
facts.

1. For every `m>=3`, every corrected endpoint aperture `o subset s` occurs
   on some lower-rainbow Johnson Hamilton path.  This follows
   unconditionally from the fixed-boundary Middle Levels lollipop theorem.
2. For `m>=3d+1`, the literal pivot collar has a legal predecessor matching
   phase and a simple directed successor path with distinct immediate-upper
   colours.
3. Relative to that predecessor matching, all rank-`m+1` upper colours,
   including the full boundary/`D` shore, admit distinct rooted-tail
   representatives extending the pivot tickets.
4. For every fixed predecessor matching, the full upper-colour partition
   and graphic acyclicity have a common integral forest.  Separately, a
   pivot-compatible total order exposes an acyclic candidate atlas which
   contains the pivot and at least one arc of every upper colour.

The third object is only a semimatching: its opposite heads can collide and
its rooted links need not be acyclic.  The fourth forest does not impose
tail/head capacities and is not proved to contain the pivot.  The first
path need not contain the pivot collar and need not be upper-surjective.
Thus these facts cannot be superposed.

The exact first missing implication is

\[
 \boxed{\text{choose one common Hamilton support containing the collar on
 which every immediate-upper colour actually occurs.}}
 \tag{0.1}
\]

After that support is fixed, the contracted graphic--Rado theorem adds no
large selection theorem: on a path, one eligible occurrence per colour is
necessary and sufficient.  Before it is fixed, a total-order reduction
removes the graphic row completely but leaves a coloured near-perfect
tail/head matching.  Therefore ordinary Hall/Rado must not be cited as
proving (0.1).

## 1. An unconditional corrected-aperture owner host

Put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal V={ [2m-1]\choose m},\qquad
 W=|\mathcal L|=|\mathcal V|.
\]

### Proposition 1.1 (fixed-aperture lower-rainbow path)

For `m>=3`, let `o\in\mathcal L` and `s\in\mathcal V` satisfy
`o\subset s`.
There is a Johnson Hamilton path

\[
                 T_0,T_1,\ldots,T_{W-1}=s             \tag{1.1}
\]

on `\mathcal V` such that the `W-1` intersections

\[
                 X_i=T_i\cap T_{i+1}                  \tag{1.2}
\]

are pairwise distinct and enumerate `\mathcal L-\{o\}`.  Moreover

\[
 M_0(X_i)=T_i,\qquad M_0(o)=T_{W-1}                  \tag{1.3}
\]

is a perfect incidence matching.  Hence `(o,s)` is exactly the corrected
terminal endpoint phase, not merely an abstract omitted-root count.

#### Proof

Write `s=o+{b}`.  Choose `a in o` and put

\[
                         D=o-\{a\}+\{b\}.             \tag{1.4}
\]

Then `o,D` are distinct Johnson-adjacent lower vertices and
`o union D=s`.  Apply the fixed-boundary lollipop theorem with `M=o` and
this `D`.  Its Hamilton path in `ML(2m-1)` starts with the incidence edge
`o--s` and ends on the owner shore.  Reverse it.  Reading only owner
vertices gives (1.1).  The intervening lower vertices are all lower
vertices except the terminal `o`, once each, and each is the intersection
of its adjacent owners.  The predecessor incidence edges in the reversed
path give (1.3).  \(\square\)

This proposition proves the unprotected owner/aperture part of `PCS` Row 1.
It does **not** put the length-`3d` pivot successor collar into the path and
does not assert anything about the adjacent unions
`T_i union T_(i+1)`.

## 2. What is unconditional around the literal pivot

Let

\[
 P=(V_0,\ldots,V_{3d}),\qquad
 I_i=V_i\cap V_{i+1},\qquad
 R_i=V_i\cup V_{i+1}.                                \tag{2.1}
\]

For `m>=3d+1`, the pivot theorem proves that the `I_i` are distinct, the
`R_i` are distinct, and

\[
 P_0=\{I_iV_i\},\qquad P_1=\{I_iV_{i+1}\}            \tag{2.2}
\]

are the two legal incidence phases.  The matching `P_0` extends to a
perfect `M_0`, while `P_1` contracts to one directed path.

There is a further unconditional full-shore marginal.

### Proposition 2.1 (full upper-tail marginal, not a support)

For every such extension `M_0`, the protected pairs

\[
                         (R_i,V_i),\qquad 0\le i<3d,  \tag{2.3}
\]

extend to an injection

\[
 \psi:{[2m-1]\choose m+1}\longrightarrow
                         {[2m-1]\choose m},
 \qquad \psi(R)\subset R,                            \tag{2.4}
\]

and the corresponding rooted incidences retain every edge of `P_1`.

#### Proof

The pairs (2.3) have distinct upper colours and distinct tails.  Their
number is `3d<=m-1<m`.  The protected rooted upper-tail extension theorem,
whose Hall proof uses

\[
             |\partial X|\ge |X|+m                    \tag{2.5}
\]

for every nonempty family of rank-`m+1` sets, applies.  Its domain in (2.4)
is the entire rank-`m+1` shore, so no quotient or non-`D` exception is being
discarded.  The literal incidence associated with `(R_i,V_i)` is precisely
`I_iV_(i+1)`.  \(\square\)

For a pair `(R,T)` in (2.4), the corresponding other diamond corner is

\[
 L=M_0^{-1}(T),\quad T=L+\{a\},\quad R=T+\{b\},
 \quad V=L+\{b\}.                                    \tag{2.6}
\]

Distinct `T` make the rooted tails `L` distinct.  They do not make the
heads `V` distinct.  Thus Proposition 2.1 is not an incidence-matching
support `S` and cannot feed the path corollary of graphic Rado.

This failure is genuine, not a wording technicality.  At `m=3`, the two
legal tickets

\[
                     (1234,123),\qquad(1245,245)      \tag{2.7}
\]

have distinct colours and tails but force the same head.  A separate
three-arc example in the repository has distinct tails, heads and colours
and is a directed forest, yet extends to no Hamilton path for its fixed
`M_0`.  Consequently neither ``add head injectivity'' nor ``add protected
acyclicity'' upgrades Proposition 2.1 post hoc.

### Proposition 2.2 (protected forward atlas)

Fix any perfect `M_0` extending the pivot predecessor phase.  Its rooted
digraph has owner-coordinate arcs

\[
 T\longrightarrow T-\{\rho(T)\}+\{x\},
 \qquad x\notin T,                                   \tag{2.8}
\]

where `rho(T)` is the coordinate deleted by `M_0`.  For every upper colour
`R`, the `m+1` arcs of colour `R` form a loopless functional digraph on the
`m+1` owner facets of `R`, and hence contain a directed cycle of length at
least three.

Choose an injective potential `phi` which increases along the protected
successor path and put

\[
 E_\phi=\{u\longrightarrow v:\phi(u)<\phi(v)\}.       \tag{2.9}
\]

Then `E_phi` contains the protected pivot arcs, contains at least one arc of
every rank-`m+1` upper colour, and has no directed cycle.

#### Proof

The protected arcs form one directed path, so their order extends to a
total order of all rooted vertices.  This gives `phi` and retains those
arcs in (2.9).  On a directed cycle in any upper-colour fibre, not every
edge can decrease an injective potential.  Hence that fibre contributes a
forward edge.  Strict increase excludes a directed cycle in `E_phi`.
\(\square\)

Thus **ambient occurrence availability, with the protected order and a
common acyclic orientation, is unconditional**.  What remains is selecting
the occurrences with simultaneous tail and head capacity one.  The atlas
`E_phi` itself is not an incidence matching and hence is not the support
`S` assumed by the PCPS Rado--erosion product theorem.

There is also an unconditional unprotected integral marginal: for every
fixed `M_0`, one can select exactly one arc of every upper colour so that
the underlying rooted edges form a forest with `Cat_m` components.  This is
matroid intersection between the upper-colour partition matroid and the
graphic matroid.  It still need not have tail or head degree at most one,
and the proved statement does not force the pivot arcs.  Extending this
forest to an ordinary spanning tree likewise does not linearize it.

## 3. The exact Row-2 owner statement

Fix the protected phase `(M_0,P_1)`.  For an incidence `e=LV` outside
`M_0`, put

\[
 \lambda(e):L\longrightarrow M_0^{-1}(V),\qquad
 \operatorname{up}(e)=M_0(L)\cup V.                  \tag{3.1}
\]

The support part of `PCS` Rows 1--2 is exactly the existence of a matching
`Q` such that

\[
 \begin{aligned}
   &P_1\subseteq Q,\qquad |Q|=W-1,\\
   &\lambda(Q)\text{ is graphic-independent},\\
   &\operatorname{up}(Q)={[2m-1]\choose m+1},        \tag{3.2}
 \end{aligned}
\]

with the corrected endpoint phase and the literal collar position.  The
first two lines make `lambda(Q)` one directed Hamilton path; the last line
is precisely occurrence availability of every full-shore immediate-upper
colour.

Equivalently, choose one occurrence of each upper colour to obtain a rooted
Catalan forest `Q_0` containing `P_1`, then join its `C=Cat_m` directed path
components by `C-1` compatible free-port arcs forming their directed
Hamilton path.  This is an exact equivalence, not a construction.

For a **fixed** replayed path support `S=Q`, the contracted graphic--Rado
inequalities reduce to

\[
       E_R=\{e\in S:\operatorname{up}(e)=R\}\ne\varnothing
       \qquad\text{for every residual colour }R.      \tag{3.3}
\]

Thus (3.3), rather than a hidden matroid inequality, is the first missing
Row-2 implication.  An interval-OR witness outside `S` cannot replace a
missing `E_R`.

### Proposition 3.1 (exact forward-linearization reduction)

For fixed `M_0` and protected path `P_1`, the unpinned object (3.2) exists
if and only if there are

* an injective potential `phi` increasing along `P_1`; and
* an arc set `Q subseteq E_phi` containing `P_1`

such that

\[
 \begin{aligned}
 |Q|&=W-1,\\
 |Q\cap\delta^+(v)|&\le1,
 &|Q\cap\delta^-(v)|&\le1 &&(v),\\
 |Q\cap E_R|&\ge1 &&&
   \left(R\in{[2m-1]\choose m+1}\right).             \tag{3.4}
 \end{aligned}
\]

#### Proof

If (3.2) exists, order vertices along its directed Hamilton path and use
that order for `phi`; then (3.4) is immediate.  Conversely, the port rows in
(3.4) imply that every undirected cycle of `Q` would be coherently directed:
at every cycle vertex one incident edge enters and one leaves.  This is
impossible in `E_phi`.  Hence `Q` is a forest.  It has `W` vertices and
`W-1` edges, so it is connected; the port rows make it one directed
Hamilton path.  The last row is exactly full-shore upper surjectivity.
\(\square\)

This is the smallest exact integral Row-2 selector found in the audited
notes.  It is a coloured near-perfect matching between tail and head
copies, not ordinary bipartite Hall: the same choice must cover the third
(upper-colour) role.  The potential removes graphic subtour inequalities,
but it does not round the three correlated roles.

If a rooted source `s_*` and sink `t_*` are prescribed, the equivalence
requires the additional endpoint state

\[
       \phi(s_*)=\min\phi,qquad \phi(t_*)=\max\phi,qquad
       Q\cap\delta^-(s_*)=Q\cap\delta^+(t_*)=\varnothing.       \tag{3.4a}
\]

The port equalities are automatic from the two potential extrema but are
displayed to record the physical endpoint roles.  In the corrected terminal
aperture one takes `t_*=o` and fixes `M_0(o)` to the intended endpoint
owner containing `o`.  Omitting this named state would prove only an
unrooted Row-2 path, not the aperture-qualified support.

### 3.2 Quantitative external-chord form

For any completed lower-rainbow path, occurrence availability has an exact
load form.  For an upper colour `R`, let `g_R` count used roots `L subset R`
whose two incident owners both lie outside `R`; let `a_R` count path
endpoints which are facets of `R`; and let `m_R=1_(o subset R)` for the
omitted root.  Then

\[
 u_R-1=g_R-\left(h_m+a_R-m_R\right),\qquad
 h_m={m+1\choose2}-2(m+1)+1.                         \tag{3.5}
\]

Therefore Row 2 is equivalent, on the completed path, to

\[
                    g_R\ge h_m+a_R-m_R
                    \qquad\text{for every }R.         \tag{3.6}
\]

The total surplus in (3.6) is exactly `Cat_m-1`.  At `K17` (`m=9`) the
generic threshold is `26` and the total surplus is `4861`.  This is an
unconditional quantitative reformulation strictly below `PCS`, but not an
existence proof: it identifies Row 2 as a tightly balanced external-chord
design.

## 4. Exact transparent pull-tree route and its limits

The cycle-cover route has a proof-safe sufficient form.

### Lemma 4.1 (protected transparent pull implication)

Suppose a spanning Middle Levels cycle factor `F` has:

1. the protected pivot incidence path `P`;
2. one fixed occurrence of every immediate-upper colour;
3. a jointly compatible sequence of factor-alternating `C6`/ECO toggles
   whose component incidence graph is a tree and which merges `F` to one
   Hamilton cycle;
4. at every toggle, equality of the selected local turn-colour multisets
   on each shore and the retained-fragment boundary-alternation condition;
5. protection of `P` and of one valid opening state.

Then the final cycle contains `P` and is immediate-upper-surjective.  If a
nonprotected redundant provider occurrence is cut, the resulting incidence
Hamilton path remains upper-surjective and its omitted lower root is
contained in its incident endpoint owner, so the corrected aperture holds.

#### Proof

The local transparent-hex theorem says that items 3--4 preserve the fixed
representative palettes at every toggle.  The auxiliary tree merges all
factor components without splitting the final topology.  Deleting one
incidence edge destroys one lower-turn occurrence.  If its colour has
another occurrence, surjectivity survives; the deleted incidence itself
gives omitted-root containment at the new endpoint.  Protection retains
the collar.  \(\square\)

In the pivot range a completed upper-surjective Hamilton cycle has enough
redundant provider occurrences to choose one outside `P_1`: there are `W`
turns and `U` colours, with Catalan excess `C=W-U`, while `|P_1|=3d` and
`C+1>3d`.  This is the proved safe-opening count.  If the temporal model
requires a *named* opening next to a particular collar port, redundancy
somewhere else is insufficient; that stronger address condition remains a
separate row.

Lemma 4.1 is useful because it isolates the missing all-`m` pull statement,
but none of its existence hypotheses follows from uncoloured component
connectivity:

* coherent ECO atoms have connected component two-section in every
  dimension, but simultaneous physical compatibility and a common
  decoration are not proved;
* transparency requires per-shore local palette equality **and** boundary
  alternation; an alternating hexagon or a component merge alone is not
  transparent;
* the raw canonical `m=5` ECO Hamiltonizations all miss the same three
  colours on each shore, despite disjoint physical ports and disjoint
  forced colour triples;
* the lexical `F_01` plus canonical pull-tree family has a certified positive
  upper-colour deficit for every `m>=12`.  That no-go is scoped to the
  lexical family; it does not rule out a prepared nonlexical factor or
  noncanonical repair packet.

Hence the smallest transparent-route existence lemma is:

> construct a protected upper-surjective cycle factor together with one
> jointly compatible representative-transparent component-spanning pull
> tree and an admissible redundant opening.

It is strictly smaller than full `PCS`: it concerns only the owner and
immediate-upper support.  It is still unproved for all `m`.

## 5. Small positive calibration, not an induction

The explicit `m=3` fixed-boundary lollipop path has owner sequence

```text
123,134,124,245,125,145,345,234,235,135.
```

Its nine adjacent unions have multiplicities

```text
1234:2, 1235:1, 1245:3, 1345:1, 2345:2,
```

so all five rank-four colours occur.  This confirms that the endpoint
lollipop and Row 2 can coexist in the first nontrivial dimension.  It does
not contain the general depth-`d` pivot (the range `m>=3d+1` is empty here)
and supplies no recursive state.

## 6. Audited frontier

The strongest unconditional statements relevant to Row 2 are therefore:

\[
\begin{array}{c}
\text{arbitrary corrected aperture on a lower-rainbow Hamilton path}
\\
\text{and, separately,}
\\
\text{pivot-preserving full-shore upper-tail semimatching}.
\end{array}
\]

In addition, the full upper partition has an unprotected graphic forest for
every fixed `M_0`, and Proposition 2.2 gives a protected acyclic atlas with
no missing colour.  These stronger marginals sharpen, but do not remove,
the common-support correlation.

The exact first missing implication is their **common-support correlation**,
equation (3.2).  A proof may proceed through a prepared upper-surjective
cycle factor and Lemma 4.1, or construct the path directly.  It may not
proceed by applying graphic Rado before occurrence availability is proved.

This audit makes no claim about full-row residence, the `4d` source replay
rows, strictly higher upper shadows, old crossing-window transport, the
common lower compiler, regeneration, `PCS(m,d)`, or `PCPS(m,d)`.

## 7. Source scope checked

The statements above were checked against:

* `MATH_THEOREM_ODD_MIDDLE_LEVELS_FIXED_BOUNDARY_LOLLIPOP_EXISTENCE_20260802.md`;
* `MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_CONNECTOR_BIRTH_AND_PREPARED_SCAFFOLD_GATE_20260802.md`;
* `MATH_THEOREM_PROTECTED_UPPER_EXACT_HAMILTON_PATH_AND_ROOTED_TAIL_EXTENSION_20260801.md` and its independent audit;
* `MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md`;
* `MATH_THEOREM_ODD_ROOT_LINK_UPPER_FIBRES_EXCURSIONS_AND_FRACTIONAL_PATH_20260802.md`;
* `MATH_THEOREM_ODD_ROOT_LINK_UPPER_MULTIPLICITY_EXTERNAL_CHORD_IDENTITY_20260802.md`;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`;
* `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`;
* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_R_PROSPECTIVE_GMN_COLORED_PULL_TREE_AND_LEXICAL_UPPER_OBSTRUCTION_20260801.md`; and
* `MATH_THEOREM_K_PCPS_FIRST_CLAUSE_RADO_EROSION_FACTORIZATION_20260802.md`.
