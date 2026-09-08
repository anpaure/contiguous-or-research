# Three global singleton rails, exact PBBS alternating insertion, and the exponential residence distance

**Date:** 2026-08-13  
**Method:** two complementary long rails plus one guarded cleanup rail;
balanced red--blue circuit decomposition; exact PBBS short-return census  
**Status:** unconditional singleton-module and factor-level insertion theorem,
plus an unconditional no-local-graft theorem for residence.  What remains is
an exponentially supported flag-preserving resident rethread, not a local
owner/q1 insertion.

## 0. Outcome

Work on

\[
 n=2M-1,qquad \mathcal L=\binom{[n]}{M-1},qquad
 \mathcal U=\binom{[n]}M,
\tag{0.1}
\]

and put

\[
 q=d+1,\qquad c=M-q,qquad r=2q+1,qquad N=n-c=M+q-1.
\tag{0.2}
\]

In the intended regime

\[
 q^2/M\longrightarrow\pi/4.
\tag{0.3}

\]

This note proves three facts.

1. Three pairwise palette-disjoint, biresident pure rails supply **all**
   singleton targets simultaneously.  They use

   \[
   2N+r=2M+4q-1=n+4q
   \tag{0.4}
   \]

   owners and have only three components.

2. Their incidence cycles extend to an exact spanning owner/q1 two-factor.
   Relative to the canonical PBBS factor, this extension is an exact
   equal-size union of alternating-circuit exchanges.

3. No local alternating graft can simultaneously repair PBBS residence.
   For `q>=5`, every `q`-resident factor on the same owners deletes at least

   \[
   {2^{M-2}-1\over5}
   \tag{0.5}
   \]

   projected PBBS transitions.  Thus the resident integration, if it
   exists, is necessarily a global rethread.

The first two facts remove the singleton and owner/q1 insertion gates.  The
third prevents them from being confused with the still-open residence and
all-width flag-transport theorem.

## 1. Pure rails of arbitrary long period

Let `C` be a `c`-set and let

\[
 T=(z_0,\ldots,z_{s-1})
\tag{1.1}

\]

be a cyclic order of distinct labels outside `C`, where `s>=2q+1`.  Put

\[
 P_i=C\cup\{z_i\},
\tag{1.2}

and define the three central rows

\[
 \begin{aligned}
 L_i&=C\cup\{z_i,\ldots,z_{i+q-2}\},\\
 O_i&=C\cup\{z_i,\ldots,z_{i+q-1}\},\\
 U_i&=C\cup\{z_i,\ldots,z_{i+q}\}.
 \end{aligned}
\tag{1.3}

\]

### Lemma 1.1 (long pure rail)

The owner row `(O_i)` is a simple Johnson cycle, its immediate-lower and
immediate-upper palettes `(L_i)` and `(U_i)` are simple, and its toggle
traces are

\[
 1^q0^{s-q}.
\tag{1.4}

\]

Hence the rail is two-sided `q`-resident.

#### Proof

Consecutive `q`-windows delete `z_i` and insert `z_(i+q)`, so they are
Johnson adjacent.  Since the labels are distinct and `s>=2q+1`, two cyclic
windows of any of the three lengths `q-1,q,q+1` coincide only when their
starts coincide.  A toggle label occurs in exactly `q` consecutive owner
windows and is absent for `s-q>=q+1`; a core label is constant.  \(\square\)

### Lemma 1.2 (guarded simultaneous caps)

Suppose some positions are declared guards and every cyclic `(q-1)`-window
contains a guard.  Leave guard letters maximal as in `(1.2)` and cap every
other position `i` to `{z_i}`.  Then all three rows `(1.3)` are unchanged,
and every capped position is a literal singleton cell.

#### Proof

Every window of length at least `q-1` contains a maximal guard and hence
still contains the whole core.  Capping never changes its toggle label.
Thus every displayed union is unchanged.  \(\square\)

For a cyclic word of length `s`, a prescribed guard set of cardinality

\[
 a(s)=\left\lceil{s\over q-1}\right\rceil
\tag{1.5}

\]

can be ordered with at most `q-2` active positions between successive
guards, because `s-a(s)<=a(s)(q-2)`.

## 2. Two long rails and one cleanup rail

Assume eventually

\[
 c>q+1,qquad
 a:=\left\lceil{N\over q-1}\right\rceil\le2q-2.
\tag{2.1}

\]

Both inequalities follow from `(0.3)`.

Choose disjoint `c`-sets `C_1,C_2`.  This is possible since
`2c=2M-2q<n`.  Put

\[
 T_1=[n]\setminus C_1,qquad
 T_2=[n]\setminus C_2.
\tag{2.2}

\]

Then

\[
 |T_1|=|T_2|=N,qquad
 T_1\cup T_2=[n],qquad
 I:=T_1\cap T_2,quad |I|=2q-1.
\tag{2.3}

\]

Choose `a`-element guard sets `G_1,G_2 subseteq I` with the least possible
intersection

\[
 \ell:=|G_1\cap G_2|=max\{0,2a-(2q-1)\}.
\tag{2.4}

\]

By `(2.1)`, `ell<=2q-3`.  Order `T_j` so `G_j` is a guard set as in
Lemma 1.2.  A label is active in at least one of the two long rails unless
it belongs to

\[
 D=G_1\cap G_2.
\tag{2.5}

\]

Choose an active set `A_3` of size `2q-2` containing `D`, and then choose
three guard labels outside `A_3`; these guards may be labels already active
in a long rail.  Let `T_3` be their disjoint union, so `|T_3|=r`,
and order its active labels in three runs of length at most `q-2`, separated
by its three guards.

Finally choose a `c`-set `C_3` disjoint from `T_3` and satisfying

\[
 d_J(C_3,C_j)>q+1\qquad(j=1,2).
\tag{2.6}

\]

Such a core exists eventually: among the `binom(n-r,c)` candidates
disjoint from `T_3`, the two forbidden Johnson balls have total size at
most

\[
 2\sum_{t=0}^{q+1}\binom ct\binom{n-c}t
 =\exp(o(M)),
\tag{2.7}

\]

whereas

\[
 \binom{n-r}{c}=\binom{2c-2}{c}=exp(\Theta(M)).
\tag{2.8}

\]

### Theorem 2.1 (three-rail global singleton module)

The two period-`N` rails `(C_1,T_1),(C_2,T_2)` and the period-`r` rail
`(C_3,T_3)` have pairwise disjoint owner, immediate-lower, and
immediate-upper palettes.  After the guarded caps above, every singleton
`{x}`, `x in [n]`, occurs on at least one active cell, while all three
palettes of all three rails are unchanged.  Their total owner use is
`(0.4)`.

#### Proof

The first two cores are disjoint, so

\[
 d_J(C_1,C_2)=c>q+1.
\tag{2.9}

\]

Together with `(2.6)`, all three core distances exceed `q+1`.  If one
rank-`M+j` set, `j in {-1,0,1}`, belonged to palettes of two rails, it
would contain both cores and therefore

\[
 c+d_J(C_i,C_j)\le M+j=c+q+j,
\tag{2.10}

\]

contradicting the core distance for every `j<=1`.  Thus the three palettes
are pairwise disjoint.

The long toggle sets cover `[n]`.  Their only labels capped in neither
long rail are precisely `D`, and `D subseteq A_3`, so the cleanup rail
caps all of them.  Lemma 1.2 preserves every named palette.  The owner
count is `2N+r=2M+4q-1`.  \(\square\)

This improves an `O(n/q)`-component reserve to **three components** without
changing the `n+O(q)` owner scale or introducing any singleton defect.

## 3. Exact factor insertion

Let `P` be the union of the three alternating owner/lower incidence cycles
from Theorem 2.1.  It has

\[
 |E(P)|=2(2N+r)=4M+8q-2
\tag{3.1}

\]

incidence edges and maximum degree two.

### Theorem 3.1 (owner/q1 extension)

For all sufficiently large parameters satisfying `(0.3)`, `P` extends to
a spanning two-factor of the middle-levels incidence graph.

#### Proof

Within one cyclic interval rail, a fixed lower vertex lies below at most
two protected owners, and a fixed owner contains at most two protected
lower vertices.  Across three rails the two protected-Ore exposures are
therefore at most six.

The protected small/co-small localization cutoff is

\[
 Q={M(M-1)\over2M-1}|E(P)|=O(M^2).
\tag{3.2}

\]

For a small shore, exact loss is at most `6|A|`.  Since
`Q<binom(M+3,3)` eventually, Kruskal--Katona and the exact shadow-slack
identity give

\[
 \sigma(A)>{M-2\over M-1}\left({M\over4}-1\right)|A|>6|A|.
\tag{3.3}

\]

For a co-small optional core, every owner has at least `M-6` free facets.
The partial-shadow core theorem forces its size to be at least

\[
 \binom{2M-15}{M-8}+1=\exp(\Theta(M)),
\tag{3.4}

\]

contradicting `(3.2)`.  Thus no protected Ore cut fails, and bipartite
`b`-matching integrality supplies the extension.  \(\square\)

Let `F_0` be the canonical PBBS incidence two-factor and let `F` be any
extension supplied by Theorem 3.1.

### Theorem 3.2 (exact alternating insertion normal form)

The symmetric difference

\[
 F_0\mathbin\triangle F
\tag{3.5}

\]

decomposes into edge-disjoint even circuits alternating between
`F_0 setminus F` and `F setminus F_0`.  Toggling these circuits one at a
time transforms `F_0` into a factor containing the three singleton rails,
and every circuit deletes and inserts the same number of incidences.

#### Proof

At every incidence vertex, the red degree from `F_0 setminus F` equals the
blue degree from `F setminus F_0`, because both factors have degree two.
Every nonempty balanced red--blue component therefore has an alternating
Euler decomposition.  Splitting at repeated vertices gives alternating
even circuits.  Toggling one circuit preserves degree two and simplicity;
edge-disjointness permits iteration.  Alternation gives equal red and blue
cardinality on each circuit.  \(\square\)

This proves factor-level insertion.  It gives no useful upper bound on the
total circuit support.

## 4. PBBS residence is exponentially far away

Write `m=M-1`, so the PBBS ground size is `n=2m+1`.  Let `J_0` be its
projected Johnson owner factor.  The exact PBBS run census gives, for
`q>=5`,

\[
 N_3^++N_4^+=n(2^{m-1}-1)
\tag{4.1}

\]

coordinate-labelled positive runs of lengths three or four.

For one such run, let its **closed edge span** consist of its entering
edge, internal edges, and leaving edge.  Its size is at most five.

### Lemma 4.1 (exponential edge-disjoint run packing)

The family of closed spans in `(4.1)` has an edge-disjoint subfamily of
size at least

\[
 \boxed{\nu_q(J_0)\ge {2^{m-1}-1\over5}.}
\tag{4.2}

\]

#### Proof

For a fixed coordinate, closed spans of distinct positive runs are
edge-disjoint.  Hence one projected owner edge lies in at most one closed
span per coordinate, and therefore in at most `n` spans total.  A greedy
matching in this rank-at-most-five interval hypergraph selects at least

\[
 {N_3^++N_4^+\over5n}
 ={2^{m-1}-1\over5}
\tag{4.3}

\]

pairwise edge-disjoint spans.  \(\square\)

### Theorem 4.2 (residence edit lower bound)

Let `J` be any Johnson two-factor on the same rank-`M` owner set whose
proper positive coordinate runs all have length at least `q>=5`.  Then

\[
 \boxed{
 |E(J_0)\setminus E(J)|
 \ge {2^{m-1}-1\over5}.}
\tag{4.4}

\]

The same lower bound holds for the number of deleted PBBS incidence edges
in any incidence factor projecting to `J`.

#### Proof

If every edge of one closed short-run span were retained in `J`, its
internal vertices would already have their two factor edges fixed, and its
two boundary edges would retain the adjacent zero states.  Up to reversing
the component orientation, the same isolated positive run of length three
or four would therefore survive in `J`, contradicting `q`-residence.

Thus at least one old edge must be deleted from every member of the
edge-disjoint family in Lemma 4.1, proving `(4.4)`.  Each projected PBBS
edge is subdivided by its unique lower facet.  Deleting that projected
adjacency requires deleting at least one of its two PBBS incidence edges,
so the incidence statement follows.  \(\square\)

More quantitatively, if `t=|E(J_0) setminus E(J)|`, then at least

\[
 \left({2^{m-1}-1\over5}-t\right)_+
\tag{4.5}
\]

members of the fixed edge-disjoint family from Lemma 4.1 survive as
literal short positive runs in `J`: one deleted old edge can hit at most
one member of that disjoint family.  Thus `(4.4)` is also a stability
statement for every partially changed PBBS background.

### Corollary 4.3 (no local PBBS graft closes residence)

No alternating-circuit exchange of support `poly(m)` can turn canonical
PBBS into a `q`-resident factor when `q>=5`.  In particular, the
`n+O(q)`-owner singleton module cannot be integrated by an `O(n)`-support
graft **and simultaneously serve as the global residence repair**.

This is not an obstruction to inserting the singleton module alone:
Theorem 3.2 does that abstractly.  It is an obstruction to treating the
remaining PBBS chronology as an unchanged resident background.

## 5. Exact remaining theorem

The PBBS route now requires an exponentially supported alternating
rethread which simultaneously:

1. retains the three guarded singleton rails, or opens and reconnects them
   through source-transparent collars;
2. hits every PBBS return arc of gap at most `2q-3` and creates no new
   short run;
3. transports at least one designated occurrence of every PBBS all-width
   upper target through the rethread; and
4. preserves exact owner and q1 use.

The symmetric-difference theorem proves that item 4 alone is always an
alternating-circuit problem.  Theorem 4.2 proves that the required circuit
system cannot have local support.  Items 2--3 are therefore the genuine
global correlation theorem; protected Ore completion by itself cannot
prove them.

For a `B(k)+O(1)` theorem, the three reserve components are bounded rather
than growing, so singleton topology is no longer an asymptotic obstruction.
Eventual equality still requires their zero-defect fusion into the global
resident chronology.
