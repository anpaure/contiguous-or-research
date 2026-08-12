# The octagon source deck has a linear phase residue after the two-host reset

Date: 2026-08-01  
Lane: D, full source-word audit for the quaternary octagon tensor  
Status: exact deck classification and exact block-refinement obstruction.
The two exterior hosts repair the original typed boundary signature, but do
not make the complete source block contextually OR-transparent.

## 0. Corrected verdict

Let `Y^0,Y^1` be the two source words obtained from the resident octagon
tensor after adjoining and splitting

\[
                  X_L=\{a_0,a_1\},\qquad X_R=\{a_1,a_2\} \tag{0.1}
\]

as in
`MATH_THEOREM_THREAD_D_OCTAGON_SPLIT_BOUNDARY_RESET_20260801.md`.
That theorem remains exact in its stated scope:

* it preserves every old interval of each phase under its own refinement;
* it creates the two missing packet-near typed boundary cells;
* it has refinement charge `+2`, common host caps and local split state
  `Phi<=2`.

It does **not** identify the complete interval decks of the two source
phases.  For the sharp eight-address inverse and every `d>=2`,

\[
\begin{aligned}
 |\operatorname{Deck}(Y^0)-\operatorname{Deck}(Y^1)|&=4d+1,\\
 |\operatorname{Deck}(Y^1)-\operatorname{Deck}(Y^0)|&=6d-3. \tag{0.2}
\end{aligned}
\]

The prefix and suffix discrepancies are only one value in each direction,
but the internal deck residue is linear.  Worse, in either direction exactly
`3d-3` of the phase-only masks are outside the closure of **every** block
refinement of the opposite word, even when both endpoints of an interval may
be trimmed independently.  Thus the two exterior hosts do not provide a
blockwise full-OR reset.  If all local deck values are protected, a separate
lower compiler or newly planted ray bank is necessary.  For a global word,
the exact requirement is weaker: only protected occurrences without surviving
external/common witnesses enter the residual Hall bank of Section 6.

The maximal inverse is cleaner but not transparent: its two directed deck
differences both have size `2d+1`, and `2d-1` masks in either direction are
outside the opposite block-refinement closure.

## 1. Notation

Put

\[
 F[i,j]=\{f_i,f_{i+1},\ldots,f_j\},                     \tag{1.1}
\]

with an empty range omitted, and let `K` be the fixed core.  Define

\[
\begin{aligned}
 \mathcal G_d={}&\{F[t,d]:2\le t\le d\}\\
 &\cup\{F[t,d+1]:3\le t\le d\}\\
 &\cup\bigl\{\{f_0\}\cup F[t,d+1]:3\le t\le d\bigr\}. \tag{1.2}
\end{aligned}
\]

Thus `|G_d|=3d-5`.  The three exterior-only masks in phase zero are

\[
\begin{aligned}
 \mathcal H_0=\{&K\cup\{a_0,a_2,a_3\}\cup F[0,d],\\
                 &K\cup\{a_1,a_2,a_3\}\cup F[1,d+1],\\
                 &K\cup\{a_1,a_2,a_3\}\cup F[0,d+1]\}, \tag{1.3}
\end{aligned}
\]

and in phase one they are

\[
\begin{aligned}
 \mathcal H_1=\{&K\cup\{a_0,a_1,a_3\}\cup F[0,d],\\
                 &K\cup\{a_0,a_2,a_3\}\cup F[1,d+1],\\
                 &K\cup\{a_0,a_1,a_3\}\cup F[0,d+1]\}. \tag{1.4}
\end{aligned}
\]

These masks do not contain `z`.  They are introduced by intervals meeting
one of the two split exterior hosts and are distinct from the four original
typed owner-boundary values.

## 2. Maximal inverse: two chains plus three exterior masks

Let `Y^epsilon_max` use the maximal erosion source internally.  Then

\[
\begin{aligned}
 \Delta^\max_0
  ={}&\operatorname{Deck}(Y^0_\max)-\operatorname{Deck}(Y^1_\max)\\
  ={}&\mathcal H_0\\
   &\cup\{K\cup\{z,a_1\}\cup F[1,j]:1\le j\le d-1\}\\
   &\cup\{K\cup\{z,a_3\}\cup F[t,d]:2\le t\le d\},   \tag{2.1}\\
 \Delta^\max_1
  ={}&\operatorname{Deck}(Y^1_\max)-\operatorname{Deck}(Y^0_\max)\\
  ={}&\mathcal H_1\\
   &\cup\{K\cup\{z,a_3\}\cup F[1,j]:1\le j\le d-1\}\\
   &\cup\{K\cup\{z,a_1\}\cup F[t,d]:2\le t\le d\}.   \tag{2.2}
\end{aligned}
\]

All displayed families are disjoint, so

\[
                         |\Delta^\max_0|=|\Delta^\max_1|=2d+1. \tag{2.3}
\]

The low-rank part is two nested chains.  This set-theoretic compression does
not by itself make them physical split rays.

## 3. Sharp eight-address inverse: exact asymmetric families

Let `Y^epsilon_sh` use the sharp eight-address source for `d>=2`.  Its
phase-zero difference is

\[
\begin{aligned}
 \Delta^\mathrm{sh}_0={}&\mathcal H_0\\
 &\cup\{K\cup\{z,a_1\}\cup F[1,j]:1\le j\le d-1\}\\
 &\cup\{K\cup\{a_1\}\cup F[s,d+1]:s=1,2\}\\
 &\cup\{K\cup\{a_3,f_0,f_1\},
          K\cup\{a_3,f_0,f_1,f_2\}\}\\
 &\cup\{K\cup\{z,a_3\}\cup G:G\in\mathcal G_d\}.     \tag{3.1}
\end{aligned}
\]

The phase-one difference is

\[
\begin{aligned}
 \Delta^\mathrm{sh}_1={}&\mathcal H_1\\
 &\cup\{K\cup\{z,a_3\}\cup F[1,j]:1\le j\le d-1\}\\
 &\cup\{K\cup\{a_1,f_0,f_1\},
          K\cup\{a_1,f_0,f_1,f_2\}\}\\
 &\cup\{K\cup\{z,a_1\}\cup G:G\in\mathcal G_d\}\\
 &\cup\{K\cup\{a_3\}\cup F[s,j]:s=1,2, 3\le j\le d+1\}. \tag{3.2}
\end{aligned}
\]

Again the displayed families are disjoint.  Their counts are

\[
                 |\Delta^\mathrm{sh}_0|=4d+1,
                 \qquad |\Delta^\mathrm{sh}_1|=6d-3.    \tag{3.3}
\]

The asymmetry is caused by exact source thinning, not by the owner tensor:
the owner path and its complete interval deck remain phase-exact.

### Proof of (2.1)--(3.3)

The maximal and thinned source formulas differ only in the four active
erosion corridors of the octagon theorem.  An interval crossing two complete
corridors already contains the phase-common active union and cannot be
phase-exclusive.  Enumerating the two possible endpoints inside one
corridor gives the prefix chains `F[1,j]`, the three suffix families
`G_d`, and the two single-active families in (3.1)--(3.2).  Intervals which
meet an exterior split host give exactly (1.3)--(1.4).  No two displayed
families collide because their active-label parts differ, except within one
listed chain where the filler endpoints distinguish them.  Summing their
lengths gives (2.3) and (3.3).  The audit replays every endpoint and checks
literal equality with the displayed families.

## 4. Contextual transparency and the exact refinement obstruction

For any three consecutive blocks `L,U,R`, write `tot(U)` for the union of
all letters of `U`.  The interval deck decomposes exactly as

\[
\begin{aligned}
 \operatorname{Deck}(LUR)={}&\operatorname{Deck}(L)
 \cup\operatorname{Deck}(U)\cup\operatorname{Deck}(R)\\
 &\cup\operatorname{Suf}(L)\vee\operatorname{Pref}(U)
 \cup\operatorname{Suf}(U)\vee\operatorname{Pref}(R)\\
 &\cup\operatorname{Suf}(L)\vee\{\operatorname{tot}(U)\}
                    \vee\operatorname{Pref}(R).          \tag{4.1}
\end{aligned}
\]

Consequently equality of the internal, prefix and suffix decks (and the
total union) is sufficient for transparency in every fixed context.

For the two expanded octagon sources the totals agree, but

\[
\begin{array}{c|cc}
 &Y^0-Y^1&Y^1-Y^0\\ \hline
 \operatorname{Pref}&\{\{a_0\}\}&\{\{a_1\}\}\\
 \operatorname{Suf}&\{\{a_1\}\}&\{\{a_2\}\}.
\end{array}                                               \tag{4.2}
\]

The external guards can screen (4.2), but no context changes an interval
lying wholly inside `U`.  Thus the nonempty banks (2.1)--(3.2) alone rule
out full contextual transparency.

There is a sharper physical obstruction.  Let `Ref(Y)` be the set of
nonempty masks which can occur after replacing letters of `Y` by nonempty
consecutive blocks with the same unions.  The quantifier is existential for
one named target: the refinement may depend on that target, and it neither
merges nor reorders old letters.  The side-cell normal form gives the exact
criterion

\[
\begin{split}
 \varnothing\ne S\in\operatorname{Ref}(Y)\quad\Longleftrightarrow\quad
 &S\subseteq Y_p\text{ for some }p,\quad\text{or}\\
 &\exists a<b:\ U_{a,b}\subseteq S\subseteq
 U_{a,b}\cup Y_a\cup Y_b,\\
 &\hspace{20mm}S\cap Y_a\ne\varnothing,quad
 S\cap Y_b\ne\varnothing,                              \tag{4.3}
\end{split}
\]

where `U_(a,b)=union_(a<i<b)Y_i`.  The two endpoint pieces may be chosen
arbitrarily, so (4.3) allows every arity and any collection of letterwise
split sites for that one target.  Individual membership of several targets
does not assert that one common refinement realizes all of them
simultaneously.

Applying (4.3) to the exact families gives

\[
\begin{array}{c|cc}
 &|\Delta_0\cap\operatorname{Ref}(Y^1)|
 &|\Delta_1\cap\operatorname{Ref}(Y^0)|\\ \hline
 \text{maximal source}&2&2\\
 \text{sharp source}&d+4&3d.
\end{array}                                               \tag{4.4}
\]

Therefore

\[
\begin{array}{c|cc}
 &\text{phase-zero masks not refinable in phase one}
 &\text{phase-one masks not refinable in phase zero}\\ \hline
 \text{maximal source}&2d-1&2d-1\\
 \text{sharp source}&3d-3&3d-3.
\end{array}                                               \tag{4.5}
\]

For `d>=3`, the sharp unrefinable low-rank families are, in phase zero,

\[
\begin{aligned}
 &K\cup\{z,a_1\}\cup F[1,j] &&(2\le j\le d-1),\\
 &K\cup\{z,a_3\}\cup F[t,d] &&(2\le t\le d),\\
 &K\cup\{z,a_3\}\cup F[t,d+1]&&(4\le t\le d),        \tag{4.6}
\end{aligned}
\]

together with all three masks in `H_0`.  Phase one swaps `a_1,a_3` in
(4.6) and uses `H_1`.  At `d=2`, the three exterior masks alone are
unrefinable.  This lists exactly `3d-3` masks in either direction.

The families in (4.6) are a bounded number of nested set chains, but they
are not endpoint rays of the present opposite source word.  This is the
same distinction as in the split-letter theorem: nesting is not a physical
host certificate.

## 5. Exact ambient owner result and the fixed-`H` boundary

The source-deck failure above does **not** damage the central owner path.
Write

\[
                N=9d+23,\qquad L=N-d=8d+23.             \tag{5.1}
\]

For either phase and either inverse, let `Y` be the split expanded source and
put

\[
                   O_j=\bigcup_{p=j}^{j+d}Y_p,
                   \qquad 0\le j\le L+3.                \tag{5.2}
\]

The exact owner profile is

\[
             (r+2,r+1)\mid r^{\,L}\mid(r+1,r+2),         \tag{5.3}
\]

and, more strongly,

\[
                         O_{i+2}=T_i\qquad(0\le i<L).    \tag{5.4}
\]

Thus all `L` central owners survive literally and no central owner is lost.
The four exterior source positions `0,1,N+2,N+3` have owner-incidence
intervals

\[
             \{0\},\quad\{0,1\},\quad
             \{L+2,L+3\},\quad\{L+3\},                 \tag{5.5}
\]

respectively.  They form two Boolean staircases from rank `r+2` through
`r+1` to the endpoint rank-`r` owner.  The complete expanded path remains
resident with exact floor `d+1`.

The unchanged central lower-incidence path has `2(L-1)=16d+44` edges.  The
four staircase edges raise the mixed-rank Hasse-path count to `16d+48`.
Consequently the proved fixed-`H` path-planting theorem applies only to `H`
pairwise-disjoint **central** paths under

\[
                         H(16d+44)\le m-2.               \tag{5.6}
\]

It does not plant the `4H` off-rank boundary edges.  Those remain explicit
host obligations.  In particular (5.3)--(5.6) prove central owner and q1
survival, not upper/Catalan completion, a prescribed common-cap compiler, or
the full source-deck transport refuted in Sections 2--4.  The literal proof
and deadline audit are recorded independently in
`MATH_AUDIT_THREAD_D_OCTAGON_SPLIT_OWNER_STAIRCASE_AND_FIXED_H_SCOPE_20260801.md`.

## 6. Exact remaining lower-compiler requirement

Fix a terminal phase `epsilon` and a protected target-to-cell assignment.
Freeze the unaffected inherited assignments and delete every protected row
which retains a legal common or exterior alternate witness.  Let

\[
 \mathcal B^\epsilon=
 \{\text{remaining protected rows whose disappearing local witness lies in }
                  \Delta_{1-\epsilon}\}.                \tag{6.1}
\]

This is an occurrence-labelled bank: equal target masks may still be
different demands.  Let `C^epsilon` be the still-free physical compiler
cells outside the retained full-block lifts, filtered by literal deadline,
trace, residence-frontier and prescribed-common-cap legality.  Form the
guarded equality graph

\[
 b\sim c\quad\Longleftrightarrow\quad
       \operatorname{OR}(c)=\operatorname{target}(b)
       \quad\hbox{and `c` is legal for occurrence `b`.}  \tag{6.2}
\]

The frozen assignment extends exactly when this graph has a matching
saturating `B^epsilon`, equivalently

\[
                         |N(A)|\ge|A|
                  \qquad(A\subseteq\mathcal B^\epsilon). \tag{6.3}
\]

If the inherited assignments remain mobile, (6.3) must instead be imposed
on the combined inherited-plus-exposed graph.  If one fixed assignment is to
survive both phases, use the intersection of the two phase-admissibility
graphs (or an explicit joint two-phase matching); two separate Hall checks
are not sufficient.

Demanding literal preservation of the entire local deck is a stronger,
self-contained reset certificate: then `B^epsilon=Delta_(1-epsilon)`.
In general the raw deck differences do **not** lower-bound global compiler
deficiency.  What (4.5) proves is narrower and exact: the present two hosts
and letterwise refinements cannot supply those masks.  Any protected member
of that bank lacking an external/common alternate must be routed through
another admissible compiler or planted-ray cell.

Every residual bank is native when its own phase returns.  Hence a new
compiler whose cells form a constant number of exact physical rays could
still admit a native-return full reset.  The set families above show why
this is plausible, but do not prove it: the ray bases, filler order,
deadlines, common cap, simultaneous realization and contraction Hall must
all be literal.  Until (6.3) and that contraction are proved, the
`+2,Phi=2` result is only the original typed-boundary reset, not a
regenerative theorem for the full OR word.

The maximal inverse is the smaller residual interface and is therefore the
natural next compiler candidate, despite its larger phase-changing source
support.

## 7. Replay

Run

```text
python3 scratch/audit_threadD_octagon_full_source_deck_20260801.py --write
```

The audit checks `2<=d<=12`, both maximal and sharp source pairs, exact
family equality, all counts, prefix/suffix/total profiles, the contextual
decomposition on finite test contexts, and applies the exact arbitrary-block
refinement criterion (4.3).  Canonical interval witnesses are tabulated
independently in
`MATH_THEOREM_THREAD_D_OCTAGON_EXPANDED_DECK_DIFFERENCE_20260801.md`.
The audit does not construct the residual compiler.
