# Every upper target has a path seeded by one fixed matching

**Date:** 2026-08-06  
**Method:** a monotone missing-set elimination path and exact residual Hall;
no computation or search  
**Status:** unconditional individual-path theorem and exact simultaneous
completion reduction.  After fixing one perfect matching, every upper
target has a shortest owner path whose alternating role-zero incidences
lie in that matching and whose role-one incidences avoid it.  For a bank of
targets, the only remaining graph condition is that the selected role-one
matching extend inside the graph with the first factor deleted.  Neither
raw path abundance nor choosing the second factor first proves this Hall
condition.

## 1. One fixed matching seeds directed owner paths

Work in the balanced middle-level incidence graph

\[
 {\cal L}={ [2R-1]\choose R-1},\qquad
 {\cal U}={ [2R-1]\choose R}.                       \tag{1.1}
\]

Fix a perfect matching `M_0`.  For every owner `U in cal U`, let

\[
 \ell_0(U)=M_0^{-1}(U),\qquad
 h_0(U)=U\setminus\ell_0(U).                        \tag{1.2}
\]

Thus `h_0(U)` is one coordinate.  Define a directed graph on the owner
shore by

\[
 U\longrightarrow V
 \quad\Longleftrightarrow\quad
 U\ne V,\quad \ell_0(U)\subset V.                  \tag{1.3}
\]

The arc is the oriented owner step

\[
                         U-\ell_0(U)-V.             \tag{1.4}
\]

Its first incidence belongs to `M_0`; its second incidence does not.

## 2. Monotone elimination theorem

### Theorem 2.1 (factor-seeded upper path)

Let `Z` be any target with

\[
                         |Z|=R+s,\qquad s\ge1.      \tag{2.1}
\]

For every initial owner `U_0 subseteq Z`, there is a simple directed path

\[
                         U_0\to U_1\to\cdots\to U_s \tag{2.2}
\]

in (1.3) such that

\[
                         \bigcup_{i=0}^sU_i=Z.       \tag{2.3}
\]

The path has the minimum possible number `s` of Johnson transitions.  Its
role-one incidences

\[
             \ell_0(U_i)U_{i+1},\qquad 0\le i<s,   \tag{2.4}
\]

form a matching disjoint from `M_0`.

#### Proof

Put

\[
                         A_i=Z\setminus U_i,
 \qquad I_i=\bigcap_{j=0}^i A_j.                   \tag{2.5}
\]

Initially `|A_0|=|I_0|=s`.  While `I_i` is nonempty, choose any
`a_i in I_i` and define

\[
 U_{i+1}=\ell_0(U_i)\cup\{a_i\}
          =U_i-\{h_0(U_i)\}+\{a_i\}.               \tag{2.6}
\]

Because `a_i notin U_i`, this is a distinct rank-`R` owner contained in
`Z`, and (1.3) gives the required directed step.  Its missing set is

\[
 A_{i+1}=A_i-\{a_i\}+\{h_0(U_i)\}.                 \tag{2.7}
\]

Now `h_0(U_i) notin A_i`, and hence it is not in `I_i`.  Therefore

\[
                         I_{i+1}=I_i-\{a_i\}.       \tag{2.8}
\]

After exactly `s` steps the running intersection is empty.  Equation
(2.3) is the complement of this assertion inside `Z`.

The owners are pairwise distinct.  Indeed `a_i` is absent from every
previous owner, because it lies in `I_i`, whereas (2.6) puts it in
`U_{i+1}`.  The lower vertices `ell_0(U_i)` are pairwise distinct because
`M_0` is a matching, and the heads `U_{i+1}` are pairwise distinct.
Thus (2.4) is a matching.  It is disjoint from `M_0` because the `M_0`
edge at `ell_0(U_i)` ends at `U_i`, not at `U_{i+1}`.

Finally, one Johnson transition introduces at most one coordinate outside
the initial rank-`R` owner.  Reaching a union of rank `R+s` needs at least
`s` transitions, so the path is shortest.  \(\square\)

### Corollary 2.2 (large prospective menu)

For one target `Z`, every one of its

\[
                         {R+s\choose R}             \tag{2.9}
\]

owners can be used as `U_0`, and every ordering of the successive
persistent missing coordinates in (2.8) gives a legal shortest path.
This is a prospective menu.  The theorem does not assert that all these
paths remain after a second perfect matching has already been fixed.

## 3. Exact simultaneous completion gate

Let `mathcal D` be a bank of upper targets.  For each target choose one
path from Theorem 2.1, with all chosen owners and lower vertices mutually
disjoint.  Let

\[
 Q_0=\{\ell_0(U_i)U_i\},\qquad
 Q_1=\{\ell_0(U_i)U_{i+1}\}                         \tag{3.1}
\]

be the two alternating incidence classes over all paths.  Then

\[
                         Q_0\subseteq M_0,
 \qquad Q_1\cap M_0=\varnothing,                   \tag{3.2}
\]

and `Q_1` is a matching.

Put

\[
                         D=G-M_0.                  \tag{3.3}
\]

Let `Z_1,Y_1` be the two endpoint shores of `Q_1`.

### Theorem 3.1 (exact disjoint-factor completion criterion)

There is a perfect matching `M_1` with

\[
                         Q_1\subseteq M_1,
 \qquad M_1\cap M_0=\varnothing                    \tag{3.4}
\]

if and only if

\[
 |N_D(A)\setminus Y_1|\ge|A|
 \quad
 \text{for every }A\subseteq{\cal L}\setminus Z_1. \tag{3.5}
\]

When (3.5) holds, the simple factor `M_0 union M_1` contains every chosen
owner path and hence every target in `mathcal D`.

#### Proof

After fixing `Q_1`, a disjoint second factor is exactly a perfect matching
of

\[
 D[{\cal L}\setminus Z_1,{\cal U}\setminus Y_1].   \tag{3.6}
\]

Hall's theorem gives (3.5).  Adding `Q_1` gives `M_1`.  Equations
(3.1)--(3.2) say that the two alternating incidences of every selected
path lie respectively in `M_0,M_1`, so their union factor contains the
paths.  \(\square\)

The point of (3.5) is its quantifier.  The host `D=G-M_0` is
`(R-1)`-regular and has perfect matchings, but this alone does not imply
that an arbitrary polynomial matching `Q_1` extends.  The old spectral
localization for `G` does not transfer automatically: for a candidate
shore `A`, the deleted bank `M_0(A)` can have cardinality `|A|`, rather
than polynomial cardinality.

## 4. Why choosing the second factor first removes the menu

Suppose instead that a disjoint perfect matching `M_1` is fixed before the
backup paths.  Then `K=M_0 union M_1` is a simple two-factor.  Every
oriented owner path supported by both matchings is a contiguous segment of
one factor cycle.  Consequently a target `Z` is available precisely when
some such segment has all owners inside `Z` and owner union `Z`.

For `s=1` this condition is especially transparent:

\[
 \boxed{
 Z\text{ has a factor-supported witness}
 \iff
 Z\text{ occurs in the immediate-upper palette of }K.}          \tag{4.1}
\]

Thus fixing `M_1` first does not leave the full prospective menu (2.9); it
replaces it by the literal interval deck of one already chosen factor.
Disjointness of `M_0,M_1` and regularity of their complement do not assert
that this deck contains the prescribed PBBS residual targets.

Sections 3 and 4 give the exact quantifier dichotomy:

\[
 \begin{array}{c}
 \text{paths first}\quad\Longrightarrow\quad
       \text{the residual Hall gate (3.5)},\\[2mm]
 \text{second factor first}\quad\Longrightarrow\quad
       \text{the factor-deck gate of Section 4}.
 \end{array}                                                       \tag{4.2}
\]

Neither gate follows from the marginal path count alone.

## 5. Weakest sufficient PBBS interface

For the phase-one upper-backup bank, the weakest graph statement needed is
the following.

> **Target-conditioned factor-seeded selector.**  Choose one
> `M_0`-seeded path from Theorem 2.1 for every prescribed residual target
> so that the paths are resource-disjoint, have the required sub-half
> exposure, and their role-one matching `Q_1` satisfies (3.5).

Under this selector, the backup bank contributes no common-edge debt:
`M_1` may be chosen in `G-M_0`.  It also contributes no later upper or cap
matching once a literal antecedent has been materialized: the union of the
source interval underneath a contiguous owner path is the same target.

The exact literal/history conditions which remain external are only:

1. one resident depth-`d` antecedent for the completed directed factor;
2. the occurrence address of each selected owner interval in that
   antecedent; and
3. the two-coordinate typed suffix product for genuinely lower/compiler
   tasks.

The upper backups themselves are passive after items 1--2.  They do not
need an independent common-cap route.

What is not proved here is the target-conditioned selector.  Theorem 2.1
removes individual path existence as an obstruction and (3.5) identifies
the exact remaining simultaneous correlation.  Proving only that every
target has many paths, or only that `G-M_0` has a perfect matching, is not
enough.
