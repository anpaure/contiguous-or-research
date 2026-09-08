# The tight odd-diamond augmenter has two exact rooted phases and a
# private-gammoid completion face

Date: 2026-08-01  
Lane: owner-layer multi-funnel / protected pivot / relative upper completion  
Status: unconditional local phase classification, exact forest and endpoint
ledgers, and an exact conditional alternating-forest completion theorem.  No
global availability or final Catalan connector theorem is claimed.

## 0. Outcome

The owner-slot move in
`MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md`
replaces one auxiliary diamond by a target diamond and a rerouted copy of
the auxiliary colour.  After a first incidence matching `M_0` has been
fixed, the complete catalogue has exactly two rooted phase types; a fixed
`M_0` admits at most one of them for a given tuple.  In either admitted phase

* one missing upper colour is installed while every old upper colour is
  retained;
* the rooted support gains one edge;
* two dynamic union--find tests are necessary and sufficient for graphic
  independence; and
* every successful move lowers the forest component count by one.

The cleaner **D-phase** is

\[
 M_0(L)=A,\qquad M_0(L')=D,
 \qquad
 L\to H\ \longmapsto\ L\to P,\ L'\to H,             \tag{0.1}
\]

where `P=M_0^{-1}(B)` and `H=M_0^{-1}(C)`.  It preserves the old tail and
old head roles and consumes only the new outgoing port at `L'` and the new
incoming port at `P`.  Its exact endpoint ledger is

\[
 \operatorname {Src}(Q^+)=\operatorname {Src}(Q)\setminus\{P\},
 \qquad
 \operatorname {Term}(Q^+)=\operatorname {Term}(Q)\setminus\{L'\}. \tag{0.2}
\]

In physical-owner language this consumes source owner `B` and terminal
owner `D`.  The other phase is valid but changes an old head into a new
tail and consequently needs a stronger terminal-edge guard.

This gives a genuine constant local splice while a **relative**
upper-colour forest is being built.  It is not a duplicate-colour connector:
its deleted edge is the unique selected provider of its auxiliary upper
colour.  Once the forest is upper-exact, a pure one-to-two matching move
cannot supply any of the final `Cat_m-1` connector edges.

There is also an exact completion reduction.  A packed dependency forest of
phase-compatible augmenters gives one simultaneous protected exchange.  On
the private one-blocker face this is precisely a vertex-disjoint linkage,
so strict-gammoid rank/Menger cuts are necessary and sufficient.  With two
or three blockers the dependency object is an AND forest and ordinary Hall
is no longer exact.  The raw `Theta(m^4)` owner-slot menu does not imply even
one rooted leaf after `M_0`, occupancy and topology are imposed.

## 1. Local diamond data

Let `|Omega|=2m-1`.  Fix an upper target `R`, ordered distinct `a,b in R`,
`c notin R`, and `x in L=R-{a,b}`.  Put

\[
\begin{array}{lll}
 A=L+a,&B=L+b,&C=L+c,\\
 L'=(L-x)+c,&&D=(L-x)+a+c,
\end{array}                                                        \tag{1.1}
\]

and `S=L+a+c`.  The three diamonds are

\[
 f=(S,L;A,C),\qquad e=(R,L;A,B),\qquad g=(S,L';C,D).                \tag{1.2}
\]

Thus `f` has upper colour `S`; `e` has colour `R`; and `g` has colour
`S`.  The owner-slot theorem proves the exact resource inclusion

\[
 V(f)\subseteq V(e)\cup V(g),                                     \tag{1.3}
\]

with only the new lower resource `L'` and new owner-slot resources at
`B,D`, besides the target `R`.  Its exact labelled menu size through fixed
`R` is

\[
                  16(m+1)m(m-2)(m-1).                             \tag{1.4}
\]

Equation (1.4) is an owner-slot count before a rooted phase is imposed.

## 2. Complete fixed-`M_0` phase classification

Fix a perfect incidence matching `M_0` from rank `m-1` roots to rank `m`
owners.  Write

\[
 \phi(T)=M_0^{-1}(T),\qquad p_M(X)=M_0(X)\setminus X.               \tag{2.1}
\]

A selected diamond `(U,X;T,H)` contracts to the rooted link
`X -> phi(H)` when `M_0(X)=T`, with the two owners interchanged when the
other incidence is selected.

### Theorem 2.1 (the two phases are necessary and sufficient)

The three diamonds in (1.2) can simultaneously be rooted with the common
owner `A` retained from `f` to `e` if and only if

\[
 p_M(L)=a                                                     \tag{2.2}
\]

and one of the following two alternatives holds.

* **C-phase:** `p_M(L')=x`, equivalently `M_0(L')=C`.
* **D-phase:** `p_M(L')=a`, equivalently `M_0(L')=D`.

Put `P=phi(B)`, `H=phi(C)` and `Q_D=phi(D)`.  The rooted links are

\[
\begin{array}{c|c|c|c}
 &f&e&g\\ \hline
 C\text{-phase}&L\to L'&L\to P&L'\to Q_D\\
 D\text{-phase}&L\to H&L\to P&L'\to H.
\end{array}                                                        \tag{2.3}
\]

In both rows the colour action is `S -> {R,S}`.

#### Proof

The owner sets of `f` and `e` intersect only in `A`:

\[
                         \{A,C\}\cap\{A,B\}=\{A\}.                 \tag{2.4}
\]

Hence retaining their common rooted tail forces `M_0(L)=A`, which is
(2.2).  The owners of `g` are exactly `C,D`, so its lower row `L'` must be
matched to one of those two owners.  Since `C=L'+x` and `D=L'+a`, these are
exactly the two displayed pivots.  Substitution into the contraction rule
gives (2.3).  Conversely, either row of (2.3) consists of legal rooted
links, and the union identities

\[
 A\cup C=S,\qquad A\cup B=R,\qquad C\cup D=S                      \tag{2.5}
\]

give the colour action.  There is no third phase. \(\square\)

### Corollary 2.2 (exact free-port and endpoint ledger)

Let a directed linear forest `Q` contain `f`.

In the D-phase the replacement is a directed matching if and only if `L'`
has a free outgoing port and `P` has a free incoming port after deleting
`f`.  The incoming port at `H` is freed by deleting `f` and restored by
`g`.  Whenever the graphic guard in Section 3 also passes, (0.2) holds.

In the C-phase, `f=L->L'` must be the terminal edge of its component: `L'`
must have a free outgoing port.  In addition, `P` and `Q_D` must have free
incoming ports.  Its endpoint ledger is

\[
 \operatorname {Src}(Q^+)
 =\bigl(\operatorname {Src}(Q)\cup\{L'\}\bigr)\setminus\{P,Q_D\},
 \qquad
 \operatorname {Term}(Q^+)=\operatorname {Term}(Q)\setminus\{L'\}. \tag{2.6}
\]

#### Proof

In the D-phase deleting `L->H` frees the outgoing port of `L` and incoming
port of `H`.  The two new links use respectively `(L,P)` and `(L',H)`, so
the old two ports are restored and only the source `P` and terminal `L'`
are consumed.  In the C-phase deletion of `L->L'` makes `L'` a source;
the new edges consume incoming ports at `P,Q_D` and the outgoing port at
`L'`.  This gives (2.6). \(\square\)

Thus the D-phase preserves a distinguished source `s_*` and terminal `t_*`
provided `P != s_*`, `L' != t_*`, and `f` is not protected.  In physical
owners these conditions are `B != M_0(s_*)` and `D != M_0(t_*)`.

## 3. Exact topology and component ledger

Delete the physical edge `AC` from a physical linear forest `F`, and call
the result `F_0`.  The proposed support is

\[
                         F_0+AB+DC.                                \tag{3.1}
\]

### Theorem 3.1 (two-query union--find criterion)

Subject to the directed free-port conditions in Corollary 2.2, (3.1) is a
linear forest if and only if

1. `A,B` lie in different components of `F_0`; and
2. after uniting those components, `D,C` still lie in different
   components.

Equivalently, the two unordered component pairs in the original `F_0` are
nonloops and are not equal.  In either rooted phase, this is the same test
after applying the bijection `phi`.  When it passes,

\[
 |E(F^+)|=|E(F)|+1,\qquad \kappa(F^+)=\kappa(F)-1.                 \tag{3.2}
\]

#### Proof

Deleting one edge of a forest leaves a forest.  A new edge preserves
acyclicity exactly when it joins two different components.  Apply this
twice.  Directed role capacity gives degree at most two, hence the result is
a linear forest.  Finally (3.2) follows from the edge count and Euler's
forest identity. \(\square\)

The guard is dynamic.  Final graphic independence certifies a simultaneous
exchange, but a literal sequence of pure one-to-two moves must pass these
two tests in the current forest at every step.

## 4. What can be planted prospectively in `M_0`

For each of `t` labelled augmenters choose either phase.  Its two required
incidence rows are

\[
 (L,A),\quad (L',C)\ \text{in the C-phase};
 \qquad
 (L,A),\quad (L',D)\ \text{in the D-phase}.                         \tag{4.1}
\]

### Proposition 4.1 (bounded phase planting)

Let `P_0` be a protected predecessor matching of size `p`.  If all `2t`
rows in (4.1) are pairwise disjoint, avoid `P_0`, and

\[
                             p+2t\le m-1,                           \tag{4.2}
\]

then the protected small-matching extension theorem gives one perfect
`M_0` containing `P_0` and all phase rows.

This proves fixed-matching compatibility for a bounded prospective bank.
It does **not** say that the auxiliary providers `f` are selected, their
ports are free, or their union--find tests pass.  Nor does the unrooted
count (1.4) imply a positive number of rows satisfying (4.1) for an
arbitrary already-fixed `M_0`.

## 5. Exact relative-completion certificates

Let

\[
 W={2m-1\choose m-1},\qquad U={2m-1\choose m+1},
 \qquad W-U=\operatorname {Cat}_m.                                 \tag{5.1}
\]

A spanning forest with `U-d` selected upper colours has exactly
`Cat_m+d` components.  Therefore `d` successful augmentations install the
missing colours and give exactly `Cat_m` components.  The following theorem
allows occupied new resources to be cleared by a finite dependency forest.

### Theorem 5.1 (packed alternating-forest exchange)

Let `Q` be a fixed-`M_0` rooted upper-colour forest missing the colour set
`D_0`, `|D_0|=d`, and let `P_0` be a literally protected selected bank.
Suppose a finite family `A` of `n` phase-compatible augmenters has the
following data.

1. Its dependency nodes form a rooted forest whose `d` roots target the
   colours in `D_0` bijectively.
2. The auxiliary providers `F={f_alpha:alpha in A}` are distinct selected
   edges of `Q-P_0`.
3. Let `H` be the **entire** set of edges in `Q-F` that meet any genuinely
   new role/slot resource of an augmenter.  Then `H` is disjoint from both
   `F` and `P_0`; every `h in H` blocks exactly one parent node; and that
   parent has a unique child whose target upper colour is `col(h)`.  This
   assignment is a bijection from `H` to the nonroot nodes.
4. After deleting `F union H`, all new pairs `{e_alpha,g_alpha}` are
   mutually role/slot-disjoint, are role/slot-disjoint from every edge of
   `Q-(F union H)` (hence from the retained `P_0`), and give distinct upper
   colours.
5. The final rooted-link support

\[
 (Q\setminus(F\cup H))\cup
       \{e_\alpha,g_\alpha:\alpha\in A\}                           \tag{5.2}
\]

   is graphic-independent.

Then (5.2) is an upper-exact protected rooted forest with exactly
`Cat_m` components.

#### Proof

A forest on `n` dependency nodes with `d` roots has `n-d` parent--child
edges, hence `|H|=n-d`.  The exchange removes `n+(n-d)` selected edges and
adds `2n`, a net gain of `d`.

Every `g_alpha` restores the auxiliary colour of `f_alpha`.  Every nonroot
`e_alpha` restores the colour of its unique blocker in `H`, while the root
`e_alpha` install the missing colours `D_0`.  Thus the upper row is exact.
Hypothesis 4 gives the lower/head/tail rows, Hypothesis 5 gives the graphic
row, and avoidance preserves `P_0`.  Equation (5.1) gives the final
component count. \(\square\)

This is a simultaneous exchange.  It serializes into literal pure
one-to-two moves only if there is additionally an order in which each new
pair avoids all still-selected future auxiliary providers and passes the
current two-query union--find guard.  Without those rows, delete-all then
insert-all is the only certified realization.

### Theorem 5.2 (exact uncapacitated trap dual)

Ignore cross-node resource and graphic collisions, and let `B(alpha)` be
the set of blocker **colours** for a candidate augmenter.  Starting from

\[
 C_0=\{R:\text{some candidate for }R\text{ has }B(\alpha)=\varnothing\},
\]

define

\[
 C_{i+1}=C_i\cup
 \{R:\text{some candidate for }R\text{ has }B(\alpha)\subseteq C_i\}. \tag{5.3}
\]

A target `R` has a finite well-founded augmenter tree if and only if
`R in C_infty`.  Equivalently, failure is witnessed by a nonempty trap `X`
containing `R` such that every candidate targeting a colour in `X` has at
least one blocker colour in `X`.

#### Proof

Membership in `C_i` is equivalent by induction to a dependency tree of
height at most `i`.  If `R` never enters the closure, its complement is the
claimed trap.  Conversely, no leaf-removal process can leave a trap. \(\square\)

### Theorem 5.3 (an exact ordinary min--max face)

Assume every candidate has at most one blocker and the catalogue is
**private/linkage-faithful**: protected resources are deleted, every
consumed phase gadget has its own capacity-one node, paths cannot splice
through a shared bundle, and graphic independence is automatic for a
chosen linkage.  Make a directed network with an arc from target colour
`R` to blocker colour `S` for a one-blocker candidate and an arc to a free
sink for a blocker-free candidate; split every consumed resource to
capacity one.

Then joint completion of `D_0` is equivalent to `d` vertex-disjoint paths
from `D_0` to the sink bank.  Hence it exists if and only if

\[
                         r_\Gamma(D_0)=d,                            \tag{5.4}
\]

where `r_Gamma` is strict-gammoid rank, equivalently every separating
node cut has capacity at least `d`.

With `n_j` dependency nodes having `j` children, every rooted dependency
forest satisfies

\[
 n_0=d+\sum_{j\ge2}(j-1)n_j.                                      \tag{5.5}
\]

Thus two- and three-blocker candidates create extra leaf demand.  Their
general packed problem is an AND--OR hypergraph with partition and graphic
rows, not ordinary reachability or marginal Hall.  Equation (5.4) is exact
only on the stated private one-blocker face.

## 6. Exact interface with funnels, reserves and the pivot

The D-phase gives the clean sector splice.  Delete a provider
`f:L->H`, exposing the prefix ending at `L` and suffix starting at `H`.
If a reserved component starts at `P` and another ends at `L'`, the links

\[
                         L\to P,\qquad L'\to H                      \tag{6.1}
\]

join those pieces whenever the free-port and union--find guards pass.  Both
reserved interiors remain literal.  The move consumes the source `P` and
terminal `L'`; therefore a protected pivot source and terminal must not be
those ports.

Three qualifications are load-bearing.

1. **Provider, not connector.**  The deleted `f` is the unique selected
   provider at upper colour `S`.  It is not one of the SCD braid's
   duplicate-colour connector arcs.  Applying the move to a certified
   funnel provider requires revalidating the adjacent connector ports.
2. **Frozen reserve.**  A fixed-row isolated reserve edge cannot be used as
   `f` while also being claimed literally protected.  If it is to be
   replaced, the choice must be made before freezing and `g` must be
   declared its replacement provider.  Otherwise use only its free source
   or terminal port as in (6.1).
3. **Quotient symmetry.**  A single literal splice normally breaks the
   clean cyclic quotient.  An equivariant use must develop the whole
   parameter tuple over the quotient group and replay orbit-resource and
   voltage acyclicity; otherwise it is charged as a non-equivariant seam.

For the `m=3r+2` route, the `Cat_r` automatic isolated-edge bank remains a
valid protected reserve.  If a phase-compatible candidate realizes an
allowed source/terminal pair, the augmenter can attach those reserve ports
while completing a missing colour in the relative free bulk.  No such
candidate is proved to exist here.  In particular, the move neither removes
the `Cat_r` symmetry-breaking requirement nor services the internal
multi-funnel mass `I_m` for free.

Finally, a direct local move need not exist despite (1.4).  Every target
edge `e` for fixed `R` uses one of the facets `B=R-a`.  If both labelled
slots of every one of those `m+1` facets are occupied, every raw candidate
is blocked at `B`, even if free slot mass exists elsewhere.  Fixed-phase
and topology tests can only shrink this menu.  This refutes the inference
from polynomial local supply to a free augmenter, not the possibility of
an alternating tree.

## 7. Remaining exact theorem

The local splice has reduced the relative-completion problem to one of two
precise targets:

* prove full strict-gammoid rank for a protected private one-blocker atlas;
  or
* construct a packed AND dependency forest satisfying Theorem 5.1.

The atlas must be chosen jointly with `M_0`, the selected provider forest,
the `Cat_r`/multi-funnel reserve, and the pivot ports.  A serial physical
realization must additionally satisfy future-provider avoidance and the
dynamic union--find order.

After upper completion there are still exactly `Cat_m` components.  The
separate distinguished-source, one-defect-Hall connector braid must merge
them with `Cat_m-1` duplicate-colour edges.  Residence, deeper upper
witnesses and the common compiler cap remain outside the present theorem.
