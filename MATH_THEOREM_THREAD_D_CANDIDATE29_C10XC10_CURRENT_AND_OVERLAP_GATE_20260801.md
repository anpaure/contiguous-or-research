# Candidate29 simultaneous `H-C10 x D-C10`: terminal current, overlap rank, and provider gate

Date: 2026-08-01  
Status: **exact terminal theorem and genuine necessary obstructions; no finite existence or no-go claim**

## 0. Frozen data and scope

Let $d,h:O\to E$ be the selected literal candidate29 incidences and let
$\bar D,\bar H:O\to F$ be their owner-to-facet endpoint bijections.  Put

\[
                         \pi=\bar H^{-1}\bar D.             \tag{0.1}
\]

The quotient factor is one 1430-cycle of voltage (3\pmod {17}).  Its
upper and lower load profiles are

\[
 \mu_+:0^1 1^{879}2^{243}3^{19}4^2,
 \qquad
 \mu_-:0^1 1^{877}2^{246}3^{19}4^1,                       \tag{0.2}
\]

with holes

\[
                         u=0x0355f,\qquad \ell=0x0062f.    \tag{0.3}
\]

This note concerns a simultaneous raw H assignment 5-cycle $\beta$ and
D assignment 5-cycle $\alpha$.  It treats only terminal matching validity,
the two immediate palettes, quotient connectedness, and voltage.

## 1. Raw terminal maps and pair rescue

The raw `H-C10` and `D-C10` banks are defined exactly as in the mixed
`C6/C10` theorem: retain every literal nonloop assignment arc, including an
arc equal to the opposite base matching, enumerate every simple directed
5-cycle, and deduplicate only equal complete owner-to-incidence terminal
vectors.

Let

\[
 A=\operatorname{supp}(\alpha),\qquad
 B=\operatorname{supp}(\beta),\qquad |A|=|B|=5.            \tag{1.1}
\]

Write $d',h'$ for the literal terminal incidences.  Their endpoint maps and
the factor successor are

\[
 \bar D'=\bar D\alpha,\qquad \bar H'=\bar H\beta,\qquad
 \pi'=\beta^{-1}\pi\alpha.                                \tag{1.2}
\]

Define isolated opposite-base conflicts

\[
 C_D=\{x\in A:d'_x=h_x\},\qquad
 C_H=\{x\in B:h'_x=d_x\}.                                 \tag{1.3}
\]

### Lemma 1.1 (exact pair rescue)

A raw pair is terminal incidence-disjoint if and only if

\[
 C_D\cup C_H\subseteq A\cap B                              \tag{1.4}
\]

and

\[
                         d'_x\ne h'_x
                         \quad(x\in A\cap B).              \tag{1.5}
\]

In particular,

\[
                         |C_D\cup C_H|\le |A\cap B|\le5.   \tag{1.6}
\]

The proof is ownerwise: outside the overlap only one side moves, while on
the overlap (1.5) is the exact final condition.  Thus isolated-invalid raw
atoms must be retained.  Conversely, overlap can also create a new collision,
so (1.4) alone is not sufficient.  $\square$

The full Cartesian product of the two deduplicated raw banks, followed by
(1.4)--(1.5), is therefore the complete terminal domain.

## 2. Exact palette-current equations

Put

\[
 O_\times=A\cap B,
 \qquad
 F_\times=\bar D(A)\cap\bar H(B),                         \tag{2.1}
\]

and write

\[
 r_-=|O_\times|,\qquad r_+=|F_\times|.                    \tag{2.2}
\]

The changed lower and upper row counts are

\[
 n_-=|A\cup B|=10-r_-,\qquad
 n_+=|\bar D(A)\cup\bar H(B)|=10-r_+.                    \tag{2.3}
\]

For either shore $\varepsilon\in\{-,+\}$, let $d_T^\varepsilon$ be
the number of changed old rows carrying target $T$, and let
$g_T^\varepsilon$ be the number of terminal new rows carrying $T$.
Define the deletion current

\[
                         a_T^\varepsilon
                         =d_T^\varepsilon-g_T^\varepsilon. \tag{2.4}
\]

Then

\[
                         \sum_Ta_T^\varepsilon=0.           \tag{2.5}
\]

### Theorem 2.1 (terminal palette current)

The terminal shore is complete if and only if

\[
 a_{h_\varepsilon}^\varepsilon\le-1,
 \qquad
 a_T^\varepsilon\le\mu_\varepsilon(T)-1
 \quad(T\ne h_\varepsilon),                               \tag{2.6}
\]

where $h_+=u$ and $h_-=\ell$.

#### Proof

The terminal load is

\[
                  \mu'_\varepsilon(T)=
                  \mu_\varepsilon(T)-a_T^\varepsilon.      \tag{2.7}
\]

For the hole, $\mu_\varepsilon(h_\varepsilon)=0$, so positivity is the
first inequality in (2.6).  For every other target, positivity is the second.
The equality (2.5) follows because the packet deletes and inserts the same
number $n_\varepsilon$ of rows.  $\square$

This is necessary and sufficient.  Any scalar invariant below is only a
consequence of (2.6), not a replacement for it.

## 3. Cross-square current and overlap-rank obstruction

An isolated raw atom may use the opposite selected incidence.  At such an
owner its provisional intersection has rank eight rather than seven (and at
the upper shore the analogous provisional union has rank nine rather than
ten).  Thus isolated columns must first be formed in the free abelian group
on **all** set traces and only then restricted to the required palette.

Let $\operatorname{pr}_-$ send a rank-seven trace to its $\mathbb Z_{17}$
canonical palette target and every other trace to zero; define
$\operatorname{pr}_+$ analogously for rank ten.
Evaluate the D-C10 and H-C10 separately against the base matching, add their
two formal isolated columns, and apply $\operatorname{pr}_\varepsilon$.
Call the resulting provisional required-palette load $\nu_\varepsilon$.  At
a lower overlap owner, let

\[
 B=L(d_x,h_x),\quad P=L(d'_x,h_x),\quad
 Q=L(d_x,h'_x),\quad R=L(d'_x,h'_x).                        \tag{3.1}
\]

The formal correction from the isolated sum to the true terminal current is

\[
 \widehat\kappa_x=[R]-[P]-[Q]+[B],\qquad
 \kappa_x=\operatorname{pr}_-(\widehat\kappa_x).            \tag{3.2}
\]

The same formula, followed by $\operatorname{pr}_+$, holds at every upper
overlap facet.  Hence on the two required palettes

\[
 \mu'_-=\nu_-+\sum_{x\in O_\times}\kappa_x,
 \qquad
 \mu'_+=\nu_++\sum_{f\in F_\times}\kappa_f.               \tag{3.3}
\]

The formal square $\widehat\kappa$ has total mass zero.  Its projected square
need not: an off-rank $P$ or $Q$ is discarded.  What the deficiency argument
needs, and what remains exact, is that the projected positive mass is at most
two, because its positive part is contained in
$\operatorname{pr}_\varepsilon([B]+[R])=[B]+[R]$.  Here $B$ is a legal base
turn and $R$ is a legal terminal turn after pair validity.

Define the provisional deficiency

\[
                         \operatorname{Def}(\nu)
                         =\sum_T(1-\nu(T))_+.               \tag{3.4}
\]

### Theorem 3.1 (overlap-rank obstruction)

Every palette-exact C10 x C10 pair satisfies

\[
             \operatorname{Def}(\nu_-)\le2r_-,\qquad
             \operatorname{Def}(\nu_+)\le2r_+.             \tag{3.5}
\]

If the isolated sum does not create the named hole on a shore, then the
corresponding overlap is nonempty and some final mixed turn $R$ equals that
hole.

#### Proof

To make every provisional deficient required-palette load at least one
requires at least $\operatorname{Def}(\nu)$ units of positive projected
correction.  Each overlap square supplies at most two.  A base turn $B$
cannot equal a base-missing hole, and an off-rank provisional turn is killed
by $\operatorname{pr}_\varepsilon$, so an absent isolated hole can only be
supplied by the final mixed turn $R$.  $\square$

Thus (3.5) is a genuine no-go certificate for an individual raw pair.  It is
only necessary: the negative terms (-[P]-[Q]) can create new deficits, and
the positive units may hit the wrong targets.

Combining pair rescue and overlap current gives the useful lower bounds

\[
 r_-\ge |C_D\cup C_H|,
 \qquad
 r_-\ge\left\lceil\frac{\operatorname{Def}(\nu_-)}2\right\rceil,
 \qquad
 r_+\ge\left\lceil\frac{\operatorname{Def}(\nu_+)}2\right\rceil.          \tag{3.6}
\]

## 4. Singleton/repeat-release obstruction

For a shore $\varepsilon$, let $s_\varepsilon$ be the number of changed
old rows whose base target has load one.  These are (s_\varepsilon)
distinct protected colours.  Let $G_\varepsilon$ be the multiset of the
(n_\varepsilon) terminal new turns and define its collision excess

\[
                         \chi_\varepsilon
                         =n_\varepsilon-|\operatorname{supp}G_\varepsilon|.
                                                                    \tag{4.1}
\]

Finally put

\[
                         \rho_\varepsilon=n_\varepsilon-s_\varepsilon,
                                                                    \tag{4.2}
\]

the number of changed old rows drawn from repeated colours.

### Theorem 4.1 (repeat-release current)

Every exact terminal shore satisfies

\[
                         \rho_\varepsilon\ge1+\chi_\varepsilon.           \tag{4.3}
\]

#### Proof

Every deleted load-one colour must occur among the terminal new turns, as
must the distinct base hole.  Thus

\[
 s_\varepsilon+1\le
 |\operatorname{supp}G_\varepsilon|
 =n_\varepsilon-\chi_\varepsilon.
\]

Rearranging gives (4.3).  $\square$

In particular every repair must release at least one old repeated-colour
occurrence on each shore.  Candidate29 has 551 upper and 553 lower
repeat-colour occurrences in total, and repeat excess 287 on each shore.
Every duplicate among the new local turns requires one additional released
repeat occurrence.  Again, (4.3) is necessary but not sufficient because it
does not enforce the identities of protected singleton colours.

## 5. Sound provider pruning

For the lower hole, a terminal witness is exactly one of:

1. a D one-side provider on $A\setminus B$;
2. an H one-side provider on $B\setminus A$; or
3. a mixed pair $(D'_x,H'_x)$ on $O_\times$ whose final lower turn is
   $\ell$.

For the upper hole, replace owner rows by the disjoint parts of $D(A)$ and
$H(B)$, and use an exact mixed incidence-pair table on $F_\times$.
These two three-way disjunctions are necessary and sufficient for creating
the named holes; Theorem 2.1 is still needed to protect every old colour.

The candidate29 provider-gap theorem yields one additional sound rule.  If
both holes are witnessed by unmixed one-side providers on the same C10, the
two directed provider gaps must be `(1,2)` or `(2,1)`.  If either witness is
mixed, this rejection is unavailable.  Requiring either raw C10 alone to
contain both old provider types is therefore incomplete.

## 6. Topology and voltage

Both 5-cycles are even, so parity gives no obstruction beyond (1.3).  List
$A\cup B$ in base-$\pi$ cyclic order and let $s_0$ be its cyclic
successor.  Extending $\alpha,\beta$ by the identity, the contracted
terminal successor is

\[
                              \Phi=\beta^{-1}s_0\alpha.       \tag{6.1}
\]

The quotient factor is connected exactly when $\Phi$ is one cycle.  The
physical lift is one cycle exactly when its literal voltage is nonzero modulo
17.  Voltage must be recomputed from the selected incidence shifts; it is not
determined by $\alpha,\beta$ or by the palette currents.

## 7. Exact terminal theorem

### Theorem 7.1

A simultaneous raw H-C10/D-C10 pair is an immediate physical repair if and
only if all of the following hold:

1. the two side terminal maps are perfect and satisfy (1.4)--(1.5);
2. the exact current inequalities (2.6) hold on both shores;
3. $\beta^{-1}\pi\alpha$ is one quotient cycle; and
4. its literal voltage is nonzero modulo 17.

Conditions (3.5), (3.6), (4.3), and the provider clauses of Section 5 are
sound necessary prefilters.  None is separately sufficient.

#### Proof

Condition 1 is exactly a pair of incidence-disjoint perfect matchings.
Theorem 2.1 is exactly terminal palette completeness.  Conditions 3--4 are
exactly quotient connectedness and connected physical lift.  $\square$

## 8. Precise surviving finite gate

There is no generic parity no-go for C10 x C10.  The proved obstructions are:

* pair-rescue capacity (1.6);
* overlap positive-current rank (3.5)--(3.6);
* singleton/repeat release (4.3); and
* provider-gap compatibility for unmixed witnesses.

A global candidate29 no-go would require proving that every raw pair violates
at least one of these rows, or performing the complete terminal enumeration.
No such finite conclusion is claimed here.  Residence, deeper shadows,
opening, and the compiler remain outside scope.
