# The twelve-move `D_3` whole-factor phase path leaves an exact 22-ray suffix current

**Date:** 2026-08-06  
**Method:** pure mathematics; exact interval decomposition  
**Status:** unconditional current theorem.  It computes the complete proper
lower, and hence complementary upper, current of the canonically
suffix-suspended twelve-move path from the negative pentagon factor to the
positive pentagon factor.  The base endpoint current cancels, but the deeper
current does not.  In the capacity-one nested-ray model, the generic residual
has exactly twenty-two positive channels.  A one-cell two-ray pivot cannot
absorb it.  The note does **not** construct the required protected 22-channel
battery or common-cap host.

## 1. Canonical common-suffix suspension

Let

\[
             U=(u_1,\ldots,u_s),\qquad
             V=(v_1,\ldots,v_s),\qquad
             W=(v_1,\ldots,v_s,\infty),              \tag{1.1}
\]

where all displayed labels are distinct.  Put \(m=s+3\).  If a base row,
opened at `infinity`, is

\[
             w=(d_1,d_2,d_3,i_1,i_2,i_3,\infty),
\]

its canonical common-suffix suspension is the cyclic word

\[
 \widehat w=
 (d_1,d_2,d_3,u_1,\ldots,u_s,
  i_1,i_2,i_3,v_1,\ldots,v_s,\infty).                \tag{1.2}
\]

Thus every suspended row has the block form

\[
                            D\mid U\mid I\mid W,      \tag{1.3}
\]

with \(|D|=|I|=3\), \(|U|=s\), and \(|W|=s+1\).

Let \(\widehat{\mathcal P^-}\) and
\(\widehat{\mathcal P^+}\) be obtained from the two five-row pentagon
factors by (1.2).  The explicit twelve native moves in
`MATH_THEOREM_D3_WHOLE_FACTOR_NATIVE_ORBIT_AND_REOPENING_GATE_20260806.md`
start at the former base factor and end at the latter.  Therefore their total
suspended current, whether or not the intermediate moves suspend natively, is
the palette difference

\[
        \Delta=\operatorname{Pal}(\widehat{\mathcal P^+})
              -\operatorname{Pal}(\widehat{\mathcal P^-}).   \tag{1.4}
\]

For a signed base current
\(A=\sum_S a_S[S]\) and a fresh set \(Z\), write

\[
                         Z\star A:=\sum_S a_S[Z\cup S].       \tag{1.5}
\]

Write \(U_t^-\), \(U_t^+\), \(W_t^-\), and \(W_t^+\) for the
prefixes and suffixes of the indicated ordered banks, with the empty set at
\(t=0\).

## 2. The eight base boundary currents

For each row, split its six base labels as \(D=(d_1,d_2,d_3)\) and
\(I=(i_1,i_2,i_3)\).  Comparing the positive and negative pentagon phases
gives the following exact prefix/suffix currents:

\[
\begin{array}{c|c|c}
\text{boundary piece}&q=1&q=2\\ \hline
D\text{-prefix}&A&C\\
D\text{-suffix}&B&D\\
I\text{-prefix}&A&E\\
I\text{-suffix}&B&F,
\end{array}                                                   \tag{2.1}
\]

where

\[
\begin{aligned}
A={}&2[3]+[5]-2[2]-[4],\\
B={}&2[4]+[2]-2[5]-[3],\\
C={}&[15]+[35]-[14]-[24],\\
D={}&[24]+[25]+[14]-[15]-[35]-[34],\\
E={}&[35]+[36]+[25]-[34]-[24]-[26],\\
F={}&[24]+[26]-[35]-[36].                            \tag{2.2}
\end{aligned}

At the unique interval which crosses the whole \(U\)-bank from the final
deletion label to the first insertion label, the base current is

\[
                              G=[34]-[25].             \tag{2.3}
\]

### Lemma 2.1

Equations (2.1)--(2.3) are the exact aggregate base currents.

#### Proof

Read the first one or two entries, and the last one or two entries, of the
\(D\) and \(I\) blocks in the five rows of the two displayed pentagon
factors.  For example, the first deletion labels in the positive phase are

\[
                         3,1,1,5,3,
\]

whereas in the negative phase they are

\[
                         2,4,2,1,1.
\]

Their signed difference is \(A\).  The other seven columns give
\(B,C,D,E,F\) identically.  Finally the five pairs
\(\{d_3,i_1\}\) have signed difference \([34]-[25]\), giving \(G\).
\(\square\)

## 3. Complete proper-lower current

Let \(\Delta_\ell\) be the signed difference of the multisets of cyclic
length-\(\ell\) interval sets in the two suspended five-row factors.

### Theorem 3.1 (eight nested rails)

One has \(\Delta_1=0\).  For

\[
                              2\le \ell\le s+1,
\]

put \(t_1=\ell-1\) and \(t_2=\ell-2\).  Then

\[
\boxed{
\begin{aligned}
\Delta_\ell={}&
 W_{t_1}^+\star A+U_{t_1}^-\star B
 +U_{t_1}^+\star A+W_{t_1}^-\star B\\
&+W_{t_2}^+\star C+U_{t_2}^-\star D
 +U_{t_2}^+\star E+W_{t_2}^-\star F.
                                                               \tag{3.1}
\end{aligned}}
\]

At the maximal proper length \(\ell=s+2=m-1\), the two intervals meeting
opposite sides of the whole \(U\)-bank coalesce, and the formula is

\[
\boxed{
\Delta_{s+2}
 =W\star(A+B)+W_s^+\star C
   +U\star(D+E+G)+W_s^-\star F.                    \tag{3.2}
}
\]

#### Proof

The two phases have the same unordered \(D\)-set and the same unordered
\(I\)-set in each corresponding row.  Consequently an interval containing
all of a \(D\)- or \(I\)-block is unchanged row by row.

For \(2\le\ell\le s+1\), a changed interval cannot cross the entire
\(U\)-bank from \(D\) into \(I\), nor the entire \(W\)-bank from \(I\)
into \(D\).  Every changed interval therefore contains exactly a one- or
two-label proper prefix or suffix of one base block, together with one of
the four adjacent bank profiles.  A \(q\)-label piece uses
\(\ell-q\) bank labels.  Substitution of (2.1) gives (3.1).

At \(\ell=s+2\), the interval

\[
                          \{d_3\}\cup U\cup\{i_1\}
\]

is counted once, rather than as two separate boundary intervals.  Its base
current is \(G\).  Every other changed interval is still a proper prefix or
suffix interval.  Collecting the terms which have the same full bank gives
(3.2).  \(\square\)

Because complementing a cyclic interval of length \(\ell\) gives the
opposite cyclic interval of length \(2m+1-\ell\), equations (3.1)--(3.2)
also give the complete complementary upper current at every width.

### Corollary 3.2 (the twelve-move macro is not all-width closed)

For every nonempty common suffix, the complete current of the twelve-move
macro is nonzero.

#### Proof

Already at a generic proper length the eight fresh bank profiles in (3.1)
are distinct and at least one of the nonzero base currents in (2.2) survives.
More explicitly, for \(s\ge3\), \(\ell=3\) has positive mass twenty-two by
Theorem 4.1 below.  The cases \(s=1,2\) follow directly from (3.1), with
positive masses ten and eighteen at lengths two and three respectively.
\(\square\)

Thus cancellation of the fixed-`infinity` endpoint roots is a genuine gain,
but it is not the all-width cancellation required for a free suffix lift.

## 4. Exact capacity-one battery size

For a signed current \(H=\sum h_S[S]\), put

\[
                         \|H\|_+=\sum_{h_S>0}h_S.     \tag{4.1}
\]

The six base currents have

\[
\begin{array}{c|cccccc}
H&A&B&C&D&E&F\\ \hline
\|H\|_+&3&3&2&3&3&2.
\end{array}                                                   \tag{4.2}
\]

### Theorem 4.1 (22-channel interior residual)

For \(s\ge3\), at every length \(3\le\ell\le s\),

\[
                         \boxed{\|\Delta_\ell\|_+=22.}        \tag{4.3}
\]

At the two boundary lengths one has, for sufficiently long banks,

\[
              \|\Delta_2\|_+=14,
              \qquad
              \|\Delta_{s+1}\|_+=18,
              \qquad
              \|\Delta_{s+2}\|_+=9.                \tag{4.4}
\]

#### Proof

For \(3\le\ell\le s\), the eight bank profiles in (3.1) are distinct
fresh-label sets.  Hence their decorated supports are disjoint.  Equations
(4.2) and (3.1) give

\[
              2\|A\|_++2\|B\|_+
              +\|C\|_++\|D\|_++\|E\|_++\|F\|_+
              =6+6+2+3+3+2=22.
\]

At length two the four \(q=2\) currents share the empty profile and reduce
to

\[
                         C+D+E+F=2[25]-2[34],         \tag{4.5}
\]

leaving twelve further \(q=1\) units.  At length \(s+1\), the two full
\(U\)-profile \(q=1\) terms combine as

\[
                         A+B=[3]+[4]-[2]-[5].         \tag{4.6}
\]

At length \(s+2\), equation (3.2), together with

\[
\begin{aligned}
A+B={}&[3]+[4]-[2]-[5],\\
D+E+G={}&[25]+[14]+[36]-[15]-[34]-[26],             \tag{4.7}
\end{aligned}

has positive masses \(2,2,3,2\) on its four distinct profiles.  This proves
(4.4).  \(\square\)

### Corollary 4.2 (one pivot is insufficient in the ray model)

Any capacity-one absorber in which one protected one-ray port supplies at
most one positive claim at a fixed proper length needs at least twenty-two
active ray ports.  Equivalently, an interface made only of ordinary
two-ray monotone pivots needs at least eleven independent pivot channels.

In particular, one ordinary opening/pivot cell cannot absorb the residual
of the whole-factor macro for \(s\ge3\).

#### Proof

At an interior length, every positive basis occurrence in (4.3) must be
supplied by a distinct capacity-one occurrence.  One one-ray port supplies
at most one such occurrence, and one two-ray pivot supplies at most two.
\(\square\)

This lower bound is scoped to the literal capacity-one ray interface.  It
does not rule out a higher-valence shared cap in which one physical gadget
realizes several correlated occurrences.

## 5. The smallest current interface exposed by the calculation

Equations (3.1)--(3.2) give a constant-size abstract absorber specification:

1. twenty-two capacity-one nested rail channels realize the eight decorated
   currents in (3.1);
2. their top endpoints are joined by the nine-unit cap (3.2);
3. a complementary dual occurrence system carries the corresponding upper
   currents;
4. all claims are occurrence-disjoint from the transported compiler bank.

The twenty-two channels are necessary in the capacity-one rail model by
Theorem 4.1.  They are sufficient at the level of signed currents: decompose
each of \(A,B,C,D,E,F\) into \(\|H\|_+\) unit differences and carry each
difference along its nested profile in (3.1).  Equation (3.2) is the exact
finite top-junction rule.  What is not yet proved is a word-level protected
host realizing these channels and the complementary upper cap at only
bounded **extra** physical length.

Thus the exact remaining escape is no longer an unspecified cut slide.  It
is one of the following:

* a protected 22-ray plus dual battery embedded mostly in existing support;
* a higher-valence bounded cap which compresses those twenty-two occurrence
  channels; or
* a different whole-factor native word whose analogue of (3.1) has smaller
  or zero rail current.

The explicit twelve-move path settles dynamic base reachability, while this
note proves that base reachability alone does not close the common-suffix
gate.

## 6. Why the cheaper single-transposition phases do not lie in the native orbit

There are two superficially cheaper endpoint-sealed coordinate conjugates.
Let

\[
                         \alpha=(23),\qquad \beta=(45).        \tag{6.1}
\]

The fixed-`infinity` root family is

\[
                 \mathcal R=\{123,124,125,134,135\}.          \tag{6.2}
\]

Its coordinate stabilizer is exactly

\[
                 H=\langle\alpha,\beta\rangle
                   =\{1,\alpha,\beta,\alpha\beta\}.           \tag{6.3}
\]

Indeed, coordinate 1 is the unique label occurring in all five roots and
coordinate 6 is the unique label occurring in none.  The remaining
occurrence multiplicities split the labels into the two pairs
\(\{2,3\}\) and \(\{4,5\}\), and each of the four resulting permutations
does preserve (6.2).

The generic rail masses of the two one-transposition phases
\(\alpha\mathcal P^-\) and \(\beta\mathcal P^-\), relative to
\(\mathcal P^-\), are only twelve.  They nevertheless cannot replace the
22-channel phase inside a native serial word.

### Theorem 6.1 (row-parity obstruction)

No native sequence starting at \(\mathcal P^-\) reaches
\(\alpha\mathcal P^-\) or \(\beta\mathcal P^-\).  The even conjugate
\(\alpha\beta\mathcal P^-\) is exactly \(\mathcal P^+\) and is reached by
the twelve-move word.

#### Proof

The parity of a seven-symbol cyclic order is well-defined: rotating the
order applies a 7-cycle, which is even.  In one native move, each output row
is obtained from its input row by two disjoint adjacent transpositions:

\[
       (a,b,x,c,d,y_1,y_2)
          \longmapsto(b,a,x,d,c,y_1,y_2),
\]

and similarly for the other row.  Hence the parity of every individual row
is preserved, and so is the multiset of the five row parities.

Applying an odd coordinate permutation to all rows reverses all five
parities.  Since five is odd, the number of even rows and the number of odd
rows are interchanged and cannot remain equal.  Thus neither odd
conjugation \(\alpha\) nor \(\beta\) lies in the native orbit.

The permutation \(\alpha\beta\) is even.  Direct comparison of the two
columns of the pentagon factor gives
\(\alpha\beta\mathcal P^-=\mathcal P^+\), and the twelve displayed native
moves prove reachability.  \(\square\)

Consequently, among nontrivial **coordinate-conjugate, endpoint-sealed**
phases in the native orbit, the 22-channel phase is forced.  This does not
exclude a non-conjugate native-reachable factor with a smaller current, but
it rules out the evident twelve-channel shortcut.
