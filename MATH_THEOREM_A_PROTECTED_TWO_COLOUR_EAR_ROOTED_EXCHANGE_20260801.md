# Protected two-colour ears: exact rooted exchange and the singleton-fragment obstruction

Date: 2026-08-01  
Lane: A / protected boundary macro and compatible rooted state  
Status: unconditional fixed-state exchange theorem and exact obstruction.
No all-dimensional existence of a compatible rooted state is claimed.

## 0. Verdict

The repaired bridge singleton of item 2490A and the native J7 two-colour
fusion of item 2491H2 remove genuine **local** source and palette
obstructions.  They do not by themselves imply that the fusion can be
inserted in an upper-exact rooted Catalan state.

For a fixed predecessor matching `M0`, a two-colour path ear is a rooted
two-edge chain

\[
                 x_0\longrightarrow x_1\longrightarrow x_2.       \tag{0.1}
\]

Let `f_0,f_1` be the unique representatives in an upper-exact rooted forest
`Q0` of the two upper colours of (0.1).  Replacing `f_0,f_1` by (0.1)
preserves all four rooted rows if and only if

1. the two new tail resources and two new head resources are free after
   deleting `f_0,f_1`; and
2. `x_0,x_1,x_2` lie in three pairwise distinct components of
   `lambda(Q0-{f_0,f_1})`.

There is no further matching/head/upper/graphic condition.

If a deficiency-one connector has already been chosen, with full rooted
tree `T`, then the same exchange preserves that connector if and only if
the three roots lie in three distinct components of
`T-{f_0,f_1}`.  Equivalently, the two new ear edges reconnect the three cut
fragments as a path rather than closing two of them into a cycle.

There is a sharper directed obstruction.  If the rest of the Hamilton
connector is frozen, matching feasibility forces `x_1` to be a singleton
fragment of `T-{f_0,f_1}`.  Thus the two old representatives must be
consecutive around `x_1`, or one of the cuts must isolate a global endpoint.
The two exterior ends of the ear must then attach to the **two different**
remaining fragments.  If they attach to the same fragment, the result is
exactly one directed cycle plus one directed path.  The fixed certificate
has ordered-Hall deficiency two, not one.

This is the minimal rooted/topological obstruction left after the native
two-colour palette fusion.  It is not detected by separate provider counts.

## 1. Rooted notation

Fix a perfect incidence matching `M0` between the lower and middle shores
of `ML_m`.  Identify a lower vertex with a **root**.  An incidence

\[
                         e=(x,M_0(y))                  \tag{1.1}
\]

outside `M0` has rooted link

\[
                    \lambda(e):x\longrightarrow y,   \tag{1.2}
\]

tail resource `x`, head resource `M0(y)`, and upper colour

\[
                    u(e)=M_0(x)\cup M_0(y).           \tag{1.3}
\]

For a set `S` of such incidences write

\[
       t(S)=\{x:(x,M_0(y))\in S\},\qquad
       h(S)=\{y:(x,M_0(y))\in S\}.                   \tag{1.4}
\]

The incidence set `S` is a matching exactly when both sets in (1.4) have
size `|S|`.  Its rooted links form a forest exactly when they are independent
in the ordinary graphic matroid on the roots.

Let `Q0` be an upper-exact rooted Catalan forest: it is a matching, its
links form a forest, and `u` is a bijection from `Q0` to the rank-`m+1`
upper colours.

A **simple rooted two-colour ear** is

\[
 E=\{e_0,e_1\},\qquad
 e_0=(x_0,M_0(x_1)),\quad e_1=(x_1,M_0(x_2)),          \tag{1.5}
\]

where `x_0,x_1,x_2` are distinct and

\[
                         u(e_0)\ne u(e_1).             \tag{1.6}
\]

Let `f_i` be the unique edge of `Q0` with `u(f_i)=u(e_i)`, and put

\[
             F=\{f_0,f_1\},\qquad
             Q_0^E=(Q_0-F)\cup E.                     \tag{1.7}

Common edges should first be cancelled from `E` and `F`.  The theorem below
is the genuine two-for-two case `E cap Q0=emptyset`.

## 2. Exact rooted-state absorption

### Theorem 2.1 (forced-representative two-ear exchange)

Assume that the two old representatives in `F` are unprotected, or that
their replacement by `E` is explicitly authorized.  Subject to the fixed
edge-local guard/common-basis admissibility of the two new incidences,
`Q0^E` is again an upper-exact rooted Catalan forest if and only if both of
the following hold.

**Resource condition**

\[
 \{x_0,x_1\}\cap t(Q_0-F)=\varnothing,
 \qquad
 \{x_1,x_2\}\cap h(Q_0-F)=\varnothing.               \tag{2.1}
\]

**Three-component condition**

\[
 \operatorname{comp}_{\lambda(Q_0-F)}(x_0),\quad
 \operatorname{comp}_{\lambda(Q_0-F)}(x_1),\quad
 \operatorname{comp}_{\lambda(Q_0-F)}(x_2)
 \quad\hbox{are pairwise distinct}.                  \tag{2.2}
\]

In particular (2.1)--(2.2) are the complete
tail/head/upper/graphic test for the exchange.

#### Proof

The upper-colour partition row forces the deletion of exactly `f_0,f_1`:
they are the unique old representatives of the colours supplied by `E`.
After this forced deletion the upper row is automatically restored by
(1.5)--(1.7).

The two tails of `E` are `x_0,x_1`, and its two head roots are `x_1,x_2`.
They are internally distinct.  Therefore the two partition-matroid rows
are preserved exactly when (2.1) holds.

The graph `lambda(Q0-F)` is a forest.  Adding `x_0x_1` increases its
graphic rank exactly when `x_0,x_1` lie in different components.  After
that addition, adding `x_1x_2` increases rank exactly when `x_2` lies in
neither of those first two components.  This is precisely (2.2).  Both
new links then increase rank, so the final graph has `|Q0|` edges and the
same number of components as `lambda(Q0)`; hence it is a rooted Catalan
forest.  Conversely, failure of one of the three separations creates a
graphic circuit.  This proves necessity and sufficiency. `square`

### Matroid interpretation

After contracting `Q0-F`, the upper partition matroid has already fixed the
two-element choice `E`.  The two matching partition matroids reduce to
(2.1), while the graphic contraction reduces to (2.2).  Thus Theorem 2.1
is not merely a list of necessary rows: it is the exact common-independence
test on this forced two-colour fibre.

## 3. Preserving a deficiency-one connector

Let

\[
                    Q=Q_0\mathbin{\dot\cup}A          \tag{3.1}
\]

be a certificate for `Delta(P)=1`: `Q` is an incidence matching of size
`W-1`, `T=lambda(Q)` is a spanning tree (hence a directed Hamilton path),
and `A` is the `C-1` connector matching between the rooted components of
`Q0`.  Put

\[
                         Q^E=(Q-F)\cup E.              \tag{3.2}

### Theorem 3.1 (connector-preserving two-ear criterion)

Assume all declared boundary, socket and protected-resource predicates are
unchanged or explicitly reverified after the exchange.  Then the **same**
connector set `A` certifies `Delta(P union E)=1` if and only if

\[
 \{x_0,x_1\}\cap t(Q-F)=\varnothing,
 \qquad
 \{x_1,x_2\}\cap h(Q-F)=\varnothing,                 \tag{3.3}
\]

and

\[
 \operatorname{comp}_{T-F}(x_0),\quad
 \operatorname{comp}_{T-F}(x_1),\quad
 \operatorname{comp}_{T-F}(x_2)
 \quad\hbox{are pairwise distinct}.                  \tag{3.4}

Here the stated conclusion includes the requirement that the resulting
Hamilton path has the declared protected macro at its prescribed global
end.  If only Hamiltonicity is wanted, omit that final boundary check.

#### Proof

Condition (3.3) is exactly the assertion that (3.2) remains an incidence
matching.  Since `T` is a tree and `F` consists of two distinct tree edges,
`T-F` has exactly three components.  Adding the two links of `E` gives a
tree exactly when their component images have graphic rank two, which for
the chain (1.5) is exactly (3.4).  In that case `lambda(Q^E)` is a spanning
tree and `Q^E` is a matching of size `W-1`; its directed indegree and
outdegree are at most one, so it is a directed Hamilton path.  The bank
`Q0^E` remains upper-exact by Theorem 2.1 (or simply because it is a subset
of this tree and its two forced colours were replaced).  Contracting its
components shows that the surviving set `A` is a `C-1` connector matching.
The ordered-Hall theorem therefore gives deficiency one.

Conversely, if the same connector set survives as a Hamilton certificate,
then (3.2) is a matching and a tree, forcing (3.3) and rank two in the
three-component quotient, namely (3.4). `square`

### Proposition 3.2 (exact fixed-certificate defect ledger)

Assume (3.3), and let `rho` be the graphic rank of the two component edges
induced by `E` after contracting every component of `T-F`.  Then

\[
 \#\operatorname{comp}\lambda(Q^E)=3-\rho,
 \qquad
 \operatorname{cycl}\lambda(Q^E)=2-\rho.             \tag{3.5}
\]

If `Q0^E` passes Theorem 2.1, every cycle in `lambda(Q^E)` contains an edge
of `A`.  Deleting one unprotected `A`-edge from every cycle leaves an
upper-exact rooted path cover with exactly

\[
                              3-\rho                  \tag{3.6}
\]

paths.  Thus the old certificate gives the quantitative bound

\[
                    \Delta(P\mathbin\cup E)\le3-\rho \tag{3.7}
\]

at the owner/lower-`q1`/immediate-upper layer, provided the resulting path
cover obeys the declared boundary guards.  Under the directed matching
hypotheses of Corollary 3.3 below, `rho` is either two or one: the exchange
respectively preserves deficiency one or yields the elementary
cycle-plus-path deficiency-two state.

#### Proof

The tree `T` loses two edges, hence has three components.  Adding the two
quotient edges of rank `rho` leaves `3-rho` components.  The resulting
graph has `W` vertices and `W-1` edges, so its total cyclomatic number is

\[
 (W-1)-W+(3-\rho)=2-\rho.
\]

Because `Q0^E` is a forest, every cycle uses an edge of `A`.  Removing one
such edge per cycle preserves the number of connected components and turns
every maximum-degree-two component into a path.  The upper representatives
in `Q0^E` are untouched.  This proves (3.5)--(3.7). `square`

### Corollary 3.3 (exact singleton-fragment law)

Under (3.3), the root `x_1` is a singleton component of `T-F`.  Therefore
one of the following is necessary:

1. the two old representatives `f_0,f_1` are consecutive arcs of `T`, one
   entering and one leaving `x_1`;
2. the first cut isolates the global initial root `x_1`; or
3. the last cut isolates the global terminal root `x_1`.

Let the other two components of `T-F` be `K` and `K'`.  Condition (3.4)
is then equivalent to

\[
        x_0\in K,\ x_2\in K'\qquad\hbox{or}\qquad
        x_0\in K',\ x_2\in K.                        \tag{3.8}
\]

If instead `x_0,x_2` lie in the same one of `K,K'`, then `Q^E` is exactly
the disjoint union of one directed cycle and one directed path.  Provided
`Q0^E` satisfies Theorem 2.1, the cycle contains a connector edge from `A`;
deleting one such unprotected edge gives a two-path cover.  Thus this fixed
state has deficiency at most two, and in the absence of another admissible
port arc its deficiency is exactly two.

#### Proof

Deleting two arcs from a directed Hamilton path leaves three directed path
fragments.  Their ends are exactly the tail resources free after deletion,
and their starts are exactly the head-root resources free after deletion.
By (3.3), `x_0,x_1` are fragment ends and `x_1,x_2` are fragment starts.
Hence `x_1` is both the start and the end of one fragment, so that fragment
is a singleton.  This gives the three listed possibilities.

The two ear arcs join the singleton fragment to the fragments containing
`x_0` and `x_2`.  They join all three fragments into a path exactly in
(3.8).  If those two roots lie in the same exterior fragment, the ear
closes that fragment together with `x_1` into a directed cycle and leaves
the third fragment as a directed path.  Since `Q0^E` is a forest, the cycle
uses at least one edge of `A`; opening it gives two paths. `square`

### Consequence for the global minimum

Theorems 2.1 and 3.1 are relative to a fixed admissible state and, in
Theorem 3.1, a fixed deficiency-one connector.  Their failure does **not**
prove `Delta(P union E)>1`: a different common basis, predecessor matching,
upper representative forest or ordered connector may work.  They do prove
that a two-colour local fusion cannot be advertised as a universal
augmentation of an arbitrary `Delta=1` certificate.

## 4. Minimal two-edge port obstruction

The singleton law has a five-root abstract obstruction.  Let the old rooted
Hamilton path be

\[
                 1\to2\to3\to4\to5,                  \tag{4.1}
\]

put the two upper representatives

\[
                 F=\{1\to2,\ 3\to4\},                \tag{4.2}
\]

and regard `2->3,4->5` as the old connector arcs.  Give `1->2` and `5->1`
one upper colour, and `3->4` and `1->4` a second colour.  The replacement

\[
                         5\to1\to4                    \tag{4.3}
\]

is a simple two-colour ear.  Its tails and heads are free after (4.2) is
deleted.  As a replacement for the rooted upper bank it is a forest:

\[
                  5\to1\to4,\qquad\{2\},\qquad\{3\}.
\]

Thus the two matching rows, the two upper representatives and the rooted
graphic row all pass.  But together with the frozen connector arcs it is

\[
                    (1\to4\to5\to1)\quad\dot\cup\quad(2\to3), \tag{4.4}
\]

one cycle plus one path.  With no further port arcs the ordered deficiency
is exactly two.

This example is an abstract rooted-port system, not a claimed Boolean
diamond counterexample.  Its purpose is exact: matching/head/upper/graphic
feasibility of the new `Q0` does not imply preservation of the old ordered
connector.  The extra three-fragment row (3.4) is logically indispensable.

## 5. Native J7 fusion: exact rooted gate

For the forward orientation of item 2491H2, the native path is

\[
       30844\longrightarrow26750\longrightarrow27246. \tag{5.1}
\]

Its two lower colours are `26748,26734`.  In rooted coordinates it can lie
on the `Q0` shore only if

\[
 M_0(26748)=30844,\qquad M_0(26734)=26750.             \tag{5.2}
\]

Writing

\[
                         z=M_0^{-1}(27246),            \tag{5.3}
\]

the forced ear is

\[
 26748\longrightarrow26734\longrightarrow z,         \tag{5.4}
\]

represented by the incidences

\[
 (26748,26750),\qquad(26734,27246).                    \tag{5.5}
\]

Their upper colours are exactly `30846,27262`.  Hence every upper-exact
`Q0` has forced old representatives

\[
                         f_{30846},f_{27262}.           \tag{5.6}
\]

The fusion is absorbed in that rooted state if and only if

1. the tails `26748,26734` and heads `26750,27246` are free in
   `Q0-{f_30846,f_27262}`;
2. the three roots `26748,26734,z` lie in distinct components of
   `lambda(Q0-{f_30846,f_27262})`; and
3. the still-separate parent demand `28926`, the three exported child
   colours `26878,27502,30972`, and every fixed guard/common-basis row are
   simultaneously satisfied.

To preserve a previously chosen deficiency-one connector without changing
its other arcs, replace `Q0` by the full connector `Q` in conditions 1--2.
Corollary 3.3 then says that the root `26734` must be the singleton fragment
created by deleting the two old representatives, and the roots `26748,z`
must lie in the two different exterior fragments.

The `10/18/12` surviving provider counts and the `1,584` pairwise-disjoint
provider triples in item 2491H2 verify that condition 3 has no immediate
three-child zero row.  They do not verify (5.2), either component condition,
the parent `28926` row, or compatibility with one common basis.  Thus the
native fusion kills the frozen `K_{3,2}` palette core but does not yet prove
nonemptiness of the compatible rooted state or `Delta(P)=1`.

For the reversed physical path, the analogous predecessor requirements are

\[
 M_0(26734)=27246,\qquad M_0(26748)=26750,             \tag{5.7}
\]

and the rooted ear is

\[
 26734\longrightarrow26748\longrightarrow M_0^{-1}(30844). \tag{5.8}
\]

Whether this phase is allowed is a source-level macro decision, not a
consequence of the rooted exchange theorem.

## 6. Repaired first bridge and scope audit

The bridge repair of Proposition 10.1 in item 2490A replaces one source
letter `{g1}` by `K+{a1,a3,g1}` in both phases.  It changes no owner, no
rooted incidence, no upper colour, and no tail/head/graphic row.  Therefore
Theorems 2.1--3.1 apply to the repaired comparator with exactly the same
rooted data as to its abstract owner chronology; the repair supplies the
previously missing literal lower cell and nothing more.

The following qualifications are load-bearing.

1. The theorem concerns immediate upper colours and the rooted owner/lower
   `q1` connector.  Higher accumulated unions, exterior residence and the
   common source cap remain separate.
2. A fixed-state exchange is not an existence theorem for `Sigma(P)`.
   In particular, (5.2) is a correlated restriction on `M0`, not an
   edge-local provider count.
3. If the macro is prescribed at a global boundary, the new Hamilton path's
   actual free head/free tail must realize that placement.  Treehood alone
   does not choose the desired orientation.
4. Removing a representative protected by another macro is forbidden
   unless a joint replacement was part of the declared state.
5. The abstract obstruction of Section 4 proves the necessity of the
   three-fragment row in a general rooted-port theorem.  It is not an
   unrestricted physical impossibility for Boolean diamonds.

The sharp proved boundary is therefore:

\[
\boxed{
\begin{array}{c}
\text{native two-colour ear absorption}\cr
\Updownarrow\cr
\text{forced representative deletion + resource freedom}\cr
\text{+ a three-component rooted-forest test,}
\end{array}}
\tag{6.1}
\]

and, for a fixed completed connector, one additional three-fragment test
decides exactly between preservation of deficiency one and the elementary
cycle-plus-path obstruction.
