# A support-minimal strict five-edge packet and the exact motif-descent gate

Date: 2026-07-31  
Status: exact exchange/graphic theorem and exact finite replay at structural
parameters `n=3,4,5`; no all-parameter packet-supply theorem

## 0. Verdict

The corrected recursive state is

\[
                    (F,G,Q,M^-,M^+,\mathcal R).       \tag{0.1}
\]

Here `F` is the **structural** Catalan forest which defines the strict
occurrence catalogues, `G` is an independent guarded Catalan filler on the
isolated `c`-rail, `Q` is the common puncture bank, `M^-` and `M^+` are the
two direct SDRs, and \(\mathcal R\) is the rooted/graphic support.  The
independent filler theorem makes `c+G` a direct summand.  Therefore a
`Q`/SDR packet cannot alter a forbidden motif in `c+G`; that rail must be
supplied clean.  The packet below acts only on the complementary
three-sector support determined by `F`.

There is a canonical bounded move when one edge `e in Q` is exchanged for
one edge `f notin Q` and both SDR changes have a direct length-two
alternating path.  The move replaces exactly five selected physical edges
by five:

* three central/seam edges forced by `e -> f`;
* one upper direct representative; and
* one lower direct representative.

This support five is sharp for a one-element `Q` exchange.  Palette
preservation is automatic.  Physical legality is exactly one degree test
and one graphic-basis test: after deleting the five old edges, the five new
edges must be independent in the component quotient, equivalently the
corresponding fundamental-cycle minor is nonsingular.

The forbidden minimum-three body motif on a directed three-edge path is

\[
                         b_{i-1}=a_{i+1}.             \tag{0.2}
\]

The five-edge packet gives a conditional descent theorem: if its exact
graphic test passes and its local replay deletes the chosen motif without
creating as many new ones, it is a legal strict descent.  This is not a
tautological empty condition: on the frozen chained constructions the
complete census gives

\[
\begin{array}{c|r|r|r|r|r|r}
n&\text{direct }Q\text{-pairs}&\text{physical-safe}&
 \text{root/profile-safe}&\text{improving}&
 \text{best change}&\text{pure eliminators}\\ \hline
3&2&1&1&1&-2&0\\
4&9&9&8&2&-1&0\\
5&20&9&9&2&-1&1.
\end{array}                                           \tag{0.3}
\]

At `n=5`, the packet `e=188 -> f=67` eliminates one structural forbidden
motif and creates none.  The `c`-rail motif set is unchanged in every row,
as required by the independent-filler theorem.

What does **not** follow is a dimension-uniform bounded packet supply.
Common bases of two partition matroids can be separated by an alternating
cycle of arbitrary length, and even a fixed one-element puncture change can
force an SDR alternating path of arbitrary length.  Thus boundedness needs
a Boolean occurrence theorem; it is not a consequence of matroid exchange.

## 1. The exact coupled state

Let `F` be an oriented Catalan linear forest on the rank-`n` vertices of a
`2n`-set `Omega`.  Write an edge as

\[
 q=(\ell_q,u_q,t_q,h_q),\qquad
 \ell_q=t_q\cap h_q,\quad u_q=t_q\cup h_q.            \tag{1.1}
\]

The tail and head maps are injective because every component of `F` is
oriented as a path.  Let `O^-_F` and `O^+_F` be the strict upper-lift and
lower-projection occurrence catalogues.  For an upper occurrence `alpha`,
write `o^-(alpha)` for its outer rank-`n+2` colour and `m^-(alpha)` for its
middle rank-`n` colour.  Dually use `o^+(beta)` and `m^+(beta)` below.

The exact direct palette equations are

\[
 \sum_{\alpha:o^-(\alpha)=W}y^-_\alpha=1,             \tag{1.2}
\]

\[
 \sum_{\alpha:m^-(\alpha)=X}y^-_\alpha
   =1-\sum_{q:t_q=X}x_q,                              \tag{1.3}
\]

and

\[
 \sum_{\beta:o^+(\beta)=A}y^+_\beta=1,              \tag{1.4}
\]

\[
 \sum_{\beta:m^+(\beta)=X}y^+_\beta
   =1-\sum_{q:h_q=X}x_q.                              \tag{1.5}
\]

Together with \(\sum_qx_q=C\), integral solutions of (1.2)--(1.5) are
exactly a common bank `Q={q:x_q=1}` and its two direct SDRs.  Equivalently,
`Q` is a common basis of the two pulled-back dual transversal matroids.

Adjoin coordinates `c,z`.  The structural `Q`-block contributes

\[
\begin{array}{ll}
 q\in Q:&
 s_q^- =\{u_q,z+t_q\},\qquad
 s_q^+ =\{z+h_q,c+z+\ell_q\},\\[1mm]
 q\notin Q:&
 d_q=\{z+t_q,z+h_q\}.
\end{array}                                           \tag{1.6}
\]

The two selected SDR occurrences contribute their lifted physical Johnson
edges.  The fixed rail `c+G` is disjoint from every edge in (1.6) and from
both side sectors.  Its palettes and topology therefore direct-sum with
the structural support.  In particular, `F` and `G` need not agree.

The remaining exact rows are physical degree caps and graphic
independence.  A no-empty chosen side may be encoded by adjoining a root
to one anchor in every side component; the augmented support must be a
graphic basis.  This rooted representation changes no argument below.

## 2. General exchange decomposition

Let `(Q,M^-,M^+)` and `(Q',M'^-,M'^+)` be two integral solutions of
(1.2)--(1.5).  Put

\[
 A=Q\setminus Q',\qquad B=Q'\setminus Q,qquad |A|=|B|=s. \tag{2.1}
\]

### Theorem 2.1 (two-path/cycle decomposition)

On the upper shore, \(M^-\mathbin\triangle M'^-\) is the disjoint union of alternating
cycles and `s` alternating paths whose terminal endpoints are the changed
tail punctures

\[
       T(A)\sqcup T(B).
\]

On the lower shore the analogous paths have endpoints

\[
       H(A)\sqcup H(B).
\]

The structural physical change has, before cancellations, at least `5s`
old and `5s` new selected edges.  Equality holds exactly when both shores
use `s` length-two alternating paths and no alternating cycle, and every
structural edge in (1.6) is distinct.

#### Proof

Every outer colour has degree two in the union of the old and new
matchings unless its representative is unchanged, in which case it has
degree zero after cancellation.  A middle colour unchanged between the two
survivor banks also has degree zero or two.  Each old-surviving/new-punctured
tail has one old edge and no new edge, while each old-punctured/new-surviving
tail has one new edge and no old edge.  Thus the nontrivial components are
alternating cycles and paths with exactly those endpoints.  Tail
injectivity gives `s` paths.  The head proof is identical.

For every `e in A`, the old structural state has two seams; for every
`f in B`, it has one central edge.  Hence the old `Q`-block contains `3s`
edges which disappear, and the new block contains `3s` which appear.
Each shore path contains at least one old and one new matching edge, adding
at least `s+s` on each half.  This gives `5s`.  Equality is precisely the
stated length-two case.

This count is physical, not merely occurrence-labelled.  On either shore
the physical Johnson edge determines its incidence pair: its intersection
and union recover the middle and outer colours.  A changed-puncture path
has distinct old and new middle endpoints because the child tail/head maps
are injective.  Hence at least one physical representative really changes
on every path, even if the strict catalogue has parallel `(q,x)` labels for
one incidence.  Different paths use disjoint matching rows.  Finally, the
representative edges lie internally in sectors `0` or `cz`, whereas the
three `Q`-block edges lie in or cross the `z` sector, so no representative
change cancels a structural one. `square`

This theorem is the correct meaning of an alternating packet when `Q`
changes.  Matching cycles alone describe only the fixed-`Q` fibre; the
changed punctures export alternating **paths**, which close only after the
central/seam block is included.

## 3. The support-minimal unit packet

Fix `e in Q` and `f notin Q`.  In the current upper SDR, let
`alpha_f` be the unique representative with middle colour `t_f`, and put

\[
                         W=o^-(\alpha_f).             \tag{3.1}
\]

In the current lower SDR, let `beta_f` be the unique representative with
middle colour `h_f`, and put

\[
                         A=o^+(\beta_f).              \tag{3.2}
\]

Call `(e,f)` **directly redirectable** when

\[
          (t_e,W)\in O^-_F,qquad (A,h_e)\in O^+_F.  \tag{3.3}
\]

Then replace

\[
 Q'=Q-e+f,                                             \tag{3.4}
\]

\[
 M'^-=M^- -\alpha_f +(t_e,W),\qquad
 M'^+=M^+ -\beta_f +(A,h_e).                          \tag{3.5}
\]

Let `phi^-` and `phi^+` denote the physical Johnson-edge lifts of the two
occurrence types.  The five old physical edges are

\[
 \mathcal A(e,f)=
 \{\phi^-(\alpha_f),\phi^+(\beta_f),s_e^-,s_e^+,d_f\}, \tag{3.6}
\]

and the five new edges are

\[
 \mathcal B(e,f)=
 \{\phi^-(t_e,W),\phi^+(A,h_e),d_e,s_f^-,s_f^+\}.    \tag{3.7}
\]

### Theorem 3.1 (strict five-edge packet)

Assume the ten edges in (3.6)--(3.7) have the declared old/new status.
Then:

1. (3.4)--(3.5) preserve every upper and lower palette exactly, and `Q'`
   is a common direct basis;
2. let `R` be the current physical forest and
   \(R_0=R-\mathcal A(e,f)\).  The terminal support

   \[
                   R'=R_0+\mathcal B(e,f)             \tag{3.8}
   \]

   is a linear forest if and only if its degree caps hold and the image of
   \(\mathcal B(e,f)\) is loopless and graphic-independent after the
   components of `R_0` are contracted; and
3. if a selected side is represented as a rooted tree, its rooted condition
   survives exactly when every terminal side component contains a new
   anchor.  Equivalently one may choose one new root edge per component.

The packet has minimum possible physical support among all nontrivial
one-element `Q` exchanges in this strict sector model: five old and five
new physical edges.  Fixed-`Q` parallel occurrence relabellings may be
physically invisible; they are outside this changed-puncture assertion.

#### Proof

The upper change removes `t_f` from the survivor bank and inserts `t_e`.
Equation (3.5) changes precisely those two middle rows and keeps the same
outer row `W`; hence (1.2)--(1.3) remain exact.  The lower argument is
identical.  Thus the two SDRs themselves witness that `Q'` is common.

Deleting edges from `R` leaves a forest.  Adding an edge creates a cycle
exactly when it is a loop after contraction, or when the accumulated
contracted edges close a cycle.  Therefore graphic independence of the
five new images is equivalent to acyclicity of (3.8); the degree row is
separate and exact.  The rooted assertion is the one-root-per-component
identity.

The support lower bound is Theorem 2.1 with `s=1`, and (3.6)--(3.7) attain
it. `square`

### Corollary 3.2 (fundamental-cycle certificate)

Adjoin root edges so the current support is a tree `T`, and suppose those
root edges remain legal and selected after the packet.  For
\(a\in\mathcal A(e,f)\) and \(b\in\mathcal B(e,f)\), let \(C_T(b)\) be the
fundamental cycle of `b`.  Then the graphic row in Theorem 3.1 is
equivalent to

\[
 \det\bigl(\mathbf 1[a\in C_T(b)]\bigr)_
       {a\in\mathcal A(e,f),\ b\in\mathcal B(e,f)}=1
                         \quad\text{over }\mathbf F_2. \tag{3.9}
\]

This is a verification theorem, not a packet-supply theorem.  If the root
choice itself changes, include the deleted and added root edges as extra
rows and columns of the same fundamental-cycle minor.  If only unrooted
physical acyclicity is required, use the component-contraction criterion of
Theorem 3.1 instead.

## 4. Exact residence descent

For a four-vertex subpath `(v_0,v_1,v_2,v_3)` define

\[
 \mu(v_0,v_1,v_2,v_3)=
 (v_1\cap v_2)\setminus(v_0\cup v_3).                \tag{4.1}
\]

Because lower edge colours are injective, an internal singleton positive
run is impossible.  Moreover `mu` is nonempty exactly when it is a
singleton `{x}` and the trace of `x` is `0110`.  Orienting the path gives

\[
                  x=b(e_0)=a(e_2),                   \tag{4.2}
\]

so (4.1) is precisely the forbidden motif.  It is invariant under path
reversal.

### Theorem 4.1 (conditional unit descent)

Let `(e,f)` satisfy Theorem 3.1.  If literal replay of (3.8) gives

\[
          |\mathsf{Bad}(R')|<|\mathsf{Bad}(R)|,       \tag{4.3}
\]

then (3.4)--(3.8) is an integral strict-recursion descent preserving the
common bank, both exact palettes, degree caps, acyclicity and rooted
support.  If a specified motif belongs to
`Bad(R)-Bad(R')`, that motif is eliminated.  A stronger pure eliminator has

\[
          \mathsf{Bad}(R')\subsetneq\mathsf{Bad}(R). \tag{4.4}
\]

No motif in the independent rail `c+G` can lie in the displayed set
difference.

#### Proof

All structural assertions are Theorem 3.1.  Equation (4.1) is an exact
local characterization of body residence, so (4.3)--(4.4) say exactly what
is claimed.  The edge sets (3.6)--(3.7) are disjoint from `c+G`; hence that
rail is unchanged. `square`

The replay condition is local: only three-edge windows meeting one of the
ten packet edges can change.  It can therefore be exported as a bounded
boundary signature.  What remains occurrence-conditional is the existence
of a directly redirectable `(e,f)` whose graphic minor and motif sign are
favourable.

## 5. What remains integral, and what does not

Three separate integral facts survive.

1. Selecting `Q` alone is ordinary intersection of the two pulled-back
   transversal matroids.
2. For fixed `Q`, each SDR is a bipartite perfect-matching problem; its
   incidence matrix is totally unimodular.
3. For a prescribed packet, rooted support is one graphic-basis test,
   equivalently (3.9).

Their joint product is not ordinary matroid intersection.  The same `x_q`
columns control two changing terminal banks and three structural physical
edges, while the representative columns enter overlapping degree and
graphic rows.  Thus the full state is a common-basis/matching/graphic
correlation, not a directed network matrix.  The broader literal ordered-
diamond system already contains the determinant-two minor

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},  \tag{5.1}
\]

so no generic TU theorem follows.  This does not claim that every strict
recursive subcatalogue contains (5.1); it says the three conditional
integrality theorems cannot simply be concatenated into a global TU proof.

## 6. Sharp abstract boundedness obstructions

The five-edge theorem is conditional on a short common-basis exchange and
two direct redirections.  Neither is a matroid axiom.

### Proposition 6.1 (unbounded common-basis exchange)

For every `s>=2`, two partition matroids have two common bases whose
symmetric difference has order `2s`, and no intermediate common basis.

#### Proof

Take the edge set of the cycle `C_(2s)`.  The two endpoint partition
matroids enforce degree at most one at the two bipartition shores.  Their
common bases are the perfect matchings of the cycle, namely its two
alternating matchings.  They differ in all `s` selected edges. `square`

### Proposition 6.2 (a one-puncture exchange can force a long SDR path)

For every `s`, there is a bipartite occurrence graph with old right bank
`{r_1,...,r_s}` and new right bank `{r_0,...,r_(s-1)}` in which both banks
have a unique saturating matching, but their symmetric difference is one
alternating path of length `2s`.

#### Proof

Use left vertices `u_1,...,u_s` and only the edges

\[
                    u_i r_i,\qquad u_i r_{i-1}.       \tag{6.1}
\]

The old matching is `{u_i r_i}` and the new one is `{u_i r_(i-1)}`.  Their
union is

\[
 r_s-u_s-r_{s-1}-\cdots-r_1-u_1-r_0.                \tag{6.2}
\]

Both are forced. `square`

These are abstract occurrence/matroid obstructions, not Boolean
counterexamples.  They prove that an all-`n` bounded packet theorem must
use the strict Boolean catalogue, a protected occurrence reserve, or a
bounded alternating-corridor hypothesis.

## 7. Exact `n=3,4,5` replay

The standard-library audit

```text
scratch/audit_threadD_catalan_strict_five_edge_packet_n3_n5_20260731.py
```

authenticates

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
```

and exhausts every directly redirectable one-element exchange.  The first
three census columns in (0.3) count **ordered Q-pairs / physical packets**,
not occurrence-labelled realizations: parallel `(q,x)` labels with the same
middle/outer incidence induce the same physical redirect and are collapsed.
This is narrower than an audit allowing longer alternating representative
paths, whose labelled and physical counts need not agree.  The script
reconstructs both occurrence catalogues, all four sectors, both palettes,
the full physical forest, anchor histograms and every forbidden motif.
For every candidate it replays (3.6)--(3.8) rather than trusting a score.

The exact counts are (0.3).  The base motif totals are `17,44,144`; they
split into immutable copied-rail totals `5,17,44` and structural totals
`12,27,100`.  Every packet leaves the copied-rail motif set exactly fixed.
All five improving packets act on the structural part.

The cleanest row is the `n=5` exchange

```text
e=188 in Q  ->  f=67 outside Q.
```

It removes the single displayed structural motif

```text
bit 0x100 on 0xe62,0xf42,0xf0a,0xe8a
```

and creates none.  Both side anchor histograms are unchanged.  This is an
explicit integral strict packet, not a claim that every motif has one.

The audit writes

```text
scratch/threadD_catalan_strict_five_edge_packet_n3_n5_20260731.audit.json
```

with canonical payload SHA recorded inside.

## 8. Exact remaining induction lemma

The smallest reusable positive statement still missing is:

> For every accepted structural state `F` with a clean independent filler
> `G`, and every structural forbidden motif, either a support-minimal packet
> of Theorem 3.1 gives descent, or a uniformly bounded collection of such
> paths/cycles forms a compound packet with zero palette flux, a nonsingular
> rooted graphic exchange minor, and strictly negative motif flux; the
> terminal tuple again exports the same occurrence reserve.

The first alternative is nonempty at `n=3,4,5`.  Propositions 6.1--6.2 show
why it cannot be deduced from abstract matroid exchange.  Proving it for the
Boolean direct catalogues, or proving a bounded regenerative compound
substitute, is the precise strict-recursion gate.
