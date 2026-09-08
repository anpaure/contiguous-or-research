# The protected twin bank has an exact fixed-`M_0` one-oriented host min--max

**Date:** 2026-08-01  
**Lane:** A, reset--return upper Ferrers twin bank / rooted Catalan host  
**Status:** exact central equivalence and exact scope audit.  No all-`m`
existence theorem is claimed.

## 0. Verdict

The local theorem
`MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`
has removed the cut-collateral obstruction.  Its opened packet, two Ferrers
banks and residence collars form an `O(d)` protected collection of Johnson
paths.  Relative to a fixed predecessor matching `M_0`, embedding this
collection in one owner-exact, lower-rainbow, immediate-upper-surjective
Hamilton path is equivalent to one explicit zero--one system.

There is only one genuine arc variable.  Once the lower colour of a directed
Johnson edge is rooted by `M_0`, its tail owner, head owner and immediate
upper colour are all forced.  In particular, the disjoint second-facet
projection from
`MATH_THEOREM_HEAD_INJECTIVE_COMPLETION_AND_PROTECTED_INDUCED_PATH_20260801.md`
does not solve this system: an arbitrary second facet need not be the unique
`M_0`-legal head.

The exact scalar central obstruction is

\[
 \Delta_{M_0}({\cal P})
 =W-1+U-\max_F\bigl(|F|+|\operatorname{up}(F)|\bigr).       \tag{0.1}
\]

Here `F` ranges over `M_0`-legal directed path forests containing the
protected arcs.  Thus `Delta=0` if and only if the desired central Hamilton
host exists.  This is an **integral** maximum, not the value of its LP
relaxation and not a degree-only rainbow theorem.

Even `Delta=0` closes only the owner, lower-`q1`, upper-`q1` and topology
rows.  Residence of the unprotected bulk, exterior arbitrary-width upper
witnesses, exact maximal erosion and the terminal occurrence-labelled
compiler remain additional joint predicates on the same ordered path.
Global reversal means that those predicates need be solved in one
orientation only; it does not remove any of them.

## 1. Fixed-root coordinates

Let the ground set have order `2m-1`, and write

\[
 \mathcal L={[2m-1]\choose m-1},\qquad
 \mathcal O={[2m-1]\choose m},\qquad
 \mathcal U={[2m-1]\choose m+1},                         \tag{1.1}
\]

\[
 W=|\mathcal L|=|\mathcal O|,\qquad
 U=|\mathcal U|,\qquad C=W-U=\operatorname {Cat}_m.       \tag{1.2}
\]

Fix a perfect incidence matching

\[
 M_0:\mathcal L\longrightarrow\mathcal O,qquad
 p\subset M_0(p).                                        \tag{1.3}
\]

Define the legal rooted arc set

\[
 \mathcal A(M_0)=\{(p,q):p,q\in\mathcal L,\ p\ne q,
                                  p\subset M_0(q)\}.       \tag{1.4}
\]

For `a=(p,q)` put

\[
 T(a)=M_0(p),\qquad V(a)=M_0(q),\qquad
 \operatorname{low}(a)=p,qquad
 \operatorname{up}(a)=T(a)\cup V(a).                    \tag{1.5}
\]

Because `p` is contained in the two distinct rank-`m` sets `T(a),V(a)`,

\[
 T(a)\cap V(a)=p,qquad |\operatorname{up}(a)|=m+1.       \tag{1.6}
\]

Thus `a` is exactly the oriented Johnson edge `T(a)->V(a)` rooted at its
lower colour.

### Lemma 1.1 (fixed-`M_0` atom bijection)

The map (1.5) bijects `A(M_0)` with the oriented Johnson edges `T->V`
which obey

\[
                         M_0(T\cap V)=T.                  \tag{1.7}
\]

Equivalently, if `R=T union V` and `T subset R`, put

\[
 L=M_0^{-1}(T),\qquad b=R-T,\qquad
 V_{M_0}(R,T)=L\cup\{b\}.                                \tag{1.8}
\]

Then `(R,T)` is not a free two-endpoint choice: its only legal head is
`V_(M_0)(R,T)`.

#### Proof

Equation (1.6) proves that every arc in (1.4) gives an edge satisfying
(1.7).  Conversely, for an edge satisfying (1.7), set `p=T cap V` and
`q=M_0^{-1}(V)`.  Then `p subset V=M_0(q)` and `p ne q`, so `(p,q)` lies in
(1.4), and (1.5) recovers the original edge.  Formula (1.8) follows because
`T=L+a` and `R=T+b`, with `a ne b`.  \(\square\)

## 2. The protected input and its only extra hypothesis

After a fixed common suspension into `J(2m-1,m)`, let `\mathcal P` be the
opened reset path, the two Ferrers-bank paths and their two one-sided
residence collars from the frozen twin-bank theorem.  Choose an orientation
on each protected path; henceforth `\mathcal P` denotes the resulting set
of directed Johnson edges.

The local theorem proves that the protected owners and lower colours are
simple, that its path interiors are resident, and that its packet-plus-bank
intervals cover the exact two upper Ferrers triangles.  It does **not**
choose `M_0`.  The exact fixed-root interface is therefore

\[
             M_0(T\cap V)=T\quad\text{for every }T\to V
             \text{ in }\mathcal P.                       \tag{2.1}
\]

When (2.1) holds, write
`\mathcal P_{M_0}\subseteq\mathcal A(M_0)` for the corresponding root
arcs.  If no choice of the path orientations satisfies (2.1), the fixed
`M_0` face is impossible.  This is a compatibility obstruction, not a
failure of the local twin-bank theorem.

The fixed-protected-subgraph extension theorem used in the twin-bank note
provides an owner/lower-`q1` projection (under its stated size hypothesis).
It does not imply the upper-colour or rooted-head rows below.

## 3. Exact one-oriented host system

For every `a=(p,q) in A(M_0)` introduce `z_a in {0,1}`.  The system is

\[
 z_a=1\qquad(a\in\mathcal P_{M_0}),                       \tag{H0}
\]

\[
 \sum_{q:(p,q)\in\mathcal A(M_0)}z_{p,q}\le1
       \qquad(p\in\mathcal L),                            \tag{H1}
\]

\[
 \sum_{p:(p,q)\in\mathcal A(M_0)}z_{p,q}\le1
       \qquad(q\in\mathcal L),                            \tag{H2}
\]

\[
 \sum_{(p,q)\in\mathcal A(M_0):\,p,q\in S}z_{p,q}
       \le |S|-1
       \qquad(\varnothing\ne S\subseteq\mathcal L),       \tag{H3}
\]

\[
 \sum_{a\in\mathcal A(M_0)}z_a=W-1,                     \tag{H4}
\]

and

\[
 \sum_{a:\operatorname{up}(a)=R}z_a\ge1
       \qquad(R\in\mathcal U).                           \tag{H5}
\]

### Theorem 3.1 (fixed-`M_0` protected-host equivalence)

For every `m,d`, every fixed matching `M_0`, and every suspended oriented
protected collection satisfying (2.1), system (H0)--(H5) is feasible if
and only if there is one
oriented Hamilton path on all `W` middle owners which

1. contains every protected path as a contiguous oriented subpath;
2. uses every middle owner exactly once;
3. has pairwise-distinct lower-`q1` colours (hence exactly one omitted
   lower colour); and
4. covers every immediate-upper colour.

The path is `M_0`-coherent: an edge of lower colour `p` is directed out of
`M_0(p)`.

#### Proof

Let `F={a:z_a=1}`.  Conditions (H1)--(H2) give rooted outdegree and
indegree at most one.  Condition (H3) says that the underlying root graph
is a forest.  By (H4), this forest has `W` vertices and `W-1` edges, so it
is connected.  A connected forest of maximum undirected degree two is a
path; (H1)--(H2) force its orientation to be consistent.  Transporting the
root order through the bijection `M_0` gives a Hamilton path on the middle
owners.  Its outgoing roots are exactly its lower colours, so they are
distinct.  Condition (H5) is precisely immediate-upper surjectivity.
Forcing every protected arc makes each protected block contiguous: every
internal protected vertex already has its incoming and outgoing slots
saturated.

Conversely, orient the asserted owner path from its initial to its terminal
owner and contract every `M_0` edge.  Lemma 1.1 gives legal root arcs.
Path degrees give (H1)--(H2), acyclicity gives (H3), its size gives (H4),
upper surjectivity gives (H5), and protected containment gives (H0).
\(\square\)

### Corollary 3.2 (exact upper-representative/connector lift)

In any solution of (H0)--(H5), choose one selected arc of each upper colour
and call these `x`-arcs.  Call the remaining arcs `y`-arcs.  Then

\[
 |x|=U,\qquad |y|=W-1-U=C-1.                              \tag{3.1}
\]

The `x`-arcs form an upper-exact rooted Catalan forest; the `y`-arcs are
exactly a connector tree for its `C` components.  Conversely, let `X` be
such an upper-exact rooted forest and let `Y` consist of `C-1` legal root
arcs which join the components of `X` as a tree.  If `X union Y` contains
the protected arcs and is **root-slot compatible**--every root has
indegree and outdegree at most one--then `X union Y` gives a solution of
(H0)--(H5).  The slot condition is essential: an abstract tree on the
components can attach twice at the same directed endpoint and need not be
a Johnson Hamilton path.

The opened packet and the two uncollared Ferrers banks have pairwise
distinct certified upper colours, so their arcs may be chosen as `x`-arcs
without loss.  The collar theorem only needs their physical arcs forced;
unless global upper-colour distinctness of a particular collar is proved,
its arcs must not automatically be declared `x`-arcs.

This corollary shows that the sequential forest/connector description and
the direct one-path system are exactly equivalent.  It also avoids a false
extra quantifier: the representative/connector designation is bookkeeping,
not additional physical structure.

## 4. Exact integral deficiency

Let `\mathfrak F_{M_0}(\mathcal P)` be the family of all arc sets
containing `\mathcal P_{M_0}` and
satisfying (H1)--(H3).  Put

\[
 \operatorname{up}(F)=\{\operatorname{up}(a):a\in F\}.     \tag{4.1}
\]

Every member has at most `W-1` arcs and at most `U` upper colours.  Define

\[
 \boxed{
 \Delta_{M_0}(\mathcal P)
  =W-1+U-
    \max_{F\in\mathfrak F_{M_0}(\mathcal P)}
        \bigl(|F|+|\operatorname{up}(F)|\bigr).}          \tag{4.2}
\]

If the protected set is itself incompatible, set `Delta=+infinity`.

### Theorem 4.1 (min--max obstruction)

`Delta_(M_0)(P)=0` if and only if (H0)--(H5) is feasible.

#### Proof

Both summands inside the maximum attain their separate ceilings exactly
when `|F|=W-1` and `up(F)=U`.  These are (H4) and (H5).  The remaining
conditions are the definition of the maximization domain.  \(\square\)

For a literal zero--one optimization, add indicators `c_R` and maximize

\[
                 \sum_a z_a+\sum_R c_R                  \tag{4.3}
\]

subject to (H0)--(H3) and

\[
 c_R\le\sum_{a:\operatorname{up}(a)=R}z_a,qquad
 c_R\in\{0,1\}.                                          \tag{4.4}
\]

The optimum is `W-1+U-Delta`.  Formula (4.2) is an exact **integral**
packing obstruction.  No claim is made that the LP relaxation is integral
or that (H1)--(H5) collapse to degree inequalities.  The abstract
degree-only rainbow shortcut is unavailable; the Boolean-specific
fixed-`M_0` correlation (1.4)--(1.8) is load-bearing.

## 5. Projection audit

The following implications are exact.

* Dropping (H2)--(H4) gives an upper-to-tail matching projection.  The
  central-shadow Hall surplus can solve that projection with protected
  tickets.
* Choosing arbitrary distinct second facets gives a second-endpoint
  projection.  It need not satisfy (1.8), and therefore does not imply a
  feasible arc of `A(M_0)`.
* Conditions (H1)--(H2) without (H3) give a directed path--cycle factor,
  not a forest or Hamilton path.
* Conditions (H1)--(H4) without (H5) give an owner/lower-rainbow Hamilton
  path, but not an upper-surjective one.

In the two-endpoint notation `psi(R)=T`, `phi(R)=V`, the exact rooted row is

\[
 M_0(\psi(R)\cap\phi(R))=\psi(R),                         \tag{5.1}
\]

or equivalently `phi(R)=V_(M_0)(R,psi(R))`.  Repeated intersections and
nonextendable lower-to-tail assignments are precisely what an arbitrary
`phi` can miss.  Thus none of the two projections is a sufficient host
theorem.

## 6. What must be added for the actual twin-bank induction host

A solution `F` of Theorem 3.1 has a unique directed root order

\[
 p_0,p_1,\ldots,p_{W-1},qquad O_i=M_0(p_i).              \tag{6.1}
\]

It already contains every local Ferrers-bank witness because the protected
path blocks are contiguous.  It is a complete one-oriented induction host
only if the following additional, order-sensitive rows also hold.

1. **Residence and antecedent.**  The owner word `(O_i)` satisfies the
   required depth-`d` signed residence and endpoint states.  Its maximal
   erosion letters

   \[
    A_j=\bigcap_{i:\ i\le j\le i+d}O_i                  \tag{6.2}
   \]

   (with the evident linear boundary range) are nonempty and reconstruct
   every owner: `union_(j=i)^(i+d) A_j=O_i`.
2. **Exterior all-width deck.**  For every inherited upper target `S`
   outside the already-certified local packet/twin-bank ledger, some
   consecutive owner interval satisfies

   \[
                         \bigcup_{i=s}^{t}O_i=S.           \tag{6.3}
   \]

   Under (6.2), the corresponding source interval is literal.  The local
   theorem proves (6.3) only for its own two Ferrers triangles and surviving
   packet inventory.
3. **Terminal compiler and one-word cap.**  On this same source `A`, form the
   exact occurrence graph whose edges are literal target--cell equalities
   passing every cap, deadline and guard.  It must have the required
   target-saturating matching.  In zero--one form, for allowed incidences
   `(S,c)` this is

   \[
    \sum_c g_{S,c}=1,qquad \sum_S g_{S,c}\le1,qquad
    g_{S,c}\in\{0,1\}.                                   \tag{6.4}
   \]

   Here "one-word" means common to all selected rows in this one
   orientation.  It does not mean a fixed-address matching in a
   two-phase intersection.

4. **Regenerative endpoint state.**  The two global endpoints and the
   carried sidecar obey the next-step interface.  This is not implied by
   the fact that the protected blocks have legal local collars.

These rows are jointly necessary and sufficient once the induction's
target family, cap/guard catalogue and endpoint state are fixed: Theorem
3.1 supplies the unique owner order, (6.2) supplies its source, (6.3)
supplies every exterior upper witness, and (6.4) is exactly the residual
compiler SDR.  They are not consequences of `Delta=0`.

If desired, the whole statement is a finite zero--one formulation: use
standard position variables for the directed Hamilton order, forbid every
short signed coordinate run, introduce interval-OR witness variables for
(6.3), and use (6.4) for the compiler.  This is an exact encoding, not an
integrality theorem.

## 7. Reversal quotient and exact remaining gate

Suppose the complete **physical** state consisting of `(O,A)`, all
witnesses, compiler matching and endpoint data is closed under global
reversal.  Then the reversal theorem transports the reversed owner order,
(6.2)--(6.4), and the endpoint state bijectively.  One solves the
one-oriented system once and reflects the complete certificate.  No
fixed-address matching in `G^+ cap G^-`, no phase-common exterior bank and
no second compiler are required.

The fixed-`M_0` chart itself is not asserted to be reversal-invariant.
Indeed an edge reversal keeps its lower colour but exchanges its physical
tail and head, whereas (1.7) roots that colour at the tail.  Thus the same
`M_0` will generally not certify the reversed path.  A different
predecessor matching may do so, but the global-reversal quotient needs no
such second chart: it transports the already completed physical
certificate, not a second solution of (H0)--(H5).

This does not help before the protected components are joined: relative
component orientations remain real choices.  Nor does reversal decrease
`Delta`, create exterior witnesses, repair residence, or pay compiler
deficiency.

Consequently the weakest exact remaining theorem is:

> Choose a compatible `M_0` and an orientation of the protected packet and
> twin-bank paths for which `Delta_(M_0)(P)=0`, and choose a zero-deficiency
> maximizer satisfying (6.2)--(6.4) and the regenerative endpoint state.

The frozen twin-bank theorem proves the protected local ledger inside this
statement.  It does not prove the displayed global choice.
