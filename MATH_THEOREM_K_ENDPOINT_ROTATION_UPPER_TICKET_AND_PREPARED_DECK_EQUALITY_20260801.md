# Endpoint rotation: exact upper-ticket ledger, prepared-deck equality, and the flat-owner cut gate

Date: 2026-08-01  
Lane: K, additive-constant mixed-coatom regeneration  
Status: exact graded cut theorem, exact coatom seam profile, two sufficient
prepared faces, and sharp negative scope.  The rotation creates the desired
`Z|T` host, but endpoint preparation alone can leave a quadratic upper-ticket
debt.  On an exact flat `B` word no internal cut is witness-transparent;
setwise owner reassignment is possible only through an exact lost/new deck
matching.

## 0. Verdict

Let

\[
 W=P\,M\,Q,\qquad W'=M\,Q\,P,                              \tag{0.1}
\]

where

\[
 P=(T,\{f_{d-1}\},\ldots,\{f_2\}),\qquad
 Q=(\{f_{d-1}\},\ldots,\{f_2\},Z).                        \tag{0.2}
\]

The rotation is a two-cut operation.  It opens the old internal cut `P|M`
and closes the old exterior cut `Q|P`.  Every interval internal to `P` or to
`M Q` survives literally.  The complete signed change is

\[
 \operatorname{Suf}(M Q)\star\operatorname{Pre}(P)
 -\operatorname{Suf}(P)\star\operatorname{Pre}(M Q),        \tag{0.3}
\]

with interval length retained as part of the label.  Consequently the exact
survival test is a graded support inclusion, and exact occurrence-deck
preservation is equality of the two crossing multisets.

The new seam is indeed the desired one:

\[
 \ldots,f_3,f_2,Z,T,f_{d-1},f_{d-2},\ldots,f_2.             \tag{0.4}
\]

It supplies both complete coatom rays.  Put

\[
 X=Z\cup T,\qquad E=\{f_2,\ldots,f_{d-1}\}.                \tag{0.5}
\]

Its local cross-grid consists exactly of

\[
 X\cup(E-I),                                                \tag{0.6}
\]

where `I` is an empty or contiguous interval of the ordered filler set `E`.
In particular every newly closed-cut target contains `X`.  Hence every
cut-essential old target omitting `X` needs an unaffected duplicate or an
exterior ticket; it cannot be repaid at `Z|T`.

This obstruction can be maximal.  There are prepared endpoint words for
which the rotation loses exactly

\[
                         \frac{d(d-1)}2                     \tag{0.7}
\]

distinct old targets of deadline at most `d`.  Thus the endpoint wrap is a
valid host mechanism, but it is not a generic bounded-ticket theorem.

The exact positive route is one of the following.

1. Establish the graded prepared-deck inclusion of Theorem 4.1.
2. Give remote duplicate witnesses for every exposed old-cut target.
3. Rotate or rethread before the final owner/compiler assignment, or build
   `M Q P` directly and verify its owner, upper, residence, and common-cap
   rows there.

## 1. Graded interval decks and cut convolution

For a finite word `A`, let

\[
 \mathbf D_\ell(A)
 =\{\!\{\operatorname{OR}(A_i,\ldots,A_{i+\ell-1})\}\!\}   \tag{1.1}
\]

be the multiset of length-`ell` interval values.  Write
`Pre_a(A)` and `Suf_a(A)` for the unions of the first and last `a`
letters.  For typed entries define

\[
                 (a,U)\star(b,V)=(a+b,U\cup V).             \tag{1.2}
\]

For two nonempty words `A,B`, put

\[
 \Gamma_\ell(A,B)=
 \{\!\{\operatorname{Suf}_a(A)\cup\operatorname{Pre}_b(B):
        a,b\ge1, a+b=\ell\}\!\}.                          \tag{1.3}
\]

Only indices within the two block lengths are included.

### Theorem 1.1 (exact signed rotation ledger)

Put `R=M Q`.  For every length `ell`, multiset-disjointly,

\[
\begin{aligned}
 \mathbf D_\ell(P R)
   &=\mathbf D_\ell(P)\uplus\mathbf D_\ell(R)
       \uplus\Gamma_\ell(P,R),\\
 \mathbf D_\ell(R P)
   &=\mathbf D_\ell(P)\uplus\mathbf D_\ell(R)
       \uplus\Gamma_\ell(R,P).                             \tag{1.4}
\end{aligned}
\]

Hence

\[
 \boxed{\mathbf D_\ell(W')-\mathbf D_\ell(W)
       =\Gamma_\ell(MQ,P)-\Gamma_\ell(P,MQ).}              \tag{1.5}
\]

The common physical intervals are exactly those internal to `P` or to
`M Q`.  In particular the seam `M|Q` is unchanged.

If `p=|P|` and `r=|M Q|`, the number of crossing windows on either side at
length `ell` is

\[
 n_\ell(p,r)=
 \left[\min(p,\ell-1)-\max(1,\ell-r)+1\right]_+.           \tag{1.6}
\]

Thus rotation is scalar-neutral at every width.  Every obstruction is a
label, occurrence, cap, or deadline obstruction.

#### Proof

An interval in a concatenation is internal to the first block, internal to
the second block, or is a unique suffix-prefix concatenation.  These three
physical classes are disjoint, proving (1.4)--(1.5).  In (1.3), the first
block contribution `a` ranges from `max(1,ell-r)` through
`min(p,ell-1)`, which gives (1.6).  \(\square\)

Refining the crossing classes at all three blocks gives

\[
\begin{aligned}
 \Gamma(P,MQ)
  ={}&\operatorname{Suf}(P)\star\operatorname{Pre}(M)\\
   &\uplus\operatorname{Suf}(P)\star(|M|,\operatorname{OR}M)
                       \star\operatorname{Pre}(Q),\\
 \Gamma(MQ,P)
  ={}&\operatorname{Suf}(Q)\star\operatorname{Pre}(P)\\
   &\uplus\operatorname{Suf}(M)\star(|Q|,\operatorname{OR}Q)
                       \star\operatorname{Pre}(P).          \tag{1.7}
\end{aligned}
\]

Here the second line in each decomposition uses a nonempty part of the
third block, so there is no double counting.

## 2. Exact targetwise and occurrence-labelled ticket conditions

Fix a protected typed target `(ell,U)` with required multiplicity
`d_ell(U)`.  Let

* `b_ell(U)` be the number of certified unchanged or remote admissible
  witnesses;
* `c^-_ell(U)` be its multiplicity in `Gamma_ell(P,MQ)`;
* `c^+_ell(U)` be its multiplicity in `Gamma_ell(MQ,P)`.

The old word is assumed feasible.

### Theorem 2.1 (exact upper-ticket ledger)

The rotated word satisfies every protected typed demand if and only if

\[
                  b_\ell(U)+c^+_\ell(U)\ge d_\ell(U)        \tag{2.1}
\]

for every protected `(ell,U)`.

For ordinary one-copy coverage, let `B_ell` be the support of the unchanged
or remote bank.  The exact new hole set is

\[
 \boxed{
 H_\ell=
  \bigl(\operatorname{supp}\Gamma_\ell(P,MQ)\cap\mathcal U_\ell\bigr)
  -\bigl(B_\ell\cup\operatorname{supp}\Gamma_\ell(MQ,P)\bigr).}
                                                               \tag{2.2}
\]

Thus the minimum number of unconstrained targetwise tickets is
`sum_ell |H_ell|`.  If tickets have owner, phase, cap, orientation, or
common-`Q` restrictions, join each exposed demand to its admissible
unchanged/new occurrences.  Preservation is then exactly Hall in that
bipartite graph.  Equation (2.1) is the label-only special case.

#### Proof

Theorem 1.1 lists every post-rotation occurrence: the common bank and the
new crossing bank.  Counting admissible occurrences proves (2.1), and
specializing to demand one gives (2.2).  With occurrence restrictions, one
physical interval can serve only one selected demand, so the remaining
condition is precisely a system of distinct representatives.  \(\square\)

Ungraded OR support is insufficient here: a target repaid one position too
late does not preserve a fixed upper-shadow deadline.

## 3. The explicit coatom cut profile

Put `r=d-1` and, for `0<=i<=r-1`, define

\[
 L_i=\{f_2,\ldots,f_{i+1}\},\qquad
 H_i=\{f_{d-i},\ldots,f_{d-1}\},                           \tag{3.1}
\]

with `L_0=H_0=emptyset`.  Directly from (0.2),

\[
\begin{aligned}
 \operatorname{Pre}_i(P)&=T\cup H_{i-1},\\
 \operatorname{Suf}_i(P)&=
  \begin{cases}L_i,&i<r,\\T\cup E,&i=r,\end{cases}\\
 \operatorname{Pre}_i(Q)&=
  \begin{cases}H_i,&i<r,\\Z\cup E,&i=r,\end{cases}\\
 \operatorname{Suf}_i(Q)&=Z\cup L_{i-1}.                  \tag{3.2}
\end{aligned}
\]

If `Z=A union {f_1}` and `T=B union {f_d}`, the suffixes of `Q` and prefixes
of `P` are exactly

\[
 A\cup\{f_1,\ldots,f_i\},qquad
 B\cup\{f_{d-i+1},\ldots,f_d\},                           \tag{3.3}
\]

so the two desired flags are present at the new seam.

Let

\[
 U_j=\operatorname{Pre}_j(M),\qquad
 V_j=\operatorname{Suf}_j(M),\qquad C=\operatorname{OR}(M).\tag{3.4}
\]

The old crossing families are

\[
\begin{aligned}
 \mathcal O_1&=
  \{\operatorname{Suf}_i(P)\cup U_j\},\\
 \mathcal O_2&=
  \{\operatorname{Suf}_i(P)\cup C\cup\operatorname{Pre}_j(Q)\},
                                                               \tag{3.5}
\end{aligned}
\]

with their physical lengths `i+j` and `i+|M|+j`.  The new families are

\[
\begin{aligned}
 \mathcal N_1
   &=\{X\cup L_{i-1}\cup H_{j-1}:1\le i,j\le r\},\\
 \mathcal N_2
   &=\{V_j\cup X\cup E:1\le j\le |M|\}.                   \tag{3.6}
\end{aligned}
\]

The value in `N_2` is independent of how far the interval enters `P`,
because traversing all of `Q` already supplies `Z union E`.  The physical
lengths are `i+j` in `N_1`; in `N_2`, a suffix of `M` of length `j`, all
`r` letters of `Q`, and a prefix of `P` of length `i` give length `j+r+i`,
for `1<=i<=r`.

### Corollary 3.1 (interval-hole seam and the `X` screen)

The support of `N_1` is

\[
 \boxed{\{X\cup(E-I): I\text{ is empty or a contiguous interval of }E\}.}
                                                               \tag{3.7}
\]

It has

\[
                   1+\frac{(d-2)(d-1)}2                     \tag{3.8}
\]

distinct values.  Every value of `N_1 union N_2` contains `X`.

Therefore an exposed old crossing target which omits any coordinate of `X`
cannot be repaid at the new cut.  If it contains `X` but not all of `E`, its
filler complement must be one interval as in (3.7).  If it contains
`X union E`, its remaining excess must be supplied by one suffix value
`V_j` as in `N_2`.

#### Proof

The low prefix `L_(i-1)` and high suffix `H_(j-1)` cover `E` except for the
possibly empty interval between them.  Every interval occurs once as the
gap, while the empty gap has several physical representations.  This gives
(3.7)--(3.8).  Both new families visibly contain `Z union T=X`.  \(\square\)

For a deadline `h`, let `D_<=h` be the common internal deck through length
`h`, and restrict (3.5)--(3.6) to their displayed lengths at most `h`.  The
exact casualty set is

\[
 \boxed{
 \Delta_h=(\mathcal O_{1,\le h}\cup\mathcal O_{2,\le h})
 - (\mathcal D_{\le h}\cup\mathcal N_{1,\le h}
                         \cup\mathcal N_{2,\le h}).}         \tag{3.9}
\]

Every old target of deadline `h` survives if and only if `Delta_h` is empty,
or, with an exterior return bank `R_<=h`, iff
`Delta_h subseteq R_<=h`.

## 4. Prepared-deck equality and two concrete sufficient faces

### Theorem 4.1 (prepared rotation theorem)

The complete length-graded interval multidecks of `P M Q` and `M Q P` are
equal if and only if

\[
 \boxed{\Gamma_\ell(P,MQ)=\Gamma_\ell(MQ,P)
                    \quad\text{for every }\ell.}            \tag{4.1}
\]

For target coverage rather than occurrence multiplicity, the exact weaker
condition is

\[
 \boxed{
 \operatorname{supp}\Gamma_\ell(P,MQ)
  \subseteq \operatorname{supp}\mathbf D_\ell(P)
       \cup\operatorname{supp}\mathbf D_\ell(MQ)
       \cup\operatorname{supp}\Gamma_\ell(MQ,P)
       \quad(\forall\ell).}                                \tag{4.2}
\]

The corresponding deadline version replaces each exact length by the union
of lengths at most the declared deadline.  These conditions are necessary
and sufficient; they are not scalar seam counts.

#### Proof

Cancel the two common multidecks in (1.4).  This proves (4.1).  For support,
an old crossing label needs either a common internal occurrence or a new
crossing occurrence, which is exactly (4.2).  \(\square\)

The theorem has two useful strong sufficient faces.

### Proposition 4.2 (interval-hole prefix face)

Suppose every prefix of `M` has the form

\[
                  U_j=X\cup H_{\alpha_j},qquad
                  0\le\alpha_j\le d-2.                     \tag{4.3}
\]

Then every old crossing value belongs to the new `Q|P` support (3.7), so
the ungraded old deck is preserved.  For a proper suffix `i<r`, an old
`O_1` occurrence of length `i+j` is repaid at length

\[
                         i+\alpha_j+2.                      \tag{4.4}
\]

Thus no deadline increase follows from `alpha_j<=j-2`; a one-position
staircase follows from `alpha_j<=j-1`.  The full suffix gives `X union E`
and has a length-`d` new-seam witness, no longer than its old occurrence.
In particular the proper-suffix `j=1` row cannot be repaid with zero delay
on this face.

### Proposition 4.3 (saturated remote-duplicate face)

If

\[
                  T\cup E\subseteq U_1,\qquad
                  Z\cup E\subseteq C,                      \tag{4.5}
\]

then every old `O_1` value is exactly the internal prefix `U_j`, and every
old `O_2` value is exactly the internal value `C`.  Hence the rotation has
zero old-target loss with nonincreasing deadlines.

Both faces are literal but strong.  Already direct repayment of the smallest
old seam target through `Q|P` forces

\[
                         X\subseteq\{f_2\}\cup U_1.         \tag{4.6}
\]

Under the canonical disjointness of `X` and `f_2`, this says `X subseteq
U_1=M_1`: direct seam equality reintroduces merged-host containment in the
first middle letter.  Avoiding that host requires remote duplicates or a
different prepared deck.

## 5. Endpoint preparation alone has quadratic ticket debt

### Theorem 5.1 (full crossing-triangle counterexample)

Take fresh singleton letters `mu_1,...,mu_s`, with `s>=d`, and put

\[
                    M=(\{\mu_1\},\ldots,\{\mu_s\}),         \tag{5.1}
\]

all disjoint from `T,Z,E`.  For

\[
                  1\le i\le d-1,\qquad1\le j\le d-i,      \tag{5.2}
\]

the old suffix-`i`, prefix-`j` target

\[
 S_{i,j}=\operatorname{Suf}_i(P)
             \cup\{\mu_1,\ldots,\mu_j\}                    \tag{5.3}
\]

has deadline at most `d`.  These `d(d-1)/2` targets are pairwise distinct
and all disappear after rotation.  Consequently

\[
                         |\Delta_d|=\frac{d(d-1)}2.         \tag{5.4}
\]

#### Proof

Every new cut-crossing interval contains `X`, while (5.3) omits `Z` and
hence omits `X`.  The deck of `P` contains no `mu` label.  An interval in
`M Q` containing `mu_1` and any filler must traverse all later middle
singletons; since `j<s`, it also contains `mu_(j+1)` and cannot equal
(5.3).  An interval internal to `M` has no filler or `T`.  Thus no common or
new interval realizes (5.3).  The constraints (5.2) enumerate all old
cut-crossing intervals of deadline at most `d`, and their independent
prefix/suffix labels make their unions distinct.  Summing `d-i` proves
(5.4).  \(\square\)

A fixed common core can be adjoined to every letter, so this is equally an
upper-rank last-witness example.  It proves that a constant number of
ordinary targetwise tickets cannot be inferred from the prepared endpoint
rays.  A single compound rectangle relation may encode the triangle, but
its literal simultaneous realization is an additional theorem.

## 6. Flat `B+C` owner windows: exact cut count and the right no-go

Let a flat source word have length

\[
                         L=W+d+C,                           \tag{6.1}
\]

so it has `W+C` length-`d+1` owner windows and covers `W` distinct owners.
Cut after `c` source positions, `1<=c<=L-1`, and cyclically rotate there.

### Lemma 6.1 (changed owner-window count)

For a general length-`h<L` row, the number of old windows which cross the
internal cut, and equally the number of new wrap windows, is

\[
              x_h(c)=\min(h-1,c,L-c,L-h+1).                 \tag{6.2}
\]

For the owner row `h=d+1`, one has `L-h+1=W+C>=d` in the Boolean regime,
so this simplifies to

\[
                         x(c)=\min(d,c,L-c).                 \tag{6.3}
\]

#### Proof

An old window beginning at `s` crosses the cut exactly when

\[
             \max(0,c-d)\le s\le\min(c-1,L-d-1).
\]

Counting this interval gives the first formula (equivalently, its four
possible boundary limitations).  The stated Boolean owner-row inequality
gives (6.3).  Cyclic rotation exchanges the two cuts,
so the gained bank has the same size.  \(\square\)

### Theorem 6.2 (witness-transparent cut obstruction)

Suppose every owner must retain an old occurrence avoiding the cut; newly
closed-wrap windows are not allowed to reassign owner witnesses.  Then

\[
                              x(c)\le C.                    \tag{6.4}
\]

If `C<d`, the cut must therefore satisfy

\[
                         c\le C\quad\text{or}\quad L-c\le C.\tag{6.5}
\]

In particular, on an exact flat `B` word (`C=0`) no nontrivial internal cut
is occurrence-transparent.

#### Proof

After deleting the `x(c)` crossing occurrences, only
`W+C-x(c)` old owner windows remain.  They cannot cover `W` distinct owners
unless (6.4) holds.  Equation (6.5) follows from (6.3).  \(\square\)

This is the sharp conclusion supplied by counting.  The stronger statement
that no cyclic recut can preserve the owner **set** is false without another
structural hypothesis.  At `C=0`, setwise preservation is possible exactly
when the `x(c)` new wrap values are pairwise distinct and equal the lost
owner set.  That is the owner-width instance of (4.1).

Here is the smallest explicit flat-row counterexample.  With `d=1`, take

\[
 (\{1,2,3\},\{1,2\},\{1,4\},\{3,4\},\{2,3\}).             \tag{6.6}
\]

Its four length-two unions are

\[
                 123,124,134,234,                           \tag{6.7}
\]

all rank-three subsets of `[4]`.  Moving the first source to the end gives

\[
 (\{1,2\},\{1,4\},\{3,4\},\{2,3\},\{1,2,3\}),             \tag{6.8}
\]

whose length-two unions are `124,134,234,123`.  Thus a nontrivial exact-`B`
recut can preserve the owner set by reassignment even though it preserves no
named crossing occurrence.

Consequently full-language safe rotation is not the generic induction
theorem.  A valid positive use must either prove the exact lost/new
owner-and-upper matching at every protected width, or perform the rotation
before final owner/compiler assignment and verify the constructed `M Q P`
chronology directly.

## 7. Scope

The results prove the precise role of the global wrap.

* It supplies the missing physical adjacency `Z|T` and both coatom flags at
  zero change of source length.
* It does not by itself preserve owners, upper shadows, residence, topology,
  or common caps.
* Contracting `Z,T` to `X` is a second operation.  It preserves intervals
  containing both letters but can destroy targets whose only witnesses use
  exactly one side; those rows require a separate contraction-safe ledger.
* A protected full-deck cut is generally too strong at exact `B` length.
  The viable recursive formulation is a prepared lost/new matching, or a
  direct construction in the rotated chronology followed by owner/compiler
  assignment.

The exact remaining positive theorem is therefore:

> Construct a Pascal child directly in `M Q P` order (or a simultaneous
> lost/new return matching) so that the coatom seam (0.4), the flat or
> explicitly nonflat owner row, every protected upper deadline, residence,
> and the final common-cap matching coexist.

Endpoint-ray preparation alone proves only the seam supply, not this joint
statement.

## 8. Audit

The dependency-free replay

```text
python3 scratch/audit_k_endpoint_rotation_prepared_deck_20260801.py
```

checks 7,938 exhaustive small-word block rotations, 18,278 cut-count cases,
the coatom interval-hole grid for `2<=d<=32`, the full crossing-triangle
loss for `2<=d<=16`, and the flat setwise-recut counterexample.  It reports

```text
PASS_K_ENDPOINT_ROTATION_PREPARED_DECK
```

with canonical payload SHA-256

```text
7c45bdee7cd53a14255fcc38066e96bde7c78b5b3988c5f1cf1de56c57272fda
```

and frozen summary

```text
scratch/k_endpoint_rotation_prepared_deck_20260801.audit.json
```
