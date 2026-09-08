# Audit of the double-crossrail C8 bridge and its protected Catalan resource bank

Date: 2026-08-01  
Lane: Thread D / C8 physical bank / protected Catalan embedding  
Status: the local bridge, palettes, residence, twelve-facet completion, and
component counts are correct.  Equations (4.1)--(4.2) of the theorem needed
the common core `K`, which has been restored.  The exact `M_0/Q_0/Q_1`
resource ledger is derived below.  No spanning-carrier or common-source
embedding is claimed.

Audited input theorem SHA-256:
`b756440aff59a4333c9cd920a09b896eae9ff02f55e0f107dc5d7e12df7f4348`.
Corrected working theorem SHA-256 (common `K` and componentwise-residence
scope restored):
`936d82c8eda8e3ed2b41ebc4996747e703964e5fb36f09e22ecefbec78bd5256`.

## 0. Verdict

For `d>=2`, the bridge

\[
 G_1,\ldots,G_d,B,A,H_1,\ldots,H_d,D,E              \tag{0.1}
\]

is a simple rank-`r` Johnson path with `2d+4` owners and `2d+3`
pairwise-distinct lower colours.  Its upper multiset has support four, with
multiplicities

\[
                 d,\quad1,\quad d+1,\quad1.           \tag{0.2}
\]

The two physical rails in its maximal-envelope source give both complete
cross banks in one state, on `4(d-1)` distinct interval addresses.  Each
individual ticket consists of two adjacent disjoint intervals; intervals
belonging to different tickets may overlap, as expected for nested rays.

Adding twelve disjoint Johnson edges supplies the other twelve canonical
upper values.  The result has exactly

\[
        13\text{ components},\qquad 2d+28\text{ owners},
        \qquad2d+15\text{ Johnson edges},               \tag{0.3}
\]

and all `2d+15` lower colours are distinct.

After incidence subdivision, the protected forest has `4d+30` incidence
edges.  A proper alternating colouring gives two matching banks of size
`2d+15` each.  Relative to a perfect extension `M_0`, the canonical
maximum-protected-representative assignment is

\[
 \boxed{
 |P_0|=2d+15\text{ forced in }M_0,qquad
 |A_0|=16\text{ forced upper representatives in }Q_0,qquad
 |A_1|=2d-1\text{ forced repeated-colour connectors in }Q_1.} \tag{0.4}
\]

Here the twelve auxiliary edges and four selected bridge occurrences form
`A_0`; all remaining bridge occurrences form `A_1`.  More generally, if
`A_0=P_1 cap Q_0`, upper injectivity gives `|A_0|<=16` and hence
`|A_1|>=2d-1`; a global `Q_0` may represent one of these colours on an
unprotected occurrence, so equality is optimal but not forced.  The full
protected link bank is a thirteen-path forest, but a global `Q_0` extension
must still avoid connecting the endpoints of an `A_1` edge before that edge
is added.  Thus (0.4) is an exact minimal-connector seed, not a Catalan
completion theorem.

## 1. Bridge transitions and lower colours

Put

\[
 F=\{f_0,f_1,\ldots,f_d,f_{d+1}\},\qquad
 F^\circ=\{f_1,\ldots,f_d\},                            \tag{1.1}
\]

and

\[
 U=K\cup\{z,a_1,a_3\}\cup F^\circ,\qquad
 M_+=U+f_{d+1},\qquad M_-=U+f_0.                        \tag{1.2}
\]

The owners are

\[
 G_i=M_+-f_i,\quad H_i=M_--f_i,\quad
 B=M_+-a_3,\quad A=M_--a_3,\quad
 D=M_--a_1,\quad E=M_+-a_1.                             \tag{1.3}
\]

Every step of (0.1) exchanges one coordinate.  Its intersections split
into the following seven classes:

\[
\begin{array}{ll}
 M_+-\{f_i,f_{i+1}\},&1\le i<d,\\
 M_+-\{f_d,a_3\},&G_dB,\\
 K\cup\{z,a_1\}\cup F^\circ,&BA,\\
 M_--\{a_3,f_1\},&AH_1,\\
 M_--\{f_i,f_{i+1}\},&1\le i<d,\\
 M_--\{f_d,a_1\},&H_dD,\\
 K\cup\{z,a_3\}\cup F^\circ,&DE.
\end{array}                                             \tag{1.4}
\]

The first two lines contain `f_(d+1)` but not `f_0`; the middle-left lines
have active signature `za_1`; the `H` lines contain `f_0` but not
`f_(d+1)`; and the final lines have active signature `za_3`.  Within an
internal sweep, the omitted filler pair determines the edge.  These
signatures prove that all `2d+3` values in (1.4) are distinct, including
the endpoint case `d=2`.

The corresponding upper values are

\[
\begin{array}{c|c}
 M_+&d\text{ occurrences}\cr
 K\cup\{z,a_1\}\cup F&1\text{ occurrence}\cr
 M_-&d+1\text{ occurrences}\cr
 K\cup\{z,a_3\}\cup F&1\text{ occurrence}.
\end{array}                                             \tag{1.5}
\]

Indeed the `G` sweep together with `G_dB` contributes `d` copies of `M_+`;
`BA` is the first chord; `AH_1`, the `H` sweep, and `H_dD` contribute
`d+1` copies of `M_-`; and `DE` is the second chord.  This proves (0.2).

## 2. Residence and the two physical rails

Coordinates in `K union {z}` persist.  The `a_1` run has length `2d+2`;
the internal/right `a_3` run and the `f_0` run have length `d+2`; and the
safe `f_(d+1)` run has length `d+1`, with its remaining occurrence clipped
at the right boundary.  For `1<=s<=d`, the run between the two absences
`G_s,H_s` is

\[
 G_{s+1},\ldots,G_d,B,A,H_1,\ldots,H_{s-1},            \tag{2.1}
\]

of length

\[
                         (d-s)+2+(s-1)=d+1.             \tag{2.2}
\]

All other filler runs meet a path endpoint.  Hence the asserted internal
residence floor is exact.

In the maximal source, the left rail occupies positions `d+1,...,2d` and
has letters

\[
 q_s^{(1)}=
 \begin{cases}
 K\cup\{z,a_1,f_s\},&s=1,d,\\
 \{f_s\},&1<s<d,
 \end{cases}                                           \tag{2.3}
\]

while the right rail occupies `2d+3,...,3d+2` with `a_3` in place of
`a_1`.  Prefix/suffix union gives, for `1<=j<d`,

\[
\begin{aligned}
 P_1(j)&=K\cup\{z,a_1\}\cup F[1,j],&
 S_0(j+1)&=K\cup\{z,a_1\}\cup F[j+1,d],\\
 P_0(j)&=K\cup\{z,a_3\}\cup F[1,j],&
 S_1(j+1)&=K\cup\{z,a_3\}\cup F[j+1,d].
\end{aligned}                                          \tag{2.4}
\]

The two intervals in each row partition one rail and are adjacent and
disjoint as source intervals.  There are `2(d-1)` tickets and `4(d-1)`
distinct interval addresses.  Their constant unions are respectively
`K+za_1+F^circ` and `K+za_3+F^circ`.  This proves simultaneous physical
realization of both cross matchings in one cap state.

### 2.1 Every lower colour occurs at its native shared address

Let the bridge owners be `T_0,...,T_(2d+3)` and its source be
`Q_0,...,Q_(3d+3)`.  The native depth-`d-1` cell shared by consecutive
owners is

\[
                         J_i=\bigcup_{p=i+1}^{i+d}Q_p.   \tag{2.5}
\]

Since `D^dQ=T`, one always has `J_i subseteq T_i cap T_(i+1)`.  For the
double crossrail, direct union of the displayed maximal cells and the two
rails gives equality in every edge class:

\[
\begin{array}{c|c}
\text{transition}&J_i=T_i\cap T_{i+1}\cr \hline
G_sG_{s+1}&M_+-\{f_s,f_{s+1}\},\quad1\le s<d\cr
G_dB&M_+-\{f_d,a_3\}\cr
BA&K\cup\{z,a_1\}\cup F^\circ\cr
AH_1&M_--\{a_3,f_1\}\cr
H_sH_{s+1}&M_--\{f_s,f_{s+1}\},\quad1\le s<d\cr
H_dD&M_--\{f_d,a_1\}\cr
DE&K\cup\{z,a_3\}\cup F^\circ.
\end{array}                                             \tag{2.6}
\]

The two chord rows are especially transparent: their shared source blocks
are exactly the complete left and right rails.  For `G_dB`, the first
`d-1` left-rail fillers together with the preceding maximal cell add
`f_(d+1)`; the reflected calculation gives `H_dD`.  The adjacent
`AH_1` row uses the last `d-1` left-rail fillers and the next maximal cell
carrying `f_0`; internal sweep rows are the same shifted calculation.

Thus the bridge has **zero native lower-q1 address deficit**.  This is
strictly stronger than abstract distinctness of its Johnson intersections
and is not supplied by the protected-factor theorem.

### 2.2 Comparison with the split-core pivot's four deficits

The literal split-core pivot has four possible strict containments between
its native shared cell and its Johnson intersection.  Their missing sets
are

\[
 C\cup X_L,qquad X_R-\{x_R\},qquad
 X_L-\{x_L\},qquad C\cup X_R.                          \tag{2.7}
\]

Equations (2.5)--(2.6) show that the double crossrail has no analogue of
these four debts.  Algebraically, its endpoint-enriched rail letters place
the whole common base `K+za_1` or `K+za_3` at both ends of each rail, so
the two chord intersections and their adjacent sweep intersections are
already native source cells.

This is a positive design comparison, not a literal repair theorem.  The
split-core packet additionally supplies a monotone old/new insertion,
task cell, two compiler rays, and all-width old-deck transport.  The
double crossrail supplies neither that insertion relation nor a transport
of its background compiler.  No label substitution has been proved which
replaces the four split-core rows by (2.6) while retaining those other
properties.  Accordingly the bridge demonstrates that four native deficits
are avoidable in a different packet geometry; it does not discharge them
inside the split-core packet.

## 3. The twelve facets and the missing common core

The sixteen canonical upper targets are, with the common core displayed,

\[
 K\cup A\cup F,
 \qquad
 A\in\{za_0,za_1,za_2,za_3,
        a_0a_1,a_1a_2,a_2a_3,a_3a_0\},                 \tag{3.1}
\]

and

\[
 K\cup R\cup F^\circ\cup\{b\},
 \quad R\in\{za_0a_2,za_1a_3,a_0a_1a_2,a_0a_2a_3\},
 \quad b\in\{f_0,f_{d+1}\}.                           \tag{3.2}
\]

The original statement omitted `K` in (3.1)--(3.2).  That omission is
harmless only in the replay specialization `K=emptyset`; for general
`|K|=r-d-3` it gives targets of the wrong rank.  The theorem formulas have
now been corrected.

The bridge supplies `K+za_1+F`, `K+za_3+F`, and the two values
`K+za_1a_3+F^circ+b`.  For each of the six other high values, delete
`f_0` and `f_(d+1)` to obtain its two rank-`r` facets.  For each of the six
other boundary values, delete `f_1` and `f_2`.  These are twelve Johnson
edges.

Their twenty-four owners are distinct: active signatures separate the six
high and six boundary targets, and the two deleted-filler choices separate
the facets of one target.  They are disjoint from the bridge because the
only bridge active pairs are `za_1,za_3` and its only boundary triple is
`za_1a_3`, precisely the excluded targets.

Their lower colours are also distinct.  A high auxiliary intersection is

\[
                       K\cup A\cup F^\circ,             \tag{3.3}
\]

where `A` is one of the six unused active pairs.  A boundary auxiliary
intersection is

\[
       K\cup R\cup(F^\circ-\{f_1,f_2\})\cup\{b\},      \tag{3.4}
\]

with one of the three unused triples and one boundary label.  Active
cardinality/signature and then `b` separate (3.3)--(3.4), and (1.4) shows
that neither class meets a bridge lower colour.

The bridge is one path component and the twelve auxiliary edges are twelve
more components.  Adding their vertices and edges gives exactly (0.3).
Each isolated edge has no wholly internal short run; its residence is a
clipped-boundary assertion which must be continued or protected after a
global embedding.

## 4. Exact phase-endpoint correction

For the authenticated endpoint source

\[
 \{z,b\},\{z,c\},\{z,c,f_d\},\ldots,
 \{z,c,f_2\},\{z,c,f_1\},                              \tag{4.1}
\]

the overlooked intervals are

\[
 I^S_j=[1,d-j+1],\qquad I^P_j=[d-j+2,d+1].             \tag{4.2}
\]

They are adjacent and disjoint, and their values are

\[
 \operatorname {OR}(I^S_j)=\{z,c\}\cup F[j+1,d],
 \qquad
 \operatorname {OR}(I^P_j)=\{z,c\}\cup F[1,j].       \tag{4.3}
\]

Thus the first symmetry seam has the complete old-phase bank
`P_0(j) <-> S_1(j+1)`, while its new phase is not a cross bank.  Under the
`a_1 <-> a_3` symmetry, the second seam has the complete new-phase bank
`P_1(j) <-> S_0(j+1)`, while its old phase is not a cross bank.

This correction is exact for the authenticated factors `2<=d<=12`.  It
does not put both banks into one authenticated endpoint phase.  The bridge
of Sections 1--2 is a separate dimension-uniform construction which does
put both banks in one source state.

## 5. Incidence subdivision and the Catalan bank

Let `J` be the thirteen-component Johnson forest.  Subdivide each of its
`e=2d+15` edges through its distinct rank-`r-1` intersection.  The resulting
incidence forest `P` has

\[
 |E(P)|=2e=4d+30,qquad
 |V_{owner}(P)|=2d+28,qquad
 |V_{lower}(P)|=2d+15.                                  \tag{5.1}
\]

Properly alternate every component:

\[
                         P=P_0\mathbin{\dot\cup}P_1.    \tag{5.2}
\]

Each colour class has exactly one incidence from every Johnson edge, hence

\[
                         |P_0|=|P_1|=2d+15.             \tag{5.3}
\]

Both are matchings on the protected vertices.  If a perfect matching `M_0`
contains `P_0`, the rooted links of `P_1` form thirteen vertex-disjoint
directed paths: one of length `2d+3` and twelve of length one.  This is a
graphic-independent protected seed.

Its upper-label multiplicities are exactly (0.2), plus twelve singleton
labels.  A canonical upper-exact protected split may use

\[
\begin{aligned}
 A_0={}&\text{all twelve auxiliary incidences, both chord incidences,}\\
       &\text{one of the `d` copies of `M_+`, and one of the `d+1`
         copies of `M_-`},                              \tag{5.4}\\
 A_1={}&P_1-A_0,qquad |A_0|=16,qquad |A_1|=2d-1.     \tag{5.5}
\end{aligned}
\]

This split maximizes the number of protected edges in `Q_0`.  For an
arbitrary protected Catalan decomposition, put

\[
       A_0=P_1\cap Q_0,qquad A_1=P_1\cap Q_1.          \tag{5.5a}
\]

Then `|A_0|<=16` and `|A_1|>=2d-1`; neither the twelve auxiliary edges nor
the two chords are individually forced into `A_0`, because their upper
colour could be represented by an unprotected occurrence.  The exact
protected assignment, in either the canonical or general split, is

\[
                    P_0\subseteq M_0,qquad
                    A_0\subseteq Q_0,qquad
                    A_1\subseteq Q_1.                  \tag{5.6}
\]

Locally, the full links of `P_1` form a forest, so every `A_1` edge joins
two different components of the restricted `A_0` forest.  Globally, a
completion of `Q_0` could connect those endpoints by another route and turn
an `A_1` edge into a loop after contraction.  Hence the correct extension
condition is that `lambda(Q_0 union A_1)` remain a forest, followed by a
completion of `Q_1` to the required Catalan connector tree/path.

The owner/lower protected-factor theorem may be applied to this incidence
bank only under

\[
                              4d+30\le m-2              \tag{5.7}
\]

for one copy, or `H(4d+30)<=m-2` for `H` copies.  It supplies some spanning
two-factor containing `P`; it does not supply (5.6).

The protected upper/root-tail Hall projection can extend the sixteen
prescribed tickets of `A_0` whenever `16<=m`.  (The other `2d-1`
protected incidences belong to the connector bank `A_1`, not to that
upper-independent Hall instance.)  It still does not enforce opposite-head
injectivity, avoidance of the `A_1` ports by the rest of `Q_0`, graphic
compatibility with `A_1`, or the final port Hamilton path.

Finally, the one maximal-envelope source in the theorem realizes the bridge
only.  The twelve auxiliary edges were added at the owner level and have no
proved simultaneous source/cap embedding with that bridge.  Likewise their
clipped residence flags need continuation.  These are the exact physical
rows still separating the local sixteen-support forest from a protected
Catalan carrier.

### 5.1 Exact embedding/component-reduction verdict

There are two different completion statements, and they must not be
identified.

1. Under (5.7), the small protected-factor theorem **unconditionally**
   embeds the incidence forest in some spanning owner/lower-`q1`
   two-factor.  This is only an abstract incidence embedding.  It controls
   neither the number of completed components nor the literal source
   addresses.
2. The protected Catalan path theorem gives an exact **conditional** route
   to one alternating Hamilton path: choose `M_0` containing `P_0`, extend
   `A_0` to an upper-exact rooted Catalan forest `Q_0` while leaving every
   `A_1` port exposed, and complete `A_1` to a directed Hamilton path
   `Q_1` on the contracted `Q_0` components.  The C8 bank has no local
   matching or graphic obstruction to this formulation—its protected
   links are thirteen disjoint paths—but the required common extension and
   port Hamilton path are not proved.

In particular, “thirteen protected components” does not mean that twelve
arbitrary seams finish the construction.  The connector problem lives on
the `C=Cat_m` components of the completed `Q_0`, and all `2d-1` protected
edges of `A_1` must remain genuine intercomponent port arcs there.

At the owner-graph level the long bridge can be forced to be the initial
segment by making its first rooted head the unique unused `Q`-head and by
guarding the first continuation at its exported right port.  This is only
the root condition in the protected Catalan path theorem.  It does not put
the displayed source `Q` at the beginning of the ambient source word.  If
that literal source-prefix placement is supplied separately, appending
later source letters leaves all bridge owner windows and its native
lower-`q1` cells unchanged.

Residence is the sharp physical obstruction to a bare component reduction.
The thirteen paths have twenty-six local ends; one global Hamilton path has
only two ends.  Thus twenty-four local ends become internal and need
explicit continuation/collars (or a rethread) preserving every short
coordinate run.  The twelve isolated edges are not self-protecting after
this operation.

The Lane-A split-core correction is consistent with this conclusion.  Its
four rows in equation (4.15) are native source-address deficits even though
the abstract lower incidences exist, so fixed-`H` planting does not repair
them.  The present bridge avoids those four deficits by the exact identity
(2.6), but only in its different explicit source geometry.  No theorem
transports that advantage to the split-core packet, and no source geometry
has yet been supplied for the twelve auxiliary C8 edges.

## 6. Correct scope

The theorem proves a strong local bank:

\[
 \boxed{\text{one resident double crossrail}+12\text{ facet edges}
        +16\text{ upper tickets}+\text{exact bank split (5.6)}.}
\]

It does not prove:

1. a perfect `M_0` and rooted Catalan forest `Q_0` satisfying all forced
   heads and the `A_1` graphic constraint;
2. completion of `Q_1` to a spanning Catalan connector path;
3. one literal source/common cap containing the twelve auxiliary edges;
4. exterior residence after the thirteen components are attached; or
5. transport of an arbitrary incumbent background compiler matching.

## 7. Independent replay

The original bridge replay (whose stored script specializes to `K=empty`)
was rerun successfully.  A second audit adjoins a nonempty two-coordinate
core `K` and checks, for every `2<=d<=64`, owner ranks and adjacency,
`D^dQ=T`, all shared native lower cells (2.5), the two rail banks, and the
residence ledger:

```text
scratch/audit_threadD_c8_double_crossrail_native_q1_20260801.py
  SHA-256 a67c775cbaca2b88dace4a1d23fa96ff63289bd4208185e062cd841d18b1ecf7
scratch/threadD_c8_double_crossrail_native_q1_20260801.audit.json
  SHA-256 29523e5ca3b8b0e859fa6fa555edfddea6900330a8415941c1a11c337f3a67ea
  payload  a72ffde0429dcb446ed6797bd655ba703aa08484a19c98a4ed1fa0a1f1a97c10
```

All `2d+3` native lower rows are exact in every replayed dimension.  The
finite replay supports the formula audit; the case table (2.6) is the
dimension-uniform proof.
