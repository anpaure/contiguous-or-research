# A cyclic common-history hinge ring with exact short-deck invariance

**Date:** 2026-08-04  
**Status:** unconditional local literal construction and zero-cost cyclic
fusion theorem.  It supplies an actual common ordered depth-`d` history,
distinct owners, exact immediate palettes, and invariance of the complete
width-at-most-`d` interval-OR deck—and in fact the entire strict-lower deck—
under a cyclic component rethread.  It
does not plant the hinges in one spanning guarded factor or preserve every
arbitrary-width exterior witness automatically.

## 0. Parameters and construction

Fix integers

\[
 d\ge1,\qquad c\ge3,\qquad r\ge d+2,
\tag{0.1}
\]

and assume the ground set has at least `r+c-1` coordinates.  Choose disjoint
sets and labels

\[
 B=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
 \qquad |B|=r-2,
\tag{0.2}
\]

with every `C_j` nonempty, and

\[
 b,a_0,a_1,\ldots,a_{c-1}\notin B
\tag{0.3}
\]

all distinct.  Indices on the `a_i` are cyclic modulo `c`.

Put

\[
 X_i=\{b,a_i\},
 \qquad
 Y_i=\{a_{i-1},a_i\},
\tag{0.4}
\]

and define the literal hinge fragment

\[
 W_i=(X_i,C_1,C_2,\ldots,C_d,Y_i).
\tag{0.5}
\]

Every source letter is nonempty.  The ordered word

\[
                         \mathcal C=(C_1,\ldots,C_d)
\tag{0.6}
\]

is the same literal order-`d` history in every fragment.

## 1. Owner and immediate-palette identities

The two length-`d+1` windows of `W_i` are

\[
 L_i=B\cup\{b,a_i\},
 \qquad
 R_i=B\cup\{a_{i-1},a_i\}.
\tag{1.1}
\]

### Theorem 1.1 (simple common-history hinge bank)

The `2c` owners `L_i,R_i` are distinct rank-`r` sets.  Every original
hinge `L_i R_i` is a Johnson edge with

\[
 I_i=L_i\cap R_i=B\cup\{a_i\},
\tag{1.2}
\]

\[
 U_i=L_i\cup R_i=B\cup\{b,a_{i-1},a_i\}.
\tag{1.3}
\]

Both immediate palettes `(I_i)_i` and `(U_i)_i` are simple.

#### Proof

Every displayed owner has `|B|+2=r` elements.  The `L_i` are distinct by
their private `a_i`; the `R_i` are distinct because the cyclic adjacent
pairs `{a_(i-1),a_i}` are distinct for `c>=3`; and no `L_i` equals an
`R_j` because `b` occurs only in the former.  Equations (1.2)--(1.3) are
literal.  Their varying label sets are respectively one cyclic singleton
and one cyclic adjacent pair together with `b`, so both palettes are
simple.  \(\square\)

The overlap of the two owner windows in every hinge is exactly the same
ordered source history `mathcal C`, not merely the same union or containment
core.

## 2. The cyclic head rethread

Replace the head used after `L_i` by `R_(i+1)`.  At source level the new
hinge fragment is

\[
 \widehat W_i=(X_i,C_1,\ldots,C_d,Y_{i+1}).
\tag{2.1}
\]

Its two owners are `L_i` and `R_(i+1)`.  They are Johnson adjacent because

\[
 L_i\cap R_{i+1}=B\cup\{a_i\}=I_i,
\tag{2.2}
\]

and their union is

\[
 L_i\cup R_{i+1}
 =B\cup\{b,a_i,a_{i+1}\}=U_{i+1}.
\tag{2.3}
\]

### Theorem 2.1 (zero current on owners and q1 palettes)

The simultaneous cyclic head rethread preserves:

1. the complete owner multiset `{L_i,R_i}`;
2. the immediate lower palette pointwise, since the new colour at role `i`
   is `I_i`; and
3. the immediate upper palette as the cyclic permutation `U_i -> U_(i+1)`.

Thus it is an exact owner/lower-q1/upper-q1 zero-current move with one
actual common literal history.

#### Proof

The tails are fixed and the heads are permuted.  Equations (2.2)--(2.3)
give the two palette statements.  \(\square\)

If the original hinge `L_i -> R_i` lies on directed factor component `i`,
remove all `c` hinges and insert the rethreaded hinges
`L_i -> R_(i+1)`.  The component successor permutation is the single cycle

\[
                         i\longmapsto i+1.
\tag{2.4}
\]

Hence the completed-hinge permutation theorem fuses the `c` components into
one without adding a source position, provided the displayed occurrences
are jointly legal under the exterior guards.

### Corollary 2.2 (unconditional owner/lower-q1 planting)

Specialize to the Middle-Levels incidence graph `ML_m`, with rank-`m`
owners, and put `r=m`.  Lift the hinge bank to the incidence edges

\[
 P_c=\{I_iL_i,I_iR_i:0\le i<c\}.
\tag{2.5}
\]

This bank has `2c` edges and maximum degree two.  Therefore, whenever

\[
                         2c\le m-2,
\tag{2.6}
\]

the small protected-factor theorem extends `P_c` to a spanning two-factor
of `ML_m`.

Moreover, inside any such completion, replace `P_c` by

\[
 \widehat P_c=\{I_iL_i,I_iR_{i+1}:0\le i<c\}.
\tag{2.7}
\]

Every lower vertex `I_i` and every owner vertex `L_i,R_i` keeps the same
degree.  Hence the rethreaded graph is again a spanning two-factor.  Thus,
for fixed `c>=3` and all sufficiently large `m`, the common-history ring is
unconditionally plantable and switchable in the exact owner/lower-q1
skeleton.

This corollary does not impose the immediate-upper palette on the arbitrary
factor completion, residence away from the protected fragment, or the
all-width/common-cap guards.

## 3. Exact invariance of every short interval

The local statement extends through arbitrary exterior bodies.  Let `P_i`
be any left context ending immediately before `X_i`, and let `Q_i` be any
right context beginning immediately after `Y_i`.  Compare the cyclic family
of old local words

\[
 P_i\,X_i\,\mathcal C\,Y_i\,Q_i
\tag{3.1}
\]

with the rethreaded family

\[
 P_i\,X_i\,\mathcal C\,Y_{i+1}\,Q_{i+1}.
\tag{3.2}
\]

Only intervals which meet the displayed hinge neighbourhood are relevant;
all intervals wholly inside a context body are unchanged.

### Theorem 3.1 (complete width-`d` deck invariance)

For every `1<=ell<=d`, the occurrence-labelled multiset of OR values of
all length-`ell` intervals in the family (3.1) is exactly the corresponding
multiset for (3.2).

The same assertion holds jointly for the union of all widths at most `d`.

#### Proof

An interval of length at most `d` cannot meet both `X_i` and `Y_i`, because
the `d` letters of `mathcal C` lie strictly between them.

An interval meeting the left side of the hinge is contained in
`P_i X_i` followed by a prefix of `mathcal C`; this entire left-side word
is unchanged role by role.  An interval meeting the right side is contained
in a suffix of `mathcal C` followed by `Y_i Q_i`.  In the rethreaded family,
the complete right-side pair `(Y_i,Q_i)` is cyclically permuted to the next
role, while the preceding suffix of `mathcal C` is identical.  Hence its OR
values are permuted.  Finally, intervals contained wholly in `mathcal C`
are unchanged.  These cases exhaust every interval of length at most `d`,
with its occurrence multiplicity, proving the claim.  \(\square\)

In particular, any strict-lower compiler whose cells have width at most
`d` transports through the cyclic rethread with **zero deletion number**:
transport its occurrence-labelled matching along the multiset bijection of
Theorem 3.1.

### Corollary 3.2 (all-width strict-lower invariance)

The occurrence-labelled multiset of **every** interval-OR value of rank
strictly below `r` is preserved by the cyclic rethread, with no restriction
on interval width.

#### Proof

The left/right/context permutation in the proof of Theorem 3.1 applies to
an interval of any width unless that interval meets both exterior screen
letters `X_i` and `Y_i`.  An interval meeting both screens contains all of
`mathcal C` and therefore contains

\[
                         B\cup X_i=L_i,
\]

which already has rank `r`.  Hence every strict-lower interval meets at
most one screen and belongs to the unchanged left bank, the cyclically
permuted right bank, the common-history bank, or an unchanged context body.
These banks give an occurrence-preserving bijection.  \(\square\)

Thus **every** strict-lower compiler matching, not only a width-`d`
normal-form matching, transports with zero deletion.

### Corollary 3.3 (the complete internal fragment deck)

For intervals wholly contained in one hinge fragment, the OR multiset is
preserved at every width, including `d+1` and `d+2`.

#### Proof

Widths at most `d` follow from Theorem 3.1 with empty contexts.  At width
`d+1`, the owner multiset is preserved by Theorem 2.1.  At width `d+2`, the
only value in `W_i` is

\[
 B\cup\{b,a_{i-1},a_i\}=U_i,
\]

while the only value in `widehat W_i` is `U_(i+1)`.  These are cyclic
permutations.  \(\square\)

### Corollary 3.4 (exact upper-damage cone)

Place the fragments in a word on a `k`-coordinate ground set and perform the
cyclic rethread.  Any old interval-OR target which is not retained through
the unchanged/permuted channel contains at least one of the rank-`r+1`
sets `U_i`.  Hence the complete possible old-target damage universe is
contained in

\[
 \mathcal A
 =\bigcup_{i=0}^{c-1}\{Z:U_i\subseteq Z\subseteq[k]\},
\tag{3.3}
\]

and therefore

\[
                         |\mathcal A|
 \le c\,2^{k-r-1}.
\tag{3.4}
\]

For the two-component fallback, replace the `U_i` by the two old upper
colours in (5.3), giving the bound `2^(k-r)`.

#### Proof

An old interval which does not traverse a changed hinge is unchanged.  If
it traverses original hinge `i`, it contains `X_i`, all of `mathcal C`, and
`Y_i`; its OR therefore contains

\[
 B\cup X_i\cup Y_i=U_i.
\]

Thus every potentially lost old value lies in one displayed upper cone.
Each rank-`r+1` base has exactly `2^(k-r-1)` supersets.  The union bound gives
(3.4).  The fallback calculation is identical with two bases.  \(\square\)

This is a localization theorem, not an upper-witness theorem: the cone is
exponentially smaller than the whole Boolean lattice near the central rank,
but it is not bounded.  A protected alternative-witness or correlated
reservoir argument is still required inside `mathcal A`.

## 4. Residence and literal-overlap accounting

Every coordinate of `B` occurs in at least one source letter `C_j` inside
the common history.  Any occurrence of a coordinate at an interior source
position belongs to `d+1` consecutive length-`d+1` owner windows.  Thus the
fragment cannot create a positive owner run shorter than `d+1`; repeated
nearby occurrences can only merge such runs into a longer one.  The same
observation applies to `b` and the `a_i` at the exterior source letters,
provided the fragment is at least `d` positions from a linear word endpoint
or is equipped with the usual clipped endpoint collar.

The old and new families use the same multiset of source letters.  Their
ordered depth-`d` overlap is literally `mathcal C` at every hinge.  Therefore
the cyclic rethread pays zero bare de Bruijn connector charge.

This statement is positive-residence only.  If the construction requires a
minimum zero-run/gap length as an additional guard, that condition belongs
to the exterior planting theorem.

## 5. Two-component bounded-damage fallback

The restriction `c>=3` is sharp for the exact cyclic adjacent-pair palette,
but two residual components still admit a common-history fusion with only a
constant complete-damage bank.

Choose four distinct labels `p,q,s,t` outside `B` and define

\[
 X_1=\{p,q\},\quad Y_1=\{p,s\},
 \qquad
 X_2=\{s,t\},\quad Y_2=\{q,t\}.
\tag{5.1}
\]

This uses `r+2` ground coordinates.

Use the two fragments `(X_i,mathcal C,Y_i)`.  Their four owners are

\[
 B+pq,\quad B+ps,\quad B+st,\quad B+qt,
\tag{5.2}
\]

and are all distinct.  The original immediate colours are

\[
 \begin{array}{c|cc}
       &\text{lower}&\text{upper}\\ \hline
 1&B+p&B+pqs\\
 2&B+t&B+qst,
 \end{array}
\tag{5.3}
\]

where `B+pqs` abbreviates `B\cup\{p,q,s\}`.

Swap the two heads.  The new edges have colours

\[
 \begin{array}{c|cc}
       &\text{lower}&\text{upper}\\ \hline
 1&B+q&B+pqt\\
 2&B+s&B+pst.
 \end{array}
\tag{5.4}
\]

Both cross pairs are Johnson edges, and the head transposition fuses two
factor components into one.  Theorem 3.1 applies unchanged: swapping the
two complete right contexts preserves the entire width-at-most-`d` deck.
The owner multiset is also unchanged.  The only target values not preserved
by the displayed local comparison are the two old lower and two old upper
immediate colours in (5.3); the full-fragment width-`d+2` values are exactly
the same two old/new upper colours and add no further casualties.

Hence, after the unchanged short deck and owner bank are removed, the
two-component fusion has at most four **local immediate-palette** casualties.
If the exterior upper guard protects every longer crossing interval, a
bounded-eviction theorem may pay those four targets once at the terminal
dimension.  No exact q1-palette or unguarded arbitrary-width claim is made
for this fallback.

## 6. Exact surviving global gate

The exact ring closes, for any fixed `c>=3`, all of the following local
rows simultaneously:

1. one actual common ordered depth-`d` history;
2. distinct rank-`r` owners and simple immediate palettes;
3. zero owner/q1 current under a cyclic completed-hinge rethread;
4. zero change in the complete width-at-most-`d` interval-OR deck and, at
   arbitrary width, in the whole strict-lower deck, including occurrence
   multiplicities and hence every transported strict-lower compiler
   matching;
5. positive residence at depth `d`; and
6. zero added source positions in the component fusion.

It does **not** prove that a spanning upper-complete carrier contains one
such fragment in each of its residual components.  Nor does Theorem 3.1
control intervals longer than `d` which enter a left body, traverse the
whole common history, and exit into the newly attached right body.  Those
are precisely the arbitrary-width upper-witness and exterior common-cap
guards.

Thus the remaining all-dimensional statement is now the following narrower
protected planting theorem:

> plant a bounded cyclic bank of the fragments (0.5), one in every residual
> factor component, so that every changed long exterior interval has a
> protected alternative witness (or bounded complete damage) and the cap
> accepts the cyclic head permutation.

Together with the forest-complement component-transversal criterion, that
statement would give the zero-cost topology row needed by an additive-
constant construction.
