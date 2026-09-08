# Independent audit: six-slot `h=5` residue envelope and head dichotomy

**Date:** 2026-08-04  
**Method:** first-principles symbolic residue-path replay; no finite
enumeration program, numerical search, remote computation, or solver.  
**Verdict:** **PASS AS CORRECTED** for the current theorem bytes.

## 1. Frozen object and correction

The audited theorem is the lineage file

`MATH_THEOREM_SIX_SLOT_H5_RESIDUE_DOMINANCE_17_FORM_AND_HEAD_DICHOTOMY_20260804.md`

with current SHA-256

`b6a98dbf45f239f68f934ac0c14318ff8f5faa6b69d78cbad7796b46ee283024`.

The submitted hash
`55898b5f5cca9e326dd7c4def0075c379c4530ee44a9929a13828358d5d65825`
advertised seventeen undominated forms.  That count was not exact.  The
four inequalities already printed in the theorem imply two direct
dominations,

\[
 4d_3\le2d_1,
 \qquad
 d_1+d_3+d_4\le d_3,
\]

and two further maximum-envelope dominations,

\[
 d_3+2d_4\le\max\{d_1,4d_4\},
 \qquad
 2d_1+d_2\le\max\{d_4,4d_1\}.
\]

The theorem was corrected from seventeen to thirteen exact envelope
forms.  Its endpoint head bounds and unique long-head chamber are
unchanged.  The filename is retained only for lineage stability.

## 2. Reduced inequalities

With `P=c_5` and

\[
 d_1=c_6-6P/5,\quad
 d_2=c_2-2P/5,\quad
 d_3=c_3-3P/5,\quad
 d_4=c_4-4P/5,
\]

maximum density at five gives `d_i<=0`.  Subtracting the matching linear
density terms from

\[
 c_4\ge2c_2,\quad c_6\ge2c_3,\quad
 c_6\ge c_2+c_4,\quad P\ge c_2+c_3
\]

gives exactly

\[
 d_4\ge2d_2,quad d_1\ge2d_3,quad
 d_1\ge d_2+d_4,quad d_2+d_3\le0.
\]

No endpoint-face assumption is used in these inequalities.

## 3. Residue-path replay

A simple path from zero to a fixed nonzero residue of `Z/5Z` has zero to
three intermediate nonzero vertices.  Listing the direct path, the three
one-intermediate paths, the six two-intermediate paths, and the six
three-intermediate paths gives sixteen ordered words per target.  After
commutative weights are identified, each target has the ten raw forms
printed in equations (2.2)--(2.5) of the theorem.  Reconstructing the
step differences modulo five reproduces every one of those lists and no
additional form.

Applying the four reduced inequalities and `d_i<=0` gives the following
exact envelopes:

\[
\begin{aligned}
 \beta_1&=\max\{d_1,4d_4\},\\
 \beta_2&=\max\{d_2,2d_1,d_3+d_4,3d_4\},\\
 \beta_3&=\max\{d_3,d_1+d_2,2d_4,3d_1\},\\
 \beta_4&=\max\{d_4,d_1+d_3,4d_1\}.
\end{aligned}
\]

For completeness, the two non-single-form reductions are exact case
splits:

* if `d_3<=2d_4`, then `d_3+2d_4<=4d_4`; otherwise
  `d_3+2d_4<=2d_3<=d_1`;
* if `d_2<=2d_1`, then `2d_1+d_2<=4d_1`; otherwise
  `2d_1+d_2<=2d_2<=d_4`.

Thus thirteen forms, not seventeen, suffice for the exact stabilized
Apéry values.

## 4. Availability audit

The realizing capacities of the thirteen envelope forms are respectively

\[
\begin{array}{c|c}
r&\text{capacities}\\ \hline
1&6,16\\
2&2,12,7,12\\
3&3,8,8,18\\
4&4,9,24.
\end{array}
\]

Each listed word has distinct intermediate residues, so each is a legal
simple path.  The only envelope form first appearing after capacity
eighteen is `4d_1`, realized by `(6,6,6,6)` at capacity twenty-four.

The redundant path `2d_1+d_2`, realized by `(6,6,2)` at capacity
fourteen, must still be retained as an alternate realization: equality
with `4d_1` can shorten the availability head even though it never changes
the stabilized maximum.  This precisely explains its appearance in the
cutoff test.

## 5. Endpoint faces and the strict long chamber

On `c_6=c_1+P`, denomination one has the same reduced residue-one weight
as denomination six.  Replacing every occurrence of the latter reduces
the largest required capacity to sixteen; the remaining capacity-sixteen
word is `(4,4,4,4)`.  Hence the correction head is exactly confined to
`m<16`.

On `c_6=c_2+c_4`,

\[
 d_1=d_2+d_4\le d_4,qquad4d_1\le d_4.
\]

On `c_6=2c_3`,

\[
 d_1=2d_3,qquad4d_1=8d_3\le3d_3=d_1+d_3.
\]

Thus the capacity-twenty-four path is never the sole maximizer on either
face, and all required maxima have a realization by capacity eighteen.
More generally the same conclusion holds whenever

\[
 4d_1\le\max\{d_4,d_1+d_3,2d_1+d_2\};
\]

the third expression is the short redundant alternate just discussed.

Finally endpoint saturation is

\[
 c_6=\max\{A,c_1+P,c_2+c_4,2c_3\}.
\]

If none of the three inert equalities holds, necessarily
`c_6=A` strictly above all three.  A head through `m=23` can then be
needed only when `4d_1` is also strictly above every short residue-four
alternative.  This is exactly chamber (4.5); the quantifiers and strict
inequalities are correct.

## 6. Scope

The corrected result is an exact structural reduction and availability
dichotomy.  It does not sign the `h=5` functional, close the remaining
six-slot branches, prove arbitrary-grid Bellman positivity, or imply an
OR-word upper bound.

