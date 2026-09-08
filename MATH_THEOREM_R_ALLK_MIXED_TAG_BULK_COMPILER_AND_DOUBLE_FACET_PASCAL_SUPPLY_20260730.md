# Mixed-tag bulk compilers and the double-facet Pascal supply theorem

Date: 2026-07-30  
Lane: R, all-`k` ported Pascal theorem  
Status: exact common-source and transport theorems; conditional induction
criterion; no unconditional all-`k` word.

## 0. Result

Let the old ground be `Omega`, with `|Omega|=2r`, and add two fresh
coordinates `z,y`.  The child middle rank is `R=r+1`.  The mixed strict-lower
block is

\[
 \mathcal K_{zy}
 =\{\{z,y\}\cup X:X\subseteq\Omega, |X|\le r-2\},
\]

of exact size

\[
 M_r=\sum_{j=0}^{r-2}\binom{2r}{j}
 =\frac{4^r}{2}
  -\frac{3r+1}{2(r+1)}\binom{2r}{r}.               \tag{0.1}
\]

The weakest mixed-module condition is not a density inequality.  After all
parent, child, carrier, module, seam, port, and protected-provider relations
have been joined, there must be **one** resulting literal source under which
every mixed core absent from the internal module occurs in the exhaustive
mixed seam/multi-seam bank.  In notation developed below, the exact condition
is

\[
 \boxed{\exists\omega\in\mathcal J_{\rm good}:
        \mathcal R_{zy}\setminus U_\omega
        \subseteq V_\omega.}                       \tag{0.2}
\]

If the boundary bank is charged to `t` seams at child horizon `d`, then
(0.2) forces the quantitative bulk bound

\[
 |U_\omega\cap\mathcal R_{zy}|
 \ge |\mathcal R_{zy}|-t\binom d2.                 \tag{0.3}
\]

The converse to (0.3) is false: the missing labels, not just their number,
must occur in the boundary trace bank.

There is an exact positive algebraic supply.  Let a parent rank-`r`
chronology `T` have a horizon-`D` source `A` which is order-one transparent.
Then the double-tag derivative

\[
 H_i=\{z,y\}\cup(T_{i-1}\cap T_i)                 \tag{0.4}
\]

is realized at horizon `D-1` by the source

\[
 R_p=\{z,y\}\cup A_p.                              \tag{0.5}
\]

Every selected parent compiler occurrence of length at most `D-1` for a
nonempty old core of rank at most `r-2` transports literally to the
corresponding mixed target.  An ordinary linear source may have the two
explicit boundary exceptions of Lemma 4.1.  One socket-redundant erosion
`R_{p_*}={z,y}` supplies the empty old core.  Thus a cyclic or
exterior-completed occurrence-complete transparent parent compiler supplies
all `M_r` mixed targets internally.  After `b` genuine cuts, it loses at most

\[
                         b\binom{D-1}{2}            \tag{0.6}
\]

selected core occurrences, and exact seam traces repair precisely those
labels.

The renewable duplex theorem of item 2059 contains exactly this local
algebra:

\[
 \boxed{
 \partial_y(\nabla\partial_zT)_i
   =\{z,y\}\cup(T_{i-1}\cap T_i).}                 \tag{0.7}
\]

It does not, however, export an occurrence-complete compiler atlas.  Its
authenticated socket is cardinality one, and a Pascal label isomorphism
cannot amplify one protected provider into the exponentially large family
(0.1).  A Pascal lower-rainbow forest supplies the correct mixed **owner**
sector and has enough asymptotic mass, but source transparency, exact
compiler traces after the Catalan cuts, phase alignment, and the global
common-source join remain unproved.

The exact remaining statement is therefore the **full-core transparent
Pascal-forest lemma** in Section 7.  This is strictly sharper than the former
unspecified “bulk mixed-tag module”: it names the parent matching, the
double-facet source map, the empty-core socket, every casualty trace, and the
one natural join which must be nonempty.

## 1. The four signature blocks

Fix `r>=2`, let

\[
 Z=\{z,y\},\qquad |\Omega|=2r,qquad R=r+1.
\]

Every nonempty target below the child middle rank `R` has a unique tag
signature `sigma subseteq Z`.  Removing its tags gives one of the following
old-core families:

\[
\begin{aligned}
 \mathcal K_\varnothing
   &=\{X\subseteq\Omega:1\le |X|\le r\},\\
 \mathcal K_z=\mathcal K_y
   &=\{X\subseteq\Omega:0\le |X|\le r-1\},\\
 \mathcal K_{zy}
   &=\{X\subseteq\Omega:0\le |X|\le r-2\}.
                                                               \tag{1.1}
\end{aligned}
\]

The empty old core occurs in the three nonempty tag blocks and not in the
no-tag block.  These ranges are exact because a target `sigma union X` is
strict lower precisely when

\[
                    1\le |\sigma|+|X|\le r.        \tag{1.2}
\]

With `u` marking total target rank and `s,t` marking `z,y`, respectively, the
strict-lower target polynomial is

\[
 \sum_{j=1}^{r}\binom{2r}{j}u^j
 +(s+t)\sum_{j=0}^{r-1}\binom{2r}{j}u^{j+1}
 +st\sum_{j=0}^{r-2}\binom{2r}{j}u^{j+2}.          \tag{1.3}
\]

Thus the mixed block is exactly the old lower deck truncated before its
rank-`(r-1)` top layer, shifted by `st`, together with the empty old core.
Formula (0.1) follows from

\[
 \sum_{j=0}^{r-1}\binom{2r}{j}
   ={4^r-\binom{2r}{r}\over2},
 \qquad
 \binom{2r}{r-1}={r\over r+1}\binom{2r}{r}.        \tag{1.4}
\]

## 2. The exact common-source functional

Put `W=binom(2r+2,r+1)`.  Freeze a proposed child carrier of length `W` with
`W+d` nonempty source positions, all typed module embeddings, and an
occurrence-labelled protected provider package `\mathcal P`.  Let `\mathcal J`
be the full natural join of:

1. the parent-source relations which are retained by the recursion;
2. the nonempty child-source, carrier-owner, interface, upper-shadow,
   residence, endpoint, and terminal relations;
3. the no-tag, one-tag, and mixed-tag module source maps;
4. every protected provider, port, seam, collar, and future-dependency
   relation; and
5. any occurrence all-different relation required for protected repeated
   typed demands.

The join deliberately excludes the residual strict-lower coverage conditions
which `Delta_2` is about to measure; including them would make the criterion
circular.  The protected package is an exact occurrence matching under every
assignment in `\mathcal J`.  Remove one protected demand and its exact cell per
protected edge.  All residual Boolean-mask demands below are unit demands;
any repeated auxiliary demand must be completely discharged in the protected
package (or handled instead by the general multiplicity formula
`sum_T (b_T-m_omega(T))^+`).

The parent variables remain in `\mathcal J`; they are not projected away
before all parent-side and child-side equations have been joined.  Put
`\Delta_2=+\infty` if `\mathcal J` is empty.

For `\omega\in\mathcal J`, write `Q(\omega)=(Q_p)` for its one literal child
source.  Delete every protected target demand and protected occurrence cell.
For a remaining physical interval cell `C`, define

\[
 \tau_\omega(C)
   =\left(\bigcup_{p\in C}Q_p\right)\cap Z,
 \qquad
 \phi_\omega(C)
   =\left(\bigcup_{p\in C}Q_p\right)\setminus Z.   \tag{2.1}
\]

Let `\mathcal R_\sigma` be the residual old-core labels in signature block
`sigma`, and put

\[
 \Lambda_\sigma(\omega)
 =\{\phi_\omega(C):C\text{ is free and }
                    \tau_\omega(C)=\sigma\}.       \tag{2.2}
\]

### Theorem 2.1 (four-signature common-source criterion)

Relative to the frozen carrier and protected package, the exact strict-lower
compiler defect is

\[
 \boxed{
 \Delta_2(\mathcal J;\mathcal P)
  =\min_{\omega\in\mathcal J}
     \sum_{\sigma\subseteq Z}
       |\mathcal R_\sigma\setminus
                    \Lambda_\sigma(\omega)|.}      \tag{2.3}
\]

A literal deadline compiler preserving the package exists if and only if
`Delta_2=0`.

#### Proof

Fix `omega`.  A physical interval has exactly one literal union label.  It
therefore belongs to the host family of at most one distinct Boolean target.
Host families of distinct targets, whether in the same or different tag
blocks, are disjoint.  Consequently arbitrary choices of one occurrence for
each label present in (2.2) are automatically occurrence-disjoint.  The
number of missing unit-demand targets is the sum in (2.3).

If the minimum is zero, these choices, together with the protected package,
give the lower compiler under one source `Q(omega)`.  Conversely, the parent
and child variables of any completing typed compiler give one assignment in
`\mathcal J`, and its actual free witnesses make every summand zero.  \(\square\)

For fixed `omega`, the deficiency decomposes by signature.  Across the fibre,
however,

\[
 \min_{\omega}\sum_\sigma d_\sigma(\omega)
 \ge\sum_\sigma\min_\omega d_\sigma(\omega),       \tag{2.4}
\]

where `d_sigma=|R_sigma minus Lambda_sigma|`.  Equality holds precisely when

\[
 \bigcap_{\sigma\subseteq Z}
       \operatorname{Argmin}_{\omega\in\mathcal J}d_\sigma(\omega)
       \ne\varnothing.                              \tag{2.5}
\]

Equivalently, one may join the four argmin relations only if every relation
retains all shared variables and is joined back with `\mathcal J`; projected
argmins can give a false positive.  Cartesian factorization is sufficient
for (2.5), but is not necessary.

### Proposition 2.2 (two-position failure of separate sector sources)

On coordinates `{a,z,y}`, take the two-source fibre

```text
Q^0 = (zy,ay),
Q^1 = (azy,a).
```

Both two-position sources have owner `azy`.  The mixed target `zy` occurs
only under `Q^0`, at the first singleton cell.  The no-tag target `a` occurs
only under `Q^1`, at the second singleton cell.  Thus, for the displayed
two-target residual problem `{zy,a}`, both separate block minima are zero and
the union candidate graph has a distinct-cell perfect matching, while every
common source has total deficiency one.
This disproves both independent sector sources and exchange of the source
minimum with the signature sum.  \(\square\)

## 3. The weakest quantitative mixed module

Define the already-good source relation

\[
 \mathcal J_{\rm good}
 =\{\omega\in\mathcal J:
      \mathcal R_\sigma\subseteq\Lambda_\sigma(\omega)
      \text{ for }\sigma=\varnothing,z,y\}.         \tag{3.1}
\]

Fix a source-independent, disjoint topological partition of physical free
cells into:

- an internal bulk bank `\mathcal B`; and
- an exhaustive allowed seam, multi-seam, ear, and boundary bank `\mathcal H`.

Exhaustive means that for every `\omega\in\mathcal J_{\rm good}`, every allowed free
mixed host `C` with `tau_omega(C)={z,y}` belongs to
`\mathcal B\cup\mathcal H`.  The tag signature is filtered only after the
source is chosen; the physical banks themselves do not depend on `omega`.

For `\omega\in\mathcal J_{\rm good}`, put

\[
\begin{aligned}
 U_\omega
  &=\{\phi_\omega(C):C\in\mathcal B,
                          \tau_\omega(C)=\{z,y\}\},\\
 V_\omega
  &=\{\phi_\omega(C):C\in\mathcal H,
                          \tau_\omega(C)=\{z,y\}\}.
                                                               \tag{3.2}
\end{aligned}
\]

### Theorem 3.1 (exact mixed bulk/seam criterion)

Relative to these frozen banks, the mixed compiler closes if and only if

\[
 \boxed{
 \exists\omega\in\mathcal J_{\rm good}:
       \mathcal R_{zy}\setminus U_\omega
       \subseteq V_\omega.}                        \tag{3.3}
\]

Equivalently, its exact remaining functional is

\[
 \boxed{
 \Delta_{\rm mix}
 =\min_{\omega\in\mathcal J_{\rm good}}
   |\mathcal R_{zy}\setminus(U_\omega\cup V_\omega)|.} \tag{3.4}
\]

Set `\Delta_{\rm mix}=+\infty` when `\mathcal J_{\rm good}` is empty.

When the minimum is attained, `Delta_mix=0` is necessary and sufficient for
deadline closure.  Appending the `Delta_mix` missing masks gives only a
length-`B+Delta_mix` OR word and does not preserve the deadline carrier.

#### Proof

For fixed `omega`, internal and boundary mixed cells are free
occurrence-labelled hosts.  Theorem 2.1 says that choosing one exact host per
present target creates no inter-label collision.  Thus every internally
missing label must occur in `V_omega`, and that condition is sufficient.
Taking the one common-source minimum proves (3.4).  \(\square\)

The condition is label-exact.  If every cell of `\mathcal H` has length at
most `d` and crosses at least one of `t` charged physical tag boundaries,
including the cyclic wrap when present, then

\[
 |V_\omega|\le|\mathcal H|\le t\binom d2.          \tag{3.5}
\]

Indeed a fixed boundary is crossed by at most

\[
 \sum_{\ell=2}^{d}(\ell-1)=\binom d2              \tag{3.6}
\]

intervals of length at most `d`.  An interval crossing several seams is
charged to one of them; union bounding proves (3.5).  Hence (3.3) implies

\[
 |U_\omega\cap\mathcal R_{zy}|
 \ge |\mathcal R_{zy}|-t\binom d2.                 \tag{3.7}
\]

Neither (3.5) nor (3.7) is sufficient without (3.3).

There is also a literal position lower bound.  One contiguous internal
module of `L>=d` source positions has exactly

\[
 \sum_{j=1}^{d}(L-j+1)
       =dL-\binom d2                               \tag{3.8}
\]

interval cells of lengths at most `d`.  If it alone misses at most `h`
mixed labels, then necessarily

\[
 dL-\binom d2\ge M_r-h.                            \tag{3.9}
\]

Thus the required object is genuinely bulk even before label collisions are
considered.

## 4. Double-facet compiler transport

Let

\[
 A=(A_0,\ldots,A_{N+D-1}),\qquad D\ge2,            \tag{4.1}
\]

be a nonempty parent source on `Omega` realizing a rank-`r` chronology

\[
 T_i=\bigcup_{p=i}^{i+D}A_p,qquad 0\le i<N.       \tag{4.2}
\]

Assume complete internal order-one transparency:

\[
 K_i:=T_{i-1}\cap T_i
      =\bigcup_{p=i}^{i+D-1}A_p,qquad1\le i<N.    \tag{4.3}
\]

In a cyclic source, require (4.3) on every cyclic start.  In a linear source,
**exterior-completed transparency** means that the two exposed length-`D`
prefix/suffix cells also belong to declared rank-`(r-1)` facet windows.

### Lemma 4.1 (short-core descent)

Suppose the parent source covers every strict-lower old target.  Every core
`X` with `1<=|X|<=r-2` has a witnessing interval of at most `D-1` source
positions, except possibly the at most two labels carried solely by the
exposed length-`D` prefix and suffix cells of an ordinary linear source.
Under cyclic or exterior-completed transparency there are no exceptions.

#### Proof

Every strict-lower witness has length at most `D`, because any `D+1`
consecutive source positions contain a rank-`r` owner window.  Every internal
length-`D` interval is the right side of (4.3) and has rank exactly `r-1`.
It therefore cannot realize a core of rank at most `r-2`.  Only the two
linear length-`D` cells at starts `0,N` are not covered by (4.3).  \(\square\)

Let `\mathcal E_{\rm bd}` be the set of nonempty cores of rank at most `r-2`
which have no parent witness of length at most `D-1`.  By Lemma 4.1 each such
core is the label of one of the two exposed linear length-`D` cells.  Thus
`|\mathcal E_{\rm bd}|\le2`, and `\mathcal E_{\rm bd}` is empty under cyclic
or exterior-completed transparency.  Let `\mathcal M_{\le r-2}` choose one
short occurrence of every nonempty core outside `\mathcal E_{\rm bd}`.  Let
`p_*` be a
parent source position and define

\[
 B_{p_*}=\varnothing,
 \qquad B_p=A_p\quad(p\ne p_*),
 \qquad R_p=\{z,y\}\cup B_p.                       \tag{4.4}
\]

Call `p_*` **full-core redundant** when `A_(p_*)` is contained in the union of
the other old letters in every typed child source-union equation which
contains `p_*`, including in particular:

1. every declared `D`-position facet owner window;
2. every selected interval in `\mathcal M_{\le r-2}`;
3. every connector/interface owner window; and
4. every exported provider and complete future facet/bridge dependency
   collar.

This is the exact selected-interval survival condition, not merely a degree
or rank condition.

### Theorem 4.2 (double-facet bulk supply)

Assume:

1. the parent source and matching satisfy Lemma 4.1, with
   `\mathcal E_{\rm bd}` defined as above;
2. `p_*` is full-core redundant;
3. an occurrence-preserving embedding `iota` places the mixed source (4.4)
   in the child, maps all selected intervals literally, and is
   deadline-aligned (the `D`-position windows are actual child mixed-owner
   windows and every selected image is an allowed, free, pairwise distinct
   child mixed cell); the singleton `[iota(p_*),iota(p_*)]` is also free,
   unless its same target is already discharged by the protected package;
4. the parent variables, this mixed module, every other signature module,
   all seams, and every protected relation have one common assignment
   `\omega\in\mathcal J`.

Then the embedded source realizes the mixed owner chronology

\[
 H_i=\{z,y\}\cup K_i
    =\bigcup_{p=i}^{i+D-1}R_p                     \tag{4.5}
\]

at local horizon `D-1`, preserves every selected provider, and supplies

\[
 \{z,y\}\cup X\longmapsto\iota(C_X)
 \qquad(1\le|X|\le r-2, X\notin\mathcal E_{\rm bd}), \tag{4.6}
\]

together with

\[
 \{z,y\}\longmapsto[\iota(p_*),\iota(p_*)].       \tag{4.7}
\]

Consequently a cyclic or exterior-completed uncut module supplies all `M_r`
mixed targets internally.  An ordinary linear module supplies every mixed
target except the at most two labels in `\mathcal E_{\rm bd}`, which remain for
boundary replay.

#### Proof

Full-core redundancy preserves every union in (4.3), so adjoining `{z,y}`
gives (4.5).  It also preserves the old union `X` of every selected compiler
interval.  Adjoining the common tag pair gives (4.6), while the eroded
singleton letter is exactly `{z,y}`, proving (4.7).  The occurrence embedding
and common assignment make all displayed edges literal in one child source.
The core ranges in (1.1) show that only `\mathcal E_{\rm bd}` can remain in the
ordinary linear case.  \(\square\)

The eroded child letter is nonempty.  The parent letter `A_(p_*)` has been
deleted from the child image, so the map from parent to child sources is not
injective.  The parent variable must remain in the natural join until every
parent-side relation has been imposed.

### Corollary 4.3 (cut version)

Suppose, before embedding, the selected parent source bank is cut and
rethreaded at `b` genuine adjacencies while retaining every source position
and every piece interior.  Assume separately that every new seam-crossing
owner/source equation is deadline-aligned and that full-core redundancy holds
in every new seam-crossing equation containing `p_*`.  Put `delta=D-1`.  At
most

\[
                         b\binom\delta2             \tag{4.8}
\]

selected short-core intervals are destroyed.  Let `\mathcal E_{\rm cut}` be
the set of residual core labels outside `\mathcal E_{\rm bd}` having no free
internal host anywhere in the complete post-rethread trace catalogue.  Every
member's selected old witness crossed a cut, so its cardinality is bounded by
(4.8).  With the redundant erosion
retained, the mixed module is complete if and only if every core in

\[
                         \mathcal E_{\rm bd}\cup\mathcal E_{\rm cut} \tag{4.9}
\]

occurs in its exact same-source mixed seam/multi-seam trace bank.

Without exterior completion and without the redundant erasure, its terminal
mixed defect is at most

\[
                     2+b\binom{D-1}{2}+1,          \tag{4.10}
\]

before any seam replay: two possible linear boundary labels, the cut
casualties, and the empty core.  For `b=O(1)` and
`D=Theta(sqrt(r))`, this is `O(r)`.

#### Proof

A selected interval crossing one cut uses positive lengths `u,v` on its two
sides with `u+v\le\delta`; there are at most `\binom{\delta}{2}` such
intervals.  A union
bound over the cuts proves (4.8).  Piece interiors transport by Theorem 4.2,
and Theorem 3.1 gives the exact trace criterion.  The three terms in (4.10)
are Lemma 4.1, (4.8), and the canonical empty-core obstruction.  The
separately assumed new-owner equations make the rethreaded object a legal
mixed module; the cut count alone would not do so.  \(\square\)

The cut bound does not apply if a proposed Pascal contraction deletes source
positions or facet occurrences rather than merely cutting and reordering
retained pieces.

## 5. The four-sector Pascal diagonal

For a rank-`r` chronology `T`, define

\[
 (\partial T)_i=T_{i-1}\cap T_i,
 \qquad
 (\nabla T)_i=T_i\cup T_{i+1}.                     \tag{5.1}
\]

Before physical rethreading, one parent source `A` gives the four formal
Pascal channels

\[
\begin{array}{c|c|c}
\text{source relation}&\text{owner chronology}&\text{local horizon}\\ \hline
A&\nabla T&D+1\\
\{z\}+A&\{z\}+T&D\\
\{y\}+A&\{y\}+T&D\\
\{z,y\}+A&\{z,y\}+\partial T&D-1.
\end{array}                                        \tag{5.2}
\]

The first row follows because a `D+2`-position source union is
`T_i union T_(i+1)`; the middle rows are canonical suspensions; the last is
order-one transparency.  The formal joint source fibre is the diagonal image

\[
 \left\{(A,\{z\}+A,\{y\}+A,\{z,y\}+A):
                    A\in\mathcal F_{\rm parent}\right\}.             \tag{5.3}
\]

Deterministic redundant erosions can be added as typed relations while the
parent variable `A` remains in the join.  Equation (5.3) is the local
common-source advantage of the Pascal construction.  It does not prove that
arbitrarily rethreaded physical modules, phases, seams, and upper collars
have a nonempty global join.

The renewable duplex algebra gives the mixed row directly.  Starting from

\[
 \partial_zT=\{z\}+\partial T,
 \qquad
 \nabla\partial_zT=\{z\}+T,
\]

take the `y`-facet of the returned union mate:

\[
\begin{aligned}
 \partial_y(\nabla\partial_zT)_i
 &=\{y\}\cup
   [ (\{z\}\cup T_{i-1})
      \cap(\{z\}\cup T_i)]\\
 &=\{z,y\}\cup(T_{i-1}\cap T_i).                 \tag{5.4}
\end{aligned}
\]

On sources this is exactly `A_p -> {z,y} union A_p` at the one-shorter facet
horizon.  If the additional full-core-redundant erosion of Theorem 4.2 exists,
its eroded cell is the pure `{z,y}` cell.  Item 2059 itself does not prove
that erosion.

The exact depth signatures are

\[
 \text{lower depth }s\ge2:\quad s\mapsto s-1,
 \qquad
 \text{middle/upper depth }q\ge0:\quad q\mapsto q+1. \tag{5.5}
\]

The second map uses the natural-union bridge and the protected
no-singleton-positive-run hypothesis from item 2059.

### Proposition 5.1 (what item 2059 supplies)

Item 2059 proves the tag identities (5.4), the local horizon shift, the
protected depth transport, deterministic parent-source correlation, and the
renewable socket/bridge collars.  If its protected matching is strengthened
to the full `\mathcal M_{\le r-2}`, the separate full-core-redundant erosion
is proved, and the entire mixed facet has a deadline-aligned occurrence
embedding, Theorem 4.2 supplies the required bulk module.

The item-2059 theorem as currently proved does not make that strengthening.
Its declared matching may be cardinality one, and its sector recursion uses
the returned connector copied while avoiding `y`; that copied sector has no
internal `{z,y}` cells.  A label-preserving Pascal transport carries exactly
the declared provider occurrences and cannot amplify one protected edge into
the `M_r` edges required by (0.1).  \(\square\)

At a deadline drop where the child mixed horizon is `D-1`, the raw facet is
phase-aligned.  On a plateau where the child deadline is `D`, the whole mixed
module needs one unit of phase placement.  The local phase credit of one
socket does not align the entire compiler bank.  A generalized flat,
inverse-phase block, or equivalent braid must preserve/recreate every shifted
compiler diagonal; this is an additional hypothesis, not a consequence of
(5.4).

### Proposition 5.2 (shadow correctness does not imply source transparency)

At `D=2`, take

```text
A_0=13, A_1=2, A_2=2, A_3=14.
```

Then

\[
 T_0=A_0\cup A_1\cup A_2=123,
 \qquad
 T_1=A_1\cup A_2\cup A_3=124
\]

are strict Johnson neighbours and `T_0 intersection T_1=12`.  But the
shortened source window is

\[
                         A_1\cup A_2=2\ne12.        \tag{5.6}
\]

Thus the mixed shadow owner can exist while the source fails order-one
transparency.  All-depth carrier shadow completeness alone does not prove the
compiler transport in Theorem 4.2.  \(\square\)

## 6. The Catalan forest is a reservoir, not yet a compiler

Put

\[
 W_0=\binom{2r}{r},
 \qquad
 A_0=\binom{2r}{r-1}={r\over r+1}W_0,
 \qquad
 \operatorname{Cat}_r={1\over r+1}W_0.             \tag{6.1}
\]

A spanning acyclic lower-rainbow **path forest** on the `W_0` rank-`r`
vertices with one edge for every rank-`(r-1)` intersection colour has `A_0`
edges and

\[
                         W_0-A_0=\operatorname{Cat}_r              \tag{6.2}
\]

path components.  Its doubly tagged edge intersections enumerate exactly
the child mixed middle-owner sector

\[
 \{\{z,y\}\cup K:K\in\tbinom{\Omega}{r-1}\}.      \tag{6.3}
\]

This is the exact GMM/Pascal lower-rainbow owner reservoir.  The component
identity (6.2) uses the spanning acyclic forest hypothesis; for an arbitrary
lower-rainbow selection, `W_0-A_0` is only the vertex-edge surplus, and
isolated vertices/cycle rank must be counted explicitly.

There is a useful conditional density estimate.  Suppose this forest is
obtained by cutting an occurrence-complete, order-one-transparent parent
source at at most `Cat_r` adjacencies, retaining every source position, and
suppose its selected short-core compiler intervals are those in Theorem 4.2.
For `D=Theta(sqrt(r))`, the number of potentially destroyed selected
providers is at most

\[
 \operatorname{Cat}_r\binom{D-1}{2}
   =O\!\left({4^r\over\sqrt r}\right)
   =o(M_r).                                         \tag{6.4}
\]

Thus the forest would give a

\[
                         1-O(r^{-1/2})               \tag{6.5}
\]

density mixed bulk module before seam repair.

The hypotheses before (6.4) are not presently proved for the PBBS/GMM
forest.  In particular, exact middle-owner enumeration (6.3) does not imply
that one transparent parent compiler matching survives inside its path
pieces, and (6.4) does not identify any lost core with a new seam trace.  It
is a quantitative target for the missing theorem, not a completed compiler.

The old provider cuts `b` and the new physical tag-boundary count `t` are
different ledgers.  The former controls destroyed selected parent witnesses
through (4.8); the latter controls available child boundary cells through
(3.5).  They must not be identified without a physical embedding theorem.

## 7. Exact remaining induction lemma

The former “bulk mixed-tag module” placeholder can now be replaced by the
following explicit statement.

> **Full-core transparent Pascal-forest lemma `FCT(r,D,d)` (UNPROVED).**  There
> is one typed parent/child construction satisfying all of the following.
>
> 1. One parent source has an occurrence-labelled matching for every old
>    core `X` with `1<=|X|<=r-2`, using occurrences of length at most `D-1`
>    except for an explicitly named set `\mathcal E_{\rm bd}` of size at most two,
>    and is order-one transparent on every declared mixed-facet owner and
>    endpoint completion.
> 2. A full-core redundant position supplies the pure `{z,y}` socket while
>    preserving the selected short matching outside `\mathcal E_{\rm bd}`
>    and the renewable duplex germ.
> 3. The double-tag facet pieces form the exact mixed middle-owner sector,
>    are embedded at the child deadline phase, and retain all source
>    positions required by the cut ledger.  Every retained, non-destroyed
>    selected short provider maps to a contiguous allowed free child cell;
>    these images are pairwise distinct, and the pure-tag singleton cell is
>    free.
> 4. At the source in clause 5, every core in `\mathcal E_{\rm bd}` and every
>    residual core absent from the complete internal post-cut catalogue lies
>    in the free mixed seam bank; equivalently
>    `\mathcal E_{\rm bd}\cup\mathcal E_{\rm cut}\subseteq V_\omega`.
> 5. There is one assignment `\omega\in\mathcal J_{\rm good}` in which the parent
>    matching, erosion, retained providers, the free trace condition in
>    clause 4, the
>    no-tag and two one-tag compilers, all protected ports, every upper
>    bridge/seam witness, residence, endpoints, and the deadline position
>    ledger coexist.

### Theorem 7.1 (conditional all-block closure)

Assume the child carrier is exact-middle, upper-complete, resident, physically
legal, and has exactly `W+d=B(2r+2)` source positions.  Assume the no-tag and
two one-tag residual blocks are complete under the same joined source.  If
`FCT(r,D,d)` holds, then the mixed block satisfies (3.3), the entire strict
lower ideal is compiled, and the child source is a universal deadline word.

More generally, if under that same `omega` clause 4 leaves `h` distinct
residual mixed labels unrepaired, literal appendage gives a terminal universal
word of length at most `B(2r+2)+h`, but not a deadline-preserving recursive
child.

#### Proof

Clauses 1--3, Theorem 4.2, and Corollary 4.3 give the complete internal mixed
atlas except for the explicitly destroyed core occurrences.  Clause 4 is exactly the
inclusion in Theorem 3.1, so the mixed block closes under the one source from
clause 5.  Theorem 2.1 joins it with the other three strict-lower blocks.
The fixed carrier hypotheses supply the middle and upper ideals and every
physical obligation.  No letters are added in the exact case, so the length
is `B(2r+2)`.  Appending one literal mask per residual label proves the
last assertion.  \(\square\)

Theorem 7.1 is integral and literal.  Its mixed-block source quantifier is

\[
 \exists\omega\in\mathcal J_{\rm good}\quad
 \forall X\in\mathcal R_{zy}\quad
 \exists\text{ one exact free physical interval }C_X,             \tag{7.1}
\]

not separate source choices for different targets or sectors.

Item 2059 supplies the local identities, the renewable germ, and the
double-facet/tag/bridge transport used in clause 3.  It does not supply the
full-core redundant erosion in clause 2.  The Pascal lower-rainbow
forest supplies the owner labels and the conditional density estimate in
clause 3.  No current theorem proves the occurrence-complete transparency,
casualty traces, deadline-wide phase embedding, or nonempty global join in
clauses 1, 4, and 5.  Therefore no unconditional all-`k` upper bound is
claimed here.

## 8. Independent quantifier and proof audit

Three independent proof passes checked the decisive implications.  The
following scope points are part of the theorem.

1. The source is chosen once from the full natural join.  Fixed-source
   deficiencies add by signature; their minima do not add unless their
   argmin relations have a nonempty join.
2. One demand unit and its exact occurrence are deleted per protected edge
   before the residual sets in (2.2) are formed.  Every repeated typed demand
   is fully protected here; otherwise the multiplicity formula, not the set
   formula (2.3), is required.  Ordinary Boolean targets are unit demand.
3. Empty old cores occur in tagged blocks.  The eroded mixed cell remains a
   legal nonempty source letter because it equals `{z,y}`.
4. In a linear source, internal transparency leaves two exposed length-`D`
   cells.  Exterior completions remove the exception; otherwise their at most
   two labels are charged explicitly.
5. The cut count applies only to retained positions and piece interiors.
   Deleting positions or selected facet occurrences is outside Corollary 4.3.
6. Multi-seam intervals are included in `\mathcal H` and charged once for the
   upper bound (3.5).  A cyclic wrap is a charged boundary.
7. The provider-cut count `b` and child tag-boundary count `t` are independent
   until a physical embedding relates them.
8. Erosion is not injective on sources.  Keeping the parent variables in the
   natural join prevents an unsound premature projection.
9. The shadow counterexample in Proposition 5.2 proves that carrier owner and
   shadow correctness alone do not imply source transparency.
10. Middle ownership, upper completeness, residence, phase alignment,
    endpoints, and the exact deadline position count are hypotheses of the
    closure theorem, not consequences of mixed lower coverage.

No finite search, SAT solver, web access, or certificate computation was used.
