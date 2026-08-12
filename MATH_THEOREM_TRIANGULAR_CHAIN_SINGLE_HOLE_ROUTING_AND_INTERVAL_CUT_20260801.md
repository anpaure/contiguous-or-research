# Triangular chain factors: exact single-hole routing and the Boolean interval cut

Date: 2026-08-01  
Status: unconditional exchange theorem and quantitative Boolean menu bound.
This note does **not** prove that every overload has a route, and therefore
does not prove zero or bounded triangular deficiency.

## 0. Summary

Put

\[
 r=\left\lceil\frac k2\right\rceil,
 \qquad \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad W=\binom kr,
\]

and let

\[
 d=\min\left\{q:qW+\binom{q+1}{2}\ge |\mathcal L|\right\}.
\]

The exact triangular static problem has one anchored address of capacity
`d` for every rank-`r` owner and boundary addresses of capacities
`1,...,d`.

This note proves four facts.

1. Adjacent swaps inside one owner flag are **rank-pure**: they change one
   prefix value but preserve the complete address-load and rank-slot
   inventory.  They cannot by themselves repair the overload left after
   truncating an almost-uniform chain decomposition.
2. There is an exact target-preserving overload transfer.  A hole is moved
   through deletion gaps of distinct chains; only the first and last chain
   loads change.  Thus every admissible route lowers the total overload by
   one.
3. Absence of such a route has an exact **coloured state-closure**
   formulation.  The address-distinctness condition is real: erasing it
   gives an ordinary gap--target reachability graph, but that graph is only
   a relaxation.  This is the missing Boolean expansion row for this
   absorber.
4. Every underloaded anchored depth-`d` chain contains a gap with at least

   \[
                         2^{\lceil r/d\rceil}-2
   \]

   legal lower targets.  Since `r/d=Theta(sqrt(k))`, the raw first-step
   menu is `2^{Theta(sqrt(k))}`.  More generally the total interval menu of
   a chain has a sharp convex lower bound.

Consequently the STW `o(|mathcal L|)` leave can be attacked by a serial
moving-hole theorem without selecting a simultaneous packet packing.  The
unproved statement is no longer raw local supply; it is exclusion of a
proper address-coloured interval-closed state family containing all
underload holes and no overload occurrence.

Static chainization remains separate from suffix-OR serialization.  None
of the exchanges below impose the sliding cocycle.

## 1. Chain systems and gaps

Let `A` be the set of addresses.  An anchored address `a_T` has top
`top(a_T)=T`, where `T` has rank `r`, and capacity `c(a_T)=d`.  A boundary
address `partial_i` has capacity `c(partial_i)=i` and formal top `[k]`.

A complete chain system is a partition

\[
                         \mathcal L=\dot\bigcup_{a\in A} C_a,             \tag{1.1}
\]

where every `C_a` is an inclusion chain and every member of an anchored
`C_(a_T)` is contained in `T`.  No capacity condition is imposed yet.
Write

\[
 \ell_a=|C_a|,\qquad
 e_a=(\ell_a-c(a))_+,
 \qquad u_a=(c(a)-\ell_a)_+.                                  \tag{1.2}
\]

The total overload is

\[
                              \Phi(C)=\sum_a e_a.              \tag{1.3}
\]

Extend a chain by its bottom and top:

\[
 \widehat C_a=(\varnothing=S^a_0
       \subsetneq S^a_1\subsetneq\cdots\subsetneq
       S^a_{\ell_a}\subsetneq S^a_{\ell_a+1}=\operatorname{top}(a)).
                                                                    \tag{1.4}
\]

For an internal target `S=S^a_j`, its **deletion gap** is

\[
                         g_a(S)=(S^a_{j-1},S^a_{j+1}).          \tag{1.5}
\]

The ordinary gaps of `C_a` are

\[
                         (S^a_j,S^a_{j+1})quad(0\le j\le\ell_a).         \tag{1.6}
\]

A lower target `X` **fits** a gap `(P,Q)` when

\[
                               P\subsetneq X\subsetneq Q.      \tag{1.7}
\]

For a boundary address we additionally require `X in mathcal L`, as
always.  Inserting a fitting target into a gap preserves the chain and, at
an anchored address, preserves containment in its owner.

Every Boolean-half chain partition may be put in this form.  In
particular, the upper-half STW construction, after complementation and
owner anchoring as in
`MATH_THEOREM_TRIANGULAR_CHAIN_DEFICIENCY_STW_ROUNDING_AND_GK_BARRIER_20260801.md`,
gives (1.1); initially the boundary chains may be empty.

## 2. Rank-pure flag switches cannot pay load debt

Suppose an owner chain is represented by an ordering

\[
                   \pi=(x_1,\ldots,x_r)
\]

of its owner together with a selected rank set `R subseteq[r-1]`.  Its
members are the prefixes

\[
                   \{x_1,\ldots,x_s\}\qquad(s\in R).           \tag{2.1}
\]

### Proposition 2.1 (rank-slot invariance)

Swapping adjacent entries `x_s,x_(s+1)` changes only the rank-`s` prefix
in (2.1).  It preserves:

* the selected rank set `R`;
* the chain load `|R|`;
* every other prefix value.

Consequently every sequence of ownerwise adjacent-prefix switches fixes
the complete rank-incidence matrix

\[
                    M_{a,s}=\mathbf 1_{\{s\in R_a\}}           \tag{2.2}
\]

and the address-load vector `(ell_a)_a`.  Such switches alone cannot lower
`Phi(C)`.

#### Proof

Prefixes below rank `s` contain neither exchanged entry, and prefixes above
rank `s` contain both.  Only the prefix of rank `s` distinguishes their
order.  All stated invariants follow. \(\square\)

Thus adjacent flag switches are useful for resolving **which** target
occupies an already selected slot.  The STW truncation defect also contains
a slot-transfer problem: overloaded addresses must lose slots and
underloaded addresses must gain them.  That needs a cross-address move.

## 3. Exact single-hole rotation

An **admissible hole route** consists of pairwise distinct addresses

\[
                         a_0,a_1,\ldots,a_t,                    \tag{3.1}
\]

an ordinary gap `g_0` of `C_(a_0)`, and targets

\[
                         X_i\in C_{a_i}\qquad(1\le i\le t)     \tag{3.2}
\]

such that

\[
 X_1\text{ fits }g_0,
 \qquad
 X_{i+1}\text{ fits }g_{a_i}(X_i)quad(1\le i<t).              \tag{3.3}
\]

The route is **balancing** when `a_0` is underloaded and `a_t` is
overloaded.

### Theorem 3.1 (single-hole rotation)

Every admissible route defines another complete chain system by

\[
\begin{aligned}
 C'_{a_0}&=C_{a_0}\cup\{X_1\},\\
 C'_{a_i}&=(C_{a_i}\setminus\{X_i\})\cup\{X_{i+1}\}
                    &&(1\le i<t),\\
 C'_{a_t}&=C_{a_t}\setminus\{X_t\},
\end{aligned}                                                  \tag{3.4}
\]

with every other chain unchanged.  It uses exactly the same lower targets
and the same addresses.  Its load changes are

\[
 \ell'_{a_0}=\ell_{a_0}+1,
 \qquad \ell'_{a_t}=\ell_{a_t}-1,
 \qquad \ell'_{a_i}=\ell_{a_i}\ (0<i<t).                     \tag{3.5}
\]

If the route is balancing, then

\[
                                \Phi(C')=\Phi(C)-1.             \tag{3.6}
\]

#### Proof

At `a_0`, equation (3.3) says exactly that inserting `X_1` preserves the
chain.  At an internal address `a_i`, deleting `X_i` joins its predecessor
and successor into the gap (1.5), and (3.3) says that `X_(i+1)` may be
inserted into that gap.  At `a_t`, deletion preserves a chain.  Distinct
addresses make these verifications independent.

The target `X_1` moves to `a_0`, `X_2` moves to `a_1`, and so on, while
`X_t` moves to `a_(t-1)`.  Thus no target is lost or repeated.  The top of
every anchored address is part of its extended chain, so (1.7) also
preserves owner containment.  Formula (3.5) is immediate.  At an
underloaded first address the increase creates no overload, and at an
overloaded terminal address the decrease removes exactly one unit.  This
gives (3.6). \(\square\)

The theorem is serial.  After applying one route, rebuild the deletion
gaps and search for the next.  No simultaneous disjoint packet family and
no compiler valid at intermediate stages is required for the **static**
chainization problem.

### Corollary 3.2 (conditional exact triangular absorber)

Start from any complete owner/boundary chain system.  If every state with
`Phi>0` reachable by earlier rotations contains a balancing route, then a
finite sequence of rotations produces an exact integral triangular chain
factor.

Indeed, `Phi` is a nonnegative integer and decreases at every step.

This corollary concerns only static chains.  The rotations generally
change the chain atoms and do not preserve any chosen suffix-OR trace.

## 4. Exact coloured-state reachability

Address distinctness in Definition 3.1 must not be encoded by a naive
unit-capacity node.  A path entering one common address gate through the
target `X` has to leave through the **particular** deletion gap `g_a(X)`;
merging all targets at one gate loses that identity.  The correct exact
object is the following finite state graph.

A state is a pair

\[
                               (g,F),                          \tag{4.1}
\]

where `g` is a current hole gap and `F subseteq A` is the set of addresses
already used.  Initial states are

\[
             (g,\{a\}): a\text{ is underloaded and }g
                         \text{ is an ordinary gap of }C_a.    \tag{4.2}
\]

From `(g,F)`, choose a target `X in C_b` such that

\[
                            b\notin F,qquad X\text{ fits }g.   \tag{4.3}
\]

If `b` is overloaded, this is an accepting transition.  Otherwise move to

\[
                            (g_b(X),F\cup\{b\}).                \tag{4.4}
\]

### Theorem 4.1 (exact state criterion)

There is a balancing route if and only if an accepting state is reachable
from (4.2) by transitions (4.3)--(4.4).

#### Proof

A state path lists a starting gap followed by targets in new addresses.
Equations (4.3)--(4.4) are exactly (3.3), and acceptance says that the last
target comes from an overloaded address.  Thus it reads as a balancing
route.  Conversely, the successive used-address sets of any balancing
route give the displayed state path. \(\square\)

Consequently failure has an exact closure certificate: the family of all
reachable states contains every initial state, is closed under every
transition (4.4), and has no accepting transition.  In particular, for
each reachable `(g,F)`, every target strictly inside `g` whose address is
outside `F` either extends the reachable family through its deletion gap
or would end the route at an overload.

If the used-address coordinate `F` is erased, one obtains an ordinary
gap--target digraph.  Reachability of an overload there is necessary but
not sufficient for an admissible route: a walk may revisit one chain, and
simultaneous replacements at adjacent deletion gaps need not preserve its
order.  Thus ordinary Menger/Hall on the projected graph is only a
relaxation.  This coloured-state obstruction is the static analogue of the
occurrence/address correlation gates elsewhere in the OR problem.

Ordinary rank counts, the exact fractional chain LP and
Greene--Kleitman norms do not see the state coordinate `F`.  Excluding a
proper nonaccepting state closure is the precise Boolean expansion theorem
still required by this route.

### Proposition 4.2 (smallest literal selected-instance obstruction)

The accepting-route assertion is false for arbitrary selected Boolean
containment instances, already with two addresses and two targets.

Take ground set `[5]`, capacity one at both addresses, owners

\[
                   T_1=\{1,2,3\},\qquad T_2=\{3,4,5\},        \tag{4.5}
\]

and target family

\[
                   X=\{1\}\subsetneq Y=\{1,2\}.              \tag{4.6}
\]

Put `C_(T_1)=(X,Y)` and `C_(T_2)=emptyset`.  The first address has overload
one and the second underload one.  The unique source gap is
`(emptyset,T_2)`, but neither `X` nor `Y` is contained in `T_2`.  Hence the
initial state has no transition and is a nonaccepting state closure.

This is minimal in numbers of addresses and targets: overload and underload
need two addresses, and capacity-one overload needs two comparable targets.
It is a literal Boolean-containment instance, but **not** the complete
strict lower ideal.  In the complete ideal the interval below `T_2`
contains additional targets assigned to other addresses, which may open a
route.  Therefore (4.5)--(4.6) is a scope warning, not a counterexample to
the desired Boolean theorem.  It proves that completeness/exchange of the
whole ideal must enter any expansion proof.

## 5. Boolean gap abundance

The local supply in the preceding network is explicit.

### Lemma 5.1 (interval menu)

Let `(P,Q)` be a gap at an anchored address and put

\[
                              g=|Q\setminus P|.
\]

Then the number of lower targets fitting the gap is exactly

\[
                              2^g-2.                          \tag{5.1}
\]

#### Proof

Every strict intermediate set has the unique form `P union Z`, where
`Z` is a nonempty proper subset of `Q setminus P`.  Because `Q` has rank at
most `r`, every such strict intermediate set has rank below `r` and belongs
to `mathcal L`. \(\square\)

For a boundary gap with formal top `[k]`, the same formula is replaced by
the truncated binomial sum enforcing rank below `r`; this distinction is
irrelevant to the anchored lower bound below.

### Theorem 5.2 (exponential menu in every short owner chain)

Let an anchored owner chain have load `ell`.  If its `ell+1` gap dimensions
are `g_0,...,g_ell`, then

\[
                              \sum_{j=0}^{\ell}g_j=r            \tag{5.2}
\]

and

\[
 \sum_{j=0}^{\ell}(2^{g_j}-2)
 \ge
 (\ell+1)\left(2^{r/(\ell+1)}-2\right).                       \tag{5.3}
\]

In particular, some gap contains at least

\[
                         2^{\lceil r/(\ell+1)\rceil}-2          \tag{5.4}
\]

fitting targets.  If the address is underloaded, `ell<=d-1`, so this is at
least

\[
                         2^{\lceil r/d\rceil}-2
                         =2^{\Theta(\sqrt k)}.                  \tag{5.5}
\]

#### Proof

The extended chain rises from rank zero to rank `r`, proving (5.2).
Convexity of `x mapsto 2^x` gives (5.3), and the pigeonhole principle gives
`max_j g_j>=ceil(r/(ell+1))`, proving (5.4).  Finally
`d=Theta(sqrt(k))` and `r=Theta(k)`. \(\square\)

Because the gaps are consecutive in the extended chain, no target in an
ordinary gap menu belongs to the chain that owns that gap.  Thus (5.5) is
already an external-target menu.  The important qualification is global:
a large menu can still lie wholly
inside a nonaccepting coloured state closure from Theorem 4.1.  Menu size
is not reachability.

## 6. Relation to the STW leave

The STW construction gives a complete partition of the lower half into
`W` anchored chains before truncation.  Add the `d` empty boundary
addresses.  Relative to the triangular capacities, it has some overload
`Phi`; deleting the overloaded tails is exactly the previously recorded
`o(|mathcal L|)` uncovered set.

Theorems 3.1 and 5.2 give a different option: do not delete the tails.
Move holes serially from underloaded addresses toward overloaded ones.  If
the coloured state graph continues to reach an accepting transition, the
same complete target set is re-partitioned at the exact capacities, with
no leave at all.

This identifies a Boolean-specific absorber statement which would improve
the STW result:

> **STW coloured interval expansion.**  One can choose the STW almost-uniform
> chain partition so that every overload-positive state obtained by
> shortest balancing rotations has an accepting route in the state graph of
> Section 4.

The local menu at every underloaded anchored source is already
`2^{Theta(sqrt(k))}` by Theorem 5.2.  What is not proved is expansion after
address colouring, nor that serial rotations preserve the pseudorandomness
needed for later routes.

Even a weaker theorem saying that every terminal state closure strands at most
`O(d^2)` overload units would give

\[
                         \Gamma_d^\triangle=O(d^2),             \tag{6.1}
\]

by deleting only those terminal units.  A constant separator bound would
give the desired static `O(1)` theorem.

## 7. Proof-safe frontier

The static implication is now

\[
\boxed{
\begin{array}{c}
\text{STW complete but load-unbalanced chain partition}\\
\Downarrow\\
\text{single-hole interval routing (proved exact)}\\
\Downarrow\\
\text{exclude a large nonaccepting coloured state closure (open)}\\
\Downarrow\\
\text{exact or bounded-defect triangular chain factor.}
\end{array}}
\]

This does not solve serialization.  After static balancing one must still
choose traces and an Euler-compatible ordering satisfying the sliding-OR
cocycle, as isolated in
`MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`.

The principal gain is an exact reusable actuator and its exact obstruction:
the Boolean problem is not short of local candidates, and rank-pure flag
switches address the wrong invariant.  What remains is a coloured
interval-expansion theorem with address regeneration.
