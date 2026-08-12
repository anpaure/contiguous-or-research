# Endpoint rerooting, singleton retiming, and the ALO common-cap compiler

**Date:** 2026-07-31  
**Lane:** AD, reusable theorem extracted from the genuine-four-filter K16 construction  
**Status:** unconditional finite theorems; K16 is a verified instantiation; no all-dimension existence claim

## 0. Outcome and scope

The successful K16 construction separates into three reusable operations.

1. A middle chronology may be rerooted by orienting contiguous blocks.  All
   internal interval ORs are preserved; Johnson legality and every possible
   upper-shadow change are confined to the new block seams.
2. An order-preserving P/Q retiming has an exact lower-cell inventory.
   A uniquely hosted singleton may be contracted without losing any literal
   information.
3. After the chronology and retiming are fixed, simultaneous lower ownership
   has an exact **at-least-one-provider** (ALO) encoding.  Neither at-most-one
   per lower target nor at-most-one per physical cell is needed: exact interval
   OR semantics makes a shared cell for two distinct targets contradictory,
   while duplicate witnesses for one target can be discarded.

The third statement is strictly smaller than the earlier exact-matching
formulation.  It is not a relaxation.  It produces a literal word whenever it
is satisfiable.

The package does **not** say that an endpoint reroot with the required upper
coverage exists in every dimension, that a singleton-compatible retiming
always exists, or that the final ALO formula is always satisfiable.  Those are
the three explicit construction gates.

Throughout, unions of masks are literal bitwise ORs.

## 1. Fixed chronology, envelopes, and exact individual providers

Let \(\Omega\) be a finite coordinate set and let

\[
P=\{0,1,\ldots,L-1\}
\]

be the physical positions.  A fixed middle chronology consists of distinct
targets \(T_0,\ldots,T_{W-1}\subseteq\Omega\) and physical row intervals

\[
I_i=[s_i,d_i]\subseteq P.
\]

Put

\[
E_p=\bigcap_{i:p\in I_i}T_i,                              \tag{1.1}
\]

where an empty intersection is \(\Omega\).  We require the maximal-envelope
test

\[
E_p\ne\varnothing,\qquad
\bigcup_{p\in I_i}E_p=T_i\quad(0\le i<W).                 \tag{1.2}
\]

These conditions are necessary for any literal realization and, for the
middle rows alone, sufficient: use the word \((E_p)\).

Let \({\cal C}\) be a catalogue of distinct physical intervals intended as
lower witnesses.  For a cell \(C\in{\cal C}\), define

\[
U_C=\bigcup_{p\in C}E_p                                   \tag{1.3}
\]

and, for each middle bit \(b\in T_i\), its envelope carrier

\[
H_{i,b}=\{p\in I_i:b\in E_p\}.                            \tag{1.4}
\]

Define the mandatory mask of \(C\) by

\[
M_C=\{b:\text{ for some }i, b\in T_i
                 \text{ and }H_{i,b}\subseteq C\}.        \tag{1.5}
\]

Thus \(b\in M_C\) means that every envelope host of \(b\) in at least one
middle row lies inside \(C\).

### Theorem 1.1 (exact individual-provider criterion)

Let \(S\ne\varnothing\) be a lower target.  Capping the maximal envelope by
\(S\) on \(C\),

\[
E^{S,C}_p=
\begin{cases}
E_p\cap S,&p\in C,\\
E_p,&p\notin C,
\end{cases}                                               \tag{1.6}
\]

leaves every letter nonempty, preserves every middle row, and realizes
\(S\) exactly on \(C\) if and only if

\[
S\subseteq U_C,\qquad M_C\subseteq S,qquad
E_p\cap S\ne\varnothing\quad(p\in C).                    \tag{1.7}
\]

#### Proof

The last condition in (1.7) is exactly nonemptiness on \(C\).  Under
\(S\subseteq U_C\),

\[
\bigcup_{p\in C}(E_p\cap S)=S\cap U_C=S,                 \tag{1.8}
\]

so the cell OR is exactly \(S\).

A bit \(b\in T_i\) is erased from middle row \(i\) precisely when all of its
envelope hosts lie in \(C\) and \(b\notin S\).  Such an erasure exists
precisely when \(M_C\nsubseteq S\).  This proves both directions. \(\square\)

Write \({\cal D}\subseteq{\cal L}\times{\cal C}\) for the provider
relation given by (1.7), where \({\cal L}\) is the family of distinct lower
target masks.

### Corollary 1.2 (catalogue completeness test)

Suppose a nonempty word \((A_p)\) preserves the displayed middle rows and
realizes \(S\) on a catalogue cell \(C\).  Then \((S,C)\in{\cal D}\).

#### Proof

Middle exactness gives \(A_p\subseteq E_p\).  Exactness on \(C\) gives
\(A_p\subseteq S\) for \(p\in C\), hence every \(E_p\cap S\) there is
nonempty.  Every bit of \(S\) occurs in some \(E_p\), proving
\(S\subseteq U_C\).  If \(b\in M_C\), the middle row witnessing (1.5)
forces \(b\) to occur inside \(C\), so \(b\in S\). \(\square\)

Consequently, the only extra completeness hypothesis needed later is that
every physically permitted lower witness interval belongs to \({\cal C}\).

## 2. Exact endpoint-reroot ledger

Let \(T=(T_0,\ldots,T_{W-1})\) be any target path.  Partition its indices
into consecutive blocks

\[
B_1\Vert B_2\Vert\cdots\Vert B_t
\]

and independently orient each block forward or backward, without changing
the order of the blocks.  Let \(T'\) be the resulting sequence.

For a sequence \(R\), let

\[
{\cal U}(R)=\left\{\bigcup_{j=a}^{b}R_j:0\le a\le b<|R|\right\}. \tag{2.1}
\]

Let \({\cal U}_{\rm int}\) be the union of the interval-OR families internal
to the individual blocks.  Let \({\cal U}_{\rm old}\) and
\({\cal U}_{\rm new}\) be the interval ORs crossing at least one block seam
before and after reorientation.

### Theorem 2.1 (block-reroot localization)

The following statements hold exactly.

1. \(T'\) is a permutation of \(T\).
2. Every unordered adjacency internal to a block is preserved.  Hence, if
   \(T\) is a path in an undirected graph, \(T'\) is a path if and only if
   every new block-endpoint seam is an edge.
3. The complete interval ledgers are

   \[
   {\cal U}(T)={\cal U}_{\rm int}\cup{\cal U}_{\rm old},
   \qquad
   {\cal U}(T')={\cal U}_{\rm int}\cup{\cal U}_{\rm new}. \tag{2.2}
   \]

   In particular, no interval OR internal to a block can be lost.
4. If adjacent middle masks have a colour determined by their unordered
   endpoint pair—for Johnson paths, the colour is their union—then the
   colour multiset changes by deleting the old seam colours and inserting
   the new seam colours, with multiplicity.  No internal colour changes.

#### Proof

Reversing a block is a permutation and takes each of its contiguous
subintervals bijectively to a contiguous subinterval having the same set of
members.  Union is insensitive to their order.  Internal unordered adjacent
pairs are likewise unchanged.  Every interval not internal to one block
crosses a seam, proving (2.2) and the colour ledger. \(\square\)

### Corollary 2.2 (two-ended reroot)

For cut indices \(a<b\), orient

\[
[0,a]\text{ backward},\quad[a+1,b-1]\text{ forward},\quad
[b,W-1]\text{ backward}.                                \tag{2.3}
\]

If \(T\) is a Johnson path, only the two tests

\[
T_0\sim T_{a+1},qquad T_{b-1}\sim T_{W-1}              \tag{2.4}
\]

are needed for path legality.  The old seam colours

\[
T_a\cup T_{a+1},\qquad T_{b-1}\cup T_b                  \tag{2.5}
\]

are replaced by

\[
T_0\cup T_{a+1},\qquad T_{b-1}\cup T_{W-1}.             \tag{2.6}
\]

For any required upper family \({\cal U}^\star\), the reroot preserves it
if and only if

\[
{\cal U}^\star\subseteq
{\cal U}_{\rm int}\cup{\cal U}_{\rm new}.               \tag{2.7}
\]

Thus endpoint legality is local, but arbitrary-depth upper preservation is
an exact seam-crossing test, not an automatic consequence of q1 legality.
For a cyclic chronology one must additionally include the wrap seam; no
cyclic wrap is implicit in this theorem.

## 3. Order-preserving retiming and exact boundary restitution

Let \(L=W+h\).  Choose omitted-start and omitted-deadline sets

\[
X,Y\subseteq P,qquad |X|=|Y|=h.                       \tag{3.1}
\]

Write the complements increasingly as

\[
P\setminus X=(s_0<\cdots<s_{W-1}),qquad
P\setminus Y=(d_0<\cdots<d_{W-1}).                    \tag{3.2}
\]

An order-preserving retiming is admissible when \(s_i\le d_i\) for every
\(i\); it assigns row \(T_i\) to \(I_i=[s_i,d_i]\).

Fix a maximum free-cell length \(\ell\).  The exact prefix catalogue is

\[
{\cal C}(X,Y)=
\{[s_i,s_i+j-1]:1\le j\le d_i-s_i\}
\ \cup\
\{[x,x+j-1]:x\in X, 1\le j\le\min(\ell,L-x)\}.       \tag{3.3}
\]

The first family consists of proper prefixes of selected rows; the second
is the complete boundary restitution at omitted starts.

### Theorem 3.1 (exact cell-count identity)

The cells in (3.3) are distinct and

\[
|{\cal C}(X,Y)|
=\sum_{i=0}^{W-1}(d_i-s_i)
 +\sum_{x\in X}\min(\ell,L-x).                         \tag{3.4}
\]

#### Proof

Every interval in (3.3) is determined by its left endpoint and length.
Selected and omitted starts are disjoint; within one start the displayed
lengths are distinct.  Counting gives (3.4). \(\square\)

This is the precise replacement for a uniform \(h\ell\) boundary credit.
Near the right endpoint the restitution is truncated.

### Theorem 3.2 (forced-singleton contraction)

Let \(z\in\Omega\), and suppose the singleton lower target \(\{z\}\) has
exactly one provider cell \(C_0\) in (1.7).  Then every compiler in this
fixed retiming has

\[
A_p=\{z\}\qquad(p\in C_0).                             \tag{3.5}
\]

It is therefore equisatisfiable to:

1. replace \(E_p\) by \(\{z\}\) on \(C_0\);
2. delete the singleton target and reserve \(C_0\); and
3. rebuild all residual provider domains from the capped envelope.

#### Proof

The unique provider must witness \(\{z\}\).  Every letter is nonempty and
their union on \(C_0\) is the singleton, so each letter there equals
\(\{z\}\).  Any original compiler restricts to the contracted instance.
Conversely, a residual compiler for the capped envelope already has (3.5),
so reinserting the target and its reserved cell gives an original compiler.
Individual feasibility of the provider guarantees that all middle rows
survive the cap. \(\square\)

For a general forced target \(S\), fixing its unique provider remains exact,
but its positive OR requirements must be retained; nonemptiness alone forces
all letters only in the singleton case.  Repeated forced-provider
propagation is therefore exact provided each fixed non-singleton pin keeps
its remaining positive-bit clauses.

## 4. Maximal common cap without a matching hypothesis

Let \(F\subseteq{\cal D}\) be any selected provider set.  It may initially
contain more than one provider for a target and no cell-capacity constraints
are assumed.  Define

\[
K_p(F)=E_p\cap
\bigcap_{(S,C)\in F:\ p\in C}S.                         \tag{4.1}
\]

### Theorem 4.1 (provider-cover maximal-cap theorem)

There is a nonempty word realizing every selected provider in \(F\) and
every middle row if and only if

\[
\begin{aligned}
K_p(F)&\ne\varnothing &&(p\in P),\\
\bigcup_{p\in I_i}K_p(F)&=T_i &&(0\le i<W),\\
\bigcup_{p\in C}K_p(F)&=S &&((S,C)\in F).
\end{aligned}                                           \tag{4.2}
\]

When (4.2) holds, \(A_p=K_p(F)\) is a realizing word.

#### Proof

If \(B\) is any realizing word, middle exactness gives \(B_p\subseteq E_p\).
Every selected cell exactness gives \(B_p\subseteq S\) when \(p\in C\).
Thus \(B_p\subseteq K_p(F)\).  Since both \(K_p(F)\) and its row/cell
unions are contained in the prescribed masks, the nonempty realizing word
\(B\) forces all equalities in (4.2).

Conversely, (4.2) says directly that the maximal word \(K(F)\) is nonempty
and has every required row and cell OR. \(\square\)

### Corollary 4.2 (capacity is semantic)

If (4.2) holds, one physical cell cannot be selected for two distinct target
masks.  If \(F\) contains at least one provider for every distinct lower
target, one may retain any one provider per target; the retained cells are
automatically distinct and the same word remains valid.

#### Proof

The OR of one fixed physical interval is a single mask.  If both \((S,C)\)
and \((R,C)\) are realized, then \(S=R\).  Deleting duplicate witnesses for
one target only removes constraints. \(\square\)

This is why a lower **provider cover**, rather than an explicitly encoded
matching, is enough.

## 5. Exact ALO-only literal compiler

For every envelope bit \(b\in E_p\), introduce a word variable \(z_{p,b}\).
It denotes membership of \(b\) in the physical letter \(A_p\).  For every
provider edge \((S,C)\in{\cal D}\), introduce \(y_{S,C}\).

Use the following clauses.

### Target coverage

For each distinct lower target \(S\),

\[
\bigvee_{C:(S,C)\in{\cal D}}y_{S,C}.                    \tag{5.1}
\]

This is ALO, not exactly one.

### Nonempty letters and exact middle rows

For every physical position and every middle-row bit,

\[
\bigvee_{b\in E_p}z_{p,b},                              \tag{5.2}
\]

\[
\bigvee_{p\in H_{i,b}}z_{p,b}qquad(b\in T_i).          \tag{5.3}
\]

Bits outside \(E_p\) have no variable, so a middle row cannot gain a bit.

### Conditional exact provider semantics

For every \((S,C)\in{\cal D}\), impose

\[
\neg y_{S,C}\vee\neg z_{p,b}
\quad(p\in C,\ b\in E_p\setminus S),                   \tag{5.4}
\]

and

\[
\neg y_{S,C}\vee
\bigvee_{p\in C:\ b\in E_p}z_{p,b}
\quad(b\in S\setminus M_C).                            \tag{5.5}
\]

No positive clause is needed for \(b\in M_C\): by (1.5), some middle clause
(5.3) has all of its hosts inside \(C\).

### Theorem 5.1 (ALO collapse)

Assume the lower masks are distinct and the physical cell catalogue is
complete.  Clauses (5.1)--(5.5) are satisfiable if and only if there is a
nonempty physical word which realizes every middle target and every lower
target in the fixed schedule.

Neither target AMO nor cell AMO is required.

#### Proof

Let a satisfying assignment be given and define

\[
A_p=\{b\in E_p:z_{p,b}=1\}.
\]

Clauses (5.2)--(5.3) make the letters nonempty and the middle rows exact.
If \(y_{S,C}=1\), clauses (5.4) give
\(\bigcup_{p\in C}A_p\subseteq S\).  Clause (5.5) supplies every bit in
\(S\setminus M_C\).  For \(b\in M_C\), a middle clause (5.3) whose carrier
lies in \(C\) supplies \(b\).  Therefore

\[
\bigcup_{p\in C}A_p=S.                                  \tag{5.6}
\]

By (5.1), every lower target has at least one exact witness.

If two true selectors with distinct target masks used the same cell, (5.6)
would give two different values for the OR of that cell, an impossibility.
Thus cell AMO is implied by exact semantics.  If one target has several true
selectors, retain any one; all others are harmless redundant witnesses.
Thus target AMO is unnecessary as well.

Conversely, let a literal compiler be given.  Completeness of the catalogue
and Corollary 1.2 provide a provider edge for one physical occurrence of each
lower target.  Set precisely those selectors true and take the compiler's
letter bits as \(z\).  All clauses follow from exact middle and lower ORs.
\(\square\)

The distinct-mask hypothesis is essential only to the automatic cell-AMO
sentence.  If the same mask is represented by several independently required
labels, those labels may share a cell and a separate occurrence-capacity
condition must be stated.  The Boolean-ideal covering problem has one target
per mask, so Theorem 5.1 applies directly.

### Corollary 5.2 (upper lift)

Suppose every required upper target \(U\) has a consecutive middle witness

\[
U=T_i\cup T_{i+1}\cup\cdots\cup T_j,                    \tag{5.7}
\]

and the physical row intervals have no gap on that block:

\[
s_{h+1}\le d_h+1\qquad(i\le h<j).                       \tag{5.8}
\]

Then every satisfying assignment of (5.1)--(5.5) realizes \(U\) on the
literal physical interval \([s_i,d_j]\).

#### Proof

Condition (5.8) says that \(I_i,\ldots,I_j\) cover \([s_i,d_j]\).  At each
position of that interval, the word is contained in at least one
\(T_h\subseteq U\), so its OR is contained in \(U\).  Exactness of every
middle row supplies their union \(U\). \(\square\)

## 6. Exact clause reduction and closure domains

The ALO formulation has a direct size formula.  Write

\[
d_S=|\{C:(S,C)\in{\cal D}\}|.
\]

Selectors for \(d_S=1\) may be fixed true and deleted.  Before ordinary unit
simplification, the mandatory-aware direct formulation has

\[
|{\cal D}|-|\{S:d_S=1\}|+\sum_{p\in P}|E_p|             \tag{6.1}
\]

variables and

\[
\begin{aligned}
&|\{S:d_S\ge2\}|+L+\sum_i|T_i|\\
&\quad+\sum_{(S,C)\in{\cal D}}
\left(
|S\setminus M_C|+
\sum_{p\in C}|E_p\setminus S|
\right)                                                  \tag{6.2}
\end{aligned}

clauses.  There are no cardinality auxiliaries.

There is a second exact local choice which can reduce clauses.  For
\(b\in U_C\setminus M_C\), let

\[
h_{C,b}=|\{p\in C:b\in E_p\}|,                          \tag{6.3}
\]

\[
d^+_{C,b}=|\{S:(S,C)\in{\cal D},\ b\in S\}|,qquad
d^-_{C,b}=|\{S:(S,C)\in{\cal D},\ b\notin S\}|.        \tag{6.4}
\]

Direct selector-to-position clauses use

\[
d^+_{C,b}+h_{C,b}d^-_{C,b}                              \tag{6.5}
\]

clauses for this pair.  Alternatively introduce one shared directional OR
bit \(r_{C,b}\), use \(y\Rightarrow r\) on positive providers and
\(y\Rightarrow\neg r\) on negative providers, together with

\[
z_{p,b}\Rightarrow r_{C,b}quad(d^-_{C,b}>0),            \tag{6.6}
\]

\[
r_{C,b}\Rightarrow
\bigvee_{p\in C:\ b\in E_p}z_{p,b}quad(d^+_{C,b}>0).   \tag{6.7}
\]

This uses

\[
d^+_{C,b}+d^-_{C,b}
+h_{C,b}{\bf1}_{d^-_{C,b}>0}
+{\bf1}_{d^+_{C,b}>0}                                   \tag{6.8}
\]

clauses and one extra variable.  Selecting the smaller of (6.5) and (6.8)
independently for each \((C,b)\) is exact.  It is clause-minimal within this
two-encoding family; no claim of globally minimum CNF size is made.

The same geometry gives a bounded-rank lazy alternative.  Suppose middle
rows have length at most \(\rho\), lower cells have length at most \(\ell\),
and at most one cell of each start/length pair is present.  Every failed
integral provider selection has one of the following no-goods:

\[
\begin{array}{c|c|c}
\text{failure}&\text{maximum selected edges}&\text{maximum physical span}\\
\hline
\text{empty position}&
\min\{|E_p|,\ell(\ell+1)/2\}&2\ell-1\\
\text{missing middle bit}&\rho&\rho+2(\ell-1)\\
\text{missing selected-cell bit}&1+\ell&3\ell-2.
\end{array}                                               \tag{6.9}
\]

For an empty position, minimality gives a private surviving coordinate per
selected edge, and only \(1+\cdots+\ell\) catalogue intervals can contain
one position.  For either missing-bit case, an inclusion-minimal interval
cover has a private host position per blocker.  This proves (6.9).  Thus the
common-cap obstruction is a bounded local conflict clutter whenever
\(\rho,\ell\) are bounded, even though the target-cover choice is global.

## 7. The composed construction theorem

### Theorem 7.1 (reroot-retime-compile)

Let \({\cal L}\), \({\cal M}\), and \({\cal U}\) be distinct lower,
middle, and upper target families.  A literal universal word of length \(L\)
exists if the following data are supplied.

1. A block-rerooted chronology listing every target in \({\cal M}\), whose
   new seams are legal and whose interval ORs cover \({\cal U}\), as checked
   by Theorem 2.1.
2. An admissible order-preserving retiming whose maximal envelopes pass
   (1.2), whose cell catalogue is complete for the intended lower witnesses,
   and whose middle intervals satisfy the no-gap condition for the selected
   upper witnesses.
3. Any forced singleton providers are contracted by Theorem 3.2.
4. The residual ALO formula (5.1)--(5.5) is satisfiable.

The decoded \(z\)-letters cover

\[
{\cal L}\cup{\cal M}\cup{\cal U}                       \tag{7.1}
\]

by literal contiguous intervals.  If (7.1) is the set of all nonempty masks,
the word is universal.  If \(L\) also equals an independently proved lower
bound, it is optimal.

#### Proof

Theorem 5.1 gives a nonempty physical word covering all lower and middle
targets.  Corollary 5.2 supplies every required upper target.  Endpoint
rerooting and singleton contraction have already been proved to preserve the
respective antecedents, so no abstract factor or fractional decomposition is
used in the final word. \(\square\)

## 8. Verified K16 instantiation

The genuine four-filter K15 parent has SHA-256

```text
51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4.
```

Its natural K16 chronology was rerooted by reversing the prefix
`[0,6388]` and suffix `[12826,12869]`.  The result is

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

The two endpoint tests are legal, and exact seam-crossing replay supplies
all six upper masks missing from the natural order while losing none.

The successful retiming is

\[
X=\{12870,12871,12872\},\qquad Y=\{0,1,6388\}.           \tag{8.1}
\]

Its selected proper-prefix area is \(32224\).  The exact endpoint
restitution is \(3+2+1\), so (3.4) gives \(32230\) physical lower cells.
The singleton `0x8000` has its unique provider at physical position `6389`
and is contracted there.

The direct common-cap CNF was satisfiable.  Its decoded word is

```text
scratch/k16_optimal_12873_20260731.word
SHA 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe.
```

Independent start-by-start literal replay covers all \(65535\) nonempty
masks.  Together with the deadline lower bound, this proves

\[
\nu(16)=12873.
\]

The certificate and independent replay are frozen in

```text
MATH_CERTIFICATE_K16_OPTIMAL_12873_20260731.md
scratch/k16_trueff_commoncap_direct_cnf_20260731/independent_direct.audit.json
```

As a post-solution encoding audit, the uncapped maximal provider graph with
the forced singleton selector folded has an exact mandatory-aware ALO model
with

```text
408445 variables, 1716050 clauses.
```

The clause-minimum direct/shared choice of (6.5)--(6.8) has

```text
448269 variables, 1584660 clauses, 3619716 literal occurrences.
```

These are construction counts, not a second solve.  They are reproduced by

```text
scratch/audit_ad_k16_true_fourfilter_commoncap_cnf_counts_20260731.py
scratch/ad_k16_true_fourfilter_commoncap_cnf_counts_20260731.audit.json
```

The K16 witness proves that all four antecedents of Theorem 7.1 can hold
simultaneously.  It does not prove that the same reroot, retiming, or ALO
feasibility recurs for other dimensions.

## 9. Sharp remaining general gate

The reusable mechanism has no hidden synchronization assumption.  Its exact
future-dimensional gate is:

> construct an upper-complete block-rerooted middle chronology and an
> admissible retiming whose complete provider catalogue makes the ALO
> common-cap formula satisfiable.

Marginal Hall remains a useful necessary screen but is not sufficient.
Conversely, target/cell AMO constraints are unnecessary once the literal
provider semantics are present.  The unresolved content is the existence of
a satisfying common-cap provider cover, not integrality of an ordinary
matching polytope.
