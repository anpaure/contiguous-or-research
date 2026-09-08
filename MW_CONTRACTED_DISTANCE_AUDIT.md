# Exact move-to-front distance on the contracted Mütze--Weber paths

## 1. Outcome

Let

\[
 W_m={2m\choose m},\qquad K_m=\operatorname{Cat}_m={W_m\over m+1}.
\]

Contract the reversed-lexical matching in the all-zero Mütze--Weber
dangling paths, as in `MW_CONTRACTED_SCD_MTF_AUDIT.md`.  This gives
`K_m` paths through all `W_m` chains of the reversed Greene--Kleitman
symmetric-chain decomposition.

Allow the strongest possible interpretation of a transition: at its two
ends one may choose *arbitrary* ordered-partition states exposing the two
chains.  Even with that freedom, two MTF updates are not enough at almost
every contracted boundary.

### Theorem 1 (the one/two-step distribution)

For `m>=3`, among the `W_m-K_m` forward contracted adjacencies,

\[
 \begin{array}{c|c}
 \text{exact exposing-fiber distance}&\text{number}\
 \hline
 1&A_m=W_m{2(m-1)\over(m+1)(m+2)},\\[2mm]
 2&K_m,\\[1mm]
 \ge3&R_m=W_m{m(m-1)\over(m+1)(m+2)}.
 \end{array}                                      \tag{1.1}
\]

In particular,

\[
 {R_m\over W_m}=1-O(1/m).                         \tag{1.2}
\]

Thus the contracted Mütze--Weber order is not a hidden average-cost-two
MTF tour.  Its transition mass, before any reset between dangling paths, is
at least

\[
 A_m+2K_m+3R_m
 =W_m{3m^2+m+2\over(m+1)(m+2)}
 =(3-o(1))W_m.                                    \tag{1.3}
\]

Equation (1.3) counts states only at their assigned contracted chains.  It
does not, by itself, exclude a new construction which proves that selected
intermediate states expose other, previously unassigned chains.  No such
charging theorem follows from the Mütze--Weber support recursion; it would
be a separate global MTF theorem.

The small exception is `m=2`, where the all-star chain is also at distance
two.  It has no asymptotic relevance.

## 2. A general exact distance theorem

The useful result is not specific to Mütze--Weber.

Let

\[
 D=(A,A\cup\{f_1\},\ldots,A\cup\{f_1,\ldots,f_g\})              \tag{2.1}
\]

be a saturated target chain, and let `C` be another chain.  Let
`F(C)` denote the full ordered-partition fiber exposing `C`.  Define

\[
 \delta(C,D)=\min\{t:\Pi\in F(C),\ \Pi'\in F(D),\
             \Pi'\text{ is obtained from }\Pi\text{ by }t
             \text{ MTF updates}\}.              \tag{2.2}
\]

For `A!=empty` and `1<=t<=g+1`, put

\[
 K_t=A\cup\{f_1,\ldots,f_{t-1}\}.                 \tag{2.3}
\]

For `A=empty` and `1<=t<=g`, put

\[
 K_t=\{f_1,\ldots,f_t\}.                          \tag{2.4}
\]

As usual, `C-K` is the quotient chain obtained by deleting `K` from every
member and suppressing repetitions.  Two quotient chains are
*cross-nested* when their union is a chain.

### Theorem 2 (prefix-erasure distance formula)

For every `t` in the ranges above,

\[
 \boxed{\delta(C,D)\le t
 \quad\Longleftrightarrow\quad
 C-K_t\text{ and }D-K_t\text{ are cross-nested}.} \tag{2.5}
\]

Consequently, the exact distance is the first target-chain prefix whose
deletion makes the two chains cross-nested.  In particular, (2.5) for
`t=1` is the quotient-chain criterion from `MTF_TRANSVERSAL.md`, and
`t=2` is obtained simply by deleting one additional target increment.

### Proof

We use two elementary facts about MTF.

First, for updates `X_1,...,X_t` in chronological order, define their
surviving parts

\[
 Y_i=X_i\setminus(X_{i+1}\cup\cdots\cup X_t).     \tag{2.6}
\]

After empty parts are suppressed, the final state begins with

\[
 Y_t,Y_{t-1},\ldots,Y_1,                          \tag{2.7}
\]

and is followed by the old state with `X_1 union ... union X_t` deleted.
A shortest update sequence has no empty surviving part.

Second, every state exposing (2.1) consists of an ordered partition of
`A`, followed by the singleton blocks

\[
 \{f_1\},\ldots,\{f_g\},                          \tag{2.8}
\]

and then an ordered partition of the complement of the top of `D`.

Suppose first that `A!=empty` and that at most `t` updates lead from a
state exposing `C` to a state exposing `D`.  In a shortest such sequence,
the surviving update blocks form an initial segment of the block list in
(2.8).  At least one of them lies in `A`: otherwise an `f_i`-block would
precede the still-unmoved `A`-blocks.  Hence at most `t-1` surviving blocks
can be target increments, and their union is contained in `K_t`.  Deleting
`K_t` from the final state therefore deletes all surviving update blocks
and leaves exactly the original state with `K_t` deleted.  Its prefix chain
contains both `C-K_t` and `D-K_t`; they are cross-nested.

If `A=empty`, the surviving blocks are an initial segment of
`{f_1},...,{f_g}` of length at most `t`.  Their union is contained in
`K_t`, and the identical deletion argument proves necessity.

Conversely, suppose the quotient chains in (2.5) are cross-nested.  Extend
their union to a maximal chain of the cube outside `K_t`.  Equivalently,
choose a singleton permutation `rho` whose prefix chain contains both
quotients.  Insert the elements of `K_t` into `rho` at positions compatible
with `C`.  This gives a singleton state `Pi` exposing `C` and satisfying
`Pi-K_t=rho`.

When `A!=empty`, apply the `t` updates

\[
 \{f_{t-1}\},\{f_{t-2}\},\ldots,\{f_1\},A.       \tag{2.9}
\]

The resulting state begins

\[
 A,\{f_1\},\ldots,\{f_{t-1}\}                   \tag{2.10}
\]

and is followed by `rho`.  Since `rho` contains `D-K_t`, this state exposes
`D`.  When `A=empty`, use instead

\[
 \{f_t\},\{f_{t-1}\},\ldots,\{f_1\}.            \tag{2.11}
\]

This proves sufficiency and (2.5).  \(\square\)

## 3. Applying the formula to the contracted paths

Write a reversed Greene--Kleitman template as

\[
 \tau=u_0*u_1*\cdots*u_{2d},                     \tag{3.1}
\]

where the `u_i` are Dyck words.  Its radius is `d`.  The number of
radius-`d` chains is

\[
 N_{m,d}=[z^{m-d}]C(z)^{2d+1}.                   \tag{3.2}
\]

The exact all-zero Mütze--Weber recursion, together with the reversed
lexical-SCD recursion quoted in their relation-to-lexical-matchings lemma,
gives the following strengthened fence table.

### Lemma 3 (two-prefix MW fence table)

Let `C->D` be a forward adjacency after contraction.

1. The radii of `C` and `D` differ by one.
2. A one-step transition exists precisely for the radius-down adjacencies
   whose target has radius one.  These are the cases already counted by
   `A_m` in `MW_CONTRACTED_SCD_MTF_AUDIT.md`.
3. A two-step but not one-step transition exists precisely for a
   radius-up adjacency from radius zero to radius one.
4. Every other adjacency fails the cross-nesting test after both the first
   and second target prefixes have been erased.

#### Proof

Carry through the Mütze--Weber induction the radius of each contracted
chain and the two Boolean fence values

\[
 q_j(C,D)=
 [\,C-K_j(D)\text{ and }D-K_j(D)
       \text{ are cross-nested}\,],\qquad j=1,2. \tag{3.3}
\]

The induction basis is the contracted path `01 -> **` in dimension two.
In each of the four literal tagged copies `00,10,01,11` in
`(ind-step1-P)`, deleting the target prefix deletes the fixed tag in the
same block on both quotient chains.  Thus the radius difference and both
fence values are inherited unchanged.

At a central splice `(new-paths)`, use the reversed lexical recursion from
the final paragraph of the proof of the relation-to-lexical-matchings
lemma: the `0` copy loses its lowermost vertex and that vertex becomes the
new lowermost vertex of the corresponding chain in the `1` copy.  The
possible new contracted joins give the exhaustive table

\[
 \begin{array}{c|c|c|c}
 r(C)&r(D)&q_1&q_2\\ \hline
 0&1&0&1\\
 2&1&1&1\\
 d-1&d\ (d\ge2)&0&0\\
 d+1&d\ (d\ge2)&0&0.
 \end{array}                                      \tag{3.4}
\]

For the first row, erasing the target minimum leaves the first target star
crossing the retained source-paired coordinate; erasing that star as well
removes the crossing.  For the second row, the first erased prefix already
contains the unique crossing coordinate.  In each of the final two rows,
there are at least two target-star fences.  Erasing the first target
increment removes at most the first fence, while the second retained paired
coordinate still lies strictly between two target-star prefixes.  Hence the
quotients are not cross-nested.  These descriptions are invariant under
the four tags and are exactly the four joins made by the five-piece central
splice.  This closes the simultaneous induction.  \(\square\)

Applying Theorem 2 with `t=1,2` to Lemma 3 proves the asserted distance
classification.

## 4. Counting radius-up and radius-down arrivals

Every non-radius-zero chain occurs once as a target.  In the contracted MW
recursion the number of radius-up arrivals at radius `d` is

\[
 U_{m,d}=[z^{m-d}]C(z)^{2d},                     \tag{4.1}
\]

and the number of radius-down arrivals is

\[
 D_{m,d}=N_{m,d}-U_{m,d}
        =[z^{m-d}]C(z)^{2d}(C(z)-1).             \tag{4.2}
\]

These identities follow simultaneously from the same four-copy recursion:
a radius-up arrival is a template with a distinguished outer gap removed,
giving `2d` Dyck factors instead of `2d+1`; all remaining templates are
radius-down arrivals.  They also telescope correctly:

\[
 \sum_{d=1}^m(U_{m,d}+D_{m,d})=W_m-K_m.          \tag{4.3}
\]

At radius one,

\[
 U_{m,1}=[z^{m-1}]C^2=K_m,                       \tag{4.4}
\]

whereas

\[
 D_{m,1}=[z^{m-1}]C(C-1)
        =[z^{m-2}]C^4=A_m.                       \tag{4.5}
\]

Lemma 3 says that (4.4) is exactly the distance-two class and (4.5) exactly
the distance-one class.  Subtracting these from all contracted boundaries
gives

\[
 \begin{aligned}
 R_m
 &=W_m-K_m-A_m-K_m\\
 &=W_m{m(m-1)\over(m+1)(m+2)},
 \end{aligned}                                   \tag{4.6}

which completes the proof of Theorem 1.

## 5. What remains potentially reusable

The support theorem is still striking: `K_m=o(W_m)` dangling paths really
do order every reversed-GK chain exactly once.  What fails is the local
state metric.  Any reuse now needs a genuinely new statement of one of the
following forms:

1. intermediate MTF states on the long transitions can be injectively
   charged to the other SCD chains they expose; or
2. the contracted order can be globally shortcut by changing the exposing
   state at many chains in a compatible way.

Pairwise existential choices do not compose automatically.  The raw MW
recursion supplies neither statement, and Theorem 1 shows that they would
have to repair a `1-o(1)` fraction of all contracted boundaries.
