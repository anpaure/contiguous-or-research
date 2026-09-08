# Cap-backup/history-ticket monoid for protected heptagonal and Pascal packets

**Date:** 2026-08-02  
**Status:** unconditional cap-prefix algebra, exact one-edge bi-history ticket
criterion, and a prospective bounded-bank packing lemma.  This note does not
prove that a Pascal, pull-ear, or heptagonal host contains the required
retained paths.  It separates that host-existence problem from the already
proved central `C14` supply.

## 0. Outcome

The cap and residence rows admit one exact compositional state.

For a packet word `P`, let `z_P(U)` be its final signed multiplicity change
at upper cap `U`, and let `b_P(U)` be the largest cap debt reached at any
prefix of the word.  Let `R_P` be its bidirectional boundary-history
relation.  Then

\[
 (z_A,b_A,R_A)(z_B,b_B,R_B)
 =\bigl(z_A+z_B,\ \max\{b_A,b_B-z_A\},\ R_B\circ R_A\bigr).
 \tag{0.1}
\]

All vector operations in the middle coordinate are pointwise.  This is an
associative monoid.  A host with cap slack `s(U)=m(U)-1` supports every
prefix exactly when `s>=b_P`, and the history row closes exactly when the
composed relation has the required cyclic fixed point.  Neither condition
implies the other.

For one cap `U`, a literal backup adjacency has the form

\[
 U-\alpha\longrightarrow U-\beta,
 \qquad \alpha\ne\beta,                                  \tag{0.2}
\]

so its Johnson transition deletes `beta`, inserts `alpha`, and has upper
cap exactly `U`.  Once the two boundary collars are fixed, its complete
positive-and-negative residence test reduces to two cross-collar tests and
two forbidden-label sets.  Its exact oriented menu size is given in
Theorem 3.1.  In the central regime it is `Theta(k^2)` whenever those
cross-collar tests pass.

Thus the new bottleneck is not raw `C14` supply.  It is the simultaneous
planting of:

1. the bounded cap-debt vector `b_P` into the global repeat budget;
2. literal, resource-disjoint backup adjacencies carrying the required
   bidirectional history tickets; and
3. the retained ears/topology which make the packet and its backups part of
   one physical factor.

Items 1 and the local part of item 2 are closed below.  Item 3 remains a
host theorem.

## 1. Exact cap-prefix debt

Let `C` be a finite set of literal upper caps.  An atomic packet step `j`
removes `r_j(U)` occurrences of `U` and adds `a_j(U)` occurrences.  Put

\[
 \delta_j(U)=a_j(U)-r_j(U),\qquad
 Z_t(U)=\sum_{j=1}^t\delta_j(U),\qquad Z_0(U)=0.          \tag{1.1}
\]

We assume each step is a factor exchange, so
`sum_U delta_j(U)=0`.

Define the **prefix backup demand**

\[
 b_P(U)=\max_{0\le t\le |P|}\bigl(-Z_t(U)\bigr)
       =-\min_{0\le t\le |P|} Z_t(U).                  \tag{1.2}
\]

The zero prefix makes `b_P(U)>=0`.

### Theorem 1.1 (minimal duplicate-cap bank)

Suppose the initial cap multiplicity is

\[
                         m(U)=1+s(U),\qquad s(U)\ge0.   \tag{1.3}
\]

Every prefix of `P` retains upper-cap support if and only if

\[
                              s(U)\ge b_P(U)             \tag{1.4}
\]

for every cap `U`.  Consequently `b_P` is the unique coordinatewise
minimal duplicate-cap bank protecting every prefix.

If only the terminal factor is required to retain support, the minimal
bank is instead

\[
                         b_P^{\rm fin}(U)=(-Z_{|P|}(U))_+ .
 \tag{1.5}
\]

#### Proof

After prefix `t`, the load of `U` is `1+s(U)+Z_t(U)`.  It is positive for
every `t` exactly when `s(U)>=-Z_t(U)` for every `t`, which is (1.4).
Taking only `t=|P|` gives (1.5).  Minimality is coordinatewise.  \(\square\)

The distinction between (1.2) and (1.5) is important.  If a compound
packet is performed as one simultaneous factor exchange, only its final
delta is physical.  Decomposing it into conceptual primitives and requiring
upper support after each conceptual primitive can introduce an artificial
prefix debt.

### Theorem 1.2 (cap-debt composition law)

For packet words `A,B` applied in that order,

\[
\begin{aligned}
 z_{AB}&=z_A+z_B,\\
 b_{AB}&=\max\{b_A,b_B-z_A\} .                          \tag{1.6}
\end{aligned}
\]

The operation `(z,b)(z',b')=(z+z',max(b,b'-z))` is
associative and has identity `(0,0)`.

#### Proof

Prefixes of `AB` are either prefixes of `A`, whose largest debt is `b_A`,
or all of `A` followed by a prefix of `B`.  At the latter prefixes the cap
change is `z_A+Z_t^B`, so their largest debt is

\[
             \max_t(-z_A-Z_t^B)=b_B-z_A.
\]

Taking the pointwise maximum proves (1.6).  Associativity follows either by
expanding both parenthesizations or, more conceptually, because both compute
the same prefix minima of the concatenated word.  \(\square\)

### Corollary 1.3 (balanced repeat-budget criterion)

Suppose there are `M` cap occurrences and `N=|C|` cap values, so the total
repeat budget is

\[
                              R=M-N.                    \tag{1.7}
\]

Ignoring physical owner/facet realization, there exists a cap-surjective
initial load vector of total mass `M` which protects every prefix of `P` if
and only if

\[
                         \sum_{U\in C} b_P(U)\le R.     \tag{1.8}
\]

#### Proof

Necessity follows by summing `s(U)>=b_P(U)` and
`sum_U s(U)=R`.  For sufficiency, start with `s=b_P` and distribute the
remaining `R-sum b_P` indistinguishable repeat units arbitrarily.  \(\square\)

This is an abstract multiplicity theorem, not a physical factor theorem.
For a quotient with nonfree cap orbits one must apply it to literal physical
cap occurrences, or use the corresponding orbit-size weights.  Unweighted
quotient counts are not proof-safe in that setting.

### Corollary 1.4 (the heptagonal calibration)

The phasewise fixed-label heptagon of
`MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`
has `z=0,b=0`.  A one-step nonzero-holonomy `C14` which replaces three cap
values and returns all other cap values has

\[
 b(U)=1
\]

on its three net-removed caps and zero elsewhere.  Hence three repeat units
are necessary and sufficient at the multiplicity level.  The authenticated
`k=17` 2,822-to-2,754 packet has exactly this signature: its three removed
cap orbits have load two.  This certifies the minimal scalar backup count;
it does not prove a uniform way to plant those three duplicates.

## 2. Cap state and directed-history state form a product monoid

Let `R_P` be the exact bidirectional boundary-history relation of a directed
packet or ear.  It contains both the positive insertion history and the
negative deletion history, with phase/frame transport where required.  For
concatenable packets,

\[
                              R_{AB}=R_B\circ R_A.       \tag{2.1}
\]

### Theorem 2.1 (protected cap-history signature)

The triples

\[
                           \Sigma(P)=(z_P,b_P,R_P)       \tag{2.2}
\]

form an associative monoid under (0.1).  Given a literal host chronology,
the cap and residence rows for a cyclic packet word are accepted exactly
when

1. its initial cap slack satisfies `s>=b_P`; and
2. `R_P` has a consistent cyclic fixed state.

For an opened path, item 2 is replaced by membership of the prescribed
input/output histories in `R_P`.

#### Proof

The cap coordinates compose by Theorem 1.2, and history relations compose
associatively by ordinary relational composition.  The two acceptance
conditions are respectively Theorem 1.1 and the exact directed-history
path/cycle theorem.  \(\square\)

This is the exact state to carry through a protected Pascal or pull-ear
recurrence.  A history-reset pivot can make `R_P` constant-output, but it
does not reset `b_P`.  Conversely a cap-exact heptagon can have `b_P=0`
while its retained-path history relation has no accepting state.  Thus
history regeneration and duplicate-cap regeneration are genuinely
orthogonal.

For a fixed-history pull system `G_h`, `R_P` reduces to the identity on the
chosen history state and event costs become additive.  The cap coordinate
still follows (1.6); a prepared-tree exchange is cap-safe only when its
selected edge word fits the available `b` bank or returns cap delta
simultaneously.

## 3. Literal backup adjacency with exact bi-history collars

Let `U` be a rank-`(r+1)` cap and put `n=|U|=r+1`.  Choose distinct
`alpha,beta in U`.  The directed adjacency

\[
       U-\alpha\longrightarrow U-\beta                  \tag{3.1}
\]

deletes `beta`, inserts `alpha`, has lower facet
`U-{alpha,beta}`, and has upper cap exactly `U`.

At its left boundary let

* `H_I=(i_1,...,i_d)` be the recent insertions, newest first;
* `H_D=(u_1,...,u_d)` be the recent deletions, newest first.

At its right boundary let

* `F_D=(j_1,...,j_d)` be the forthcoming deletions;
* `F_I=(v_1,...,v_d)` be the forthcoming insertions.

These are literal physical-coordinate labels.  For shorter ears the full
history relation, rather than just these collars, must be used.

### Theorem 3.1 (exact two-sided ticket criterion and menu size)

Assume the adjacent retained ears are internally positive- and
negative-resident.  Then a ticket (3.1) realizes the displayed collars and
is resident across both joins if and only if all three of the following
conditions hold.

First, the positive `present` collars lie inside the cap and the negative
`absent` collars lie outside it:

\[
 \{i_1,\ldots,i_d,j_1,\ldots,j_d\}\subseteq U,
 \qquad
 \{u_1,\ldots,u_d,v_1,\ldots,v_d\}\cap U=\varnothing . \tag{3.2}
\]

Second, the two missing endpoint labels avoid both positive collars:

\[
 \alpha,\beta\in
 W_U:=U\setminus\{i_1,\ldots,i_d,j_1,\ldots,j_d\},
 \qquad \alpha\ne\beta .                               \tag{3.3}
\]

Third, the two exterior cross-collar conditions hold:

\[
\begin{aligned}
 i_p&\ne j_q &&(p+q\le d),\\
 u_p&\ne v_q &&(p+q\le d).                               \tag{3.4}
\end{aligned}
\]

Consequently the number of oriented backup adjacencies of cap `U` carrying
these fixed collars is exactly

\[
 \boxed{
 N_U=|W_U|(|W_U|-1)}                                    \tag{3.5}
\]

when (3.2) and (3.4) hold, and is zero otherwise.  If `n>=2d+1`, in
particular

\[
                         N_U\ge(n-2d)(n-2d-1).          \tag{3.6}
\]

If either (3.2) or (3.4) fails, no choice of `alpha,beta` can repair that
failure with one connector.

#### Proof

On a resident path, each of the last `d` inserted labels is still present
at the left endpoint and each of the last `d` deleted labels is absent.
Similarly, every one of the next `d` deletions is already present at the
right endpoint and every one of the next `d` insertions is absent.  The two
endpoints in (3.1) differ from `U` only at `alpha` and `beta`.

Endpoint consistency alone therefore says that the positive collars lie in
`U` except possibly at the corresponding missing endpoint, and that the
negative collars avoid `U` except possibly there.  The connector event adds
the remaining exclusions: deleting `beta` forbids `beta` from the recent
insertion collar; inserting `alpha` forbids `alpha` from the future deletion
collar; the dual conditions forbid `alpha` from the recent deletion collar
and `beta` from the future insertion collar.  Combining endpoint consistency
with these four event guards gives exactly (3.2)--(3.3).  Old
insertion-to-future-deletion and deletion-to-future-insertion pairs crossing
the connector give (3.4).

Once (3.2) and (3.4) hold, the ordered pair `(alpha,beta)` may be any two
distinct elements of `W_U`, proving (3.5).  Since the two positive collars
contain at most `2d` distinct labels, `|W_U|>=n-2d`, proving (3.6).  The
failed conditions do not depend on the missing-pair choice and hence cannot
be repaired by one such connector.  \(\square\)

This theorem is a literal address theorem, not merely a set-identity
calculation.  It also identifies a sharp obstruction: a huge cap menu is
irrelevant when the cap does not separate the boundary present/absent
labels as in (3.2), or when the retained ears violate one of the crossing
history inequalities.

## 4. A bounded prospective backup bank

A backup ticket consumes the two owner resources `U-alpha,U-beta` and the
facet `U-{alpha,beta}`.  Protecting these resources is stronger than merely
preserving cap support, but it is the useful private-bank face for a
recursive construction.

### Lemma 4.1 (literal conflict bounds)

For a fixed cap `U`:

1. a fixed rank-`r` owner occurs in at most `2(n-1)` oriented tickets;
2. a fixed rank-`(r-1)` facet occurs in at most two oriented tickets; and
3. one previously selected ticket excludes at most

   \[
                              4(n-1)+2                  \tag{4.1}
   \]

   further oriented tickets by owner/facet overlap.

#### Proof

An owner contained in `U` is `U-gamma` for a unique `gamma`.  It can be the
source when `alpha=gamma` or the target when `beta=gamma`, leaving at most
`n-1` choices in each case.  A facet contained in `U` determines the
unordered pair `{alpha,beta}`, hence the two orientations.  A selected
ticket has two owners and one facet.  \(\square\)

### Proposition 4.2 (exact backup-bank selector)

Expand the demand vector `b` into labelled units

\[
                    \mathcal D_b=\{(U,j):1\le j\le b(U)\}. \tag{4.2}
\]

For each demand unit, make one vertex for every ticket satisfying Theorem
3.1 and the declared protected-resource exclusions.  Join two vertices when
they belong to the same demand unit or when their owner/facet resources
intersect.  Then a literal private backup bank realizing `b` exists if and
only if this conflict graph has an independent set of size
`|\mathcal D_b|`.

#### Proof

The clique on each demand menu forces an independent set to choose at most
one ticket per unit.  An independent set of total size `|\mathcal D_b|`
therefore chooses exactly one from every menu, and the remaining conflict
edges say precisely that all selected owner/facet resources are disjoint.
The converse is immediate.  \(\square\)

For one cap, the underlying resource condition is an ordinary matching on
the missing-coordinate labels.  Across several caps, owners and facets can
couple different coordinate sets, so the exact selector is not in general
reduced to the scalar inequality (1.8) or to one ordinary Hall row.

### Theorem 4.3 (greedy bounded-bank planting)

Suppose `t` demanded backup units have prescribed cap values and prescribed
two-sided collars satisfying (3.2) and (3.4).  Let a protected ambient bank contain
`A_0` owner resources and `F_0` facet resources.  If every demand has ticket
menu size at least `L` and

\[
 L>
 2A_0(n-1)+2F_0+(t-1)\bigl(4(n-1)+2\bigr),             \tag{4.3}
\]

then there is a literal selection of all `t` tickets whose owners and
facets are pairwise disjoint and avoid the ambient bank.

#### Proof

Order the demands arbitrarily.  Before selecting demand `j`, the protected
bank deletes at most `2A_0(n-1)+2F_0` options by Lemma 4.1, and the preceding
`j-1` tickets delete at most `(j-1)(4(n-1)+2)`.  Inequality (4.3) leaves an
option.  Greedy induction proves the claim.  \(\square\)

Combining (3.6) and (4.3), a fixed number of cap backups has a prospective
private ticket bank in the central regime when `d=o(r)` and the protected
ambient boundary has `o(r)` owner/facet resources.  For `d=Theta(sqrt k)`
this is automatic for every fixed `t` once both the cap-separation and
cross-collar conditions are supplied.

What Theorem 4.3 does **not** prove is that these isolated adjacencies can be
inserted into the selected degree-two factor, that their endpoints lie on
the required retained ears, or that the resulting path permutation has the
required topology.  Those are exactly the joint host rows.

## 5. Consequence for the protected Pascal/pull-ear recurrence

The proof-safe exported state is at least

\[
 \boxed{
  (\text{payload and port state};\ z,b,R^+,R^-;
   \text{opening/topology state}).}                     \tag{5.1}
\]

The ordinary private Pascal rectangle updates its port/payload coordinates;
the cap coordinates update by (1.6); and the two directed-history relations
compose.  A pivot reset can collapse the output history to one ordered
`d`-tuple, but its triangular input guard and the cap-debt coordinate remain.
Two fresh children can reset two boundary-history coordinates only when the
crossed connectors satisfy Theorem 3.1.  They do not erase cap debt unless
their signed cap changes cancel or the required backup occurrences are
carried into the parent.

The same statement applies to a prepared pull-ear tree.  A two-pull exchange
inside one fixed-history graph has a linear history cost, but cap safety is
still governed by the prefix debt of the **actual simultaneous packet**.
Overlapping pulls must be replayed as their final symmetric difference;
adding per-pull debts can overcount or undercount.

### Exact remaining host lemma

For each bounded private task, choose jointly:

1. a rooted heptagonal or Pascal/pull packet with its literal retained ears;
2. a cap-load allocation with slack at least its combined `b` vector;
3. a private backup-ticket matching satisfying Theorem 3.1 and Proposition
   4.2 (with Theorem 4.3 as a bounded-bank sufficient condition);
4. a bidirectional history fixed point or prescribed open relation;
5. a factor-degree/topology embedding which uses the packet and backup
   tickets simultaneously.

The already proved `Theta(k^7)` rooted `C14` count and `O(k^6)` nonanchor
central load address only item 1 before the retained-ear/history filter.
Theorems 1.1--4.3 close the scalar backup ledger and the local addressed
history tickets.  They do not imply item 5 and therefore do not constitute
an all-`k` host-existence or regeneration theorem.

Two sharp obstructions survive:

* if `sum b` exceeds the global repeat budget, no host geometry can help;
* if a required cap/ear pair fails (3.2) or (3.4), no one-edge same-cap
  backup can join it, regardless of the size of the central heptagon atlas.

Upper shadows beyond immediate caps, source/erosion, the terminal common-cap
compiler, and the final word-length recurrence remain separate gates.
