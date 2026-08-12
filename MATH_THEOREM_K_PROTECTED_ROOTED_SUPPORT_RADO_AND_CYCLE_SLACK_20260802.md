# Protected rooted supports: exact Rado contraction and cycle-slack criterion

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot / weakest rooted-host clause  
**Status:** exact equivalence for the protected rooted-forest row; no
all-parameter support construction and no `PCPS`, connector, compiler, or
regeneration claim

## 0. Result

Fix the predecessor matching phase `M_0` and the sharp pivot successor
path.  The direct choice of an upper-exact rooted Catalan forest appears to
couple four resources: upper colour, lower tail, middle head, and graphic
acyclicity.  There is an exact simplification after prospective support
selection.

Let `S` be one occurrence-labelled **incidence matching support**.  Thus no
two elements of `S` use the same lower endpoint or the same middle
endpoint.  Let `F subseteq S` be a mandatory protected forest containing
the pivot successor path and any edges forced in order to keep declared
all-width witnesses inside their protected source fragments.  Then tail
and head injectivity hold for every subset of `S`.  The remaining
upper-exact extension is one independent-transversal problem in the
graphic matroid contracted by `F`.

For every family `A` of residual upper colours, let `E(A)` be all candidate
occurrences in `S-F` with colour in `A`, and let `kappa_F(A)` be the cycle
nullity of the rooted graph `F union E(A)`.  The extension exists if and
only if

\[
             |E(A)|-\kappa_F(A)\ \ge\ |A|
             \qquad\text{for every residual colour family }A.       \tag{0.1}
\]

Equivalently, occurrence surplus must pay for every rooted cycle completed
by that colour family:

\[
            |E(A)|-|A|\ \ge\ \kappa_F(A).                         \tag{0.2}
\]

This yields three useful consequences.

1. On a rooted-forest or rooted-path support, `kappa_F(A)=0`; exact upper
   completion is equivalent simply to every residual upper colour having
   an occurrence.
2. On a rooted cycle cover, (0.2) is the exact additional obstruction:
   every fully activated cycle consumes one duplicate occurrence.
3. The maximum residual number of colours that can be retained has the
   exact deficiency formula
   \[
      |\mathcal R|-\max_{A\subseteq\mathcal R}
        (|A|-|E(A)|+\kappa_F(A)).                                \tag{0.3}
   \]

The statement is compatible with the corrected physical guards.  If `S`
is bound to one literal chronology with a globally consistent address
quotient and accepted history replay, marking the subset `Q_0` does not
change that chronology.  The endpoint aperture

\[
                         o\subset s\quad\hbox{or}\quad o\subset t       \tag{0.4}
\]

and the one-credit source equation remain explicit hypotheses on the
support; they are not consequences of Rado rank.

The new `k=17` upper-`q1` trajectory illustrates both the criterion and its
scope boundary, but its augmented factor is not itself the incidence-
matching support `S` of this theorem.  Its certified three-hole count is on
the `19,412`-target necessary non-`D` row, not on the complete `19,448`-
target literal rank-10 bank.  The same carrier has `25` literal rank-10
holes: the three ordinary holes plus a fixed `22`-ticket boundary/`D` bank.
Thus any extracted fixed-`M_0`, replay-bound phase support having precisely
those absent families would have restricted Rado deficiency at least
three; the existing factor alone does not establish that premise.  A
one-hole checkpoint with missing mask `32058` now has a reported independent
replay, but is not promoted here without the authoritative frozen binding
to `S`; it still has the corresponding `22` exceptional holes.  Filling
every empty family is necessary but, on a multi-cycle support, (0.2) must
still be checked.

## 1. Rooted incidence notation

Put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal V={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},                         \tag{1.1}
\]

and

\[
 W=|\mathcal L|=|\mathcal V|,\qquad
 U=|\mathcal U|,\qquad C=W-U=\operatorname {Cat}_m.        \tag{1.2}
\]

Fix a perfect incidence matching

\[
                     M_0:\mathcal L\longrightarrow\mathcal V.          \tag{1.3}
\]

For an incidence `e=LV` outside `M_0`, define

\[
 \lambda(e):L\longrightarrow M_0^{-1}(V),\qquad
 \operatorname {up}(e)=M_0(L)\cup V.                    \tag{1.4}
\]

The map `e mapsto lambda(e)` is injective.  Moreover an incidence set `S`
is a matching precisely when its rooted arcs have distinct tails and
distinct heads.  Its underlying rooted graph therefore has indegree and
outdegree at most one; its components are directed paths and directed
cycles, with isolated rooted vertices included.

Let `P_1` be the successor phase of the sharp pivot.  Under `m>=3d+1`, the
predecessor phase extends to `M_0`, the arcs of `P_1` form one directed
path, and their upper colours are distinct.  These facts are imported from
the corrected pivot birth theorem.

## 2. Replay-bound matching supports

A **replay-bound protected support** is a tuple `(A_src,S,F)` with the
following properties.

1. `A_src` is one literal source chronology with one global address
   quotient.
   Every letter, cap, pin, and history state assigned to a common address
   agrees, including addresses identified across nonadjacent short
   components.
2. Its complete owner-coordinate history replay is accepting at the stated
   depth.  Every declared all-width upper witness and lower/compiler pin is
   an occurrence in `A_src`.
3. `S` is an occurrence-labelled incidence matching outside `M_0`, read
   from one fixed phase of `A_src`.
4. `F subseteq S` is a rooted forest, its upper colours are pairwise
   distinct, and `P_1 subseteq F`.
5. Every declared witness that must remain internal to a protected
   component has its required transition segment contained in `F`.
6. If `A_src` is obtained from an unrooted path certificate, its omitted
   root `o` satisfies (0.4) for the intended endpoint.  If it is a
   one-credit literal composition, its exact aperture charge is
   \[
                  \sum_i g_i+\sum_i(d-o_i)=1.             \tag{2.1}
   \]

Items 1--2 and 6 are physical guards, not matroid rows.  They are included
so that the theorem cannot silently reintroduce pairwise-only overlap or
the invalid unrooted endpoint implication.  The operation below only marks
some already present incidences; it does not rethread `A_src`.  Hence all
these guards survive unchanged.

The mandatory bank `F` may be just `P_1`.  It may also include a larger
witness-closure bank.  The only load-bearing restrictions for the Rado
step are that `F` is graphic-independent and upper-colour-injective.

Write

\[
 \mathcal U_F=\operatorname {up}(F),\qquad
 \mathcal R=\mathcal U\setminus\mathcal U_F.             \tag{2.2}
\]

For `R in \mathcal R`, define the occurrence family

\[
       E_R=\{e\in S-F:\operatorname {up}(e)=R\},\qquad
       E(A)=\bigcup_{R\in A}E_R.                         \tag{2.3}
\]

Occurrences of a colour already represented by `F` are deliberately not
eligible: selecting one would repeat an upper colour.

## 3. Exact protected Rado theorem

Let `M_gr` be the graphic matroid of the rooted multigraph on vertex set
`\mathcal L` and edge occurrences `\lambda(S)`.  Parallel opposite arcs
are retained as distinct graphic elements.  Since `\lambda(F)` is
independent, the contraction `M_gr/\lambda(F)` is defined.

### Theorem 3.1 (protected rooted-support Rado criterion)

For a replay-bound protected support `(A_src,S,F)`, the following are
equivalent.

1. There is a set `Q_0` with
   \[
                 F\subseteq Q_0\subseteq S                 \tag{3.1}
   \]
   such that `up:Q_0 -> \mathcal U` is a bijection and
   `\lambda(Q_0)` is a forest.
2. The residual occurrence families `(\lambda(E_R):R in \mathcal R)` have
   an independent transversal in `M_gr/\lambda(F)`.
3. For every `A subseteq \mathcal R`,
   \[
       r_{M_{\rm gr}/\lambda(F)}(\lambda(E(A)))\ge |A|.     \tag{3.2}
   \]
4. For every `A subseteq \mathcal R`,
   \[
                         |E(A)|-\kappa_F(A)\ge |A|,          \tag{3.3}
   \]
   where
   \[
      \kappa_F(A)=|F|+|E(A)|-r_{M_{\rm gr}}
                              (\lambda(F\cup E(A)))          \tag{3.4}
   \]
   is the cycle nullity of the rooted graph `F union E(A)`.
5. For every `A subseteq \mathcal R`,
   \[
      c\bigl(\lambda(F\cup E(A))\bigr)
          \le W-|F|-|A|,                                  \tag{3.4a}
   \]
   where `c` counts rooted connected components including isolated
   vertices.

Every resulting `Q_0` is an upper-exact rooted Catalan forest with exactly
`C` directed-path components and contains the complete protected pivot
path.  Its selection preserves the replay, global-address, history,
witness, endpoint-aperture, and source-charge certificates attached to
`(A_src,S,F)`.

#### Proof

Because `S` is an incidence matching, every subset of `S` has distinct
rooted tails and heads.  Thus tail and head capacity require no further
selection constraint.

After the forced independent set `lambda(F)` is contracted, choosing one
occurrence for each residual upper colour and requiring their union with
`F` to remain a forest is exactly an independent transversal of the
families in Item 2.  Rado's independent-transversal theorem makes Items 2
and 3 equivalent.

For every `A`, graphic contraction gives

\[
\begin{aligned}
 r_{M_{\rm gr}/\lambda(F)}(\lambda(E(A)))
  &=r_{M_{\rm gr}}(\lambda(F\cup E(A)))-r_{M_{\rm gr}}(\lambda(F))\\
  &=r_{M_{\rm gr}}(\lambda(F\cup E(A)))-|F|\\
  &=|E(A)|-\kappa_F(A),                                  \tag{3.5}
\end{aligned}
\]

which proves the equivalence with Item 4.

The graphic rank identity

\[
 r_{M_{\rm gr}}(\lambda(F\cup E(A)))
      =W-c\bigl(\lambda(F\cup E(A))\bigr)                 \tag{3.5a}
\]

turns (3.2) into (3.4a), proving Item 5 equivalent as well.

An independent transversal together with `F` has

\[
                      |F|+|\mathcal R|=U                  \tag{3.6}
\]

edges, represents every upper colour exactly once, and is a subset of the
incidence matching `S`.  It is therefore a rooted linear forest on all `W`
rooted vertices.  Its component number is

\[
                           W-U=C.                         \tag{3.7}
\]

It contains `P_1 subseteq F`.  Conversely, the residual edges of any set in
Item 1 form the required independent transversal.  Finally, selecting
`Q_0` only marks occurrences already present in `A_src`; it identifies no
new addresses and changes no source letter or chronology.  All replay-bound
certificates therefore remain valid.  Required witness segments contained
in `F` remain within one component because adding forest edges can merge
components but cannot split an `F`-component.  \(\square\)

The same equivalence applies verbatim to any explicitly specified subset
of upper tasks after replacing `\mathcal U` by that task shore.  Only the
component count (3.7) then changes from `W-U` to `W-|\mathcal U'|`.  Such a
restricted application must not be described as a full upper-exact
Catalan forest.

### Corollary 3.2 (exact deficiency)

Put

\[
 \delta_F(S)=\max_{A\subseteq\mathcal R}
       \bigl(|A|-|E(A)|+\kappa_F(A)\bigr).              \tag{3.8}
\]

Then the maximum number of residual upper colours that can be represented
by a rooted forest containing `F` equals

\[
                         |\mathcal R|-\delta_F(S).       \tag{3.9}
\]

In particular the protected upper-exact forest exists exactly when
`delta_F(S)=0`.

#### Proof

The deficiency form of Rado's theorem says that the maximum independent
partial transversal of families indexed by `\mathcal R` has size

\[
 \min_{A\subseteq\mathcal R}
 \left(|\mathcal R\setminus A|+
 r_{M_{\rm gr}/\lambda(F)}(\lambda(E(A)))\right).       \tag{3.10}
\]

Insert (3.5) and rearrange. \(\square\)

## 4. Path, forest, and cycle-cover normal forms

Because `S` is an incidence matching, every rooted component is a path or
a cycle.  Thus `kappa_F(A)` is literally the number of rooted cycle
components completed by `F union E(A)`.

### Corollary 4.1 (forest-support collapse)

If the whole rooted support `lambda(S)` is a forest, then a protected
upper-exact `Q_0` exists if and only if

\[
                         E_R\ne\varnothing
                         \qquad(R\in\mathcal R).         \tag{4.1}
\]

#### Proof

Every subset of a forest has zero nullity.  Since the colour families are
pairwise disjoint, (4.1) gives
`|E(A)|=sum_(R in A)|E_R|>=|A|` for every `A`.  Conversely an empty family
cannot be represented. \(\square\)

This is an exact support-first target weaker than a Hamilton scaffold:
construct any replay-bound, rooted-acyclic incidence matching support
containing the pivot and meeting every upper colour.  The Catalan forest
then costs no further integral theorem.  Existentially this target is
equivalent to the protected rooted-forest row, since a completed `Q_0`
itself may be used as `S`.

### Corollary 4.2 (cycle-slack Hall form)

For an arbitrary incidence matching support, the exact inequalities are

\[
 \boxed{\quad
   \sum_{R\in A}(|E_R|-1)\ \ge\ \kappa_F(A)
   \quad(A\subseteq\mathcal R).\quad}                  \tag{4.2}
\]

Thus duplicates are not merely global scalar slack.  They must lie in the
same colour families that activate the rooted cycles they are needed to
break.

### Corollary 4.3 (one Hamilton cycle)

Suppose `lambda(S)` is one spanning rooted cycle and `F` is a proper
subforest.  Then (4.1) is again necessary and sufficient.

#### Proof

For a proper subset of the cycle, `kappa_F(A)=0`, and colour availability
gives (3.3).  If `F union E(A)` is the full cycle, every non-`F` edge is an
eligible residual occurrence.  In particular there is no ignored
non-`F` occurrence of a colour already represented by `F`; and colour
availability forces `A=\mathcal R`.  Hence

\[
 |E(A)|=W-|F|,\qquad |A|=U-|F|,\qquad
 |E(A)|-|A|=W-U=C\ge1=\kappa_F(A).                    \tag{4.3}
\]

So the sole possible cycle penalty is automatically paid by Catalan
surplus. \(\square\)

Corollary 4.3 recovers the born-connector upper-representative step without
assuming in advance which occurrence represents each colour.  It does not
open the cycle physically or protect long windows at a cut.

## 5. Relation to `PCPS(m,d)` and the `k=17` trajectory

Define `PRS(m,d)` to be the existence of a replay-bound protected support
`(A_src,S,F)` satisfying (3.3).  Theorem 3.1 proves the exact equivalence

\[
 \boxed{\quad
   PRS(m,d)
   \iff
   \exists(A_{\rm src},Q_0,F)\ \text{satisfying the replay-bound guards
   and Item 1 of Theorem 3.1}.\quad}                    \tag{5.1}
\]

The implication from right to left keeps the quantified chronology
`A_src`, uses `S=Q_0`, and takes `F` to be the declared protected closure
bank.  An abstract `Q_0` without such a chronology cannot manufacture the
replay/history certificate.  Thus (5.1) is an exact smaller Hall/matroid
statement for the first missing clause on the replay-bound face, not merely
a sufficient condition.

It does **not** prove `PCPS(m,d)`.  After `Q_0` is marked, one still needs:

1. a globally consistent full-`d`-overlap Hamilton ordering of its `C`
   component states;
2. accepted aggregate boundary histories and the one-credit aperture
   equation;
3. an all-width exterior occurrence ledger under that ordering and its
   final opening;
4. the terminal common-cap/two-ray compiler state; and
5. regeneration of the next prepared cut.

Those are `GOP/PHWC`, `CAP`, and regeneration rows, not hidden consequences
of (3.3).

For any literally replayed support with a set `H` of absent upper colours,
take `A=H` in (3.8).  Then `E(A)` is empty and

\[
                            \delta_F(S)\ge |H|.          \tag{5.2}
\]

The independently certified `k=17` three-hole augmented factor is not by
itself a matching support `S` in Theorem 3.1.  Conditional on extracting a
fixed-`M_0`, replay-bound phase support whose absent families are exactly
those holes, (5.2) gives restricted deficiency at least three, and the same
lower bound survives any compatible protected contraction.  The restricted
shore has size `19,412`, so its forest component count would be
`24,310-19,412=4,898`, not the Catalan count `4,862` for the full `19,448`
shore.  Literal replay has `25` rank-10 holes.  The one-hole checkpoint with
mask `32058` has a reported independent replay, but no authoritative
fixed-support promotion is made here; it retains `22` literal boundary/`D`
holes.  After a repair gives every full-shore colour an occurrence, a
multi-cycle support must still pass all cycle-slack inequalities (4.2).

## 6. Exact remaining constructive statement

The protected rooted-forest clause can now be attacked without a four-way
selector:

> **Protected replay-support lemma.**  For `m>=3d+1`, construct one
> replay-bound incidence matching support containing the pivot/witness
> closure bank and satisfying the cycle-slack inequalities (4.2).

The cleanest sufficient face makes the rooted support a forest, when the
only remaining upper row is occurrence availability (4.1).  The next most
general face is a cycle cover with duplicates satisfying (4.2).

What remains genuinely correlated in constructing that support is the
choice of one physical matching phase together with its literal source
antecedent.  This theorem does not claim that an abstract `q1` factor has
such an antecedent, that an Ore/LKK marginal factor satisfies (4.2), or that
the selected Catalan components admit the required global connector order.
