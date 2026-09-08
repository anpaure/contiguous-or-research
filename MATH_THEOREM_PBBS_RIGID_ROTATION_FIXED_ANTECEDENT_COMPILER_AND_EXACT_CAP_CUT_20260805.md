# Fixed antecedents collapse ordinary compiler Hall; the remaining cap gate is one exact port cut

**Date:** 2026-08-05  
**Method:** exact-value fibres, maximal-envelope interval cuts,
adjacent-slice chain flow, and Rado/Menger; no computation or search  
**Status:** unconditional reduction.  For a fixed literal terminal word,
ordinary strict-lower compilation has no target-to-cell Hall problem:
different exact target values have disjoint occurrence fibres.  The hard
choice is upstream—selecting one antecedent and one interval atlas with no
missing target.  If an additional typed common-cap router is required, its
smallest exact residual obstruction is a single Rado/gammoid all-cut.  A
rank-scheduled chain factor removes the local common cap but not the global
trace-Euler serialization.

## 1. Fixed-word compiler fibres

Fix a nonzero linear source word

\[
                         A=(A_0,\ldots,A_{N-1})                  \tag{1.1}
\]

and deadline `d`.  Let `cal C_d(A)` be the physical interval occurrences
of source width at most `d`, and let

\[
                         v(I)=\bigcup_{p\in I}A_p.               \tag{1.2}
\]

For each nonempty strict-lower target `S`, put

\[
                         {\cal C}_S=v^{-1}(S).                  \tag{1.3}
\]

### Theorem 1.1 (fixed-antecedent compiler collapse)

The word `A` contains an occurrence-injective strict-lower compiler if and
only if

\[
                         {\cal C}_S\ne\varnothing
                         \quad\hbox{for every strict-lower }S.   \tag{1.4}
\]

When (1.4) holds, choosing an arbitrary `I_S in cal C_S` for every target
is automatically injective.  If

\[
 \lambda(A)=\#\{S:{\cal C}_S=\varnothing\},                    \tag{1.5}
\]

then `lambda(A)` is exactly the ordinary literal compiler deficiency of
this fixed word.

#### Proof

Necessity is immediate.  Conversely, if `I_S=I_(S')`, applying the
single-valued map `v` gives `S=S'`.  Thus arbitrary representatives of the
nonempty exact-value fibres are distinct physical interval occurrences.
`square`

Consequently, for a fixed owner chronology `T`, the familiar quantity

\[
                         \lambda_d(T)=min_{A:D^dA=T}\lambda(A) \tag{1.6}
\]

is difficult because the antecedent is being chosen.  It is not a residual
matching problem after `A` is fixed.

If “common cap” means only that all target equalities must hold in one
ordinary OR word, then the fixed word `A` is already that common cap.  Any
additional cap gate must encode extra occurrence types, phase flags, shared
routes, or sink capacities not present in ordinary exact-value compilation.

## 2. Owner-path support does not determine lower source support

The full rigid-rotation theorem supplies an exact owner-path intersection
bank and its paired upper bank.  It does not imply (1.4).

### Proposition 2.1 (same owners, different lower decks)

At deadline one, the two nonzero source words

\[
 A=(\{b\},\{a\},\{c\}),
 \qquad
 A'=(\{a,b\},\{a\},\{a,c\})                       \tag{2.1}
\]

have the same Johnson owner path

\[
                         DA=DA'=(\{a,b\},\{a,c\}),             \tag{2.2}
\]

but different strict-lower occurrence decks.  In particular, `A` contains
the singleton targets `{b}` and `{c}`, while `A'` does not.

#### Proof

Both adjacent unions in (2.1) are the two sets in (2.2).  Every interval
of `A'` containing `b` also contains `a`, and similarly for `c`; hence the
two declared singleton targets are absent from its deck. `square`

Thus exact owner support, owner-path occurrence injectivity, and even a
fixed owner chronology do not remove the choice in (1.6).

## 3. The exact fixed-atlas obstruction is coordinatewise

Now fix a linearly `d`-resident owner chronology

\[
                         T=(T_0,\ldots,T_{W-1})                  \tag{3.1}
\]

and its maximal envelope

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(p,W-1)}T_i.              \tag{3.2}
\]

For every strict-lower target `S`, prospectively choose one source interval
`I_S` of width at most `d`.  Define

\[
 Q_x=
 \{p:x\in P_p\}\setminus
 \bigcup_{S:\,x\notin S}I_S.                                  \tag{3.3}
\]

### Theorem 3.1 (smallest ordinary common-word cut)

The selected atlas is realized by one nonzero word `A` with `D^dA=T` if
and only if

\[
 Q_x\cap[i,i+d]\ne\varnothing
 \quad(i<W,\ x\in T_i),                                      \tag{3.4}
\]

\[
 Q_x\cap I_S\ne\varnothing
 \quad(x\in S),                                               \tag{3.5}
\]

and

\[
                         \{x:p\in Q_x\}\ne\varnothing
                         \quad(p<N).                            \tag{3.6}
\]

When they hold, the coordinatewise maximal word

\[
                         A_p=\{x:p\in Q_x\}                    \tag{3.7}
\]

realizes every owner and every selected target interval simultaneously.

#### Proof

Every realizing letter is contained in `P_p`.  A target interval whose
label omits `x` forbids `x` at every one of its positions, so the support of
`x` is contained in `Q_x`.  The positive sides of the owner and target
equalities give (3.4)--(3.5), and nonzero letters give (3.6).

Conversely, (3.3) prevents every forbidden coordinate.  Conditions
(3.4)--(3.5) supply every required coordinate, and (3.6) makes every letter
nonempty.  Taking all allowed coordinates as in (3.7) proves every equality.
`square`

### Corollary 3.2 (literal interval-cover form)

For each coordinate put

\[
 E_x=\{p:x\in P_p\},
 \qquad
 F_x=\bigcup_{S:\,x\notin S} I_S.                            \tag{3.8}
\]

The fixed atlas is feasible if and only if

\[
 E_x\cap[i,i+d]\not\subseteq F_x
 \quad(i<W,\ x\in T_i),                                    \tag{3.9}
\]

\[
 E_x\cap I_S\not\subseteq F_x
 \quad(x\in S),                                             \tag{3.10}
\]

and, for every source position `p`, some `x in P_p` satisfies

\[
                         p\notin F_x.                         \tag{3.11}
\]

Thus the exact obstruction after the atlas is fixed is a family of
one-dimensional interval-cover cuts, one coordinate at a time.  It is not
a Hall cut indexed by families of target values.

Hence, after source intervals are selected, ordinary common-cap failure is
one of only three literal one-dimensional failures:

1. a central window required to contain `x` is covered by negative pins;
2. a chosen target interval required to contain `x` is covered by negative
   pins; or
3. one position is forbidden for every coordinate.

There is no additional subset-Hall inequality.  Laminarity of target labels
or interval supports alone does not force (3.4): two disjoint negative
intervals can jointly cover one central window.  The positive-hit rows must
be retained.

For the rigid-rotation programme, the owner-path bank fixes upper intervals
after a terminal antecedent is known, but it does not select the short
intervals `I_S` required here for every strict-lower target.  That atlas
selection is the exact ordinary compiler gate.

## 4. A rank-scheduled chain factor removes the local cap

There is one clean sufficient face on which interval selection is
completely integral.

Let `A_0` be the `W` rank-`r` owners.  Partition the strict-lower targets
into ordered layers

\[
                         {\cal A}_1\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}{\cal A}_d,          \tag{4.1}
\]

with

\[
                         |{\cal A}_0|\ge|{\cal A}_1|\ge\cdots
                         \ge|{\cal A}_d|.                       \tag{4.2}
\]

Join `S in cal A_j` to `R in cal A_(j-1)` exactly when `S` is a strict
subset of `R`.

### Theorem 4.1 (adjacent-slice Hall ladder)

The targets and owners decompose into chains

\[
                         T\supset S_1\supset\cdots\supset S_\ell,
                         \qquad \ell\le d,                       \tag{4.3}
\]

with each member of `cal A_j` occupying position `j` if and only if, for
every `1<=j<=d`,

\[
 |N_j(X)|\ge|X|
 \qquad(X\subseteq{\cal A}_j),                              \tag{4.4}
\]

where `N_j` is the strict-containment neighbourhood in `cal A_(j-1)`.

Every such chain has a literal nonzero depth-`d` trace in which its declared
members occur at their assigned proper suffixes.  Padding a shorter chain
may create additional repeated suffix values, but it creates no compiler
deficiency.  Therefore the local target/owner common cap has zero deficiency
on this face.

#### Proof

Hall gives a matching of `cal A_j` injectively into `cal A_(j-1)` for every
`j`.  The union of the adjacent matchings has indegree and outdegree at most
one and strictly increases set size toward layer zero, hence is a disjoint
union of the chains (4.3).  The converse restricts those chains to each
adjacent pair and gives the matchings, proving (4.4).

For one nontrivial chain, put

\[
 B_0=T\setminus S_1,
 \quad B_j=S_j\setminus S_{j+1}\ (1\le j<\ell),
 \quad B_\ell=S_\ell.                                      \tag{4.5}
\]

All displayed letters are nonempty by strictness.  If `ell<d`, append
`d-ell` copies of one element of `S_ell`.  Then the suffix union starting at
`B_j` is `S_j`, and the full union is `T`.  If `ell=0`, use `B_0=T` followed
by `d` copies of any one element of `T`.  In both cases the trace has exactly
`d+1` nonempty letters.  Its padding suffixes may repeat an already covered
lower value, which is harmless because the declared compiler occurrences
remain distinct.  This gives the required trace.
`square`

Theorem 4.1 is an exact rank/schedule reduction, not an all-`k` existence
proof.  The open content is choosing the layers so that every adjacent Hall
system passes while their traces serialize in the prescribed terminal
chronology.  Independent per-owner traces need not have matching length-`d`
prefix/suffix states; that is the rooted coloured trace-Euler gate.

Thus the rigid owner-path support theorem does not by itself prove a chain
factor, but it also leaves no mysterious local common cap once such a
factor and its serialization have been constructed.

### Theorem 4.2 (exact trace-Euler serialization gate)

Fix one labelled `(d+1)`-letter trace

\[
                         B^\alpha=(B^\alpha_0,\ldots,B^\alpha_d) \tag{4.6}
\]

for every owner label `alpha`.  Make a directed multigraph whose vertices
are literal `d`-letter states and whose owner edge `alpha` is

\[
 (B^\alpha_0,\ldots,B^\alpha_{d-1})
 \longrightarrow
 (B^\alpha_1,\ldots,B^\alpha_d).                            \tag{4.7}
\]

These traces serialize into one cyclic source word, using every owner edge
once, if and only if

1. every state has equal indegree and outdegree; and
2. the nonisolated underlying graph is connected.

They serialize into one linear source word if and only if the same graph is
connected and either all degrees balance or exactly one state has
`outdegree-indegree=1`, exactly one has `indegree-outdegree=1`, and every
other state balances.

#### Proof

Consecutive `(d+1)`-windows overlap in their common `d`-letter state, so
any serialization orders the labelled edges as an Euler circuit or trail.
The degree and connectivity conditions are therefore necessary.  Conversely,
Euler's theorem orders all labelled edges in one circuit or trail.  Gluing
successive traces along their equal overlap states reconstructs the required
cyclic or linear source word. `square`

Consequently, after the adjacent-slice Hall ladder is solved, the exact
remaining local-to-global obstruction is not another target matching.  It
is the coloured edge-selection problem of choosing one legal trace for each
owner so that (4.7) is balanced and connected.  Balance without connectedness
leaves multiple source components; connectedness without balance cannot be
repaired by merely reordering the chosen traces.

## 5. Exact typed-cap obstruction after a literal atlas

Suppose now that the ordinary word/atlas has been fixed, but each target
must additionally use an occurrence-labelled route to a typed terminal
bank.  Let `Gamma` be the residual strict gammoid after the transported
background capacities and sinks have been deleted or contracted in the
declared semantics.  Let `M_S` be the complete menu of legal physical entry
ports belonging to exact occurrences of target `S`, and write

\[
                         M(X)=\bigcup_{S\in X}M_S.               \tag{5.1}
\]

### Theorem 5.1 (single-system Rado cut)

The maximum number of strict-lower targets which can receive distinct
legal typed routes is the rank of the Rado matroid

\[
 \rho(X)=\min_{Y\subseteq X}
          \bigl(|X\setminus Y|+r_\Gamma(M(Y))\bigr).           \tag{5.2}
\]

In particular all targets are routable if and only if

\[
                         r_\Gamma(M(X))\ge|X|
                         \quad(X\subseteq{\cal L}),             \tag{5.3}
\]

and the exact typed deficiency is

\[
 \boxed{
 \delta_{\rm type}
   =\max_{X\subseteq{\cal L}}
      \bigl(|X|-r_\Gamma(M(X))\bigr).}                         \tag{5.4}
\]

#### Proof

This is Rado's transversal theorem applied to the port menus in the strict
gammoid.  Taking `X=cal L` in (5.2) and subtracting its rank from `|cal L|`
gives (5.4). `square`

By Menger, (5.3) is equivalently the all-subset/all-cut condition

\[
 \operatorname{cap}(C)\ge |X|
 \quad\hbox{for every }X\subseteq{\cal L}
 \hbox{ and every admissible cut }C
 \hbox{ separating }M(X)\hbox{ from }T_{\rm sink}.              \tag{5.5}
\]

This cut is genuinely additional: two distinct exact source cells may have
only one common unit-capacity suffix sink.

### Corollary 5.2 (canonical fixed-port collapse)

If one exact source occurrence `b(S)` is fixed for every target and

\[
                         P=\{b(S):S\in{\cal L}\},               \tag{5.6}
\]

then the typed gate reduces to

\[
                         \boxed{r_\Gamma(P)=|P|.}                \tag{5.7}

\]

Equivalently, the one super-source max-flow from the complete active port
set `P` to the typed sink bank has value `|P|`.  Full-set independence is
hereditary, so no separate target-subset Hall audit remains on this
fixed-port face.

For two separately required physical occurrence systems, (5.4) is replaced
by the exact two-Rado/Edmonds disjoint-pair formula; separate marginal
full-rank claims are insufficient unless cross-system capacities and legal
ticket pairs factor in the fixed cap state.

## 6. Consequence for the rigid-rotation route

After the full fan-support, owner-path SDR, and maximal-antecedent row
identity theorems, the hierarchy is:

1. **upper owner paths:** complete and occurrence-injective;
2. **upper source cells:** automatic once compatible terminal antecedents
   and bounded-charge component joins exist;
3. **top `d` strict-lower rows:** explicit source cells in the maximal
   antecedent, with no target-to-cell matching;
4. **deeper ordinary strict-lower compiler:** exactly the interval-atlas cut
   (3.4)--(3.6), including preservation of the top-row cells, or
   conditionally the adjacent-slice Hall ladder plus the trace-Euler gate;
5. **typed external common cap:** exactly (5.4), reduced to the single
   full-port rank (5.7) after canonical occurrences are fixed.

The current rigid braid does not yet supply item 4: the generalized
full-rail common-history payload equation is impossible, and owner-path
support does not determine a lower source atlas by Proposition 2.1.  Nor
does the current record supply the private typed suffix router needed for
(5.7).

Thus the shortest honest missing theorem is a **serialized chain-atlas plus
full-port router**: select one terminal antecedent whose short interval atlas
passes (3.4)--(3.6), then prove full typed port rank after all protected
background routes.  There is no further owner/q1 or target-to-cell matching
gate beyond those two rows.

## 7. Dependencies and scope

The owner-path support and occurrence SDR are in

`MATH_THEOREM_PBBS_RIGID_ROTATION_E1_FAN_COMPLETE_SUPPORT_REPAIR_20260805.md`

and

`MATH_THEOREM_PBBS_RIGID_ROTATION_OWNER_PATH_SDR_AND_SOURCE_LIFT_BOUNDARY_20260805.md`.

The fixed-atlas criterion is the unrestricted compiler theorem in

`THREAD_A_UNRESTRICTED_COMP_TWO_BOUNDARY_LAMINAR_HALL_THEOREM_20260729.md`.

The automatic top-`d` source rows are proved in

`MATH_THEOREM_PBBS_MAXIMAL_ANTECEDENT_INTERSECTION_SOURCE_ROW_IDENTITY_20260805.md`.

The typed cut specializes the terminal common-cap Rado framework in

`MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`.

No rank layering satisfying (4.4), terminal trace-Euler selection,
residual-component antecedent, bounded opening, or full typed router is
claimed here.
