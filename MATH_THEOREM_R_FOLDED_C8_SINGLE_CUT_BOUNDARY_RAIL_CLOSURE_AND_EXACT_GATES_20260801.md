# A single boundary rail can absorb the folded-C8 host residence defect, but only with an occurrence-level cut certificate

Date: 2026-08-01  
Lane: R, quotient-folded C8 physical host/common-cap closure  
Status: exact conditional all-`d` theorem and sharp missing-data statement.  No
all-`k` construction is claimed.

## 0. Result

The quotient-folded C8 has two nested source rays in either phase,

\[
\begin{aligned}
 {\mathcal P}_0&=\{K+za_3+F[1,j]:1\le j<d\},&
 {\mathcal S}_0&=\{K+za_1+F[j,d]:1<j\le d\},\\
 {\mathcal P}_1&=\{K+za_1+F[1,j]:1\le j<d\},&
 {\mathcal S}_1&=\{K+za_3+F[j,d]:1<j\le d\}.
\end{aligned}                                                   \tag{0.1}
\]

Its abstract terminal birail Hall deficiency is zero.  The physical two-host
module also gives a literal diagonal matching on all `2d-2` ray targets.  The
remaining question is whether the two nonnative hosts can be planted at one
global opening without losing owner rank, the two `q1` palettes, residence,
or the ambient common-`Q` matching.

This note proves the exact conditional answer.

* A rank-`r` host trail of length `d` is a Johnson path in a
  `(d-1)`-subset link.  It is locally residence-safe at one global opening
  if and only if no coordinate has trace `0 1^+ 0` on the trail.  Prefix,
  suffix, and prefix-plus-suffix traces are allowed because their positive
  runs are clipped at the two global word boundaries.
* In the tight case in which `2d-2` events lie on once-changing coordinates,
  the unique repeated coordinate must be deleted and later reinserted.  An insertion
  followed by deletion is a short internal positive run and is impossible.
  This proves precisely what a single cyclic cut can and cannot absorb.
* Two independent full-window minimal hosts at addresses separated by `d`
  have disjoint forced transition arcs.  One cut cannot legalize both.  A
  positive construction must make them genuinely coupled/clipped boundary
  occurrences, not merely reroot the two internal hosts.
* Once an occurrence-labelled boundary rail satisfies that trace condition,
  the exact owner and palette tests are finite link-path identities.  The
  folded ray cells remain a free transversal bank

  \[
                         U_{2d-2,2d-2}.                 \tag{0.2}
  \]

  The aligned opening has exactly one lower-`q1` and one upper-`q1`
  casualty; the upper-safe opening has exactly one lower casualty.
* In one matching-closed cap state, the necessary-and-sufficient ambient
  completion condition is the ordinary residual Hall/rank cut after fixing
  the ray diagonal and any palette sidecars.
* The address equality `p_R-p_L=d` and the host rank alone do **not** prove
  graded/context closure.  Nevertheless, an exact H100 replay on the
  authenticated family (`2<=d<=12`) finds a unique common cut which cancels
  the whole internal `6d+16` residue.  One common left screen then equalizes
  both boundary signatures, giving full fixed-exterior equality of the
  unlabelled width-graded OR deck.  Addressed occurrence equality, owner
  legality of that screen and legality of the clipped hosts remain separate.

Thus the single-cut idea is mathematically viable, but its remaining input is
an explicit occurrence-labelled boundary rail, not another scalar Hall
inequality.

## 1. Owner-link normal form

Let `X` be a fixed set of size

\[
                              |X|=r-d+1.                \tag{1.1}
\]

Let

\[
 O_i=X\mathbin{\dot\cup}S_i\qquad(0\le i\le d),        \tag{1.2}
\]

where `S_i` is a `(d-1)`-subset disjoint from `X`.

### Lemma 1.1 (owner and palette normal form)

The sequence `O_0,...,O_d` is a simple rank-`r` Johnson path if and only if
the `S_i` are distinct and

\[
                         |S_{i-1}\triangle S_i|=2
                         \qquad(1\le i\le d).           \tag{1.3}
\]

For its `i`th edge the lower and upper `q1` colours are respectively

\[
 \ell_i=X\cup(S_{i-1}\cap S_i),\qquad
 u_i=X\cup(S_{i-1}\cup S_i).                           \tag{1.4}
\]

#### Proof

Equation (1.1) and `|S_i|=d-1` give `|O_i|=r`.  Two distinct rank-`r`
sets are Johnson adjacent exactly when their symmetric difference has size
two.  The common summand `X` cancels from the symmetric difference, proving
(1.3).  Intersection and union give (1.4).  \(\square\)

This is the exact meaning of the proposed `(d-1)`-subset link.  Merely
knowing that `d+1` owner windows contain `X` does not imply (1.3), simplicity,
or either palette identity.

## 2. What the global cut absorbs

For a coordinate `x` outside `X`, write its trace on the link path as

\[
                       \tau_x=(1_{x\in S_0},\ldots,
                                  1_{x\in S_d}).        \tag{2.1}
\]

The two ends of this displayed path are placed at the two ends of the final
linear owner word.  Hence a positive run meeting index `0` or `d` is a
clipped boundary run.  A positive run strictly between them is internal.

### Theorem 2.1 (exact one-cut residence criterion)

The boundary link path creates no internal positive run of length at most
`d` if and only if, for every `x`, the support of `tau_x` is one of

\[
 \varnothing,\quad[0,d],\quad[0,a],\quad[b,d],
 \quad[0,a]\cup[b,d]                                   \tag{2.2}
\]

for some `0<=a<b<=d`.  Equivalently, no `tau_x` contains a pattern

\[
                              0\,1^+\,0.                \tag{2.3}
\]

If the exterior continuation certifies the inherited boundary run ages,
then (2.2) is also sufficient for the complete depth-`d` residence test.

#### Proof

The trail has only `d+1` owner positions.  Any positive run wholly inside
it has length at most `d-1`, hence violates a `d+1` residence floor.  Such a
run exists exactly when the trace contains (2.3).  If (2.3) is absent, every
positive component meets the left or right endpoint; the possible supports
are precisely (2.2).  They are clipped locally.  The last assertion only
adds the stated exterior-age check, which is necessary because this local
argument does not determine the neighbouring owner bits.  \(\square\)

### Corollary 2.2 (the tight extra transition)

The `d` Johnson edges of (1.3) contain `2d` coordinate-transition events.
At least one coordinate changes at least twice.  Every coordinate changing
exactly twice is locally residence-compatible only when its two changes are
delete-then-reinsert, with trace

\[
                              1^+0^+1^+,                \tag{2.4}
\]

not insert-then-delete with trace `0^+1^+0^+`.  In the tight case in which
exactly `2d-2` transition events belong to coordinates changing once, the
remaining two events belong to one such exceptional coordinate, so (2.4)
is necessary and sufficient for that extra pair.

#### Proof

Every edge deletes one coordinate and inserts one, so there are `2d`
events.  If every coordinate changed at most once, deletion events could
use only coordinates of `S_0` and insertion events only coordinates of
`S_d`, giving at most `|S_0|+|S_d|=2d-2` events, a contradiction.  For a
coordinate changing exactly twice, the two possible nonmonotone traces are
(2.4) and `0^+1^+0^+`; Theorem 2.1 accepts exactly the former.  The final
sentence follows by the stated event count.  \(\square\)

This is the rigorous form of the “`d`th swap” mechanism.  A single cut can
turn one delete/reinsert into two clipped positive runs.  It cannot hide an
insert/delete island, two independent internal islands, or a deficient
exterior boundary age.

### Lemma 2.3 (disjoint endpoints force one neutral relay)

Suppose `S_0=A`, `S_d=B`, where `A,B` are disjoint `(d-1)`-sets.  For
`alpha_i=|S_i cap A|`, let `n_-`, `n_0`, `n_+` count steps on which
`alpha` decreases, stays fixed, or increases.  Then

\[
 n_-+n_0+n_+=d,\qquad n_--n_+=d-1,
\]

and consequently

\[
                         n_0=1,\qquad n_+=0.            \tag{2.5}
\]

Thus exactly `d-1` steps delete one old `A` coordinate and exactly one step
is an outside-to-outside relay.  The outside coordinate deleted at the
neutral step was inserted earlier; in the uncut contiguous rail its first
positive run is therefore a forbidden internal `0 1^+ 0` island.

#### Proof

Each Johnson step changes `alpha` by `-1,0`, or `1`; summing from
`alpha_0=d-1` to `alpha_d=0` gives the two displayed equations.  Eliminating
`n_-` gives `n_0+2n_+=1`, whose unique nonnegative integral solution is
(2.5).  Before the neutral step no outside coordinate can have been deleted,
so the outside coordinate deleted there must have entered on an earlier
decreasing step.  \(\square\)

### Theorem 2.4 (explicit one-cut boundary ear, `d>=3`)

Let `d>=3`, and let

\[
 A=\{a_1,\ldots,a_{d-1}\},\qquad
 B=\{b_1,\ldots,b_{d-1}\}
\]

be disjoint and disjoint from `X`, and let `c` be outside
`X union A union B`.  Define

\[
\begin{aligned}
 S_0&=A,\\
 S_i&=(A\setminus\{a_1,\ldots,a_i\})
       \cup\{c,b_1,\ldots,b_{i-1}\}, &&1\le i<d,\\
 S_d&=B.                                                   \tag{2.6}
\end{aligned}
\]

Then `X union S_0,...,X union S_d` is a simple Johnson path.  Its `d`
lower colours and its `d` upper colours from (1.4) are separately
pairwise distinct.  Every active coordinate is monotone on the rail except
`c`, whose positive run is exactly `S_1,...,S_(d-1)`.  Hence placing one
global cyclic cut anywhere inside that `c`-run turns it into two clipped
boundary fragments and removes the sole rail-internal residence defect.

This conclusion assumes that `c` is absent on the exterior continuation of
the rail until its displayed re-entry and that the exterior run ages of the
one-way `a_i,b_i` labels meet the required floor.  Under those explicit
guards, (2.6) is an all-`d` owner/residence ear; it makes no assertion that
its q1 colours are unused in the ambient factor.

#### Proof

For `1<=i<d`, step `i` removes `a_i`; step `1` adds `c`, and step `i>=2`
adds `b_(i-1)`.  The final step removes `c` and adds `b_(d-1)`.  Thus every
step has symmetric difference two and the displayed sets are distinct.
The lower edge labels successively contain decreasing `A` parts and
increasing `B` parts, with `c` present precisely on the middle edges; the
upper labels have the analogous strict progression.  No two labels on the
same shore coincide.  The trace assertion is immediate from (2.6), and
cutting inside its unique positive arc converts that arc to a prefix plus a
suffix as allowed by (2.2).  \(\square\)

Theorem 2.4 proves that the proposed boundary mechanism exists at the
abstract owner-link level.  What remains is to identify the folded host
endpoints with `A,B,X,c` occurrence by occurrence and pass the ambient
palette and compiler tests below.  The restriction `d>=3` is sharp for this
double-rainbow ear: at `d=2` the residual sets are singletons, so both link
edges have the same lower colour `X`.

### Theorem 2.5 (one cut cannot legalize two independent full hosts)

Let an actual source host at cyclic position `p` belong to all `d+1` owner
windows

\[
              O_{p-d},O_{p-d+1},\ldots,O_p,            \tag{2.7}
\]

and suppose these form a full minimal link as in Section 1.  Among its `d`
insertions, at least one arrival run begins after `O_(p-d)` and ends before
`O_p`: otherwise all `d` arrival runs would still occupy the final residual
set of size `d-1`; if a label is inserted twice, its first arrival run has
already ended and gives the same conclusion.  Hence every full minimal host
has a positive island strictly internal to (2.7).  A global cyclic cut can
clip that island only by cutting one of the transition edges

\[
 \Gamma(p)=\{(O_{j-1},O_j):p-d+1\le j\le p\}.          \tag{2.8}
\]

For aligned host positions `p_R=p_L+d`,

\[
 \Gamma(p_L)=\{p_L-d+1,\ldots,p_L\},\qquad
 \Gamma(p_R)=\{p_L+1,\ldots,p_L+d\}                    \tag{2.9}
\]

in transition-index notation, so the two sets are disjoint.  Therefore one
global cut cannot make **two independent full-window minimal hosts**
residence-safe.

The surviving boundary-rail route must be genuinely coupled or clipped:
at least one endpoint host must be constrained by fewer than all `d+1`
windows, or the two nominal hosts must share one arrival/transition state so
that the independent counting above no longer applies.  Merely moving the
two old full hosts to opposite sides of a cut does not meet this condition.

#### Proof

Each Johnson edge starts one arrival run.  If `d` distinct arrival runs all
survived to the last residual set, that `(d-1)`-set would contain at least
`d` labels.  If an arrival label repeats, its previous run ended strictly
inside the trail.  Thus in all cases an internal positive island exists.
Splitting it into clipped boundary pieces requires the cut to meet one of
its incident trail edges, all of which lie in (2.8).  Equation (2.9) is
immediate from `p_R=p_L+d`; one edge cannot belong to both disjoint sets.
\(\square\)

## 3. The folded two-host ray bank

Put

\[
\begin{array}{ll}
 L_0=K+za_3+f_1,&L_1=K+za_1+f_1,\\
 R_0=K+za_1+f_d,&R_1=K+za_3+f_d,
\end{array}                                                \tag{3.1}
\]

Here `z,a_1,a_3,f_1,...,f_d` are pairwise distinct and lie outside `K`,
as in the folded audit.  Without this standing hypothesis the ray targets
need not be distinct, and neither (3.5) nor the free-matroid claim follows.

and

\[
 X_L=L_0\cup L_1=K+za_1a_3+f_1,
 \qquad
 X_R=R_0\cup R_1=K+za_1a_3+f_d.                         \tag{3.2}
\]

A **typed boundary-rail certificate** is an occurrence-labelled source
collar satisfying all of the following.

1. Its two marked old blocks have full unions `X_L,X_R`; in phase
   `epsilon` their inward halves are `L_epsilon,R_epsilon` in the orders

   \[
       X_L,L_\epsilon,\ldots,R_\epsilon,X_R.            \tag{3.3}
   \]

2. The intervals from `L_epsilon` into the left filler chain are exactly
   `P_epsilon`, and the intervals from the right filler chain into
   `R_epsilon` are exactly `S_epsilon` from (0.1), with all `2d-2`
   occurrences distinct.
3. In their actual order, all changed width-`d+1` owner windows form the
   simple Johnson link path (1.2)--(1.3), and its trace state satisfies
   Theorem 2.1 at the chosen global cut.
4. Every old interval meeting a marked block has its full-block lift, and
   every interval trimming both blocks is declared with its actual endpoints.

The definition is occurrence-level.  In particular, if the native marked
addresses differ by `d`, there are `d-1` source positions strictly between
them.  The abstract word

\[
                    X_L,f_2,\ldots,f_{d-1},X_R          \tag{3.4}
\]

has only `d-2` intermediate positions.  Therefore the address equation
alone leaves one spacer/cut occurrence unspecified.  That occurrence must
either lie outside every ray witness after opening or be OR-transparent in
each witness containing it.  If one common spacer belongs to every ray in
both phases, it must lie in

\[
 \bigcap_{\epsilon=0}^1\ 
 \bigcap_{T\in{\mathcal P}_\epsilon\cup{\mathcal S}_\epsilon}T
                  =K\cup\{z\}.                         \tag{3.5}
\]

Equation (3.5) is a necessary condition, not an existence proof.

### Theorem 3.1 (local owner/common-cap closure)

Every typed boundary-rail certificate has the following properties.

1. Its changed owners are rank `r`, simple and Johnson adjacent.
2. Every old OR interval transports injectively by full-block contraction.
3. The ray bank in phase `epsilon` has transversal matroid

   \[
                         U_{2d-2,2d-2}.                 \tag{3.6}
   \]

4. The pointwise cap can use `X_L` on both left-block positions and `X_R`
   on both right-block positions.
5. A cell trimming both blocks is phase-common, since

   \[
                  L_0\cup R_0=L_1\cup R_1.             \tag{3.7}
   \]

Hence there is no additional cross-host ray target and no local common-cap
Hall defect.

#### Proof

Item 1 is Lemma 1.1 and certificate row 3.  A marked block has the same full
union in both refinements, so contraction gives item 2.  Certificate row 2
gives one different physical interval for each different target in (0.1),
hence a diagonal matching of size `2d-2` and item 3.  Containment in (3.2)
gives item 4.  Equation (3.7), together with the common intermediate rail,
makes every double-trimmed OR phase-independent, proving item 5.  \(\square\)

The theorem is stronger than the scalar antitone calculation: it exhibits
an integral matching.  The antitone theorem independently confirms that the
canonical marginal multisets

\[
               \{0^{d-1},1,\ldots,d-1\}
\]

on both shores have optimum deficiency zero.

## 4. Exact palette ledger

Let `A,B` be the endpoints of the common folded-cycle edge used for the
opening.  Its lost lower colour is

\[
                              c_\downarrow=A\cap B.     \tag{4.1}
\]

On the aligned-base face there is additionally one lost upper support value

\[
 U_*=K\cup\{z,a_0,a_2,f_0,f_1,\ldots,f_d\}.            \tag{4.2}
\]

The upper-safe face loses no upper support value.  These are the exact
pre-host casualties: one lower plus one upper on the aligned face, and one
lower only on the upper-safe face.

Let `E_old` be the multiset of owner edges removed by the boundary rethread,
and let `E_new` be the link edges inserted.  Define

\[
\begin{aligned}
 C_\downarrow&=
  \{P\cap Q:PQ\in E_{old}\}\setminus
  \bigl(B_\downarrow\cup\{P\cap Q:PQ\in E_{new}\}\bigr),\\
 C_\uparrow&=
  \{P\cup Q:PQ\in E_{old}\}\setminus
  \bigl(B_\uparrow\cup\{P\cup Q:PQ\in E_{new}\}\bigr),
                                                               \tag{4.3}
\end{aligned}
\]

where `B_downarrow,B_uparrow` are the unchanged background supports.

### Proposition 4.1 (necessary and sufficient `q1` support test)

The rethread preserves complete lower and upper `q1` support if and only if

\[
                     C_\downarrow=C_\uparrow=\varnothing.      \tag{4.4}
\]

This is a support statement; preservation of rainbow occurrence
multiplicity needs the corresponding occurrence-labelled bijection.  For
the link path, the inserted labels in (4.3) are exactly the sets
`ell_i,u_i` in (1.4).  Thus (4.4) is an explicit finite label test.

If the rethread changes no edge except the common opening edge, (4.4)
reduces to requiring a provider for (4.1), and also for (4.2) on the aligned
face.  In general it is unsound to quote only the one/two canonical
casualties: every additionally removed local edge must be included in
(4.3).

#### Proof

Unchanged edges provide exactly `B_downarrow,B_uparrow`; new edges provide
their intersections and unions.  A formerly provided label is absent after
the move exactly when it belongs to the corresponding set in (4.3).  This
is equivalent to (4.4).  \(\square\)

Condition (4.4) is a support criterion.  If the required lower palette is
bijective, its necessary-and-sufficient replacement is equality of the
complete occurrence counters after the move, with every prescribed lower
colour having multiplicity one.  Support equality alone does not preserve
rainbow multiplicity.

## 5. Exact common-`Q` and background rank condition

Fix one phase `epsilon` and one occurrence-labelled cap/boundary state
`theta`.  Put into a mandatory matching `M_0^theta`:

* the `2d-2` diagonal ray incidences;
* the owner and protected rows of the boundary rail;
* any selected cells repairing (4.3); and
* every frozen ambient incidence.

For every source position `p`, intersect its cap with all targets using it:

\[
 Q_p^\theta=C_p^\theta\cap
       \bigcap_{R:\,p\in J_R} S_R.                    \tag{5.1}
\]

Call `theta` **matching closed** if (5.1) is nonempty, every selected row
reconstructs its target, and every matching in the declared residual graph
can be added without changing these facts.  Let `D_theta` be the unmatched
targets and `G_theta` the graph from them to unused legal physical cells.

### Theorem 5.1 (exact background criterion)

In a matching-closed state `theta`, the boundary-rail packet extends to a
literal common-`Q` compiler if and only if

\[
 |N_{G_\theta}(Y)|\ge |Y|\qquad(Y\subseteq D_\theta).   \tag{5.2}
\]

Equivalently, if the remaining cells are split into packet and background
banks with transversal matroids `M_P^theta,M_B^theta`, then

\[
 r_{M_P^\theta}(Y)+r_{M_B^\theta}(Y)\ge |Y|
                  \qquad(Y\subseteq D_\theta).          \tag{5.3}
\]

After the ray diagonal and palette sidecars are fixed and all packet cells
are thereby consumed, (5.2) is simply Hall on the remaining background
bank.  For a two-phase reusable comparator, there must be compatible states
`theta_0,theta_1` sharing one separator and pointwise cap word, with (5.2)
holding separately in each phase.  Equivalently one may use a single joint
state whose two restrictions have this property.  One may not union the two
phase graphs.

#### Proof

Matching closure says precisely that graph matchings are the physically
legal common-`Q` extensions of `M_0^theta`.  Hall's theorem gives (5.2).
The matroid-union rank theorem gives (5.3).  \(\square\)

This is the requested necessary-and-sufficient background rank condition.
The local ray bank contributes full rank and therefore cannot be the source
of a positive cut.  Any positive cut comes from palette repair, structural
zeros, addressed protected rows, or an incompatible cap state.

## 6. Graded/context residue and the exact cut test

Let an addressed cyclic interval be a triple `(s,t,V)` recording its start,
end, and OR value.  For a cyclic cut `c`, let `Pi_c` retain exactly the
interval occurrences which do not cross `c`; these are the physical
intervals of the opened linear word.  Let `Delta_addr` be the signed
addressed deck difference between the folded source plus opposite host
phase on its two sides, including every protected exterior seam row whose
status is claimed to be preserved.

### Theorem 6.1 (necessary and sufficient cut cancellation)

If the protected occurrence ledger must be preserved literally, the
boundary opening cancels the packet's complete contextual residue if and
only if

\[
                         \Pi_c(\Delta_{addr})=0          \tag{6.1}
\]

on every protected occurrence row.  If only target service, rather than
literal occurrence equality, is required, put every positive casualty of
the nonzero vector in (6.1) into `D_theta` and every released negative
occurrence into the residual cell bank.  Then exact repair is equivalent to
the Hall/rank conditions (5.2)--(5.3) in that same cap state.

#### Proof

Opening at `c` deletes exactly the wrapping cyclic intervals and retains
every nonwrapping interval with its address and value unchanged.  Therefore
the signed physical difference is exactly `Pi_c(Delta_addr)`.  It vanishes
precisely under (6.1).  When occurrences may move, its positive part is
exactly the additional target bank and its negative part exactly the
released cell bank, so Theorem 5.1 gives the second assertion.  \(\square\)

For the canonical aligned folded source and the opposite two-host word, the
known **value/width** projection has `L1=6d+16`, with one positive and one
negative unit at every width `2d+5,...,5d+12`.  This does not determine
`Pi_c(Delta_addr)`: the projection forgot the endpoints.  Consequently

\[
  p_R-p_L=d,\qquad |X_L|=|X_R|=r-d+1                 \tag{6.2}
\]

does not imply (6.1).  An occurrence-endpoint ledger showing that every
uncancelled row wraps the chosen cut, or an explicit background transport,
is indispensable.

### Theorem 6.2 (the canonical common cut cancels the internal graded row)

Let `S_0,S_1` be the canonical aligned folded source words and let `G_0,G_1`
be the two-host ray words.  For every audited `2<=d<=12`, form either

\[
             W_0=S_0G_1,\quad W_1=S_1G_0               \tag{6.3}
\]

or the reverse block order.  Rotate both phase words by the same occurrence
cut.  In the first order the unique zero cut is one letter into `S`; in the
second it is at position `d+3`, the same cyclic location after the ray word.
At this cut,

\[
                   D_{\rm graded}(\rho W_0)
                   =D_{\rm graded}(\rho W_1),          \tag{6.4}
\]

and their ungraded support decks also agree exactly.  Thus the global cut
does cancel the previously surviving internal `6d+16` row on the
authenticated folded family.

Before screening, the complete suffix signatures agree but the prefix
signatures differ in exactly `3d+8` positions.  Prepending either common
screen

\[
                         \{a_1,a_3\}
              \quad\hbox{or}\quad\{z,a_1,a_3\}        \tag{6.5}
\]

preserves (6.4) and makes **both** complete prefix and suffix signatures
equal.  By the standard interval decomposition into internal, left-crossing,
right-crossing and two-sided cells, the screened words therefore have equal
width-graded decks in every common fixed exterior context.  Thus one common
left screen closes the unlabelled width-graded source-language row on the
audited family.
It costs one source position if inserted afresh and zero only if an existing
boundary collar already carries it.

Indeed, an interval in `L W R` is either wholly inside one block, meets `W`
from the left and is determined by a suffix of `L` and a prefix of `W`,
meets it from the right and is determined by a suffix of `W` and a prefix of
`R`, or spans all of `W` and is determined by its full union.  Equality of
the internal graded deck, every length-indexed prefix and suffix union, and
the common word length therefore pairs all four classes in arbitrary fixed
`L,R`.

This does **not** prove `Pi_c(Delta_addr)=0`: equal `(width,value)` counters
may pair different start/end occurrences.  Any protected addressed ledger
must still satisfy (6.1), or enter the occurrence-labelled Hall transport in
Theorem 6.1.  The replay also does not check Johnson owners, palettes,
residence or common-`Q` legality.

This is an exact finite statement for `2<=d<=12`; the displayed uniform
pattern is not promoted here to an unproved all-`d` identity.  Nor does the
audit make the screen or either host owner-legal: it uses the source words
and checks their OR language only.  The owner-link obstruction of Theorem
2.5 and the cap/background conditions remain independent.

The replay is

```text
scratch/audit_r_c8_common_cyclic_cut_graded_recycling_20260801.py
scratch/r_c8_common_cyclic_cut_graded_recycling_20260801.audit.json
```

and was executed on the H100 CPU under a 1 GiB virtual-memory and 240-second
wall cap.  Frozen script/JSON SHA-256 values are respectively
`3a5ebde85b068668eed7a666a37703559d04f47378c0e4c4d31fb7b94eea0988`
and `40a10b8b45fea6bbb16aabd80c5c3e436b1837f84f303e88cd54b6e8452704dd`;
the payload is
`14b35db40037510a074d70d0c745742f4f5830d97f216d53a43ff1b0f9dbb16a`.

## 7. Conditional boundary-rail closure theorem

### Theorem 7.1

Fix `d>=2`.  Suppose a quotient-folded aligned or upper-safe C8 pair admits
one typed boundary-rail certificate such that:

1. its link path obeys Theorem 2.1 with correct exterior run ages;
2. its palette ledger obeys (4.4);
3. its addressed contextual ledger obeys (6.1), or its residue is included
   in the matching state;
4. compatible phase states sharing one separator/cap word obey (5.2)
   separately, or one joint matching-closed state has those restrictions;
   and
5. contraction of the two marked blocks returns the same separator state
   when regeneration is required.

Then the boundary rethread is owner-legal, Johnson, depth-`d` resident,
lower/upper-`q1` complete, exact on every protected OR row, and has a literal
common-`Q` compiler.  Its two ray chains contribute no Hall deficiency.

For the aligned face the mandatory palette bank initially has size two
(`c_downarrow,U_*`); for the upper-safe face it has size one
(`c_downarrow`).  Any further sidecars are exactly the nonempty sets in
(4.3), not an unaccounted asymptotic term.

#### Proof

Owner rank, adjacency, and residence are Sections 1--2.  The local ray and
cap conclusions are Theorem 3.1.  Proposition 4.1 gives both palettes.
Theorem 6.1 gives protected contextual equality, and Theorem 5.1 completes
the literal compiler.  Clause 5 is exactly the extra assertion needed to
iterate rather than use the packet once.  \(\square\)

## 8. Sharp remaining obstruction

The current quotient-fold audit supplies Hamilton owner topology, the ray
supports, the canonical cut casualties, and resident/nonzero inverses.  It
does **not** yet supply the following occurrence data:

1. the missing spacer/cut source occurrence between aligned addresses,
   including its ray transparency as in (3.5);
2. the actual `(d-1)`-link owner path and its no-`0 1^+ 0` trace certificate;
3. the intersection/union label ledger (4.3) after the owner rethread;
4. an all-`d` proof (or the required finite-depth scope) of the common-cut
   screened identity in Theorem 6.2, with an owner-legal screen; and
5. a common matching-closed background state satisfying (5.2) in both
   phases and returning under contraction.

Any one of these can fail while all scalar data in (6.2) remain true.  The
smallest immediate obstruction is the extra aligned source occurrence: if
it lies in a ray interval and contains a coordinate outside that ray target,
the advertised ray value is destroyed.  A second independent obstruction is
an `0 1^+ 0` coordinate trace in the link rail, which no choice of common
cap can repair.

Accordingly, the new mechanism is a sound prospective route, and the
source-language part is now exact through depth twelve.  The next artifact
must expose the complete occurrence-labelled **clipped** boundary word (or
its five ledgers above).  Theorem 2.5 proves that a host-address/rank census
of two independent full occurrences cannot certify the lift.

## 9. Independent proof audit

An independent proof audit checked the residence trace classification, the
`2d`-versus-`2d-2` transition count, the spacer intersection, both canonical
palette casualties, and the Hall/rank formula.  It required the explicit
simple-link condition in certificate row 3, the pairwise-distinct label
hypothesis, the support-versus-rainbow distinction in Section 4, and separate
phase restrictions of one compatible cap state.  Those corrections are
incorporated above.  Separately, Theorem 6.2 was obtained by the explicitly
scoped remote exact replay recorded there; no solver or unbounded search was
used.
